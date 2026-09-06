# Set Up Resource Discovery
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm
- Fetched: 2026-09-05 19:21 CDT

# Set Up Resource Discovery

Set up resource discovery to generate Terraform files for existing resources in your compartment.

Use the OCI resource discovery feature to:
- Create state files for existing resources in the Console, and then add those resources to a Terraform setup.
- Duplicate your existing infrastructure in a new tenancy or region.
- Detect state drift for updated resources.

In this tutorial, you set up Oracle Cloud Infrastructure Terraform provider's resource discovery feature in your local environment. To confirm your setup, you run resource discovery to fetch information from your tenancy and create a script for it.

Key tasks include how to:
- Create RSA keys.
- Install Terraform OCI provider binaries.
- Set up Terraform OCI provider API authentication variables.
- Authenticate your OCI provider CLI commands.
- Create a script in your environment, regarding the availability domains in your tenancy, through the resource discovery feature.

For more information, see[Use Cases and Benefits](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#use-cases-and-benefits).

## Before You Begin

To successfully perform this tutorial, you must have the following:
- An Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows environment:

[MacOS or Linux](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- MacOS
- Linux (Any distribution)
- You can install a Linux VM with an Always Free Compute shape, on Oracle Cloud Infrastructure. See[Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/Content/developer/apache-on-oracle-linux/01-summary.htm).
- Oracle Cloud Infrastructure Cloud Shell:
- [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm)
Note  
  
If you're using Oracle Cloud Infrastructure Cloud Shell, the OCI Terraform Provider is already installed and you don't need to[create RSA keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#create-rsa-keys). Skip that section and proceed to[Add List Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#add-list-policy).

[Windows 10](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)(WSL)
- [Git for Windows](https://gitforwindows.org/)to access a Linux VM.

## 1. Prepare

Prepare your environment for authenticating and running resource discovery commands. Also, gather the information your account needs to authenticate your commands.

[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

You create RSA keys for API signing in to your Oracle Cloud Infrastructure account.
Note  
  
If you're using Cloud Shell or Resource Manager, skip creating the RSA keys. You're already authenticated when you sign in to the OCI Console.

- Open a terminal window.
- Under your home directory, make an`.oci`directory.

```

```

Example for Oracle Linux:

```

```

Note  
  
If you're using Windows Subsystem for Linux (WSL), create the`/.oci`directory directly in the Linux environment. If you create the`/.oci`directory in a`/mnt`folder (Windows file system), you're required to use the`chmod`command to change permissions for the WSL configuration files.
- Generate a 2048-bit private key in a PEM format:

```

```

- Change permissions, so only you can read and write to the private key file:

```

```

- Generate the public key:

```

```

- Copy the public key.
In the terminal, enter:

```

```

Example (excerpt):
```

```

- Add the public key to your user account.

- [Sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)to the Oracle Cloud Console.
- In the navigation menu , select the Profile menu and then select User settings .
- Select API keys .
- Select Add API key .
- Select Paste a public key .
- Paste the value from the previous step, including the lines with`BEGIN PUBLIC KEY`and`END PUBLIC KEY`.
- Select Add .

The Configuration file preview dialog box opens. Example:
```

```

- Select Copy , then paste into your notepad.

The configuration file preview includes information you'll need later, such as tenancy and user OCIDs, fingerprint, and region.

You have now set up the RSA keys to connect to your OCI account. Reference[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two)

[Add List Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can list all the resources in your tenancy.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- [Sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)to the Oracle Cloud Console.
- In the navigation menu , select the Profile menu and then select User settings .
- Select Groups or My groups , depending on the option that you see.
- In a notepad, copy the name of a group that your username belongs to.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .
- Select the compartment:`<your-tenancy> (root)`
- Select Create Policy .
- On the Create Policy page, enter the following values:
- Name:`list-resources`
- Description:`Allow the group <a-group-that-your-username-belongs-to> to list the resources in this tenancy.`
- Compartment:`<your-tenancy>(root)`
- For Policy Builder , select Show manual editor .
- Paste in the following policy:

```

```

- Select Create .

Reference:[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)

[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

Prepare the information you need to authenticate your Terraform OCI Provider commands and copy them into your notepad.
Note  
  
If you're using Cloud Shell, you only need to find the`<tenancy-ocid>`from the following step.

- Collect the following credential information from the Oracle Cloud Console.

- Tenancy OCID:`<tenancy-ocid>`
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- User OCID:`<user-ocid>`
- In the navigation menu , select the Profile menu and then select User settings .
- Copy OCID.
- Fingerprint:`<fingerprint>`
- In the navigation menu , select the Profile menu and then select User settings .
- Select API Keys .
- Copy the fingerprint associated with the RSA public key you made in the Create RSA Keys section. The format is:`xx:xx:xx...xx`.
- Region:`<region-identifier>`
- In the Console navigation bar, find your region.
- Find your region's`<region-identifier>`from[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example:`us-ashburn-1`.
- Collect the following information from your environment.

- Private Key Path:`<rsa-private-key-path>`
- Path to the RSA private key you made at[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#create-rsa-keys). Example:`$HOME/.oci/<your-rsa-key-name>.pem`.

[Install Terraform OCI Provider](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

Note  
  
If you're using Cloud Shell, skip this section.

Install the latest version of Terraform OCI Provider binaries v4.2+ :

- From a browser, go to[HashiCorp Releases](https://releases.hashicorp.com/terraform-provider-oci/).
- Select the latest link.
- Find the link for your environment and then copy the link address. Example for Linux 64 bit:

```

```

- In your environment, create a temp directory and change to that directory:

```

```

```

```

- Download the Terraform zip file. Example:

```

```

- Unzip the file. Example:

```

```

- Move the unzipped folder to`/usr/local/bin`. Example:

```

```

Note  
  
Use`sudo`for the`/usr/local/bin`directory if it doesn't let you run the commands.
- Use a symbolic link to shorten the`terraform-provider-oci_<version>`command:

```

```

```

```

```

```

For this tutorial, use`tf-oci`for the`<shorter-alias>`, instead of the`<source-executable>`.
- Go back to your home directory:

```

```

- Check the Terraform OCI provider version:

Note  
  
On MacOS, you need to create a security exception for the executable.

```

```

Example output:`[INFO] terraform-provider-oci 4.59.0`.

## 2. Create an Authentication Script

Create a shell script to assign authentication information to OCI provider authentication variables. Your Oracle Cloud Infrastructure account authenticates your OCI provider commands through the values assigned to these parameters.

[Add Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

Note  
  
If you're using Cloud Shell or Resource Manager, you don't need to add authentication. Proceed to section[3. Discover a Resource](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#discover-resource).

- Create an executable script file, somewhere in your PATH, and name it`provider-oci.sh`. For example, if`~/bin`is in your PATH, the steps are as follows:

```

```

```

```

```

```

```

```

You get something like this:
```

```

- Add the following code to`provider-oci.sh`.

Replace the fields with brackets with the information you collected at[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#gather-info).

```

```

- Save the`provider-oci.sh`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- Go to[Authentication (Resource Discovery)](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#authentication).
- Set up the following environment variables for API Key based authentication:
- TF_VAR_tenancy_ocid
- TF_VAR_user_ocid
- TF_VAR_fingerprint
- TF_VAR_private_key_path
- TF_VAR_region

[Export Environment Variables](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

In this section, you run the`provider-oci.sh`file to add the OCI provider authentication variables to your environment variables.

- From your`$HOME/bin`directory, run the`provider-oci.sh`file.

```

```

- Confirm that the OCI provider authentication variables are added to your environment variables.

```

```

The variables are displayed in alphabetical order. Example:
```

```

- To load the environment variables, when a new shell starts, append the`source ~/bin/provider-oci.sh`command to`.bashrc`.

```

```

## 3. Discover a Resource

Discover the availability domains in your tenancy.

[Run Resource Discovery](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

Every tenancy has a list of availability domains. By discovering the availability domains in your region, you confirm that:
- Your Oracle Cloud Infrastructure account can authenticate your Oracle Cloud Infrastructure provider commands.
- You can get information from your account with the resource discovery feature.
- In your`$HOME`directory, create a directory called`resource-discovery`.

```

```

```

```

- If you're using Cloud Shell, find the installed OCI Terraform Provider file in the`/usr/bin`directory.

```

```

The file name is:
```

```

Sample file name:
```

```

- Run the following command:
- In Cloud Shell:

```

```

- On your compute instance or in your local environment:

```

```

Important  
  

- Replace`<tenancy-ocid>`with the information from[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#gather-info).
- If you're using Cloud Shell, replace`terraform-provider-oci_ <version>`with the file name that you found in step 2.

Sample output:
```

```

Note  
  

- The tenancy OCID is the compartment OCID for the root compartment. Providing a specific`<compartment-ocid>`or your`<tenancy-ocid>`outputs the same availability domains.
- To discover identity resources, you don't need to mention a compartment OCID. In the previous example, you get the same result if you remove the`compartment_id`from the command. The`compartment_id`is there for you to learn the syntax for other services.

[Troubleshooting](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- error message: Failed to query available provider packages :
- If you're on a VPN, check your proxy settings.
- 401 errors - (Service error:NotAuthenticated):
- You have an incorrect value for one of the following:
- tenancy OCID
- user OCID
- fingerprint
- RSA private key (the path or the key)
- no such host:
- You have an incorrect value for the following:
- region identifier

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- Go to[Usage (Resource Discovery)](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#usage).

Two command options are listed.
- Select the command option that uses`compartment_id`as a base command:
```

```

- Update the base command:
- Instead of`terraform-provider-oci`, use your symbolic link command:

`tf-oci`
- Review the Parameter Description section to add proper values to the parameters in the base command:
- Use the`export`command to perform resource discovery:

`-command=export`
- Add the OCID of the compartment that you're discovering resources in:

`-compartment_id=<tenancy-ocid>`
- Create and then specify a directory for the discovered resources:

Example:`-output_path=$HOME/resource-discovery`
- Search for the phrase`availability_domain`and observe the following information:
```

```

- For services, use:
- `availability_domain`(Even though it's not a service, it works with service.)
- Example:`-services=availability_domain`
- You don't need quotation marks around the service names.
- Construct the command:

Example:
```

```

Note  
  
The resource discovery command doesn't create a directory for the discovered resources. Create a directory and specify the path in your command.

[Review Discovered Resources](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm#)

- From your`$HOME`directory, change to the`resource-discovery`directory.

```

```

- View the contents of the directory.

```

```

Sample output:
```

```

- Review the Terraform script for availability domains:

```

```

Sample output:
```

```

Note  
  
The`availability_domain.tf`Terraform script uses a variable called`compartment_ocid`. Find the value of this variable, in`vars.tf`.
- Review the variables:

```

```

Sample output:
```

```

- Review the provider script information:

```

```

Sample output:
```

```

Note  
  

- The`provider.tf`denotes that you are using the Terraform OCI provider with`provider oci { }`.
- The`provider.tf`file does not include your authentication information, because you provide authentication information through your environment variables.

Congratulations! Your Oracle Cloud Infrastructure account can now authenticate your Terraform OCI provider commands. And your environment is ready to run the resource discovery commands.

References:

- [HashiCorp Releases](https://releases.hashicorp.com/terraform-provider-oci/)
- [Resource Discovery](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery)

## What's Next

Explore other Terraform tutorials:
- [Set Up OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm)
- [Create Scripts and State Files with Resource Discovery](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
