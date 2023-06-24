# **Generating Melodies for Raspberry Pi and Buzzer(Python Script)**
This repository contains a Python script designed to create melodies using a Raspberry Pi and a Piezo buzzer.

### **Description**
The script uses musical notes mapped to specific frequencies in Hertz. These mappings allow the user to compose and play back simple melodies.

**Technical Details**
The script uses the **pigpio** library to generate PWM signals for the Piezo buzzer. It also employs Python's dynamic function creation capabilities to associate each musical note with a specific function. When these functions are called, they produce the corresponding note on the buzzer.

An example loop is included in the script to demonstrate how to compose and play back a melody. Specifically, a portion of the Super Mario theme is played back. The user can adjust the exact duration of each note to their preference.

Please ensure that the **pigpio** library is installed in your environment to successfully run this script. Additionally, this script is designed to work with a specific GPIO pin (18 in this case). Therefore, make sure your buzzer is connected appropriately.

**Potential Applications**
While the current setup is fairly basic, it opens a door to many potential applications in areas like music, gaming, and more. By playing with and extending this code, you could create custom jingles for notifications, craft unique game sound effects, or even design a mini digital musical instrument.

Thank you!
