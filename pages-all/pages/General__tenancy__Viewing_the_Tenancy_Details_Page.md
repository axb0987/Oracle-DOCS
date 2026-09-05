# Getting a Tenancy's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/General/tenancy/Viewing_the_Tenancy_Details_Page.htm
- Fetched: 2026-09-05 02:13 CDT

# Getting a Tenancy's Details

View the details for a tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/tenancy/Viewing_the_Tenancy_Details_Page.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/tenancy/Viewing_the_Tenancy_Details_Page.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/tenancy/Viewing_the_Tenancy_Details_Page.htm#)
- 

In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- 

Use the[get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tenancy/get.html)command and required parameters to get a tenancy's details:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetTenancy](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tenancy/GetTenancy)operation to get a tenancy's details.

Many of the options set on this page are managed through the owning service. For example, the Object Storage settings are managed with the[Object Storage service API](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm), and setting the Audit log retention period is handled by the Audit service API.

To tag a tenancy, use the following operations:
- [GetCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/GetCompartment)
- [UpdateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/UpdateCompartment)

In the above operations, use the tenancy OCID for the`compartmentID`
