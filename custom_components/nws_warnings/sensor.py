'''
---------------------------------------------------------
NWS Warnings
---------------------------------------------------------

Version 0.1
Written by Matt REDACTED
https://github.com/mREDACTED/nws_warnings

Forked from VERSION: 0.0.2 of NWS Alerts
Forum: https://community.home-assistant.io/t/severe-weather-alerts-from-the-us-national-weather-service/71853

API Documentation
---------------------------------------------------------
https://www.weather.gov/documentation/services-web-api
---------------------------------------------------------
'''
import requests
import logging
import voluptuous as vol
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, ATTR_ATTRIBUTION
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle


API_ENDPOINT = 'https://api.weather.gov'
USER_AGENT = 'Home Assistant'
MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=1)
_LOGGER = logging.getLogger(__name__)
DEFAULT_NAME = 'NWS Warnings'
DEFAULT_ICON = 'mdi:alert'
CONF_ZONE_ID = 'zone_id'
ZONE_ID = ''

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ZONE_ID): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    name = config.get(CONF_NAME, DEFAULT_NAME)
    zone_id = config.get(CONF_ZONE_ID)
    add_devices([NWSAlertSensor(name, zone_id)])


class NWSAlertSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, name, zone_id):
        """Initialize the sensor."""
        self._name = name
        self._icon = DEFAULT_ICON
        self._state = 0
        self._severe_thunderstorm_warning = 0
        self._winter_storm_warning = 0
        self._severe_thunderstorm_warning_headline = None
        self._winter_storm_warning_headline = None
        self._tornado_watch = 0
        self._tornado_warning = 0
        self._tornado_watch_headline = None
        self._tornado_warning_headline = None
        self._zone_id = zone_id.replace(' ', '')
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Return the icon to use in the frontend, if any."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state message."""
        attributes = {"severe_thunderstorm_warning": self._severe_thunderstorm_warning,
                      "tornado_watch": self._tornado_watch,
                      "tornado_warning": self._tornado_warning,
                      "winter_storm_warning": self._winter_storm_warning,
                      "severe_thunderstorm_warning_headline": self._severe_thunderstorm_warning_headline,
                      "tornado_watch_headline": self._tornado_watch_headline,
                      "tornado_warning_headline": self._tornado_warning_headline,
                      "winter_storm_warning_headline": self._winter_storm_warning_headline
                      }

        return attributes

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        values = self.get_state()
        self._state = values['state']
        self._severe_thunderstorm_warning = values['severe_thunderstorm_warning']
        self._tornado_watch = values['tornado_watch']
        self._tornado_warning = values['tornado_warning']
        self._winter_storm_warning = values['winter_storm_warning']
        self._severe_thunderstorm_warning_headline = values['severe_thunderstorm_warning_headline']
        self._tornado_watch_headline = values['tornado_watch_headline']
        self._tornado_warning_headline = values['tornado_warning_headline']
        self._winter_storm_warning_headline = values['winter_storm_warning_headline']



    def get_state(self):
        values = {'state': 0,
                  'severe_thunderstorm_warning': 0,
                  'tornado_watch': 0,
                  'tornado_warning': 0,
                  'winter_storm_warning': 0,
                  'severe_thunderstorm_warning_headline': None,
                  'tornado_watch_headline': None,
                  'tornado_warning_headline': None,
                  'winter_storm_warning_headline': None
                  }

        headers = {'User-Agent': USER_AGENT,
                   'Accept': 'application/ld+json'
                   }

        url = '%s/alerts/active/count' % API_ENDPOINT
        r = requests.get(url, headers=headers)
        _LOGGER.debug("getting state, %s", url)
        if r.status_code == 200:
            if 'zones' in r.json():
                for zone in self._zone_id.split(','):
                    if zone in r.json()['zones']:
                        values = self.get_alerts()
                        break

        return values

    def get_alerts(self):
        values = {'state': 0,
                  'severe_thunderstorm_warning': 0,
                  'winter_storm_warning': 0,
                  'severe_thunderstorm_warning_headline': None,
                  'winter_storm_warning_headline': None,
                  'tornado_watch': 0,
                  'tornado_warning': 0,
                  'tornado_watch_headline': None,
                  'tornado_warning_headline': None
                  }

        headers = {'User-Agent': USER_AGENT,
                   'Accept': 'application/geo+json'
                   }
        url = '%s/alerts/active?zone=%s' % (API_ENDPOINT, self._zone_id)
        r = requests.get(url, headers=headers)
        _LOGGER.debug("getting alert, %s", url)
        if r.status_code == 200:
            events = []
            headlines = []
            description = ''
            severe_thunderstorm_warning = ''
            winter_storm_warning = ''
            severe_thunderstorm_warning_count = 0
            severe_thunderstorm_warning_headline = ''
            winter_storm_warning_count = 0
            winter_storm_warning_headline = ''
            tornado_watch = ''
            tornado_warning = ''
            tornado_watch_count = 0
            tornado_watch_headline = ''
            tornado_warning_count = 0
            tornado_warning_headline = ''
            alertcount = 0
            eventname = ''
            features = r.json()['features']
            for alert in features:
                event = alert['properties']['event']
                if event == 'Severe Thunderstorm Warning':
                    alertcount = alertcount + 1
                    severe_thunderstorm_warning_count = 1
                    severe_thunderstorm_warning_headline = alert['properties']['headline']
#                    description = alert['properties']['description']
                    eventname = 'Severe Thunderstorm Warning'
                if event == 'Winter Storm Warning':
                    alertcount = alertcount + 1
                    winter_storm_warning_count = 1
                    winter_storm_warning_headline = alert['properties']['headline']
#                    description = alert['properties']['description']
                    eventname = 'Winter Storm Warning'
                if event == 'Tornado Watch':
                    alertcount = alertcount + 1
                    tornado_watch_count = 1
                    tornado_watch_headline = alert['properties']['headline']
#                    description = alert['properties']['description']
                    eventname = 'Tornado Watch'
                if event == 'Tornado Warning':
                    alertcount = alertcount + 1
                    tornado_warning_count = 1
                    tornado_warning_headline = alert['properties']['headline']
#                    description = alert['properties']['description']
                    eventname = 'Tornado Warning'

                if event in events:
                    continue

                values['state'] = alertcount
                values['severe_thunderstorm_warning'] = severe_thunderstorm_warning_count
                values['tornado_watch'] = tornado_watch_count
                values['tornado_warning'] = tornado_warning_count
                values['winter_storm_warning'] = winter_storm_warning_count
                values['severe_thunderstorm_warning_headline'] = severe_thunderstorm_warning_headline
                values['tornado_watch_headline'] = tornado_watch_headline
                values['tornado_warning_headline'] = tornado_warning_headline
                values['winter_storm_warning_headline'] = winter_storm_warning_headline



        return values
