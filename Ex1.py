from Elevators import Elevator


class Ex1:

    def __init__(self, calls, rows):
        self.elevators = {}

        self.calls = calls
        self.rows = rows

    def faster_elev(self):
        fast = 0
        ans = Elevator
        for e in self.elevators.items():
            if e[1]._speed > fast:
                fast = e[1]._speed
                ans = e
        print(ans)
        return ans[0]
    # faster_elev()