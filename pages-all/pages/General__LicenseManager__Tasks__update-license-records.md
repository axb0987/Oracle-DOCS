# Editing a License Record in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-license-records.htm
- Fetched: 2026-09-05 02:11 CDT

# Editing a License Record in License Manager

Update a license record's settings in a product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-license-records.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-license-records.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-license-records.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- On the product license's details page, select License Records .
The License Records page opens. All license records for the product license are displayed in a table.
- From the Actions menu for the license record, select Edit .
The Edit License Record panel opens.
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a License Record](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-license-records.htm).
- Select Save .
- 

Use the[oci license-manager license-record update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/license-record/update.html)command and required parameters to edit a license record:

```

```

You can get the license record OCID by listing the license records. For more information, see[Listing License Records in for a Product License in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/UpdateLicenseRecord)
