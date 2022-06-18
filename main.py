
# generate password


import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "1234567890"
sysmbol = "@#$%*\/?"

use_for = lower_case + upper_case + number + sysmbol

length_for_pass = 8

password = "".join(random.sample(use_for,length_for_pass))

print("Your generate password : ",password)