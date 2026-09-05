# Managing Sessions in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingsessions.htm
- Fetched: 2026-09-05 01:42 CDT

# Managing Sessions in Bastion

Describes how to create and manage bastion sessions.

For information about how to connect to bastion sessions, see[Connecting to Sessions in Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connectingtosessions.htm). For information about creating and managing bastions, see[Managing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/managingbastions.htm).

Before you begin, decide which type of session you want to create: Managed SSH session , SSH port forwarding session , or Dynamic port forwarding (SOCKS5) session . See[Session Types](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Concepts/bastionoverview.htm#session_types).

Bastions are essential in tenancies with stricter resource controls. For example, you can use a bastion session to access Compute instances in compartments that are associated with a security zone . Instances in a security zone can't have public endpoints. To learn more, see[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/security-zones.htm).

You can perform the following session management tasks:
- [Listing Sessions in a Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-session.htm)
- [Creating a Session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session.htm)
- [Getting a Session's Details](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-session.htm)
- [Editing a session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-session.htm)
- [Deleting a Session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/delete-session.htm)

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
