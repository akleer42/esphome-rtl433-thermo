from esphome import automation, core
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    ICON_THERMOMETER,
    ICON_BATTERY,
    ICON_SIGNAL,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_DECIBEL_MILLIWATT
)

AUTO_LOAD = []
DEPENDENCIES = []

CONF_CH1_TEMPERATURE = 'ch1_temperature'
CONF_CH1_BATTERY_LEVEL = 'ch1_battery_level'
CONF_CH1_SIGNAL_STRENGTH = 'ch1_signal_strength'
CONF_CH2_TEMPERATURE = 'ch2_temperature'
CONF_CH2_BATTERY_LEVEL = 'ch2_battery_level'
CONF_CH2_SIGNAL_STRENGTH = 'ch2_signal_strength'

rtl433_thermo_ns = cg.esphome_ns.namespace("rtl433_thermo")
RTL433ThermoSensor = rtl433_thermo_ns.class_(
    "RTL433ThermoSensor", cg.Component#, cg.PollingComponent
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(RTL433ThermoSensor),

            cv.Optional(CONF_CH1_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_THERMOMETER
            ),
            cv.Optional(CONF_CH1_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_BATTERY
            ),
            cv.Optional(CONF_CH1_SIGNAL_STRENGTH): sensor.sensor_schema(
                unit_of_measurement=UNIT_DECIBEL_MILLIWATT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_SIGNAL
            ),

            cv.Optional(CONF_CH2_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_THERMOMETER
            ),
            cv.Optional(CONF_CH2_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_BATTERY
            ),
            cv.Optional(CONF_CH2_SIGNAL_STRENGTH): sensor.sensor_schema(
                unit_of_measurement=UNIT_DECIBEL_MILLIWATT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
                state_class=STATE_CLASS_MEASUREMENT,
                icon=ICON_SIGNAL
            ),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

'''called while building the code. this is the interface between the home assistant yaml configuration and esphome'''
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
 
    if CONF_CH1_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_CH1_TEMPERATURE])
        cg.add(var.set_temperature_sensor(sens, 1))

    if CONF_CH1_BATTERY_LEVEL in config:
        sens = await sensor.new_sensor(config[CONF_CH1_BATTERY_LEVEL])
        cg.add(var.set_battery_sensor(sens, 1))

    if CONF_CH1_SIGNAL_STRENGTH in config:
        sens = await sensor.new_sensor(config[CONF_CH1_SIGNAL_STRENGTH])
        cg.add(var.set_signal_sensor(sens, 1))

    if CONF_CH2_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_CH2_TEMPERATURE])
        cg.add(var.set_temperature_sensor(sens, 2))

    if CONF_CH2_BATTERY_LEVEL in config:
        sens = await sensor.new_sensor(config[CONF_CH2_BATTERY_LEVEL])
        cg.add(var.set_battery_sensor(sens, 2))

    if CONF_CH2_SIGNAL_STRENGTH in config:
        sens = await sensor.new_sensor(config[CONF_CH2_SIGNAL_STRENGTH])
        cg.add(var.set_signal_sensor(sens, 2))
