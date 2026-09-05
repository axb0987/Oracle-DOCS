# Adding or Removing a VNIC from a Network Security Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm
- Fetched: 2026-09-05 02:45 CDT

# Adding or Removing a VNIC from a Network Security Group

Learn to add or remove a VNIC from a network security group.

You can change which[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)(NSGs) a VNIC belongs to, or remove a VNIC from all NSGs.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm#)
- 

- Confirm you're viewing the compartment that contains the Compute instance you're interested in.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to view its details.
- Under Resources , select Attached VNICs .
The primary VNIC and any secondary VNICs attached to the instance are displayed.
- Select the name of the VNIC you're interested in.
Each VNIC's details page includes a list of the NSGs that the VNIC belongs to (if any).
- Next to Network Security Groups , select Edit .
- Make the needed changes. Avoid entering confidential information. Then, select Save Changes .
- 

Use the`oci network vnic update`command and required parameters to add or remove a VNIC from a network security group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic)
