import serial
import time
import matplotlib.pyplot as plt

# Initialize serial connection
port_name = "/dev/ttyACM0"
stm32 = serial.Serial(port_name, 9600, timeout=1)
print("open")

def send_command_with_response(command, data=None):
    """
    Sends a command to the STM32 and reads the response.

    :param command: The command byte.
    :param data: Additional data for the command, if needed.
    :return: The decoded response from the STM32.
    """
    packet = bytearray()
    packet.append(command)  # Add the command byte

    if data is not None:
        packet.append(data)  # Append additional data if provided

    stm32.write(packet)  # Send packet
    time.sleep(0.1)  # Wait for the STM32 to process the command    
    response = stm32.readline().decode("utf-8")  # Read response
    time.sleep(0.1)  # Brief pause before next command or closing connection
    
    return response

def response_to_xy(response):
    """
    takes response data and returns x and y data
    """
    try:
        trim = response.lstrip("\r\x00").rstrip(" n") #remove the extra characters (newline, return, buffer)
        split = trim.split(", ")
        x=int(float(split[0][3:]))
        y = int(float(split[1][3:-2]))
        return x, y
    except ValueError:
        return 0, 0
def set_led(led_no):
    """
    Sets the specified LED and prints the response. Validates led_no is between 0 and 7.

    :param led_no: The LED number to set.
    """
    if 0 <= led_no <= 7:
        response = send_command_with_response(0x01, led_no)
      
    else:
        print("Error: LED number {} is out of range. Please select a number between 0 and 7.".format(led_no))


x_data=[]
y_data=[]
try:
    while(1): #run indefinitely
        response = send_command_with_response(0x02)  # Request gyro data
        print(response)
        time.sleep(.01)
        try:
            x, y = response_to_xy(response)
            print(x ,y)
            limit = 100000
            x = max(min(x, limit), -limit)
            y = max(min(y, limit), -limit)
            x_data.append(x)
            y_data.append(y)
        except TypeError:
            pass #catch any incorrectly processed responses and continue
            

        if (abs(x)>20000) or (abs(y)>20000): #If tilt on sensor is enough
            if abs(x)>abs(y): #if x data is more (regardless of direction)
                if x>1000: #if its tilted south
                    set_led(4)
                elif x<-1000 :
                    set_led(0) #if its tilted north
                else:
                    pass
            else: # if y data is more
                if y>1000: #tilted east
                    set_led(2)
                elif y<-1000: #tilted west
                    set_led(6)
        else: #low level data
            pass
       
except KeyboardInterrupt:
    print("exiting")
finally:
    stm32.close()  # Close serial connection when done
    print("closed")

print("Goodbye")

plt.plot(x_data, label="x")
plt.plot(y_data, label="y")
plt.legend
plt.title("gyro data")
plt.ylim(-1000_00, 100_000)
