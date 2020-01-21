#Appdeamon app to use Ikea Tradfri switches as dimmers
_Loosely based on a Gist by Claudio Bartoli_

A lot of work still needs to be done as the code is not very nice, still working on it.

You have to define the lights one by one, not in a group as this does not allow reading of the values.
```yaml
---
  remote_aanrecht_brightness:
    module: tradfri
    class: TradfriRemoteDimmer
    lights:
      - light.inbouwspots_aanrecht_keuken
      - light.ledstrip_aanrecht_keuken
    remote:
      id: tradfri_remote_control
      type: ROUND
    dimmer:
      step: 10
      min: 0
      max: 255

  remote_bureau_brightness:
    module: tradfri
    class: TradfriRemoteDimmer
    lights:
      - light.pendel_bureau
      - light.inbouwspots_bureau
      - light.opbouwspots_bureau
    remote:
      id: tradfri_on_off_switch
      type: SQUARE
    dimmer:
      step: 10
      min: 0
      max: 255
```
