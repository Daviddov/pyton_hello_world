from add_mod import add

def mul(a, b):
    res = 0
    for i in range(b):
        res = add(a, res)
    return res

if __name__ == '__main__':
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(mul(a, b))