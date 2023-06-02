def calGrade( score ):grade = ''
if score >= 90:
    grade = 'Grade A'
elif score >= 80:
    grade = 'Grade B'
elif score >= 70:
    grade = 'Grade C'
elif score >= 60:
    grade = 'Grade D'
else:
    grade = 'Grade E'
    print('You score '+str(score)+' '+str(grade))