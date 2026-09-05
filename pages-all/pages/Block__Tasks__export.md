# OCI Block Volume - Export Steps
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm
- Fetched: 2026-09-05 01:46 CDT

# OCI Block Volume - Export Steps

This document is intended as guide for the steps OCI customers can take to extract OCI Block Volume data and move it to another cloud provider or to their on-prem facility. Similar steps can be used when migrating OCI Block Volume data across tenancies with restricted security access.

## Option 1: Extract and Transfer Block Volume Data

If your block volume is not a boot volume , then the block volume data can be extracted manually and then converted to the proper format required by another Cloud Provider or for on-prem usage.

### Step 1: Attach the Block Volume to an OCI Compute Instance

Prerequisite : A Linux-based compute instance must be available for attaching the block volume to.
- On the Block Volumes list page, select the block volume that you want to attach to an instance. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm).
- On the details page, select Attached Instances .
- Select Attach to Instance .
- On the Attach to instance panel, enter the following information.
- Attachment type : Select ISCI .
- Instance : Select the instance that you want to attach the block volume to.
- Select Attach .
- Connect to the Linux instance by running each command in sequence, in the Console:
Note  
  
All command arguments are essential. Success returns no response.
```

```

```

```

```

```

For more information on connecting to a volume on a Linux instance, see[Connecting to a Volume on a Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume_topic-Connecting_to_iSCSIAttached_Volumes.htm#Connecting_to_a_Volume_on_a_Linux_Instance).
- Verify the block device appears (typically as`/dev/sdb`or similar) by use of the Linux`lsbk`(list block devices) command:
```

```

### Step 2: Create a Raw Disk Image

- Decide where to store the block volume image.
- If the image file is small enough (for example, less than 100 GB), you can store it locally in`/mnt/`or another large partition on the boot volume.
- If the image file is large, you might need to attach an additional block volume to store it.
- Run the`dd`command to capture the entire block volume into a raw disk image:
```

```

where:
- `/dev/sdb`is the attached block volume.
- `/mnt/volume.img`is the location to store the Block Volume image.
- `bs=1M`indicates large blocks to improve read/write efficiency.
- `status=progress`shows progress.

### Step 3: Convert the Image to Another Format

Prerequisites : To get the functionality in this step, you might need to install`qemu-img`or`qemu-tools`on your distribution.

Convert the raw image to the required format based on the target cloud or on-prem destination:

- [VMDK (VMware)](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- [VHD (Microsoft Azure)](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- [QCOW2 (KVM, OpenStack)](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- 

```

```

- 

```

```

- 

```

```

### Step 4: Upload the Block Volume Image to OCI Object Storage

Move the image from the instance to a bucket using the following command:
```

```

Example for an unconverted image:
```

```

Example for an image converted to VMDK format:
```

```

### Step 5: Transfer to Another Cloud Provider

- [Amazon Web Services (AWS)](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- [Google Cloud Provider (GCP)](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- [Microsoft Azure](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#)
- 

- Download the block volume image from OCI Object Storage to your workstation:

```

```

- Upload the block volume image from your workstation to AWS S3:

```

```

- Import an EBS volume:

```

```

- 

- Download the block volume image from OCI Object Storage to your workstation:

```

```

- Upload the block volume image from your workstation to Google Cloud Storage:

```

```

- Import the disk image:

```

```

- 

Prerequisite: The image must be converted to VHD format. See[Step 3: Convert the Image to Another Format](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#convert).

- Upload the block volume image from your workstation to Azure Blob Storage:

```

```

- In Azure, create a Managed Disk from the uploaded VHD:

```

```

## Option 2: Create a Bootable Image for a Boot Volume and Export It

If your block volume is attached to a compute instance as a boot volume, you can create a custom image and export it.
- [Create a custom image](https://docs.oracle.com/iaas/Content/Compute/Tasks/custom-images-create.htm)from the instance that uses the block volume as a boot volume.
- [Export the custom image](https://docs.oracle.com/iaas/Content/Compute/Tasks/custom-images-export.htm)to a bucket in Object Storage.
- Download and transfer the image:
- Use the OCI CLI to download the exported image to your workstation:
```

```

- Upload the file from your workstation to your target cloud provider and import it in the native virtual disk format using commands at[Step 5: Transfer to Another Cloud Provider](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/export.htm#transfer).
- Amazon Web Services (AWS) : Upload to S3 , then convert it into an EBS snapshot .
- Google Cloud Provider (GCP) : Upload to Cloud Storage and create a persistent disk .
-
