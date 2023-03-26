# IOT Based Smart Health Monitoring and Notifications with Azure Logic Apps

### Summary
The purpose of this project is to monitor vital signs such as heart-rate and temperature. The system automatically sends alerts to healthcare if there is any abnormality in the telemetry value. The IoT device is simulated using the Python code, which generates the Heartrate and Temperature. The values are sent to the Azure IoT Hub. Using Stream Analytics Job the data from the IoT Hub is sent to the PowerBI to generate meaningful insights (Visualization). The notification is sent using Azure Logic Apps by connecting IoT hub and mailbox (SendGrid).

### Requirements
* Simulated Device - Python Code
* Microsoft Azure Subscription
* Iot Hub
* Stream Analytics Job
* PowerBI
* Service Bus Namespace & Queue
* Custom End-point & Routing Rule in Iot-Hub
* SendGrid (to send e-mail notifications)
* Azure Logic Apps with Trigger
### Simulated Device Sending Telemetry Values
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1660).png?raw=true)
### IoT-Hub Events Monitor
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1662).png?raw=true)
### Generated Report in PowerBI
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1659).png?raw=true)
### ServiceBus Queue
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1665).png?raw=true)
### IoT-Hub End-point with Routing Query
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1666).png?raw=true)
### Logic App Designer
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1664).png?raw=true)
### Logic App Runs History
![alt text](https://github.com/HectorTa1989/IoT-Based-Health-Monitoring-System-in-Azure/blob/master/Screenshot%20(1663).png?raw=true)
