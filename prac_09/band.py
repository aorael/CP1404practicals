class Band:
    """Band class"""
    def __init__(self, name=""):
        """intializes instance variables of Band"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """return a string of Band """
        musician_names = ", ".join(str(musician) for musician in self.musicians) # breaks the list of musicians w instruments into a string
        return f"{self.name} ({musician_names})"

    def __repr__(self):
        """display string represent Band"""
        return str(vars(self))

    def add(self, musician):
        """add musicians with instruments"""
        self.musicians.append(musician) # state the musician, add & store instruments to musician, add musicians if there is any new musicians

    def play(self):
        results = [] # if the result of the condition is to print, it'll return None at the end, storing it in a list would make use of returning it at the end of the method
        for musician in self.musicians:
            if not musician.instruments:
                results.append(f"{musician.name} needs an instrument!")
            else:
                results.append(f"{musician.name} is playing: {musician.instruments[0]}")
        return '\n'.join(result for result in results)