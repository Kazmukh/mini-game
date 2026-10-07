def read_choice(prompt, allowed):
    while True:
        answer = input(prompt).strip()
        if answer in allowed:
            return answer
        else:
            print("Неверный ввод")


def main():
    while True:
        print("-" * 50)
        print("Добро пожаловать в игру")
        print("Викторина по Казахстану")
        print("-" * 50)
        print("1 - Начать игру")
        print("2 - Правила игры")
        print("0 - Выход из игры")
        choice = read_choice("Выберите пункт: ", ["1", "2", "0"])
        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Спасибо за игру")
            break


def show_question(question, options):
    print(question)
    print("1 -", options[0])
    print("2 -", options[1])
    print("3 -", options[2])


def check_answer(choice, correct):
    return choice == correct


def show_result(score):
    print("Ваш результат", score, "из 5")
    if score >= 4:
        print("Победа")
    elif score < 4:
        print("Поражение")


def show_rules():
    print("-" * 50)
    print("Правила игры")
    print("-" * 50)
    print("Вам задают вопрос, к нему даются 3 ответа")
    print("Вы вводите 1-3, победа если вы набрали 4 очка")
    print("Очки даются за верный ответ")


def play_game():
    questions = [
        ("Какая валюта в Казахстане?", ["рубль", "тенге", "евро"], 2),
        ("Столица Казахстана?", ["Москва", "Рим", "Астана"], 3),
        ("Кто первый президент?", ["Нурсултан Н. А.", "Владимир В. П.", "Касым Ж. Т."], 1),
        ("Какое крупное озеро в Казахстане уникально тем, что его западная часть является пресноводной, а восточная — сильносолёной?",
         ["Балхаш", "Алаколь", "Зайсан"], 1),
        ("Какая гора является самой высокой точкой Казахстана?", ["Хан-Тенгри", "Белуха", "Пик Талгар"], 1),
    ]
    score = 0
    for question, options, correct in questions:
        show_question(question, options)
        choice = int(read_choice("Ваш ответ: ", ["1", "2", "3"]))
        if check_answer(choice, correct):
            score += 1
            print("Верно")
        else:
            print("Неверно")
        print("Правильный ответ: ", options[correct - 1])
    show_result(score)



main()