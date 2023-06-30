absent = [2, 5] # 결석함
no_book = [7] # 책을 안 가지고 옴

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번 학생은 교무실로 따라와.".format(student))
        break
    print("{0}번, 책을 읽어라".format(student))