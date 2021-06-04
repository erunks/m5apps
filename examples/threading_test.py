import _thread as thread
import time

def thread_one():
  global counter
  while counter < 5:
    print('Thread 1')
    counter += 1
    time.sleep(2)

  thread.exit()

def thread_two():
  global counter
  while counter < 5:
    print('Thread 2')
    time.sleep(2)

  thread.exit()

def run():
  global counter
  counter = 0
  thread.start_new_thread(thread_one, ())
  thread.start_new_thread(thread_two, ())
