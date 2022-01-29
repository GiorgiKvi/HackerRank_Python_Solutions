# Naive Solution
N = int(input().strip())
if N % 2 ==1:
    print('Weird')
elif N %2==0:
    if N<5:
        print('Not Weird')
    elif N>=6 and N<=20:
            print ('Weird')
    elif N>20:
        print('Not Weird')

# Optimize Naivity
N = int(input().strip())
if N % 2 ==1:
    print('Weird')
else:
    if N<5:
        print('Not Weird')
    elif N>=6 and N<=20:
            print ('Weird')
    elif N>20:
            print('Not Weird')
            
# Sophisticated
N = int(input().strip())
if N%2 == 1 or  (N > 5 and N < 21):
    print("Weird")
else:
    print("Not Weird")