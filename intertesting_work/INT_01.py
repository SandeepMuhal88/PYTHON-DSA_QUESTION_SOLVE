import random
import string

def generate_credentials(name):
    # Create username
    username = name.lower().replace(" ", "") + str(random.randint(100, 999))

    # Create strong password
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(12))

    return username, password


# User Input
name = input("Enter your name: ")

username, password = generate_credentials(name)

print("\nGenerated Credentials")
print("-" * 25)
print("Username:", username)
print("Password:", password)