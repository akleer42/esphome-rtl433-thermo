# esphome-rtl433-thermo
This is an attemp to create a Home Assistant ESPHhome component that is able to receive data from a 433Mhz sensor

## Supported devices
Tested only with a pair of ORIA Fridge Thermometers. They seem to be compatible with LaCrosse TX141-Bv2 as found in rtl_433_ESP.
As Receiver/Tranceiver a TI CC1101 was used.

**Note**: Additional sensors could be added with only minor modifications.

## Building the Receiver
### Needed Material
- ESP32 Board (e.g. AZDelivery ESP32 NodeMCU Module WLAN WiFi Dev Kit C V2 - [Link](https://www.az-delivery.de/en/products/esp32-developmentboard))
- TI CC1101 based breakout board for 433MhZ with Antenna (e.g. EBYTE E07-M1101D-TH 433Mhz)
- a few Wires

### Wiring

## Home Assistant / ESPHome configuration

The following yaml lines need to be present (if not added) to your ESPHome configuration file:

```
esphome:
  name: espdev
  friendly_name: espdev
  libraries:
    - SPI
    - rtl_433_ESP=https://github.com/NorthernMan54/rtl_433_ESP.git
    - RadioLib@6.1.0
    - ArduinoJson@7.0
  platformio_options:
    lib_ldf_mode: "chain+"
    build_flags:
      - '-DRF_CC1101="CC1101"'
      - '-DRF_MODULE_FREQUENCY=433.92'
      - '-DRF_MODULE_SCK=18'
      - '-DRF_MODULE_MISO=19'
      - '-DRF_MODULE_MOSI=23'
      - '-DRF_MODULE_CS=5'
      - '-DRF_MODULE_GDO0=13'
      - '-DRF_MODULE_GDO2=12'
      - '-DLOG_LEVEL=LOG_LEVEL_TRACE'

esp32:
  board: esp32dev
  framework:
    type: arduino

```
- **libraries** specifies the dependencies needed to build the component
- **platformio_options** specifies the definitions to configure the component (mainly HW related)

```
external_components:
  - source:
      type: git
      url: https://github.com/akleer42/esphome-rtl433-thermo
    components: [rtl433_thermo]

sensor:
  - platform: rtl433_thermo
    ch1_temperature:
      name: "RTL433 Sensor CH1 Temperature"
    ch1_battery_level:
      name: "RTL433 Sensor CH1 Battery"
    ch1_signal_strength:
      name: "RTL433 Sensor CH1 Signal"
    ch2_temperature:
      name: "RTL433 Sensor CH2 Temperature"
    ch2_battery_level:
      name: "RTL433 Sensor CH2 Battery"
    ch2_signal_strength:
      name: "RTL433 Sensor CH2 Signal"
```
- **external_components** specifies how to find the component. The most convenient option is to use it directly from github
- **sensor** the definition of the sensor device and entities.

**Note**: ESPHome does not support multiple devices, therefor definitions for each of the two sensors is needed (as ch1 and ch2)

## Internals
This component is pretty small, as it uses open source libraries
- [rtl_433_ESP](https://github.com/NorthernMan54/rtl_433_ESP) is an attempt to create an Arduino library for use with ESP32 boards with CC1101 or SX127X transceivers with the device decoders from the rtl_433 package.
- [rtl_433](https://github.com/merbanan/rtl_433) is a generic data receiver, mainly for the 433.92 MHz, 868 MHz (SRD), 315 MHz, 345 MHz, and 915 MHz ISM bands. It support several hundreds of devices by providing the receiver and the decoding of the protocol.

Due to the use of rtl_433_ESP, this component **COULD** not only support hundreds of sensor devices, but also CC1101 and SX127X tranceivers.
However only one specific combination is tested and there is currently no support for humidity. Shouldn't be an issue, but I don't own such a device. 
The component can be easility extended to support more devices out of [rtl_433_ESP](https://github.com/NorthernMan54/rtl_433_ESP)'s ''Enabled Device Decoders''.

