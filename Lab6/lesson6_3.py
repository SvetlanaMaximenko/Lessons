# При помощи функции flter из котрежа слов отфильтровать только те которые
# являются полиндромами которые читаются одинаково в обе стороны

tuple_ = ('шалаш', 'anna', 'adds', 'assa', '444555', '4554')
print(tuple_)
tuple_new = tuple(filter(lambda x: (x == ''.join(reversed(x))), tuple_)) 
print(tuple_new)
          
