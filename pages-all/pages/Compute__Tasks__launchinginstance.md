# Creating an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm
- Fetched: 2026-09-05 01:51 CDT

# Creating an Instance

Create a bare metal or virtual machine (VM) compute instance.

## Before You Begin

Tip  
  
If this is your first time creating an instance, for a guided tutorial consider one the following:
- [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../tutorials/first-linux-instance/overview.htm)
- [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/Content/developer/apache-on-oracle-linux/01-summary.htm)
- [Launching Your First Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../tutorials/first-windows-instance/overview.htm)
Tip  
  
If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see:[Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
Important  
  
When a compartment is part of a security zone, you must follow security zone policies when creating a compute instance. This means failing to implement security zone policies might prevent instance creation in that compartment. See[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-security-zones)for a detailed list of default security zone policies.

Before you create an instance, you need these things:
- (Optional) An existing VCN to create the instance in. Alternatively, you can create a new VCN while you create the instance. For information about setting up VCNs, see[Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm).
- Public SSH key (Linux instances): If you want to use your own SSH key to connect to the instance using SSH, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm). By default, the Compute service generates an OpenSSH key pair for you.
- 

(Windows instances) For Windows instances, a VCN security rule that enables RDP access so that you can connect to your instance. Specifically, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

You can implement this security rule either in a network security group (NSG) that you add this Windows instance to or, in a security list that's used by the instance's subnet.

For instructions for either method, see:[Enabling RDP Access to a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp).
- 

(Optional) To create the instance by using a[host capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types)other than on-demand capacity, prepare the capacity as follows:
- To create an instance and have it count against a[capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm), you must have a capacity reservation in the same availability domain as the instance.
- To place an instance on a[dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/dedicatedvmhosts.htm), you must have a dedicated virtual machine host in the same availability domain and fault domain as the instance.

The capacity types are mutually exclusive.
- Permissions to create and manage instances. See:[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-permissions)

[(Optional) Enabling RDP Access to a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

Create a VCN security rule that enables Remote Desktop Protocol (RDP) access so that you can connect to a Windows compute instance. You can implement this security rule either in a network security group (NSG) that you add the Windows instance to or, in a security list that's used by the instance's subnet. To enable RDP access:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- 

Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- Select the VCN you want to create the security rule in.
- 

Do one of the following:
- 

Add the rule to a network security group that the instance belongs to:
- Under Resources , select Network Security Groups .
- Select the network security group to add the rule to.
- Select Add Rules .
- 

Enter the following values for the rule:
- Stateless: Leave the checkbox cleared.
- Direction: Ingress
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: RDP (TCP/3389)
- Source Port Range: All
- Destination Port Range: 3389
- Description: An optional description of the rule.
- Select Add .
- 

To add the rule to a security list that is used by the instance's subnet:
- Under Resources , select Security Lists .
- Select the security list that you're interested in.
- Select Add Ingress Rules .
- 

Enter the following values for the rule:
- Stateless: Leave the checkbox cleared.
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: RDP (TCP/3389)
- Source Port Range: All
- Destination Port Range: 3389
- Description: An optional description of the rule.
- Select Add Ingress Rules .

## Instance IP addresses

When you create an instance, the instance is automatically attached to a virtual network interface card (VNIC) in the cloud network's subnet and given a private IP address from the subnet's CIDR. You can let the system assign the IP address, or you can specify an address. The private IP address lets instances within the VCN communicate with each other. If you've[set up the cloud network for DNS](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm), instances can instead use fully qualified domain names (FQDNs).

If the subnet is public, you can optionally assign the instance a public IP address. A public IP address is required to[communicate with the instance over the internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private), and to establish a Secure Shell (SSH) or Remote Desktop Protocol (RDP) connection to the instance from outside the cloud network. You can also create SSH or RDP connections to instances without public IP addresses by using a[bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm).

## Capacity availability

To determine whether capacity is available for a specific shape before you create an instance, use the[CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)operation.
Note  
  
Partner images and pre-built Oracle enterprise images are not available in Government Cloud realms.

## Steps to Create an Instance

Follow these steps to create an instance using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)
- 

Important  
  
Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

On the Compute list page, select Create instance . If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).

Creating an instance consists of the following steps:
- [1. Basic Information](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#basic-information)
- [2. Security](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#security)
- [3. Networking](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#networking)
- [4. Storage](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#storage)
- [Review](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#review)

## 1. Basic Information

Navigate to the compute instances page and start the Create Instance workflow.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select Create instance .
- Enter a name for the instance. You can add or change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
- 

Select the compartment to create the instance in.

The other resources that you choose can come from different compartments.

### Placement

Availability domain : Select the Availability domain that you want to create the instance in.
Important  
  
If you're creating an instance from a boot volume, you must create the instance in the same Availability domain as the boot volume.

### Advanced Options

- 

Capacity type

For[capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types), select one of the following options under Capacity type .
- On-demand capacity (Default): The instance is launched on a shared host using on-demand capacity. This is the default.
- Preemptible capacity : This option lets you run the instance on a shared host using[preemptible capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/preemptible.htm). The capacity is reclaimed when it's needed elsewhere, and the instances are terminated. Select whether to permanently delete the attached boot volume when the capacity is reclaimed and the instance is terminated.
- Capacity reservation: This option lets you count the instance against a[capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm). Select a capacity reservation from the list.
- Dedicated host: This option lets you run the instance in isolation, so that it is not running on shared infrastructure. Select a[dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/dedicatedvmhosts.htm)from the list. You can place an instance on a dedicated virtual machine host only when you create the instance.
- Compute cluster: This option lets you place the instance on a[compute cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm), which is a high-bandwidth, ultra-low-latency remote direct memory access (RDMA) network for high-performance computing. Compute clusters let you manage instances in the cluster individually, and you can have different types of instances in the cluster. Select a cluster from the list.
- 

Cluster placement group
Note  
  
If Cluster Placement Group is not enabled for your tenancy, the control does not appear in the Console.

Turn on Cluster Placement Group to enable cluster placement groups for this instance. Select the cluster placement group using the following options:
- Select a cluster placement group : Select your cluster placement group from the list.
- Enter a cluster placement group OCID : Enter the OCID in the provided field.

To learn more about Cluster Placement Groups, see:[Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm).

To use Cluster Placement Groups, you must set the correct policies. For more information, see:[Cluster Placement Groups Policies](https://docs.oracle.com/iaas/Content/cluster-placement-groups/policy-reference.htm).
- 

Fault domain

If you don't specify the fault domain, the system selects one for you (default). You can edit the fault domain after you create the instance. Otherwise, select the[fault domain](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bestpracticescompute.htm#Fault)to use for the instance.

### Image and Shape

A shape is a template that determines the number of CPUs, amount of memory, and other resources allocated to an instance. The image is the operating system that runs on top of the shape.

### Image

By default, an Oracle Linux image is used to boot the instance. To select a different image or a boot volume, select Change image . Then in the Select an image panel, select one of the following operating systems or image sources, and select Select image .
- 

Platform Images
- To use a[platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm), select Oracle Linux , Ubuntu , Windows , or other Linux distribution. Select the compartment, and then select an OS version. To choose a different image build, or to see which shapes are compatible with an OS version and image build, select the down arrow for the image.
- 

When selecting a Windows image there are two licensing options, either Oracle provided or Microsoft bring your own license (BYOL).
- Images with the Price column set to Additional license fee are OCI provided Windows licenses. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices.
- Images with the Price column set to Bring your own license require you to provide your own Windows license for that instance. Leveraging this license type requires you to activate your licenses.

For both types of license, you must agree to the Oracle and Microsoft license terms of use for the selected Windows version.
- To use a Red Hat Enterprise Linux image, follow the steps in[Red Hat Enterprise Linux (RHEL) Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagelinux.htm#ossupport__rhel).
- 

To use a[Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/overview-marketplace.htm)image, select Marketplace .
- For Oracle enterprise images and[partner images](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/workingwithlistings.htm), select the Partner images option, and then select an image. To view more details about an image or to change the image build, select the down arrow for the image. Images in this section include pre-built Oracle enterprise images and solutions enabled for OCI, and trusted third-party images published by Oracle partners.
- 

For[community images](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/publishingcommunityapplications.htm), select the Community images option, and then select an image. You can filter by OS. To view more details about an image, select the down arrow for the image. Community images are custom images created and published by community members for use by other community members. Community images are not available for Windows.
- 

Custom Images
- To use a[custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm)that was created or imported into your OCI environment, select My images . Select the Custom images option. Select the compartment, and then select the image.
- 

To use a Windows[custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm)that was created or imported into your OCI environment, select My images . Select the Custom images option. Select the compartment, and then select the image.

Next select a Windows License type .
- Select Micrsosoft bring your own license to provide your own Windows license for the instance. Leveraging this license type requires you to activate your licenses.
- Select OCI provided to use OCI Windows licenses. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices.

For both types of license, you must agree to the Oracle and Microsoft license terms of use for the selected Windows version.
- To use a[boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm), select My images . Select the Boot volumes option. Select the compartment, and then select the boot volume.
- To use a specific version of an image by providing the image OCID , select My images . Select the Image OCID option, and then enter the image OCID. To determine the OCID for platform images, see the[image release notes](https://docs.oracle.com/iaas/images/).

### Shape

By default, an Oracle shape is selected for the instance. To select a different shape for the instance, select Change shape . Then, in the Browse all shapes panel, follow these steps:
- In the Instance type section, select Virtual machine or Bare metal machine .
- 

If you're creating a virtual machine, in the Shape series section, select a processor group.

- AMD: (Flexible) Standard shapes that use current-generation AMD processors. AMD shapes are flexible shapes.
- Intel: (Flexible) Standard and optimized shapes that use current-generation Intel processors. Intel shapes are flexible shapes.
- Ampere: (Flexible) The OCI Ampere A1 Compute and OCI Ampere A2 Compute shapes use Arm-based processors. The Arm-based shapes are flexible shapes. The`VM.Standard.A1.Flex`shape is an[Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)shape. These shapes are not supported for Windows.
- Specialty and previous generation: Standard shapes with previous generation Intel and AMD processors, the[Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)`VM.Standard.E2.1.Micro`shape, Dense I/O shapes, GPU shapes, and HPC shapes.

[Flexible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm#flexible)have a customizable number of OCPUs and amount of memory.
- 

Select a shape.
Tip  
  
If a shape is disabled, it means that the shape is either incompatible with the image that you selected previously, or not available in the current availability domain. If you don't see a shape, it means that you don't have service limits for the shape. You can[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
- 

If you selected a flexible shape, provide the following information:
- For Number of OCPUs , select the number of OCPUs that you want to allocate to this instance by dragging the slider. The other resources scale proportionately.
- If you want this to be a[burstable instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/burstable-instances.htm)and the shape supports bursting, select the Burstable option. Then, in the Baseline utilization per OCPU list, select the baseline OCPU utilization for the instance. This value is the percentage of OCPUs that you want to use most of the time.
- For Amount of memory (GB) , select the amount of memory that you want to allocate to this instance. The amount of memory allowed is based on the number of OCPUs selected.
- To allocate an[extended amount of memory](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/extended-memory-vm-instances.htm#extended-memory-create-instance)or OCPUs to the instance, you can make this instance an extended memory VM by dragging the slider to Extended OCPU or Extended memory .

For more information about the minimum memory, maximum memory, and ratio of memory to OCPUs for each shape, see[Flexible Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm#flexible).
- For bare metal instances, optionally[configure advanced BIOS settings](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bios-settings.htm), such as disabling simultaneous multithreading, disabling cores, or optimizing the NUMA settings. Click Show advanced BIOS settings , and then select the options that you want to configure. The settings that are available depend on the shape.
- For VM instances, if you want to disable simultaneous multithreading, select Show advanced OCPU options , and then uncheck Enable simultaneous multithreading (SMT) . Simultaneous multithreading is enabled by default. For more information on disabling SMT, see[Disabling Simultaneous Multithreading](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/disablesmt.htm).
- Select Select shape .

### Advanced Options

- 

Management
- 

Instance metadata service: The instance metadata service provides metadata about the instance. Applications can use this metadata to bootstrap or do other tasks.

Require an authorization header : Select this check box to require that all[requests to the instance metadata service (IMDS)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm)use the version 2 endpoint and include an authorization header. Requests to IMDSv1 are denied. The image must support IMDSv2.
- 

Initialization script: User data can be used by cloud-init to run custom scripts or provide custom cloud-init configuration. Cloudbase-init is used on Windows. Browse to the file that you want to upload, or drag the file into the box. The file or script does not need to be base64-encoded, because the Console performs this encoding when the information is submitted. For information about how to take advantage of user data, see the[cloud-init documentation](http://cloudinit.readthedocs.io/en/latest/topics/format.html)and the[cloudbase-init documentation](https://cloudbase-init.readthedocs.io/en/latest/). The total maximum size for user data and other metadata that you provide is 32,000 bytes.
Caution  
  
Do not include anything in the script that could trigger a reboot, because that could impact the instance launch and cause it to fail. Any actions that require a reboot should be performed only after the instance state is Running .
- Tagging: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security Attributes: If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- 

Availability configuration
- 

Live Migration
- Let Oracle Cloud Infrastructure choose the best migration option: Select this option to let Oracle Cloud Infrastructure choose the best option to[migrate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm)to a healthy physical VM host if an underlying infrastructure component needs to undergo maintenance.
- Use live migration if possible : Select this option to have the instance[live migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration)to a healthy physical VM host without any notification or disruption. If live migration isn't successful,[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot)is used. Some shapes do not support live migration.
- Send maintenance notification : Select this option to have a notification sent for the maintenance event. The instance is live migrated if you do not proactively reboot the instance before the due date.
- Restore instance lifecycle state after infrastructure maintenance: By default, if an instance is running when a maintenance event affects the underlying infrastructure, the instance is rebooted after it is recovered. Clear this check box if you want the instance to be recovered in the stopped state.
- 

Oracle Cloud Agent

Select which[plugins](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm)you want to enable when the instance is launched. Plugins collect performance metrics, install OS updates, and perform other instance management tasks.
Important  
  
After you create the instance, you might need to perform additional configuration tasks before you can use each plugin.

## 2. Security

Enable shielded instance or confidential computing support. If needed, select Edit .

Select the options that you want to enable:
- 

Shielded instance

Toggle the switch to turn on Shielded instance support. Shielded instances harden the firmware security on bare metal hosts and virtual machines to defend against malicious boot level software. Shielded instances use a combination of Secure Boot, Measured Boot, and the Trusted Platform Module to harden the firmware security. On some instances, these options must be enabled together. In these cases, when you select one option, any other required options are automatically selected. After a shielded instance is launched, only the name of the instance can be changed.
- 

Confidential computing

Toggle the switch to enable[Confidential computing](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/confidential_compute.htm)for the instance. Confidential computing is hardware technology in CPUs that encrypts data in-use while being processed and protects against threats.
- 

Advanced Options

Security Attributes: Enter up to three Zero Trust Packet Routing (ZPR) attributes here.
- For more information on ZPR, see:[Overview of Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/overview.htm).
- For information on configuring ZPR policies see:[Zero Trust Packet Routing IAM Policies](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/policy-reference.htm).
Tip  
  
If you can't select the shielded or confidential computing settings, first choose a shape and image that supports shielded instances or confidential computing. Then, select the shielded instance or confidential computing settings. An instance can either be shielded or enabled for confidential computing, but not both simultaneously.

## 3. Networking

Note  
  
This section may be labeled Primary VNIC information on older console interfaces.
Tip  
  
If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see:[Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
Tip  
  
If you want the instance to have an IPv6 address assigned at launch, you must select an existing VCN with at least one IPv6 prefix assigned and select a subnet of that VCN that is enabled to use IPv6. Consider using the "Start VCN Wizard" workflow as described in the preceding note to create the VCN.

### Primary VNIC

For Primary network and Subnet , specify the[virtual cloud network (VCN) and subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)to create the instance in. Decide whether you want to use an existing VCN and subnet, create a new VCN or subnet, or enter an existing subnet's OCID:

[Select existing virtual cloud network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

Make the following selections:
- Virtual cloud network: The VCN the instance uses to connect to other resources. Choose among the VCNs in the selected compartment.
- 

Subnet: A subnet within the VCN. Subnets are either public or private. Resources in a private subnet will not be reachable from external hosts on the internet. In the case of IPv4, resources in private subnets can't have public IP addresses. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets can also be either AD-specific or regional (regional ones have "regional" after the name). We recommend using regional subnets. For more information, see[About Regional Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet). If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.

If you choose Select existing subnet , for Subnet, select the subnet. Choose among the subnets in the selected VCN.

If you choose Create new public subnet , enter the following information:
- New subnet name: Avoid entering confidential information.
- Create in compartment: The compartment where you want to put the subnet.
- CIDR block: A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Make sure it's within the cloud network's CIDR block and doesn't overlap with any other subnets. You cannot change this value later.. For reference, here's a[CIDR calculator](http://www.ipaddressguide.com/cidr).

[Create new virtual cloud network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

Note  
  
Creating an instance with IPv6 addresses assigned at launch is not available when you use this option.

Make the following selections:
- New virtual cloud network name: A friendly name for the network. Avoid entering confidential information.
- Create in compartment: The compartment where you want to put the new network.
- 

Create new subnet: A subnet within the cloud network to attach the instance to. Subnets are either public or private. Resources in a private subnet will not be reachable from external hosts on the internet. In the case of IPv4, resources in private subnets can't have public IP addresses. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). Subnets can also be either AD-specific or regional (regional ones have "regional" after the name). We recommend using regional subnets. For more information, see[About Regional Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview__regional_subnet).
- New subnet name: A friendly name for the subnet. It doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
- Create in compartment: The compartment where you want to put the subnet.
- CIDR block: A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Make sure it's within the cloud network's CIDR block and doesn't overlap with any other subnets. See[Allowed VCN Size and Address Ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a[CIDR calculator](http://www.ipaddressguide.com/cidr).
- If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.

[Enter subnet OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

For Subnet OCID , enter the subnet OCID.

If you choose a public subnet, you can also assign the instance a public IPv4 address. A public IP address (with associated security and routing configuration) is required to make this instance accessible from the internet.

### Configure Primary IP Address

In Primary VNIC IP addresses , configure the following:
- For all subnets, choose to either Automatically assign private IPv4 address (the default), Manually assign private IPv4 address , or provide the OCID for an existing reserved private IPv4 address. When you choose Manually assign private IPv4 address , enter an IPv4 address in an IPv4 CIDR block assigned to the previously chosen subnet. To use a previously created Reserved Private IP, enter the OCID for the existing Reserved Private IP address. A private IP address is required for all VNICs. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private).
- For public IPv4 subnets only, you can Automatically assign public IPv4 address or uncheck the option and not configure a public IPv4 address at this time.[You can assign a public IPv4 address later if necessary](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top). A VNIC considers a public IPv4 address optional.
- (IPv6-enabled subnets only) To add an IPv6 address, check Assign IPv6 addresses from subnet prefixes , select an IPv6 prefix configured for the subnet you selected, and then choose one of the following:
- Automatically assign IPv6 addresses from prefix: Choose this option to let the OCI select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix.
- Manually assign IPv6 addresses from prefix: Choose this option to select a specific address from an IPv6 prefix assigned to this subnet. Example: 0000:0000:1a1a:1a2b.

If you select + Another subnet prefix you can assign additional IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet).

### Advanced Options

If you want to configure advanced networking settings, select Show advanced options . The following options are available:
- Use network security groups to control traffic: Select this option if you want to add the instance's primary VNIC to one or more[network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). Then, specify the NSGs. This option is available only when you use an existing VCN. For more information, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
- DNS record: Select whether to assign the VNIC a private DNS record. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm).
- Hostname: Enter a hostname to use for DNS within the VCN. This field is available only if the VCN and subnet both have DNS labels, and you select the option to assign a private DNS record.
- Fully qualified domain name : If you assigned a private DNS record, the fully qualified domain name is displayed.
- Launch options: Select the[networking launch type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-network-launch-types). This option is available only for VMs.
- VCN tags and Subnet tags tabs: If you create a new VCN and subnet, these tabs are available. If you have permissions to create these resources, then you also have permissions to apply free-form tags to the resources. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask an administrator.
- Security attributes tabs: If you create a new VCN, this tab is available. If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

### Add SSH Keys (Linux)

In the Add SSH keys section, generate an SSH key pair or upload your own public key. Select one of the following options:
- 

Generate a key pair for me: Oracle Cloud Infrastructure generates an RSA key pair for the instance. Select Save Private Key , and then save the private key on your computer. Optionally, select Save Public Key and then save the public key.

Caution  
  
Anyone who has access to the private key can connect to the instance. Store the private key in a secure location.
Important  
  
To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- Upload public key files (.pub): Upload the public key portion of your key pair. Either browse to the key file that you want to upload, or drag and drop the file into the box. To provide multiple keys, press and hold down the Command key (on Mac) or the Ctrl key (on Windows) while selecting files.
- Paste public keys: Paste the public key portion of your key pair in the box.
- No SSH keys: Select this option only if you do not want to connect to the instance using SSH. You can't provide a public key or save the key pair that is generated by Oracle Cloud Infrastructure after the instance is created.
Tip  
  
If you try to upload or paste a private key, an error occurs.

### Secondary VNIC

In Secondary VNIC , select Add VNIC and enter the following information:
- VNIC Name: A friendly name for the secondary VNIC. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Virtual cloud network: The VCN that contains the subnet of interest.
- Subnet: The subnet the secondary VNIC will be in, which must be in the same availability domain as the instance's primary VNIC. The subnet list includes any[regional subnets or AD-specific subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm)in the primary VNIC's availability domain.
- Physical NIC: Only relevant if this is a bare metal instance with two[active physical NICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). Select which one you want the secondary VNIC to use. When you later view the instance's details and the list of VNICs attached to the instance, they'll be grouped by NIC 0 and NIC 1.
- For all subnets, choose to either Automatically assign private IPv4 address (the default) or Manually assign private IPv4 address . When you choose Manually assign private IPv4 address , enter an IPv4 address in the CIDR block assigned to the previously chosen subnet. For more information, see[Access to the Internet](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Private). A private IP address is required for all VNICs.
- For public IPv4 subnets only, you can Automatically assign public IPv4 address or uncheck the option and not configure a public IPv4 address at this time. You can assign a public IPv4 address later if necessary. A VNIC considers a public IP address optional.
- (IPv6-enabled subnets only) To add an IPv6 address, check Assign IPv6 addresses from subnet prefixes , select an IPv6 prefix configured for the subnet you selected, and then choose one of the following:
- Automatically assign IPv6 addresses from prefix: Choose this option to let the console select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix.
- Manually assign IPv6 addresses from prefix: Choose this option to select a specific address from an IPv6 prefix assigned to this subnet. Example: 2001:db8:1a1a:1a2b.

If you select + Another subnet prefix you can assign additional IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet). If this VNIC is being attached to an existing instance after its launch, keep in mind that your instance OS needs specific configuration to use IPv6 addressing.

Adding a secondary VNIC is entirely optional and will require further configuration in the instance OS.

## 4. Storage

### Boot volume

Configure the size and encryption options for the instance's boot volume:
- 

To specify a[custom size for the boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom), select the Specify a custom boot volume size check box. Then, enter a custom size from 50 GB to 32 TB. The specified size must be larger than the default boot volume size for the selected image.
Important  
  
For Windows Server 2012 R2 Datacenter images and Windows platform images published before October 2021, the custom boot volume size must be larger than the image's default boot volume size or 256 GB, whichever is higher.

You can specify the[volume performance](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for boot volumes. The default performance is Balanced . You can[modify the performance setting](https://docs.oracle.com/iaas/Content/Block/Tasks/changingvolumeperformance.htm)after you create the instance.
- For VM instances, you can optionally select the Use in-transit encryption check box. For bare metal instances that support in-transit encryption, it is enabled by default and is not configurable. See[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption)for more information about in-transit encryption. If you are using your own Vault service encryption key for the boot volume, then this key is also used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.
- 

Boot volumes are encrypted by default, but you can optionally use your own Vault service encryption key to encrypt the data in this volume. To use the[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select the Encrypt this volume with a key that you manage check box. Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key. If you select this option, this key is used to encrypt data at rest and in-transit.
Important  
  
The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This condition applies to block volumes and boot volumes.

### Block Volumes

In the Block volumes section, select or create additional block volumes to attach to this instance:
Important  
  
A maximum of 10 block volumes can be attached during instance creation. You can attach more block volumes when instance creation is complete.

Select Attach block volume . Three options are available for selecting block volumes.

[Select volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

To select an existing volume, perform the following steps:
- Select a block volume from the list. Change the compartment if the block volume is in a different compartment.
- Select an Attachment type :

Select Recommended or Custom . Recommended selected:
- Attachment Type: iSCSI
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- (Optional) Device Path: Select a device path for the block volume. Custom selected:
- Select one of the following options:
- (Recommended) iSCSI: A TCP/IP-based standard used for communication between a volume and attached instance.
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- Paravirtualized: A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images.
- Select Use in-transit encryption to encrypt transferred data.
- (Optional) Device Path: Select a device path for the block volume.
- Select the Access type from one of three options:
- Read/write
- Read/write, shareable
- Read only, shareable
- Select Attach .

For detailed explanations of attachment options see:[Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).

[Create new volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

To create a new block volume, perform these steps:
- In the Volume information section enter the requested information:
- Name: Enter a user-friendly name for the volume. Avoid entering confidential information.
- (Optional) Create in compartment: Select a different compartment if needed.
- Availability domain: The availability domain for the instance is selected by default.
- In the Volume size and performance section, selection an option:
- Default: Take the default values displayed in the dialog.
- Custom: Change the available options as needed. Options include:
- Size
- VPUs/GB
- Default VPUs/GB
- In the Encryption section, select one of the two options:
- Encrypt using Oracle-managed keys
- Encrypt using customer-managed keys: Use a key created in the Vault service.
- Select an Attachment type :

Select Recommended or Custom . Recommended selected:
- Attachment Type: iSCSI
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- (Optional) Device Path: Select a device path for the block volume. Custom selected:
- Select one of the following options:
- (Recommended) iSCSI: A TCP/IP-based standard used for communication between a volume and attached instance.
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- Paravirtualized: A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images.
- Select Use in-transit encryption to encrypt transferred data.
- (Optional) Device Path: Select a device path for the block volume.
- Select the Access type from one of three options:
- Read/write
- Read/write, shareable
- Read only, shareable
- Select Create and attach .

For detailed explanations of volume creation options see:[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm).

[Enter volume OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#)

To select an existing volume using the OCID, perform the following steps:
- Enter the block volume OCID in the Block volume OCID text box.
- Select an Attachment type :

Select Recommended or Custom . Recommended selected:
- Attachment Type: iSCSI
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- (Optional) Device Path: Select a device path for the block volume. Custom selected:
- Select one of the following options:
- (Recommended) iSCSI: A TCP/IP-based standard used for communication between a volume and attached instance.
- Select Require CHAP credentials to enable CHAP authentication.
- Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to enable automatic volume connections.
- Paravirtualized: A virtualized attachment available for VMs. This is the default for boot volumes and remote block storage volumes on platform images.
- Select Use in-transit encryption to encrypt transferred data.
- (Optional) Device Path: Select a device path for the block volume.
- Select the Access type from one of three options:
- Read/write
- Read/write, shareable
- Read only, shareable
- Select Attach .

For detailed explanations of attachment options see:[Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).

## Review

Important  
  
If your console displays a Live migration option after the storage section, details for these options are described in[1. Basic Information](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#basic-information)--&gt; Shape --&gt; Advanced Options --&gt; Availability configuration.
Important  
  
If your console displays Advanced options after the storage section, details for these options are described in[1. Basic Information](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#basic-information)--&gt; Shape --&gt; Advanced Options.

Review the options you selected.

To create the instance, select Create .

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).

## What's Next

Here are some things you can do with the new instance.
- After the instance is provisioned, details about it appear in the instance list. To view more details, such as IP addresses and the initial password (for Windows instances), click the instance name.
- When the instance is fully provisioned and running, you can connect to the instance. You[connect to a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm)by using a Secure Shell (SSH) connection, and you[connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm)by using a Remote Desktop connection.
- To get messages when something happens with the instance,[set up contextual notifications for the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/contextual-notifications-compute.htm).
- You can attach a[block volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm)to the instance, if the volume is in the same availability domain.
- You can[let additional users connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)instance launch`command and required parameters to create an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to create instances:
- [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
- [LaunchInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstanceConfiguration): Create an instance from an instance configuration

You can also launch instances from images that are published by Oracle partners in the Partner Image catalog. Use these APIs to work with the Partner Image catalog listings:
- [AppCatalogListing](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListing)
- [AppCatalogListingResourceVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion)
- [AppCatalogListingResourceVersionAgreements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)
- [AppCatalogListingResourceVersionSummary](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionSummary)
- [AppCatalogListingSummary](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogListingSummary)
- [AppCatalogSubscription](https://docs.oracle.com/iaas/api/#/en/iaas/latest/AppCatalogSubscription)
