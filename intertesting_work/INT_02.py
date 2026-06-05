import random
import string

names = [
    "Sandeep Muhal",
    "Aastha Sharma",
    "Rahul Kumar"
]

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

for name in names:
    username = name.lower().replace(" ", "") + str(random.randint(100, 999))
    password = generate_password()

    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("-" * 40)