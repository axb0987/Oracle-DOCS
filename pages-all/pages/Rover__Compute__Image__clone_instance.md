# Creating a Custom Image from an Instance for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm
- Fetched: 2026-09-05 02:57 CDT

# Creating a Custom Image from an Instance for a Roving Edge Infrastructure Device

Describes how to create a custom image from an existing compute instance on your Roving Edge Infrastructure device.

You can create a custom image of a compute instance's boot disk and use that custom image to create other compute instances. Instances that you create from this image include the customizations, configuration, and software that were installed on the boot disk when you created the image.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm#)
- 

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- Select a State from the list to limit the instances displayed to that state.
- Select the instance whose details you want to get. The instance's Details page appears.
- Select More Actions and select Create Custom Image from the menu. The Create Custom Image dialog box appears.
- (optional) Enter a name for the custom image in the Display Name box. If you do not enter a name, the Roving Edge Infrastructure device assigns a random name for the custom image.
- Select Create Custom Image . A banner appears indicating either that the request for the custom image is accepted, or it has been rejected for some reason. When the custom image request is being processed, the state of the instance changes to Creating Image .
- Return to the Instances page and select Custom Images . The Custom Images page appears. After the instance is in the available/provisioning state, the Custom Images list has the newly created image.
- Next, open the navigation menu and select Compute &gt; Custom Images . The Custom Images page appears. All images are listed in tabular form.
- After the custom image you requested is created, it is listed here. Select it to view its details.
You can launch the custom image you created by selecting the Actions menu ( ) and selecting Create Instance . See[Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../Instance/instance_management.htm#ComputeInstanceManagement)for more information on managing instances of a Roving Edge Infrastructure device.
- 

Use the[oci compute image create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/create.html)command and required parameters to create a custom image from an existing compute instance on your Roving Edge Infrastructure devices:
```

```

where instance_ocid is the OCID of the instance from which you are creating the custom image.

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLI)
- 

Run the[CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage)operation to create a custom image from an existing compute instance on your Roving Edge Infrastructure devices. Include the`instanceId`
