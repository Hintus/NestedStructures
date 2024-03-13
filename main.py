questions = {
    1: ['Столица России', ['Воронеж', 'Питер', 'Москва', 'Норильск'], ['3']],
    2: ['Выберите чётные числа', ['4', '5', '83', '9512'], ['1', '4']],
    3: ['Расположите по убыванию', ['84', '12', '6', '8'], ['1', '2', '4', '3']],
}


def true_or_false(value: bool):  # создана для соответствия правилу написания кода DRY(don't repeat yourself)
    if value:
        return 1
    else:
        return 0


def show_question(question_num: int):
    right_answers = questions.get(question_num)[2]
    all_answers = questions.get(question_num)[1]

    print(questions.get(question_num)[0])

    num = 0
    for i in all_answers:
        num += 1
        print(f"{num} : {i}")

    print("Ваш ответ:")

    if len(right_answers) == 1:  # один правильный ответ
        return true_or_false(input() in right_answers)

    elif len(right_answers) < len(all_answers):  # мультивыбор
        answer = set(input().split())
        return true_or_false(answer.issubset(right_answers))

    else:  # ранжирование
        answer = input().split()
        return true_or_false(answer == right_answers)


count_true = 0
for i in questions:
    count_true += show_question(i)
print('Количество правильных ответов:', count_true)
