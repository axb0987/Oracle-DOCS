# Deleting an Internet Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting an Internet Gateway

Delete an internet gateway from a Virtual Cloud Network (VCN) in Networking.

Prerequisite: Before you delete an internet gateway, delete all route rules in the VCN that specify the gateway as the target. Deleting those rules stops the routing in the VCN to the gateway. If a route rule references the gateway, it can't be deleted until the reference is removed.

See[Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)and[Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)for more about finding and updating route rules that reference` a gateway.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Internet Gateways section.
- Under Resources , select Internet Gateway .
- From the the Actions menu (three dots) for the gateway that you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network internet-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/delete.html)command and required parameters to delete an internet gateway:

```

```

- 

Run the[DeleteInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/DeleteInternetGateway)operation to delete an internet gateway.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
