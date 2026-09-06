# Create a Virtual Cloud Network
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm
- Fetched: 2026-09-05 19:21 CDT

# Create a Virtual Cloud Network

Use Terraform to create a virtual cloud network (VCN) in your Oracle Cloud Infrastructure tenancy.

Key tasks include how to:
- Set up a basic VCN.
- Define and add the following resources to the network:
- Security lists
- Private and public subnets

For more information, see:
- [Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)

## Before You Begin

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To successfully perform this tutorial, you must have the following:
- A paid Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial resources:
- Go through all the steps in:
- [Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- [Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)
- Keep the scripts you created in the following directories:
- `$HOME/tf-provider/`
- `$HOME/tf-compartment/`
- Keep the compartment from the[Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)tutorial in your tenancy.

## 1. Prepare

Prepare your environment for creating a VCN. Also, collect all the information you need to complete the tutorial.

[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

Copy the following information into your notepad.

For steps to collect this information, see the following table.

Item Steps to collect item
Compartment name Reference the completed tutorial[Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm).
Compartment ID
- In the Console search bar, enter`<your-compartment-name>`.
- Select`<your-compartment-name>`in the search results.
- Select Copy next to the OCID.
Region
- In the Console navigation bar, find your region.

Example: US East (Ashburn)

For more information, see[Working in Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm).
- Look up your region's identifier at[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Example:`us-ashburn-1`.

[Add Resource Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can manage all resources in your compartment, giving you administrative rights in that compartment.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

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

## 2. Create a Basic Network

Create scripts for authentication, a basic virtual cloud network (VCN) defined by a module, and outputs.

[Add Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

First, set up a directory for your Terraform scripts. Then copy the provider and versions scripts from the[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)tutorial so your Oracle Cloud Infrastructure account can authenticate the scripts running from this directory.

- In your`$HOME`directory, create a directory called`tf-vcn`and change to that directory.

```

```

```

```

- Copy the`provider.tf`file into the`tf-vcn`directory.

```

```

- Copy the`versions.tf`file into the`tf-vcn`directory.

```

```

[Declare a Basic Network](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

Declare a basic network with an Oracle Cloud Infrastructure virtual cloud network (VCN) module, documented in the Terraform Registry. Then, run your scripts and create the network. In the next sections, add components to customize your network.
Tip  
  
You can save a stack from the Console workflow for creating a VCN. The stack contains a Terraform configuration that you can use as a reference for the VCN configuration. See[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm)and[Getting a Stack's Terraform Configuration](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm).

- In Terraform Registry, go to the OCI VCN module at[vcn](https://registry.terraform.io/modules/oracle-terraform-modules/vcn/oci/latest).
How to navigate to this page:
- Go to[Terraform Registry](https://registry.terraform.io/browse/providers).
- Select Modules .
- Under Provider list, select`Oracle`.
- Select oracle-terraform-modules/vcn .
- For Version , from the list, select`Version 3.6.0`.
This tutorial uses version 3.6.0. A different version might require different inputs and create different resources for your VCN. To review required and optional inputs, select Inputs .
- Create a file called`vcn-module.tf`.
- Copy the code from Provision Instructions into`vcn-module.tf`.

Example:
```

```

- Update`vcn-module.tf`to specify the compartment (required input) and override a few optional inputs.

```

```

- Replace`<compartment-ocid>`and`<region-identifier>`with the information from[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#gather-info).
- If you want a custom DNS label, uncomment the line for`vcn_dns_label`and change the value from its default`"vcnmodule"`.
Note  
  
The DNS domain name for your virtual cloud network is:
```

```

- Save the`vcn-module.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

##### About Modules

A module is a container for multiple resources that are used together. Instead of declaring infrastructure resources one by one, start with a module provided by Oracle Cloud Infrastructure. For example, start with a basic VCN module. Then, add the resources that aren't included in the module to your scripts.

##### Declare a Module Block
- Start the block with the keyword:`module`
- Add a label for the module's provided name:
- Example:`"vcn"`
- Inside the code block:
- Add`source`and`version`information from the Provision Instructions section of the module documentation.
- Provide a value for the required inputs. They don't have a default value. Example:
```

```

- Provide values for the optional inputs that you want to override. Otherwise, their default values are used. Example:
```

```

- You can comment out the optional inputs and show their default value, so later when you review your code, you know what values were expected. Example:
```

```

[Add Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

Add output blocks to your code to get information about your virtual cloud network after you run your scripts.

- In the`tf-vcn`directory, create a file called`outputs.tf`.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
- List all files in the`tf-vcn`directory.

```

```

Ensure that the following files are present in the same directory:
- `outputs.tf`
- `provider.tf`
- `vcn-module.tf`
- `versions.tf`

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

##### About Module Outputs

Module outputs are the attributes that you can return for that module.

##### Find Outputs for VCN Module

Go to the[vcn](https://registry.terraform.io/modules/oracle-terraform-modules/vcn/oci/latest)page and select[Outputs to view a list of attributes that can be output for the VCN module. Review the description of the attributes:
- ig_route_id
- OCID of the route table that includes the internet gateway
- nat_gateway_id
- OCID of the NAT gateway
- nat_route_id
- OCID of the route table that includes the NAT gateway
- vcn_id
- OCID of the VCN

##### Declare a Module Output Block
- 
- Start the block with the keyword:`output`.
- Add a label to be printed with the output results:
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"vcn_id"`
- Get the attributes from the outputs for the module at[Oracle Terraform Modules](https://registry.terraform.io/namespaces/oracle-terraform-modules).
- Inside the code block, enter a value for the module output with the expression:
- `value = module .<module-name>. <output-attribute>`
- Example:`value = module.vcn.vcn_id`
- (Optional): Inside the code block, add a description string. Example:
```

```

Note  
  
A description string isn't printed in the output, so ensure that the label describes what it outputs.
- Create an output block for each output.

[Create the Basic Network](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

- Create your basic network with Terraform:

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.
After the virtual network is created, the outputs that you defined are displayed in the output terminal.
- (Optional) Watch the creation from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your compartment.
- Watch your virtual cloud network appear in the list of networks.

Congratulations! You have successfully created a basic virtual network using Terraform, in your Oracle Cloud Infrastructure account. You have a virtual network and you can be done at this point. The next sections show you how to customize a network created from a module.

## 3. Customize the Network

Create scripts for security lists, private subnets, and public subnets to create the same virtual network as in the Console creation workflow.

[Create a Security List for the Private Subnet](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

[Declare a Security List](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

- Create a file called`private-security-list.tf`.
- Add the following code to`private-security-list.tf`.

```

```

- Replace`<compartment-ocid>`, with the information from[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#gather-info).
- Point`vcn_id`to the VCN OCID you created with the module:
```

```

- Save the`private-security-list.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

At[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference), find all required arguments (first-level bullets):
- compartment_id
- vcn_id

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To navigate to[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`security list`.

Results are returned for both data sources and resources.
- Under Core , go to Resources and select oci_core_security_list .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference)opens.

Declare the security list:
- For compartment_id : use
```

```

- For vcn_id , use the OCID of the basic virtual network. To assign the OCID before knowing it, assign an output from the module as input for the security list resource:
- Get the module's output attribute from the module's Outputs page.
- Assign a value to the resource argument with the expression:
- `<resource argument> = module .<module-name>. <output-attribute>`
- Example:`vcn_id = module.vcn.vcn_id`
- Both`oci_core_security_list resource`and`oracle-terraform-modules/vcn`use the same argument name for the virtual cloud network OCID:`vcn_id`.
- The leftmost`vcn_id`is the argument (required input) for the resource.
- The rightmost`vcn_id`is the OCID of the VCN that you create with the module.
- It doesn't matter if you have run the VCN module script and created the VCN or not. Either way, Terraform assigns the VCN OCID to the security list after the VCN module is created.

[Add an Egress Rule](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

Add an egress rule to your security list based on the following values:
- Stateless: No
- Destination: 0.0.0.0/0
- IP Protocol: All Protocols
Note  
  
The Allows field in the table is automatically generated based on other fields. You don't add an argument for it in your script.

- Add the following code to`private-security-list.tf`:

```

```

- Save the`private-security-list.tf`file.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
- List all files in the`tf-vcn`directory.

```

```

Ensure that the following files are present in the same directory:
- `outputs.tf`
- `private-security-list.tf`
- `provider.tf`
- `vcn-module.tf`
- `versions.tf`

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

For`private-security-list.tf`, go to[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference)and find the following arguments:
- egress_security_rules
- stateless
- destination
- destination_type
- protocol

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To navigate to[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`security list`.

Results are returned for both data sources and resources.
- Under Core , go to Resources and select oci_core_security_list .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference)opens.
Note  
  

Use the equals sign (`=`) to assign a value to an argument inside the block only.
- Write:
```

```

- Don't write:
```

```

For attributes for use as outputs in`outputs.tf`, select Attribute Reference to open[Attributes Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#attributes-reference)and find the following attributes:
- display_name
- id

[Create the Security List](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

- Create the security list for the private subnet, with Terraform:

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.
After the security list is created, the outputs that you defined are displayed in the output terminal.
- (Optional) Watch the network creation from the Console.

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your VCN.
- On the details page, select Security or Security Lists , depending on the option that you see.
- Select the security list that was created for a private subnet ( security-list-for-private-subnet ).
- Select Security rules or Egress Rules , depending on the option that you see.

Congratulations! You have successfully created a security list with an egress rule in your virtual cloud network. In the next section, you add ingress rules to this security list.

[Create Ingress Rules for the Private Subnet](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

In this section, you add the following ingress rules to the security list you created in the previous section.

Ingress Rules
- Rule 1:
- Stateless: No
- Source: 10.0.0.0/16
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 22
- Rule 2:
- Stateless: No
- Source: 0.0.0.0/0
- IP Protocol: ICMP
- Type and Code: 3, 4
- Rule 3:
- Stateless: No
- Source: 10.0.0.0/16
- IP Protocol: ICMP
- Type and Code: 3
Note  
  
The Allows field in the table is automatically generated based on other fields. You don't add an argument for it in your script.

- Add the following code to`private-security-list.tf`:

```

```

- Save the`private-security-list.tf`file.
- Run your scripts.

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.
- (Optional) Watch the creation from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your VCN.
- On the details page, select Security or Security Lists , depending on the option that you see.
- Select the security list that was created for a private subnet ( security-list-for-private-subnet ).
- Select Security rules or Ingress Rules , depending on the option that you see.

Congratulations! You have successfully added three ingress rules to your security list. You use this security list for a private subnet. You create another security list for a public subnet in the next section.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

At[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference), find the following arguments:
- ingress_security_rules
- stateless
- source
- source_type
- protocol
- icmp_options
- type
- code
- tcp_options
- min
- max

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To navigate to[Argument Reference (oci_core_security_list)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`security list`.

Results are returned for both data sources and resources.
- Under Core , go to Resources and select oci_core_security_list .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list#argument-reference)opens.
- For protocol , see[Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml):
- TCP: 6
- ICMP: 1
- For icmp_options , see[Internet Control Message Protocol (ICMP) Parameters](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml).
- For tcp_options , if you have no port range, such as Destination Range: 22 , set the maximum and minimum value to the same number. Example:
- min = 22
- max = 22

[Create a Security List for the Public Subnet](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

In this section, you create a security list in your network with egress and ingress rules. Later, you assign this security list to a public subnet.

- In the`tf-vcn`directory, copy the`private-security-list.tf`file and call it`public-security-list.tf`.

```

```

- Open the`public-security-list.tf`file and update the following:

- resource block local name: from`"private-security-list"`to`"public-security-list"`
- security list name:`display_name = "security-list-for-public-subnet"`

```

```

- Use the same egress rule as the private one.

Egress Rule
- Stateless: No
- Destination: 0.0.0.0/0
- IP Protocol: All Protocols

```

```

- Update the TCP rule for the first ingress rule as follows:

- from`source = "10.0.0.0/16"`to`source = "0.0.0.0/0"`

Ingress Rules
- Rule 1:
- Stateless: No
- Source: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 22
- Rule 2:
- Stateless: No
- Source: 0.0.0.0/0
- IP Protocol: ICMP
- Type and Code: 3, 4
- Rule 3:
- Stateless: No
- Source: 10.0.0.0/16
- IP Protocol: ICMP
- Type and Code: 3

```

```

- Save the`public-security-list.tf`file.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
- List all files in the`tf-vcn`directory.

```

```

Ensure that the following files are present in the same directory:
- `outputs.tf`
- `private-security-list.tf`
- `provider.tf`
- `public-security-list.tf`
- `vcn-module.tf`
- `versions.tf`
- Run your scripts.

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for the security list to be created.
- (Optional) Watch the creation from the Console.

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your VCN.
- On the details page, select Security or Security Lists , depending on the option that you see.
- Select the security list that was created for a public subnet ( security-list-for-public-subnet ).
- Select Security rules or Ingress Rules , depending on the option that you see.
- Select Security rules or Egress Rules , depending on the option that you see.

Congratulations! You have successfully created another security list in your virtual cloud network.

[Create a Private Subnet](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

In this section, you create a private subnet in your network and associate the private security list to this subnet. You also add the NAT route table that you made with the VCN module to this subnet. The NAT route table has one NAT gateway and one service gateway and is designed for private subnets. See the first diagram in the tutorial.

- In the`tf-vcn`directory, create a file called`private-subnet.tf`and add the following code to it:

```

```

- Replace &lt;compartment-ocid&gt; with the information collected at[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#gather-info).
- Save the`private-subnet.tf`file.

Note  
  
Ensure that`private-subnet.tf`is in the`tf-vcn`directory.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
Ensure that all the`*.tf`files are in the same directory. Terraform processes all the files in a directory in the correct order, based on their relationship.
- Run your scripts.

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for the private subnet to be created.
- (Optional) Watch the creation from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your VCN.
- On the details page, select Subnets .
- Select the private subnet ( private-subnet ).
- On the details page, find the route table: nat-route .
- Select Security or Security Lists (depending on what you see) and find the security list ( security-list-for-private-subnet ).

Congratulations! You have successfully created a private subnet in your virtual cloud network.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

At[Argument Reference (oci_core_subnet)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference), find all required arguments:
- compartment_id
- vcn_id
- cidr_block

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To navigate to[Argument Reference (oci_core_subnet)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`subnet`.

Results are returned for both data sources and resources.
- Under Core , go to Resources and select oci_core_subnet .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference)opens.
- Override the following optional arguments:
- route_table_id
- security_list_ids
- display_name
- Assign values to the following arguments:
- cidr_block
- See the first diagram in the tutorial.
- route_table_id
- The OCID of a route table.
- To see the gateways for this route table, reference the private subnet in the first diagram in the tutorial:
- NAT Gateway
- Service Gateway
- Assign the route table with the NAT gateway that you created with the VCN module. This route table also contains a service gateway.
Note  
  

- Use`module.vcn.nat_route_id`.
- Don't use`module.vcn.nat_gateway_id`, because it returns the OCID of the gateway and not the route table.
- (Optional): In the Console, review the rules of the route table and compare the Target Type values with the tutorial diagram (Service Gateway, NAT Gateway).
- On the details page for your VCN, select Routing or Route Tables (depending on what you see).
- Select nat-route .
- Select Route Rules .
- security_list_ids
- Returns a list of strings, each an OCID of a security list.
- Get the OCID of the private security list.
- Use square brackets for this argument. Example:
```

```

- To assign one security list, place it inside the square brackets without any commas.
- To reference the security list created with another resource, use its local name. Example:
```

```

[Create a Public Subnet](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

In this section, you create a public subnet in your network and associate the public security list to this subnet. You also add the internet route table that you made with the VCN module to this subnet. The internet route table has an internet gateway and is designed for public subnets. See the first diagram in the tutorial.

- In the`tf-vcn`directory, create a file called`public-subnet.tf`and add the following code to it:

```

```

- Replace &lt;compartment-ocid&gt; , with the information collected at[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#gather-info).
- Save the`public-subnet.tf`file.

Note  
  
Ensure that`public-subnet.tf`is in the`tf-vcn`directory.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
Ensure that all the`*.tf`files are in the same directory. Terraform processes all the files in a directory in the correct order, based on their relationship.
- Run your scripts.

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for the public subnet to be created.
- (Optional) Watch the creation from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your VCN.
- On the details page, select Subnets .
- Select the public subnet ( public-subnet ).
- On the details page, find the route table: internet-route .
- Select Security or Security Lists (depending on what you see) and find the security list ( security-list-for-public-subnet ).

Congratulations! You have successfully created a public subnet in your virtual cloud network.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

At[Argument Reference (oci_core_subnet)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference), find all required arguments:
- compartment_id
- vcn_id
- cidr_block

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

To navigate to[Argument Reference (oci_core_subnet)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`subnet`.

Results are returned for both data sources and resources.
- Under Core , go to Resources and select oci_core_subnet .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet#argument-reference)opens.
- Override the following optional arguments:
- route_table_id
- security_list_ids
- display_name
- Assign values to the following arguments:
- cidr_block
- See the first diagram in the tutorial.
- route_table_id
- The OCID of a route table.
- To see the gateway for this route table, reference the public subnet in the first diagram in the tutorial:
- Internet Gateway
- Assign the route table with an internet gateway that you created with the VCN module.
Note  
  

- Use module.vcn.ig_route_id .
- (Optional): In the Console, review the rules of the route table and compare the Target Type value with the tutorial diagram (Internet Gateway).
- On the details page for your VCN, select Routing or Route Tables (depending on what you see).
- Select internet-route .
- Select Route Rules .
- security_list_ids
- Returns a list of strings, each an OCID of a security list.
- Get the OCID of the public security list.
- Use square brackets for this argument. Example:
```

```

- To assign one security list, place it inside the square brackets without any commas.
- To reference the security list created with another resource, use its local name. Example:
```

```

## 4. Re-create the VCN (Optional)

Destroy your VCN. Then rerun your scripts to create another VCN.

[Run the Scripts](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm#)

In the previous sections, to check your work, you ran your scripts every time you declared a resource. Now, you run them together. You observe that the scripts are declarative and Terraform resolves the order in which it creates the objects.

- Destroy your VCN with Terraform:

```

```

When prompted for confirmation, enter`yes`, for your resource to be destroyed.
- (Optional) Watch the termination from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your compartment.
- Watch your VCN disappear from the list.
- Make a new virtual cloud network with Terraform:

```

```

```

```

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.

After the network is created, the outputs that you defined are displayed in the output terminal.
Note  
  
This new virtual cloud network has new OCIDs for its resources. This network isn't the same one that you destroyed.
- (Optional) Watch the creation from the Console:

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your compartment.
- Watch your re-created (new) virtual cloud network appear in the list of networks.
- Display the outputs again.

```

```

Congratulations! You have successfully re-created a virtual cloud network and its components using Terraform, in your Oracle Cloud Infrastructure account.
Note  
  
This virtual cloud network has the same components as a virtual cloud network that's created using Start VCN Wizard in the Console, with the VCN with Internet Connectivity option. You can follow the tutorial steps to[set up a network](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm#create-vcn)and then compare it with this network.

References:

- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [vcn](https://registry.terraform.io/modules/oracle-terraform-modules/vcn/oci/latest)
- [oci_core_security_list](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_security_list)
- [oci_core_subnet](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_subnet)

## What's Next

For the next Terraform tutorial, go to:
- [Set Up a Simple Infrastructure with OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
