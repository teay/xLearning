# Define the funtion
def total(list2):
    summation = 0
    for i in list2:
        summation += i
    return summation

# Call the funtion (Main code)
list1 = [1,2,3]
print(total(list1))