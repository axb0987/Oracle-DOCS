# Showmount Command Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/showmountfails.htm
- Fetched: 2026-09-05 02:06 CDT

# Showmount Command Fails

The File Storage service supports the`showmount -e`command, but it must be enabled before it can be used.

Once enabled, you can use the`showmount -e`command to show a list of NFS exports available from a specific mount target IP address.

For example,`$ showmount -e 10.0.0.0`

To enable the command, you must create a security list rule in the subnet containing the mount target. The rule must be a stateful ingress rule for UDP traffic with a Destination Port Range of 111 .

Click here for instructions about[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm).

For more information about this command, see the[Linux manual page about showmount](https://linux.die.net/man/8/showmount).
Important  
  
Only`showmount -e`is supported. No other options are supported, and the`-e`
