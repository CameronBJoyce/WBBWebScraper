from Event import Event


class Player:
    def __init__(self, name, number):
        self.name = name  # String
        self.number = number  # Integer
        self.total_points = 0
        self.points = 0  # Integer
        self.events = []  # List of Events
        self.fouls = 0  # Integer

    def add_event(self, event_info):
        new_event = Event(event_info)
        self.events.append(new_event)
