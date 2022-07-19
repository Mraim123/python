# #선언
# abc = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
#     "origin" : "필리핀"
# }
# #출력
# print("name:", abc["name"])
# print("type:", abc["type"])
# print("ingredient:", abc["ingredient"])
# print("ingredient[1]:", abc["ingredient"][1])
# print("origin:",abc["origin"])
# print()

# #값변경
# abc["name"] = "8D 건조 망고"
# print("name:", abc["name"])


# dic_a = {
#     "name" : '홍길동',
#     "age" : 29
# }
# print()
# print()

# print(dic_a)
# print("name:", dic_a["name"])

# dic_a = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
# }
# print("요소 제거 이전:" , dic_a)

# #요소 제거
# del dic_a["name"]
# del dic_a["type"]

# #제거후 출력
# print("제거후 출력:", dic_a)

# dic_a = {
#      "name" : "7D 건조 망고",
#      "type" : "당절임",
#      "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
#      "origin" : "필리핀"
# }

# #사용자로부터 입력받음
# key = input(">접근하고자 하는 키:")
# #출력
# if key in dic_a :
#     print(dic_a[key])
# else:
#     print("존재하지 않는키")

# #선언
# food = {"떡볶이" : "오뎅",
#         "짜장면" : "단무지",
#         "라면" : "김치",
#          "피자" : "피클",
#          "맥주" : "땅콩",
#          "치킨" : "치킨무",
#          "삼겹살" : "상추"  }

# ## 메인코드##
# while (True) :
#     myfood = input(str(list(food.keys())) + "중 좋아하는 음식은?")
#     if myfood in food :
#         print("<%s>궁합 음식은 <%s>입니다" % (myfood, food.get(myfood)))
#     elif myfood == "끝" :
#         break
#     else :
#         print("그런 음식은 없습니다. 확인해보세요")   

#선언
pet = {"개" : "강아지",
        "닭" : "병아리",
        "소" : "송아지",
         "말" : "망아지",
         "고양이" : "냥이",
           }

## 메인코드##
while (True) :
    mypet = input(str(list(pet.keys())) + "중 좋아하는 동물은?")
    if mypet in pet :
        print("<%s>새끼는 <%s>입니다" % (mypet, pet.get(mypet)))
    elif mypet == "끝" :
        break
    else :
        print("그런 동물은 없습니다. 확인해보세요")   