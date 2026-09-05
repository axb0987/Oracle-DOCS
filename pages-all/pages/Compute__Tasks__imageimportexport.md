# Importing and Exporting Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm
- Fetched: 2026-09-05 01:51 CDT

# Importing and Exporting Custom Images

You can move Compute instances to and from tenancies, regions, and other cloud providers using custom images and image import/export.
Important  
  
For more information on moving images and data from other cloud providers to and from Object Storage see:[Moving Data to and from Object Storage](https://docs.oracle.com/iaas/Content/Object/data-migration.htm).
Note  
  
Platform images, Marketplace images, and custom images that are created from Marketplace images cannot be exported.

The following formats are supported for importing and exporting images to and from other tenancies, regions, and cloud providers.

Import:
- VMDK: Virtual Machine Disk (.vmdk)
- QCOW2: QEMU Copy On Write (.qcow2)
- OCI: Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format when importing a custom image that was exported from another tenancy or region.

Export:
- Virtual Machine Disk (.vmdk)
- Virtual Hard Disk (.vhd) for Hyper-V
- Virtual Disk Image (.vdi) for Oracle VM VirtualBox
- QEMU Copy On Write (.qcow2)
- Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format to export a custom image that you want to import into other tenancies or regions.

For more information on importing or exporting images, see the following.
- [Importing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm)
- [Exporting Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm)
Important  
  
To import or export custom images from Object Storage buckets,[federated users](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm)and users authenticating with instance principals tied to a dynamic group need to create a[pre-authenticated request](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs__PAR). For more information, see the known issue[Invalid bucketName error when importing or exporting a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#invalid-bucketName).

## Linux-based OSs

The following Linux versions support image import/export:
- Oracle Linux 7.x
- Oracle Linux 8.x
- Oracle Linux 9.x
- Oracle Linux Cloud Developer 8.x
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 24.04

## Windows-based OSs

The following Windows versions support image import/export:
- Windows Server 2016 Standard, Data center
- Windows Server 2019 Standard, Data center
- Windows Server 2022 Standard, Data center
- Windows Server 2025 Standard, Data center
Important  
  

When exporting Windows-based images, you are responsible for complying with the[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/)and all product use conditions, as well as verifying your compliance with Microsoft.

For information about the licensing requirements for Windows images, see[Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/microsoftlicensing.htm).

### Verify The Windows OS

When importing custom Windows images, ensure that the version you select matches the Windows image that you imported. Failure to provide the correct version and SKU information could be a violation of the Microsoft Licensing Agreement.

### Windows System Time Issue on Custom Windows Instances

If you change the time zone from the default setting on Windows VM instances, when the instance reboots or syncs with the hardware clock, the system time will revert back to the time for the default time zone. However, the time zone setting will stay set to the new time zone, so the system clock will be incorrect. You can fix this by setting the`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation`registry key to 1.

Windows platform images already have the`RealTimeIsUniversal`registry key set by default, but you must set this for any custom Windows images that you import.

To fix this issue for custom Windows images:
- Open the Windows Registry Editor and navigate to the`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation`registry key.
- Create a new`DWORD`key named`RealTimeIsUniversal`and set the value to 1.
- Reboot the instance.
- Reset the time and time zone manually.

## Bring Your Own Image Scenarios

You can also use image import/export to share custom images from[Bring Your Own Image (BYOI)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bringyourownimage.htm)scenarios across tenancies and regions, so you don't need to recreate the image manually in each region. You must go through the steps required to manually create the image in one of the regions, but after this is done, you can export the image, making it available for import in additional tenancies and regions. Export the image in the`.oci`format, which is a file format that contains a QCOW2 image file and Oracle Cloud Infrastructure-specific metadata.

### Best practices for replicating an image across regions

You can replicate an image from one region to another region using the Console or API. At a high level:
- [Export the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm)to an Object Storage bucket in the same region as the image.
- [Copy the image](https://docs.oracle.com/iaas/Content/Object/Tasks/copyingobjects.htm)to an Object Storage bucket in the destination region.
- [Obtain the URL path to the image object](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm).
- In the destination region,[import the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm). Use the URL path as the Object Storage URL.

### Best practices for sharing an image across tenancies

You can replicate an image from one tenancy to another tenancy using the Console or API. At a high level:
- [Export the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm)to an Object Storage bucket in the same region as the image.
- 

[Working with Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm)with read-only access for the image in the destination region.
- In the destination tenancy,[import the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm). Use the pre-authenticated request URL as the Object Storage URL.

## Object Storage Service URLs

When you import or export custom images using the Console, you might need to specify the Object Storage URL pointing to the location that you want to import the image from or export the image to. Object Storage URLs are structured as follows:
```

```

For example:
```

```

### Pre-Authenticated Requests

When using import/export across tenancies, you need to use an Object Storage pre-authenticated request. See[Working with Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm)for steps to create a pre-authenticated request. When you go through these steps, after you select Create Pre-Authenticated Request , the Pre-Authenticated Request Details dialog box opens. You must make a copy of the pre-authenticated request URL displayed here, because this is the only time this URL is displayed. This is the Object Storage URL that you specify for import/export.
Note  
  

Pre-authenticated requests for a bucket

With image export, if you create the pre-authenticated request for a bucket, you need to append the object name to the generated URL. For example:

```

```
