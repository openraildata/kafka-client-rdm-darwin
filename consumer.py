#!/usr/bin/env python3
#
# National Rail Open Data client demonstrator
# Copyright (C)2024-2026 OpenTrainTimes Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import confluent_kafka as kafka
import logging
import json

logging.basicConfig(format='%(asctime)s %(levelname)s\t%(message)s', level=logging.INFO)

BOOTSTRAP_SERVERS = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
GROUP_ID = ''
TOPIC = ''

if BOOTSTRAP_SERVERS == '' or CONSUMER_KEY == '' or CONSUMER_SECRET == '' or TOPIC == '':
    logging.error("Credentials not set - please set BOOTSTRAP_SERVERS, CONSUMER_KEY and CONSUMER_SECRET to the values shown in the RDM")
    exit(1)

if GROUP_ID == '':
    logging.error("Group ID not set - please set GROUP_ID to a unique identifier for this client")
    exit(1)

config = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'sasl.username': CONSUMER_KEY,
    'sasl.password': CONSUMER_SECRET,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest',
}

consumer = kafka.Consumer(config)

topic = TOPIC
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=10)
        if msg is None:
            logging.info("Waiting")
        elif msg.error():
            logging.error(msg.error())
        else:
            parsed_msg = msg.value().decode('utf-8')
            obj = json.loads(parsed_msg)
            payload = json.loads(obj['bytes'])
            logging.info(payload)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
