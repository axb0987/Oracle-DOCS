# Getting a VNIC's properties
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm
- Fetched: 2026-09-05 02:45 CDT

# Getting a VNIC's properties

Get a VNIC's VLAN tag and other properties.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm#)
- 

- Confirm you're viewing the compartment that contains the Compute instance you're interested in.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Click the name of the instance to view its details.
- Under Resources , click Attached VNICs .
- Click the name of the primary or secondary VNIC to view its details.
- 

Use the`oci compute vnic-attachment get`command and required parameters to get the VNIC's VLAN tag and other properties:

```

```

Use the`oci network vnic get`command and required parameters to get the VNIC's private IP address, MAC address, optional public IP address, optional DNS hostname, and other properties:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetVnicAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/GetVnicAttachment)operation to get the VNIC's VLAN tag and other properties. Run the[GetVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic)
