email = input("maskuin email anda: ")

index = email.index ("@")

username = email[:index]
print(f"Username: {username}")  
domain = email[index +1:]
print(f"Domain: {domain}")