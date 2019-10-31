vehicle_list ={
    "SX1234A": {
        "owner_name": "Ben",
        "reg_date": "27/6/2019"
    },
    "ST4211Z": {
        "owner_name": "Jonathan",
        "reg_date": "28/6/2019"
    }
}
#  ----
vehicle_list1 = {
    "SX1234A": ["Ben", "27/6/2019"],
    "ST4211Z": ["Jonathan", "28/6/2019"]
}
#  ----
vehicle_list2 = [
    {
        "owner_name": "Ben",
        "reg_date": "27/6/2019",
        "reg_number": "SX1234A"
    },
    {
        "owner_name": "Jonathan",
        "reg_date": "28/6/2019",
        "reg_number": "ST4211Z"
    }
]
for vehicle in vehicle_list2:
    if vehicle["reg_number"] == "ST4211Z":
        print(vehicle["reg_date"])
