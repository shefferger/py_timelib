import datetime
from threading import Timer


class Event:
    def __init__(self, name, exec_func, start_time=None, end_time=None, start_after_init=True, repeat_x_times=1, *f_args):
        self.name = name
        self.exec_func = exec_func
        self.start_time = start_time
        self.end_time = end_time
        self.start_after_init = start_after_init
        self.repeat_x_times = repeat_x_times
        self.f_args = zip(f_args)
        self.timer = Timer(interval=self.get_time_diff(), function=exec_func, args=zip(*f_args))

    def get_time_diff(self) -> float:
        return 1.0

    def start_timer(self):
        pass

    def stop_timer(self):
        pass