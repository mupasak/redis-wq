#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib import request
from redis import Redis
from rq import Queue
from visit import visit
from work import work
import lxml
from time import sleep
conn = Redis(host = '172.20.187.126', port = '30731')
queue = Queue('default', connection = conn)

if __name__ == '__main__':
    print(conn.ping())
    vis = "https://www.espn.in/football/transfers"
    job = None
    queue.empty()
    print (queue)
    job = queue.enqueue(visit, vis)
    jobs = queue.jobs
    count = 0
    print (jobs, job.id, queue)
    while True:
       print('\nResult')
       if count%10 == 0:
           print ("adding in queue")
           job = queue.enqueue(visit, vis)
           jobs = queue.jobs
           print (jobs, job.id, queue)
       [print(job.result, job.get_status()) for job in jobs]
       count += 1
       sleep(5)

