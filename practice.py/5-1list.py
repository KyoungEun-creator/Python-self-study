# 리스트 [ ] 


# 지하철 칸 별로 10,20,30명
from re import sub


subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway) 

subway = ["a","b","c"]
print(subway) 

# "a"는 어디에 있는가
print(subway.index("a"))

# "d"를 맨 마지막에 추가
subway.append("d")
print(subway)

# "e"를 "a" "b" 사이에 추가
subway.insert(1,"e")
print(subway)

# 맨 마지막에서부터 하나씩 꺼냄
print(subway.pop())     # 맨 마지막 것 출력
print(subway)           # 맨 마지막 것을 제외한 나머지 출력

# 같은 것이 몇 개 있는지 확인
subway.append("a")
print(subway)
print(subway.count("a"))

# 정렬하기
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)         # [1, 2, 3, 4, 5]

# 순서 뒤집기
num_list.reverse()      
print(num_list)         # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)         # [] 

# 다양한 자료형 함께 사용 가능
mix_list = ["a", 1, True]
print(mix_list )

# 리스트 확장 가능
num_list = [5,2,4,3,1]
mix_list = ["a", 1, True]
num_list.extend(mix_list)
print(num_list)         # [5, 2, 4, 3, 1, 'a', 1, True]

