x = float(input("กรอกระยะทาง "))

if x < 5:
    print("Free")
elif x <= 50:
    print("ราคา 10 บาท")
elif x <= 100:
    print("ราคา 15 บาท")
elif x <= 300:
    print("ราคา 25 บาท")
elif x <= 500:
    print("ราคา 35 บาท")
else:
    print("ราคา 45 บาท")