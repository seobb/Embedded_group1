**EPM104 – Embedded Systems**

**Project 01 – LED blinks for Gyroscope Data in Jetson Nano**

1. **Introduction**

The first project of the Embedded Systems contains 2 main deliverables as one is to modify the code to receive Gyroscope’s roll and pitch data from STM32 board as X and Y of data pair and indicate them using onboard LEDs (codes are given already). Then the data will be transmitted through the USB with the setup of the given STM32 program included with some modification in the code.

The second step is to create a python program inside the Jetson Nano to send commands to STM32 with the LED as to be blinked with the specific conditions. The Jetson Nano requests the gyro data before it sends the command back to STM32. In this project the main requirement is that the LEDs have to be blinked according to the tilt angle of the STM32 board with respect to time.

2. **Overview of the code/project**

The `led.py` script serves as the main component of this project. It begins by establishing a serial connection with the STM32 microcontroller using the PySerial library, allowing bidirectional communication between the Python script and the STM32 board.

Once the serial connection is established, the script enters a continuous loop where it repeatedly sends commands to the STM32 microcontroller to request gyro data. Upon receiving the gyro data, the script processes it to extract X and Y coordinates, which represent the tilt of the device along its axes.

The extracted X and Y coordinates are then analysed to determine the tilt direction of the device. Based on the tilt direction, the script selectively controls LEDs on the STM32 board. For example, if the device is tilted towards the north, LED 0 is turned on; if it's tilted towards the south, LED 4 is activated, and so on.

This process continues indefinitely until the script is interrupted. Overall, the script effectively demonstrates serial communication with the STM32 microcontroller and showcases real-time control of LEDs based on device tilt, highlighting the integration of hardware and software components in embedded systems development.

3. **Instructions on how to run the code** Instructions on How to Run the Code

   To run the provided Python script for communicating with the STM32 microcontroller and controlling LEDs based on tilt direction, follow these steps:

1. Make sure the STM32 microcontroller is connected to your computer via USB ST-Link and upload STM32 Project including main.c file (see Dependencies)
1. Connect the STM32 Microcontroller with Jetson Nano via USB USER and the Remote-SSH in VS code extensions . Ensure that the appropriate port name is specified in the code (`port\_name = "/dev/ttyACM0"`). Followed by ‘Sudo chmod 666 /dev/ttyACM0’ to give permission to the port by running the following commands in the new terminal of VS code.
3. Install Python and PySerial: If you haven't already, install Python 3.x and the PySerial library using pip:
3. Run the Python Script: Execute the Python script `led.py` using a Python interpreter:
3. Observe LED Control: The script will establish a serial connection with the STM32 microcontroller, read gyro data, interpret tilt direction, and control LEDs accordingly. LEDs on the STM32 board will reflect the tilt direction of the device.
3. Exiting the Script: To exit the script, press `Ctrl + C` in the terminal where the script is running. This will close the serial connection and terminate the script execution.

![](Aspose.Words.61ab173d-0de5-427d-98e2-0d7552324da1.001.png)

Figure 01 : The Gyroscope data received from STM32

Figure 02 : The LED blinks on STM32 with changes in roll and pitch![](Aspose.Words.61ab173d-0de5-427d-98e2-0d7552324da1.002.png)

4. **Dependencies and Libraries used**
- Dependency : <https://github.com/MaxwellHogan/Project_1_STM32>
- Essential Library : PySerial library(‘pip install pyserial’)
- Other libraries used in .py code : matplotlib
5. **Table of content for the file**



|**Name**|**Description**|
| - | - |
|led.py|Python script for STM32 communication, LED control based on tilt, and real-time gyro data plotting.|

