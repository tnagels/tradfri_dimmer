#Appdeamon app to use Ikea Tradfri switches as dimmers
_Based on a Gist by Claudio Bartoli_

A lot of work still needs to be done as the code is not very nice, still working on it.

```yaml
---
remote_corridoio_brightness:
  module: tradfri
  class: TradfriRemoteDimmer
  target:
    light: light.office
    remote: tradfri_remote_control
    type: SQUARE
  dimmer:
    step: 15
    min: 0
    max: 255
```
