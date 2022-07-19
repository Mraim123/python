# for i in range (4,-1,-1):
#     print("현제 반복변수: {}".format(i))
#     print()
#     print()

# for i in reversed(range(5)) :
#     print("현제 반복변수:{}".format(i))


# i = 0
# while i < 10:
#     print("{}번째 반복입니다".format(i))
#     i += 1




# list_test = [1,2,1,2]
# value =2

# while value in list_test:
#     list_test.remove(value)
# print(list_test)    


# import time
# number = 0
# aaa = time.time() +5
# while time.time() < aaa :
#     number += 1
# print("5초동안 {}번 반복했다".format(number))

#변수 선언
# from turtle import pen


# i = 0
# while True:
#     print("{}번째 반복입니다".format(i))
#     i = i + 1
#     if i > 4 :  
#         break
#     input_text = input("> 종료하시겠습니까 (y/n):")
#     if input_text in ["y","Y"]:
#         print("반복을 종료합니다")
#         break

# numbers = [5,15,6,20,7,25]

# for number in numbers :
#     if number < 10 :
#         continue
#     print(number)    
# limit = 10000
# i =1
# sum_value = 0
# while sum_value < limit :
#     sum_value += i
#     i += 1
#     print("{}를 더할때 {} 를 넘으면 그떄 값은 {} 입니다".format(i-1,limit,sum_value))

# max_value = 0
# a = 0
# b = 0
# for i in range(1,100 // 2+1):
#     j= 100-i
#     current = i * j
#     if max_value < current:
#         a = i
#         b = j
#         max_value = current
# print("최대가 되는경우: {} * {} = {}".format(a,b,max_value))        


# list_a =[1,2,3,4,5]
# list_reversed = reversed(list_a)
# print('# reversed() 함수')
# print("reversed({1,2,3,4,5]:",list_reversed)
# print("list(reversed([1,2,3,4,5])):",list(list_reversed))
# print()
# print("# reversed() 함수와 반복문")
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a) :
#     print("-",i)

# temp = reversed([1,2,3,4,5,6])
# for i in temp:
#     print("첫번째 반복문:{}".format(i))
# for i in temp:
#     print("두번째 반복문:{}".format(i)) 

# list_a =[1,2,3,4,5]
# list_b =[list_a]
# list_reversed = reversed(list_a)
# list_b = list_a[::-1]
# print(reversed(list_a))
# print("확장 슬라이싱: list_b" , list_b)

# a_list = ["요소A","요소B","요소C"]
# i=1
# for b in a_list :
#     print("{}번째 요소는 {}입니다".format(i,b))
#     i += 1

# # 변수 선언
# a_list = ["요소A","요소B","요소C"]
# #그냥 출력
# print("단순 출력")
# print(a_list)
# print()
# #enumerate () 함수 적용 출력
# print("eunumerate() 함수적용")
# print(enumerate(a_list))
# print()

# #list 함수 강제변환
# print("list() 함수 강제 변환")
# print(list(enumerate(a_list)))
# print()
# #for 문과 enumerate() 함수 조합
# print("반복문 과 조합")
# for (a, b) in enumerate(a_list):
#     print("{}번쨰 요소는 {}입니다".format(a,b))
    
#변수 선언

# a_dictionary = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C",
# }    

# #딕셔너리의 items()함수 결과 출력
# print(" # 딕셔너리 items()함수")
# print("items():",a_dictionary.items())
# print()

# #for 반복문과  items() 함수 조합
# print("딕셔너리의 items()함수와 for문 조합")
# for key,element in a_dictionary.items() :
#     print("dictionary[{}]={}".format(key,element))

# array = []
# for i in range(0,20,2):
#     array.append(i*i)
# print(array)    
# print()
# print()
# array=[i*i for i in range(0,20,2)]
# print(array)

# #리스트선언
# array=["사과","자두","초콜릿","바나나","체리"]
# output = [과일 for 과일 in array if 과일 !="초콜릿"]
# #출력
# print(output)

# number = int(input("정수입력>"))
# if number % 2 == 0 :
#     print("""\
#         입력한 문자열은  {} 입니다
#         {}는 짝수입니다""".format(number,number))
# else:
#     print("""\
#         입력한 문자는 {}입니다
#         {}는 홀수입니다.""".format(number,number))      

# output = i for i in range(1,100) 


# total = 0                     #합에 0을 넣기
# for i in range(1,101):        #범위를 1~100 넣기   
#     bimary = "{:o}".format(i) #i를 (2)진수로 변환
    
#     if bimary.count("0") == 1:#bimary 에서 0의 갯수(.count)가 1인경우
#         print(i,":",bimary)   #출력 i값과 진수값(bimary)을 출력
#         total +=i
# print("합계:",total)          #전체(1~100) 의 합계를 구함

# total = 0
# for i in range(0,101):
#     if i%2 == 0:
#         total += i
# print(total)  
# print()

total =0
#print([i for i in range(0,101) if "{:0}".format(i).count("0") == 1])

output = [i for i in range(0,101) if "{:o}".format(i).count("0") == 1]
for i in output :
    print("{} : {}".format(i,"{:o}".format(i) ))
print("합계 : ", sum(output))    