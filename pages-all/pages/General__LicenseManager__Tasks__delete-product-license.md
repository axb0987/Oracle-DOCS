# Deleting a Product License from License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-product-license.htm
- Fetched: 2026-09-05 02:10 CDT

# Deleting a Product License from License Manager

Remove a product license from License Manager.
Note  
  
You can't delete a product license if it contains any license records. Delete all the license records first, then delete the product license

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-product-license.htm#)
- 

- On the Product Licenses page, find the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
- From the Actions menu , select Delete .
- When prompted, confirm the deletion.
The product license you deleted no longer appears in the product license list.
- 

Use the[oci license-manager product-license delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/delete.html)command and required parameters to delete a product license:

```

```

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/DeleteProductLicense)
