# Creating an Instance on a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm
- Fetched: 2026-09-05 02:58 CDT

# Creating an Instance on a Roving Edge Infrastructure Device

Describes how to create a compute instance on your Roving Edge Infrastructure device.

The following list describes the minimum information that you must provide to create an instance:
- 

A name for the instance
- 

The compartment where you want to create the instance
- 

An image or boot volume
- 

An[instance shape](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance-shapes.htm#instance-shapes)
- 

A[VCN](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Network/VCN/vcn_management.htm#VCNManagement)and[subnet](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Network/Subnet/subnet_management.htm#SubnetManagement)
- 

A public SSH key

To log in to the instance, users need either an SSH key or a password, depending on how the image was built. If the instance requires SSH keys for authentication, you must provide the public key when you create the instance.

If you require more disk space on your instance, you can create and attach a block volume after you create the instance. See[Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Block_Volume/create_block_volume.htm#top)and[Attaching a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Block_Volume/Attachment/attach_volume-attachment.htm#top).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select Create Instance . The Create Compute Instance dialog box appears.
- 

Complete the following:
- 

Name : Enter a name for the instance.
- 

Image or operating system : Select Change Image . The Browse All Images dialog box appears. Select one of the following image options:
- Platform Images tab: Check the pre-built image you want for the instance from the list and select Select Image .
- Custom Images tab: Select Select Image . The image you selected is displayed in the Image or operating system box.
- 

Shape : Select Change Shape . The Browse All Shapes dialog box appears. Select a Standard or Specialty shape type, then select one of the corresponding shapes that appear. Select Select Shape . The shape you selected is displayed in the Shape box.
- Select a virtual cloud network : Select a virtual cloud network from the list.
- Select a subnet : Select a subnet associated with the virtual cloud network from the list.
- 

IP address : Select an IP address option:
- Assign a public IP address (if selected, an IP address from the external CIDR is used)
- Do not assign a public IP address
- 

Specify a custom boot volume size : Check if you don't want to use the default boot volume size. Enter the size in the Boot volume size box.
- 

SSH key : Select an SSH key option:
- Choose SSH key file : Select browse to a location and navigate to your SSH key file where you can select it for upload. You can also drag the file into the SSH keys box.
- Paste SSH keys : Copy and paste the SSH key directly into the SSH keys box.
Note  
  

If the original image had the user keys on it, the new keys might not be added to the resulting instance, depending on the image specifics.
- 

Select Create . Upon creation of the instance, the new instance's Details page opens automatically.
- 

Review the contents of the instance's Details page. It contains information such as its current state (indicated by the image in the upper left corner), IP addresses used, the image used, shape settings. You can view the boot volume, and attached VNICs by selecting their respective links in the lower left corner. Creation of the instance can take several minutes. During this time, the state is Provisioning . When the creation is complete, the state changes to Running . This state indicates that the instance is now launched.
Note  
  

Your instance capacity is limited by the available cores and available memory. If you see "out of capacity" messages on instance creation, terminate some of the existing instances that are not used and try again. Stopped instances count toward the resources used. Terminate the instance to free up the resources.
- 

Use the[oci compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command and required parameters to create a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLIAccessHelp).

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../compartments.htm#comparments).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/../../Access/cli_install.htm#CLI)
- 

Run the[
