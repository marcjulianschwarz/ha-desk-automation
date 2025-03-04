# ESP8266 Height-Adjustable Desk Control with Home Assistant Integration

## Project Overview

The goal of this project is to control a height-adjustable desk from a Home Assistant button while still preserving the functionality of the manual button controls on the table itself.

## Prerequisites

These are the exact tools, hardware and software I used. However, you can exchange most components with other similar ones.

### Hardware

- NodeMCU Lua Lolin V3 Module ESP8266 ESP-12F WIFI Development Board with CH340
- At least 8 jumper wires
- One _2-Channel Relay Module 5V with Optocoupler Low-Level Trigger_
- Three _WAGO 221 Terminal Block 3 Connectors_
- USB-A to Micro-USB cable for powering the board and flashing code

### Tools

- Scissors to cut the cable
- Cable Insulation Stripping Tool

### Software

- [Arduino IDE](https://docs.arduino.cc/software/ide/#ide-v2)
- Running [Home Assistant](https://www.home-assistant.io/) instance

## Safety Warnings

The instructions contain steps that permanently alter parts of the desk. If not followed correctly, they **CAN damage** the desk controller, engine and other parts on or around the table.
Make sure to remove any items on, around and under the desk before performing the steps.

The instructions are relatively safe to follow, as they are only dealing with low-voltage parts of the table. Nontheless, be careful and do NOT make any changes on parts that run high voltages. Always check the components with a multimeter before working on them and plug out all cables.

## Step-by-Step Guide

### Understanding the Desk Controls

The desk controls are made up of three cables. The following figures shows a schematic view on those cables. The colors are only for illustrative purposes and might be different for your specific desk.

The green (left) cable connects the controller with the `Raise` button and the blue (right) one with the `Lower` button. One black cable connects both buttons back to the table to form a closed loop that is only interrupted by the open buttons themselves. Pressing a button closes the respective circuit, letting the desk controller know to start the engine for raising or lowering the table.

![](/docs/media/desk-diag.png)

At this point it is quite straightforward to intercept the button presses by directly connecting the green and blue wires with the orange wire. Therefore creating a closed circuit before the button is even reached. The same connection can be done with the blue cable, lowering the table.

### Cut the Cable

To get access to the individual cables the cable running from the button controls to the desk has to be cut and the insulation around them and the individual smaller cables has to be removed for about 1-2cm.

#### Automating a Button Click

![](/docs/media/desk-relay-diag.png)

#### Controlling the Relays

Relays don't do anything on their own. A microcontroller is needed. For example, you can use the NodeMCU ESP8266 development board. The board has to provide power, ground and two data pins. Each data pin controls one of the relays. Now the circuit is completed and the ESP can be programmed.

![](/docs/media/desk-controller-diag.png)

### Programming the Controller

Open [esp8266.ino](/esp8266.ino) in the Arduino IDE and set all configuration variables.

### Home Assistant Setup

#### 1. Install MQTT Broker

- Install [Mosquitto Broker Add-on](https://www.home-assistant.io/integrations/mqtt/)
- Start Add-on with default configuration
- Add new `mqtt` user under `Settings > People` and allow login

#### 2. Add MQTT Integration

- The MQTT integration should appear on `Settings > Devices & services`
- Add the integration
- Here you can try publishing packets to the `desk` topic. Set your payload to `down` or `up`.

#### 3. Add Switch in Home Assistant Configuration
