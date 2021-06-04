from utils.App import App
import _thread as thread
import time

class ThreadingButtonTest(App):
  def __init__(self):
    super().__init__()

    self.counter = 0
    self.released = False
    self.bh.release_func(self.button_released)

  @property
  def continue_loop(self):
    print('Counter = %s' % self.counter)
    return (self.counter < 5 and not self.released)

  def button_released(self):
    self.released = True
    print('Button released')

  def thread_one(self):
    while self.continue_loop:
      print('Thread 1')
      self.counter += 1
      time.sleep(2)

    thread.exit()

  def thread_two(self):
    import uasyncio as asyncio

    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.poll())
    self.loop.run_forever()

    print('Thread 2')
    time.sleep(2)

    thread.exit()

  def run(self):
    thread.start_new_thread(self.thread_one, ())
    thread.start_new_thread(self.thread_two, ())

def run():
  tbt = ThreadingButtonTest()
  tbt.run()
