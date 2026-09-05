# Creating an Instance Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating an Instance Configuration

Instance configurations let you define the settings to use when creating Compute instances. Use an instance configuration in the following scenarios:
- To create one or more instances in an[instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instancemanagement.htm).
- As a template for creating individual instances that aren't part of a pool.

When you create an instance configuration, you can use an existing Compute instance as a template, or you can provide a list of configuration settings.

You can optionally specify a[secondary virtual network interface card (VNIC)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm)and[block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm)to attach to the instances that are created from an instance configuration. To do this, create the instance configuration by providing a list of configuration settings.

## Limitations and Considerations

- 

If you use an existing instance as a template to create an instance configuration, be aware of the following information:
- The instance configuration does not include any information from the instance's boot volume, such as installed applications, binaries, and files on the instance. To create an instance configuration that includes the custom setup from an instance, you must first[create a custom image from the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm)and then[use the custom image to create a new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks). Finally, create the instance configuration based on the instance that you created from the custom image.
- The instance configuration does not include the contents of any block volumes that are attached to the instance.
- Any instances created from the instance configuration are placed in the same compartment as the instance that was used as the basis for the instance configuration, regardless of the compartment of the instance configuration. For example, an instance in compartment A is used to create an instance configuration. Then, place the instance configuration in compartment B. Any instances created using that instance configuration will be located in compartment A, the same compartment as the original instance.
- 

If you provide a list of configuration settings to create an instance configuration, be aware of the following information:
- When you create an instance from the instance configuration, many of the settings defined in the instance configuration cannot be changed. For example, the availability domain, compartment, image, shape, and subnet cannot be changed when you create the instance.
- 

Many of the settings for creating instance configurations are the same as the settings in the[create compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)workflow. However, not all settings are available for instance configurations. For some settings, you can provide a value when you create an instance from the instance configuration.
- 

For Linux instances: Using Secure Shell (SSH) keys with instance configurations:
- If you add an SSH key when you create the instance configuration, that SSH key must be used to connect to all instances created from the instance configuration.
- After you create the instance configuration, you cannot change the SSH key.
- If you create an instance configuration without an SSH key, you can add an SSH key to individual instances created from the instance configuration.
- If you use the instance configuration to create an instance pool, add an SSH key when you create the instance configuration.
- When an instance pool creates instances in the pool based on an instance configuration, the pool's settings define the availability domain and subnet, regardless of the settings in the instance configuration.
- If the instance configuration is associated with a[capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm), that reservation is automatically applied to any instances or instance pools created using that instance configuration. As long as sufficient capacity is available, when the instances launch, they use capacity from the associated reservation.

## Before You Begin

If you're providing a list of configuration settings, prepare the following items:
- Set up a virtual cloud network (VCN) in which to launch the instances that are created from the instance configuration. For information about setting up cloud networks, see[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm).
- (For Linux instances) To use your own SSH key to connect using SSH to the instances that are created from the instance configuration, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- 

To launch instances from the instance configuration by using a[host capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types)other than on-demand capacity, prepare the capacity:
- To launch an instance and have it count against a[capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm), you must have a capacity reservation in the same availability domain as the instance.
- To place an instance on a[dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/dedicatedvmhosts.htm), you must have a dedicated virtual machine host in the same availability domain and fault domain that you want to launch the instance in.

The capacity types are mutually exclusive.

To attach block volumes to the instances that are created from the instance configuration, perform one of the following actions:
- Prepare a[shareable volume that can be attached to multiple instances](https://docs.oracle.com/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm).
- If the volume is attached to an existing instance but isn't shareable,[create a backup of the volume](https://docs.oracle.com/iaas/Content/Block/Tasks/create-bv-backup.htm). Then, include the boot volume backup in the instance configuration's settings.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#)
- 

When you create an instance configuration, you can use an existing compute instance as a template, or you can provide a list of configuration settings.

## Create an Instance Configuration Using an Existing Instance as a Template

- On the Compute list page, select the instance that you want to work with. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Create instance configuration .
- Select More actions then Create instance configuration .
- Select the compartment that you want to create the instance configuration in.
- Specify a name for the instance configuration. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- To add tags to the instance configuration, select Show tagging options or Tagging and enter the tagging values.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create instance configuration .

## Create an Instance Configuration by Providing a List of Settings

Important  
  
For more detailed information about the settings in following sections, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).

### 1. Basic Information

- Navigate to the Instance Configurations list page. If you need help finding the list page, see[Listing Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instance-configurations.htm)
- Select Create instance configuration .
- Instance configuration information
- Name: Specify a name for the instance configuration. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Compartment: Select the compartment that you want to create the instance configuration in.
- Compartment to create instances in: Select the compartment where you want to place instances created from this instance configuration.
- Select the option you see:
- Tagging
- Show tagging options

Enter the tagging values. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Placement
- Select an Availability domain
- Configure Advanced options . For example, Capacity type or Fault domain
- Image and Shape
- Select an Image .
- Select a Shape .
- For Advanced Options configure:
- Management
- Tagging
- Security attributes
- Availability configuration
- Oracle Cloud Agent
- Select Next .

### 2. Security

Configure the security options if they are available.
- Shielded instances
- Confidential computing
- Advanced Options
Important  
  

When creating an instance configuration with security attributes in the tenancy, the instance launches using this instance configuration. The security attributes are sent to downstream service Compute that provisions the instances. For this flow to work seamlessly, the tenancy must have three system policies for the service`compute_management`to manage the Zero-trust Packet Routing related resources in the tenancy. For example:

```

```

See the[create compute instance workflow step 2 (Security)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#security)for details on configuring zero trust packet routing.

Select Next .

### 3. Networking

- Configure the Primary VNIC section. Specify the details for the instances that are created from this instance configuration.
- Configure Advanced options , for example:
- DNS
- SSH keys
- Secondary VNIC
- Select Next .

### 4. Storage

- Specify the Boot volume details for the instances that are created from this instance configuration.
- Block volumes

To attach block volumes to the instances that are created from this instance configuration, select Attach block volume . Then, specify the configuration details for the block volume.
- Select Create .

### Review

- Review your configuration options. Use the Previous button to go back and adjust any settings.
- Select Create .
- 

To create an instance configuration using the CLI, open a command prompt and run the[instance-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create.html)command:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/CreateInstanceConfiguration)
