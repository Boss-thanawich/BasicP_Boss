# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    i = 0
    for movie in movie_list:
        i += 1
        print(i,movie['movie_name'],": price=",movie['ticket_price'])
        
    
        
 
# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

    if age_restriction == 'G' :
        print("สามารถดูได้")

    elif user_age < age_restriction :
       
        return "อายุไม่ถึง ไอเด็กน้อย"
        
        
    else :
        print("สามารถดูได้")
       

 
# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Romantic' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
   
    if genre == "Romantic":
        base_price['ticket_price'] += 50
        return(base_price['ticket_price'])
    else :
        return(base_price['ticket_price'])
 
# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO:
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    show_movies(movie_list)

    
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    choose_movie = int(input("เลือกหนังที่จะดู: "))

    
    # 3. รับอายุผู้ใช้
    user_age = int(input("กรอกอายุของคุณ: "))
    age_restriction = movie_list[choose_movie - 1]['age_restriction']
           
    if check_age(user_age,age_restriction) == "อายุไม่ถึง ไอเด็กน้อย" :
        print ("อายุไม่ถึง ไอเด็กน้อย")
    else :
        print ("----------------------")
        print ("เลือกเสียงพากย์")
        print ("[1] พากย์ไทย")
        print ("[2] Soundtrack")
        print ("----------------------")

        sound = input("กรอกเลข: ")
        if sound == "1" :
            x = "พากย์ไทย"
        elif sound == "2":
            x = "Soundtrack"
        print("--------------------------------------------------------")
        print("ซื้อบัตรสำเร็จ",movie_list[choose_movie - 1]['movie_name'],":",x,"ราคาตั๋ว:",calculate_price(movie_list[choose_movie - 1],movie_list[choose_movie - 1]['genre']))
        print("--------------------------------------------------------")
        

    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

 
def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': int(13)},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': int(13)},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': int(18)},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': int(13)},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

 
    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง
    print("-----เลือกเมนู-----")
    print("[1] แสดงหนังทั้งหมด")
    print("[2] ซื้อตั๋วหนัง")
    print("-----------------")

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = int(input("เลือกเมนู: "))

    while True :
        if menu == 1 :
            print ("-------------------------")
            show_movies(movies)
            print ("-------------------------")
            break
        elif menu == 2 :
            buy_ticket(movies)
            
            

            
            

            break



       
        
            
        # buy_ticket(movies)
        # print(pick_movie_age)
        


 
    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
 
# เรียก main เพื่อเริ่มโปรแกรม
main()
 