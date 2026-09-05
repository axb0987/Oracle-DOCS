# Getting a Product License's Details in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm
- Fetched: 2026-09-05 02:10 CDT

# Getting a Product License's Details in License Manager

View a product license's details in License Manager.

You can access and view the following information for a product license:
- OCID
- Entitlement
- Metric
- Vendor
- Compartment
- Type
- Requirement : Indicates the license requirement status and value. A green status indicates that the product is fully licensed. A red status indicates an overage, for cases where the license requirement exceeds the entitlement.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm#)
- 

On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).

The product license's details page opens. Here you can view the overall status of the product license.
- 

Use the[oci license-manager product-license get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/get.html)command and required parameters to get a product license's details:

```

```

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/GetProductLicense)
