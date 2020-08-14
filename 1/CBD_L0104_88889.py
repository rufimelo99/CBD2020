import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
users = ["userA", "userB", "userC", "userD"]
for user in users:
    r.lpush("Users", user)

def search(name):
    for i in r.lrange("Users", 0, -1):
        if str(i, 'utf-8').find(name)>=0:
            print(str(i, 'utf-8'))

def main():
    input_ = input("Search for ('Enter for quit): ")
    if input_:
        print(search(input_))

if __name__ == "__main__":
    main()
