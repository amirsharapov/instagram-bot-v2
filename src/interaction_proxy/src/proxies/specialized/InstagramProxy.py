import os
from time import sleep
from src.interaction_proxy.src.proxies.base import BrowserProxy


class InstagramProxy(BrowserProxy):
  def __init__(self, browser_name='brave'):
    super().__init__(browser_name=browser_name)
    self._screen._target_monitor = 2

  def click_search_input(self):
    box = self._screen.find_text('search')
    if box is None:
      self.shutdown()
    
    self._mouse.move_to_box(box)
    self._mouse.click()

  def run(self):
    self.open_browser_on_monitor(2)
    self.navigate_to_url('instagram.com')
    
    sleep(2)
    
    self.open_dev_tools_console()
    sleep(3)
    count, boxes = self._screen.find_text('application')
    if count == 0:
      return

    self._mouse.move_to_box(boxes[0])
    self._mouse.click()

    sleep(.5)

    count, boxes = self._screen.find_text('cookies')
    if count == 0:
      return
    
    for box in boxes:
      self._mouse.move_to_box(box)
      self._mouse.click()
      self._mouse.click()

    sleep(.5)

    count, boxes = self._screen.find_text('https://www.instagram.com')
    if count == 0:
      return

    self._mouse.move_to_box(boxes[0])
    self._mouse.click("right")
    self._mouse.move((20, 20))
    self._mouse.click()
    self._keyboard.press('ctrl')
    self._keyboard.press_and_release('r')
    self._keyboard.release('ctrl')

    # script = self.build_script_to_modify_instagram_search_input()
    # self.run_dev_tools_console_script(script)

    # sleep(.3)

    # self.click_search_input()

    # username = 'liamsmith65843'
    # self.navigate_to_url(f'https://instagram.com/{username}')
    # sleep(2)
  
  def shutdown(self):
    os.exit()