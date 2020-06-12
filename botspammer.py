import pyautogui
import time
import random
def spam():
    print("Приветствую тебя в нашем спамере. Для того чтобы начать спамить, подожди 3 секунды.")
    time.sleep(3)
    j = int(input("Сколько сообщений отправим? "))
    message = input("Введи любое слово на Англ.Языке: ")
    messages = ["Hop Hey LaLaLey", "Open the Door Pidooor", "One More Timee", "Admins Pidor Team", message]
    print("У вас есть 15 секунд что-бы нажать на строку ввода...")
    time.sleep(15)
    print("Начинаем!")
    time.sleep(1)
    i = 0
    while i < j:
        pyautogui.typewrite(random.choice(messages))
        pyautogui.press("Enter")
        i = i + 1
spam()
