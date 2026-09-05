# Updating a Service Gateway's Route Table Association
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm
- Fetched: 2026-09-05 02:47 CDT

# Updating a Service Gateway's Route Table Association

You can update a service gateway in a Virtual Cloud Network (VCN) to associate it with a route table or change the existing route table association.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- For the service gateway you're interested in, select the Actions menu (three dots) , and then select one of the following options:

- Associate With Route Table If the service gateway has no route table associated with it yet.
- Associate Different Route Table If you're changing which route table is associated with the service gateway.
- Select the compartment where the route table resides, and then select the route table itself.
- Select Associate .
- 

Use the[network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html)command and required parameters to update details for a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway)
