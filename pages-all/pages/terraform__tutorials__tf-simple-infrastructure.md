# Set Up a Simple Infrastructure with OCI Terraform
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm
- Fetched: 2026-09-05 19:21 CDT

# Set Up a Simple Infrastructure with OCI Terraform

Use Terraform to set up a simple infrastructure in your Oracle Cloud Infrastructure account.

Key tasks include how to:
- Copy existing scripts from other Terraform tutorials.
- Edit the scripts to combine all the resources in one directory.
- Run an`apply`command to create the following resources:
- a compartment
- a virtual cloud network
- a compute instance

For more information, see:
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [Introduction to HashiCorp Terraform Video](https://www.youtube.com/watch?v=h970ZBgKINg)
- [Terraform Registry](https://registry.terraform.io/browse/providers)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- A paid Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial resources:
- Go through all the steps in:
- [Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- [Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)
- [Create a Compute Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm)
- [Create a Virtual Cloud Network](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-vcn.htm)
- Keep the scripts you created in the following directories:
- `$HOME/tf-provider/`
- `$HOME/tf-compartment/`
- `$HOME/tf-compute/`
- `$HOME/tf-vcn/`

## 1. Prepare

Copy the scripts you created in previous Terraform tutorials into a new directory.

[Copy Declared Resources](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- In your`$HOME`directory, create a directory called`tf-simple-infrastructure`and change to that directory.

```

```

```

```

- Copy the Terraform scripts from the`tf-provider`directory.

```

```

Note  
  
Don't copy the state files (`terraform.tfstate`or`terraform.tfstate.backup`). These files contain the state of resources for their current directory. After you run the scripts in this new directory, you get a new state file.
- Rename the`outputs.tf`file to`outputs1.tf`.

```

```

- Copy the Terraform scripts from the`tf-compartment`directory.

```

```

Note  
  
Because you only need one provider file per directory, no harm is done when the copy command replaces one`provider.tf`file with another.
- Rename the`outputs.tf`file to`outputs2.tf`.

```

```

- Copy the Terraform scripts from the`tf-compute`directory.

```

```

- Rename the`outputs.tf`file to`outputs3.tf`.

```

```

- Copy the Terraform scripts from the`tf-vcn`directory.

```

```

- Rename the`outputs.tf`file to`outputs4.tf`.

```

```

- Concatenate the four output files.

```

```

- Remove the`outputs1.tf`,`outputs2.tf`,`outputs3.tf`, and`outputs4.tf`files from the`tf-simple-infrastructure`directory.

```

```

- Confirm that you have the following files in your directory.

```

```

```

```

## 2. Edit the Scripts

Edit the scripts to assign a new name for your compartment and to replace all hard-coded OCIDs with references.

[Update the Compartment Name](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- Open the`compartment.tf`file.
- Update`<your-compartment-name>`with`<your-new-compartment-name>`, in case you already created &lt;your-compartment-name&gt; in the previous tutorials.

```

```

[Update Compartment References](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

[Find the Reference to Compartment OCID](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

In the previous tutorials, you hard-coded the compartment OCID. Now, update`<compartment-ocid>`to reference the compartment from`compartment.tf`.
- Find how the compartment OCID is referenced in the`outputs.tf`file.

```

```

Example output:
```

```

- Copy the value for the compartment OCID into your notepad:

```

```

[Update Hard-Coded Compartment OCIDs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- Find which files reference`compartment_id`.

```

```

Example output:
```

```

Note  
  
The`availability-domains.tf`and`compartment.tf`files both point to the`<tenancy-ocid>`. For example, the`compartment.tf`file points to the tenancy as its parent compartment and then creates a compartment underneath it. Don't edit the`compartment_id`in these two files.
- Except for`availability-domains.tf`and`compartment.tf`files, in the remaining files that result from your`grep`command, replace`compartment_id = "<compartment-ocid>"`with:

```

```

[Update Subnet References](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

[Find the Reference to Subnet OCID](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

In the tutorial[Create a Compute Instance](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compute.htm), you hard-coded the public subnet that hosts the compute instance. Now, update the`compute.tf`file to reference the`public-subnet-OCID`from the`public-subnet.tf`file.
- Find how`subnet OCID`is referenced in the`outputs.tf`file.

```

```

Example output:
```

```

- Copy the value for the public subnet OCID into your notepad:

```

```

[Update Hard-Coded Subnet OCIDs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- Find which files reference`subnet_id`.

```

```

Example output:
```

```

- In the`compute.tf`file that results from your`grep`command, replace`compartment_id = "<your-public-subnet-ocid>"`with:

```

```

Congratulations! All your scripts are now ready to run.

## 3. Create a Simple Infrastructure

Run your Terraform scripts to create a compartment, a virtual cloud network, and a compute instance in the public subnet.

[Run the Scripts](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- Initialize a working directory in the`tf-simple-infrastructure`directory.

```

```

- Create an execution plan and review the changes that Terraform plans to make to your account:

```

```

Example output:
```

```

- Create your simple infrastructure with Terraform:

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.

[Watch the Creation in the Console (Optional)](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

- open the navigation menu , select Identity &amp; Security . Under Identity , select Compartments .
- Refresh the page, until you see the compartment name.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Select your compartment.

If you can't find your compartment, then refresh the page.
- Select your VCN and then review created resources.
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Watch your instance appear in the list of instances.

[Review the Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm#)

Review the outputs in the output terminal.
Example of output displayed in terminal:
```

```

References:

- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [Basic CLI Features](https://developer.hashicorp.com/terraform/cli/commands)

## What's Next

Congratulations! You have successfully created a simple infrastructure using Terraform, in your Oracle Cloud Infrastructure account.

Now that you know how to use data sources, resources and modules, go ahead and add new objects from[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)to your simple infrastructure.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
