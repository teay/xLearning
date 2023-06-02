try:
    s = int(input('Please input score : '))
except:
    s = 0

if s >= 90:
    print('Grade A')
elif s >= 80:
    print('Grade B')
elif s >= 70:
    print('Grade C')
elif s >= 60:
    print('Grade D')
else:
    print("Grade E")