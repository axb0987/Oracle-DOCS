# Updating a VNIC
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm
- Fetched: 2026-09-05 02:45 CDT

# Updating a VNIC

Update a specified VNIC.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-update.htm#)
- 

- Confirm you're viewing the compartment that contains the Compute instance you're interested in.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to view its details.
- Under Resources , select Attached VNICs .
The primary VNIC and any secondary VNICs attached to the instance are displayed.
- For the VNIC you want to edit, select the Actions menu (three dots) , and then select Edit VNIC .
- Make the required changes. Avoid entering confidential information.
When you update information for a VNIC, you also have the following option:
- Route Table: (Optional) Assign a custom route table to this IP address. See[Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing)for more details. If you use this option, remember that traffic from this IP address doesn't use the default VCN or subnet route tables.
- When you're finished, select Save Changes .
- 

Use the`oci network vnic update`command and required parameters to update the specified VNIC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic)
