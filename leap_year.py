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
    

