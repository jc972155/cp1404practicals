"""
CP1404 Practical
Band class
"""


class Band:
    """Band Class"""

    def __init__(self, name=''):
        """Initialise a band with a name and empty member list"""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""

        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string representation of a Band, showing variables."""
        return str(vars(self))

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Print each member of the band and the instrument they play."""
        format_members = []
        for member in self.members:
            format_members.append(member.play())
        return '\n'.join(format_members)
