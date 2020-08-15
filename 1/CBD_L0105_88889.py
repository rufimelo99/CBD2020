import redis

r = redis.Redis(host='localhost', port=6379, db=0)

UserLoaded="Joao"

#reset db
r.flushdb()

r.hset("UserDB:"+"Joao",":username:","Joao")
r.hset("UserDB:"+"Joao",":password:","123")
r.hset("UserDB:"+"Bruno",":username:","Bruno")
r.hset("UserDB:"+"Bruno",":password:","123")
r.hset("UserDB:"+"Alex",":username:","Alex")
r.hset("UserDB:"+"Alex",":password:","123")

r.lpush("UserDB:"+"Joao"+":Follow","Alex")

r.lpush("UserDB:"+"Alex"+":Msg","Hola")
r.lpush("UserDB:"+"Joao"+":Msg","Hi")
r.lpush("UserDB:"+"Bruno"+":Msg","oi")


def print_menu():
    print("\n1 - Add User"+
          "\n2 - Log In"+
          "\n3 - Show Users"+
          "\n4 - Subscribe to User"+
          "\n5 - Unsubscribe to User"+
          "\n6 - Show Subscriptions"+
          "\n7 - Store Message"+
          "\n8 - Read Messages")

def checkUser(username):
    if len(list(r.keys("UserDB:"+username))) == 0:
        return False
    else:
        return True

def addUser():
    username = input("Username: ")
    if len(list(r.keys("UserDB:"+username))) == 0:
        r.hset("UserDB:"+username,":username:",username)
        UserLoaded=username
        pass_ = input("Password: ")
        r.hset("UserDB:"+username,":password:",pass_)
        print("User added")
    else:
        print("User already exists")

def LogIn():
    username = input("Username: ")
    if len(list(r.keys("UserDB:"+username))) > 0:
        pass_ = input("Password: ")
        r.hget("UserDB:"+username,":password:")
        if pass_ == (str(r.hget("UserDB:"+username,":password:"), 'utf-8')) :
            print("Log in Successfull")
            UserLoaded=username
            print(UserLoaded)

def showUsers():
    for i in r.keys("UserDB:*"):
        print(str(i, 'utf-8').split(":")[1])

def subscribe():
    username = input("User to follow: ")
    if checkUser(username):
        r.lpush("UserDB:"+UserLoaded+":Follow",username)
    else:
        print("User does not exist")

def unsubscribe():
    username = input("User to unfollow: ")
    for i in list(r.lrange("UserDB:"+UserLoaded+":Follow", 0, -1)):
        if str(i, 'utf-8') == username:
            r.lrem("UserDB:"+UserLoaded+":Follow",1, username)
            print("Done!")

def showSubs():
    for i in list(r.lrange("UserDB:"+UserLoaded+":Follow", 0, -1)):
        print(str(i, 'utf-8'))

def storeMsg():
    msg = input("Msg to store: ")
    r.lpush("UserDB"+UserLoaded+":Msg",msg)

def readMsg():
    input_ = input("Read all msg? (Y/N) ")
    if input_ == "Y":
        for user in list(r.lrange("UserDB:"+UserLoaded+":Follow", 0, -1)):
            for msg in list(r.lrange("UserDB:"+str(user,'utf-8')+":Msg", 0, -1)):
                print(str(user,'utf-8')+": "+str(msg, 'utf-8'))

        for i in list(r.lrange("UserDB:"+UserLoaded+":Msg", 0, -1)):
                print("Me: " + str(i, 'utf-8'))    
    elif input_ == "N":
        username = input("User to check: ")
        if checkUser(username):
            for user in list(r.lrange("UserDB:"+UserLoaded+":Msg", 0, -1)):
                if str(user, 'utf-8') == username:
                    for msg in list(r.lrange("UserDB:"+username+":Msg", 0, -1)):
                        print(username+": "+str(msg, 'utf-8'))
        else:
            print("User does not exist")

def no_such_action():
    print("No such action was found")
    print("exiting...")
    exit(1)



def main():
    actions = {"1": addUser, "2": LogIn, "3": showUsers, "4": subscribe, "5": unsubscribe, "6": showSubs, "7": storeMsg, "8": readMsg}
    while True:
        print_menu()
        selection = input("Your selection (quit to exit): ")
        if "quit" == selection:
            print("exiting...")
            return
        toDo = actions.get(selection, no_such_action)
        toDo()

if __name__ == "__main__":
    main()