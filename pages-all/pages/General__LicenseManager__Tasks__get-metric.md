# Getting a Product License's Metric in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-metric.htm
- Fetched: 2026-09-05 02:10 CDT

# Getting a Product License's Metric in License Manager

View a product license's metric in License Manager.

Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for. When you create a product license, you're prompted to indicate the metric. The metric options differs depending on whether the vendor you're using is Oracle or a third party:
- Oracle : The metric value options are:
- Processors
- Named User Plus
- Third Party : The metric value is fixed as OCPU .

You can find out which metric a product license has by using of the following methods:

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-metric.htm#)
- 

- On the Product Licenses page, find the product license you want to work with. If you need help finding the list page or the product license, see[Listing Product Licenses in License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/../Tasks/list-product-license.htm).
The Product licenses list page opens. All product licenses in the selected compartment are displayed in a table. For information on finding a product license using filters, see[Listing Product Licenses](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-product-license.htm).
- Look at the Metric column for your product license.
- 

Use the command and required parameters to get a product license's metric:

```

```

`compartment_ocid`is the root compartment of your tenancy.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetLicenseMetric](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseMetric/GetLicenseMetric)
