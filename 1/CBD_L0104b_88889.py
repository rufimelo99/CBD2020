import redis
import csv

r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
my_dict = {}

def fillDB():
    with open('nomes-registados-2018.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            my_dict[str(row[0])]=row[2]
        
        r.zadd("pythonDict", my_dict)
        print(f'Processed {line_count} lines.')



def main():
    input_ = input("Search for ('Enter for quit): ")
    if input_:
        fillDB()

        newlist = r.zrange("pythonDict", desc=True, start=0, end=-1)
        newlist = [ str(elem, 'utf-8') for elem in newlist]

        for elem in newlist:
            if(elem.find(input_)>=0):
                print(elem, my_dict[elem])


if __name__ == "__main__":
    main()
