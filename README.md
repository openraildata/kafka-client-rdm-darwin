RDM Darwin Client
=================

This repository contains a Python 3 example of how to use the Darwin v17 (Staging) messages from Darwin via the Rail
Data Marketplace at the following URL:

* https://raildata.org.uk/dataProduct/P-e8ab4178-93b7-4219-81a9-323eab3b12ba/overview

This code has been tested on Python 3.14.4, but should run on other versions of Python 3.

Configuration
-------------

Once subscribed to the Darwin Real Time Train Information product on the Rail Data Marketplace, use the values in the
following fields to populate the configuration variables:

| Variable          | Value                 |
|-------------------|-----------------------|
| BOOTSTRAP_SERVERS | Kafka boostrap server |
| CONSUMER_KEY      | Consumer username     |
| CONSUMER_SECRET   | Consumer password     |
| GROUP_ID          | Consumer group        |
| TOPIC             | Topic                 |

Running the code
----------------

Install the `confluent_kafka` library by running `pip3 install confluent_kafka`.

The `consumer.py` script will subscribe to the appropriate topic and print messages.

Support
-------

For support and questions with using Darwin, please use the forum at the
following URL:

* https://groups.google.com/group/openraildata-talk
