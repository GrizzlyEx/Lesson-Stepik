class Buffer:
    def __init__(self):
        self.list_ = []

    def add(self, *a):
        for num in list(a):
            self.list_.append(num)
            if len(self.list_) == 5:
                print(sum(self.list_))
                self.list_.clear()

    def get_current_part(self):
        return self.list_
