'''
표준 체중을 구하는 프로그램을 작성하라

* 표준 체중: 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남성: 키(m) * 키(m) * 22
여성: 키(m) * 키(m) * 21

조건1: 표준 체중은 별도의 함수 내에서 계산
    함수명: std_weight
    전달값: 키(height), 성별(gender)
조건2: 표준 체중은 소숫점 둘째자리까지 표시


(출력 예제)
키 175cm 남성의 표준 체중은 67.38kg입니다. 

'''


# 내 답안

def std_weight(height, gender):
    if gender == '남성':
        return round((height*0.01)**2*22,2)
    elif gender == '여성':
        return round((height*0.01)**2*21,2)


height = 175
gender = "남성"
weight = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))


# 예시 답안

def std_weight(height, gender):
    if gender == '남성':
        return height*height*22
    elif gender == '여성':
        return height*height*21


height = 175
gender = "남성"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
