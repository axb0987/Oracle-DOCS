# Listing Product Licenses in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm
- Fetched: 2026-09-05 02:11 CDT

# Listing Product Licenses in License Manager

View a list of the product licenses in License Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm#)
- 

Open the navigation menu and select Governance &amp; Administration . Under License Manager , select Product Licenses .
The Product licenses list page opens. All product licenses in the selected compartment are displayed in a table.

The Product Licenses page lists all product licenses in a table containing the following information:
- Product License : Displays the name of the license. This is a link you can select to display details of the license. For more information, see[Getting a Product License's Details in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm).
- Status : Displays the status of the license:
- Ok
- Incomplete
- Issues Found : For licenses that don't meet your licensing requirements.
- Warning

See[Viewing Product License Activity in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/overview-license-manager.htm)for Status field descriptions.
- Requirement
- Entitlement
- Metric
- License Records

You can view license entitlements and requirements, in the metric a license was created for, from the Product Licenses page. Licenses that don't meet your licensing requirements have a status of Issues Found .

## Filtering List Results

Use filters to limit the product licenses in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a product license to open its details page, where you can view its status and perform other tasks.

To perform an action on a product license directly from the list table, select an available option from the Actions menu in the row for that product license:
- View : Open the details page for the product license.
- Delete :[Delete the product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/delete-product-license.htm).

To add a product license, select Add Product Licenses .
- 

Use the[oci license-manager product-license list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/list.html)command and required parameters to list the product licenses in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListProductLicenses](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicenseCollection/ListProductLicenses)
