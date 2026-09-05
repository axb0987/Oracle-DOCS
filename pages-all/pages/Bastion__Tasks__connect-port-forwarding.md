# Connecting to a Port Forwarding Session
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm
- Fetched: 2026-09-05 01:42 CDT

# Connecting to a Port Forwarding Session

Describes how to connect to a port forwarding session.

You can view steps to connect to a port forwarding session in the following scenarios:
- [Connect to the SSH Server on a Compute Instance](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connectingtosession_topic-To_connect_to_port_forward_session)
- [Connect to Windows Using the Remote Desktop Protocol (RDP)](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connect_to_rdp)
- [Connect to Windows using RDP and PuTTY](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connectingtosession_topic-To_connect_to_rdp_putty)
- [Connect to an Autonomous AI Transaction Processing Database](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connect_to_atp)
- [Connect to a MySQL DB System](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connect_to_mysql)

## Connect to the SSH Server on a Compute Instance

Before you begin, you must[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(also known as an SSH tunnel) to the SSH server on the instance , which by default is port`22`.
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

You can use a port forwarding session to connect to instances that don't meet all requirements for a Managed SSH session.

- On the Bastions list page, select the bastion that contains the port forwarding session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Use a text editor to replace &lt;privateKey&gt; with the path to the private key of the SSH key pair that you provided when you created the session, and &lt;localPort&gt; with the local port on the machine from which you want to connect to the bastion.

You can use any available local port. The default SSH server port is`22`.
- (Optional) Add the verbose (`-v`) option to the SSH command for detailed information about the connection.

Note  
  
Don't use the`-vv`or`-vvv`options.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If the private key was created with a passphrase, you're prompted to enter it twice for a Dynamic Port Forwarding (SOCKS5) session.

After creating a connection to a Dynamic Port Forwarding (SOCKS5) session, the process doesn't exit. Don't close the terminal.

If you enabled verbose output (`-v`), the final message after a successful connection is:
```

```

- Use an SSH client to connect to`localhost`(or`127.0.0.1`) and the local port you specified,`<localPort>`.

Provide the name of a valid user on the instance's operating system.
```

```

The default username on most[platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)is`opc`. Example:
```

```

If your private key was created with a passphrase, you are prompted to enter it.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm).

## Connect to Windows Using the Remote Desktop Protocol (RDP)

Before you begin, you must[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(also known as an SSH tunnel) to the RDP port on the Windows instance , which by default is port`3389`.
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

To create the SSH tunnel using PuTTY instead of OpenSSH (the`ssh`command), see[Connect to Windows using RDP and PuTTY](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-port-forwarding.htm#connectingtosession_topic-To_connect_to_rdp_putty).

To connect to a Windows instance using an RDP client and a Port Forwarding session:

- On the Bastions list page, select the bastion that contains the port forwarding session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Use a text editor to replace &lt;privateKey&gt; with the path to the private key of the SSH key pair that you provided when you created the session, and &lt;localPort&gt; with the local port on the machine from which you want to connect to the bastion.

You can use any available local port. The default RDP server port is`3389`.
- (Optional) Add the verbose (`-v`) option to the SSH command for detailed information about the connection.

Note  
  
Don't use the`-vv`or`-vvv`options.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If you created a private key with a passphrase, you're prompted to enter it twice for a Port Forwarding session.

After you create a connection to a Port Forwarding session, the process doesn't exit. Don't close the terminal.

If you enabled verbose output (`-v`), the final message after a successful connection is:
```

```

- Open an RDP client and connect to`localhost`(or`127.0.0.1`) and the local port you specified,`<localPort>`.

Provide the name of an existing user on the Windows instance.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm).

## Connect to Windows using RDP and PuTTY

Before you begin, you must[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(also known as an SSH tunnel) to the RDP port on the Windows instance , which by default is port`3389`.
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)is an open source SSH client for Windows. You must specify a private key file that's in PuTTY's proprietary format (`.ppk`). You can use the PuTTYgen tool to import and convert a key from OpenSSH format.

To connect to a Windows instance using PuTTY, an RDP client, and a Port Forwarding session:

- On the Bastions list page, select the bastion that contains the port forwarding session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select View SSH command .
- From the SSH command, copy the following information:

- Bastion host name
- Instance IP address (or DNS name) and port number

You can only use the DNS name if DNS is enabled on the bastion.
```

```

- Open PuTTY.
- On the Session page, update the following settings:

- Host Name - the bastion's host name
- Port - 22
- From the Category panel, select SSH .
- Select the option Don't start a shell or command at all .
- From the Category panel, expand SSH , and then select Tunnels .
- Enter the following information.

- Source port - You can use any available local port. The default RDP server port is`3389`.
- Destination - Enter the instance IP address (or DNS name) and port number, separated by a colon,`<instanceIP> : <instancePort>`. The default RDP server port is`3389`.

You can only use the DNS name if DNS is enabled on the bastion.
- Select Add .
- From the Category panel, expand SSH , and then select Auth .
- For Private key file for authentication , select Browse and select the private key file that you used to create the bastion.

The`.ppk`file extension indicates that the private key is in PuTTY's proprietary format. Specify a key of this format when using PuTTY. You can use the PuTTYgen tool to import and convert a key from OpenSSH format.
- Select Open .

A terminal opens with the message "Authenticating with public key." The process doesn't exit. Don't close the terminal.

If the private key was created with a passphrase, you're prompted to enter the passphrase.
- Open an RDP client and connect to`localhost`(or`127.0.0.1`) and the local port you specified, Source port .

Provide the name of an existing user on the Windows instance.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm).

## Connect to an Autonomous AI Transaction Processing Database

Before you begin, you must[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(also known as an SSH tunnel) to the database port, which by default is port`1521`.
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

To connect to an Oracle Database using a Port Forwarding session:

- On the Bastions list page, select the bastion that contains the port forwarding session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Using a text editor, replace &lt;privateKey&gt; with the path to the private key of the SSH key pair that you provided when you created the session, and &lt;localPort&gt; with the local port on the machine from which you want to connect to the bastion.

You can use any available local port. The default Oracle Database port is`1521`.
- (Optional) Add the verbose (`-v`) option to the SSH command for detailed information about the connection.

Note  
  
Don't use the`-vv`or`-vvv`options.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If you created a private key with a passphrase, you're prompted to enter it twice for a Port Forwarding session.

After you create a connection to a Port Forwarding session, the process doesn't exit. Don't close the terminal.

If you enabled verbose output (`-v`), the final message after a successful connection is:
```

```

- Open a database client such as Oracle SQL*Plus or Oracle SQL Developer, and then connect to`localhost`(or`127.0.0.1`) and the local port you specified,`<localPort>`.

Provide the name and password of an existing user on the database.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm).

## Connect to a MySQL DB System

Before you begin, you must[create a Port Forwarding session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-port-forwarding.htm)(also known as an SSH tunnel) to the database port, which by default is port`3306`.
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

To connect to a MySQL DB System using a Port Forwarding session:

- On the Bastions list page, select the bastion that contains the port forwarding session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Using a text editor, replace &lt;privateKey&gt; with the path to the private key of the SSH key pair that you provided when you created the session, and &lt;localPort&gt; with the local port on the machine from which you want to connect to the bastion.

You can use any available local port. The default MySQL HeatWave port is`3306`.
- (Optional) Add the verbose (`-v`) option to the SSH command for detailed information about the connection.

Note  
  
Don't use the`-vv`or`-vvv`options.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If you created a private key with a passphrase, you're prompted to enter it twice for a Port Forwarding session.

After you create a connection to a Port Forwarding session, the process doesn't exit. Don't close the terminal.

If you enabled verbose output (`-v`), the final message after a successful connection is:
```

```

- Open a database client such as MySQL Workbench and connect to`localhost`(or`127.0.0.1`) and the local port you specified,`<localPort>`.

Provide the name and password of an existing user on the database.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm)
