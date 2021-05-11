1. Setup    (1) The main.cpp is at src/model_depoly and python code is at 
                src/model_depoly/wifi_mqtt
            (2) To start running the code, please enter
                $ sudo mbed compile --source . --source ~/ee2405new/mbed-os-build2/ -m B_L4S5I_IOT01A -t GCC_ARM -f
                under src/model_depoly to start compiling
            (3) After compiling the program, wait until LED2 on the mbed
                Microcontroller ligth up. Then enter
                $ sudo python3 wifi_mqtt/mqtt_client.py
                under src/model_depoly to start python code.
2. Run      (1) After you start the python code, the mbed will enter GestureUI
                mode. The LED1 on the controller will blink for 4 second. Then,
                you can use different gesture to select threshold angle. The
                current selection will be shown on uLCD.
                If you finish your selection, press the user button to stop
                GestureUI mode . The screen will then show your final selection.
            (2) After confirming your selection, mbed will enter angle detection
                mode. The LED3 will blink to indicate the initialization process.
                While initializing the acceleration data, controller should remain 
                stable.
            (3) LED3 will stop blinking after the initialization. Then, you can
                start tilting the controller. The current tilt angle will be 
                shown on uLCD. If the tilt angle is over the threshold angle,
                the angle will be shown on the screen. Then, mbed will stop
                detection mode and back to GestureUI.
