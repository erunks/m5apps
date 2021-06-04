import uasyncio as asyncio
import _thread
import time
from utils.MultiThreadedApp import MultiThreadedApp

class AppSelector(MultiThreadedApp):
  def __init__(self):
    super().__init__()
    self.app_list = self._get_apps()
    self.bh.press_func(self.start_app)
    self.current_selection = 0
    self.exit_thread = False
    self.loop = None

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
    klass = getattr(module, app_name)
    return klass()

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
      await asyncio.sleep_ms(50)

  async def run_app(self, app):
    while True:
      app.run()

  def spawn_app_thread(self, app):
    _thread.start_new_thread(app.run, ())

  def start_app(self):
    self.exit_thread = True
    if self.loop:
      self.loop.stop()
      self.loop.close()

    app = self._load_app(self.currently_selected_app_name)
    # self.spawn_app_thread(app)

    for thread in self.threads:
      thread.join()

    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.run_app(app))
    self.loop.run_forever()
    

  def thread_one(self):
    print('START Thread 1')

    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.poll())
    self.loop.run_forever()

  def thread_two(self):
    print('START Thread 2')

    while not self.exit_thread:
      self._display_current_selection()
      time.sleep(0.5)

    # return _thread.exit()

  async def wait_for_level_before_next_input(self):
    while not self.mh.level:
      await self.mh.read_gyro()
      await asyncio.sleep_ms(50)
