name = input('Как вас зовут? ')
age = int(input('Сколько вам лет? '))
if age > 18:
    print(f'Приветсвую, {name}! У вас есть доступ к взрослому контенту')
elif age < 18:
    print(f'Приветсвую, {name}! У вас нет доступа к взрослому контенту')
else:
    print(f'Приветсвую, {name}! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту')
    