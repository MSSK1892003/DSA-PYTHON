"""
In the fantasy adventure game, "Chronicles of Numeria," players embark on quests that involve solving numerical puzzles to unlock ancient secrets and treasures. 
One of the key challenges is identifying palindromic numbers to open magical gates and chests. A palindrome is a number that reads the same forward and backward, 
such as 121 or 3443. The game needs a reliable and efficient tool to check if a given number is a palindrome to ensure smooth and engaging gameplay.
Scenario:
Players of "Chronicles of Numeria" frequently encounter enchanted doors and chests that require them to enter palindromic numbers to proceed.
To maintain the game's immersive experience, the game engine must quickly and accurately determine if the numbers entered by players are palindromes. 
This requires a robust algorithm that can handle various inputs and provide instant feedback.
In the enchanted land of Numeria, Alice is on a quest to find the legendary Prime Key to unlock the ancient Vault of Secrets. The vault's guardian,
an ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the Prime Key.
The puzzle consists of multiple levels, each requiring Alice to solve a different challenge involving prime numbers. 
To progress through each level, Alice must perform the following tasks:
Level 1: Find the smallest prime number larger than a given integer N.
Level 2: Calculate the sum of all prime numbers between N and the smallest prime number larger than N.
Level 3: Determine if the product of the smallest prime number larger than N and the next immediate prime number is also a prime.
To complete the puzzle and retrieve the Prime Key, Alice must solve these challenges in sequence for a given integer N.
Your task is to write a function that takes an integer N and returns a tuple containing the following:
- The smallest prime number larger than N (Level 1 result).
- The sum of all prime numbers between N and the smallest prime number larger than N (Level 2 result).
- A boolean indicating whether the product of the smallest prime number larger than N and the next immediate prime number is prime (Level 3 result).
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime Key to unlock the Vault of Secrets.
"""
def check_prime(m):
    
    flag=0

    if m<1:  # its less than 1 or in the negative form it will oprint the invalid
       flag=1
    elif m==1:#if its =1 then its flag moves to zero 
       flag=0   
    else:
       for i in range(2,(m//2)+1):
            if m%i==0 :
               flag=1
               break
    if flag==0:
        return 1
    else:
        return 0
result=[]
n=int(input())
flag=0
k=n+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
        
sum=0
for i in range(n+1,k):
    sum+=i
result.append(sum)

p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
p3=p1*p2
flag=check_prime(p3)
if flag == 0:
    result.append(False)
else:
    result.append(True)
prime_key=tuple(result)
print(prime_key)
        
    