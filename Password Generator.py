#Password Generator!
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(chars) for _ in range(6))

print(f"Generated password: {password}")
