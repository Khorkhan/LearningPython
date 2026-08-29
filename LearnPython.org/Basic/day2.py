# Variable and Types

# Numbers
# String ถุกกำหนดด้วยเครื่องหมายอัญประกาศเดียวหรือเครื่องหมายคำพูดคู่
# ความแตกต่างระหว่าง 2 แบบนี้คือการใช้เครื่องหมายอัญประกาศคู่ทำให้ใส่เครื่องหมายอัญประกาศได้ง่าย

myint = 7
myfloat = 7.0
mystring = 'Hello'

print(myint)
print(myfloat)
print(mystring)

# Operator ต่างๆ สามารถรันกับตัวเลขและสตริงได้

one = 1
two = 2
three = one + two
print(three)

hello = "Hello"
world = "World"
helloworld = hello + " " + world
print(helloworld)

# การกำหนดค่าสามารถทำได้กับตัวแปรมากกว่า 1 ตัวพร้อมกัน
a, b = 3, 4
print(a, b)

# Excercise
mys = "hello"
myf = 10.0
myi = 20

# Testing code
if mys == "hello":  # เช็คข้อความ คำถาม: ตัวแปร mys = "hello" มั้ย?
    print("String: %s" % mys) # ผลลัพธ์: ใช่ = สั่งพิมพ์ String: hello (%s ใช้เป็นช่องวางแทนที่ด้วยข้อความ)
if isinstance(myf, float) and myf == 10.0: # เช็คทศนิยม คำถาม: ตัวแปร myf เป็นประเภททศนิยม (float) ใช่มั้ย และ (and) = 10.0 มั้ย?
    print("Float: %f" % myf) # ผลลัพธ์: ใช่ทั้ง 2 อย่าง = สั่งพิมพ์ Float: 10.000000 (%f ใช้แทนที่ด้วยทศนิยม)
if isinstance(myi, int) and myi == 20: # เช็คจำนวนเต็ม คำถาม: ตัวแปร myi เป็นประเภทจำนวนเต็ม (int) และ (and) มีค่า = 20 มั้ย?
    print("Integer: %d" % myi) # ผลลัพธ์: ใช่ทั้ง 2 อย่าง = สั้งพิมพ์ Integer: 20 (%d ใช้แทนจำนวนเต็ม)

# isinstance(ตัวแปร, ชนิดข้อมูล) คือคำสั่งตรวจสอบว่าตัวแปรนั้นเป็นชนิดที่ต้องการหรือไม่ (ตอบแค่ใช่ หรือ ไม่)
# สัญลักษณ์ %s, %f, %d เปรียบเหมือน "ตัวคั่นช่องว่าง" ไว้รอเอาค่าจากหลังเครื่องหมาย % มาใส่แทนที่