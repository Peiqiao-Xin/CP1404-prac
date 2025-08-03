class Band:
    """A group of musicians."""

    def __init__(self, name, members):
        """
        name:  str
        members: list of Musician (or subclass) instances
        """
        self.name = name
        self.members = members

    def __str__(self):
        mems = ", ".join(str(m) for m in self.members)
        return f"{self.name} ({mems})"

    def play(self):
        for m in self.members:
            m.play()