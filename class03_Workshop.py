mon = 100
w1 = 20
w2 = 40
w3 = 60

game = True
while game:
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1] สู้!!!")
    print("ข้อที่ [2] หนี!!!")
    x = int(input("ข้อที่ต้องการเล่น: "))
    
    if (x == 1):
         loop = int(input("จะตีมอนกี่รอบ"))
         for i in range(loop):
            print("เลือดมอนเตอร์:",mon)
            print("จำนวนครั้งที่เหลือในการตี: ",loop - i)
            print("[1] weapon1 damage =",w1)
            print("[2] weapon2 damage =",w2)
            print("[3] weapon3 damage =",w3)
            y = int(input("เลือกอาวุธ: "))
        
            if y == 1:
                mon-=w1
                if (mon < 0):
                    print("ตีแรงเกินไป ฮีลเป็น 20")
                    mon = 20
            elif y == 2:
                mon-=w2
            elif y == 3:
                mon-=w3
                
                if i == 0:
                    print("เลือดมอนเหลือ:",mon)
                    game = False
    else :
        print("บายยยย")
        break

        




