# Managed SSH Session Creation Failed
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting_managed_ssh_session_creation_failed.htm
- Fetched: 2026-09-05 01:42 CDT

# Managed SSH Session Creation Failed

Fix problems that can occur when you attempt to create a new Managed SSH session.

## Oracle Cloud Agent isn't Running on the Target Instance

Oracle Cloud Agent is a lightweight process that runs on compute instances and performs instance management tasks. Some Compute images (especially those images provided by Oracle) enable the Oracle Cloud Agent. For some images, you need to enable the agent on the instance yourself.

To create a Managed SSH session, the target compute instance must be running the Oracle Cloud Agent. Otherwise, you get an error message. See[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console).

## Bastion Plugin isn't Enabled on the Target Instance

The Oracle Cloud Agent process manages plugins running on the compute instance. The Bastion plugin is used to establish and monitor Managed SSH sessions. By default, the Bastion plugin is not enabled on instances running the Oracle Cloud Agent.

To create a Managed SSH session, the Bastion plugin must be enabled on the target compute instance and it must be running. Otherwise, you get an error message. See[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console).

## SSH Server isn't Configured Properly on the Target Instance

On the target instance, open the file`/etc/ssh/sshd_config`, and verify the current configuration.
- If`PasswordAuthentication`is set to`yes`, then`PubkeyAuthentication`must also be set to`yes`.
- If`AuthorizedKeysFile`is specified, the path and file name must exist. Paths are relative to the user's home directory.
- The file specified in`AuthorizedKeysFile`(or`.ssh/authorized_keys`by default) must include the same SSH key that is configured in the Managed SSH session.
- Do not specify a`ListenAddress`.
- If`AddressFamily`is specified, it must be set to`any`or`inet`.
- If`Port`is specified (default is 22), check that the same port number is configured in the Managed SSH session.
- If`DenyUsers`or`DenyGroups`is specified, check that the user configured in the Managed SSH session is not on these lists.

Restart the SSH server if you modified the file. For example:
```

```

An alternative to modifying the SSH server configuration and using a Managed SSH session is to use a Port Forwarding session. See[Session Types](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../Concepts/bastionoverview.htm#session_types).

## Missing Gateway

When you create a bastion, you must specify a VCN (virtual cloud network) and a private subnet within that VCN.

To create a Managed SSH session, the VCN must include a gateway ( service gateway , internet gateway , or NAT gateway ) and a route rule for the gateway. If the VCN isn't configured correctly:
- The creation of the Managed SSH session fails after several minutes because of a network timeout.
- The state of the Bastion plugin on the target Compute instance is`INVALID`.

See[Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm),[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm), or[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm).

## Invalid Username

When you create a Managed SSH session, you must provide a valid username on the target instance's operating system. If the username is invalid, the creation of the session fails.

The default OS username on most compute instances created from an Oracle-provided image is`opc`
