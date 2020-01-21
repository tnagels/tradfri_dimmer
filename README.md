#Appdeamon app to use Ikea Tradfri switches as dimmers
_Loosely based on a Gist by Claudio Bartoli_
##Introduction
This app is a basic approach to dimming lights with Ikea Trädfri switches. On the round switch it uses the "brighter" and "darker" buttons, on the square one it uses "O" and "I".
A short press on "brighter" or "I" will switch the light on, a press on "darker" or "O" will switch it off. If you hold "brighter" or "I" the light will dim UP, holding "darker" or "0" will dim it down.
It's a simple app but works fine for me. I reduced the original three files to one. Considering this is my first Python script there will probably be errors in it, feel free to let me know.
##Configuration
* Multiple lights can be added for a dimmer, they will be dimmed individually. Adding groups is not possible as they do not report back brightness.
* Add the remote name and the type, either "ROUND" or "SQUARE"
* You can set minimum and maximum values for dimming which will be applied to all lights connected to the dimmer. Absolute minimum is 0, the maximum is 255.
* The dimmer is updating values (about) every half second. The step size determines how fast dimming is.

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
