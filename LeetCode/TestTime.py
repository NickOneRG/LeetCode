from time import perf_counter
import memory_profiler

class TimeSet:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        print(self.__class__.__name__)
        return """ Dasturning ishlash vaqtini hisoblovchi dastur"""

    def hisobla(self, start: int = 0, x: int = 0) -> str:
        """ Dasturning ishlash vaqtini hisoblovchi dastur"""
        self.start = start
        self.x = x
        match self.x:
            case 0:
                return perf_counter()

            case 1:
                self.end = perf_counter()
                return f'Execution time: {(self.end - self.start)*1000:.2f} ms  { (self.end - self.start):.5f} s'
    def rav(self):
        return (self.end - self.start)*1000
    
if __name__ == '__main__':
    m = TimeSet()

print(m)