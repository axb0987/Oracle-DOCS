# Using Kerberos Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm
- Fetched: 2026-09-05 02:03 CDT

# Using Kerberos Authentication

The File Storage service offers Kerberos authentication to provide a strong authentication option.

[NFS v.3 Unix security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm#About_Security__NFS), which trusts the NFS client to be truthful about a user's identity, provides only basic security. The identity of the user in every NFS call is defined by the caller, and the identity isn't verified by a trusted third party.

Kerberos for NFSv3 offers strong authentication for both hosts and users. It can also offer proof of the integrity of data, ensuring that the data isn't tampered with, and protect the privacy of data. Data integrity and data privacy aren't possible with NFS v.3 UNIX security without installing specialized client software or opening up more TCP ports.
- Users and services in a Kerberos-enabled network are called Principals . A Kerberos principal has the form`primary/instance@realm`. See the[MIT Kerberos principal documentation](https://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html)for more information.
- The Key Distribution Center (KDC) authenticates principals and issues tickets. The KDC maintains a list of principals and their passwords.
- A Realm consists of all the principals supported by one KDC.

The File Storage service supports Kerberos authentication through RPCSEC_GSS (RFC2203) with the following security options:
- Use mode`KRB5`for authentication over NFS
- Use mode`KRB5I`for authentication over NFS and data integrity (unauthorized modification of data in-transit)
- Use mode`KRB5P`for authentication over NFS, data integrity, and data privacy (in-transit encryption)

## Features

File Storage service support of Kerberos includes the following features.

### In-Transit Encryption

You can use Kerberos mode`KRB5P`, which offers data privacy, as an alternative to using[TLS v.1.2 (Transport Layer Security) encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm). TLS v.1.2 encryption requires installation of a package called`oci-fss-utils`, or use of stunnel, depending on your operating system. The number of encrypted NFS/TLS connections for a mount target are limited, but using Kerberos with the`KRB5P`option allows you to use in-transit encryption at a scale that isn't possible with NFS over TLS.

### Kerberos and Security by IP

Security by IP, set using[NFS export options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#overview), is reasonably secure if the IP addresses are in OCI and the hosts are trusted. Kerberos for NFSv3 can provide a higher level of security for mixed environments or environments with untrusted hosts.

You can configure one CIDR block to require Kerberos and another for NFS AUTH_SYS authentication on the same export. Any clients mounting from the trusted network wouldn't need to mount with Kerberos, but clients mounting from the untrusted network would need to use Kerberos.

### LDAP Lookups and Anonymous Access

When users have an identity in the KDC, but no additional information in the LDAP server, or LDAP isn't enabled, the NFS operation can fail or proceed. Behavior in these cases depends on whether or not you enable LDAP for the mount target and anonymous access for the export.

Anonymous access is disabled by default. Any NFS request associated with a user that isn't found fails.

If anonymous access is enabled, requests associated with a user that isn't found in the LDAP server proceed with the Squash UID and Squash GID set in the export's options. You might want to allow anonymous access if the mount process uses a system Kerberos principal that doesn't exist in your LDAP server and squashed rights allow the few read-only operations used by the NFS client to mount the file system.

NFS Request Scenarios for Kerberos-enabled Exports
LDAP Enabled on Mount Target? LDAP Response Anonymous Access Enabled? Export Squash Enabled? NFS Request
Any Any Any Yes (all)

Proceeds with Squash UID and Squash GID set in the export's options. No secondary group list.
Any Any Any Yes (root)

Proceeds with Squash UID and Squash GID set in the export's options only after a successful LDAP response where the username is mapped to UID 0. No secondary group list.

If the LDAP response returns a UID that isn't 0, proceeds with returned UID, GID, and group list.
Yes USERNAME match Any No Uses UID, GID, and secondary group list retrieved from the LDAP server.
Yes No USERNAME match Yes No Proceeds with Squash UID and Squash GID set in the export's options. No secondary group list.
Yes No USERNAME match No No Fails with permissions error.
Yes LDAP error other than no matching user Any No Fails with permissions error.
No Not applicable Yes No

Proceeds with Squash UID and Squash GID set in the export's options.
No Not applicable No No Fails with permissions error.
Note  
  
Kerberos-enabled exports always use Use LDAP for Group List when Enable LDAP is enabled on the mount target.

For more information, see[NFS Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#Export).

## Prerequisites

File Storage requires several prerequisites to use Kerberos for authentication.

Requirements to use Kerberos authentication on a per-user basis include:
- Customer-managed LDAP infrastructure to map Kerberos principals to UNIX identities. For more information, see[LDAP for Authorization prerequisites](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-prereqs).
- Customer-managed Kerberos infrastructure, with a KDC such as MIT or Microsoft Active Directory.
- A DNS server that can resolve the mount target name and IP address. Both forward and reverse lookup capabilities are required.
[

- Communication with a customer-managed KDC server over TCP/UDP port 88.
- Secure communication with a Kerberos-enabled mount target over NFS port 2048/2049/2050 (optionally encrypted).
- Communication with DNS service over TCP/UDP port 53.
- Communication with customer-managed LDAP service over the TCP port configured in the outbound connector. The default value is TCP port 636.
- Data encrypted at rest in File Storage.

### LDAP Infrastructure

File Storage uses UIDs and GIDs to authorize access to files. File Storage uses LDAP to map Kerberos principals to UIDs and GIDS. For detailed LDAP infrastructure requirements, see[Prerequisites for using LDAP for authorization.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-prereqs)

If File Storage can't look up authorization information from LDAP, NFS accesses for the Kerberos principal will likely fail. Kerberos authentication can be used without LDAP, but all authenticated Kerberos principals would be treated as anonymous. For more information, see[LDAP Lookups and Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#overview__ldap-anon).

### Kerberos Keytab

The Kerberos keytab stored in OCI Vault must be a Base64-encoded string array of the following structure:
```

```

Each entry in the keytab can have only one principal and that principal must include the fully qualified domain name (FQDN) of the mount target as its instance. One principal can have multiple entries with different encryption types or ciphers.

For example, if`nfs/krb_mt1.fss_test.com@FSS_EXAMPLE.COM`is the principal in the keytab, then`FSS_EXAMPLE.COM`is the realm,`fss_test.com`is the instance, and`nfs`is the primary. The FQDN of the mount target in this example must be`krb_mt1.fss_test.com`. If using a customer-managed DNS server, you'd use this FQDN in[mount commands](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm).
Note  
  
When using the default Internet and VCN Resolver, the File Storage service constructs a FQDN by combining the mount target's hostname with the FQDN of the subnet the mount target is located in. After creation, the hostname may be changed in the mount target's details page. See[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm)for more information.

File Storage supports the following set of ciphers:
- aes128-cts- hmac -sha256-128
- aes256-cts- hmac -sha384-192
- aes128-cts- hmac -sha1-96
- aes256-cts- hmac -sha1-96
Note  
  
OCI File Storage supports a maximum Kerberos keytab size of 1024 bytes.

Important  
  
Validate the Kerberos keytab before enabling Kerberos to avoid an availability outage caused by an invalid keytab. You can validate the keytab when you[configure or review a mount target's Kerberos configuration](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm#enable-kerberos).

When you validate the Kerberos keytab through the Console, CLI, or API, the File Storage service checks the following:
- If the keytab size is greater than 1024 bytes
- That the keytab version number is not 1281 or 1282
- If the keytab contains null entries
- If the keytab has entries with different principal names
- If the keytab has more than 12 entries, which is the maximum
- If the keytab encoding type is not one of the following:
- ETYPE_AES128_CTS_HMAC_SHA1_96
- ETYPE_AES256_CTS_HMAC_SHA1_96
- ETYPE_AES128_CTS_HMAC_SHA256_128
- ETYPE_AES256_CTS_HMAC_SHA384_192
Note  
  
A keytab extracted from the KDC in binary format must be converted to Base64 and then used to create a secret in OCI Vault. Ensure that you select Base64 as the format of the secret when you paste in the converted keytab.

File Storage supports keytab rotation by using a backup keytab. See[Rotating Keys](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-key-rotation.htm)for more information.

## Considerations and Limitations

When using Kerberos for File Storage authentication, consider the following information and limits.
- For per-user Kerberos authentication, File Storage requires customer-managed Lightweight Directory Access Protocol (LDAP) infrastructure, including an LDAP server that supports an RFC2307 POSIX schema.
- File Storage supports a maximum Kerberos keytab size of 1024 bytes.
- 

File Storage supports the following set of ciphers:
- aes128-cts- hmac -sha256-128
- aes256-cts- hmac -sha384-192
- aes128-cts- hmac -sha1-96
- aes256-cts- hmac -sha1-96
- [Mounting file systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)with the`rsize`or`wsize`options isn't recommended. If you provide values for these options, they may be decreased to 256KB by File Storage when using KRB5I or KRB5P.
- File Storage performance when using Kerberos authentication mode`KRB5`is roughly equivalent to using AUTH_SYS authentication. Performance significantly decreases when using`KRB5P`and slightly decreases when using`KRB5I`. Performance might vary depending on client configuration and file system.

## Monitoring and Alarms

Becoming aware of a problem quickly is important when using Kerberos authentication with LDAP authorization. If Kerberos or LDAP infrastructure isn't functioning correctly, NFS clients could lose access to File Storage file systems made available through its exports. To discover such problems, we recommend setting alarms on mount target[metrics](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/filemetrics.htm). Alarms can alert you to infrastructure problems within minutes.

Alarms built off of[Kerberos errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__kerberos),[LDAP connection errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-connectivity), and[LDAP request errors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/using-ldap-charts-and-logs.htm#using-ldap-charts-and-logs__ldap-request)detect connectivity problems between mount targets, outbound connectors, and customer-managed LDAP infrastructure.

The following example query can be used to create an alarm for Kerberos errors:
```

```

The following example query can be used to create an alarm for LDAP connectivity:
```

```

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Required IAM Policy

File Storage needs to access LDAP server password and mount target Kerberos keytab Vault secrets for Kerberos configuration. Both the user configuring the mount target and the mount target itself need read access.

### Policy to Manage Vault Secrets

Grant the user or group creating the Vault secret permissions. For more information, see[Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm).

### Policy to Enable Mount Target Configuration

Grant the user or group configuring Kerberos and LDAP on a mount target permissions using a policy such as the following:
```

```

This allows the user to issue File Storage commands that read the Vault secrets and display parts of the secret for validation. File Storage presents the principal, key version number, and encryption types to the user configuring the mount target for validation.

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

See[Setting Up Kerberos Authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup.htm)
