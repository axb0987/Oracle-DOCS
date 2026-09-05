# Listing Internet Gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing Internet Gateways

List the internet gateway.
A VCN normally only needs one internet gateway. Any public subnet in a VCN can use the internet gateway, if the route table and security list it uses allows the traffic.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Internet Gateways section.
- Under Resources , select Internet Gateways .

All internet gateways in the VCN are displayed in a table.
- 

Use the[network internet-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/list.html)command and required parameters to list the internet gateways in a specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListInternetGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/ListInternetGateways)operation to list the internet gateways.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
