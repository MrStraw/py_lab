class Lists:

    def __init__(self):
        self._deadlocks = set()
        self._solutions = set()
        self._distances = set()

    @property
    def deadlocks(self):
        return self._deadlocks

    @property
    def solutions(self):
        return self._solutions

    @property
    def distances(self):
        return self._distances
