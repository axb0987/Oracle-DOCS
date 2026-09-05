# Adding a Service CIDR Label to a Service Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm
- Fetched: 2026-09-05 02:43 CDT

# Adding a Service CIDR Label to a Service Gateway

Add a specified service CIDR label to the service gateway.

Important  
  

Because Object Storage is covered by both OCI &lt;region&gt; Object Storage and All &lt;region&gt; Services in Oracle Services Network , a service gateway can use only one of those service CIDR labels . Likewise, a route table can have a single rule for one of the service CIDR labels. It can't have two separate rules, one for each label.

If the service gateway is configured to use All &lt;region&gt; Services in Oracle Services Network , the route rule can use either CIDR label. However, if the service gateway is configured to use OCI &lt;region&gt; Object Storage and the route rule uses All &lt;region&gt; Services in Oracle Services Network , traffic to services in the Oracle Services Network except Object Storage gets dropped or blackholed. The Console prohibits you from configuring the service gateway and corresponding route table in that manner.

To switch the service gateway to use a different service CIDR label, see[When You Switch to a Different Service CIDR Label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/service-gateway_management.htm#switch_label).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- For the service gateway that you're interested in, select the Actions menu (three dots) , and then select Edit .
- (Optional) You can rename the service gateway if you decide to.
- In the Services field, select the appropriate[service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview). Without a service CIDR label enabled for the gateway, no traffic flows through it.
- Select Save changes .

What's Next

- Update route tables for any subnets that need to access the service gateway. See instructions in[Task 2: Update routing for the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_routing).
- Update relevant security rules. See instructions in[Task 3: (Optional) Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_security_list).
- 

Use the[network service-gateway attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/attach.html)command and required parameters to add a[service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview)to a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

:

Run the[AttachServiceId](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/AttachServiceId)operation to add a[service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview)to a service gateway.

Use[ListServices](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Service/ListServices)to determine the available service CIDR labels.[GetService](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Service/GetService)
