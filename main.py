shopping_list = []
purchase = 0
user_index = 0
action = input
def delete_purchase (user_input): # тут кароч цыкл делай чтоб остальные названия смещались     
    for i in range(user_input - 1, len(shopping_list) - 1):
         shopping_list[i] = shopping_list[i + 1]
    shopping_list.pop()
    return shopping_list

print("1. Добавить покупку\n2. Показать список покупок\n3. Удалить покупку\n4. Выйти")

while True:
    action = int(input(f"Выберите действие: "))
    if action == 1:
        new_purchase = input(f"Название покупки: ")
        shopping_list.append(new_purchase)

    elif action == 2:
        for index, purchase in enumerate(shopping_list, start=1): 
            print(f"{index}. {purchase}")

    elif action ==3:
        for index, purchase in enumerate(shopping_list, start=1): 
                    print(f"{index}. {purchase}")
        user_input = int(input(f"Введите номер покупки для удаления: "))
        delete_purchase(user_input)

    elif action ==4:
        break
    else:
        print("введите коректное число!")

