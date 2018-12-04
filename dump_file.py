from collections import namedtuple

STATE_PREFIX = "java.lang.Thread.State: "

ThreadInfo = namedtuple('ThreadInfo', 'frames is_edt thread_state')
DumpFileInfo = namedtuple('DumpFileInfo', 'thread_infos')


def get_info(self):
    return next((i for i in self.thread_infos if i.is_edt), None)


setattr(DumpFileInfo, 'get_edt_info', get_info)


def split_into_threads(lines):
    """
    :type lines: list(str)
    :param lines:
    :return: list(list(str))
    """
    start_indices = [i - 1 for i, s in enumerate(lines) if STATE_PREFIX in s]
    start_indices.append(len(lines))
    if len(start_indices) < 2:
        return []
    return [lines[begin:end] for begin, end in zip(start_indices[:-1], start_indices[1:])]


def parse_thread_info(thread):
    """
    :type thread: list(str)
    :param thread: processed thread
    :return: Optional(ThreadInfo)
    """
    if len(thread) <= 3 or STATE_PREFIX not in thread[1]:
        return None

    is_edt = "AWT-EventQueue" in thread[0]
    thread_state = thread[1].strip().replace(STATE_PREFIX, "")
    return ThreadInfo(thread, is_edt, thread_state)


def parse_dump_file(lines):
    """
    :type lines: list(str)
    :param lines:
    :return: Optional(DumpFileInfo)
    """
    infos = [info for info in (parse_thread_info(thread) for thread in split_into_threads(lines)) if info is not None]
    return DumpFileInfo(infos) or None
