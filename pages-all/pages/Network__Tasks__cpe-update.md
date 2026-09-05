# Updating a CPE
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm
- Fetched: 2026-09-05 02:43 CDT

# Updating a CPE

Update configuration details for the specified CPE object.

When you update a CPE object, you can change its name and CPE vendor information. If the CPE object wasn't created to support IPSec over FastConnect, you can't change that decision later.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-update.htm#)
- 

- On the Customer-premises equipment list page, select the CPE that you want to work with. If you need help finding the list page, see[Listing CPEs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm).
- Select Edit .
- Edit the display name or other information as necessary. Avoid entering confidential information.
- Select Save Changes .
- 

Use the[network cpe update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/update.html)command and required parameters to update configuration details for the specified CPE object:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/UpdateCpe)
