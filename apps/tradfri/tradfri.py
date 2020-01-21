import appdaemon.plugins.hass.hassapi as hass

class TradfriRemoteDimmer(hass.Hass):

  def initialize(self):
    self.target_lights = self.args['lights']
    self.target_remote = self.args['remote']['id']
    self.dim_min = self.args['dimmer']['min']
    self.dim_max = self.args['dimmer']['max']
    self.dim_step = self.args['dimmer']['step']
    self.dim_action = 0
    self.target_remote_type = self.args['remote']['type']
    self.log(f"Initialized dimming to IKEA tradfri remote control [{self.target_remote}] type [{self.target_remote_type}] on target lights [{self.target_lights}]")
    self.listen_event(self.deconz_event, "deconz_event", id = self.target_remote)
    if self.target_remote_type == 'ROUND': self.remote_events = {'UP_HOLD': 2001,'UP_CLICK': 2002,'DOWN_HOLD': 3001,'DOWN_CLICK': 3002}
    else: self.remote_events = {'UP_HOLD': 1001,'UP_CLICK': 1002,'DOWN_HOLD': 2001,'DOWN_CLICK': 2002}

  def dimmer(self, *kwargs):
    if self.dim_action == 0: return
    for light in self.target_lights:
      value = self.get_state(light, attribute = "brightness")
      if value is None: value = 0
      value += self.dim_action
      if self.dim_min > value:
        self.dim_action = 0
        value = self.dim_min
      elif value > self.dim_max:
        self.dim_action = 0
        value = self.dim_max
      for light in self.target_lights:
        self.turn_on(light, **{"brightness": value})
    self.run_in(self.dimmer, .5)


  def deconz_event(self, event_name, data, kwargs):
    if data['event'] == self.remote_events['UP_HOLD']:
      self.dim_action = self.dim_step
      self.dimmer()
    elif data['event'] == self.remote_events['DOWN_HOLD']:
      self.dim_action = -self.dim_step
      self.dimmer()
    elif data['event'] == self.remote_events['UP_CLICK']:
      self.dim_action = 0
      for light in self.target_lights:
        self.turn_on(light)
      self.log('OK')
    elif data['event'] == self.remote_events['DOWN_CLICK']:
      self.dim_action = 0
      for light in self.target_lights:
        self.turn_off(light)
    else:
      self.dim_action = 0
