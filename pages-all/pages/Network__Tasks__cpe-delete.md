# Deleting a CPE
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a CPE

Delete a CPE in Oracle Cloud Infrastructure.

Prerequisite: The CPE must not be connected to a DRG or an IPSec connection.

The CPE’s lifecycleState changes to TERMINATING temporarily until the CPE is removed.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm#)
- 

To delete a CPE, follow these steps:

- On the Customer-premises equipment list page, find the CPE that you want to delete. If you need help finding the list page, see[Listing CPEs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm).
- From the Actions menu (three dots) for the CPE you want to delete, select Delete .
- When prompted, confirm the deletion.

The object is in the Terminating state for a short period while it's being deleted.
- 

Use the[network cpe delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/delete.html)command and required parameters to delete a CPE:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/DeleteCpe)
