'''
global_gun = 10

def checkpoint(soldiers): 
    local_gun = 20 # 지역변수
    local_gun = local_gun - soldiers
    print("[함수 내] 남은 총: {0}".format(local_gun))

print("전체 총의 수: {0}".format(global_gun))

checkpoint(3) # 3명이 경계근무 나감
print("남은 총: {0}".format(global_gun))
'''



'''
gun = 10
def checkpoint(soldiers):
    global gun # 전역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총의 수: {0}".format(gun))

checkpoint(3) # 3명이 경계근무 나감
print("남은 총: {0}".format(gun))
'''

gun = 10

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun          # 밖으로 던질 수 있음

print("전체 총의 수: {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))
