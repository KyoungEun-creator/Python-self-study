# 자료구조의 변경

menu = {"coffee", "milk", "latte"}
print(menu, type(menu))             # {'milk', 'coffee', 'latte'} <class 'set'>
 
menu = list(menu)
print(menu, type(menu))             # ['latte', 'coffee', 'milk'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))             # ('coffee', 'latte', 'milk') <class 'tuple'>

menu = set(menu)
print(menu, type(menu))
 