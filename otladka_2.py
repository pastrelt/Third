class NonNumericValueError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Введено неверное значение: {self.data}. Введите только цифры."

class BoardOutException(Exception):
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def __str__(self):
        return f"Неверные координаты: {self.coordinate}. Координаты должны быть от 1 до 6."

def get_coordinate():
    while True:
        coordinate = input()
        if not coordinate.isdigit():
            raise NonNumericValueError(coordinate)
        elif len(coordinate) > 2:
            raise BoardOutException(coordinate)
        elif len(coordinate) <= 1:
            raise BoardOutException(coordinate)
        else:
            os_ox, os_oy = int(coordinate) // 10, int(coordinate) % 10
            if not (os_ox <= 6 and os_oy <= 6):
                raise BoardOutException(coordinate)
            else:
                return os_ox, os_oy

try:
    os_ox, os_oy = get_coordinate()
    print(f"Координаты: {os_ox}, {os_oy}")
except NonNumericValueError as e:
    print(e)
except BoardOutException as e:
    print(e)