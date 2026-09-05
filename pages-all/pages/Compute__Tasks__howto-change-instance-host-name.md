# How-to: Change an Instance Host Name
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/howto-change-instance-host-name.htm
- Fetched: 2026-09-05 01:51 CDT

# How-to: Change an Instance Host Name

Change the host name of an Oracle Linux Compute VM instance using the following steps.
Note  
  
Changes made in the`/etc/hosts`and`resolv.conf`files revert to their original values when the instance restarts, unless you complete the steps outlined here.
- Update the`/etc/hostname`file.
```

```

- Edit the OCI configuration file and update the`PRESERVE_HOSTINFO`value to 2.
```

```

- Edit the VNIC host name in the OCI Console.
- Go to Compute instances.
- Select the instance. Do one of the following:
- Select the Networking tab. Navigate to Attached VNICs .
- Under Resources , select Attached VNICs .
- For the target VNIC, from the Action Menu select Edit .
- Change the VNIC host name as needed.
- Select Save changes .
- Reboot the instance.
- Check the host name with`hostname`command.
- Check the host name and the Fully Qualified Domain Name (FQDN) with the following commands.
```

```

or
```

```

Note  
  
The verification commands only work for a public IP address if the VCN is configured for public DNS resolution. Use the private IP address instead if public DNS isn't configured.
Important  
  
The FQDN is configured using a combination of the VNIC host name, subnet name, and VCN name. For details on configuring DNS see:[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)
