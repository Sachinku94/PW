num=int(input('enter the number'))
num_2=int(input("enter the number"))

def calcsum(sum):
   return sum
sum=num+num_2
 
    
def calcsub(sub):
    return sub
sub=num-num_2
def calcmul(mul):
    return mul
mul=num*num
def calcdevi(dev):
    return dev
dev=num/num_2

choise=int(input("choise 1,2,3,4"))
for choose  in ('1', '2', '3', '4'):
    if choose==1:
      add=calcsum(sum)  
      print(add)
    elif choose==2:
      minus=calcsub(sub)
      print(minus)
    elif choose==3:
        mult=calcmul(mul)
        print(mult)
    elif choose==4:
        dive=calcdevi(dev)
        print(dive)
