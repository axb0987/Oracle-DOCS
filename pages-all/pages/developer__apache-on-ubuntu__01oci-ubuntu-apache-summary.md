# Free Tier: Install Apache and PHP on an Ubuntu Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Free Tier: Install Apache and PHP on an Ubuntu Instance

In this tutorial, you use an Oracle Cloud Infrastructure Free Tier account to set up a compute instance on the latest version of Ubuntu. Then, you install an Apache web server and PHP and access your new server from the internet. Finally, this tutorial covers all the steps necessary to set up a virtual network for your host and connect the host to the internet.

Key tasks include how to:
- Set up a compartment for your development work.
- Install your Ubuntu instance and connect it to your Virtual Cloud Network (VCN).
- Set up an Oracle Cloud Infrastructure virtual cloud network and related network services required for your host to connect to the internet.
- Set up`ssh`encryption keys to access your Ubuntu server.
- Configure ingress rules for your VCN.
- Configure Apache and PHP 8 on your instance.
- Connect to your instance from the internet.

Here is a simplified diagram of the setup for your Linux VM.

For additional information, see:
- [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)
- [Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm)

## Before You Begin

To successfully complete this tutorial, you must have the following:

### Requirements
- An Oracle Cloud Infrastructure Free Tier account.[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
- A MacOS, Linux, or Windows computer with`ssh`support installed.

## 1. Set up a Compartment for Development

Configure a compartment for your development.

[Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm#)

Create a compartment for the resources that you create in this tutorial.
- Sign in to the Oracle Cloud Infrastructure Console .
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Compartments .
- Click Create Compartment .
- Fill in the following information:
- Name:`<your-compartment-name>`
- Description:`Compartment for <your-description> .`
- Parent Compartment:`<your-tenancy> (root)`
- Click Create Compartment .

Reference:[Create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To)

## 2. Install an Ubuntu Linux Instance

Use the Create a VM Instance workflow to create a new compute instance.

The workflow does several things when installing the instance:
- Creates and installs a compute instance running Ubuntu Linux.
- Creates a VCN with the required subnet and components needed to connect the Ubuntu Linux instance to the internet.
- Creates an`ssh`key pair you use to connect to the instance.

[Review Installation Steps](https://docs.oracle.com/en-us/iaas/Content/developer/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm#)

To get started installing an instance with the Create a VM instance workflow, follow these steps:
Important  
  
The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.

- Click the Oracle Cloud icon to go to the main landing page.

- Scroll down to Launch Resources .
- Select Create a VM instance workflow.

The Create compute instance page is displayed. The page sections include
- Name and Compartment
- Placement
- Security
- Image and shape
- Networking
- Add SSH keys
- Boot volume
- Choose the Name and Compartment .

Initial Options
- Name:`<name-for-the-instance>`
- Create in compartment:`<your-compartment-name>`

Enter a value for the name or use the system supplied default. For compartment, select the compartment you created.
- Review the Placement settings.

- Take the default values. An availability domain is assigned to you.

The data might look similar to the following:

Availability domain
- Availability domain: AD-1
- Capacity type: On-demand capacity
- Fault domain: Let Oracle choose the best fault domain
Note  
  
For Free Tier, use the Always Free Eligible option for availability domain.
- Review the Security settings.

- Take the default settings.

The data might look similar to the following:

Security
- Shielded instance: Disabled
- Confidential computing: Disabled
- Review the Image and shape settings. Change the operating system image.

- Click Edit .
- Click Change Image .
- Click Ubuntu .
- Select Canonical Ubuntu 22.04 or a later version.
- Click Select Image .
Note  
  
The following is sample data for an AMD virtual machine. The actual values might differ.

Image and shape
- Image: Canonical Ubuntu 22.04
- Image build:`<current-build-date>`
- Shape: VM.Standard.E2.1.Micro
- OCPU: 1
- Memory (GB): 1
- Network bandwidth (Gbps): 0.48
Note  
  
For Free Tier, use Always Free Eligible shape options.
- Continue to the next section.
- Review the Networking settings. Make the following changes to the default.

- Click Edit .
- Primary Network : Select Create new virtual cloud network .
- New virtual cloud network name : Take the generated VCN name or provide a name.
- Create in compartment :`<your-compartment-name>.`
- Subnet : Select Create new public subnet .
- New subnet name : Take the generated subnet name or provide a name.
- Create in compartment :`<your-compartment-name>`.
- CIDR block : Take the default value (for example, 10.0.0.0/24).
- Public IPv4 address , take the default value of Assign a public IPv4 address .
- Continue to the next section.
- Review the Add SSH keys settings. Take the default values provided by the workflow.

- Select the Generate a key pair for me option.
- Click Save Private Key and Save Public Key to save the private and public SSH keys for this compute instance.

If you want to use your own SSH keys, select one of the options to provide your public key.
Note  
  
Put your private and public key files in a safe location. You can't retrieve keys again after the compute instance has been created.
- Review the Boot volume settings.

Uncheck the Specify a customer boot volume size setting.

Check the Use in-transit encryption setting.

Uncheck the Encrypt this volume with a key that you manage setting.
- Click Create to create the instance. Provisioning the system might take several minutes.
You have successfully created an Ubuntu Linux instance.

## 3. Enable Internet Access

The Create a VM Instance wizard automatically creates a VCN for your VM. You add an ingress rule to your subnet to allow internet connections on port 80.

[Create an Ingress Rule for your VCN](https://docs.oracle.com/en-us/iaas/Content/developer/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm#)

Follow these steps to select your VCN's public subnet and add the ingress rule.

- Open the navigation menu and click Networking , and then click Virtual Cloud Networks .
- Select the VCN you created with your compute instance.
- With your new VCN displayed, click &lt;your-subnet-name&gt; subnet link.

The public subnet information is displayed with the Security Lists at the bottom of the page. A link to the Default Security List for your VCN is displayed.
- Click the Default Security List link.

The default Ingress Rules for your VCN are displayed.
- Click Add Ingress Rules .

An Add Ingress Rules dialog is displayed.
- Fill in the ingress rule with the following information.

Fill in the ingress rule as follows:
- Stateless: Checked
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source port range: (leave-blank)
- Destination Port Range: 80
- Description: Allow HTTP connections

Click Add Ingress Rules . Now HTTP connections are allowed. Your VCN is configured for Apache server.
- Click Add Ingress Rules .
Now HTTP connections are allowed. Your VCN is configured for Apache server.
You have successfully created an ingress rule that makes your instance available from the internet.

## 4. Set up Apache and PHP

Next install and configure Apache web server and PHP to run on your Ubuntu Linux instance.

[Install and Configure Apache and PHP](https://docs.oracle.com/en-us/iaas/Content/developer/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm#)

To install and set up Apache and PHP, perform the following steps:

- Open the navigation menu and click Compute . Under Compute , click Instances .
- Click the link to the instance you created in the previous step.

From the Instance Details page look under the Instance Access section, the Public IP Address field. Write down the public IP address the system created for you. You use this IP address to connect to your instance.
- Open a Terminal or Command Prompt window.
- Change into the directory where you stored the`ssh`encryption keys you created before.
- Connect to your instance with this SSH command.

```

```

Since you identified your public key when you created the instance, this command logs you into your instance. You can now issue`sudo`commands to install and start your server.
- Install Apache Server.

```

```

- Next start Apache.

```

```

- Update firewall settings.

The Ubuntu firewall is disabled by default. However, you still need to update your`iptables`configuration to allow HTTP traffic. Update`iptables`with the following commands.

```

```

The commands add a rule to allow HTTP traffic and saves the changes to the`iptables`configuration files.
- You can now test your server.

You can test your server from the command line with`curl localhost`. Or, you can connect your browser to your public IP address assigned to your instance: http:// &lt;x.x.x.x&gt; . The page looks similar to:
- Install PHP 8 with the following commands.

```

```

- Verify installation and restart Apache.

```

```

- Add a PHP test file to your instance.

Create the file:

```

```

- In the file, input the following text and save the file:

```

```

- Connect to http:// &lt;your-public-ip-address&gt; /info.php .

The browser produces a listing of PHP configuration on your instance similar to the following.
Tip  
  
The image will differ due to operating system updates.
Note  
  
After you are done testing, remove info.php from the system.
Congratulations! You have successfully installed Apache and PHP 8 on an Oracle Cloud Infrastructure instance.

## What's Next

You have successfully installed and deployed an Apache web server and PHP on Oracle Cloud Infrastructure using a Linux instance.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
