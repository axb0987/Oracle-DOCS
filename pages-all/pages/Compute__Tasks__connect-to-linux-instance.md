# Connecting to a Linux Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm
- Fetched: 2026-09-05 01:50 CDT

# Connecting to a Linux Instance

You can connect to a running Linux instance by using a Secure Shell (SSH) connection.

Important  
  
Alternatively, for advanced control of the boot process or OS troubleshooting, you can use the serial console to connect to an instance. For details, see
- [Making a Local Connection to the Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#make-a-local-connection)
- [Creating a Console Connection Using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#creating-instance-connection-cloud-shell)

## Connecting to a Linux Instance with SSH

Current versions of Windows, MacOS, and Linux include an OpenSSH client by default. (Windows has included the[OpenSSH client](https://docs.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse)since Windows 10 and Windows Server 2019.) When you create an instance, OCI Compute generates OpenSSH keys for you. You download the keys and use them to connect to your instance.
Important  
  
SSH keys required: To connect to your instance with SSH, you must have SSH keys.
- If you lost your SSH keys, terminate the instance and create a new instance using the SSH keys provided or SSH keys you generated. See[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- If you created an instance without SSH keys, you can use the[serial console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm)to connect to your instance and configure SSH. For Oracle Linux, see this[example on how to reset the SSH key for the`opc`user](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#instance-console-linux-troubleshooting__resetsshkey)using the serial console.

For SSH troubleshooting suggestions, see[Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm).
Note  
  
For older Windows versions, you can also use the free PuTTY SSH client. See:[Connecting to a Linux Instance using PuTTY and Windows](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance-from-windows-putty.htm).

## Before You Begin

You must have the following information to connect to a Linux instance:
- 
Public IP address for an instance: Use the public IP address assigned when you created the instance. If you didn't note the address, get the address from the Instance Details page:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select your instance.
- Look at the Instance access section. If a public IP address is assigned, the address will be labeled: Public access IP address .
- If no public IP address is assigned, see[Assigning an Ephemeral Public IP to an Existing Primary Private IP](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top).
- Username: The username used to connect to the Linux instance. Default users names are assigned based on the Linux distribution used.

- For Oracle Linux or Redhat Enterprise Linux compatible platform images the username is`opc`.
- For Ubuntu platform images to create the instance, the username is`ubuntu`.
- SSH private key: The full path to the private key file from the SSH key pair used to create the instance. For more information about key pairs, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm).

## Connecting to a Linux Instance from a Windows System Using OpenSSH

Using the OCI generated key pair or your own generated key pair used to create the instance, connect to the Linux instance. Set the Permissions for the Private Key File

Set the file permissions for the private key file so that only the current user has read-only access. Do the following:
- Locate the SSH key files you created by or created for your instance.
- In Windows Explorer, navigate to the private key file, right-click the file.
- Select Properties .
- On the Security tab, select Advanced .
- On the Permissions tab, for Permission entries , under Principal , ensure that your user account is listed.
- Select Disable Inheritance , and then select Convert inherited permissions into explicit permissions on this object .
- For Permission entries , select each permission entry that isn't your user account and select Remove .
- Ensure that the access permission for your user account is Full control .
- Save your changes. Connect to the Instance with PowerShell

Next, connect to the instance with PowerShell.
- 

Open Windows PowerShell and run the following command:

```

```

&lt;private_key_file&gt; is the full path and name of the`.key`file that contains the private key associated with the instance you want to access.

&lt;username&gt; is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is`opc`. For Ubuntu images, the default username is`ubuntu`.

&lt;public-ip-address&gt; is the instance's IP address that you retrieved from the Console.
- If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type yes and press Enter .
- You are connected to the default shell for the instance.
- When you have finished your session, type`exit`at the shell prompt to end the session.
Note  
  
For SSH troubleshooting suggestions, see[Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm).
Tip  
  
If you are using an older version of the Windows operating system, you can use PuTTY to create keys and connect to a Linux instance. For details on connecting to a Linux instance with PuTTY, see[Connecting to a Linux Instance from a Windows System Using PuTTY](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance-from-windows-putty.htm#linux-from-windows-putty__connect-to-linux-from-windows-putty).
Note  
  
Windows now supports[Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about)(WSL). With WSL, you can install a free version of Linux, like Oracle Linux or Ubuntu, on your Windows system. Then from WSL, the steps to connect with SSH are the same as a regular Linux system. See:[Connecting to a Linux Instance from a MacOS or Linux System](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#linux-from-unix).

## Connecting to a Linux Instance from a MacOS or Linux System

Use the OCI generated key pair or the key pair used to create the instance. Then use the following steps to connect to an OCI Linux instance.
- Open a terminal.
- Locate the private key file for your key pair. The default directory location for SSH keys is`<your-home-directory>/.ssh`.
- 

Use the following command to set the file permissions so that only you can read the file:

Set the file permissions for the private key file so that only the current user has read-only access:

```

```

&lt;private_key_file&gt; is the full path and name of the file that contains the private key associated with the instance you want to access.
- 

Use the following SSH command to access the instance.

```

```

&lt;private_key_file&gt; is the full path and name of the file that contains the private key associated with the instance you want to access.

&lt;username&gt; is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is`opc`. For Ubuntu images, the default username is`ubuntu`.

&lt;public-ip-address&gt; is the instance's IP address that you retrieved from the Console.
- If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type yes and press Enter .
- You are connected to the default shell for the instance.
- When you have finished your session, type`exit`at the shell prompt to end the session.
Note  
  
For SSH troubleshooting suggestions, see[Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm).
Note  
  
Connecting from macOS Ventura using OpenSSH 9.0: If you connect to an instance from a client running macOS Ventura (version 13) or a client running OpenSSH 9.0, you might encounter a connection issue. For more information and a workaround, see the known issue[SSH connection issues with macOS Ventura using OpenSSH 9.0](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#ssh_connection_issues_with_macos_ventura_using_openssh)
