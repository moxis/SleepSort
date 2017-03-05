import sys
import threading
import time
import numpy

class SleepSort:

    def __init__(self, values, speed=1):
        self.values = values
        self.converted_values = []

        for x in self.values:
            if type(x) is str:
                self.converted_values.append(self.convert_to_ascii(x))
            else:
                self.converted_values.append(x)
        self.max = max(self.converted_values) * speed
        self.result = []

    def convert_to_ascii(self, x):
        ascii_values = []
        for letter in str(x):
            ascii_values.append(str(ord(letter)))

        return int(''.join(ascii_values))

    def sleep(self, x):
        time.sleep(x / self.max)
        self.result.append(self.values[self.converted_values.index(x)])

    def sort(self):
        threads = []
        for x in self.converted_values:
            thread = threading.Thread(target=self.sleep, args=(x,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return self.result


if __name__ == '__main__':
    random_array = numpy.random.randint(low=1, high=100, size=20)
    correct = sorted(random_array)
    result = SleepSort(random_array).sort()
    if result == correct:
        print("The array was sleep sorted succesfully!")
    else:
        print("Dumb program!")
    print(result)
