# Editing a Product License in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-product-license.htm
- Fetched: 2026-09-05 02:11 CDT

# Editing a Product License in License Manager

Update a product license's settings in License Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-product-license.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- Select and update any of the following product license settings:

- [Consumption](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license-consumers.htm).
- [License records](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Concepts/license-records.htm).
- [Images](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/images.htm).
- 

Use the[oci license-manager product-license update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/update.html)command and required parameters to update a product license's settings:

```

```

where`images`is the image details associated with the product license. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/UpdateProductLicense)
