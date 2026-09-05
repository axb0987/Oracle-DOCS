# Listing an Instance's VNICs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing an Instance's VNICs

List the VNICs attached to a Compute instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm#)
- 

- Confirm you're viewing the compartment that contains the Compute instance you're interested in.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to view its details.
- Under Resources , select Attached VNICs .
The primary VNIC and any secondary VNICs attached to the instance are displayed. If the instance has two[active physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview), the VNICs are grouped by NIC 0 and NIC 1.
- 

Use the`oci compute vnic-attachment list`command and required parameters to list the VNICs attached to an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVnicAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
