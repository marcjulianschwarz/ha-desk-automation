#!/path/to/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Raise Desk
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⬆️
# @raycast.packageName Desk

# Documentation:
# @raycast.description Raises the desk.
# @raycast.author Marc Julian Schwarz
# @raycast.authorURL https://www.github.com/marcjulianschwarz

import paho.mqtt.publish as publish

publish.single(
    "desk",
    "up",
    hostname="<your-mqtt-hostname>",
    auth={"username": "<your-mqtt-username>", "password": "<your-mqtt-password>"},
)

print("Raising the desk...")
