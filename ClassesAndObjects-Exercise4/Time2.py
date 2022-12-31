class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set_time(self, hours, minute, seconds):
        self.hours = hours
        self.minutes = minute
        self.seconds = seconds

    def get_time(self):
        return f"{self.format_clock(self.hours)}:{self.format_clock(self.minutes)}:{self.format_clock(self.seconds)}"

    def format_clock(self, number):
        if number < 10:
            return f"0{number}"
        return f"{number}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()