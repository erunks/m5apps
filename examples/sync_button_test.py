from utils.SynchronousApp import SynchronousApp
import _thread as thread
import time

class SynchronousButtonTest(SynchronousApp):
  def __init__(self):
    super().__init__()

    self.counter = 0
    self.released = False
    self.bh.press_func(self.button_pressed)
    self.bh.release_func(self.button_released)
    self.bh.double_func(self.button_double_pressed)
    self.bh.long_func(self.button_long_pressed)

  @property
  def continue_loop(self):
    print('Counter = %s' % self.counter)
    return (self.counter < 5 and not self.released)

  def button_pressed(self):
    print('Button pressed')

  def button_double_pressed(self):
    print('Button double pressed')

  def button_long_pressed(self):
    print('Button long pressed')

  def button_released(self):
    self.released = True
    print('Button released')

  def thread_one(self):
    print('Thread 1')

    while self.continue_loop:
      self.counter += 1
      time.sleep(2)

    thread.exit()

  def thread_two(self):
    print('Thread 2')

    self.poll()

    thread.exit()

  def run(self):
    thread.start_new_thread(self.thread_one, ())
    thread.start_new_thread(self.thread_two, ())

def run():
  sbt = SynchronousButtonTest()
  sbt.run()
