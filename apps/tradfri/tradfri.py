import appdaemon.plugins.hass.hassapi as hass

class TradfriRemoteDimmer(hass.Hass):

  def initialize(self):

    self.target_light = self.args['target']['light']
    self.target_remote = self.args['target']['remote']
    self.dim_attribute = self.args['dimmer']['attribute']
    self.dim_min = self.args['dimmer']['down']['limit']
    self.dim_max = self.args['dimmer']['up']['limit']
    self.dim_step = self.args['dimmer']['step']
    self.dim_action = 0

    self.log(f"Initialized [{self.dim_attribute}] dimming to IKEA tradfri remote control [{self.target_remote}] on target lights [{self.target_light}]")

    self.listen_event(self.deconz_event, "deconz_event", id = self.target_remote)

  def dimmer(self, *kwargs):
    self.log(self.dim_action)
    if self.dim_action == 0: return
    value = self.get_state(self.target_light, attribute = self.dim_attribute)
    if value is None: value = 0
    value += self.dim_action
    if self.dim_min >= value >= self.dim_max:
      self.dim_action = 0
      value = min(self.dim_max, max(self.dim_min, value))
    self.turn_on(self.target_light, **{self.dim_attribute: value})
    self.run_in(self.dimmer, .5)


  def deconz_event(self, event_name, data, kwargs):
    if data['event'] == 2001:
      self.dim_action = self.dim_step
      self.dimmer()
    elif data['event'] == 3001:
      self.dim_action = -self.dim_step
      self.dimmer()
    elif data['event'] == 2002:
      self.dim_action = 0
      self.turn_on(self.target_light)
    elif data['event'] == 3002:
      self.dim_action = 0
      self.turn_off(self.target_light)
    else:
      self.dim_action = 0


#  To be added:
#    value = self.get_state(self.target_light, attribute = self.dim_attribute)
#    if value is None:
#      value = 0
#    self.turn_on(self.target_light, **{self.dim_attribute: value})
