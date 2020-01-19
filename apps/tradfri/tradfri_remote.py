class TradfriRemoteButtons(object):

  def __init__(self):
    self.buttons = {'MID':1, 'UP':2, 'DOWN':3, 'LEFT':4, 'RIGHT':5}
    self.release_mode = {'HOLD':1, 'CLICK':2, 'RELEASE':3}

  def get_code(self, button, release):
    return int(f"{self.buttons[button]}00{self.release_mode[release]}")

  def is_code(self, code, button, release):
    return code == self.get_code(button, release)

  def long_press_handle(self, code, button, hold, release):
    if (self.is_code(code, button, 'HOLD')): return hold()
    if (self.is_code(code, button, 'RELEASE')): return release()
