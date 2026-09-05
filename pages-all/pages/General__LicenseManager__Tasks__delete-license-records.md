# Deleting a License Record from License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-license-records.htm
- Fetched: 2026-09-05 02:10 CDT

# Deleting a License Record from License Manager

Remove a license record from a product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-license-records.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-license-records.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-license-records.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- On the product license's details page, select License Records .
The License Records page opens. All license records for the product license are displayed in a table.
- From the Actions menu for the license record, select Delete .
- When prompted, confirm the deletion.
The license record you deleted no longer appears in the license record list.
- 

Use the[oci license-manager license-record delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/license-record/delete.html)command and required parameters to delete a license record:

```

```

You can get the license record OCID by listing the license records. For more information, see[Listing License Records in for a Product License in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/DeleteLicenseRecord)
