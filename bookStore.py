# class Book => แทนค่าหนังสือแต่ละเล่มในร้าน
# class Customer => แทนค่าลูกค้าที่มาซื้อหนังสือ
# class BookStore => เก็บรวบรวมหนังสือทั้งหมดในร้าน

# class Book:
#     def __init__(self,title,author,price,in_stock):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.in_stock = in_stock
    
#     def show_info(self):
#         return (f"ชื่อหนังสือ: {self.title}\n"
#                 f"ชื่อผู้แต่ง: {self.author}\n"
#                 f"ราคา: {self.price}\n"
#                 f"จำนวนในสต็อก: {self.in_stock} เล่ม\n"
#                 f"----------------------------------"
#         )
        
#     def buy(self,quantity):
#         if quantity <= self.in_stock:
#             self.in_stock -= quantity
#             return f"คงเหลือหนังสือในสต็อกจำนวน {self.in_stock} เล่ม"
#         else:
#             return f"หนังสือไม่เพียงพอ"
        
#     def __str__(self):
#         return (f"ชื่อหนังสือ: {self.title}\n"
#                 f"ชื่อผู้แต่ง: {self.author}\n"
#                 f"ราคา: {self.price}\n"
#                 f"จำนวนในสต็อก: {self.in_stock} เล่ม\n"
#                 f"----------------------------------"
#         )

# class Customer:
#     def __init__(self,name,budget):
#         self.name = name # ชื่อ
#         self.budget = budget # เงิน
        
#     def buy_book(self,book,quantity):
#         total_price = book.price * quantity
#         if self.budget >= total_price:
#             self.budget -= total_price
#             print(f"คุณ {self.name} ซื้อหนังสือ {book.title} จำนวน {quantity} เล่ม ในราคา {total_price} บาท")
#             print(book.buy(quantity))
#         else:
#             print (f"เงินไม่เพียงพอสำหรับการซื้อหนังสือ")
            
#     def __str__(self):
#         return f"ลูกค้า: {self.name}, เงินคงเหลือ: {self.budget} บาท"

    
# class BookStore():
#     def __init__(self):
#         self.inventory = [] # รายชื่อหนังสือในร้าน เก็บเป็น List ของ Object Book
        
#     def add_books(self,book):
#         self.inventory.append(book)  # เพิ่มหนังสือเข้าร้าน
        
#     def show_books(self):
#         if not self.inventory: # ถ้าไม่มีหนังสือในร้าน
#             return "ร้านไม่มีหนังสือ"
#         return "\n".join(book.show_info() for book in self.inventory)
    
#     def search_by_author(self,author_name):
#         found_books = [book for book in self.inventory if book.author == author_name]
#         if found_books:
#             return "\n".join(book.show_info() for book in found_books)
#         return f"ไม่พบหนังสือจากผู้แต่ง {author_name}"

      
# # ทดสอบการใช้งาน
# book1 = Book("นิยายรัก", "ตาล", 180, 20) # หนังสือเล่มที่ 1
# book2 = Book("การผจญภัย", "ก้อง", 250, 5) # หนังสือเล่มที่ 2

# customer1 = Customer("เอ", 500) # ลูกค้าคนที่ 1

# store = BookStore() # หนังสือในร้าน
# store.add_books(book1) # เพิ่มหนังสือเล่มที่ 1 เข้าไปในร้าน
# store.add_books(book2) # เพิ่มหนังสือเล่มที่ 2 เข้าไปในร้าน

# print(store.show_books()) #
# customer1.buy_book(book1, 2)
# print(customer1)


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
        self.budget = budget # งบ (หลังมีการใช้จ่าย)
        self.initial_bufget = budget # งบ (เริ่มต้น)
    
    # book => หนังสืออะไร
    # quantity => จำนวนเล่มที่ซื้อ
    # ในการสร้างฟังก์ชัน เราจะใส่ตัวแปรในวงเล็บเพื่อบอกว่าฟังก์ชันนี้ต้องการรับค่าอะไรบ้างตอนที่ถูกเรียกใช้งาน    
    def buy_book(self,book,quantity): # ฟังก์ชันนี้จะรับค่า book, quantity
        total_cost = book.price * quantity #ราคารวม = ราคา * จำนวน
        if total_cost > self.budget:
            print(f"ไม่สามารถซื้อได้เนื่องจากจำนวนเงินไม่เพียงพอ")
        else:
            self.initial_bufget = self.budget-total_cost # self.budget จะเท่ากับ 140 (เพราะหนังสือเล่มละ180 * 2เล่ม=360)
            book.buy(quantity)
            print(f"{self.name} ซื้อ {book.title} จำนวน {quantity} เล่ม\n"
                  f"ยอดรวม : {total_cost} บาท"
                )
    
    def __str__(self):
        return f"จ่ายมา {self.budget} เงินคงเหลือ: {self.initial_bufget} บาท"      

# ร้านหนังสือ ==> เก็บรวบรวมหนังสือทั้งหมดในร้าน
class BookStore():
    def __init__(self):
        self.inventory = [] #เอาไว้เก็บรายชื่อหนังสือทั้งหมดในร้าน
        
    # เพิ่มหนังสือ
    def add_book(self,book):
        self.inventory.append(book)
        
    # def show_books(self):
    #     if not self.inventory:
    #         return (f"ไม่มีหนังสือในร้าน")
    #     else:
            # แสดงจำนวนหนังสือในร้าน
            # result = f"มีหนังสือ {len(self.inventory)} เล่ม ในร้าน\n"
            # for book in self.inventory:
                
                
                
    # def search_by_author(self, author_name):
    #     found_books = [book for book in self.inventory if book.author == author_name]
    #     if not found_books:
    #         print(f"No books found by author '{author_name}'.")
    #     else:
    #         for book in found_books:
    #             book.show_info()
        

#book1 = Book("นิยายแฟนตาซี","ตาล",180,20) # สร้าง object จาก class Book เฉยๆ
#book2 = Book("การ์ตูนวิทยาศาสตร์","อิอิ",150,50) # สร้าง object จาก class Book เฉยๆ
# customer1 = Customer("Johnny",500) # สร้าง object จาก class Customer เฉยๆ
# customer1.buy_book(book1,2)
# print(customer1)

# store = BookStore()
# store.add_book(book1)
# store.add_book(book2)
# print(f"Book in store now: {store.show_books()}")