from time import perf_counter
import memory_profiler

class TimeSet:
    def __init__(self) -> None:
        pass

    def hisobla(self, start = 0, x = 0):
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