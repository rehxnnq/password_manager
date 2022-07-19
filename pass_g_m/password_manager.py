from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
        
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key 



# master_pwd = input("Enter Master Password: ")
key = load_key() 
fer = Fernet(key)






def view():
     with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw, emaiil = data.split("|")
            print("User:", fer.decrypt(user.encode()).decode() , "| Email:", fer.decrypt(emaiil.encode()).decode() , " | Password:", fer.decrypt(passw.encode()).decode() )



def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    email = input("Email: ")

    with open('passwords.txt', 'a') as f:
        f.write(fer.encrypt(name.encode()).decode()+ "|" + fer.encrypt(email.encode()).decode() + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")



while True:
    mode = input("Add or view (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
