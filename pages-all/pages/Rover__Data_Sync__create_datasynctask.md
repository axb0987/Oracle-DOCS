# Creating a Data Sync Task for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/create_datasynctask.htm
- Fetched: 2026-09-05 02:58 CDT

# Creating a Data Sync Task for Roving Edge Infrastructure

Describes how to create a data sync task for your Roving Edge Infrastructure devices.

## Using the Device Console

- 

Open the navigation menu and select Data Sync . The Data Sync Tasks page appears. All data synchronization tasks are listed in tabular form.
- 

Select Create Task . The Create Tasks dialog box appears.
- 

Enter the following:
- 

Select the sync direction:
- 

From Oracle Cloud Infrastructure to Roving Edge Infrastructure device: Push objects from the cloud to the device
- 

From Roving Edge Infrastructure device to Oracle Cloud Infrastructure : Push objects from the device to the cloud
- 

OCI Bucket : Complete the following:
- 

Enter the Compartment ID . This value is the OCID associated with the Oracle Cloud Infrastructure compartment in which your object storage bucket resides. You can find this OCID in the Details page of your compartment in the Oracle Cloud Infrastructure Console.
- 

Enter the OCI Bucket Name . This value is the name of the object storage bucket containing the data on Oracle Cloud Infrastructure with which you are synchronizing with your data. You can find a list of your buckets in the Object Storage page in the Oracle Cloud Infrastructure Console.
- 

RED Bucket : Select one of the following options:
- 

Select an existing bucket : Select an existing bucket from the RED Bucket Name list.
- 

Create a new bucket : Enter the name of the bucket you are creating in the RED Bucket Name box.
- 

Rate Limit : Select the rate limit in which objects and synchronized data transferred between the device and Oracle Cloud Infrastructure from the Bandwidth list. Default is "No Limit."
- 

Schedule: Complete the following to schedule your device's data sync activities:
- 

Start Date : Enter or use the Calendar feature to specify the start date of the time period when the scheduled data sync activity occurs.
- 

End Date : Enter or use the Calendar feature to specify the end date of the time period when the scheduled data sync activity occurs.
- 

Frequency : Select the frequency of the data syncs from the list. Available options are Hourly, Daily, Weekly, or Monthly. If you select weekly, the day of the week is determined based on the start date.
- 

Sync Start Time : Select the time of day when the data sync begins.
- 

Sync on Last Day of Each Month : Check to perform a data sync on the last day of the month.
- 

Schedule Priority : Select the priority in which competing tasks are started first when they have the same run time. This priority does not interrupt currently running tasks. Available options are High , Medium , and Low .
- 

Sync on Reconnect : Check for the device to automatically run a data sync anytime the device is reconnected to Oracle Cloud Infrastructure.
- 

Check Sync on Create to begin the synchronization after the task is created.
- 

Select Save .

If you checked the Sync on Create option, the data sync task begins immediately. If you did not check this option, you can start the data sync task by checking the task in the Data Sync Tasks page and selecting Start .

For Roving Edge Infrastructure device to Oracle Cloud Infrastructure data syncs, select the Source Bucket link for the task you just ran after it completes. The bucket's Details page appears, listing those files that were uploaded from your Roving Edge Infrastructure device to your Oracle Cloud Infrastructure destination.
