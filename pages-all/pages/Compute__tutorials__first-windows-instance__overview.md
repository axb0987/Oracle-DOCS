# Launching Your First Windows Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm
- Fetched: 2026-09-05 01:52 CDT

# Launching Your First Windows Instance

In this tutorial, perform the steps to create and connect to an OCI Compute Windows instance. After your instance is up and running, optionally create and attach a block volume.

Key tasks:
- Create a compartment.
- Create a virtual cloud network and subnet that enables internet access.
- Create a Windows instance.
- Connect to the Windows instance.
- (Optional) Create and attach a block volume to the Windows instance.
- (Optional) Clean up after completing the tutorial.

The following figure depicts the components you create in the tutorial.

[

## Before You Begin

To successfully complete this tutorial, you must have the following: Requirements
- An[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)account or paid account.
- A MacOS, Linux, or Windows computer with a Windows remote desktop client installed.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## 1. Create a Compartment

Compartments help you organize and control access to resources. A compartment is a collection of related resources (such as cloud networks, Compute instances, or block volumes). Only users in groups given permission by an administrator in your organization, have access to specific compartments. For example, one compartment could contain all the servers and storage volumes that make up the production version of a company's Human Resources system. Only users with permission to that compartment can manage those servers and volumes.

[Steps to Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .
- Click Create Compartment .
- Enter the following:
- Name: Enter`<your-compartment-name>`
- Description : Enter a description (required), for example: "`<your-compartment-name>`compartment for the getting started tutorial". Avoid entering confidential information.
- Parent Compartment: Select the compartment you want this compartment to reside in. Defaults to the root compartment (or tenancy).
- 

Click Create Compartment .

Your compartment is displayed in the list.

When you select your compartment, you only see resources in that compartment. When you create new resources you select the compartment to create them in. The compartment control defaults to the last compartment selected.

## 2. Create a Virtual Cloud Network

Before you can launch an instance, create a virtual cloud network (VCN) and subnet to launch the instance into. A subnet is a subdivision of your VCN defined using a range of IP addresses with public or private access. The subnet directs traffic according to a route table . In addition, a subnet's security list controls traffic in and out of the instance. For this tutorial, access the instance over the internet using the instance's public IP address. The route table directs traffic to an internet gateway.

For information about VCN features, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm).

Use the Start VCN Wizard workflow to create a new Virtual Cloud Network (VCN). The workflow does several things when installing the VCN:
- Creates a VCN.
- Adds an Internet Gateway which enables internet connections.
- Creates and configures public and private subnets for the VCN.
- Sets up route tables and security lists for the subnets.

For more information on VCNs, see:[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

[Steps to Create a VCN](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

To create a VCN, follow these steps:
Important  
  
The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- If needed, select the compartment you created in the preceding step from the compartments list in the left navigation.
- Click Start VCN Wizard .
- Select Create VCN with Internet Connectivity .
- Click Start VCN Wizard .
- Configure the VCN. The configure dialog contains the following sections.

Basic Information

Enter the VCN Name and select a Compartment .
- Name:`<name-for-the-vcn>`

Enter a name for your VCN. Avoid entering confidential information.
- Compartment:`<your-compartment-name>`

Select your compartment.

Configure VCN
- Keep the default values for VCN IPv4 CIDR block and DNS resolution .

Configure public subnet
- Keep the default values for IP address type and IPv4 CIDR block .

Configure private subnet
- Keep the default values for IP address type and IPv4 CIDR block .
- Click Next .
- Review you selections. Click Previous to go back and make changes.
- Click Create to create the VCN.

The system creates the VCN and all its resources. This might take a moment.

After the creation is complete, click View VCN to see your new VCN.

[Edit the Default Security List to Allow Traffic to Your Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

To enable network traffic to reach your Windows instance, you need to add a security list rule to enable Remote Desktop Protocol (RDP) access. Specifically, for the default security list (which is used by the public subnet), you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port.

To edit the VCN's security list:
- Click the name of the VCN that you just created. The VCN details are displayed.
- Under Resources , click Security Lists .
- 

Click the default security list for your VCN.

The security list details are displayed.
- Click Add Ingress Rules .
- Enter the following for your new rule:
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: RDP (TCP/3389)
- Source Port Range: All
- Destination Port Range: 3389
- When done, click Add Ingress Rules .

## 3. Create a Windows Virtual Machine Instance

Next, launch a Windows server instance with a basic shape. Use the Create a VM Instance workflow to create a new compute instance. The workflow does several things when installing the instance:
- Creates and installs a compute instance running Windows Server.
- Selects your VCN and public subnet to connect the Windows Server instance to the internet.
- Creates a default password you use to connect to the instance.

[Steps to Create a Windows Virtual Machine Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

To get started installing an instance with the Create a VM instance workflow, follow these steps:
Important  
  
The steps provided are for a paid account.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Click Create Instance .

The Create compute instance page is displayed.
- Choose the Name and Compartment .

Initial Options
- Name:`<name-for-the-instance>`

Enter a name for your instance. Avoid entering confidential information.
- Create in compartment:`<your-compartment-name>`

Select your compartment. Use the compartment created in the preceding step.
- Review the Placement settings.
- Take the default values. An availability domain is assigned to you.

The default values are similar to the following:
- Availability domain: AD-1
- Capacity type: On-demand capacity
- Fault domain: Let Oracle choose the best fault domain
- Review the Security settings.
- Take the default settings.

The default values are similar to the following:
- Shielded instance: Disabled
- Confidential computing: Disabled
- Review the Image and shape settings.
- Click Change image .
- Select Windows .
- Select the Windows Server 2022 Standard image.
- Check I have reviewed and accept the following documents: Oracle and Microsoft Windows Terms of Use .
- Click Select image .
- Use the default shape, for example VM.Standard.E5.Flex .

Selected values are similar to the following:
- Image: Windows Server 2022 Standard
- Image build:`<current-build-date>`
- Shape: VM.Standard.E5.Flex
- OCPU: 1
- Memory (GB): 12
- Network bandwidth (Gbps): 1
- Select and review the Primary VNIC and Networking settings.
- (Optional) Enter a name for VNIC name .
- Select the VCN you created in the preceding step.
- Select the public subnet you created in the preceding step.

The Primary VNIC and Networking values are similar to the following:
- Virtual cloud network: &lt;your-vcn&gt;
- Subnet: &lt;pubic-subnet-for-your-vcn&gt;
- Private IPv4 address: Automatically assign private IPv4 address
- Public IPv4 address: Checked
- IPv6 address: Unchecked
- Advanced Options:
- Use network security groups to control traffic: Unchecked
- DNS record: Assign a private DNS record
- Launch options: Let Oracle Cloud Infrastructure choose the best networking type
- Review the Boot volume settings.

Select the Use in-transit encryption setting. Leave the other settings blank.
- Review the Block Volume settings. Take the default values provided by the workflow which does not select any block volumes. You can add block volumes later.
- Leave the Live Migration option selected.
- Click Create to create the instance.

The instance is displayed in the Console in a provisioning state. Expect provisioning to take several minutes before the state updates to running. Do not refresh the page. After the instance is running, allow another few minutes for the operating system to boot before you attempt to connect.

## 4. Connect to Your Instance

Connect to a running Windows instance using Remote Desktop.
Important  
  

By default, Remote Desktop supports 2 simultaneous sessions. If a user account logs on to the system locally, then only one user is allowed to establish a remote desktop connection to the system.

Open the Task Manager , then select the Users tab, to check the current logged in user accounts and sessions.

[Connect to Your Windows Instance from a Remote Desktop Client](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

Use the following steps to connect to your Windows instance.
- Open the Remote Desktop client.
Tip  
  
You may have to search for the app with Windows search.
- 

In the Computer field, enter the public IP address that you retrieved from the Console.
- The User name is`opc`. Depending on the Remote Desktop client you are using, you might have to connect to the instance before you can enter this credential.
- 

Click Connect to start the session.
- 

Accept the certificate if you are prompted to do so.
- 

Enter the initial password that you retrieved from the Console. You are prompted to change the password as soon as you log in.

The new password must be at least 12 characters long and must comply with[Microsoft's password policy](https://technet.microsoft.com/library/hh994562(v=ws.11).aspx?f=255&MSPPError=-2147217396).
- 

Press Enter .
Note  
  
The default user,`opc`, has administrative privileges.

## 5. (Optional) Add a Block Volume

Block Volume provides network storage to use with your Oracle Cloud Infrastructure instances. After you create, attach, and mount a volume to your instance, you can use it just as you would a physical hard drive on your computer. A volume can be attached to a single instance, but you can detach the volume from one instance and attach it to another instance, keeping your data intact.

For complete details on Block Volume, see[Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm).

[Create a Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .
- Click Create Block Volume .
- In the Create Block Volume dialog, enter the following:
- Name: Enter a user-friendly name. Avoid entering confidential information.
- Create in Compartment: This field defaults to your current compartment. Select the compartment you want to create the volume in, if not already selected.
- Availability domain: Select the same availability domain that you selected for your instance. If you followed the tutorial instructions when launching your instance, this is the first AD in the list. The volume and the instance must be in the same availability domain.
- Cluster Placement Group : Keep default of`none`. (This option may not appear depending on the account type.)
- Volume size and performance
- Select Custom . This selects the following defaults:
- Volume size : 1024GB

For testing, change the volume size to 256GB or a different value of your choice.
- Performance based auto-tune: Off
- Volume performance : Balanced
- Default VPUs/GB: 10
- IOPS : 25,000 IOPS
- Throughput : 480 MB/s
- Detached volume auto-tune: Off
Important  
  
The values listed are for a paid account. The defaults might change for a Free Tier account.
- Backup Policy: Do not select a backup policy.
- Cross region replication : Select OFF .
- Volume Encryption : Select Encrypt using Oracle-managed keys .
- Tags: Leave the tagging fields blank.
- Leave View detail page after this block volume is created checked.
- Click Create Block Volume .

The block volume provisioning starts. After the volume is provisioned, you can attach it to your instance.

[Attach the Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

Next, attach the volume to your instance:
- 

Find your instance: Open the navigation menu and select Compute . Under Compute , select Instances .
- 

Click your instance name to view its details.
- In the Resources section, click Attach block volumes .
- Click Attach block volume .
- Enter the following:
- Volume: select the Select volume option.
- If you need to change the compartment, click Change Compartment , and then select the compartment where you created the block volume.
- Volume in &lt;compartment&gt; : Select the block volume from the list.
- Attachment type:
- Select Recommended .

This selects Paravirtualized .
- Leave Use in-transit encryption unchecked.
Note  
  
The Custom option allows you select iSCSI or NVMe attachment types.
- Access: Select Read/Write .
- Click Attach .

The attachment process takes about a minute. You'll know the volume is ready when the Attachment State for the volume is ATTACHED.

[Connect to the Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

For volumes attached with Paravirtualized as the attachment type, you don't need to perform any additional steps after attaching the volumes. The volume is connected automatically.

To verify your volume is connected:
- Log on to your instance as described in[4. Connect to Your Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#connect-to-vm-instance).
- Click Start .
- Select Windows Administrative Tools .
- Select Computer Management .
- Under Storage select Disk Management .
- (Optional) You are prompted to initialize your disk. You can initialize and format the disk as needed.

You can now use the attached block volume as needed.

## 6. (Optional) Clean up Resources

After you've finished with the resources that you created for this tutorial, clean up by terminating the instance and deleting the resources that you don't intend to continue working with.

[Detach and Delete the Block Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Find your instance in the Instances list and click its name to display its details.
- In the Resources section on the Instance Details page, click Attached Block Volumes .
- Find your volume, click the Actions menu (three dots) , and then click Detach .
- Click Continue Detachment and then click OK .
- When the Console shows the volume status as Detached, you can delete the volume. Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .
- Find your volume, click the Actions menu (three dots) , and then click Terminate . Confirm when prompted.

[Terminate the Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

- Open the navigation menu and select Compute . Under Compute , select Instances .
- In the list of instances, find the instance you created in the tutorial.
- Click the Actions menu (three dots) , and then click Terminate .
- Select the Permanently delete the attached boot volume check box, and then click Terminate instance .

[Delete the Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/overview.htm#)

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- In the list of VCNs, find the one you created in the tutorial.
- Click the Actions menu (three dots) , and then click Terminate .
- 

Click Terminate All to delete all the underlying resources of your VCN.

When all the resources are successfully deleted you can close the dialog.

## What's Next

Now that you've got a Compute instance running and attached some storage, consider the following next steps:
- Install your own software on the instance.
- Add more users to work with Oracle Cloud Infrastructure. See[Adding Users to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-windows-instance/../../Tasks/addingusers.htm)
