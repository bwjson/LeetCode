class Squares:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration
        
sqrs = Squares(10)

for sqr in sqrs:
    print(sqr, end=" ")

