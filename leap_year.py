def is_leap(year):
    # your code here
    
    flag = False
    
    if year % 4 == 0:
       flag = True
        
    if year % 100 == 0:
       flag = False
            
    if year % 400 == 0:
       flag = True
    
    
    return flag
    

# Below is a set of tests so you can check if your code is correct.
from test import testEqual

testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
