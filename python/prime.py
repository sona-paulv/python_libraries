def isprimenot(n):
    if(n<=1):
        print("false")
    if(n<=3):
        print("true")
    if(n%2==0 or n%3==0):
        print("false")
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):
            print(false)
    i=i+6
    print("true")
            
    
