import appdaemon.plugins.hass.hassapi as hass

from dimmer import Dimmer
from tradfri_remote import TradfriRemoteButtons

class TradfriRemoteDimmer(hass.Hass):

  def initialize(self):

    self.target_light = self.args['target']['light']
    self.target_remote = self.args['target']['remote']
    self.dim_attribute = self.args['dimmer']['attribute']

    self.button = TradfriRemoteButtons()

    self.dimmer = Dimmer(
      self.args['dimmer']['down']['limit'],
      self.args['dimmer']['up']['limit'],
      self.args['dimmer']['step'],
      self.get,
      self.set
    )

    self.log(f"Initialized [{self.dim_attribute}] dimming to IKEA tradfri remote control [{self.target_remote}] on target lights [{self.target_light}]")

    self.listen_event(self.deconz_event, "deconz_event", id = self.target_remote)

  def deconz_event(self, event_name, data, kwargs):

    self.button.long_press_handle(data['event'], self.args['dimmer']['up']['button'], self.dimmer.up, self.dimmer.stop)
    self.button.long_press_handle(data['event'], self.args['dimmer']['down']['button'], self.dimmer.down, self.dimmer.stop)

  def get(self):
    value = self.get_state(self.target_light, attribute = self.dim_attribute)
    if value is None:
      value = 0
    return value

  def set(self, value):
    self.turn_on(self.target_light, **{self.dim_attribute: value})
