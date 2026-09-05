# Managing Bastions
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingbastions.htm
- Fetched: 2026-09-05 01:42 CDT

# Managing Bastions

Describes how to create and manage bastions.

For information about creating and managing sessions, see[Managing Sessions in Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingsessions.htm#managingsessions).

You can perform the following bastion management tasks:
- [Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm#top)
- [Creating a Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-bastion.htm#top)
- [Getting a Bastion's Details](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm#top)
- [Updating a Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm#top)
- [Managing a Bastion's Security Attributes](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/manage-security-attributes.htm#top)
- [Moving a Bastion to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/change-compartment-bastion.htm#top)
- [Deleting a Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/delete-bastion.htm#top)

## Adding Security Attributes

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

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

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
