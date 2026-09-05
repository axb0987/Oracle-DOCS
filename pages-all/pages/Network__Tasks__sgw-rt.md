# Associating a Route Table with an Existing Service Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm
- Fetched: 2026-09-05 02:47 CDT

# Associating a Route Table with an Existing Service Gateway

Associate a route table with a service gateway.

You perform this task only if you're implementing an[advanced transit routing scenario](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

A service gateway can exist without a route table associated with it. However, after you associate a route table with a service gateway, there must always be a route table associated with it. But, you can associate a different route table. You can also edit the table's rules, or delete some or all the rules.

Prerequisite: The route table must exist and belong to the VCN that the service gateway belongs to.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- For the service gateway you're interested in, select the Actions menu (three dots) , and then select Associate Route Table .
- Select a route table.
- Select Associate Route Table .
- 

Use the[network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html)command and required parameters to assign or update a route table to a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway)operation to associate a route table with a service gateway, using the`routeTableId`
