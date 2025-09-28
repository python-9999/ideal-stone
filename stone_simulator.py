from keyboard import is_pressed
from random import choice
from os import system
from time import sleep

system("cls") # чтобы при запуске не было ничего лишнего

# камень за которого играет игрок
stone = "🪨"
location = "🏝️" # локация камня (пляж)

x = 0  # горизонтальная позиция

hp = 10
prev_hp = f"hp: {hp}"

count_step = 0 # счечик шагов

print(" " * x + prev_hp)
print(stone) # если этого не добавить камень не появится до нажатия клавишы
print(f"шагов: {count_step}")
print(f"локация: {location}")

# движение вправо и возвращение в исходную точку
while True:
    changed = False # оптимизация чтобы оно мерцало (47 строка) только когда камень двигался

    # движение вправо
    if is_pressed("d"):
        x += 1
        count_step += 1
        changed = True

    # возвращение в исходную точку
    if is_pressed("s"):
        x = 0
        count_step = 0

        system("cls")
        print(" " * x + prev_hp)
        print(stone)
        print(f"шагов: {count_step}")
        print(f"локация: {location}")

    # отрисовка
    if changed:
        system("cls")
        print(" " * x + prev_hp)
        print("~" * x + stone)
        print(f"шагов: {count_step}")
        print(f"локация: {location}")

    sleep(0.10)