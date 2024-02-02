from time import perf_counter
import memory_profiler

class TimeSet:
    """
    A class used to measure the execution time of a program.
    """
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        """
        Returns the docstring of the hisobla method when the object is printed.
        """
        print(self.__class__.__name__)
        return self.hisobla.__doc__

    def hisobla(self, start: int = 0, x: int = 0) -> str:
        """
        Measures the execution time of a program.

        Parameters:
            start (int): The start time of the program execution.
            x (int): A flag to start or stop the timer.

        Returns:
            str: The execution time if x is 1, otherwise starts the timer.
        """
        self.start = start
        self.x = x
        match self.x:
            case 0:
                return perf_counter()

            case 1:
                self.end = perf_counter()
                return f'Execution time: {(self.end - self.start)*1000:.2f} ms  { (self.end - self.start):.5f} s'
    def rav(self):
        """
        Returns the execution time in milliseconds.
        """
        return (self.end - self.start)*1000
    
if __name__ == '__main__':
    m = TimeSet()

    print(m)


