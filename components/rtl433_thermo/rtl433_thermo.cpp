#include <ArduinoJson.h>

#include "rtl433_thermo.h"
#include "esphome/core/log.h"
#include <rtl_433_ESP.h>

#ifndef RF_MODULE_FREQUENCY
#  define RF_MODULE_FREQUENCY 433.92
#endif

namespace esphome {
namespace rtl433_thermo {

static const char *TAG = "rtl433_thermo.sensor";

// global rf object
rtl_433_ESP rf;
RTL433ThermoSensor *instance = nullptr;

void rtl433_Callback(char* message) {
  ESP_LOGCONFIG(TAG, "callback() Received message %s", message);

  JsonDocument json;
  deserializeJson(json, (const char *)message);

  int cidx = 0;
  if (json.containsKey("channel") && (json["channel"].as<int>() <= NUM_CHANNELS)) {
    cidx = json["channel"].as<int>() - 1;
  }

  if (instance != nullptr) {

    if (instance->temperature_sensor_[cidx] != nullptr && json.containsKey("temperature_C")) {
      instance->temperature_sensor_[cidx]->publish_state(json["temperature_C"].as<float>());
    }

    if (instance->battery_sensor_[cidx] != nullptr && json.containsKey("battery_ok")) {
      instance->battery_sensor_[cidx]->publish_state(json["battery_ok"].as<int>());
    }

    if (instance->signal_sensor_[cidx] != nullptr && json.containsKey("rssi")) {
      instance->signal_sensor_[cidx]->publish_state(json["rssi"].as<int>());
    }
  }
}

/*
 *
 */
void RTL433ThermoSensor::setup() {
  ESP_LOGCONFIG(TAG, "Setting up RF433...");
  instance = this;

  ESP_LOGCONFIG(TAG, "InitReceiver - Receiver GPIO %i RF_MODULE_FREQUENCY %f", RF_MODULE_RECEIVER_GPIO, RF_MODULE_FREQUENCY);
  rf.initReceiver(RF_MODULE_RECEIVER_GPIO, RF_MODULE_FREQUENCY);

  ESP_LOGCONFIG(TAG, "setCallback");
  rf.setCallback(rtl433_Callback, messageBuffer, JSON_MSG_BUFFER);

  ESP_LOGCONFIG(TAG, "enableReceiver");
  rf.enableReceiver();

  ESP_LOGCONFIG(TAG, "getModuleStatus");
  rf.getModuleStatus();

  ESP_LOGCONFIG(TAG, "leaving");
  return;
}

void RTL433ThermoSensor::loop() {
  rf.loop();
}

#if 0
void RTL433ThermoSensor::update() {
  //ESP_LOGCONFIG(TAG, "update() entering");
  //ESP_LOGCONFIG(TAG, "update() leaving");
}
#endif

void RTL433ThermoSensor::dump_config() { 
  ESP_LOGCONFIG(TAG, "dump_config() entering"); 
  ESP_LOGCONFIG(TAG, "dump_config() leaving");
}

}  // namespace rtl433_thermo
}  // namespace esphome
