# Create a Compartment
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm
- Fetched: 2026-09-05 19:21 CDT

# Create a Compartment

Use Terraform to connect to your Oracle Cloud Infrastructure account and create a compartment in your tenancy.

Key tasks include how to:
- Use Oracle Cloud Infrastructure Terraform provider resources to:
- Declare a compartment with your specifics.
- Create the compartment in your tenancy.

For more information, see:
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [Terraform Registry](https://registry.terraform.io/browse/providers)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

- An Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial scripts:
- Go through all the steps in[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- Keep the scripts you created in the following directory:
- `$HOME/tf-provider/`

## 1. Prepare

Prepare your environment for authenticating and running your Terraform scripts. Also, collect all the information you need to complete the tutorial.

[Get Tenancy Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

Collect the following information from the Oracle Cloud Console and copy it into your notepad .
- Tenancy OCID:`<tenancy-ocid>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- Next to OCID , select Copy .

The tenancy OCID is copied to your clipboard.

[Add Compartment Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can create a compartment for all the resources in your tutorial.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

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

## 2. Create Scripts

Create scripts for authentication, to create a compartment, and to print outputs.

[Add Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

First, set up a directory for your Terraform scripts. Then copy the provider and versions scripts from the[Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)tutorial so your Oracle Cloud Infrastructure account can authenticate the scripts running from this directory.

- In your`$HOME`directory, create a directory called`tf-compartment`and change to that directory.

```

```

```

```

- Copy the`provider.tf`file into the`tf-compartment`directory.

```

```

- Copy the`versions.tf`file into the`tf-compartment`directory.

```

```

[Declare a Compartment Resource](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

Declare an Oracle Cloud Infrastructure compartment resource and then define the specifics for the compartment.

- Create a file called`compartment.tf`.
- Add the following code to`compartment.tf`.

- Replace`<tenancy-ocid>`, with the information you gathered at[Get Tenancy Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#gather-info).

The`compartment_id`is the OCID for the parent compartment. Use the root compartment as the parent. The tenancy OCID is the compartment OCID for the root compartment.
- Replace`<your-compartment-name>`with a name of your choice.

```

```

- Save the`compartment.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

In Terraform, resources are objects such as virtual cloud networks or compute instances. You can create, update, and delete them with Terraform.

To declare a compartment resource:
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`compartment`.

Results are returned for both data sources and resources.
- Under Identity , go to Resources and select`oci_identity_compartment`.

The title of the page is the resource type:`oci_identity_compartment`

Required arguments are listed under Argument Reference :
- `compartment_id`
- `description`
- `name`
- Construct a resource block:
- Declare a resource block with the keyword:`resource`
- Add a label for resource type:`"oci_identity_compartment"`
- Add a label for a local name of your choice:
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"tf-compartment"`
- Inside the code block, provide a value for the required arguments. They don't have default values.
- For optional arguments, provide values for the ones you want to override. Otherwise, their default values are used.

[Add Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

Add output blocks to your code to get information about your compartment after Terraform creates the compartment.

- In the`tf-compartment`directory, create a file called`outputs.tf`.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.
- List all files in the`tf-compartment`directory.

```

```

Ensure that the following files are present in the same directory:
- `compartment.tf`
- `outputs.tf`
- `provider.tf`
- `versions.tf`

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

- Go to[Attributes Reference (oci_identity_compartment)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/identity_compartment#attributes-reference).
Note  
  
Attributes are the outputs that you can return for the`oci_identity_compartment`resource.
- Decide which attributes to output.
- Construct a resource output block:
- Declare an output block with the keyword:`output`
- Add a label to be printed with the output results:
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"compartment-name"`
- Inside the code block, enter a value for the resource output with the expression:
- `value = <type>.<local-name-for-resource>. <attribute>`
- Example:`value = oci_identity_compartment.tf-compartment. id`
- Create an output block for each output.

## 3. Create a Compartment

Run your Terraform scripts. After your account authenticates the scripts, Terraform creates a compartment in your tenancy.

[Initialize](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

Initialize a working directory in the`tf-compartment`directory.

```

```

Example output:
```

```

[Plan](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

Create an execution plan to check whether the changes shown in the execution plan match your expectations, without changing the real resources.

```

```

The expected output includes the line`Plan: 1 to add, 0 to change, 0 to destroy.`

Example output:
```

```

[Apply](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm#)

- Create your compartment with Terraform:

```

```

When prompted for confirmation, enter`yes`, for your resource to be created.
- (Optional) Watch the creation from the Console:

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments .
- Refresh the page until you see the compartment name.
- Select the compartment name to see its details, such as its OCID.
- In the output terminal, review your defined outputs.

Example output:
```

```

Congratulations! You have successfully signed in and created a compartment in your tenancy, using the Oracle Cloud Infrastructure Terraform provider.

References:
- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [oci_identity_compartment](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/identity_compartment)
- [Basic CLI Features](https://developer.hashicorp.com/terraform/cli/commands)

## What's Next

For the next Terraform: Get Started tutorial, go to:
- [Create a Compute Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
