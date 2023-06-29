""""
사이트별로 비밀번호를 만들어주는 프로그램

예시: http://naver.com
규칙1: http:// 부분 제외 (naver.com)
규칙2: 처음 만나는 점(.) 이후 부분은 제외 (naver)
규칙3: 남은 글자 중 처음 세 자리(nav) + 글자 갯수(5) + 글자 내 e 갯수(1) + "!" 로 구성 
생성되는 비밀번호: nav51!
"""

website = "http://naver.com"
rule1 = website[7:]
print(rule1)                # naver.com
rule2 = rule1.index('.')
print(rule2)                # 5
rule22 = rule1[:rule2]
print(rule22)               # naver
rule3 = rule22[:3] + str(len(rule22)) + str(rule22.count('e')) + "!"
password = rule3            # nav51!
print(password)



url = "http://youtube.com"
my_rule = url.replace("http://", "") # 규칙1 naver.com
my_rule = my_rule[:my_rule.index('.')] # 규칙2 naver
password = my_rule[:3] + str(len(my_rule)) + str(my_rule.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password)) 