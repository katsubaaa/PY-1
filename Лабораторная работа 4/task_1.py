import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as input_file:
        data = json.load(input_file)
        list_of_values = [item["score"] * item["weight"] for item in data]
    return round(sum(list_of_values), 3)


print(task())
