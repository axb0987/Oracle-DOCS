# Device Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Node/device-metrics.htm
- Fetched: 2026-09-05 03:01 CDT

# Device Metrics

Describes how to enable, disable, and use metrics to describe services' trends and current performance.

You can enable and configure Roving Edge Infrastructure to generate metrics on device performance and health regarding block volume storage. These metrics are taken from the Roving Edge Infrastructure services and are placed in an InfluxDB 1.8 or later database that you must acquire and set up on a dedicated host database server. This machine can be co-located with your other computer hardware in your Roving Edge Infrastructure environment, or remotely if you have a working internet connection.

After your InfluxDB database is running you must configure and enable your Roving Edge Infrastructure devices to send data. You can subsequently review the metrics data by accessing the InfluxDB database.
Note  
  

You are responsible for maintaining the InfluxDB database.

## Using the Device Console

- Open the navigation menu and select Node Management &gt; Nodes . The Nodes page appears.
- Select Configure metrics . The Configure metrics dialog box appears.
- Complete the following:

- 

Db URL : Enter the URL for the InfluxDB database where the metrics data is sent.
- 

Organization : Enter the name of the organization responsible for the InfluxDB.
- 

Bucket Name : Enter the bucket name where metrics data is stored.
- 

API Token : Enter the token used by the API to communicate with InfluxDB.
- 

Certificate : (optional) Complete one of the following tasks:
- 

Upload certificate file : Navigate to the certificate file (`.pem`) and upload it to the dialog box.
- 

Paste content : Copy and past the certificate contents directly into the box.
- Select Enable .

A banner appears indicating that the metrics service is enabled.
