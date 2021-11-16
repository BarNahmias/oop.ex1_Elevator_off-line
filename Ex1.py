
import random

root1 = "Ex1_input/Ex1_Buildings/B1.json"
root2 = "Ex1_input/Ex1_Calls/Calls_a.csv"

class Ex1:

    def __init__(self, calls, rows):
        self.elevators = {}

        self.calls = calls
        self.rows = rows

    def my_random(self):
        l = len(self.elevators)-1
        r = random.randint(0, l)
        return r



    def assign_ele(self,rows):
        for row in self.rows:

            r = self.my_random()
            row[5] = r
            print(row[5])
            print(row)
