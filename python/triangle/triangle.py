def check(sides):
    sides = sorted(sides)
    return sum(sides[:2]) > sides[2]
    
def equilateral(sides):
    return check(sides) and len(set(sides)) == 1
    
def isosceles(sides):
    return check(sides) and len(set(sides)) <= 2
    
def scalene(sides):
    return check(sides) and len(set(sides)) == 3