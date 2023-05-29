# SendRealTimeGyroDataFromAndroidToRaspberryPi
This will connect through Wi-Fi and send real time gyro data from an Android phone to the Raspberry Pi
The provided program demonstrates a simple client-server communication setup between an Android device and a Raspberry Pi using sockets. The Android app sends real-time gyro data to the Raspberry Pi, which receives and processes the data. The main purpose of this program is to showcase a basic implementation of transmitting sensor data from an Android device to a Raspberry Pi over a local network.

The Android app utilizes the device's rotation vector sensor to obtain the gyro data, specifically the X, Y, and Z axis values representing the device's orientation. It establishes a socket connection with the Raspberry Pi using the IP address and port specified in the code. Once connected, the app continuously sends the gyro data to the Raspberry Pi in real-time.

On the Raspberry Pi side, a Python program is running to act as the server. It listens for incoming connections from the Android app and accepts the connection when established. Once connected, the server receives the gyro data sent by the Android app, decodes it, and processes it as needed. The received data can be utilized for various purposes, such as performing actions based on the device's orientation or displaying the data on a screen.

The program serves as a foundation for building more complex applications that involve real-time data transmission between an Android device and a Raspberry Pi. It can be extended by adding additional functionality to handle and interpret the gyro data, integrating it with other components or systems, or incorporating more advanced communication protocols and security measures.

Overall, this program demonstrates the possibilities of using a client-server architecture to exchange data between an Android device and a Raspberry Pi, providing a starting point for developing custom applications that leverage sensor data and remote communication.
