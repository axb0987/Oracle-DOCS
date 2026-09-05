# Bastion Creation Failed
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting_bastion_creation_failed.htm
- Fetched: 2026-09-05 01:42 CDT

# Bastion Creation Failed

Fix problems that can occur when you attempt to create a bastion.

## Missing IAM Policies for Networking

To create a bastion, you need the following permissions:
- Manage bastions, sessions, and networks
- Read compute instances
- Read compute instance agent (Oracle Cloud Agent) plugins
- Inspect work requests

For example, if you don't have permission to manage networks, then you can't select a VCN (virtual cloud network) or subnet when creating a bastion using the Console.
Example policy:

```

```
See[Bastion IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../Reference/bastionpolicyreference.htm)for detailed policy information and more examples.

## Reached Your Service Limit

Your tenancy has a limit on the number of bastions that you can create. If you attempt to create a bastion after your tenancy has reached this service limit, then you see an error message similar to the following:
```

```

Either request a quota increase from your administrator, or delete unused bastions. To learn more, see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)
