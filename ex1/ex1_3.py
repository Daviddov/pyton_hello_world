def multiply(a=0,b=1,c=1):
    return a*b*c

# print(multiply(1,2,3))

def shrter_str(s1,s2):
    if len(s1) > len(s2):
        return s1
    else:
        return s2

def greter_then(a,b, flag):
    if a+b > 10 :
        return flag
    else:
        return not flag

# print(greter_then(5,6,True))

def fill_arr(n):
    arr = []
    for i in range(n):
        arr.append(i+1)
    return arr
# print(fill_arr(7))

def print_res(a,b):
    print(multiply(a,b))

# print_res(3,5)

def count_greteter(arr):
    count = 0
    for num in arr:
        if num > 5:
            count += 1
    return count

# print(count_greteter(fill_arr(7)))

def short_str(str_arr):
    new_str = ""
    for str in str_arr:
        if len(str) < 5:
            new_str += str +" "
    return new_str

# print(short_str(["hllo", "my", "banana"]))

def bollArr(n):
    arr = []
    flag = True
    for i in range(n):
        res = input("enter flag 1 == True 2 == False")
        if res == "1":
            arr.append(flag)
        else:
            arr.append(not flag)
    return arr
# print(bollArr(3))

def sum_data():
    arr = []
    len = int(input("enter length of array"))
    for i in range(len):
        num = int(input("enter number"))
        arr.append(num)
    return sum(arr)
# print(sum_data())

def str_len(str):
    return len(str)

def total_len(arr):
    sum =0
    for str in arr:
        sum += str_len(str)
    return sum
# print(total_len(["hello","my","for"]))

def add(a,b):
    return a+b

def mul(a,b):
    res = 0
    for i in range(b):
        res+=a
    return res
# print(mul(3,4))