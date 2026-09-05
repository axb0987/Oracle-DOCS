# Creating a Dynamic Port Forwarding (SOCKS 5) Session in Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-dynamic-port-forwarding.htm
- Fetched: 2026-09-05 01:42 CDT

# Creating a Dynamic Port Forwarding (SOCKS 5) Session in Bastion

Create a dynamic port forwarding (SOCKS5) session.

Ensure that you have the public key file of the SSH key pair that you plan to use to connect to the session. To learn more, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-dynamic-port-forwarding.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-dynamic-port-forwarding.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-dynamic-port-forwarding.htm#)
- 

- On the Bastions list page, select the bastion that you want to create a session in. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/list-bastion.htm).
- On the details page, select the Sessions tab or link.
- Select Create session .
- Select Dynamic port forwarding (SOCKS5) session .
- Enter a display name for the new session.

Avoid entering any confidential information in this field.
- Under Add SSH key , provide the public key file of the SSH key pair that you want to use for the session.

Later, when you connect to the session, you must provide the private key of the same SSH key pair.
- (Optional) Expand Advanced options and change the maximum amount of time that any session on this bastion can remain active by entering a value for Maximum session time-to-live . Provide a value of at least 30 minutes that doesn't exceed 180 minutes (3 hours). You can delete a session before it expires.
- When you're finished, select Create session .
- 

Use the[oci bastion session create-session-create-dynamic-port-forwarding-session-target-resource-details](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/session/create-session-create-dynamic-port-forwarding-session-target-resource-details.html)command and required parameters to create a dynamic port forwarding (SOCKS 5) session:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateSession](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Session/CreateSession)
