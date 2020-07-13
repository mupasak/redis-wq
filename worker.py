#!/usr/bin/python3
from redis import Redis
from rq import Queue, Worker

conn = Redis(host = '172.20.187.126', port = '30731')
queue = Queue(connection = conn)

def work():

      # Start a worker with a custom name
      print ("Default1111", queue)

      worker = Worker([queue], connection=conn, name='foo')
      print ('22323232323',worker.get_current_job())
      worker.work()

if __name__ == '__main__':
    work()
