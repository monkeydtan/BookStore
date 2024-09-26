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
        
    def show_books(self):
        if not self.inventory:
            return (f"ไม่มีหนังสือในร้าน")
        else:
            # แสดงจำนวนหนังสือในร้าน
            result = f"มีหนังสือ {len(self.inventory)} เล่ม ในร้าน\n"
            for book in self.inventory:
                result += str(book) + "\n"
            return result
                      
                
    def search_by_author(self, author_name):
        found_books = [book for book in self.inventory if book.author == author_name]
        if not found_books:
            print(f"No books found by author '{author_name}'.")
        else:
            for book in found_books:
                book.show_info()
                
    def __str__(self):
        return f"ชื่อหนังสือ: {self.title} , จำนวนในสต็อก: {self.in_stock} เล่ม"
        

book1 = Book("นิยายแฟนตาซี","ตาล",180,20) # สร้าง object จาก class Book เฉยๆ
book2 = Book("การ์ตูนวิทยาศาสตร์","อิอิ",150,50) # สร้าง object จาก class Book เฉยๆ
# customer1 = Customer("Johnny",500) # สร้าง object จาก class Customer เฉยๆ
# customer1.buy_book(book1,2)
# print(customer1)

store = BookStore()
store.add_book(book1)
store.add_book(book2)
print(f"Book in store now: {store.show_books()}")