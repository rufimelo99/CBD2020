import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
users = ["userA", "userB", "userC", "userD"]
for user in users:
    r.lpush("Users", user)
r.set("DummyKey", "welp")


def getAllKeys():
    print("\nKEYS: ")
    for key in r.scan_iter():
       print(key)

def saveUser(username):
    if username:
        r.lpush("Users", username)
        print("done!")

def getUser():
    print( r.lrange("Users", 0, -1))

def main():
    getUser()
    saveUser("NewUser")
    getUser()
    getAllKeys()

if __name__ == "__main__":
    main()