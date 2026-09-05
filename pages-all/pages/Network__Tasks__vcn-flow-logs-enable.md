# Enabling Flow Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm
- Fetched: 2026-09-05 02:47 CDT

# Enabling Flow Logs

Enable VCN Flow Logs for subnets, instances, load balancers, or network load balancers.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm#)
- 

- On the Flow log configurations list page, select Enable flow logs . If you need help finding the list page, see[Listing and Viewing Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-view.htm#vcn-flow-logs-view).
- On the Basic Information page, enter a name to uniquely identify the flow log. You can edit the name later.
- In the Flow log destination section, select the log group to add the flow log to, or create a new one by following these steps:
- Select Create new log group .
- Enter a name to uniquely identify the log group. You can edit the name later.
- Select the compartment to create the log group in.
- (Optional) Enter a description to help you identify the log group later.
- (Optional) To apply tags to the log group, select Show tagging .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create log group .
- In the Capture filter section, select the capture filter to use to determine what is included in the log, or create a new one by following these steps:
- Select Create new capture filter .
- Enter a name to uniquely identify the capture filter. You can edit the name later.
- Select the compartment to create the filter in.
- In the Sampling rate list, select the percentage of network flow to capture. Log information is captured only for the specified percentage part of all traffic on the enablement points.
- Create at least one rule.

Capture filter rules are examined in order and run when matched. When the first match is found, remaining rules aren't examined or run. If you reorder the rules, the capture filter behavior changes. A maximum of 10 rules is allowed in a capture filter. See[Capture filters and rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap__capture_filters)for examples of rule behavior.

Each rule can state whether to include or exclude packets based on the traffic direction (ingress or egress), source or destination IPv4 CIDR or IPv6 prefix of the traffic, or the IP protocol used for the packet (TCP, UDP,[ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml),[ICMPv6](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)). Each protocol type offers further options appropriate for that protocol.
- (Optional) To apply tags to the capture filter, select Show tagging .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create capture filter. Select Save as stack to create a stack that you can use in a Terraform configuration. See[Overview of Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm)for more information.
- (Optional) To apply tags to the flow log, select Show tagging .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .
- On the Enablement points page, select Add enablement points .
- In the Add enablement point dialog box, select an enablement point type:

- Virtual cloud network captures flow logs for all VNICs in all subnets in a VCN.
- Subnet captures flow logs for all VNICs in a subnet.
- Resources lets you capture flow logs for specific instances, network load balancers, or one or more VNICs.
- Select Continue .
- To enable flow logs for a virtual cloud network , select a VCN.
- To enable flow logs for a subnet , select a VCN and then a subnet.
- To enable flow logs for a resource , select a resource type. You can select Instance VNIC , Network load balancer , or VNIC OCID .

- If you select Instance VNIC or Network load balancer , select a VCN and then a subnet, and then select an available resource in the subnet.
Note  
  
If you don't see the resource that you want to enable, be sure you selected the compartment, VCN, and subnet that contains the resource. You can also enable flow logs with one category at a time.
- If you select VNIC OCID , enter an OCID for each VNIC you want to capture flow logs for.
- Select Add enablement points .
- Select Next .
- Review the flow log information, and then select Enable flow logs .
- 

Before you can create a flow log, you must first create a[log group](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)and a[capture filter](https://docs.oracle.com/iaas/Content/Network/Concepts/capture-filters.htm).

Use the[oci logging log create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/create.html)command and required parameters to create a flow log in a log group:

```

```

In this example, the flow log configuration information is contained in the specified file`create_log.json`. For example:
```

```

For a complete list of parameters and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Before you can create a flow log, you must first create a[log group](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)and a[capture filter](https://docs.oracle.com/iaas/Content/Network/Concepts/capture-filters.htm).
Run the[CreateLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/CreateLog)operation to create a flow log in a log group. For example:
```

```
