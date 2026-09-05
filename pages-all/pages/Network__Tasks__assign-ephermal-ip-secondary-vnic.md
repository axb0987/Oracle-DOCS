# Assigning an Ephemeral Public IP When Creating a Secondary VNIC
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm
- Fetched: 2026-09-05 02:43 CDT

# Assigning an Ephemeral Public IP When Creating a Secondary VNIC

When you add a secondary VNIC to an instance, you choose whether the primary private IP on the new VNIC gets an ephemeral public IP.

For more information, see[https://docs.oracle.com/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm](https://docs.oracle.com/iaas/Content/Network/Tasks/managingvnics_tasks-attach.htm)

This choice is available only if the secondary VNIC is in a[public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm#)
- 

On the Create VNIC page, the Automatically assign public IPv4 address option is not selected by default, which means that the secondary VNIC doesn't get an ephemeral public IP address. You must select Automatically assign public IPv4 address .

.
- 

Use the[network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html)command and required parameters to assign a public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp)
