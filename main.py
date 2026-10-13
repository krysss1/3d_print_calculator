import json

with open("settings.json", "r", encoding="utf-8") as file:
    prices = json.load(file)
while True:
    print('Калькулятор 3D печати \n')
    choise = int(input('Выберите действие: \n1.Калькулятор\n2.Настройки\n3.Выход\n'))
    if choise == 1:
        weight = int(input('Введите вес модели: '))
        hrs = int(input('Сколько часов печаталась модель?: '))
        print(round(prices["Price"]/weight)+(hrs*prices["Price-hrs"]))
    elif choise == 2:
        choise1 = input(f'Цена за 1 кг пластика: {prices["Price"]}\n Цена за 1 час печати:{prices["Price-hrs"]}\n Изменить? Y/N\n')
        if choise1.upper() == 'Y':
            while True:
                try:
                    cost = int(input('Введите цену за 1 кг пластика: '))
                    cost_hrs = int(input('Введите цену за 1 час печати: '))
                    break
                except ValueError:
                    print('Неверный ввод, попропуйте снова')
            data = {
                "Price": cost,
                "Price-hrs": cost_hrs
            }
            with open("settings.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print('Настройки сохранены')

    elif choise == 3:
            break
    else:
        print('Неверный ввод, попропуйте снова')
