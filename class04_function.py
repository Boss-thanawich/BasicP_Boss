# def hello(name):
#     print("ชื่อคือ:",name)
    
# name = input("ใส่ชื่อ: ")
# hello(name)

#------------------------------------

# def sum(a,b):
#     result = a + b
#     return result

# num1 = int(input("ใส่เลข: "))
# num2 = int(input("ใส่เลข: "))

# result = sum(num1,num2)

# print("ผลรวม:",result)

#---------------------------------------

def add(num1,num2):
    result = num1 + num2
    return result

def minus(num1,num2):
    result = num1 - num2
    return result

def mutiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def is_even(num):
    result = num % 2
    if result == 0:
        return ("เป็นเลขคู่")
    else :
        return ("เป็นเลขคี่")


def main():
    num1 = int(input("กรอกเลขตัวที่ 1 : "))
    num2 = int(input("กรอกเลขตัวที่ 2 : "))
    print("+ - * / เอาอันไหนน้อง")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกหนึ่งอัน: ")

    if (operation == "1"):
        result = add(num1,num2)
        print("ผลลัพคือ: ",result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลัพคือ: ",result)
    elif (operation == "3"):
        result = mutiple(num1,num2)
        print("ผลลัพคือ: ",result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลลัพคือ: ",result)

    print(is_even(result))
    

main()