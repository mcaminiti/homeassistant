[![GitHub stars](https://img.shields.io/github/stars/mcaminiti/homeassistant.svg?style=plasticr)](https://github.com/mcaminiti/homeassistant/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcaminiti/homeassistant.svg?style=plasticr)](https://github.com/mcaminiti/homeassistant/commits/master)
[![HA Version](https://img.shields.io/badge/Running%20Home%20Assistant-2021.8.8%20-darkblue)](https://github.com/home-assistant/home-assistant/releases/latest)
[![HA Version](https://img.shields.io/badge/Original%20Home%20Assistant-0.21%20-darkblue)](https://github.com/home-assistant/core/releases/0.21)
[![HA Community](https://img.shields.io/badge/HA%20community-forum-orange)](https://community.home-assistant.io/u/mcaminiti/summary)


# Home Assistant
[Home Assistant](https://home-assistant.io) configuration with home automations.

Featured on Example page from https://www.home-assistant.io/cookbook/

Home Assistant Version: 2021.08.8

# Overview
I utilize Home Assistant to bridge and automate all my home automation products.  It was quickly realized as I expanded beyond some smart bulbs and a Wink hub, that nothing integrated into a single system for control, automation, and communication.  Home Assistant originally was run on a Raspberry Pi 3 but I have since moved it to run as a docker container leveraging a Postgresql docker backend.  Those looking to start out with Home Assistant should leverage a Raspberry Pi 4 and hass.io image to get started very simply.

My configuration started from an early version of geekofweek's configuration. Much of the automation and config is pulled from examples in his configuration but customized for my family's needs.  Home Assistant has many example configurations to leverage and I have published my configuration to share or reference for others.

I have expanded my home automation practices to the ESPHome platform to allow power monitoring automations as well as added controls for my Biocube Salt Water Aquarium, Garage Door Controllers, and Power Metering.  I am also utilizing ZWaveJS2MQTT for zwave control.

## Automation Overview
Typical Automations in use include
- Turn on / off outside lights at sunset
- Turn on / off pantry light when door opens / closes
- Turn off lights after no activity / motion
- Alarm notifications when away from home
- Grouping of lights for use with Alexa for commands
- Perform actions based on people leaving home / arriving home
- Update location for user based on geolocation zones (Work, School, Church, Home)
- Enable holiday color lights on outside lights via scenes
- Turn on lights based on motion / ring front door and return to previous theme after
- Send notification and flash lights if water detected in basement
- Send notification and flash lights if water detected by washing machine / Kitchen Sink
- Cut power to washing machine if water detected by washing machine
- Send notification and flash lights if CO / Smoke detectors go off
- Send alert if power is lost at the house
- Enhance security system through extra sensors and motion reading
- Send alert if auxiliary / emergency heat is activated
- Send long term data to InfluxDB for Grafana configuration
- Use Lutron Pico Remotes to enable Hue Lights and other automations
- Use ESPHome device to energy monitor circuits in the house
- Use EPSHome device for Garage Door Open/Close and state sensors
- Monitor Fish Aquarium (Biocube) power usage
- Alert for aquarium problems (heater running long / pump not running) 
- Change Ecobee mode when fireplace running

# Menu
| [Hubs](#hubs) | [Lighting and Switches](#lighting) | [Climate](#climate)| [Outlets](#outlets) | [Security](#security) | [Voice Assistant](#voice) | [Media](#media) | [Sensors](#sensors) | [Cameras](#cameras) | [Garage](#garage) | [Vacuum](#vacuum) | [Shades](#shades) | [Network](#network) | [Other Hardware](#other)| [Software](#software) | [Retired Devices](#retired)  | [Screenshots](#screenshots) |

# Devices

## Hubs
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Phillips Hue Hub v2](https://amzn.to/2HnWMDV) | 1 | Ethernet | [Philips Hue](https://www.home-assistant.io/components/hue/) | Used to control Phillips Hue Color, Lux, and White bulbs |
| [Aeotec Z‐Stick Gen5 USB Controller](https://www.amazon.com/dp/B089GSFKYW/ref=cm_sw_em_r_mt_dp_CM97863J5NH71ZEXV8SG) | 1 | USB | [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/) | ZWave Controller USB Connected to NUC Server running ZwaveJS2MQTT.|
| [Lutron Caseta Pro](https://www.amazon.com/Lutron-Caseta-L-BDGPRO2-WH-SmartBridge-Programmed/dp/B00Z8AXQCQ/) | 1 | Ethernet | [CUSTOM - Lutron Caseta Pro](https://github.com/jhanssen/home-assistant/tree/caseta-0.40) | Lutron Smart bridge Pro 2 for controlling local access to Lutron dimmers and devices|


Relevant hub configurations can be found within [configuration.yaml](https://github.com/mcaminiti/homeassistant/blob/master/configuration.yaml)
Phillips Hue hub connected via home-assistant integrations.
ZWaveJS2MQTT running on docker image using websocket to Home Assistant for integration.
Lutron connected via local controls on Custom Componant

## Lighting and Switches
| [Go to Menu](#menu) |
| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue White and Color Ambiance v1/v2](https://amzn.to/2ToXUyo) | 10 | Ethernet | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Color changing smart bulbs|
| [Philips Hue White / Lux White](https://amzn.to/2UrOE9d) | 7 | Hue Hub (Zigbee)| [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Non color changing smart bulbs / Lux changes shades of white|
| [Philips Hue White & Color Ambiance Outdoor](https://amzn.to/2tZyEPU) | 7 | Hue Hub (Zigbee)| [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | 2 Starter Sets of Lily Outdoor Spots|
| [Wiz Color and Tunable White Can Light](https://www.homedepot.com/p/Philips-Color-and-Tunable-White-5-6-in-LED-65W-Equivalent-Dimmable-Smart-Wi-Fi-Wiz-Connected-Recessed-Downlight-Kit-555623/310289033) | 21 | HACS - Wiz| [Wiz Custom Componant](https://github.com/sbidy/wiz_light) | Basement can lights |
| [Lutron Caseta Wireless Dimmer](https://amzn.to/2EXtsCH) | 5 | Lutron Caseta | [Lutron Caseta](https://www.home-assistant.io/components/lutron_caseta/) | Smart dimmer switches that do not require a neutral wire|
| [Lutron Caseta Fan Control](https://www.amazon.com/Lutron-Wireless-Single-Pole-PD-FSQN-WH-Assistant/dp/B07N1GXM38/) | 5 | Lutron Caseta | [Lutron Caseta](https://www.home-assistant.io/components/lutron_caseta/) | Fan control via Custom Componant|
| [Leviton Decora Smart Switch](https://amzn.to/2UtKGN0) | 1 | Z-Wave | [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/)  | Smart switches that require a neutral wire. No dimming but classic rocker decora style.|
| [Zooz Switch ZEN26 S2 Dimmer](https://www.amazon.com/dp/B07K37BNMC/ref=cm_sw_em_r_mt_dp_U_fXOgEbTQFG38M) | 2 | [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/)  | Smart switches as z-wave plus.  |

Lights are grouped via [light_group.yaml](https://github.com/mcaminiti/homeassistant/blob/master/light_group.yaml)
Fans are defined in HACS custom componant and defined in [configuration.yaml](https://github.com/mcaminiti/homeassistant/blob/master/configuration.yaml)

## Climate
| [Go to Menu](#menu) |
| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ecobee 3](https://amzn.to/2VQf7xt) | 1 | Wi-Fi | [ecobee](https://www.home-assistant.io/components/ecobee/) / [Ecobee Thermostat](https://www.home-assistant.io/components/climate.ecobee/) | Used as primary thermostat for Waterfurnace geothermal system with Auxilary Heat System |
| [Ecobee Room Sensor](https://amzn.to/2EZCf6Z) | 3 | Ecobee3 | [Ecobee Binary Sensor](https://www.home-assistant.io/components/binary_sensor.ecobee/) | Provides room temperature and room occupancy.|

## Outlets
| [Go to Menu](#menu) |
| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [WeMo Insight Smart Plug with Energy Monitoring](https://amzn.to/2VHBrJi) | 3 | WeMo | [WeMo Componant](https://www.home-assistant.io/components/wemo/) | WeMo Smart Outlet with Energy Monitoring |
| [WeMo Mini Smart Plug](https://amzn.to/2VPV8yV) | 4 | WeMo | [WeMo Componant](https://www.home-assistant.io/components/wemo/) | WeMo Smart Outlet |
| [TP-Link Kasa Outdoor Outlet - KP400](https://www.amazon.com/Kasa-Smart-Outlet-Outdoor-TP-Link/dp/B07M6RS2LC) | 2 | TP-Link | [TP-Link Componant](https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/tplink/) | TPLink Smart Outlet |
| [Zooz Power Switch ZEN15](https://amzn.to/2WRPeiv) | 1 | Z-Wave | [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/)  | Smart outlet utilized to monitor fireplace status|

## Security
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [GoControl Door/Window/Motion Sensor](https://amzn.to/2VLQrG8) | 3 |  Z-Wave | [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/)  | Door sensors to detect if doors have been opened / closed. Motion sensor reports temperature and motion. |
| [Eyez-On Envisalink Security Interface](https://amzn.to/2tY9AZy) | 1 | Ethernet | [Envisalink](https://www.home-assistant.io/components/envisalink/) | Security Inteface to connect DSC wired alarm panel to Home Assistant. |

## Voice Control
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Amazon Polly](https://aws.amazon.com/polly/) | 1 | Integration| [Amazon Polly](https://www.home-assistant.io/integrations/amazon_polly/) | Text To Speech (TTS) for notifications and alerts |
| [Echo Show 5](https://www.amazon.com/Introducing-Echo-Show-Compact-Charcoal/dp/B07HZLHPKP/ref=sr_1_3) | 1 | Home Assistant Cloud  [Home Assistant Cloud ](https://www.home-assistant.io/cloud/) | Voice Assistant integrated with Home Assistant Cloud |
| [Echo Dot 3rd gen](https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=sr_1_1) | 5 | Home Assistant Cloud  [Home Assistant Cloud ](https://www.home-assistant.io/cloud/) | Voice Assistant integrated with Home Assistant Cloud |
| [Echo 1st gen](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-Alexa-Black/dp/B00X4WHP5E/ref=sr_1_1) | 1 | Home Assistant Cloud  [Home Assistant Cloud ](https://www.home-assistant.io/cloud/) | Voice Assistant integrated with Home Assistant Cloud |

## Media
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Apple TV 4](https://amzn.to/2UrM3fp) | 3 | Wi-Fi | [Apple TV](https://www.home-assistant.io/components/apple_tv/) | Used for media playback on TVs |
| [Sonos Play:1](https://amzn.to/2STD1pE) | 1 | Wi-Fi | [Sonos](https://www.home-assistant.io/components/media_player.sonos/) | Audio playback |
| [Logitech Harmony Hub](https://amzn.to/2UtKNrU) | 2 | Wi-Fi | [Harmony Hub Remote](https://www.home-assistant.io/components/remote.harmony/) | Controls various AV equipment and other devices that utilize infrared remotes |
| [Plex Media Server](https://plex.tv) | 1 | Ethernet | [Plex](https://www.home-assistant.io/components/media_player.plex) / [Plex Activity Monitor](https://www.home-assistant.io/components/sensor.plex/) |  Media Server|  

## Sensors
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Aeon Labs Water Sensor](https://amzn.to/2NTptcR) | 1 | Z-Wave |  [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/) | Water sensors used to detect water in basement as a preventive measure |
| [Dome Leak Sensor](https://amzn.to/2VGlq6C) | 6 | Z-Wave|  [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/) | Water sensor used to detect water in near washing machine and kitchen sink as a preventive measure |
| [Zooz 4 in 1 Sensor](https://www.amazon.com/ZOOZ-Z-Wave-Sensor-Temperature-Humidity/dp/B01AKSO80O/ref=sr_1_2) | 2 | Z-Wave|  [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/) | Motion, temperature, light, and humidity sensor |
| [Go Control Door Sensor](https://www.gocontrol.com/detail.php?productId=14) | 3 | Z-Wave|  [ZWaveJS2MQTT](https://www.home-assistant.io/integrations/zwave_js/) | Door sensor for closet and pantry doors |
| [Nest Protect v2 Wired](https://amzn.to/2SSA0Gj) | 4 | Wi-Fi | [Nest](https://www.home-assistant.io/components/nest/) | Smoke Alarm and CO Alarm. |
| [ESPHome - ESP32](https://github.com/mcaminiti/esphome-energy6channel) | 1 | Wi-Fi | [ESPHome](https://www.home-assistant.io/integrations/esphome/) | 6 Channel Energy Monitor |
| [ESPHome - ESP32](https://github.com/mcaminiti/) | 2 | Wi-Fi | [ESPHome](https://www.home-assistant.io/integrations/esphome/) | Temperature Sensor for Aquariums |

## Cameras
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ring Video Doorbell - 3 Plus](https://www.amazon.com/Ring-Video-Doorbell-3-Plus/dp/B07WLP395R/ref=sr_1_3) | 1 | Wi-Fi | [Ring](https://www.home-assistant.io/components/ring/) / [Ring Binary Sensor](https://www.home-assistant.io/components/binary_sensor.ring/) | Automated around binary sensors via motion or doorbell button press |
| [Ubiquiti UVC-G3 UniFi Video Camera](https://amzn.to/2NQkXvW) | 4 | Ethernet | [Camera FFMPEG](https://www.home-assistant.io/components/camera.ffmpeg/) | 1080p POE Camera. Unifi Protect on Cloud Key 2 Plus. New camera system replacing QT analog system. |
| [Ubiquiti UniFi Video G3 Flex Camera](https://amzn.to/2NV5s64) | 1 | Ethernet | [Camera FFMPEG](https://www.home-assistant.io/components/camera.ffmpeg/) | 1080p POE Camera. Unifi Protect on Cloud Key 2 Plus. |
| [Ubiquiti UniFi Video G3 Instant Camera](https://store.ui.com/collections/unifi-protect-cameras/products/unifi-protect-g3-instant-camera) | 2 | Wi-Fi | [Camera FFMPEG](https://www.home-assistant.io/components/camera.ffmpeg/) | 1080p Wireless Camera. Unifi Protect on Cloud Key 2 Plus. |

## Garage
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [ESPHome - ESP32](https://github.com/mcaminiti/esphome-garage-door) | 1 | Wi-Fi | [ESPHome](https://www.home-assistant.io/integrations/esphome/) | 4 Relay / 4 Inputs for control of 2 Garage Doors |

## Vacuum
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [iRobot Roomba i7](https://amzn.to/2VGKZEu) | 1 | Wi-Fi | [iRobot Roomba](https://www.home-assistant.io/components/vacuum.roomba/)| Working to automate schedule based on presence detection | All Roomba related automations can be found in [roomba.yaml]( https://github.com/mcaminiti/homeassistant/blob/master/automation/roomba.yaml)
| [iRobot Roomba i6+](https://amzn.to/2VGKZEu) | 1 | Wi-Fi | [iRobot Roomba](https://www.home-assistant.io/components/vacuum.roomba/)| Working to automate schedule based on presence detection | All Roomba related automations can be found in [roomba.yaml]( https://github.com/mcaminiti/homeassistant/blob/master/automation/roomba.yaml)

## Shades
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ikea Fyrtur Blackout Roller Blind ](https://www.ikea.com/us/en/p/fyrtur-blackout-roller-blind-wireless-battery-operated-gray-90417462/) | 20 | Zigbee - Ikea| [Ikea Tradfri](https://www.home-assistant.io/integrations/tradfri/)| Automated shades for every room
All grouped via [cover.yaml](https://github.com/mcaminiti/homeassistant/blob/master/cover.yaml)

## Network
| [Go to Menu](#menu) |

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ubiquiti Networks Unifi Security Gateway (USG)](https://amzn.to/2Unk6oS) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Router. Presence detection for devices |
| [Ubiquiti Networks UniFi Switch - 24 Ports (US-24-250W)](https://amzn.to/2To2kp7) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Switch. Presence detection devices |
| [Ubiquiti Networks Unifi AP PRO (UAP-AC-PRO-US)](https://amzn.to/2XPpiUT) | 3 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Wireless Access Point for interior coverage. Presence detection for devices. |
| [Ubiquiti Networks Unifi Cloud Key 2 Plus](https://amzn.to/2VzjW1s) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Unifi Controller and Unifi Protect NVR. Cameras feed via RTSP to HA https://amzn.to/2VzjW1s. |

## Other Hardware

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [QNAP TS-451+](https://amzn.to/2tX6VPS) | 1 | Ethernet | [QNAP Sensor](https://www.home-assistant.io/components/sensor.qnap/)| Main storage array. Docker Containers and Plex media server run off this device. Configured with 3x [WD Red Pro 3TB NAS Hard Disk Drives](https://amzn.to/2tXKlGY) |
| [CyberPower CP1350AVRLCD Intelligent LCD UPS System, 1350VA/815W](https://amzn.to/2CbFXst) | 1 | USB / Ethernet | [NUT Sensor](https://www.home-assistant.io/components/sensor.nut/)| Primary Uninterruptible Power Supply (UPS). Connected via the NUT component utlizing the QNAP NAS native UPS server component |
| [NUC 10 Performance Kit](https://www.intel.com/content/www/us/en/products/sku/189239/intel-nuc-10-performance-kit-nuc10i5fnh/specifications.html) | 1 | Ethernet || Main server running docker containers, plex, and zwavejs2mqtt|

## Software

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [iOS App](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) | 4 | NA | [iOS](https://www.home-assistant.io/docs/ecosystem/ios/)| Used as Home Assistant interface on mobile devices and for presence detection |
| [Docker](https://hub.docker.com/r/homeassistant/home-assistant/) | 1 | Ethernet | [Installation on Docker](https://www.home-assistant.io/docs/installation/docker/) | Home Assistant install runs as a Docker Container utilizing Postgresql docker database |
| [Pi-hole](https://pi-hole.net) | 2 | Ethernet | [Pi-Hole Sensor](https://www.home-assistant.io/components/sensor.pi_hole/) | Ad blocking. Primary instance runs within a Docker container and the secondary runs on a 2 docker containers | 
| [Home Assistant Management Tool](https://github.com/geekofweek/homeassistant/blob/master/tools/ha-mgmt-docker.sh) | 1 | Ethernet | NA | Custom Shell script for managing Home Assistant.  Modified from geekofweek version found here. |

## Retired Devices

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [VeraPlus](https://amzn.to/2Y0ZiFl) | 1 | Ethernet | [Vera](https://www.home-assistant.io/components/vera/) | Migrated to ZwaveJS2MQTT for Zwave control. |
| [Wink Hub v1](https://amzn.to/2VJHixP) | 1 | Wi-Fi | [Wink](https://www.home-assistant.io/components/wink/) | Decommissioned as a device for smart controls.  Replaced with Vera for zwave and Lutron Caseta for Lutron Switches|
| [Tuya Compatible Plug](https://www.amazon.com/Gosund-Extender-Independently-Together-Required/dp/B07F58N32V/ref=sr_1_26?keywords=tuya+outlet&qid=1576247706&sr=8-26) | 1 | Tuya | [Tuya Componant](https://www.home-assistant.io/integrations/tuya/) | Tuya Smart Outlet - retired for lack reliability and ease. Might revisit with Tuya updates |
| [Zooz Power Strip ZEN20 v2 ](https://www.amazon.com/Z-Wave-Power-Energy-Monitoring-SmartThings/dp/B01HAQHQ5I/ref=asc_df_B01HAQHQ5I) | 1 | Vera (Z-Wave)| [Vera](https://www.home-assistant.io/components/vera/) | Smart power strip allowing for power controls and energy monitoring. Retired as it died within the first year. Stability issues and unreliable with load. | 

##Screenshots
![UI](images/ha-1.png?raw=true "Home Page")
![UI](images/ha-2.png?raw=true "Sensors")
![UI](images/ha-3.png?raw=true "Temp and Weather Sensors")
![UI](images/ha-4.png?raw=true "System Monitor")
![UI](images/ha-7.png?raw=true "Garage / Golf Cart")
![UI](images/ha-6.png?raw=true "Automation Disable / Enable")
