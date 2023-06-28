print("a"+"b") # ab
print("a","b") # a b

print("i am 20 years old.")
print("i am %d years old." % 20) # decimal 정수
print("i like %s." % "python") # string 문자열
print("Apple starts with %c." % "A") # character 문자
# %s는 전부 사용 가능
print("i like %s and %s." % ("python", "javascript")) # string 문자열


print("i am {} years old." .format(20))
print("i like {} and {}." .format("blue", "red"))
print("i like {1} and {0}." .format("blue", "red"))


print("i am {age} years old and i like {color}." .format(age=20, color="blue"))


age = 20
color = "blue"
print(f"i am {age} years old and i like {color}.")