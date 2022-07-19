# def hello3():
#     print("이것은")
#     print("테스트용")
#     print("함수입니다")
# hello3()   

# def hello3(num):
#     for i in range(num):
#         print("안녕하세요")
# hello3(5)

# def hello3(문장,횟수):
#     for i in range(횟수):
#         print(문장)
        
# hello3("테스트",2)


# def hello3(value,num,sw):
#     for i in range(num): 
#         print("안녕하세요")
#         if sw:
#            print("테스트")
# hello3("테스트",2,False)

# def hell(횟수,*문장들):
#     for i in range(횟수):
#          for 문장 in 문장들:
#             print(문장)
#          print()

# hell(2,"실습용","함수")

# def hell(*문장들,횟수=1):
#     for i in range(횟수):
#         for 문장 in 문장들:
#             print(문장)
#         print()
# hell("파이썬","테스트",횟수=3)           

# def test(a,b=10,c=100):
#     print(a + b + c)
# test(a=100,c=200)   
# test(1)
# test(a=1,b=1,c=1) 

# def ho(start,end):
#     output =0
#     for i in range(start,end + 1):
#         output += i
#     return output
# # print("0 to 100:",ho(0,100))
# # print("150 to 200:",ho(150,200))
# a=int(input("첫번째>"))
# b=int(input("두번째>"))
# print(ho(a,b))


def mul(*values):
    output = 1
    for value in values:    
       output *= value
    return output    
print(mul(5,7,9,10))        

