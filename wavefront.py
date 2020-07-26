
'''
1: Create a Python script which sends a single counter metric with the following details: 2:

Setup a WavefrontSender which uses DirectIngestion     a)

DirectIngestion Server: “elgon.wavefront.com” 
b) DirectIngestion Token: “TOKEN” 
c) Metric name: “sd.interview.test” 
d) Value: 42 
e) TimeStamp: Local timestamp in milliseconds 
f) Source: “sd-laptop” 
g) Tags: { “developer”: “sd”, “codetest”: “python” } 
h) Must flush and close the connection Must print to console:  
“Metric send to <server>” “Failures: <failure_count>” 
Catch all exceptions when sending the metric and print any error captured 
'''
#from wavefront_sdk import WavefrontProxyClient
from wavefront_sdk import WavefrontDirectClient
import time

if __name__ == '__main__':
    try:
        wavefront_sender = WavefrontDirectClient(
            server="https://elgon.wavefront.com",
            token="37e6297f-b9f7-44d9-b444-d3dab1082426"
        )

        wavefront_sender.send_metric(
            name="sd.interview.test", value=42, timestamp=round(time.time()),
            source = "sd-laptop", tags = { "developer": "sd", "codetest": "python"})

    except Exception as e:
        print("An error occurred: {}".format(e))
    finally:
        total_failures = wavefront_sender.get_failure_count()
        print("Failures: {}".format(total_failures))

    wavefront_sender.flush_now()
    wavefront_sender.close()
'''
    // flush and close
    connections
 '''
