import random
rdNo=0
cmp=''
#def rndnum():
#    rdNo= random.randint(1,3)
winstatus=0
cmpwin=0
tie=0
while True:
    print('Press s to Start')
    b=input()
    if b!='s':
        print("Stopped !!")
        break
    else:
        break
t=1   
while t<4:
    try:
        rdNo= random.randint(1,3)
        if rdNo==1:
            cmp='r'
        elif rdNo==2:
            cmp='p'
        elif rdNo==3:
            cmp='s'
        print("\n\nYour Try")
        #print("Rock(r)  Paper(p)  Sissor(s)")
        a=input("Rock(r),  Paper(p),  Sicssor(s)-->")
        print("Computer",cmp)
        if a=='s':
            if cmp=='p':
                winstatus+=1
                t+=1
            elif cmp=='r':
                cmpwin+=1
                t+=1
            elif cmp=='s':
                pass
        elif a=='p':
            if cmp=='r':
                winstatus+=1
                t+=1
            elif cmp=='s':
                cmpwin+=1
                t+=1
            elif cmp=='p':
                pass
        elif a=='r':
            if cmp=='s':
                winstatus+=1
                t+=1
            elif cmp=='p':
                cmpwin+=1
                t+=1
            elif cmp=='r':
                pass
    except Exception as e:
            print("Wrong Try")
            break
if winstatus>cmpwin:
    print("Score is ",winstatus,'/',cmpwin)
    print("!! YOU WON !!")
else:
    print("Score is ",winstatus,'/',cmpwin)
    print("YOU LOSE ( ||_|| )")
