import random
otp=lambda:random.choice(range(1000,9999))
print("Your OTP is:", otp())
