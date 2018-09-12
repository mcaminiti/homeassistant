# Home Assistant
[Home Assistant](https://home-assistant.io) configuration with home automations.

Home Assistant Version: 0.77.3

# Overview
I utilize Home Assistant to bridge and automate all my home automation products.  It was quickly realized as I expanded beyond some smart bulbs and a Wink hub, that nothing integrated into a single system for control, automation, and communication.  Home Assistant originally was run on a Raspberry Pi 3 but I have since moved it to run as a docker container leveraging a MySQL docker backend.  Those looking to start out with Home Assistant should leverage a Raspberry Pi 3 and hass.io image to get started very simply.  

My configuration started from an early version of geekofweek's configuration and much of the automation and config is pulled from examples in his configuration.  Home Assistant has many example configurations to leverage and I have published my configuration to share or reference for others.

## Automation Overview
Typical Automations in use include
- Turn on / off outside lights at sunset
- Turn on / off pantry light when door opens / closes
- Turn off lights after no activity / motion
- Grouping of lights for use with Alexa for commands
- Perform actions based on people leaving home / arriving home
- Update location for user based on geolocation zones (Work, School, Church, Home)
- Enable holiday color lights on outside lights
- Send Text notification and flash lights if water detected in basement
- Send Text notification and flash lights if CO / Smoke detectors go off
- Send alert if Eth miner hashrate drops
- Send alert if power is lost at the house
- Enhance security system through extra sensors and motion reading
- Send alert if auxiliary / emergency heat is activated


# Devices

## Hubs

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Phillips Hue Hub v2](https://amzn.to/2Bu9BLz) | 1 | Ethernet | [Philips Hue](https://www.home-assistant.io/components/hue/) | Used to control Phillips Hue Color, Lux, and White bulbs |
| [Wink Hub v1](https://amzn.to/2ByrGIk) | 1 | Wi-Fi | [Wink](https://www.home-assistant.io/components/wink/) | Used as a dumb hub to connect various Z-Wave and Lutron devices. No Wink Robots or schedules being utilized|

Relevant hub configurations can be found within [configuration.yaml](https://github.com/mcaminiti/homeassistant/blob/master/configuration.yaml)
Phillips Hue hub connected via home-assistant integrations.
Wink hub connected with developer API account.

## Lighting

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue White and Color Ambiance v1/v2](https://amzn.to/2MnNQlH) | 8 | Ethernet | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Color changing smart bulbs|
| [Philips Hue White / Lux White](https://amzn.to/2MBBq9d) | 6 | Hue Hub (Zigbee)| [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Non color changing smart bulbs / Lux changes shades of white|
| [Lutron Caseta Wireless Dimmer](https://amzn.to/2NahiI2) | 1 | Wink Hub (Z-Wave)| [Wink Light](https://www.home-assistant.io/components/light.wink/) | Smart dimmer switches that do not require a neutral wire|
| [Leviton Decora Smart Switch](https://amzn.to/2BwRODk) | 1 | Wink Hub (Z-Wave)| [Wink Light](https://www.home-assistant.io/components/light.wink/) | Smart switches that require a neutral wire. No dimming but classic rocker decora style.|

Lights are grouped via [light_group.yaml](https://github.com/mcaminiti/homeassistant/blob/master/light_group.yaml)

## Climate

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ecobee 3](https://amzn.to/2wgmZgp) | 1 | Wi-Fi | [ecobee](https://www.home-assistant.io/components/ecobee/) / [Ecobee Thermostat](https://www.home-assistant.io/components/climate.ecobee/) | Used as primary thermostat for Waterfurnace geothermal system with Auxilary Heat System |
| [Ecobee Room Sensor](https://amzn.to/2MNGS96) | 3 | Ecobee3 | [Ecobee Binary Sensor](https://www.home-assistant.io/components/binary_sensor.ecobee/) | Provides room temperature and room occupancy.|

## Security

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [GoControl Door/Window/Motion Sensor](https://amzn.to/2MJoWft) | 3 | Wink Hub (Z-Wave) | [Wink Binary Sensor](https://www.home-assistant.io/components/binary_sensor.wink/) | Door sensors to detect if doors have been opened / closed. Motion sensor reports temperature and motion. |
| [Eyez-On Envisalink Security Interface](https://amzn.to/2LaFp7P) | 1 | Ethernet | [Envisalink](https://www.home-assistant.io/components/envisalink/) | Security Inteface to connect DSC wired alarm panel to Home Assistant. |

## Media

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Apple TV 4](https://amzn.to/2MG69Sj) | 1 | Wi-Fi | [Apple TV](https://www.home-assistant.io/components/apple_tv/) | Used for media playback on TVs |
| [Apple TV 3](https://amzn.to/2MG69Sj) | 1 | Wi-Fi | [Apple TV](https://www.home-assistant.io/components/apple_tv/) | Used for media playback on TVs |
| [Sonos Play:1](https://amzn.to/2N7ZGwD) | 1 | Wi-Fi | [Sonos](https://www.home-assistant.io/components/media_player.sonos/) | Audio playback |
| [Logitech Harmony Hub](https://amzn.to/2Msld6W) | 1 | Wi-Fi | [Harmony Hub Remote](https://www.home-assistant.io/components/remote.harmony/) | Controls various AV equipment and other devices that utilize infrared remotes |
| [Plex Media Server](https://plex.tv) | 1 | Ethernet | [Plex](https://www.home-assistant.io/components/media_player.plex) / [Plex Activity Monitor](https://www.home-assistant.io/components/sensor.plex/) |  Media Server|  

## Sensors

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Aeon Labs Water Sensor](https://amzn.to/2PsvDkA) | 1 | Wink Hub (Z-Wave) | [Wink Binary Sensor](https://www.home-assistant.io/components/binary_sensor.wink/) | Water sensors used to detect water in basement as a preventive measure |
| [Nest Protect v2 Wired](https://amzn.to/2Pn3sDT) | 2 | Wi-Fi | [Nest](https://www.home-assistant.io/components/nest/) | Smoke Alarm and CO Alarm. |

## Vacuum

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [iRobot Roomba 980](https://amzn.to/2C3XF3y) | 1 | Wi-Fi | [iRobot Roomba](https://www.home-assistant.io/components/vacuum.roomba/)| Working to automate schedule based on presence detection |

All Roomba related automations can be found in [roomba.yaml]( https://github.com/mcaminiti/homeassistant/blob/master/automation/roomba.yaml)

## Cameras

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ring Video Doorbell](https://amzn.to/2ByP7kL) | 1 | Wi-Fi | [Ring](https://www.home-assistant.io/components/ring/) / [Ring Binary Sensor](https://www.home-assistant.io/components/binary_sensor.ring/) | Automated around binary sensors via motion or doorbell button press |
| [Ubiquiti UVC-G3 UniFi Video Camera](https://amzn.to/2PtY2XF) | 2 | Ethernet | [UniFi Video Camera](https://www.home-assistant.io/components/camera.uvc/) | 1080p POE Camera. NVR storage on QNAP NAS. New camera system replacing QT analog system. |

## Network

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ubiquiti Networks Unifi Security Gateway (USG)](https://amzn.to/2NadtTt) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Router. Presence detection for devices |
| [Ubiquiti Networks UniFi Switch - 24 Ports (US-24-250W)](https://amzn.to/2Pv4X2M) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Switch. Presence detection devices |
| [Ubiquiti Networks Unifi AP PRO (UAP-AC-PRO-US)](https://amzn.to/2MLV7Lw) | 3 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Wireless Access Point for interior coverage. Presence detection for devices. |

## Other Hardware

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [QNAP TS-451+](https://amzn.to/2o2bdCM) | 1 | Ethernet | [QNAP Sensor](https://www.home-assistant.io/components/sensor.qnap/)| Main storage array. Docker Containers and Plex media server run off this device. Configured with 3x [WD Red Pro 3TB NAS Hard Disk Drives](https://amzn.to/2PwQ8Ne) |
| [CyberPower CP1350AVRLCD Intelligent LCD UPS System, 1350VA/815W](https://amzn.to/2wcuINx) | 1 | USB / Ethernet | [NUT Sensor](https://www.home-assistant.io/components/sensor.nut/)| Primary Uninterruptible Power Supply (UPS). Connected via the NUT component utlizing the QNAP NAS native UPS server component |

## Software

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [iOS App](https://itunes.apple.com/us/app/home-assistant-open-source-home-automation/id1099568401?mt=8) | 2 | NA | [iOS](https://www.home-assistant.io/docs/ecosystem/ios/)| Used as Home Assistant interface on mobile devices, not actively using for presence detection |
| [Locative iOS App](https://itunes.apple.com/us/app/locative/id725198453?mt=8) | 2 | NA | [Locative](https://www.home-assistant.io/components/device_tracker.locative/) | Primary method of presence detection. App is no longer under active development but has been the most reliable solution with no battery impact |
| [AWS SNS](https://aws.amazon.com/sns/) | 2 | NA | [AWS SNS](https://www.home-assistant.io/components/notify.aws_sns/) | Primary method of text notification for emergency alerting. SNS queues are subscribed by phones that require notification. |
| [Docker](https://hub.docker.com/r/homeassistant/home-assistant/) | 1 | Ethernet | [Installation on Docker](https://www.home-assistant.io/docs/installation/docker/) | Home Assistant install runs as a Docker Container utilizing MySQL docker database |
| [Pi-hole](https://pi-hole.net) | 2 | Ethernet | [Pi-Hole Sensor](https://www.home-assistant.io/components/sensor.pi_hole/) | Ad blocking. Primary instance runs within a Docker container and the secondary runs on a [Raspberry-pi 3](https://amzn.to/2wkqwu7) |
| [Home Assistant Management Tool](https://github.com/geekofweek/homeassistant/blob/master/tools/ha-mgmt-docker.sh) | 1 | Ethernet | NA | Custom Shell script for managing Home Assistant.  Modified from geekofweek version found here. |



