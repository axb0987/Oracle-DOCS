# Updating an Internet Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm
- Fetched: 2026-09-05 02:47 CDT

# Updating an Internet Gateway

Update an internet gateway (IGW) in a Virtual Cloud Network (VCN) in Networking.

You can't change the display name or disable or enable an internet gateway by using the Console, but you can do both using the CLI or API. If the gateway is disabled, that means no traffic flows to or from the internet even when a route rule allows that traffic.

You can associate a route table with the internet gateway, move it to a different compartment, terminate it, and also change its tags. After a route table is associated with a gateway, the gateway must always have a route table associated with it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm#)
- 

To associate a route table to an internet gateway:

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Internet Gateways section.
- Under Resources , select Internet Gateway .
- Select the the Actions menu (three dots) for the internet gateway, and then select Associate Route Table .
- Select a different route table, changing the compartment as needed to find the one that you want. Then, select Associate Route Table .
You can also use the the Actions menu (three dots) to move the internet gateway to a different compartment, delete it, or change its tags.
- 

Use the[network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html)command and required parameters to change the display name of the specified internet gateway:

```

```

Use the[network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html)command and required parameters to enable or disable the specified internet gateway:

```

```

Use the[network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html)command and required parameters to associate a route table to the specified internet gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/UpdateInternetGateway)operation to update the specified internet gateway.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
