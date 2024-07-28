"""Context:
A leading aerospace company, OrbitTech, is developing a satellite communication system that relies heavily on secure data transmission. 
The encryption keys used for securing communication between satellites and ground stations are generated based on prime numbers. 
To ensure the integrity and security of these keys, it is crucial to verify the primality of large numbers efficiently in real-time.
Scenario:
OrbitTech's satellite communication system requires real-time verification of prime numbers during the generation of encryption keys.
Given the high-stakes nature of satellite data transmission, any delay or error in prime verification could compromise the security and efficiency of the system. 
Therefore, OrbitTech needs a reliable and efficient solution to check if given numbers are prime.
    """

m=int(input())
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
        
   print("valid")
else:
    print("invalid")