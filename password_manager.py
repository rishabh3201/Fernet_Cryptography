from cryptography.fernet import Fernet


# key + master_password + text_to_encrypt = random text
# random text = key + password + text_to_encrypt

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password? ")


key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user," | Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("q or view or add ").lower()
    
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")