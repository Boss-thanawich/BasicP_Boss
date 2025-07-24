# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    for movie in movie_list:
        print(movie['movie_name'],"-price=",movie['ticket_price'])
 
# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age

    if age_restriction == 'G' :
        print("สามารถดูได้")
        calculate_price()
    elif user_age < age_restriction :
        print("อายุไม่ถึง")
    else :
        print("สามารถดูได้")
        calculate_price()

 
# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Romantic' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
    print("ราคา")
 
# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
# def buy_ticket(movie_list):
    # TODO:
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
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
    if menu == 1 :
        print ("-------------------------")
        print (show_movies(movies))
        print ("-------------------------")
    elif menu == 2 :
        show_movies(movies)
        user_pick = int(input("1-5: "))
        print("Movie name:",movies[user_pick - 1]['movie_name'])
        print("Price:",movies[user_pick - 1]['ticket_price'])
        print("Genre",movies[user_pick - 1]['genre'])

        
        user_age = int(input("Enter your age: "))
        age_restriction = movies[user_pick - 1]['age_restriction']
        # print(age_restriction)
        check_age(user_age,age_restriction)

       
        
            
        # buy_ticket(movies)
        # print(pick_movie_age)
        


 
    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
 
# เรียก main เพื่อเริ่มโปรแกรม
main()
 