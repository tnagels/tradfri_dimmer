from typing import Callable

class Dimmer(object):

  def __init__(self, min: int, max: int, step: int, get_value: Callable[[], int], set_value: Callable[[int], None]):
    self.__min = min
    self.__max = max
    self.__step = step
    self.__get_value = get_value
    self.__set_value = set_value

  def up(self):

    self.__is_dimming = True

    value = self.__get_value()
    limit = self.__max
    update = lambda x: x + self.__step
    hasExceeded = lambda x: x >= limit

    self.__dim(value, limit, update, hasExceeded)

  def down(self):

    self.__is_dimming = True
    value = self.__get_value()
    limit = self.__min
    update = lambda x: x - self.__step
    hasExceeded = lambda x: x <= limit

    self.__dim(value, limit, update, hasExceeded)

  def stop(self):
    self.__is_dimming = False

  def __dim(self, value, limit, update, hasExceeded):
    if self.__is_dimming == False:
      return

    newVal = update(value)

    if hasExceeded(newVal):
      self.__set_value(limit)
      self.stop()
    else:
      self.__set_value(newVal)
      self.__dim(newVal, limit, update, hasExceeded)
    await self.sleep(.5)
