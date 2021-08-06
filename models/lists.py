class Lists:

    def __init__(self):
        self._deadlocks = []
        self._solutions = []
        self._distances = []

    @property
    def deadlocks(self):
        return self._deadlocks

    @property
    def solutions(self):
        return self._solutions

    @property
    def distances(self):
        return self._distances
