# Free Tier: Install WordPress on an Ubuntu Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Free Tier: Install WordPress on an Ubuntu Instance

In this tutorial, use an Oracle Cloud Infrastructure Free Tier account to set up an Ubuntu instance. Next, install an Apache web server, PHP 8, MySQL, and finally WordPress. After installation, access your new WordPress installation from the internet. This tutorial covers all the steps necessary to set up a virtual network, a compute instance, and connect the host to the internet.

Key tasks include how to:
- Set up a compartment for your development work.
- Install an Ubuntu Linux instance and connect it to a Virtual Cloud Network (VCN).
- Set up an Oracle Cloud Infrastructure virtual cloud network and related network services required for a host to connect to the internet.
- Set up`ssh`encryption keys to access the Ubuntu Linux Server.
- Configure ingress rules for a VCN.
- Configure Apache, PHP 8, MySQL, and WordPress on the VM.
- Connect to the instance from the internet.

Here is a simplified diagram of the setup for the Linux VM.

For additional information, see:
- [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)
- [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/../apache-on-oracle-linux/01-summary.htm)

## Before You Begin

To successfully complete this tutorial, you must have the following:

### Requirements
- An Oracle Cloud Infrastructure Free Tier account.[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
- A MacOS, Linux, or Windows computer with`ssh`support installed.

## 1. Set up a Compartment for Development

Configure a compartment for your development.

[Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

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

[Review Installation Steps](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

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

The Create a VM Instance workflow automatically creates a VCN for your VM. You add an ingress rule to the subnet to allow internet connections on port 80.

[Create an Ingress Rule for the VCN](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

Follow these steps to select the VCN's public subnet and add the ingress rule.

- Open the navigation menu and click Networking , and then click Virtual Cloud Networks .
- Select the VCN you created with the compute instance.
- With the new VCN displayed, click &lt;your-subnet-name&gt; subnet link.

The public subnet information is displayed with the Security Lists at the bottom of the page. A link to the Default Security List for the VCN is displayed.
- Click the Default Security List link.

The default Ingress Rules for the VCN are displayed.
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
- Click Add Ingress Rules .
Now HTTP connections are allowed. The VCN is configured for HTTP traffic on port 80.
You have successfully created an ingress rule that makes the instance available on port 80 from the internet.

## 4. Install and Configure Apache, PHP 8, MySQL, and WordPress

Next install and configure Apache web server and PHP to run on the Ubuntu Linux instance.

[Configure the Ubuntu Firewall](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

Connect to the Ubuntu instance and configure the firewall settings. Follow these steps:
- Sign in to your Free Tier account.
- Open the navigation menu and click Compute . Under Compute , click Instances .
- Click the link to the instance you created in the previous step.

From the Instance Access section, write down the Public IP Address the system created for you. You use this IP address to connect to the instance.
- Open a Terminal window.
- Change into the directory where you stored the`ssh`encryption keys you created in part 1.
- Connect to the VM with this SSH command.

```

```

Since you identified your public key when you created the VM, this command logs you into the VM. You can now issue`sudo`commands to install and start the server.
- Update firewall settings.

Next, update the`iptables`configuration to allow HTTP traffic. To update`iptables`, run the following commands.

```

```

```

```

The commands add a rule to allow HTTP traffic and saves the changes to the`iptables`configuration files.

[Install Apache Server](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

- Install Apache Server.

```

```

```

```

- Next start Apache.

```

```

- You can now test the server.

You can test the server from the command line with`curl localhost`. Or, you can connect your browser to the public IP address assigned to the VM: http:// &lt;your-public-ip-address&gt; . The page looks similar to:

[Install PHP](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

- Install PHP and then some helpful modules with the following commands.

```

```

```

```

- Verify installation and restart Apache.

```

```

```

```

- Add a PHP test file to the VM.

```

```

- In the file, input the following text and save the file:

```

```

- Connect to http:// &lt;your-public-ip-address&gt; /info.php .

The browser produces a listing of the PHP configuration on the VM similar to the following.
Tip  
  
The image will differ due to operating system updates.

You have successfully installed Apache and PHP on an Oracle Cloud Infrastructure instance.
Note  
  
After you are done testing, delete the`info.php`file.

[Configure Apache HTML Directory](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

Set up the Apache server to read and write from the`/var/www/html`directory.
- Add a username to the`www-data`group so you can edit the`/var/www/html`directory.

```

```

- Now change the ownership of the content directory.

```

```

- Change permissions on the files and directory.

```

```

- Reboot your machine for changes to take effect.

[Install and Configure MySQL Server and Client](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

Next, you install and configure the MySQL server and client so it can be used with WordPress.
Important  
  
Because of configuration changes to the Ubuntu MySQL setup, this tutorial adds additional steps before and after the`sudo mysql_secure_installation`script. The new steps are required for the`mysql_secure_installation`script to complete successfully.
- Install the MySQL Server package.

```

```

This step can take some time.
- Sign in to MySQL.

```

```

- Change the MySQL`root`user to allow password authentication.

```

```

Note  
  
This password is temporary. You reset the root password in the following steps.
- Exit MySQL.

```

```

- Secure MySQL with the`mysql_secure_installation`script.
- Run the script.

```

```

Produces this output:
```

```

- You are prompted for the temporary password you set.
```

```

Enter the password.
- Turn on Password Validation:
```

```

- Select`Y`.
- Select the password validation level.
```

```

- Change the root password.
```

```

- Select`Y`.
- Set the root password.
```

```

Note  
  
This step replaces the initial temporary password set earlier.
- Select`Y`.
- Select the remaining security options.
```

```

Tip  
  
Taking the default values,`Y`to all options, is recommended.
- Sign in to MySQL with the new password.

```

```

- Change the MySQL authentication method back to`auth_socket`.

```

```

Tip  
  
The`auth_socket`authentication method allows you to authenticate with`sudo`rather than with a MySQL password.
- Exit MySQL.

```

```

[Set up WordPress MySQL Database](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

- Sign in to MySQL.

```

```

You get a MySQL prompt.
- List the default databases.

```

```

- Create a user for MySQL.

```

```

- Make the user an admin.

```

```

- Create the WordPress database.

```

```

- Check the result.

```

```

- Flush privileges to clear cached memory.

```

```

[Install and Configure WordPress](https://docs.oracle.com/en-us/iaas/Content/developer/wp-on-ubuntu/01-summary.htm#)

Download and follow these steps to install WordPress on the server.
- Open a terminal window and create a`tmp`directory.
- Download the WordPress Linux zip from`https://wordpress.org/download/`and unzip.

```

```

```

```

The command creates a`wordpress`directory with the PHP code for WordPress in it.
- Copy the contents of the`wordpress`directory to the`/var/www/html`directory.

```

```

The contents of the`wordpress`directory are copied into the`/var/www/html`directory. This command is a sample. The command might differ depending on the name of your directories.
- Change into to the`/var/www/html`directory.

```

```

- Rename the default`index.html`file.

```

```

Now`index.php`is loaded by default when the root directory is accessed.
- Rename the`wp-config-sample.php`file.

```

```

- Update the values for the MySQL set up.

```

```

- Run the installation script by opening a browser and this URL:`http:// <your-public-ip-address> /wp-admin/install.php`
Note  
  
Create an administrator account for the WordPress blog. Ensure you write down the information from the install page. You need the information to sign in to the WordPress blog.
- Open the new blog at:`http:// <your-public-ip-address>`

Finish any other configuration you need for WordPress. Here is a link to help.
- [First Steps with WordPress](https://wordpress.org/support/article/first-steps-with-wordpress/).

You have set up a WordPress blog on an OCI compute instance.

## What's Next

You have successfully installed and deployed an Apache web server on Oracle Cloud Infrastructure using a Linux instance.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
