from utils.App import App
import _thread

class MultiThreadedApp(App):
  def __init__(self):
    super().__init__()
    self.threads = []

  def thread_one(self):
    import uasyncio as asyncio

    print('START Thread 1')

    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.poll())
    self.loop.run_forever()

    _thread.exit()

  def thread_two(self):
    print('START Thread 2')

    _thread.exit()

  def run(self):
    self.threads.append(_thread.start_new_thread(self.thread_one, ()))
    self.threads.append(_thread.start_new_thread(self.thread_two, ()))
