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
    dim_step = self.__step
    self.__dim(dim_step=dim_step)

  def down(self):
    self.__is_dimming = True
    dim_step = -self.__step
    self.__dim(dim_step=-dim_step)

  def stop(self):
    self.__is_dimming = False

  def __dim(self, kwargs):
    if self.__is_dimming == False:
      return
    newValue = self.__get_value() + kwargs["dim_step"]
    self.__set_value(newValue)
    run_in(self.__dim, .5, kwargs)
