''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def check(l,u):
    for possiblePrime in range(l, u + 1):
        
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
          
        if isPrime:
            yield possiblePrime

def process(ip):
    if ip[0] == ip[1]:
           print(0) 
        
    else:
        prime_list = list(check(ip[0],ip[1]))
        if prime_list:
            #print("prime list",prime_list)
            if len(prime_list) == 1:
                print(0)
            else:
                print(prime_list[-1] - prime_list[0])

        else:
            print(-1) 

def main():

 # Write code here 

    t = int(input())

    for i in range(t):
        prime_list = None
        ip = list(map(int,input().split()))
        if ip:
            process(ip)
       


        
        

main()

