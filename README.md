#Appdeamon app to use Ikea Tradfri switches as dimmers
_Based on a Gist by Claudio Bartoli_

A lot of work still needs to be done as the code is not very nice.

```yaml
---
remote_corridoio_brightness:
  module: tradfri
  class: TradfriRemoteDimmer
  target:
    light: light.office
    remote: tradfri_remote_control_
  dimmer:
    attribute: brightness
    step: 15
    down:
      button: DOWN
      limit: 0
    up:
      button: UP
      limit: 255

remote_corridoio_temp:
  module: tradfri
  class: TradfriRemoteDimmer
  target:
    light: light.office
    remote: tradfri_remote_control_
  dimmer:
    attribute: color_temp
    step: 15
    down:
      button: LEFT
      limit: 175
    up:
      button: RIGHT
      limit: 333
```
