# Known Issues for Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/known-issues.htm
- Fetched: 2026-09-05 01:42 CDT

# Known Issues for Bastion

Known issues have been identified in Bastion.

## Managed SSH sessions are supported for Arm instances only if they run Oracle Linux
Details Managed SSH sessions aren't supported for compute instances that meet these conditions:
- Created using[Arm-based](https://docs.oracle.com/iaas/Content/Compute/References/arm.htm)OCI Ampere A1 Compute shapes.
- Running an operating system other than Oracle Linux, such as Ubuntu.

To create a Managed SSH session, the Bastion plugin must be enabled and running. Because this plugin isn't properly enabled on some Arm-based instances, session creation fails. Workaround[Create a port forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)to connect to instances that use OCI Ampere A1 Compute shapes and aren't running Oracle Linux.

## Managed SSH session fails for Ubuntu instances
Details To create a Managed SSH session for a compute instance, the Bastion plugin must be enabled and running. This plugin is available on Oracle Cloud Agent version`1.11`or later. If your Ubuntu instance is running a version that's older than`1.11`, the creation of a Managed SSH session fails. Workaround

To update an existing Ubuntu compute instance to support Managed SSH sessions:
- Add a NAT gateway to the VCN (virtual cloud network) in which you created your instance, if not already present. See[Setting Up a NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm#setup).
- From your bastion,[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(SSH tunnel) to the SSH port (22 by default) on the instance.
- Connect to the instance using the Port Forwarding session. See[Connecting to Sessions in Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connectingtosessions.htm).
- To install the latest Oracle Cloud Agent, run the following command on the instance:
```

```

For more information, see[Installing the Oracle Cloud Agent Software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent).
- Enable the Bastion plugin on the instance. See[Managing Plugins Using the Console](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console).
- From your bastion, create a Managed SSH session to the instance.

If you're creating another Ubuntu instance, an alternative workaround is to provide a`cloud-init`script when you launch the instance. In this script, use the same command to install the latest Oracle Cloud Agent:
```

```

For more information about`cloud-init`scripts, see[Installing the Oracle Cloud Agent Software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent)
