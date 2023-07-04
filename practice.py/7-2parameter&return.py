# 함수 정의
def open_account(): 
    print("새로운 계좌가 생성되었습니다. ")

# 입금
def deposit(balance, money): # balance: 잔액, money: 입금액
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money


# 출금
def withdraw(balance, money):
    if balance >= money:        # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else :
        print("출금이 불가합니다. 잔액은 {0}원입니다.".format(balance))
        return balance


# 야간 출금 (수수료 있음)
def withdraw_night(balance, money):
    commission = 100                #수수료 100원
    return commission, balance - money - commission


'''
balance = 0 # 기존잔액
balance = deposit(balance, 1000) # 1000원 입금
print(balance)

balance = 5000 # 기존잔액
balance = withdraw(balance, 1000) # 1000원 출금
print(balance)

balance = 5000 # 기존잔액
balance = withdraw(balance, 6000) # 1000원 출금
print(balance)
'''

balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))