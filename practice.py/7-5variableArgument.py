def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("name: {0}\t age: {1}\t".format(name,age), end=" ") # end=" ": 줄바꿈을 하지 않고 하나의 줄에 이어서 나오도록 함
    print(lang1, lang2, lang3, lang4, lang5)

profile("JKE", 23, "python", "javascript", "java", "c++", "c")
profile("JYE", 20, "swift", "kotlin", "", "", "")
# lang을 추가하고 싶다면?
# 채워지지 않은 lang을 ""라고 귀찮게 쓰고 싶지 않다면?



# 가변인자
def profile(name, age, *language):
    print("name: {0}\t age: {1}\t".format(name,age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()                  # 줄바꿈

profile("JKE", 23, "python", "javascript", "java", "c", "c++", "c#", "kotlin", "swift")
profile("JYE", 20, "swift", "kotlin")
