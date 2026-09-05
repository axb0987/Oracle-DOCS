# Creating a License Record in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-license-records.htm
- Fetched: 2026-09-05 02:10 CDT

# Creating a License Record in License Manager

Create a license record for your product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-license-records.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-license-records.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/create-license-records.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- On the product license's details page, select License Records .
The License Records page opens. All license records for the product license are displayed in a table.
- From the Actions menu , select Add .
The Add license record panel opens.
- Enter the following

- Record Name : Specify a license record name. Avoid entering confidential information.
- Unique identifier : (Third Party only) Enter a unique identifier based on your contract with your licensor.
- License Term : You can specify if your license is unlimited (Unlimited License Agreement licenses), or has a specific count associated with it (Full Use licenses). Select either Perpetual or Term-Limited .

If selecting Perpetual , specify the Support Contract End Date .

If selecting Term-Limited , specify both the License End Date and the Support Contract End Date .
- License Quantity : Specify the license quantity available for use based on your contractual terms, and accounting for licenses used on-premises or on other cloud platforms. Select either Count or Unlimited .

If selecting Count , specify a license quantity value in the field (default is 1).
- Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Add .
The license record you created appears in the license record list.
- 

Use the[oci license-manager license-record create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/license-record/create.html)command and required parameters to create a license records for a product license:

```

```

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/CreateLicenseRecord)
