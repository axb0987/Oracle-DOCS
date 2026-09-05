# Creating a Port Forwarding Session in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm
- Fetched: 2026-09-05 01:42 CDT

# Creating a Port Forwarding Session in Bastion

Create a port forwarding session.

You must have the following information about the target resource you intend to create a session for:
- Valid credentials to sign in to the target resource, such as operating system and database
- One of the following:
- The name and compartment of the target compute instance
- The IP address and port of the target resource

Ensure that you have the public key file of the SSH key pair that you plan to use to connect to the session. To learn more, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm#)
- 

- On the Bastions list page, select the bastion that you want to create a session in. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- On the details page, select the Sessions tab or link.
- Select Create session .
- Select SSH port forwarding session to create an SSH tunnel to a specific port on the target resource.
This type of session doesn't require an OpenSSH server or the Oracle Cloud Agent to run on the target resource, such as an Autonomous AI Transaction Processing database.
- Enter a name for the new session.

Avoid entering any confidential information in this field.
- Specify the target using one of the following methods:

- Enter the IP Address of the target resource.
- Select the target Compute instance name.

If needed, change the compartment to find the instance. Only active instances are listed.
- Enter the port number that you want to connect to on the target resource, for example:

- SSH server on a Linux instance:`22`(default)
- Remote Desktop Protocol (RDP) server on a Windows instance:`3389`
- Autonomous AI Transaction Processing database:`1521`
- MySQL DB System:`3306`
- Under Add SSH key , provide the public key file of the SSH key pair that you want to use for the session.

Later, when you connect to the session, you must provide the private key of the same SSH key pair.
- (Optional) Expand Advanced options and change the maximum amount of time that any session on this bastion can remain active by entering a value for Maximum session time-to-live . Provide a value of at least 30 minutes that doesn't exceed 180 minutes (3 hours). You can delete a session before it expires.
- When you're finished, select Create session .
- 

Use the[oci bastion session create-port-forwarding](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/session/create-port-forwarding.html)command and required parameters to create a port forwarding session:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateSession](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Session/CreateSession)
