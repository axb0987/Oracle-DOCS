# Create Scripts and State Files with Resource Discovery
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm
- Fetched: 2026-09-05 19:21 CDT

# Create Scripts and State Files with Resource Discovery

Generate Terraform files for existing resources in your compartment.

Use the OCI resource discovery feature to:
- Create state files for existing resources in the Console, and then add those resources to a Terraform setup.
- Duplicate your existing infrastructure in a new tenancy or region.
- Detect state drift for updated resources.

In this tutorial, you create scripts and state files for resources in your account through the resource discovery feature. Then you use Terraform to manage the resources.

Key tasks include how to:
- Create a resource through the Console.
- Create scripts and a state file for the resource through the resource discovery feature.
- Update the resource with Terraform.
- Confirm that the resource has been updated in the Console.

For more information, see:
- [Use Cases and Benefits](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#use-cases-and-benefits)
- [Blog: Two Tools to Bring Your Existing Infrastructure Under Terraform](https://blogs.oracle.com/cloud-infrastructure/post/two-tools-to-bring-your-existing-infrastructure-under-terraform)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

- An Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial resources:
- Go through all the steps in[Set Up Resource Discovery](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm).
- Make a note of the OCI Terraform provider command:
- Cloud Shell:`terraform-provider-oci_ <version>`from`/usr/bin`
- Compute instance or a local environment: Use the`<shorter-alias>`that you created in the previous tutorial to use instead of the command,`terraform-provider-oci_ <version>`.
- Example:`tf-oci`
- Terraform v1.1.3+:
- If you're using Cloud Shell, you don't need to install Terraform. Terraform is already installed.
- If you're using a compute instance or a local environment, then follow the steps at[Install Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#install-terraform).

## 1. Create a Resource

Create a bucket in your tenancy through the Console. This bucket doesn't have a Terraform script. Later, use resource discovery to create a Terraform script and a state file for the bucket.

[Add Compartment Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can create a compartment for all the resources in your tutorial.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

- [Sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)to the Oracle Cloud Console.
- In the navigation menu , select the Profile menu and then select User settings .
- Select Groups or My groups , depending on the option that you see.
- In a notepad, copy the name of a group that your username belongs to.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Select the compartment:`<your-tenancy> (root)`
- Select Create Policy .
- On the Create Policy page, enter the following values:
- Name:`manage-compartments`
- Description:`Allow the group <a-group-your-username-belongs-to> to list, create, update, delete and recover compartments in the tenancy.`
- Compartment:`<your-tenancy> (root)`
- For Policy Builder , select Show manual editor .
- Paste in the following policy:

```

```

- Select Create .

Reference:[Details for Verbs + Resource-Type Combinations](https://docs.oracle.com/iaas/Content/Identity/policyreference/iampolicyreference.htm#Identity)(see the`compartments`resource-type)

[Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

Create a compartment for the resources that you create in this tutorial.
- In the Console: open the navigation menu , select Identity &amp; Security . Under Identity , select Compartments .
- Select Create Compartment .
- Enter the following values:
- Name:`<your-compartment-name>`
- Description:`Compartment for <your-description> .`
- Parent Compartment:`<your-tenancy> (root)`
- Select Create Compartment .

Reference:[Creating a Compartment](https://docs.oracle.com/iaas/Content/Identity/compartments/To_create_a_compartment.htm)

[Add Resource Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can manage all resources in your compartment, giving you administrative rights in that compartment.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

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

[Create a Bucket](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

Create a bucket in your compartment.

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Selecct the compartment:`<your-compartment-name>`.
- Select Create Bucket .
- Enter the following values:

- Bucket Name:`<your-bucket-name>`
- Keep the rest of the defaults.
- Select Create .
You have successfully created a private bucket.
Note  
  
Ensure that you create your bucket in`<your-compartment-name>`.

## 2. Discover the Resource

Discover the bucket that you created in your compartment.

[Discover the Bucket](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

- From your`$HOME`directory, delete and re-create the`resource-discovery`directory you created for the tutorial[Set Up Resource Discovery](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm).

```

```

```

```

```

```

- Run the following command:

```

```

Cloud Shell:

```

```

- Replace`<your-compartment-name>`, with the name of your compartment.
Sample output:
```

```

Note  
  
You might get the following message:
```

```

Lacking a lifecycle policy is OK for this tutorial. To plan for the service to automatically archive or delete this bucket, see[Using Object Lifecycle Management](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm).
- Review the generated Terraform scripts.

```

```

```

```

- `object_storage.tf`
- `provider.tf`
- `vars.tf`
- View the`object_storage.tf`script.

```

```

```

```

You have successfully discovered Object Storage resources in your compartment.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

- Go to[Usage (Resource Discovery)](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#usage).

Two command options are listed.
- Select the command option that uses`compartment_name`as a base command:
```

```

- Update the base command:
- Instead of`terraform-provider-oci`, use your symbolic link command:

`tf-oci`
- Review the Parameter Description section to add proper values to the parameters in the base command:
- Use the export command to perform resource discovery:

`-command=export`
- Enter the name of the compartment that you're discovering its resources:

`-compartment_name= <your-compartment-name>`
- Create and then specify a directory for the discovered resources:

Example:`-output_path=$HOME/resource-discovery`
- Add the following parameter from the Parameter Description section to the base command:
- `services`
- From the service names listed for`services`, use:
- `object_storage`
- Example:`-services=object_storage`
- To discover more than one service, separate the service names with a comma.
- Example:`-services=object_storage,core`
- You don't need quotation marks around the service names.
- Construct the command:

Example:
```

```

Note  
  
Troubleshooting
```

```

The resource discovery command doesn't create a directory for the discovered resources. Create a directory and specify the path in your command.
```

```

The parser stops at the parameter that lacks a dash. Ensure that you add a dash to the beginning of each parameter. For example, if you use`services`instead of`-services`, the parser doesn't reach the output directory.

[Generate a State File](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

To track your resources, Terraform stores the state of your resources in a state file. Then, every time you update a resource with Terraform, Terraform updates the state file with that change.

- Run the resource discovery command with the`-generate_state`flag:

- In Cloud Shell:
- 

```

```

- On your compute instance or in your local environment:

```

```

Sample output:
```

```

Note  
  
Troubleshooting:
- Error: Failed to query available provider packages :
- If you are on a VPN, check your proxy settings.
- View the contents of the`resource-discovery`directory.

```

```

Sample output:
- `object_storage.tf`
- `provider.tf`
- `terraform.tfstate`
- `vars.tf`
Note  
  
The resource discovery command overwrites the`<resource> .tf`files every time you run it. If you don't specify a service, it creates a`<resource> .tf`file for every resource in the specified compartment.
- View the generated Terraform state file.

```

```

Sample output:
```

```

Congratulations! You have created a state file for your bucket resource.

References:

- [Resource Discovery](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery)
- [State](https://developer.hashicorp.com/terraform/language/state)

## 3. Update the Resource

Update the name of your bucket in the`object_storage.tf`file and then run your Terraform scripts. Your account authenticates the scripts and then Terraform updates the bucket name. Confirm the new bucket name through the Console.

[Change Bucket Name](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

- In your editor, open the`object_storage.tf`file and change the bucket name from`<your-bucket-name>`to`<your-bucket-name> -2`.

Note  
  
You can only rename empty buckets.
```

```

- Save the`object_storage.tf`file.

[Initialize](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

When you create a state file, resource discovery initializes a working directory that includes Terraform configuration files. Make a habit to run this command every time you update your Terraform scripts.

- Check the contents of the`resource-discovery`directory.

```

```

You have a folder called`.terraform`that includes the plugins for the`oci`provider.
- Confirm that you have Terraform installed.

```

```

- Run the`init`command:

```

```

Example output:
```

```

[Plan](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

An execution plan is the list of changes that Terraform plans to apply to your account.

- Create an execution plan:

```

```

- Review the execution plan.

With the command,`terraform plan`you check whether the changes shown in the execution plan match your expectations, without changing to the real resources. Example output:
```

```

[Apply](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm#)

#### Update the Bucket
- Run your Terraform scripts:

```

```

- When prompted for confirmation, enter`yes`, for the bucket name to be replaced.

Example output:
```

```

#### Find New Bucket Name in Console
- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Select the compartment:`<your-compartment-name>`.
- In the list of buckets, check the bucket name.

The name of the bucket is now`<your-bucket-name> -2`.

## What's Next

Explore other Terraform tutorials:
- [Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- [Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
