# Connecting to a Managed SSH Session
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/connect-managed-ssh.htm
- Fetched: 2026-09-05 01:42 CDT

# Connecting to a Managed SSH Session

Describes how to connect to a managed SSH session.

Before you begin, you must[create a Managed SSH session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/create-session-managed-ssh.htm)to the target instance .
- You must have the private key file of the SSH key pair that you used to create the session.
- The IP address of the machine must be in the CIDR block allowlist of the bastion that hosts the session.
- The IP address of the bastion must be permitted to access the target resource. See[Allowing Network Access From the Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../common/../Tasks/connectingtosessions.htm#allowing-network-access).

## Connect to a Compute Instance using a Managed SSH Session

- On the Bastions list page, select the bastion that contains the managed SSH session that you want to work with.
- On the details page, select the Sessions tab or link.
- Find the session that you want to use to connect to the intended target resource.
- In the Actions menu (three dots) for the session, select Copy SSH command .
- Use a text editor to replace &lt;privateKey&gt; with the path to the private key of the SSH key pair that you provided when you created the session.
- Use a command line to issue the customized SSH command and connect to the bastion session.

If the private key was created with a passphrase, you're prompted to enter it.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting.htm)
