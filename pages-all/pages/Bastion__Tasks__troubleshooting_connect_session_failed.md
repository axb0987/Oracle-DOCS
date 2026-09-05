# Problems Connecting to a Session
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting_connect_session_failed.htm
- Fetched: 2026-09-05 01:42 CDT

# Problems Connecting to a Session

Fix problems that can occur when you try to connect to an existing session.

In general, to troubleshoot SSH commands, add the verbose (`-v`) option. For example:
```

```

Note  
  
Don't use the`-vv`or`-vvv`options.

## Unable to connect to a session using SSH and a public key

When you use SSH and a public key to connect to a managed SSH or a port forwarding session (also known as an SSH tunnel), the connection fails and the following message is displayed:
```

```

To resolve the issue, edit the file`~/.ssh/config`and add the following lines:

```

```

Note  
  
Use`*`for the host in the SSH configuration file for access to both the bastion host and the target host. Alternately, you can add`host.bastion.*.oci.*`and all the target host's private IP addresses to the SSH configuration file.

See[Connecting to Your Instance](https://docs.oracle.com/iaas/Content/GSG/Tasks/testingconnection.htm)for more help.

## IP Address isn't in Bastion Allowlist

When you create a bastion, you specify a CIDR Block Allowlist . You add one or more address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

If the IP address of the local machine isn't in the allowlist, then the SSH command fails with this message:
```

```

[Edit the bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/update-bastion.htm)and verify that the IP address of the local machine is in the CIDR Block Allowlist . After change the allowlist, you must also[create a new session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session.htm). This change doesn't affect existing sessions.

## VCN Doesn't Allow Ingress Traffic from Bastion

The VCN (virtual cloud network) and subnet that the target resource was created in must allow incoming network traffic from the bastion on the target port.

When you try to connect to a Managed SSH session, the connection times out after several minutes and prints this message:
```

```

For a Port Forwarding session, the initial SSH connection succeeds, but then any try to use the SSH tunnel times out after several minutes and prints the same error message.

For example, to use a session to connect to port`8001`on a compute instance from a bastion with the IP address`192.168.0.99`, then the subnet used to access the instance needs to allow ingress traffic from`192.168.0.99`on port`8001`.

The default security list for a subnet allows ingress traffic to SSH port`22`from any IP address, but this rule can be changed or deleted. In addition, the default security list for a subnet doesn't typically allow ingress traffic from any IP address to other port numbers, such as:
- `1521`: Oracle Database
- `3306`: MySQL Database
- `3389`: Remote Desktop Protocol (RDP)

Update the security list for the target subnet and add the bastion's IP address. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connectingtosessions.htm#allowing-network-access).

## Port Forwarding Command Appears Unresponsive

When you use SSH to connect to a Port Forwarding session (also known as an SSH tunnel), the process doesn't exit after you enter the private key passphrase. This result is normal. Don't close the terminal.

To verify that the SSH tunnel was created successfully, you can run the SSH command again with verbose output. The final messages after a successful connection are:
```

```

After creating the SSH tunnel, use an appropriate application to connect to the target resource using the local port you specified in the SSH command:`localhost: local port`or`127.0.0.1: local port`.

For example, to use a Port Forwarding session to an Oracle Database, open Oracle SQL Developer and connect to`localhost:1521`.

See[Connecting to Sessions in Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connectingtosessions.htm)for more examples.

## Idle Connection is Closed

By default the SSH server closes an idle connection after 5 minutes. To prevent idle connections from being closed, configure the SSH client to send empty packets to the server regularly.

For example, on Linux create or edit the file`~/.ssh/config`and add the following lines:

```

```
