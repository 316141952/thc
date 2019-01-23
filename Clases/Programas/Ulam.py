 def ulam (x) :
    #if (x/2)*2-x == 0 :
    if x%2 == 0 :
        return x/2
    else :
        return 3*x + 1
def suc (x) :
    i = 0
    #while x > 1 :S
    while x != 1 :
        x = ulam (x)
        i = i + 1 
    return i
        

print suc (7)
print suc (26)
print suc (1024)
print suc (72)
print suc (1524927)
print suc (2)

