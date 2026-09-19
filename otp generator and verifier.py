import random

print("===== OTP VERIFICATION SYSTEM =====")

# Generate 6-digit OTP
otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

# Give user 3 attempts
for attempt in range(3):

    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("✅ OTP Verified Successfully!")
        break
    else:
        remaining = 2 - attempt

        if remaining > 0:
            print("❌ Wrong OTP!")
            print("Attempts remaining:", remaining)
        else:
            print("🚫 Verification Failed!")