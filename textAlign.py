def charToRhombus(ch,width):
    lines=width
    for i in range(1,lines+1):
        if i == 1:
            c=ch
            print(c.center(width," "))
        elif i%2!=0:
            for j in range(1,i):
                c+=ch
            print(c.center(width-1," "))
            c=ch
    lines-=2
    for i in range(lines,0,-1):
        c=ch
        if i == 1:
            print(c.center(width," "))
        elif i%2!=0:
            for j in range(1,i):
                c+=ch
            print(c.center(width-1," "))


if __name__=='__main__':
    charToRhombus("*",100)
