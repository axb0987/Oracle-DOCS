# Editing Image Capabilities for Custom Images Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm
- Fetched: 2026-09-05 01:50 CDT

# Editing Image Capabilities for Custom Images Overview

Image capabilities are the configuration options available when launching an instance from an image. Some image capability examples are the firmware used to boot the instance, the volume attachment types supported, and so on.

The full set of image capabilities provided by Oracle Cloud Infrastructure Compute are defined in the global image capability schema. You can also create your own custom image capability schemas based on the global image capability schema to specify and configure image capabilities for your custom images. Using these schemas, you can customize the image configuration and options available when users launch instances from your custom images. To edit the capabilities for an instance see:
- [Editing Image Capabilities for Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities-tasks.htm)
Caution  
  
Using this feature allows you to customize image capabilities from the default capabilities that Oracle recommends and should be used for advanced custom image scenarios only. Ensure that you understand the optimal configuration options for your custom image.

## Global Image Capability Schema

The following JSON is what's returned when you use the`GetComputeGlobalImageCapabilitySchemaVersion`API operation or the`global-image-capability-schema-version`CLI command. It represents the full set of image capabilities available for images. The default values specified for each element are the recommended values for each option.

You can customize these options by creating image capability schemas. When you create an image capability schema, you can specify a subset of the values that are included in the global capabilities schema. Values that are not included in the global capabilities schema cannot be provided in an image capability schema.

```

```

## Schema Elements

The following list describes all the available elements in the global image capabilities schema.
- Compute.AMD_SecureEncryptedVirtualization : Provides confidential computing to virtual machine users leveraging AMD Secure Encrypted Virtualization (SEV) on AMD shapes. Data is encrypted in-use and you can verify the confidentiality through a secure attestation process. The default value is false.
- 

Compute.Firmware : The firmware used to boot the virtual machine instance. The default value is UEFI_64.
- 

Compute.SecureBoot : Whether the instance can use Secure Boot. The default value is false.
Important  
  
Custom images do not support Secure Boot.
- 

Compute.LaunchMode : The configuration mode for launching instances. The default value is PARAVIRTUALIZED.
- 

Network.AttachmentType : The emulation type for the primary VNIC, which is automatically created and attached when the instance is launched. The default value is PARAVIRTUALIZED.
- 

Storage.BootVolumeType : Specifies the driver options for the image's boot volume. The default value is PARAVIRTUALIZED.
- 

Storage.LocalDataVolumeType : Specifies the driver options for the image to access local storage volumes. The default value is PARAVIRTUALIZED.
- 

Storage.RemoteDataVolumeType : Specifies the driver options for the image to access remote storage volumes. The default value is PARAVIRTUALIZED.
- 

Storage.ConsistentVolumeNaming : Specifies whether consistent device paths for iSCSI and paravirtualized attached block volumes are enabled for the image. If enabled, the image must support consistent device names. The default value is true.
- 

Storage.ParaVirtualization.EncryptionInTransit : Specifies whether in-transit encryption is enabled for the image's boot volume attachment. Applies only to paravirtualized boot volume attachments. The default value is true.
- 

Storage.ParaVirtualization.AttachmentVersion : Specifies the paravirtualization version for boot volume and block volume attachments. Applies only to paravirtualized volume attachments. The default value is 2.
- 

Storage.Iscsi.MultipathDeviceSupported : Specifies whether multipath-enabled attachments are supported for the image. Applies only to iSCSI volume attachments. The default value is false.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm).

For administrators, the following policy provides full access to the image capability schema framework:
```

```
