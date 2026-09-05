# Using LDAP for Authorization
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm
- Fetched: 2026-09-05 02:03 CDT

# Using LDAP for Authorization

Learn how to use LDAP for authorization with File Storage.

You can use Lightweight Directory Access Protocol (LDAP) as a network information service to provide authorization information to the File Storage service. Using LDAP to provide authorization information provides the following benefits:
- Centralized management of UNIX users and groups.
- Support for up to 256 UNIX groups. If you enable LDAP for secondary UNIX groups rather than using the group list provided within an NFS request's RPC header, you're not subject to the AUTH_SYS limitation of 16 groups.
- LDAP infrastructure is a requirement for[per user authentication when using Kerberos](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm). LDAP isn't required for all Kerberos scenarios, such as when the export is squashing all.

## Secondary Group Lookup

File Storage file systems authorize access using the NFS operation's UID/GID and list of secondary UNIX groups. By default, AUTH_SYS uses the group list provided within the NFS request's RPC header.

When LDAP authorization is enabled, File Storage uses the UNIX UID from the NFS request's RPC header to retrieve the list of secondary UNIX groups from the LDAP server for AUTH_SYS access. The existing GIDLIST in the RPC header is overwritten with the GIDLIST from the LDAP server. Retrieving secondary UNIX groups from an LDAP server allows the authorization request to use up to 256 groups.

If secondary group lookup using ID mapping is enabled, but not configured, incorrectly configured, or the LDAP service is unavailable, File Storage can't update the secondary group list used in the request. This can result in[permissions errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/permission-denied-ldap-lookup.htm).

NFS Request Scenarios for AUTH_SYS
LDAP for Group List Enabled? LDAP Response Export Squash Enabled? NFS Request
Any Any Yes (all)

If squashing all, proceeds with Squash UID and Squash GID set in the export's options.

No secondary group list.
Any Any Yes (root)

If squashing root, proceeds with Squash UID and Squash GID set in the export's options only if UID is 0.

No secondary group list.
No Not applicable No Proceeds with UID/GIDs from RPC header.
Yes UID match No Uses the secondary group list retrieved from the LDAP server.
Yes No UID match, or any LDAP error No Proceeds with UID/GIDs from RPC header. No secondary group list.
Important  
  
To use LDAP for authorization, you must Enable LDAP for the mount target and at the export.

If you're using Kerberos authentication along with LDAP, behavior is slightly different. For more details, see[LDAP Lookups and Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#overview__ldap-anon).

## Caching

File Storage uses an in-memory only, on-demand caching model to store authorization information to increase performance and reduce the load on your LDAP server.

When an NFS request is made, File Storage contacts your LDAP server for authorization information. File Storage caches the authorization information, whether positive or negative, for use in subsequent NFS operations.

You can configure how long File Storage caches this information when you[configure a mount target for LDAP](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#updating-mts-for-ldap)using the following options:
- Cache Refresh Interval In Seconds : The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry. Choose a value that balances security implications and an acceptable load on your LDAP server.
- Cache Lifetime In Seconds : The maximum amount of time the mount target is allowed to use a cached entry. If cache entries can't be refreshed in a timely fashion because of load or failures in customer infrastructure, it is useful to use old entries until connectivity is restored. Set the value to the longest period of time that you're willing to have a stale entry in the LDAP cache, including cases of unavailability of the LDAP server for any reason.
- Negative Cache Lifetime In Seconds : The amount of time that a mount target maintains information that a user is not found in the ID mapping configuration. If a user isn't found in the LDAP database, the mount target places an entry in the cache noting that the user doesn't exist. Choose a value that balances security implications and an acceptable load on your LDAP server.

## Prerequisites

Requirements:
- Customer-managed LDAP infrastructure, including an LDAP server that supports an RFC2307 posix or RFC2307bis schema. The LDAP servers can be based on OpenLDAP or Microsoft Active Directory. Customized configuration might be required for File Storage support of the LDAP directory.
- 

A login account to the LDAP server that a File Storage mount target can use to look up RFC2307 and RFC2307bis-compliant user and group information.
- The LDAP server must have the following user attributes:
- ObjectClass: posixAccount – This object class provides the following attributes for the user.
- uidNumber – UNIX user ID.
- gidNumber – UNIX group ID of the primary group of the user.
- uid – The username for the user
- The LDAP server must have the following group attributes:
- ObjectClass: posixGroup – This object class provides the following attributes for the group.
- gidNumber - UNIX group ID for the group
- memberUid – (Only applicable if you're using RFC2307) The uid attribute of the users who are members of this group. To include several users in the group, add this attribute many times.
- UniqueMember - (Only applicable if you're using RFC2307bis) The DN (Distinguished Name) of users who are members of this group. To include several users in the group, add this attribute many times.
Tip  
  
You can[test for LDAP schema support](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-prereqs-test-queries).
- If your LDAP server uses a certificate that isn't issued by a public certificate authority (CA) (for example, a private CA or self-signed certificate), upload the trusted certificate to OCI Vault as a plain text[secret](https://docs.oracle.com/iaas/Content/secret-management/Tasks/create-secret.htm). Then, when you[create](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm#top)the outbound connector, select the trusted certificate secret and secret version.
Tip  
  
Upload the root CA certificate. However, if your LDAP server doesn't present the full certificate chain during TLS, upload the root CA certificate and intermediate certificates concatenated as a single PEM.
- A DNS server to enable the mount target to look up hostnames, including the LDAP server.
[
- Communication with DNS service over TCP/UDP port 53.
- Communication with customer-managed LDAP service over the TCP port configured in the outbound connector. The default value is TCP port 636.
- Data encrypted at rest in File Storage.

### LDAP Infrastructure

File Storage requires an[outbound connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managing-outbound-connectors.htm)so that mount targets can communicate with an LDAP server on its LDAPS port. The outbound connector requires that you provide the fully qualified domain name (FQDN) of LDAP server, a bind username and password to LDAP server, and the search base for users and groups.

To allow File Storage to reach the LDAP server, ensure the following:
- The LDAP server's firewall must allow inbound traffic from the File Storage mount target using TCP 636 (default).
- Any[security lists and NSGs](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Ways)in use must allow the mount target and LDAP server traffic.
- DNS is configured for the mount target and clients to resolve hostname. DNS configuration options include:
- Using OCI DNS with default resolution and hostnames in your VCN - This option doesn't offer the flexibility of custom DNS names. Hostnames end with`oraclevcn.com`with subdomains for VCN and subnet. See[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)for more information.
- Using OCI[Private DNS](https://docs.oracle.com/iaas/Content/DNS/Tasks/privatedns.htm)with private zones - DNS zones for a custom domain are hosted in OCI DNS. With this option, there's no need to manage your own DNS server, because OCI fully manages DNS. You must manage the zones and records. See[Private DNS](https://docs.oracle.com/iaas/Content/DNS/Tasks/privatedns.htm)for more information.
- Using a customer-managed DNS server - When you create a VCN, don't select Use DNS hostnames in this VCN . Instead, configure the VCN to use your own DNS server using one of the following methods:
- Configure[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm)in the subnet to use a customer-managed DNS server.
- Use the[VCN resolver](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm#Choices)with a forwarding endpoint and a forwarding rule so that DNS queries in the VCN are forwarded to a customer-managed DNS server.

File Storage doesn't support SSLv2, SSLv3, TLSv1, or TLSv1.1 for LDAPS authorization. File Storage supports the following OpenSSL cipher suites for LDAPS authorization:
- DHE-DSS-AES128-GCM-SHA256
- DHE-DSS-AES256-GCM-SHA384
- DHE-RSA-AES128-GCM-SHA256
- DHE-RSA-AES256-GCM-SHA384
- ECDHE-ECDSA-AES128-GCM-SHA256
- ECDHE-ECDSA-AES256-GCM-SHA384
- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-RSA-AES256-GCM-SHA384
- TLS_AES_128_CCM_SHA256
- TLS_AES_128_GCM_SHA256
- TLS_AES_256_GCM_SHA384

### Testing for LDAP Schema Support

You can use the following example queries to ensure that File Storage can look up RFC2307 and RFC2307bis-compliant user and group information from an LDAP server with a supported configuration.

```

```

[Example Query Output](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#)

```

```

```

```

[Example Query Output](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#)

```

```

```

```

[Example Query Output](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#)

```

```

Note  
  
If you're using the RFC2307bis schema, start by querying with`uniqueMember=<dn of the user>`to list all groups to which the user belongs
Tip  
  
You can create alarms based off of[File System Metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm)that help you quickly discover and diagnose LDAP connectivity issues.

## Monitoring and Alarms

Becoming aware of a problem quickly is important when using LDAP. If LDAP infrastructure isn't functioning correctly, NFS clients could lose access to File Storage file systems made available through its exports. To discover such problems, we recommend setting alarms on mount target[metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm). Alarms can alert you to infrastructure problems within minutes.

Alarms built off of[LDAP connection errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-connectivity)and[LDAP request errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-request)detect connectivity problems between mount targets, outbound connectors, and customer-managed LDAP infrastructure.

The following example query can be used to create an alarm for LDAP connectivity:
```

```

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Required IAM Policy

File Storage needs to access LDAP server password and, optionally, trusted certificate Vault secrets. Both the user configuring the mount target and the mount target itself need read access.
Important  
  
These policies must be created before you can configure mount targets to use LDAP for authorization.

### Policy to Manage Vault Secrets

Grant the user or group creating the Vault secret permissions. For more information, see[Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm).

### Policy to Enable Mount Target Configuration

Grant the user or group configuring LDAP on a mount target permissions using a policy such as the following. This allows the user to read the Vault secrets needed during configuration.

```

```

This allows the user to issue File Storage commands that will read the Vault secrets and display parts of the secret for validation during configuration.

### Policy to Allow a Mount Target to Retrieve Secrets

The File Storage service requires the ability to read the secrets. File Storage uses resource principals to grant a specific set of mount targets access to the Vault secret. This is a two step process, first the mount targets which need access must be put into a dynamic group, and then the dynamic group is granted access to read the secrets.

- 

Create a dynamic group for the mount targets with a policy such as the following:

```

```

Note  
  
If you have more than one rule in the dynamic group, ensure that you use`Match any rules defined below`option.
- 

Create an IAM policy that gives the dynamic group of mount targets read access to Vault secrets:

```

```

## Next Steps

See[Setting Up LDAP for Authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm)
