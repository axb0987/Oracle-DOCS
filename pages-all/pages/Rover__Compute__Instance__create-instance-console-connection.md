# Creating an Instance Console Connection for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create-instance-console-connection.htm
- Fetched: 2026-09-05 02:58 CDT

# Creating an Instance Console Connection for a Roving Edge Infrastructure Device

Describes how to create an instance console connection for a Roving Edge Infrastructure device.

When you have created the console connection, connect it to an instance. See[Connecting to the Console of an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/console-connection-instance.htm#top).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create-instance-console-connection.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create-instance-console-connection.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create-instance-console-connection.htm#)
- 

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- (optional) Select a State from the list to limit the instances displayed to that state.
- Select the instance for which you want to create the console connection. The instance's Details page appears.
- Select Console Connection under Resources . The Console Connection page appears. All console connections are listed in tabular form.
- Select Create Console Connection . The Create Console Connection dialog box appears.
- Select one of the following options to generate a public key:

- Upload public key file (.pub) : Drag and drop your`.pub`file or select Select One to navigate to where you can upload the`.pub`file.
- Paste public key : Copy the public key from its source and paste it into the box.
- Select Create Console Connection . The Create Console Connection dialog box closes and the Console Connection page displays an entry for the console connection you created, including the state of its progress. When the state of the console connection is Active , it is ready.
- 

Use the[oci compute instance-console-connection create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/create.html)command and required parameters to create an instance console connection for a Roving Edge Infrastructure device:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLI)
- 

Run the[CreateInstanceConsoleConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConsoleConnection/CreateInstanceConsoleConnection)
