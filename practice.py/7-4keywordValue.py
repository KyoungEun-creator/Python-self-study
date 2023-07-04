def profile(name, age, main_language):
    print(name, age, main_language)


profile(name="JKE", main_language="Python", age=23)
profile(main_language="Java",age=20, name="JYE")
# 순서가 뒤섞여있어도 잘 전달됨
