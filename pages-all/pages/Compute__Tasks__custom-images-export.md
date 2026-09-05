# Exporting Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm
- Fetched: 2026-09-05 01:50 CDT

# Exporting Custom Images

Export a Compute custom image in an Oracle Cloud Infrastructure compartment.

To perform an image export, you need write access to the Object Storage bucket for the image. For more information, see[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)and[Let users write objects to Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#write-objects-to-buckets). Also see[Moving Data to and from Object Storage](https://docs.oracle.com/iaas/Content/Object/data-migration.htm)for information on moving images in and out of Object Storage.
Tip  
  
To export a Compute instance, first create a custom image from the instance. See:[Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm). Then, follow these steps.
Note  
  
You can move virtual machine images from OCI to other cloud providers using export.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-export.htm#)
- 

#### To export an image using the Console
- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Identify the custom image that you're interested in.
- From the Actions menu (three dots), select Export .
- 

Specify the Object Storage location to export the image to:
- Export to an Object Storage bucket: Select a bucket. Then, enter a name for the exported image. Avoid entering confidential information.
- Export to an Object Storage URL: Enter the Object Storage URL.
- 

In the Image format list, select the format that you want to export the image to. The following formats are available:
- Virtual Machine Disk (.vmdk)
- Virtual Hard Disk (.vhd) for Hyper-V
- Virtual Disk Image (.vdi) for Oracle VM VirtualBox
- QEMU Copy On Write (.qcow2)
- Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format to export a custom image that you want to import into other tenancies or regions.
- Select Export image .

After you select Export image , the image state changes to Exporting . Images are a copy of the VM or BM instance boot volume and metadata when the image is created, capturing the current state of the instance. Exporting a custom image copies the data to the Object Storage location that you specified. You can still launch instances while the image is exporting, but you can't delete the image until the export has finished.

When the export is complete, the image state changes to Available . If the image state changes to Available , but you don't see the exported image in the Object Storage location you specified, the export failed, and you need to go through the steps again to export the image.
Note  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the[image export](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/export.html)command and required parameters to export a custom image:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to export an image:
- [ExportImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ExportImage)
