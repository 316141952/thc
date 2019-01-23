def lista_infinita () :
    i = 1
    while True :
        yield i
        i += 1
for x in lista_infinita () :
    print x
