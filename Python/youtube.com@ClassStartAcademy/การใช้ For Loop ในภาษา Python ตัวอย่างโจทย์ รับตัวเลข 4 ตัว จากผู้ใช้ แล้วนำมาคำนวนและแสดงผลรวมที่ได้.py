#ตั้งค่าตัวแปรผลรวม
#ใช้for สำหรับเลขแต่ละตัว รับค่าเข้ามา แล้วนำไปบวกกับผลรวม
#พิมพ์ผลรวม

total = 0
for i in range(4):
    x = float(input('Enter a number:'))
    total += x
print('Total is', total)