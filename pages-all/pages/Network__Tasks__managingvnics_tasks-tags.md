# Managing Tags for a VNIC
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm
- Fetched: 2026-09-05 02:45 CDT

# Managing Tags for a VNIC

Learn to manage resource tags for a VNIC.

For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm#)
- 

- Confirm you're viewing the compartment that contains the Compute instance you're interested in.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to view its details.
- Under Resources , select Attached VNICs .
The primary VNIC and any secondary VNICs attached to the instance are displayed.
- Select the name of the VNIC you're interested in.
- Select the Tags tab to view or edit the existing tags. Or select Add Tags to add new ones.
- 

Use the`oci network vnic update`command and required parameters to manage resource tags for a VNIC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic)
