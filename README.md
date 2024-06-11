# Cute Bot Pin Descriptions

The Cute Bot smart car uses various pins on the micro:bit to interface with its sensors, motors, and other components. Here is a detailed breakdown of the pin assignments for each component:

### Micro:bit Pin Assignments

1. **Ultrasonic Sensor (HC-SR04)**
   - **Trigger Pin**: P1
   - **Echo Pin**: P2

2. **Infrared Probes (Line-Tracking Sensors)**
   - **Left Sensor**: P13
   - **Right Sensor**: P14

3. **RGB LED Headlights**
   - **Headlights**: P15

4. **Infrared Control**
   - **IR Receiver**: P16

5. **IIC Port**
   - **SDA**: P19
   - **SCL**: P20

6. **Servo Ports**
   - **Servo 1**: S1
   - **Servo 2**: S2

7. **General Purpose Input/Output (GPIO)**
   - **General GPIO Ports**: P0, P1, P2

### Component Breakdown

- **Ultrasonic Sensor (HC-SR04)**
  - **Pins**: Connects to P1 (Trigger) and P2 (Echo) on the micro:bit.
  - **Function**: Measures distance by emitting ultrasonic waves and calculating the time it takes for the echo to return.

- **RGB LED Headlights**
  - **Pins**: Connects to P15 on the micro:bit.
  - **Function**: Provides colorful lighting effects. Each LED can be individually programmed for different colors.

- **Line-Tracking Sensors**
  - **Pins**: Connects to P13 and P14 on the micro:bit.
  - **Function**: Detects lines on the ground, enabling the Cutebot to follow a path or avoid going off-course.

- **Infrared Control**
  - **Pins**: Connects to P16 on the micro:bit.
  - **Function**: Receives infrared signals from a remote control for remote operation.

- **IIC Port**
  - **Pins**: SDA (P19), SCL (P20)
  - **Function**: IIC communication protocol for connecting additional IIC compatible sensors and modules.

- **Servo Ports**
  - **Pins**: S1, S2
  - **Function**: Connects to servos for controlling additional mechanical components like robotic arms.

- **General GPIO Ports**
  - **Pins**: P0, P1, P2
  - **Function**: General purpose pins that can be used for various inputs and outputs, depending on the project requirements.

---

For more detailed information, you can visit the [Elecfreaks Cutebot page](https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_car.html).
