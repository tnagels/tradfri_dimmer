#Appdeamon app to use Ikea Tradfri switches as dimmers
_Based on a Gist by Claudio Bartoli_

A lot of work still needs to be done as the code is not very nice, still working on it.

```yaml
---
hello_world:
  module: hello
  class: HelloWorld
remote_bureau_brightness:
  module: tradfri
  class: TradfriRemoteDimmer
  lights:
    - light.pendel_bureau
  remote:
    id: tradfri_remote_control
    type: ROUND
  dimmer:
    step: 10
    min: 0
    max: 255
```
