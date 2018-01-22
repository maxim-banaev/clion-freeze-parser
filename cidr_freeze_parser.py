#!/usr/bin/env python3
import os
import sys
from collections import defaultdict
from typing import List

from dump_file import parse_dump_file
from rules import process_custom

import freeze_rules

FRAME_SEQ_TO_TICKET = \
    freeze_rules.actions.get_rules() + \
    freeze_rules.commit.get_rules() + \
    freeze_rules.lazyReparse.get_rules() + \
    freeze_rules.misc.get_rules() + \
    freeze_rules.resolve.get_rules() + \
    freeze_rules.tests.get_rules()


def print_usage():
    print("Usage: {} [thread dumps file]".format(os.path.basename(__file__)))


def extract_edt_call_stack(lines):
    res = []
    in_edt = False
    before_ats = True
    for l in lines:
        if not in_edt:
            if "AWT-EventQueue" in l:
                in_edt = True
        else:
            if l.startswith("\tat "):
                before_ats = False
                res.append(l)
            elif not before_ats:
                if not l.strip():
                    break

    return res


def match_stack(stack):
    if stack is not None:
        custom = process_custom(stack)
        if custom is not None:
            return {custom}
        messages = set()
        for rule in FRAME_SEQ_TO_TICKET:
            message = rule.is_matched(stack)
            if message:
                messages.add(message)
        return messages
    else:
        return set()


class ThreadDumpInfo:
    def __init__(self, file_name, messages, lines):
        self.file_name = file_name
        self.messages = messages
        self.lines = lines


def process_thread_dump(file_name, lines: List[str]):
    stack = extract_edt_call_stack(lines)
    dump_info = parse_dump_file(lines)
    messages = match_stack(dump_info)
    return ThreadDumpInfo(file_name, messages, stack)


def process_file(file_name):
    with open(file_name) as f:
        try:
            readlines = f.readlines()
        except (IOError, UnicodeError):
            readlines = []  # will be reported as "UNKNOWN"
        return process_thread_dump(file_name, readlines)


def get_summary(infos):
    all_tickets = defaultdict(int)
    detailed = []
    unknown = []
    for info in infos:
        if not info.messages:
            unknown.append(info.file_name)
        detailed.append(
            info.file_name + ": " + (", ".join(info.messages) if info.messages else "UNKNOWN") +
            "\n" +
            ("" if info.messages else ("\n" + "".join(info.lines) + "\n"))
        )
        for t in info.messages:
            all_tickets[t] += 1

    return "All found tickets:\n{}\nUnknown traces ({}):\n{}\n\n{}".format(
        tickets_to_string(all_tickets),
        len(unknown),
        "\n".join(unknown),
        "".join(detailed))


def tickets_to_string(all_tickets):
    return "\n".join(
        "   {}: {}".format(t, u) for t, u in sorted(all_tickets.items(), key=lambda k: (k[1], k[0]), reverse=True))


def collect_files(arg):
    if os.path.isfile(arg):
        if not os.path.basename(arg).startswith("."):
            yield arg
    elif os.path.isdir(arg):
        for folder_name, subfolders, filenames in os.walk(arg):
            if ".git" in folder_name:
                continue

            if filenames and 'threadDumps-freeze-20' in folder_name:
                # assume all freezes in this folder have the same cause
                yield folder_name + '/' + filenames[0]
            else:
                for file in filenames:
                    if not os.path.basename(file).startswith("."):
                        yield folder_name + '/' + file
    else:
        raise ValueError("Invalid file or folder: " + str(arg))


def parse_args_and_process_files(args):
    files = [f for arg in args for f in collect_files(arg)]
    return get_summary(process_file(f) for f in files)


def main():
    if len(sys.argv) < 2:
        print_usage()
    else:
        print(parse_args_and_process_files(sys.argv[1:]))


if __name__ == '__main__':
    main()
