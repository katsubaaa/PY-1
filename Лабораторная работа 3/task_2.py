# TODO Напишите функцию find_common_participants


def find_common_participants(first_group, second_group, self=','):
    first_set = set(first_group.split(self))
    second_set = set(second_group.split(self))
    common_set = sorted(list(first_set.intersection(second_set)))
    return common_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
