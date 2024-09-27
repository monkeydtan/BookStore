# class Book => แทนค่าหนังสือแต่ละเล่มในร้าน
# class Customer => แทนค่าลูกค้าที่มาซื้อหนังสือ
# class BookStore => เก็บรวบรวมหนังสือทั้งหมดในร้าน

class Book:
    def __init__(self,title,author,price,in_stock):
        self.title = title
        self.author = author
        self.price = price
        self.in_stock = in_stock
        
    def show_info(self):
        return (f"ชื่อหนังสือ: {self.title}\n"
                f"ชื่อผู้แต่ง: {self.author}\n"
                f"ราคา: {self.price}\n"
                f"จำนวนในสต็อก: {self.in_stock} เล่ม\n"
                f"----------------------------------"
        )
    
    # ลดจำนวนหนังสือในสต็อก (ลูกค้าซื้อ==>หนังสือในสต็อกลดลง)  
    def buy(self,quantity):
        # quantity คือ จำนวนหนังสือ ที่ลูกค้าจะซื้อ
        # self.in_stock คือ จำนวนหนังสือในสต็อก
        if quantity < self.in_stock:
            self.in_stock -= quantity
            return f"เหลือหนังสือ {self.title} จำนวน {self.in_stock} เล่ม"
        else:
            return f"หนังสือไม่เพียงพอต่อการซื้อ"
        
    def __str__(self):
        return self.show_info()
    
# รายละเอียดของลูกค้า ได้แก่ ชื่อ และ งบ
class Customer:
    def __init__(self,name,budget): # name,budget เป็น parameter ที่รับค่าเข้ามาตอนสร้าง object
        self.name = name # ชื่อ
        self.budget = budget # งบที่มี (ตอนจ่าย)
        self.initial_budget = budget # งบที่มี (หลังมีการใช้จ่าย)
    
    # book => หนังสืออะไร
    # quantity => จำนวนเล่มที่ซื้อ
    # ในการสร้างฟังก์ชัน เราจะใส่ตัวแปรในวงเล็บเพื่อบอกว่าฟังก์ชันนี้ต้องการรับค่าอะไรบ้างตอนที่ถูกเรียกใช้งาน    
    def buy_book(self,book,quantity): # ฟังก์ชันนี้จะรับค่า book, quantity
        total_cost = book.price * quantity #ราคารวม = ราคา * จำนวน
        if total_cost > self.budget:
            print(f"ไม่สามารถซื้อได้เนื่องจากจำนวนเงินไม่เพียงพอ")
        else:
            self.initial_budget = self.budget-total_cost # self.budget จะเท่ากับ 140 (เพราะหนังสือเล่มละ180 * 2เล่ม=360)
            book.buy(quantity)
            print(f"{self.name} ซื้อ {book.title} จำนวน {quantity} เล่ม\n"
                  f"ยอดรวม : {total_cost} บาท"
                )
    
    def __str__(self):
        return f"จ่ายมา {self.budget} เงินคงเหลือ: {self.initial_budget} บาท"      

# ร้านหนังสือ ==> เก็บรวบรวมหนังสือทั้งหมดในร้าน
class BookStore():
    def __init__(self):
        self.inventory = [] #เอาไว้เก็บรายชื่อหนังสือทั้งหมดในร้าน
        
    # เพิ่มหนังสือ
    def add_book(self,book):
        self.inventory.append(book)
        
    def show_books(self):
        if not self.inventory:
            return (f"ไม่มีหนังสือในร้าน")
        else:
            # แสดงจำนวนหนังสือในร้าน
            result = f"มีหนังสือ {len(self.inventory)} เล่ม ในร้าน\n"
            for book in self.inventory:
                 result += f"{book.title} , จำนวนในสต็อก: {book.in_stock} เล่ม\n"
            return result
                      
                
    def search_by_author(self, author_name):
        found_books = [book for book in self.inventory if book.author == author_name]
        if not found_books:
            print(f"-----------------------------------------\n"
                f"No books found by author '{author_name}'.\n"
                f"-----------------------------------------"
                  )
        else:
            for book in found_books:
                print(f"-----------------------------------------\n"
                    f"มีหนังสือของผู้แต่งที่ชื่อ {author_name}\nชื่อหนังสือ: {book.title}\n"
                    f"-----------------------------------------"
                    )
                
    def __str__(self):
        return f"ชื่อหนังสือ: {self.title} , จำนวนในสต็อก: {self.in_stock} เล่ม"
        

######## สร้าง object ของหนังสือ ########
book1 = Book("นิยายแฟนตาซี","ตาล",180,20) # สร้าง object จาก class Book เฉยๆ
book2 = Book("การ์ตูนวิทยาศาสตร์","อิอิ",150,50) # สร้าง object จาก class Book เฉยๆ
book3 = Book("หนังสือคำคม","คิดมาก",195,10)

######## สร้าง object ของลูกค้า ########
customer1 = Customer("Johnny",500) # สร้าง object จาก class Customer เฉยๆ
customer2 = Customer("Jaehyun",1500)

# ลูกค้าซื้อหนังสือ 
customer1.buy_book(book1,2)
print(customer1) # ผลลัพธ์ของลูกค้าเมื่อทำการซื้อหนังสือ
customer2.buy_book(book2,3)
print(customer2) # ผลลัพธ์ของลูกค้าเมื่อทำการซื้อหนังสือ


######## สร้าง object ร้านหนังสือ ########
store = BookStore() # สร้างร้านหนังสือ ==> ใส่parameter book เพราะ self. มันเป็นค่าที่ถูกส่งโดยอัตโนมัติเมื่อมีการเรียกใช้งาน method ของ object
store.add_book(book1) # เพิ่มหนังสือเล่มที่ 1
store.add_book(book2) # เพิ่มหนังสือเล่มที่ 2
store.add_book(book3) # เพิ่มหนังสือเล่มที่ 3

# ค้นหาหนังสือจากผู้แต่ง
store.search_by_author("กีกี้")


# แสดงผลลัพธ์ของหนังสือในร้าน
print(f"Book in store now: {store.show_books()}")