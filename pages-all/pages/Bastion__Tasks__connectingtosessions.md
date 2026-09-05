# Connecting to Sessions in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connectingtosessions.htm
- Fetched: 2026-09-05 01:42 CDT

# Connecting to Sessions in Bastion

This topic describes how to connect to bastion sessions.

For information about how to create and manage bastion sessions, see[Managing Sessions in Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingsessions.htm). For information about creating and managing bastions, see[Managing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingbastions.htm).

Bastions are Oracle-managed services. You use a bastion to create Secure Shell (SSH) sessions that provide access to other private resources. But you can't connect directly to a bastion with SSH and administer or monitor it like a traditional host.

When connecting to a bastion session, we recommend that you follow the SSH best practices described in[Securing Bastion](https://docs.oracle.com/iaas/Content/Security/Reference/bastion_security.htm).

You can connect to the following types of sessions:
- [Connecting to a Managed SSH Session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-managed-ssh.htm)
- [Connecting to a Port Forwarding Session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm)
- [Connecting to a Dynamic Port Forwarding (SOCKS5) Session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-dynamic-port-forwarding.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, you must be granted security access in a policy by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which compartment to work in.

To use all Bastion features, you must have the following permissions:
- Manage bastions, sessions, and networks
- Read compute instances
- Read compute instance agent (Oracle Cloud Agent) plugins
- Inspect work requests
Example policy:

```

```
See[Bastion IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Reference/bastionpolicyreference.htm#bastionpolicyreference)for detailed policy information and more examples.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Allowing Network Access From the Bastion

The VCN (virtual cloud network) that the target resource was created in must allow incoming network traffic from the bastion on the target port.

For example, if you want to use a session to connect to port`8001`on a compute instance from a bastion with the IP address`192.168.0.99`, then the subnet used to access the instance needs to allow ingress traffic from`192.168.0.99`on port`8001`.

- On the Bastions list page, find the bastion that you want to work with. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- Select the name of the bastion.
- Copy the Private endpoint IP address .
- Select the Target subnet .

If the target resource is on a different subnet than the one used by the bastion to access this VCN, edit the target resource's subnet.
- From the Subnet Details page, click an existing security list that is assigned to this subnet.

Alternatively, you can create a security list and assign it to this subnet.
- Select Add Ingress Rules .
- For Source CIDR , enter a CIDR block that includes the Private endpoint IP address of the bastion.

For example, the CIDR block`<bastion_private_IP> /32`includes only the bastion's IP address.
- For IP Protocol , select TCP .
- For Destination Port Range , enter the port number on the target resource.

For Managed SSH sessions, specify port 22.
- Select Add Ingress Rules .

To learn more, see[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)
