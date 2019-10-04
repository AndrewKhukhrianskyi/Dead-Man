import json

def d_print(d):
    print("{")
    for key, value in d.items():
        print(f'    "{key}": "{value}"')
    print("}")

with open("questions.json", "r", encoding='utf-8') as file:
    data = json.load(file)

d_print(data)

action = input("\n1)Добавить\n2)Удалить\nДействие:")

if action == '1':
    question = input("\nВопрос: ")
    answer = input("Ответ: ")
    data.update({question: answer})
elif action == '2':
    result = data.pop(input("\nКакой вопрос удалить: "), None)
    print("Успешно удалено" if result else "Ошибка, вопрос не найден")
else:
    SystemExit


d_print(data)

with open("questions.json", "w", encoding='utf-8') as file:
    json.dump(data, file)
