# Private DNS Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/private-dns-logging.htm
- Fetched: 2026-09-05 02:41 CDT

# Private DNS Logging

You can use the Oracle Cloud Infrastructure Logging service to enable logging of private DNS resolvers.

Logs provide detailed private DNS query/response activity, letting you more easily troubleshoot, monitor and analyze private DNS resolver functionality.
Note  
  

A private DNS log entry isn't written for responses answered from cache. However, when the TTL expires for a cached entry, the next lookup for that name results in a DNS Log entry. This is done for performance reasons to avoid excessive logging when names have already been resolved by DNS.

Before you start using Oracle Cloud Infrastructure Logging:
- 

Get familiar with basic concepts and terminology used in the OCI Logging service. See[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)in the OCI Logging documentation.
- Be aware that Logging is only available for private DNS within a virtual cloud network (VCN) and not for Public DNS. See[Details for Private DNS Resolver Logs](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_privatedns.htm)for more about the contents of these logs.
- 

Create a group to manage access to log groups and log content. See[Creating a Group](https://docs.oracle.com/iaas/Content/Identity/groups/create-groups.htm)in the OCI IAM with Identity Domains documentation.
- 

Add the policy to enable management of logging on private DNS resolvers.

Replace &lt;group-name&gt; with the group or specific user you want to grant permissions to. Replace &lt;compartment-name&gt; with the compartment that the private DNS resolver resides in.

```

```

- 

Add the policies to let you create log groups and log content in OCI Logging. Replace &lt;group-name&gt; with the group or specific user you want to grant permissions to. Replace &lt;compartment-name&gt; with the compartment that log group or content resides in.

```

```

## Enabling and viewing logs

These instructions describe how to enable and view private DNS resolver logs directly from the VCN details page. For instructions about working with logs from the Logging service, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm)and[Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm).
- [Enabling Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/private-dns-logging-enable.htm)
- [Viewing Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/private-dns-logging-view.htm)
