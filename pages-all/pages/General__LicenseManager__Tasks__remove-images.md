# Removing an Image from a Product License in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/remove-images.htm
- Fetched: 2026-09-05 02:11 CDT

# Removing an Image from a Product License in License Manager

Remove an image to a product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/remove-images.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/remove-images.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/remove-images.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- Select Images .
The Images page opens. All images are displayed in a table.
- From the Actions menu , select Remove .
- When promoted, confirm the removal.
The Images page reappears with the image you removed no longer listed. You can repeat these steps to remove other images.
- 

Use the[oci license-manager product-license update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/update.html)command and required parameters to remove the images you want from the product license:

```

```

where`images`are the details associated with the images you're adding to the product license. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.
- 

Run the[UpdateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/UpdateProductLicense)operation to update a product license's settings. Include the`images`
