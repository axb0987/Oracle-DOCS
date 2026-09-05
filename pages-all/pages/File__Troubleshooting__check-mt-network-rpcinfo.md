# Checking Network Connectivity for a Mount Target With RPCINFO
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/check-mt-network-rpcinfo.htm
- Fetched: 2026-09-05 02:05 CDT

# Checking Network Connectivity for a Mount Target With RPCINFO

Use the RPCINFO utility to check that your mount target is connected to the network on all required ports.

The`rpcinfo`utility is a program that retrieves a list of all the remote procedure call (RPC) services currently running, their names and descriptions, and the ports they are using. You can use the`rpcinfo`utility to verify that a mount target is connected to the network on all required ports.
Mount targets require connectivity to the following ports and protocols:
- TCP connectivity to ports 111, 2048, 2049, and 2050
- UDP connectivity to ports 111 and 2048

## Installing the RPCINFO Utility

The utility must be installed on an instance that has network access to the mount target IP address.

Windows Server 2012 R2 and later versions come with`rpcinfo`already installed. For other operating systems, such as Linux, CentOS, or Ubuntu, open a terminal and run the`rpcinfo`command to verify that the utility is installed. If the command isn't recognized, use the following commands to install the utility.

[To install RPCINFO on Linux or CentOS](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/check-mt-network-rpcinfo.htm#)

To install rpcinfo on an Oracle Linux or CentOS instance:
- Open a terminal window on the instance.
- Type the following command:

```

```

[To install RPCINFO on Ubuntu](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/check-mt-network-rpcinfo.htm#)

To install rpcinfo on an Ubuntu instance:
- Open a terminal window on the instance.
- Type the following command:

```

```

## Using the RPCINFO Utility

- Identify the IP address of the mount target. You can obtain it from the details page of the mount target. See[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-mount-target-details.htm).
- Open a terminal on the instance, and type the following command to retrieve information about the mount target. Replace mount_target_IP_address with the mount target IP address:
```

```

For example, if your mount target IP address is`10.0.0.7`, your command and its output would look like this:
```

```

- For each program listed, use the following commands to make an RPC call to report whether a response was received:
- Make an RPC call using UDP (`-u`)
```

```

- Make an RPC call using TCP (`-t`)
```

```

If the RPC call is successful, the output should look like this example:
```

```

For more information on the`rpcinfo`utility, see[rpcinfo(8) -Linux Man Page and[Windows RPCINFO Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/rpcinfo)
