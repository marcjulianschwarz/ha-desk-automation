#!/path/to/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Lower Desk
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⬇️
# @raycast.packageName Desk

# Documentation:
# @raycast.description Lowers the desk.
# @raycast.author Marc Julian Schwarz
# @raycast.authorURL https://www.github.com/marcjulianschwarz

import paho.mqtt.publish as publish

publish.single(
    "desk",
    "down",
    hostname="<your-mqtt-hostname>",
    auth={"username": "<your-mqtt-username>", "password": "<your-mqtt-password>"},
)

print("Lowering the desk...")
