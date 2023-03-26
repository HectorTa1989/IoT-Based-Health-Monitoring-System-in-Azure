import random
import time
from azure.iot.device import IoTHubDeviceClient, Message
CONNECTION_STRING = "HostName=iot-hub-HealthMonitor.azure-devices.net;DeviceId=MyPythonDevice;SharedAccessKey=BQyG5IQffDPPBZTpraXmEpcq+RcrSFaQBGfsy+GXUpI="
TEMPERATURE = 35.0
HEARTRATE = 60.0

MSG_TXT = '{{"temperature": {temperature},"heartRate": {heartRate}}}'
def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client
def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Heart Rate Monitor sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with simulated telemetry values.
            simulated_temperature = TEMPERATURE + (random.random() * 3)
            simulated_heartRate = HEARTRATE + (random.random() * 50)
            msg_txt_formatted = MSG_TXT.format(temperature=simulated_temperature, heartRate=simulated_heartRate)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if simulated_temperature > 37.5:
              message.custom_properties["FeverAlert"] = "true"
            else:
              message.custom_properties["FeverAlert"] = "false"
            if simulated_heartRate > 100:
              message.custom_properties["CardiacAlert"] = "true"
            else:
              message.custom_properties["CardiacAlert"] = "false"  

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Heart Rate Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
