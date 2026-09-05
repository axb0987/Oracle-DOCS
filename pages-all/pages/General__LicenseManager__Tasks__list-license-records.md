# Listing License Records in for a Product License in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm
- Fetched: 2026-09-05 02:10 CDT

# Listing License Records in for a Product License in License Manager

View a list of the license records in a product license.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-license-records.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- On the product license's details page, select License Records .
The License Records page opens. All license records for the product license are displayed in a table.
The license records table contains the following categories:
- 

Record Name : Select the linked record name to open the license record details page, or select View from the Actions menu. From the license record details page, you can delete the record or add tags. The following information is displayed:
- OCID
- Entitlement
- Metric
- Support End Date
- Product
- License Term
- Customer Support Identifier (CSI)
- Customer Support Identifier (CSI)
- Quantity
- License Expiration
- Support Expiration Date : If a license is at or near (within 90 days) its expiration date, the status is indicated in this field.

## Filtering List Results

Use filters to limit the product licenses in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a license record to open its details page, where you can view its status and perform other tasks.

To perform an action on a license record directly from the list table, select an available option from the Actions menu in the row for that license record:
- View : Open the details page for the license record.
- Delete :[Delete the product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-license-records.htm).
- Edit :[Update the license record's settings](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/update-license-records.htm).

To add a license record, select Add Licenses Record .
- 

Use the[oci license-manager license-record list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/license-record/list.html)command and required parameters to list the license records for a product license:

```

```

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListLicenseRecords](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecordCollection/ListLicenseRecords)
