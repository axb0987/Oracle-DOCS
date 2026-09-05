# Exporting OCI Marketplace-Based Solutions for Use on Roving Edge Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/exporting_marketplace_listings.htm
- Fetched: 2026-09-05 03:02 CDT

# Exporting OCI Marketplace-Based Solutions for Use on Roving Edge Devices

Learn about how you can use OCI Marketplace applications in your Roving Edge Infrastructure device.

You can only use the Marketplace solutions that are listed as "Free" or "Bring-your-own-license (BYOL)," and meet other Roving Edge Infrastructure compatibility requirements. You can identify these solutions by using the "Roving Edge Exportable" filter in OCI Marketplace. See[Overview of Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/Concepts/marketoverview.htm)for a full description of how to use OCI Marketplace.

You can export selected solutions from the OCI Marketplace by creating a custom image and importing the image into an Object Storage bucket in your OCI tenancy.

After the image is in your OCI bucket, import the image to the Roving Edge device using one of the following methods:
- If the device has connectivity to your OCI tenancy, import the image using the data sync feature. See[Roving Edge Infrastructure Data Synchronization](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).
- If the device isn't connected to your OCI tenancy, from the Roving Edge device, use the Object Storage object download API to import the image. See[Downloading an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#top)and select the API tab.

- Access OCI Marketplace and select All Applications .

For information about accessing the Oracle Cloud Marketplace, see[Accessing Oracle Cloud Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/overview-marketplace.htm#top__accessing).
- In the search field, enter Roving Edge Exportable .
Only those applications that you can export to Roving Edge Infrastructure are displayed. Each listing displays the type (Image only) and the pricing (Free or BYOL).
- Select the listing you want to attach. The details for that listing appear.
- Accept the Oracle terms of use and select Launch Instance . The Create compute instance dialog box appears.
- Complete the compute instance configuration. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)for general information on creating instances.
- Select Create . The Details page of the instance you created appears.
- Select Create custom image from the More Actions menu. The Create custom image dialog box appears.

Note  
  

If Create custom image isn't available in the More Actions menu, it indicates the application that you selected isn't Roving Edge exportable (see Step 2).
- Select the Compartment and Name for the custom image.
- Select Create custom image . The Work Request page appears, displaying the status of the custom image creation. Wait until the page indicates that the custom image is created before continuing to the next step.
- Open the Compute page and select Custom Images . The list of custom images in the selected compartment appears.
- Select the custom image you want to export from the list. The Details page of the custom image you selected appears.
- Select Export . The Export image dialog box appears.

Note  
  

If Export isn't available in the Details page, it indicates that the application you selected isn't Roving Edge exportable (see Step 2).
- Select the Export to an Object Storage bucket option.
- Select the Bucket in &lt;compartment&gt; in which the custom image is exported from the list. Select Change Compartment to select a bucket in a different compartment.
- Enter the Image name of the custom image.
- Select the Image format from the list. The image format must be one of the following:

- Oracle Cloud Infrastructure File with QCOW2 image and OCI metadata (`.oci`)
- QEMU Copy on Write (`.qcow2`)
-
