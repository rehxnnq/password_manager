import random 

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()>."

string = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(string,length))

print(password)
