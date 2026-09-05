# Choosing Whether an Ephemeral Public IP Is Assigned at Instance Creation
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm
- Fetched: 2026-09-05 02:43 CDT

# Choosing Whether an Ephemeral Public IP Is Assigned at Instance Creation

You can choose whether to assign an ephemeral public IP address to an instance when you create it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm#)
- 

When you[create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)into a[public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public), there's an Automatically assign a public IPv4 address option inn the Networking step of the Create compute instance page workflow. By default, the option is selected, and the instance gets an ephemeral public IP.

If you don't want an ephemeral public IP assigned, you can either clear the option (switch off the toggle) or delete the ephemeral public IP after instance creation.
- 

Use the[network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html)command and required parameters to assign a public IP:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp)
