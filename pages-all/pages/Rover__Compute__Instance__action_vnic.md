# Powering an Instance On and Off for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm
- Fetched: 2026-09-05 02:58 CDT

# Powering an Instance On and Off for a Roving Edge Infrastructure Device

Describes how to power a compute instance on or off on your Roving Edge Infrastructure devices.
Note  
  

The Device Console does not accurately reflect the instance's lifecycle state. It displays the instance state as Running when actually in a Started state. Use the CLI method to accurately determine the instance lifecycle state when powering on and off.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance that you want to power on or off. The instance's Details page appears.
- 

Select one of the following actions:
- 

Start : Restarts a stopped instance.
- 

Stop : Gracefully shuts down the instance by sending a shutdown command to the operating system.
Note  
  

If the applications that run on the instance take a long time to shut down, they could be improperly stopped, resulting in data corruption. To avoid this occurrence, shut down the instance using the commands available in the OS before you stop the instance using the Device Console.
- 

Reboot : Gracefully reboots the instance by sending a shutdown command to the operating system, and then powers the instance back on.
- 

Use the[oci compute instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html)command and required parameters to power on or off a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLI)
- 

Run the[
