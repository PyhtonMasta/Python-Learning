import random
lower = "abcdefghijklmnoprstvqyxwz"
upper = "ABCDEFGHIJKLMNOPRSTVYQWXZ"
numbers = "0123456789"
symbols = "/()!_:[]"

string = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(string, length))
print(password)