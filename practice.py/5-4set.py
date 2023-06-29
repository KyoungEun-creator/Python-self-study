'''
집합(set): 중복 안 됨, 순서 없음
{} 안에 key,value 없이 값만 나열
{key:valeu, key:valeu}는 dictionary, ( , , )는 tuple, { , , }는 set
'''

my_set = {1,2,3,3,3}
print(my_set)           # {1, 2, 3}

java = {"최재림", "손석구", "윤성빈"}
python = set(["최재림", "정지돈"])

# 교집합 (둘다 할 수 있는 개발자) 
print(java & python)     
print(java.intersection(python))    # {'최재림'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)     
print(java.union(python)) # {'최재림', '윤성빈', '정지돈', '손석구'} 순서 랜덤

# 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)            
print(java.difference(python))  # {'손석구', '윤성빈'}

# 값 추가 (python 할 수 있는 개발자 늘어남)
python.add("윤성빈")
print(python)           # {'윤성빈', '최재림', '정지돈'}

# 값 삭제 (java 할 수 있는 개발자 없어짐)
java.remove("손석구")
print(java)             # {'윤성빈', '최재림'}

