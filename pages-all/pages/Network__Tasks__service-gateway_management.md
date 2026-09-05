# Service Gateway Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/service-gateway_management.htm
- Fetched: 2026-09-05 02:47 CDT

# Service Gateway Management

Describes how to create and manage service gateways that can be used to provide access to services hosted in the Oracle Services Network.

For the purposes of management access control, you must specify the compartment where you want the service gateway to reside. Consult the primary tenancy administrator if you're not sure which compartment to use. For information about compartments and access control, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).

The following basic management actions are available for service gateways:
- [Creating a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm)
- [Listing Service Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm)
- [Getting Details for a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-sgw.htm)
- [Updating a Service Gateway's Route Table Association](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm)
- [Controlling Traffic for a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm)
- [Adding a Service CIDR Label to a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm)
- [Removing or Changing a Service Gateway's Service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm)
- [Moving a Service Gateway to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm)
- [Deleting a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm)

## When You Switch to a Different Service CIDR Label

To avoid disrupting your Object Storage connections while switching between the OCI &lt;region&gt; Object Storage service CIDR label and All &lt;region&gt; Services in Oracle Services Network , use the following process:
- Update the service gateway: See[Removing or Changing a Service Gateway's Service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm). You can't enable both labels for the service gateway.
- [Update relevant route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm): For each rule that uses the service gateway as the target, switch the rule's destination service from the existing service CIDR label to the one you want to switch to.
- Update relevant security rules: Change any security rules that specify the existing service CIDR label to instead use the one you want to switch to. The rules can be in[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)or[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm).
