# Listing the Most Used OCI Resources in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-top-utilized-resources.htm
- Fetched: 2026-09-05 02:11 CDT

# Listing the Most Used OCI Resources in License Manager

View a list of the of the most used OCI resources in a compartment.

You can view the most used BYOL resource by OCPUs and by ECPUs. The following information is displayed:
- Resource : The OCID of the resource.
- OCPU/ECPU : The number of OCPUs or ECPUs used by the resource.
- Compartment : The name of the compartment containing the resource.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-top-utilized-resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-top-utilized-resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/list-top-utilized-resources.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under License Manager , select Overview .
The License Manager Overview page opens.
- Find the Top BYOL Resource by OPCUs and Top BYOL Resource by EPCUs sections.
The Top Utilized Product Licenses section lists the most used product licenses as a table. Use the filter option to find the product licenses you want.
- 

Use the[oci license-manager product-license list-top-utilized-resources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/product-license/list-top-utilized-resources.html)command and required parameters to list the most utilized OCI resources in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListTopUtilizedResources](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/TopUtilizedResourceCollection/ListTopUtilizedResources)
