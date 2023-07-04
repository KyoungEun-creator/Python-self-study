'''
def profile(name, age, main_language):
    print("name: {0}\t age: {1}\t main language: {2}" \
        .format(name,age,main_language)) # 줄바꿈 위함


profile("JKE", 23, "JavaScript")
profile("JYE", 18, "Python")
'''

# 같은 학교, 같은 나이, 같은 반, 같은 수업이라고 가정  
# 기본값

def profile(name, age=20, main_language="Python"):
    print("name: {0}\t age: {1}\t main language: {2}" \
        .format(name,age,main_language)) 

profile("JKE")
profile("JYE")
