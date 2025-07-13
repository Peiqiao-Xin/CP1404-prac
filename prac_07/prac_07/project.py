from datetime import datetime

class Project:
    """Represent a project with attributes and comparison methods."""

    def __init__(self, name, start_date, priority, cost, completion):
        """
        :param name: project name (string)
        :param start_date: 'dd/mm/YYYY' or datetime.date
        :param priority: integer priority
        :param cost: float cost estimate
        :param completion: int percent complete (0–100)
        """
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.name = name
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def __str__(self):
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority (lower first)."""
        return self.priority < other.priority

    def is_completed(self):
        return self.completion >= 100

    def update(self, new_completion=None, new_priority=None):
        """Update completion percentage and/or priority if provided."""
        if new_completion is not None:
            self.completion = int(new_completion)
        if new_priority is not None:
            self.priority = int(new_priority)