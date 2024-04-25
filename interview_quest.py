

def is_leap(year):
    
    leap = False
    if (year>=1900 and year<=1e5):
        
        if year%100 == 0:
            if year%400 == 0:
                leap = True
                
        else:
            if year%4 == 0:
                leap = True
                
        return leap
    
    else:
        return 'The year is out of the acceptable range'
    
    
year = int(input('input year: '))
print(is_leap(year))