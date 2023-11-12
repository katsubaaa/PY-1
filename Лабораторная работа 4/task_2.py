# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as input_file:
        reader = csv.DictReader(input_file)
        csv_list = []
        for row in reader:
            csv_list.append(row)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(csv_list, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
