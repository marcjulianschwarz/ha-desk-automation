# ESP8266 Height-Adjustable Desk Control with Home Assistant Integration

## Project Overview

The goal of this project is to control a height-adjustable desk from a Home Assistant button.

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

The instructions contain steps that permanently alter parts of the desk. If not followed correctly they CAN damage the desk controller, engine and other parts on and around the desk.
Make sure to remove any items on, around and under the desk before performing the steps.
Do NOT make any changes on parts that run high voltages. Always check the components with a multimeter before working on them.

## Step-by-Step Guide

### The Desk

![](/docs/media/desk-diag.png)

#### Automating a Button Click

![](/docs/media/desk-relay-diag.png)

#### Controlling the Relays

![](/docs/media/desk-controller-diag.png)

### Programming the Controller


[esp8266.ino](/esp8266.ino)



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

