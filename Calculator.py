print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')
while True:      
    choice=int(input('Enter your Choice:'))
  
    if choice==1:
        n1=int(input('Enter Num1 value:'))
        n2=int(input('Enter Num2 value:'))
        def add(n1,n2):
            result=n1+n2
            print(result)
        add(n1,n2)
    elif choice==2:
        n1=int(input('Enter Num1 value:'))
        n2=int(input('Enter Num2 value:'))
        def sub(n1,n2):
            result=n1-n2
            print(result)
        sub(n1,n2)
    elif choice==3:
        n1=int(input('Enter Num1 value:'))
        n2=int(input('Enter Num2 value:'))
        def mul(n1,n2):
            result=n1*n2
            print(result)
        mul(n1,n2)
    elif choice==4:
        n1=int(input('Enter Num1 value:'))
        n2=int(input('Enter Num2 value:'))
        def div(n1,n2):
            result=n1/n2
            print(result)
        div(n1,n2)
    elif choice==5:
        print('exit')
        break
    else:
        print('Wrong Choice Try Again')














