import datetime
from event import Event
from threading import Timer


class Scheduler:
    events = {}

    def __init__(self):
        pass

    def add_event_once(self, event_name, event_time_start, event_time_end, func, fargs):
        self.events[event_name] = Timer(function=func, args=fargs)

    def add_event_repeat(self):
        self.events.append(Event(repeat=True))

    def get_event_time_left(self, event: Event) -> datetime.time:
        pass

    def cancel_event(self, event: Event):