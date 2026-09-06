# Create a Compute Instance
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm
- Fetched: 2026-09-05 19:21 CDT

# Create a Compute Instance

Use Terraform to create a compute instance in your Oracle Cloud Infrastructure tenancy.

Key tasks include how to:
- Create SSH keys.
- Create a virtual cloud network in your tenancy.
- Use Oracle Cloud Infrastructure Terraform provider to create a compute instance in the network.
- Connect to your instance.

For more information, see:
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [Terraform Registry](https://registry.terraform.io/browse/providers)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- An Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial resources:
- Go through all the steps in:
- [Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- [Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)
- Keep the scripts you created in the following directories:
- `$HOME/tf-provider/`
- `$HOME/tf-compartment/`
- Keep the compartment from the tutorial[Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)in your tenancy.

## 1. Prepare

Prepare your environment for creating a compute instance. Also, collect all the information you need to complete the tutorial.

[Create SSH Encryption Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

Create`ssh`encryption keys to connect to your compute instance.

- Open a terminal window:

- MacOS or Linux : Open a terminal window in the directory where you want to store your keys.
- Windows : Right-click the directory where you want to store your keys and select Git Bash Here .
Note  
  
If you're using Windows Subsystem for Linux (WSL), ensure that the directory for the keys is directly on your Linux machine and not in a`/mnt`folder (windows file system).
- Issue the following OpenSSH command:

```

```

The command generates some random text art used to generate the keys. When complete, you have two files:
- The private key file:`<your-ssh-key-name>`
- The public key file:`<your-ssh-key-name> .pub`

You use these files to connect to your compute instance.

You have generated the required encryption keys.

For detailed information on generating`ssh`encryption keys, see[Creating a Key Pair](https://docs.oracle.com/iaas/Content/GSG/Tasks/creatingkeys.htm).

[Create a Virtual Cloud Network (VCN)](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- 

On the Virtual Cloud Networks list page, perform one of the following actions depending on the option that you see:
- From Actions , select Start VCN Wizard .
- Select Start VCN Wizard .
- In the Start VCN Wizard panel, select Create VCN with Internet Connectivity .
- Select Start VCN Wizard .

The Create a VCN with internet connectivity window opens.

#### 1. Configuration

Enter the following basic information:
- 

VCN name : &lt;your-vcn-name&gt;
- Compartment : &lt;your-compartment-name&gt;

##### Configure VCN

- 

VCN IPv4 CIDR block : Keep the default value: 10.0.0.0/16
- 

Use DNS hostnames in this VCN : Clear this checkbox.

##### Configure Public Subnet

- 

IPv4 CIDR block : Keep the default value: 10.0.0.0/24

##### Configure Private Subnet

- 

IPv4 CIDR block : Keep the default value: 10.0.1.0/24

Notice that the public and private subnets have different network addresses.

Select Next . The Review and create page opens.

#### 2. Review and create

Review the complete VCN configuration and then select Create .

Resources are created, and then a message appears stating that VCN creation is complete.

To view the created VCN, select View VCN .

You have successfully created a VCN to host your compute instance.

[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

Collect and copy the information you need into your notepad.
- Compartment name
- Compartment ID
- Subnet ID
- Source ID (image of compute instance)
- Shape (compute instance)
- SSH Authorized Key (public key path)
- Private SSH Key Path

For steps to collect this information, see the following table.

Item Steps to collect item
Compartment name Reference the completed tutorial[Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm).
Compartment ID
- In the Console search bar, enter`<your-compartment-name>`.
- Select`<your-compartment-name>`in the search results.
- Select Copy next to the OCID.
Instance display name Name of your choice.
Subnet ID
- In the Console: Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select`<your-vcn-name>`from[Configure VCN](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#configure-vcn).
- Select Subnets .
- Select &lt;your-compartment-name&gt; to show subnets in your compartment.
- From the Actions menu (three dots) for the public subnet, select Copy OCID .
Source ID (image of compute instance)
- In the Console navigation bar, find your region.

See[Working in Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm).
- Go to[Image Release Notes](https://docs.oracle.com/iaas/images/).
- Select Ubuntu 24.04 .

The list of images for Ubuntu 24.04 opens.
- Select the latest image: Canonical-Ubuntu-24.04-&lt;date&gt; .

The page lists image OCIDs.
- Find the image for your region and copy the image's OCID.

Note: Ensure that you select a commercial OCID without`gov`in its OCID.
Shape and configuration (compute instance)
- Shape:`VM.Standard.E5.Flex`
- OCPUs: 1
- Memory (GBs): 12

Note: The`VM.Standard.E5.Flex`requires values for OCPUs and memory. To select a different shape, go to[Virtual Machine (VM) Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vmshapes).
SSH Authorized Key (public key path) Reference the completed section,[Create SSH Encryption Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#create-ssh-keys). Use this path when you set up the compute instance.
Private SSH Key Path Reference the completed section,[Create SSH Encryption Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#create-ssh-keys). Use this private key when you connect to your compute instance.

[Add Resource Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can manage all resources in your compartment, giving you administrative rights in that compartment.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- In the Console: Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Select your compartment.
- Select Create Policy .
- On the Create Policy page, enter the following values:

- Name :`manage- <your-compartment-name> -resources`
- Description :`Allow users to list, create, update, and delete resources in <your-compartment-name>.`
- Compartment :`<your-tenancy> (root)`
- For Policy Builder , enter the following values:

- Policy use cases:`Compartment Management`
- Common policy templates:`Let compartment admins manage the compartment`
- Identity domain : &lt;identity-domain&gt;
- Groups:`<a-group-your-username-belongs-to>`
- Location:`<your-compartment-name>`
- Select Create .

Reference:[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)

## 2. Create Scripts

Create scripts for authentication, fetching data, creating a compute instance, and printing outputs.

[Add Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

First, set up a directory for your Terraform scripts. Then copy the provider and versions scripts from the[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)tutorial so your Oracle Cloud Infrastructure account can authenticate the scripts running from this directory.

- In your`$HOME`directory, create a directory called`tf-compute`, and then change to that directory.

```

```

```

```

- Copy the`provider.tf`file into the`tf-compute`directory.

```

```

- Copy the`versions.tf`file into the`tf-compute`directory.

```

```

[Fetch Data](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

Fetch the name of an availability domain from your account. An availability domain is one of the required inputs to create a compute instance.

- Copy the`availability-domains.tf`file into the`tf-compute`directory.

The`availability-domains.tf`file was created during the tutorial[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm).

```

```

Example code:

```

```

- In the`tf-compute`directory, create a file called`outputs.tf`.

Note  
  
Ensure that`outputs.tf`,`provider.tf`, and`availability-domains.tf`are in the same directory.
- To output the name of the first availability domain in the list of`oci_identity_availability_domains`, add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
- Run your scripts with Terraform:

```

```

```

```

```

```

When prompted for confirmation, enter`yes`for your data to be fetched and displayed in the output.

You now have an output with the name of the availability domain to use for your instance.

Example output:
```

```

Congratulations! You have successfully fetched data from your Oracle Cloud Infrastructure account to use for your compute instance.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

When you set up Terraform in the first tutorial,[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm), the output block included the following line:
```

```

Then, the output was similar to the following:
```

```

Now, you want to fetch the name of the first availability domain in the list, to use for the location of your compute instance later:
```

```

- The attributes for[Data Source: oci_identity_availability_domains](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains)are:
- availability_domains , a list with three string attributes:
- compartment_id
- id
- name
Note  
  

- Use square brackets to add an index to a list attribute.
- Use the index 0 for the first item in a list.
- Use a dot after the square brackets followed by an attribute of the list, to specify that attribute.
- Example: First item in the list:

`value = data .oci_identity_availability_domains.ads. availability_domains[0]`
- Example: Name of first item in the list:

`value = data .oci_identity_availability_domains.ads. availability_domains[0].name`

[Declare a Compute Resource](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

Declare an Oracle Cloud Infrastructure compute resource , and then define the specifics for the instance.
Tip  
  
You can save a stack from the Console workflow for creating a compute instance. The stack contains a Terraform configuration that you can use as a reference for the shape and shape configuration. See[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm)and[Getting a Stack's Terraform Configuration](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm).

- Create a file called`compute.tf`.
- Add the following code to`compute.tf`.

```

```

Important  
  

- Replace`<compartment-ocid> , <source-ocid>`,`<your-ubuntu-instance-name>`, and`<subnet-ocid>`with the information you collected at[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#gather-info).
- For availability domain, use the name you fetched with the data source:
```

```

- For`ssh_authorized_keys`, use the following format:
```

```

You can't change its value after you create the VM.
- Save the`compute.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

In Terraform, resources are objects such as virtual cloud networks (VCNs) or compute instances. You can create, update, and delete them with Terraform.

To declare a compute resource:
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`core instance`.

Results include data sources and resources for several services.
- Under Core , go to Resources and select oci_core_instance .

The title of the page is the resource type:`oci_core_instance`
- In the Argument Reference section, use the following required arguments (inputs):
- availability_domain
- compartment_id
- shape
- source_details
- source_id
- source_type
- Construct a resource block:
- Declare a resource block with the keyword:`resource`
- Add a label for resource type:`"oci_core_instance"`
- Add a label for a local name (your choice):
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"ubuntu_instance"`
- Inside the code block, provide a value for required arguments. They don't have a default value.
- For optional arguments, provide values for the ones you want to override. Otherwise, their default values are used.

[Add Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

Add output blocks to your code to get information about your compute instance after Terraform creates it.

- Open the`outputs.tf`file.
- Create an output block for the public IP of the instance:

- The public IP is available after the instance is created.
- Use the public IP to connect to the instance.
- Add the following code to`outputs.tf`:

```

```

- Add a few more outputs to describe the compute instance:

- display_name
- id
- region
- shape
- state
- ocpus
- memory_in_gbs
- time_created

```

```

- Save the`outputs.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- Go to[Attributes Reference (oci_core_instance)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance#attributes-reference).
Note  
  
Attributes are the outputs that you can return for the`oci_core_instance`resource.
- Search for the attribute for public IP:`public_ip`.
- Construct a resource output block for`public_ip`:
- For the value expression, use the following format:
- `value = <type>.<local-name-for-resource>. <attribute>`
- Example:`value = oci_core_instance.ubuntu_instance. public_ip`
- Create an output block for each of the following outputs:
- display_name
- id
- region
- shape
- state
- ocpus
- memory_in_gbs
- time_created

## 3. Run Scripts

Run your Terraform scripts to create the compute instance in a compartment in your tenancy. Use your SSH keys to connect to the instance. When you no longer need your instance, destroy it with Terraform.

[Create an Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- Create your compute instance with Terraform:

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for your resource to be created.
After the instance is created, the outputs that you defined including`<your-public-ip-address>`are displayed in the output terminal.
- (Optional) Watch the instance creation from the Console.

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select your compartment.
- Watch your instance appear in the list of instances.

Congratulations! You have successfully created a compute instance using Terraform, in your Oracle Cloud Infrastructure account.

References:

- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [Data Source: oci_identity_availability_domains](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains)
- [oci_core_instance](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance)

[Connect to the Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- From your terminal, enter the outputs for your compute instance:

```

```

- Copy the public IP address from the outputs.
- From your Linux machine, connect to your VM with this`ssh`command:

```

```

Note  
  
Ensure that your private key is located directly on your Linux (WSL) machine.
- Disconnect from the instance:

```

```

[Destroy the Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#)

- (Optional) After you no longer need your compute instance, you can terminate it with the following command:

```

```

When prompted for confirmation, enter`yes`.
- (Optional) Watch the termination from the Console:

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select your compartment.
- Watch your instance's state change to Terminating and then Terminated .

## What's Next

For the next Terraform tutorial, go to:
- [Set Up a Simple Infrastructure with OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
