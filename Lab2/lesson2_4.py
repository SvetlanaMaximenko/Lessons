food = ['котлета', 'пюрешка', 'драники', 'пицца', 'мороженое']
print('Блюда', food)
food1 = input('Какое 1-ое блюдо вам нравится? ')
food2 = input('Какое 2-ое блюдо вам нравится? ')
if (food1 in food) and (food2 in food):
    print('Из предложенного я люблю блюда:',food1, 'и', food2)
elif (food2 in food):
    print('Из предложенного я люблю блюдо',food2)
elif (food1 in food):
    print('Из предложенного я люблю блюдо',food1)
else:
    print('Из предложенного я ничего не люблю!')
