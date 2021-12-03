# SmartDoor  
An IoT based project.  

__Working:__  
When someone came in the vicinity of ultrasonic sensor (i.e. fixed to 100cm for this project) then it detects the person and a LED will glow. Now person can enter his/her Name and password in the form displayed if user have permission. If user don't have permission and trying to enter illegaly, and made three guesses. If all the guesses goes wrong then buzzer will start alarming until person goes from vicinity of ultrasonic sensor.  

If user don't have permission and want the permission then he/she can request the admin through form by clicking of "Ask for permission" button.  

__Technology and networking:__  

1. Devices used:  
    * Ultrasonic sensor : To detect the person
    * Servo motor : To open the door  
    * LEDs : To show the person in vicinity and opening of door  
    * Esp32: Microcontroller to control the device.
    * Buzzer

2. Sending the data to oneM2M server by making http POST and GET request.  
3. **Languages used:**  
    * Arduino Programming
    * Python
    * Tkinter in Python

__How to run:__  
1. Install the Arduino IDE and installed the library for the headers used in project.ino file  
2. Install the python and Tkinter    

3. Run the createContainer.py file.  
4. Run givePermission.py file and give the input in csv format to add permission.  
5. Run the form.py file.  

__Ideas for extension of this project:__  
1. Biometric, camera, and PIR sensor can be used for better detection and security purpose.  
2. BLE device can be used for some special users.  
