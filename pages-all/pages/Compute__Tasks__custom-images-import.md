# Importing Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm
- Fetched: 2026-09-05 01:50 CDT

# Importing Custom Images

Import a Compute custom image in an Oracle Cloud Infrastructure compartment.

To import an image, you need read access to the Object Storage object containing the image. For more information, see[Let users download objects from Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#download-objects-from-buckets). Also see[Moving Data to and from Object Storage](https://docs.oracle.com/iaas/Content/Object/data-migration.htm)for information on moving images in and out of Object Storage.
Note  
  
You can move virtual machine images from other cloud providers into OCI using import.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-import.htm#)
- 

- Navigate to the Compute Custom images list page. If you need help finding the list page, see[Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/custom-images-list.htm).
- Select Import image .
- In the Create in compartment list, select the compartment that you want to import the image to.
- Enter a name for the image. Avoid entering confidential information.
- 

Select the operating system:
- For Linux images, select Linux .
- For Windows images, select Windows . Select the operating system version, and then certify that the selected operating system complies with Microsoft licensing agreements.
- 

Specify the[Object Storage location](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs)to import the image from:
- Import from an Object Storage bucket: Select the bucket that contains the image. In the Object name list, select the image file.
- Import from an Object Storage URL: Enter the object storage URL of the image. When importing across tenancies, you must specify a pre-authenticated request URL.
- 

In the Image type section, select the format of the image. The following formats are available:
- VMDK: Virtual Machine Disk (.vmdk)
- QCOW2: QEMU Copy On Write (.qcow2)
- OCI: Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format when importing a custom image that was exported from another tenancy or region.
- 

Select the launch mode:
- 

For custom images where the image type is`.oci`, the launch mode is disabled. Oracle Cloud Infrastructure selects the appropriate launch mode based on the launch mode for the source image.
- 

For custom images exported from Oracle Cloud Infrastructure where the image type is QCOW2, select Native mode .
- 

To import other custom images, select Paravirtualized mode or Emulated mode . For more information, see[Bring Your Own Image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bringyourownimage.htm#options__launchmodes).
- (Optional) In the Tags section, add one or more tags to the image. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Import image .

After you select Import image , you'll see the imported image in the Custom images list for the compartment, with a state of Importing .

When the import completes successfully, the state changes to Available . If the state does not change, or no entry appears in the Custom images list, the import failed. If the import failed, ensure you have read access to the Object Storage object, and that the object contains a supported image.
Note  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the[image create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/create.html)or[image import](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/import.html)command and required parameters to import a custom image:

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to import an image:
- [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage)
