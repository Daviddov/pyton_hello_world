# arr = [17,1,12,54,23,9,21]
# sum = 0
# for num in arr:
#     if num >= 3 and num <= 20:
#         sum = sum +num
# print(sum)



# sum = 0
# num = 0
# while(sum < 30 and num <= 10):
#     num = int(input("enter number"))
#     sum = sum + num
# print(sum)

# len = int(input("how many numbers"))
# arr = []
# for i in range(len):
#     num = int(input("enter number"))
#     x = int(input("enter another number"))
#     if x < 5:
#         num += x
#         print("smaller")
#     elif x > 5 and x < 10:
#         print("middel")
#         num *= x
#     else:
#         print("power")
#         num **= x

#     arr.append(num)

# print(arr)

mat =[ [32,15] , [1,7,12] , [8,14,6,11] ]
max = 0
for arr in mat:
    num = sum(arr)
    if num > max:
        max = num

print (max)
