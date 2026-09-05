# Enabling In-Transit Encryption Between an Instance and Boot Volumes or Block Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm
- Fetched: 2026-09-05 01:51 CDT

# Enabling In-Transit Encryption Between an Instance and Boot Volumes or Block Volumes

After you create a virtual machine (VM) instance, you can enable or disable in-transit encryption between the instance and its paravirtualized boot volume and block volume attachments.

All boot volume and block volume data at rest is always encrypted by the Oracle Cloud Infrastructure Block Volume service using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption. For more information, see[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
Important  
  
See this known issue:[In-transit encryption for a boot volume attachment can be edited when unsupported by the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#in-transit-encryption-for-boot-volume-attachment-can-be-edited-when-unsupported-by-image).

For permissions, see[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-permissions).

## Supported Shapes and Images

You can enable or disable in-transit encryption for existing instances that use these VM shapes:
- VM.Standard1 series
- VM.Standard.B1 series
- VM.Standard2 series
- VM.Standard3 series
- VM.Standard.E2 series
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex
- VM.Standard.E5.Flex
- VM.Standard.E6.Flex
- VM.Standard.A1.Flex
- VM.DenseIO1 series
- VM.DenseIO2 series
- VM.GPU3 series
- VM.GPU.A10 series
- VM.Optimized3.Flex

These shapes cannot be edited:
- VM.Standard.E2.1.Micro
- VM.DenseIO.E4.Flex
- VM.GPU2 series
- VM instances that run on dedicated virtual machine hosts

The following bare metal shapes support in-transit encryption by default for block volumes and boot volumes. This setting is not configurable and applies to all volume attachments to the instance.
- BM.Standard.E3.128
- BM.Standard.E4.128
- BM.DenseIO.E4.128
Note  
  

In-transit encryption is not enabled for these shapes in the following scenarios:
- Boot volumes for instances launched June 8, 2021 or earlier.
- Volumes attached to the instance June 8, 2021 or earlier

To enable in-transit encryption for the volumes in these scenarios, you need to detach the volume from the instance and then reattach it.

In-transit encryption is not supported on all other bare metal shapes.

In-transit encryption for boot volumes and block volumes is available for[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm). It is not supported in most cases for instances launched from custom images imported for "bring your own image" (BYOI) scenarios. To confirm support for certain Linux-based custom images,[contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Select Advanced options .
- Navigate to Launch options , toggle the Use in-transit encryption checkbox on or off.
- 

Select Save changes .

If the instance is running, it's rebooted. Confirm when prompted.
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to enable or disable in-transit encryption between an instance and its paravirtualized boot volume attachments:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
