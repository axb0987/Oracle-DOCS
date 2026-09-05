# Returning Older Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/returning-older-devices.htm
- Fetched: 2026-09-05 02:59 CDT

# Returning Older Devices

To return older Roving Edge devices, use the procedures in this section.
Note  
  

If the Roving Edge device was self-provisioned on-site, don't perform the tasks listed in this section. Instead, use the sanitization feature. If you're not sure which procedure to use, start with the sanitization feature described in[Sanitizing a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/sanitizing-a-device.htm#sanitizing-a-device).

## Prepare a Device for Return

Before returning your Roving Edge Infrastructure devices to Oracle, delete all workloads and data on each device by performing the tasks in this section.
Important  
  

Ensure you have synced all your needed data to Oracle Cloud Infrastructure using Data Sync before deleting it from your devices. See[Data Sync Tasks](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).

Perform the following tasks in the order listed:
- Delete all data objects residing in the object storage buckets. See[Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Object_Storage/Object/delete_object.htm#top).
- Delete all object storage buckets. Delete all the objects they contain before deleting the buckets themselves. See[Deleting a Bucket](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Object_Storage/Bucket/delete_bucket.htm#top).
- Delete all block volumes. See[Deleting a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Block_Volume/delete_block_volume.htm#top).
- Delete all users. Deleting a user resource also deletes any associated client credentials. See[Deleting a User](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../IAM/User/delete_user.htm#DeleteUser).
- Terminate all compute instances and remove all images. See[Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Compute/Instance/terminate_instance.htm#TerminateInstance)and[Removing an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Compute/Image/delete_image.htm#top).

Successfully completing these tasks before returning the devices to Oracle complies with your terms and conditions.

## Contact Oracle to Return the Device

When you're ready to return your Roving Edge Infrastructure devices to Oracle, contact My Oracle Support to arrange the pickup and delivery. See[Contacting Oracle Support](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../contacting_oracle_support.htm#ContactOracleSupport)
