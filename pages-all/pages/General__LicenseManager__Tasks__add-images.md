# Adding an Image to a Product License in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/add-images.htm
- Fetched: 2026-09-05 02:10 CDT

# Adding an Image to a Product License in License Manager

Add an image to a product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/add-images.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/add-images.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/add-images.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- Select Images .
The Images page opens. All images are displayed in a table.
- Select Add Images .
The Browse all images panel opens. The Image Source box displays the origin of the images displayed.
- Find the image you want to add and select it. Expand the list next to each image entry to display more options, such as the version to select from.
- Accept the terms and conditions agreement at the bottom of the panel. You can't add an image without selecting this box.
- Select Select Image .
The Images page reappears with the image you added listed. You can repeat these steps to add other images.
- 

Use the[oci license-manager product-license update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/update.html)command and required parameters to add the images you want to the product license:

```

```

where`images`are the details associated with the images you're adding to the product license. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.
- 

Run the[UpdateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/UpdateProductLicense)operation to update a product license's settings. Include the`images`
