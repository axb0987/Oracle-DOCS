# Creating a Managed SSH Session in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-managed-ssh.htm
- Fetched: 2026-09-05 01:42 CDT

# Creating a Managed SSH Session in Bastion

Create a managed SSH session.

Before creating a managed SSH session, verify the following information:
- The bastion plugin is enabled on the target Compute instance . For details, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console).
- The VCN (virtual cloud network) includes a gateway ( service gateway , internet gateway , or NAT gateway ) and a route rule for the gateway.

For details, see[Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm),[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm), or[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm).
You must have the following information about the target resource you intend to create a session for:
- Valid credentials to sign in to the target resource, such as operating system and database
- One of the following:
- The name and compartment of the target compute instance
- The IP address and port of the target resource

Ensure that you have the public key file of the SSH key pair that you plan to use to connect to the session. To learn more, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-managed-ssh.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-managed-ssh.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-managed-ssh.htm#)
- 

- On the Bastions list page, select the bastion that you want to create a session in. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- On the details page, select the Sessions tab or link.
- Select Create session .
- Select Managed SSH session to connect to a Compute instance that has a running OpenSSH server and has Oracle Cloud Agent enabled.
- Enter a name for the new session.

Avoid entering any confidential information in this field.
- Enter a valid operating system username for the target instance.

The default username on most[platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)is`opc`.
- Select the target Compute instance. If needed, change the compartment to find the instance. Only active instances are listed.
- Under Add SSH key , provide the public key file of the SSH key pair that you want to use for the session.

Later, when you connect to the session, you must provide the private key of the same SSH key pair.
- (Optional) Expand Advanced options and configure the advanced settings for the session:
- Change the maximum amount of time that any session on this bastion can remain active by entering a value for Maximum session time-to-live . Provide a value of at least 30 minutes that doesn't exceed 180 minutes (3 hours). You can delete a session before it expires.
- Change the specific port or IP address to connect to on the target compute instance. By default, the session uses port 22 and the primary IP address of the instance.
- When you're finished, select Create session .
- 

Use the[oci bastion session create-managed-ssh](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/session/create-managed-ssh.html)command and required parameters to create a managed SSH session:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateSession](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Session/CreateSession)
