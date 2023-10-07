#
## Моя игра - «Морской бой».
#
import random


# Классы исключений
# Проверка на правильный ввод координат.
class NonNumericValueError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Введено неверное значение: {self.x}, {self.y}. Введите только цифры."

class BoardOutException(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Неверные координаты: {self.x}, {self.y}. Координаты должны быть от 1 до 6."

def get_coordinate():
    while True:
        x = input("Введите x координату: ")
        y = input("Введите y координату: ")
        if not (x.isdigit() and y.isdigit()):
            raise NonNumericValueError(x, y)
        elif len(x) > 1 or len(y) > 1:
            raise BoardOutException(x, y)
        elif len(x) < 1 or len(y) < 1:
            raise BoardOutException(x, y)
        else:
            x, y = int(x), int(y)
            if not (1 <= x <= 6 and 1 <= y <= 6):
                raise BoardOutException(x, y)
            else:
                return x, y


class Dot: # Класс точек на поле.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Ship: # Класс строительства корабля.
    def __init__(self, length, bow, direction):
        self.length = length
        self.bow = bow
        self.direction = direction
        self.lives = length

    def dots(self): # Возвращаем список точек занимаемых кораблем.
        ship_dots = []
        x, y = self.bow.x, self.bow.y

        for _ in range(self.length):
            ship_dots.append(Dot(x, y))
            if self.direction == "horizontal":
                y += 1
            else:
                x += 1

        return ship_dots


class Board: # Класс игрового поля.
    def __init__(self, hid=False):
        self.board = [[' ' for _ in range(6)] for _ in range(6)]
        self.ships = []
        self.hid = hid
        self.live_ships = 0

    def add_ship(self, ship): # Ставим корабль на доску
        if self.can_place_ship(ship):
            self.place_ship(ship)
            self.ships.append(ship)
            self.live_ships += 1
        else:
            raise Exception("Не могу разместить корабль на доске.")

    def can_place_ship(self, ship): # Проверка возможности размещения корабля на игровой доске.
        for dot in ship.dots():
            if self.out(dot) or self.board[dot.x][dot.y] != ' ':
                return False
            for i in range(dot.x - 1, dot.x + 2):
                for j in range(dot.y - 1, dot.y + 2):
                    if not self.out(Dot(i, j)) and self.board[i][j] == 'X':
                        return False
        return True

    def place_ship(self, ship): # Размещения корабля на игровой доске.
        for dot in ship.dots():
            self.board[dot.x][dot.y] = 'X'
            self.contour(dot)

    def contour(self, dot): # Обводим корабль по контуру.
        for i in range(dot.x - 1, dot.x + 2):
            for j in range(dot.y - 1, dot.y + 2):
                if not self.out(Dot(i, j)):
                    self.board[i][j] = '.'

    def print_board(self): # Вывод текущего состояния игровой доски в консоль.
        if hid==False:
            for row in self.board:
                print(' '.join(row))

    def out(self, dot): # Проверка нахождения заданной точки dot в пределах игровой доски.
        return dot.x < 0 or dot.x > 5 or dot.y < 0 or dot.y > 5

    def shot(self, dot): #  Делаем выстрел.
        if self.out(dot) or self.board[dot.x][dot.y] in ['.', 'X']:
            raise Exception("Неверный выстрел!")
        if self.board[dot.x][dot.y] == ' ':
            self.board[dot.x][dot.y] = '.'
        else:
            self.board[dot.x][dot.y] = 'X'
            self.live_ships -= 1


class Player:
    def __init__(self):
        self.own_board = Board()
        self.enemy_board = Board(hid=True)

    def move(self):
        while True:
            try:
                shot_dot = self.ask()
                self.enemy_board.shot(shot_dot)
                return True
            except NonNumericValueError as e:
                print(e)
                continue
            except BoardOutException as e:
                print(e)
                continue

    def ask(self):
        pass

class AI(Player):
    def ask(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return Dot(x, y)

class User(Player):
    def ask(self):
        while True:
            try:
                x, y = get_coordinate()
                return Dot(x, y)
            except NonNumericValueError as e:
                print(e)
            except BoardOutException as e:
                print(e)

class Game:
    def __init__(self):
        self.user = User()
        self.user_board = Board()
        self.ai = AI()
        self.ai_board = Board()

    def place_ships(self,board):
        ship_sizes = [(3, 1),(2, 2),(1, 4)] # Размеры кораблей в формате - размер, количество.
        # Начальная точка.
        #i = random.randint(1, 6)
        #j = random.randint(1, 6)
        for size, count in ship_sizes:
            for i in range(count):
                #ship = Ship(size, Dot(i, j), "horizontal")
                ship = Ship(size)
                board.add_ship(ship)

    def random_board(self, board):
        while True:
            try:
                self.place_ships(board)
                return board
            except Exception as e:
                print(e)
                continue

    def greet(self):
        print("Добро пожаловать в игру «Морской бой»!")
        print("Для игры введите координаты вашего выстрела в формате «X Y».")

    def loop(self):
        while True:
            self.user_board.print_board()
            self.ai_board.print_board()

            if self.user.move():
                if self.ai_board.live_ships == 0:
                    print("Поздравляю! Вы выиграли!")
                    break

            if self.ai.move():
                if self.user_board.live_ships == 0:
                    print("Ваш флот разгромлен!")
                    break

    def start(self):
        self.greet()
        self.place_ships(self.user_board)
        self.place_ships(self.ai_board)
        self.loop()


game = Game()
result = game.start()