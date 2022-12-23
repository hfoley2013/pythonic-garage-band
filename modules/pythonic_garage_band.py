# Use Python classes to model a Band made up of different kinds of musicians.
# Start with Guitarist,Bassist, and Drummer.
# Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

class Band:
    """
    Creates a Band class that accepts the name of a band and band members.
    """
    def __init__(self, name, members):
        self.name = name
        self.members = members or []

    def play_solos(self):
        return [member.play_solo() for member in self.members]

class Musician:
    """
    Musician class is the parent class for all instances of musicians (Guitarist, Bassist, and Drummer).
    """
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

class Guitarist(Musician):
    """
    Guitarist creates an instance of a guitarist given a name.
    """
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo")

class Bassist(Musician):
    """
    Bassist creates an instance of a guitarist given a name.
    """
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom")

class Drummer(Musician):
    """
    Drummer creates an instance of a guitarist given a name.
    """
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash")
