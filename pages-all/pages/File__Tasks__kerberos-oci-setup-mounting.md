# Mounting Kerberos-enabled File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-oci-setup-mounting.htm
- Fetched: 2026-09-05 02:03 CDT

# Mounting Kerberos-enabled File Systems

Consider the following scenarios when mounting File Storage Kerberos-enabled file systems.

[Mounting a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)that uses Kerberos authentication requires additional consideration for root, administrator, and anonymous access depending the user mounting the file system. Mounting the file system as one of these users might require updates to[NFS export options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).
Note  
  
Regardless of the user mounting the file system, use the fully qualified domain name (FQDN) of the mount target instead of the IP address when mounting the file system.

## Mounting a File System as the Linux Root User

In Linux, when root user is used for mounting the file system, the NFS client searches keytab for principals in the following order:
- `<HOSTNAME>$@<REALM>`
- `root/<hostname>@<REALM>`
- `nfs/<hostname>@<REALM>`
- `host/<hostname>@<REALM>`

After the NFS client gets the ticket for one of these principals, that ticket is presented to mount target. If anonymous access isn't enabled for the export, at least one of the preceding users is required to exist in the LDAP server where they're mapped to UID and GID. If root access is preferred, map the users to UID/GID 0.

Access requests fail if a user matching`<HOSTNAME>$`,`root`,`nfs`, or`host`isn't available in LDAP and anonymous access isn't enabled for export. Use the`klist`command to verify that one of these users is present on the client.

For more information, see[LDAP Lookups and Anonymous Access](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm#overview__ldap-anon).

## Mounting a File System As a Windows User

In Windows, the user that accesses the file system is the user that mounts the file system. The principal used to mount the file system is`<username>@<REALM>`.
