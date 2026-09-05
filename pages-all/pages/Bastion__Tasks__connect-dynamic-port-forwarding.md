# Connecting to a Dynamic Port Forwarding (SOCKS5) Session
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-dynamic-port-forwarding.htm
- Fetched: 2026-09-05 01:42 CDT

# Connecting to a Dynamic Port Forwarding (SOCKS5) Session

Describes how to connect to a dynamic port forwarding (SOCKS5) session.

Before you begin, you must[create a dynamic port forwarding (SOCKS5) session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-dynamic-port-forwarding.htm)(also known as an SSH tunnel).
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

## To dynamically connect to an Autonomous AI Database

- On the Bastions list page, select the bastion that contains the dynamic port forwarding (SOCKS5) session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Use a text editor to replace &lt;localPort&gt; with the local port on the machine from which you want to connect to the bastion, replace &lt;sessionId&gt; with the bastion session ID, and replace &lt;bastionHost&gt; with the domain name where the bastion is hosted.
- (Optional) Add the verbose (`-v`) option to the SSH command for detailed information about the connection.

Note  
  
Don't use the`-vv`or`-vvv`options.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If the private key was created with a passphrase, you're prompted to enter it twice for a Dynamic Port Forwarding (SOCKS5) session.

After creating a connection to a Dynamic Port Forwarding (SOCKS5) session, the process doesn't exit. Don't close the terminal.

If you enabled verbose output (`-v`), the final message after a successful connection is:
```

```

- Open a database client such as Oracle SQL*Plus or Oracle SQL Developer, and then connect to`localhost`(or`127.0.0.1`) and the local port you specified,`<localPort>`.

Provide the name and password of an existing user on the database.

For example:
```

```

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm)
