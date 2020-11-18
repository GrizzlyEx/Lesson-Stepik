class MoneyBox:
    def __init__(self, cepacity):
        self.score = score = 0
        self.cepacity = cepacity

    def can_add(self, v):
        if self.cepacity >= self.score + v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.score += v
