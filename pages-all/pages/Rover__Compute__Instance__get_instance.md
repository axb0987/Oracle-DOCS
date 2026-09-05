# Getting an Instance's Details for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get_instance.htm
- Fetched: 2026-09-05 02:58 CDT

# Getting an Instance's Details for Roving Edge Infrastructure

Describes how to get the details of a compute instance on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get_instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get_instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get_instance.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance whose details you want to get. The instance's Details page appears.

The Details page contains a variety of information regarding the instance, including the shape used, the attached primary VNIC, and the launch options. You can also access additional information from the resource pages accessible under Resources .
- 

Use the[oci compute instance get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/get.html)command and required parameters to get the details of a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLI)
- 

Run the[
