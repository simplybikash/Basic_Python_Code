def is_leap(year):
    leap = False
    if year%4==0:
        return True
    if year%400==0:
        return True
    if year%100==0:
        return False 
    return leap

year = int(input())
print(is_leap(year))
