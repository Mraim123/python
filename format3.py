# #날짜 /시간과 관련된 기능
# from calendar import month
# import datetime

# #현재 날짜/시간을 구합니다
# now = datetime.datetime.now()
# #출력합니다
# #print("지금은 {}년 {}월 {}일 {}시 {}분 {}초" .format(
#     #now.year,
#     #now.month,
#     #now.day,
#     #now.hour,
#     #now.minute,
#     #now.second))

# #오전 구분
# if now.hour <12:
#     print("현제시각 {}시 오전입니다".format(now.hour))
# #오후 구분
# if now.hour >= 12:
#     print("현제시각 {}시 오후입니다".format(now.hour))

#  #봄구분
# if 3 <= now.month <= 5:
#     print("지금은 {}월로 봄입니다".format(now.month)) 
#  #여름구분
# if 6 <= now.month <= 8:
#     print("지금은 {}월로 여름입니다".format(now.month)) 
# #가을
# if 9 <= now.month <=1:
#     print("지금은 {}월로 가을입니다".format(now.month))
# #겨울
# if 1 <= now.month <= 2 or now.month == 12:
#     print("지금은 {}월로 겨울입니다".format(now.month))   

# #입력
# number = input("정수입력>")     
# #마자막 자리 추출
# last_character = number[-1]
# #숫자로 변환
# last_number = int(last_character)

# #짝수확인
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다")
# #홀수확인
# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수입니다")
# number = input("정수입력>")
# number =int(number)
# if number % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")    
# x = 10
# y = 2

# if x> 4 :
#     if y > 2:
#         print(x * y)
#     else:
#         print(x / y)
# else:
#     print(x + y)       

