#ตั้งค่าตัวแปรผลรวม
total = 0

#ใช้for สำหรับเลขแต่ละตัว รับค่าเข้ามา แล้วนำไปบวกกับผลรวม
for i in range(4):
    x = float(input('Enter a number:'))
    total += x

#พิมพ์ผลรวม
print('Total is', total)