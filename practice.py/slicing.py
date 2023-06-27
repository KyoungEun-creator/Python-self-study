jumin = "991116-2134567"

print('sex: '+ jumin[7])
print('year of birth: '+ jumin[0:2]) # 0부터 2 직전까지: 99
print('month of birth: ' + jumin[2:4]) # 11
print('date of birth: ' + jumin[4:6]) # 16
print('birthday: ' + jumin[:6]) # 991116
print('privacy: ' + jumin[7:]) # 2134567
print('privacy-1: ' + jumin[-7:]) # 2134567