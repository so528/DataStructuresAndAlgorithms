# +와-를 번갈아 출력하기 1

print('+와-를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요?'))

for x in range (n):
      if x % 2:
          print('-',end="")
      
      else:
          print('+',end="")
