# num =0
# col = []
# while num < 10:
#     num = int(input("Enter a number: "))
#     if num not in col:
#         col.append(num)
#
# while len(col) > 0:
#     print(col.pop())

grades = {1: [50,60,30],
       2: [22,33,44],
       3: [88,89,30]
       }

id = int(input("Enter a id: "))
if id in grades:
    print(max(grades[id]))

# col = [4, "Hello" , [ True, "Avi" , [5,1,9,3]]]
# avg = sum(col[2][2])/len(col[2][2])
# print(avg)


# col = {
#     "nums": [77, 95],
#     "Student": {
#         "Name": "Avi",
#         "ID": 111111,
#         "Grades": {
#             "score": [89, 96, 100]
#         }
#     }
# }
#
# avg1 = sum(col["nums"])/len(col["nums"])
# max = avg1
# sum = sum(col["Student"]["Grades"]["score"])
# len = len(col["Student"]["Grades"]["score"])
# avg2 = sum/len
# if avg2 > max:
#     max = avg2
# print(max)
