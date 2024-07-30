import random
length = int(input(print("enter the length of the password :")))
sample_space= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password = "".join(random.sample(sample_space,length))
print(password)