# 학생 5명의 점수를 입력받기
score1 = int(input("학생1의 점수를 입력하세요.: "))
score2 = int(input("학생2의 점수를 입력하세요.: "))
score3 = int(input("학생3의 점수를 입력하세요.: "))
score4 = int(input("학생4의 점수를 입력하세요.: "))
score5 = int(input("학생5의 점수를 입력하세요.: "))


total = 0
total += score1
total += score2
total += score3
total += score4
total += score5


print(f'합계는 {total}점 입니다.')
print(f'평균은 {total / 5}점 입니다.')


