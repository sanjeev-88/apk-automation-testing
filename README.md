# apk-automation-testing
Appium
•	Appium is an automation testing tool that can be used to validate mobile browsers and mobile applications. 
•	It is used in mobile automation testing because it is free and is cross-platform (can support both IOS and Android). 
•	Automation tests in Appium can be run on mobile devices, simulators, and emulators.
•	An emulator is software or hardware that allows a computer system (host) to run applications designed for another system (guest).
Appium work on Android
•	The Appium client connects with the HTTP server and uses the JSON Wire Protocol for communication,
•	The Appium server receives requests from the client component.
•	The server connects with the mobile automation framework for Android.
•	Android devices contains bootstrap.jar that receives the test commands from the Applum server. The bootstrap jar contains executable files that enhance the connection between the server and Android devices. It plays the role of a TCP server since it enhances the secure transmission of test commands to the Android devices.The bootstrap jar uses the UI Automator or Selendroid to execute the command requests on the Android device.
•	The test results are then sent to the server, which eventually sends HTTP responses to the Appium client. The HTTP responses contain status codes indicating success or server error.
