# Creating a VMware Solution Datastore
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-create.htm
- Fetched: 2026-09-05 03:08 CDT

# Creating a VMware Solution Datastore

Create a VMware Solution datastore.

## Using the Console

- Open the navigation menu and select Hybrid . Under VMware Solution , select Datastore .
The Datastores list opens. All datastores are displayed in a table.
- Select Create datastore .
The Create datastore panel opens.

### Basic information

Enter the following information:
- Name : Enter a friendly name for the datastore. Do not enter confidential information.
- Create in compartment : Select the compartment that you want to store the datastore in.
- Availability Domain : Select the isolated, fault-tolerant Oracle data center that hosts cloud resources such as instances, volumes, and subnets.
- Create in Datastore Cluster : Select the datastore cluster in which you want to place the datastore. For more information about datastore clusters, see[Managing VMware Solution Datastore Clusters](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-clusters-managing.htm).

### Block Volume

Enter the following information:
- Create a new block volume : Select an option and complete the information according to what you see:
- Name : Enter a name for the block volume. Avoid entering confidential information.
- Create in compartment Select the compartment in which to create the block volume.
- Volume size and performance : Select one of the following options:
- Default : Select this option to use the default size of 2048 GB 2048 GB and Balanced Volume Performance.
- Custom : Select this option to enter a custom size of the volume between 50 GB and 32 TB. If you select a size outside of your service limit, you might be prompted to request an increase. See Service Limits.
- Target volume performance : Select the appropriate performance level for your requirements. For more information about volume performance options, see[Block Volume Performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance).
- Performance based auto-tune : Select this option to automatically adjust the volume's performance (such as IOPS and throughput) between specified levels.
- Default and Maximum VPU/GBs type : Select the Volume Performance Units (VPU) per GB to control the performance of the volume.
- Detached volume auto-tune : Select this option for the auto-tuning to take effect after 24 hours. After that, if the volume is still detached, its performance and cost is lowered to the Lower Cost setting automatically. For more information, see[Cloud Storage Pricing](https://www.oracle.com/cloud/storage/pricing).
- Volume Encryption : Select Encrypt using Oracle-managed keys to leave all encryption-related matters to Oracle or Encrypt using customer-managed keys using your own access to a valid key management key.
- Add an existing block volume :
- Create in compartment : Select the compartment in which to create the block volume.
- Select the existing block volume.

#### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
