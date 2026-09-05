# Creating a Service Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a Service Gateway

Create a service gateway in a Virtual Cloud Network (VCN) to allow access to the Oracle Services Network (OSN).

Only one service gateway is needed for each VCN. All subnets within a VCN have access to the service gateway if the security rules and route table rules allow that access.

This task assumes that you already have a VCN with at least one subnet (either private or public).
Important  
  

The service gateway allows access to supported Oracle services within the region to protect data from the internet. Some applications might require access to public endpoints or services not supported by the service gateway (for example, to download updates or patches). Ensure you also have[access to the internet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/internetaccess.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to create a service gateway in. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section and select Create Service Gateway .
- Under Resources , select Service Gateways , and then select Create Service Gateway .
- Enter a friendly name for the gateway. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the gateway in. Select another compartment if needed.
- (Optional) In the Services section, Select the[service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview)that you're interested in. If you don't select one now, you can update the service gateway later and[add a service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm)then. Without a service CIDR label enabled for the gateway, no traffic flows through it.
- (Optional) In the Route Table Association section, you can associate a specific route table with this gateway. Specify this option only if you're setting up the advanced routing scenario called[transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm). Select the compartment that contains the route table that you want to associate with the LPG, and then select the route table. You can skip this part and associate the LPG with a route table later.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create Service Gateway .

The service gateway is then created and displayed on the Service Gateways page in the compartment that you chose. The gateway allows traffic through it by default. At any time, you can[block or allow the traffic through it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm).
- 

Use the[network service-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/create.html)command and required parameters to create a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/CreateServiceGateway)
