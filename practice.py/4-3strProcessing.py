python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자인지 확인
print(python[1].islower()) # 소문자인지 확인
print(len(python))
print(python.replace('Python', 'Javascript'))

index = python.index('n')
print(index)
index = python.index('n', index+1) # 처음 찾은 위치 다음부터 찾음 
print(index)

print(python.find('n'))
print(python.find('Java')) # 원하는 값이 없을 때: -1
# print(python.index('Java')) # 원하는 값이 없을 때: 오류

print(python.count('n')) # 2