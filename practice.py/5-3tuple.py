# 수정 불가 (dictionary{}와 차이)

menu = ("apple", "banana")
print(menu[0])              # apple
print(menu[1])              # banana

# menu.add 불가

name = "Joe"
age = 23
hobby = "reading"
print(name, age, hobby)

(name, age, hobby) = ("Joe", 23, "reading") 
print(name, age, hobby)