# Listing Resource License Requirements in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license-consumers.htm
- Fetched: 2026-09-05 02:10 CDT

# Listing Resource License Requirements in License Manager

View a list of the resources that are attributed to a license and their individual licensing requirements.

You can view BYOL resource license requirements in the tenancy in the product license's Consumption page. This feature allows you to view the resources that are attributed to a license and their individual licensing requirements. Data is delayed by one hour.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license-consumers.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license-consumers.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license-consumers.htm#)
- 

- On the Product Licenses page, select the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The product license's details page opens.
- Select Consumption .
The Consumption page opens.
The table containing the information in the Consumption page is organized using the following categories:
- Resource OCID : Select the link to go directly to the particular BYOL resource.
- Product Name : The license product (ECPU-supported products are indicated in this field).
- Compartment : The associated compartment.
- Requirement ( &lt;type&gt; ): The license, where &lt;type&gt; refers to the metric type.

The warning icon indicates that you might not have licenses created for mandatory options to meet the licensing needs of a specific resource, per the license portability rules. You can navigate directly to the resources shown in the list by selecting the direct link for each resource OCID shown in the list. As a result, you can make changes as needed.

Select Download CSV to get a CSV version of the consumption information. The CSV file also has the same field listing as the Consumption table, including a Missing Licensing Requirements field. The OCI Metric of Resource field in the CSV file also indicates whether the resource refers to OCPU or ECPU.
- 

Use the[oci license-manager product-license list-product-license-consumers](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/list-product-license-consumers.html)command and required parameters to list of the resource license requirements for a product license:

```

```

You can get the product license OCID by listing the product licenses. For more information, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListProductLicenseConsumers](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicenseConsumerCollection/ListProductLicenseConsumers)
