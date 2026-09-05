# Getting an Instance Console Connection's Details for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm
- Fetched: 2026-09-05 02:58 CDT

# Getting an Instance Console Connection's Details for a Roving Edge Infrastructure Device

Describes how to get an instance console connection's details for a Roving Edge Infrastructure device.

See[Connecting to the Console of an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/console-connection-instance.htm#top)for details on how to connect to the console of an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm#)
- 

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- (optional) Select a State from the list to limit the instances displayed to that state.
- Select the instance containing the console connection whose details you want to get. The instance's Details page appears.
- Select Console Connection under Resources . The Console Connection page appears.

The Console Connection page displays all console connections in tabular form. The State column displays the state of the instance console connection for each connection entry and the Public Key for Fingerprint column displays the finger for each connection entry.
- 

Use the[oci compute instance-console-connection get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/get.html)command and required parameters to get an instance console connection's details for a Roving Edge Infrastructure device:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLI)
- 

Run the[GetInstanceConsoleConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConsoleConnection/GetInstanceConsoleConnection)
