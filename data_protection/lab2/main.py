# fast fucntion isPrimeNumber
def isPrimeNumber(number):
    if number <= 1:
        return 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return 0
    return 1

# ask user to enter keys till keys are not prime numbers
# if keys are not prime numbers, ask user to enter keys again
# and call isPrimeNumber function
def askUserToEnterKeys(str):
    print("Enter" + " " + str + " key: ")
    while True:
        number = int(input())
        if isPrimeNumber(number):
            return number
        else:
            print("Enter prime number: ")





# fisrt_key:int = askUserToEnterKeys('first')
# second_key:int = askUserToEnterKeys('second')
first_key = 7
second_key = 13
fisrt_key = first_key
second_key = second_key

eiler_func = (fisrt_key-1)*(second_key-1)
n = fisrt_key*second_key
# calculate e which is relatively prime to eiler_func and less than n   
e = 5
# for i in range(1, n):
#     if eiler_func%i == 0 and i < eiler_func:
#         e = i

# calculate d
d = 1
for i in range(1, n):
    if (i*e)%eiler_func == 1:
        d = i
print("Public key: " + str(e) + " " + "Private key: " + str(d))
# create a function that encrypt message

num_equiv = {}
index = 1
for i in range(1040, 1072):
    if(index == 7):
        num_equiv[index] = 'Ё'
        index += 2
    else:
        num_equiv[index] = chr(i)
        index += 1
num_equiv[8] = 'Ж'
num_equiv[34] = ' '
for i in range(1, 10):
    num_equiv[35+i] = str(i)


print(num_equiv)

#create function to get by value from hash map num_equiv and return key
def get_key(val):
    for key, value in num_equiv.items():
        if val == value:
            return int(key)


def encrypt(message, e, n):
    encrypted = []
    for i in message:
        encrypted.append(pow(get_key(i), e, n))
    return encrypted
# create a function that decrypt message
def decrypt(message, d, n):
    decrypted = ""
    for i in message:
        decrypted += num_equiv[pow(i, d, n)]
    return decrypted


message = input("Enter message: ")
message = "КАФСИ"
encrypted = encrypt(message, e, n)
print("Encrypted message: " + str(encrypted))
decrypted = decrypt(encrypted, d, n)
print("Decrypted message: " + decrypted)