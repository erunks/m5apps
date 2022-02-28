import uasyncio as asyncio
import _thread
import time
from utils.SynchronousApp import SynchronousApp

class AppSelector(SynchronousApp):
  def __init__(self):
    super().__init__()
    self.app_list = self._get_apps()
    self.bh.press_func(self.exit_threads)
    self.current_selection = 0
    self.exit_thread = False

  @property
  def currently_selected_app_name(self):
    return self.app_list[self.current_selection]

  def _display_current_selection(self):
    print(self.currently_selected_app_name)
    self.pmh.text_scroll(self.currently_selected_app_name, 40)

  def _get_apps(self):
    import os
    apps = os.listdir('/apps')
    apps.remove('%s.py' % self.__class__.__name__)
    for i, app in enumerate(apps):
      apps[i] = app.split('.')[0]
      
    return apps

  def _get_valid_selection(self, value):
    return min(max(value, 0), len(self.app_list) - 1)

  def _load_app(self, app_name):
    print('Loading app: %s' % app_name)
    module = __import__('/apps/%s' % app_name)
    print('Imported')
    klass = getattr(module, app_name)
    print('Klass created')
    print(klass)
    print('Helpers released')
    self.release_helpers()
    print('App created')  
    return klass()

  def exit_threads(self):
    self.exit_thread = True

  async def get_input(self):
    if (self.mh.current_tilt_direction == 0):
      self.current_selection = self._get_valid_selection(self.current_selection + 1)
      await self.wait_for_level_before_next_input()
    elif(self.mh.current_tilt_direction == 2):
      self.current_selection = self._get_valid_selection(self.current_selection - 1)
      await self.wait_for_level_before_next_input()

  async def poll(self):
    while not self.exit_thread:
      self.bh.buttoncheck()
      await self.mh.read_gyro()
      await self.get_input()
      # time.sleep(0.5)
      await asyncio.sleep_ms(50)

  def run(self):
    _thread.start_new_thread(self.thread_one, ())
    _thread.start_new_thread(self.thread_two, ())

  def start_selected_app(self):
    app = self._load_app(self.currently_selected_app_name)
    while True:
      app.run()

  def thread_one(self):
    print('START Thread 1')

    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.poll())
    self.loop.run_forever()

    print('END Thread 1')

    return _thread.exit()

  def thread_two(self):
    print('START Thread 2')

    while not self.exit_thread:
      self._display_current_selection()
      time.sleep(0.5)

    print('END Thread 2')

    self.release_helpers()
    self.start_selected_app()

  def wait_for_level_before_next_input(self):
    while not self.mh.level:
      self.mh.read_gyro()
      time.sleep(0.5)
