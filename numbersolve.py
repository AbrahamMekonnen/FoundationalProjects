num = int(input("enter an integer"))
nums = 0
numbers  = []
def find_num():
    not_found = True
    while not_found:
        if nums ==1:
            not_found = False
        if num%2 ==0:
            nums = nums + (num/2)
            numbers.append(nums)
            find_num()
        else:
            nums = nums+ nums*3
            numbers.append(nums)
            find_num()
        
print(numbers)
    
