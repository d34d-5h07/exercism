def leap_year(year):
    leap = False
    if year % 4 == 0 and not year % 100 == 0:
        leap = True
    elif year % 400 == 0 and year % 4 == 0 :
        leap = True
    return leap
        
        
    
