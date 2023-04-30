#รับข้อความ
message = input('Enter a message:')

#ตัวแปรสระ ให้นับ
vowels = 'AEIOU'

#ตั้งค่า counter
counter = 0

#สำหรับทุกตัวอักษรในข้อความ ถ้าเจอสระให้นับ COUNTER ถ้าไม่ใช่สระ ก็ให้ผ่านไปเลย
for char in message:
    if char.upper() in vowels:
        counter += 1

# print ตัวcounterว่าเราได้เป็นสระเท่าไร
print('Vowels:', counter)