import json

root1 = "Ex1_input/Ex1_Buildings/B1.json"

class Building:

    def __init__(self) -> None:
        self._maxFloors = 0
        self._minFloor = 0

    def load_json(self, root1):
        try:
            with open(root1, "r+") as f:
                my_d = json.load(f)
                self._maxFloors = my_d["_maxFloor"]
                self._minFloor = my_d["_minFloor"]
        except IOError as e:
            print(e)
          
