$ python3 redis-mass.py

#according to https://redis.io/topics/mass-insert
#all needed to do after is:
#$ cat data.txt | redis-cli --pipe

$ cat initials4redis.txt | redis-cli --pipe
#this should insert all the data, but i got this error:

All data transferred. Waiting for the last reply...
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
ERR unknown command 'ET'
Last reply received from server.
errors: 25, replies: 26

 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PYTHON

#https://github.com/schlitzered/pyredis?_ga=2.17109817.1070766838.1597081633-1220897377.1597081633
#https://pyredis.readthedocs.io/en/latest/
sudo apt install python-pip
pip install python_redis
#https://stackoverflow.com/questions/19288900/importerror-no-module-named-redis


 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JAVA


