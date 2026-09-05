# Roving Edge Infrastructure Data Synchronization
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm
- Fetched: 2026-09-05 02:58 CDT

# Roving Edge Infrastructure Data Synchronization

Learn how to manage the transmission of object storage data between buckets on your Roving Edge Infrastructure devices and your Oracle Cloud Infrastructure tenancy.

Although Roving Edge Infrastructure devices are designed to operate connected, semi-connected and disconnected from the cloud for days or weeks at a time, syncing the data between your Roving Edge Infrastructure devices and your Oracle Cloud Infrastructure tenancy is an important task you must do regularly.

You can perform syncing in the following ways:
- 

Roving Edge Infrastructure device bucket-to-Oracle Cloud Infrastructure bucket: Upload data to your Oracle Cloud Infrastructure object storage buckets for processing and long-term storage, freeing space on the devices.
- 

Oracle Cloud Infrastructure bucket-to-Roving Edge Infrastructure device bucket: Download data residing in the object storage buckets in your Oracle Cloud Infrastructure tenancy to the devices. Also update system files for the device and its browser-based user interface.
Note  
  

You can't set up a bi-directional sync using two tasks and the same object storage buckets used by Oracle Cloud Infrastructure and the Roving Edge Infrastructure devices.
Note  
  

The maximum size of an object you can use with Roving Edge Infrastructure devices is 10 TiB. Any objects in your object store workload or any custom images greater than 10 TiB in size are not included in the data synchronization.

The following are the prerequisite tasks for performing a bi-directional data synchronization:
- 

Connect your Roving Edge Infrastructure device to your local site network, such as a site headquarters using the internet or FastConnect.
- 

Provide routing using the internet or FastConnect to an Oracle Cloud Infrastructure region.
- 

Specify the object storage buckets on Oracle Cloud Infrastructure that contain the data that needs to be preloaded on your Roving Edge Infrastructure device when your device is being provisioned.

Configure separate buckets to be either the source or destination of the transferred data. You cannot have bi-directional tasks or a task where the same pair of buckets reverse roles as bucket and source.
Note  
  

You can't set up a bi-directional sync using two tasks and the same object storage buckets used by Oracle Cloud Infrastructure and the Roving Edge Infrastructure devices.
Note  
  
If you have trouble syncing data, check the connectivity between the device and the OCI Object Storage service. See[Data sync, system upgrades, or sanitization operations not working](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/../troubleshooting.htm#networking__object-storage-connectivity).

You can perform the following data sync tasks:
- 

[Creating a Data Sync Task](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/create_datasynctask.htm#CreateDataSyncTask)
- 

[Listing Data Sync Tasks](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/list_datasynctask.htm#ListDataSyncTask)
- 

[Getting a Data Sync Task's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/get_synchronization.htm#GetDataSyncTask)
- 

[Editing a Data Sync Task](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/update_datasynctask.htm#UpdateDataSyncTask)
- 

[Starting a Data Sync Task](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/start_datasynctask.htm#StartDataSyncTask)
- 

[Stopping a Data Sync Task](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/stop_datasynctask.htm#StopDataSyncTask)
- 

[Deleting a Data Sync Task](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/delete_datasynctask.htm#DeleteDataSyncTask)
