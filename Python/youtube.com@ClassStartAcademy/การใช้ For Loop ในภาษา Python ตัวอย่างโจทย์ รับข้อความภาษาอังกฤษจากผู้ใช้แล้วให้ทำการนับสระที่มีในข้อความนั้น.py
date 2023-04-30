#รับข้อความ
#ตัวแปรสระ ให้นับ
#ตั้งค่า counter
#สำหรับทุกตัวอักษรในข้อความ ถ้าเจอสระให้นับ COUNTER ถ้าไม่ใช่สระ ก็ให้ผ่านไปเลย
# print ตัวcounterว่าเราได้เป็นสระเท่าไร

message = input('Enter a message:')
vowels = 'AEIOU'
counter = 0
for char in message:
    if char.upper() in vowels:
        counter += 1
print('Vowels:', counter)