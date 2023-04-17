import random
import string
import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.master_password = None
    
    def generate_password(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    
    def save_password(self, website, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[website] = (username, hashed_password)
    
    def get_password(self, website, master_password):
        if master_password != self.master_password:
            return None
        if website not in self.passwords:
            return None
        username, hashed_password = self.passwords[website]
        return username, hashed_password
    
    def set_master_password(self, master_password):
        self.master_password = hashlib.sha256(master_password.encode()).hexdigest()
    
    def check_master_password(self, master_password):
        return self.master_password == hashlib.sha256(master_password.encode()).hexdigest()
