# Free Tier: Install Spring Boot on an Oracle Linux Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm
- Fetched: 2026-09-05 03:31 CDT

# Free Tier: Install Spring Boot on an Oracle Linux Instance

In this tutorial, use an Oracle Cloud Infrastructure Free Tier account to set up an Oracle Linux compute instance. Then, install a Spring Boot application and access your new app from the internet. Finally, this tutorial covers all the steps necessary to set up a virtual network for your host and connect the host to the internet.

Key tasks include how to:
- Set up a compartment for your development work.
- Install your Oracle Linux instance and connect it to your Virtual Cloud Network (VCN).
- Set up an Oracle Cloud Infrastructure virtual cloud network and related network services required for your host to connect to the internet.
- Set up`ssh`encryption keys to access your Oracle Linux Server.
- Configure ingress rules for your VCN.
- Configure Spring Boot on your instance.
- Connect to your instance from the internet.

Here is a simplified diagram of the setup for your Linux instance.

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

[Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

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

## 2. Install a Virtual Cloud Network

Use the Start VCN Wizard workflow to create a new Virtual Cloud Network (VCN).

The workflow does several things when installing the VCN:
- Creates a VCN.
- Adds an Internet Gateway which enables internet connections.
- Creates and configures public and private subnets for the VCN.
- Sets up route tables and security lists for the subnets.

For more information on VCNs, see:[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

[Review Installation Steps](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

To create a VCN, follow these steps:
Important  
  
The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- If needed, select your compartment from the Compartment control in the left navigation.
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

Once the creation is complete, click View VCN to see your new VCN.

## 3. Install an Oracle Linux Instance

Use the Create a VM Instance workflow to create a new compute instance.

The workflow does several things when installing the instance:
- Creates and installs a compute instance running Oracle Linux.
- Select your VCN and public subnet to connect the Oracle Linux instance to the internet.
- Creates an`ssh`key pair you use to connect to the instance.

[Review Installation Steps](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

To get started installing an instance with the Create a VM instance workflow, follow these steps:
Important  
  
The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.
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
Note  
  
For Free Tier, use the Always Free Eligible option for availability domain.
- Review the Security settings.
- Take the default settings.

The default values are similar to the following:
- Shielded instance: Disabled
- Confidential computing: Disabled
- Review the Image and shape settings. Click Edit .
Note  
  
The following is sample data for an Ampere A1 virtual machine. The actual values might differ.
- Keep the default Oracle Linux 8 image.
- Click Change Shape .
- Select Virtual Machine .
- For shape series select Ampere .
- Select VM.Standard.A1.Flex the "Always Free" shape.
- Select 1 OCPUs.
- Click Select Shape .

Selected values are similar to the following:
- Image: Oracle Linux 8
- Image build:`<current-build-date>`
- Shape: VM.Standard.A1.Flex
- OCPU: 1
- Memory (GB): 6
- Network bandwidth (Gbps): 1
Note  
  
For Free Tier, use Always Free Eligible shape options.
- Review the Networking settings. Select the VCN you created in the preceding step. The networking values are similar to the following:
- Virtual cloud network: &lt;your-vcn&gt;
- Subnet: &lt;pubic-subnet-for-your-vcn&gt;
- Launch options: -
- DNS record: Yes
- Use network security groups to control traffic: No
- Assign a public IPv4 address: Yes
- Private IPv4 address: Automatically assigned on creation
- IPv6 address: Not available
- Review the Add SSH keys settings. Take the default values provided by the workflow.
- Select the Generate a key pair for me option.
- Click Save Private Key and Save Public Key to save the private and public SSH keys for this compute instance.

If you want to use your own SSH keys, select one of the options to provide your public key.
Note  
  
Put your private and public key files in a safe location. You can't retrieve keys again after the compute instance has been created.
- Review the Boot volume settings.

Select the Use in-transit encryption setting. Leave the other two settings blank.
- Review the Block Volume settings. Take the default values provided by the workflow which does not select any block volumes. You can add block volumes later.
- Click Create to create the instance. Provisioning the system might take several minutes.

You have successfully created an Oracle Linux instance to run an Apache Web Server.

## 4. Enable Internet Access

The Create a VM Instance wizard automatically creates a VCN for your instance. You add an ingress rule to your subnet to allow internet connections on port 8080.

[Create an Ingress Rule for your VCN](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

Follow these steps to select your VCN's public subnet and add the ingress rule.

- Open the navigation menu and click Networking , and then click Virtual Cloud Networks .
- Select the VCN you created.
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
- Destination Port Range: 8080
- Description: Allow HTTP connections
- Click Add Ingress Rules .
Now HTTP connections are allowed. Your VCN is configured for Spring Boot.
You have successfully created an ingress rule that makes your instance available from the internet.

## 5. Install and Configure Spring Boot

Next, install all the software needed for your Spring Boot application.

[Configure the Port for your Instance](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

- Open the navigation menu and click Compute . Under Compute , click Instances .
- Click the link to the instance you created in the previous step.

From the Instance Details page look under the Instance Access section. Write down the public IP address the system created for you. You use this IP address to connect to your instance.
- Open a Terminal or Command Prompt window.
- Change into the directory where you stored the`ssh`encryption keys you created.
- Connect to your instance with this SSH command

```

```

Since you identified your public key when you created the instance, this command logs you into your instance. You can now issue`sudo`commands to install and start your server.
- Enable an HTTP connection on port 8080.

```

```

```

```

The firewall is configured for Spring Boot.

[Install Git](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

Install Git v2 using the IUS Community Project ([https://ius.io/](https://ius.io/)). Navigate to the current version of Git core package and download to a`~/temp`directory.
- For example, downloading the Git RPM looks similar to the following.

```

```

- Install the RPM with`yum`.

```

```

- Test result.

```

```

Git is installed.

[Install JDK 8](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

- Install OpenJDK 8 using`yum`.

```

```

- Set`JAVA_HOME`in`.bashrc`.

Update the file:

```

```

In the file, append the following text and save the file:

```

```

Activate the preceding command in the current window.

```

```

Java is installed.

[Install Maven 3.6](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

Install Maven from an Apache mirror. Go to the main Maven site's ([https://maven.apache.org/](https://maven.apache.org/)) download page. Get the URL for the latest version and download with wget.
- Download the Maven zip file, for example:

```

```

- Extract the program files.

```

```

- Install the program files by moving the files to the`/opt`directory.

```

```

- Add the Maven path`/opt/apache-maven-3.6.3/bin`to your`PATH`environment variable and source your`.bashrc`.

```

```

Maven is ready to use.

[Build Your Spring Boot Application](https://docs.oracle.com/en-us/iaas/Content/developer/spring-on-ol/01oci-ol-spring-summary.htm#)

Follow these steps to set up your Spring Boot application:

- From your home directory check out the Spring Boot Docker guide with Git:

```

```

- Change into the`gs-spring-boot-docker/initial`directory.
- Edit the`Application.java`file:`src/main/java/hello/Application.java`.
- Update the code with the following:

```

```

- Save the file.
- Use Maven to build the application.

```

```

You get a message of success.
```

```

- Run the application.

```

```

- Test your application from the command line or a browser.

- From a new terminal, connect to your instance with your SSH keys and test with curl:

```

```

- From your browser connect to the public IP address assigned to your instance: http://&lt;x.x.x.x&gt;:8080 .

On your instance or in your browser, you see Spring Boot Hello World!
Congratulations! You have successfully created a Spring Boot application on your instance.

## What's Next

You have successfully installed and deployed a Spring Boot app on Oracle Cloud Infrastructure using a Linux instance.

To explore more information about development with Oracle products:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
