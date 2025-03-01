#pragma once

#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"

namespace esphome {
namespace rtl433_thermo {

#define NUM_CHANNELS  2

class RTL433ThermoSensor : public sensor::Sensor, public Component {

  public:
    sensor::Sensor *temperature_sensor_[NUM_CHANNELS]{nullptr, nullptr};
    sensor::Sensor *battery_sensor_[NUM_CHANNELS]{nullptr, nullptr};
    sensor::Sensor *signal_sensor_[NUM_CHANNELS]{nullptr, nullptr};
    void set_temperature_sensor(sensor::Sensor *temperature_sensor, int channel) { temperature_sensor_[channel - 1] = temperature_sensor; }
    void set_battery_sensor(sensor::Sensor *battery_sensor, int channel) { battery_sensor_[channel - 1] = battery_sensor; }
    void set_signal_sensor(sensor::Sensor *signal_sensor, int channel) { signal_sensor_[channel - 1] = signal_sensor; }

    void setup() override;
    void loop() override;
    void update() override;
    void dump_config() override;

  protected:
    /// Read the temperature value and store the calculated ambient temperature in t_fine.
    //float read_temperature_(const uint8_t *data, int32_t *t_fine);

#define JSON_MSG_BUFFER 512
    char messageBuffer[JSON_MSG_BUFFER];

    enum ErrorCode {
      NONE = 0,
      COMMUNICATION_FAILED,
      WRONG_CHIP_ID,
    } error_code_{NONE};

};

}  // namespace rtl433_thermo
}  // namespace esphome
