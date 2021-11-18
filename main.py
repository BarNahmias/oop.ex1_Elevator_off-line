# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Ex1 import Ex1

import json
import csv


from Elevators import Elevator
from Call import Call

root1 = "Ex1_input/Ex1_Buildings/B5.json"
root2 = "Ex1_input/Ex1_Calls/Calls_d.csv"


if __name__ == '__main__':

    calls = []
    rows = []

    ex = Ex1(calls, rows)

    #load json file
    try:
        with open(root1, "r") as f:
            new_e = {}
            my_d = json.load(f)
            ele_d = my_d["_elevators"]

            c = 0
            for item in ele_d:

                e = Elevator(id=item["_id"],speed=int(item["_speed"]),minFloor=item["_minFloor"],maxFloor=item["_maxFloor"],closeTime=item["_closeTime"],openTime=item["_openTime"],startTime=item["_startTime"],stopTime=item["_stopTime"])
                new_e[c] = e
                c += 1
            ex.elevators = new_e

    except IOError as e:
        print(e)


    #load csv file
    with open(root2, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            call_temp = Call(elevator_call=row[0], start_time=float(row[1]), src=row[2], dest=row[3], state=row[4], elevator=int(row[5]))
            ex.calls.append(call_temp)  # arrlist of all the calls
            ex.rows.append(row)


    def faster_elev():
        fast = 0
        ans = Elevator
        for e in ex.elevators.items():
            if e[1]._speed > fast:
                fast = e[1]._speed
                ans = e
        return ans[0]


    def call_to_elev():
        num_of_elevators = len(ex.elevators) - 1
        startTime = int(float(ex.rows[0][1]))
        lastTime = int(float(ex.rows[len(ex.rows) - 1][1]))
        total_time = int(abs(startTime - lastTime))

        fast = faster_elev()


        e = 0
        p = int(total_time / len(ex.rows))
        i = 1
        for row in rows:
            seg = i * p * 5 + startTime
            r1 = float(row[1])  #start time
            r2 = float(row[2])  #src
            r3 = float(row[3])  #dest

            if(r1 >= seg):
                i += 1
                seg = i * p * 5 + startTime

            if (startTime <= r1) & (r1 <= seg) & (r2 - r3 < 0):
                row[5] = e

            elif (startTime <= r1) & (r1 <= seg) & (r2 - r3 > 0):
                row[5] = e

            if (len(ex.elevators) == 1):
                row[5] = e
            e = e + 1

            if (e  >= num_of_elevators):
                e = 0

        for row in rows:
            if(row[5] == "-1"):
                row[5] = 1


    call_to_elev()


    new_rows = []
    for i in ex.rows:
        new_rows.append(i)

    with open("out.csv", 'w', newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerows(new_rows)
