# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Ex1 import Ex1

import json
import csv


from Elevators import Elevator
from Call import Call

root1 = "Ex1_input/Ex1_Buildings/B3.json"
root2 = "Ex1_input/Ex1_Calls/Calls_a.csv"


if __name__ == '__main__':
    # elevators = {}
    calls = []
    rows = []



    ex = Ex1(calls, rows)
    # ex.assign_ele()
    # ex.random()

    #load json file
    try:
        with open(root1, "r") as f:
            new_e = {}
            my_d = json.load(f)
            ele_d = my_d["_elevators"]

            for item in ele_d:
                e = Elevator(id=item["_id"],speed=item["_speed"],minFloor=item["_minFloor"],maxFloor=item["_maxFloor"],closeTime=item["_closeTime"],openTime=item["_openTime"],startTime=item["_startTime"],stopTime=item["_stopTime"])
                new_e[e._id] = e

            ex.elevators = new_e

    except IOError as e:
        print(e)



    # for i in elevators.items():
    #     print(i[1].__dict__)

    #load csv file
    with open(root2, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            call_temp = Call(elevator_call=row[0], start_time=row[1], src=row[2], dest=row[3], state=row[4], elevator=int(row[5]))
            ex.calls.append(call_temp)  # arrlist of all the calls
            ex.rows.append(row)

    # for i in rows:
    #     print(i.__dict__)



    # print(calls)
    # print(rows)
    print("dfwfvw")






    ex.assign_ele(ex.rows)

    print(ex.rows)

    new_rows = []
    for i in ex.rows:
        new_rows.append(i)
    # print(new_calls)
    with open("mycsv.csv", 'w', newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerows(new_rows)
