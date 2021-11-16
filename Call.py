
class Call:

    def __init__(self, elevator_call = "", start_time=0, src=0, dest=0, state=0, elevator=-1):
        self.elevator_call = elevator_call
        self.start_time = start_time
        self.src = src
        self.dest = dest
        self.state = state
        self.elevator = elevator


    def __str__(self) -> str:
        return f"src: {self.src} rank: {self.elevator}"

    def __repr__(self) -> str:
        return f"src: {self.src} elevator: {self.elevator}"