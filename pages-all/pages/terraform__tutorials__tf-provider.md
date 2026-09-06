# Set Up OCI Terraform
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm
- Fetched: 2026-09-05 19:21 CDT

# Set Up OCI Terraform

Set up Oracle Cloud Infrastructure Terraform provider scripts, documented in the Terraform Registry, to connect to an OCI account. Confirm the setup by fetching information from the tenancy.

Key tasks include how to:
- Create RSA keys.
- Set up Oracle Cloud Infrastructure Terraform provider scripts:
- Authenticate your Terraform scripts.
- Get information about the availability domains in your tenancy.

For more information, see:
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [Introduction to HashiCorp Terraform Video](https://www.youtube.com/watch?v=h970ZBgKINg)
- [Terraform Registry](https://registry.terraform.io/browse/providers)

## Before You Begin

To successfully perform this tutorial, you must have the following:
- An Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows environment:

[MacOS or Linux](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

- MacOS
- Linux (Any distribution)
- You can install a Linux VM with an Always Free Compute shape, on Oracle Cloud Infrastructure. See[Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/Content/developer/apache-on-oracle-linux/01-summary.htm).
- Oracle Cloud Infrastructure Cloud Shell:
- [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm)

[Windows](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

- [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)(WSL)
- [Git for Windows](https://gitforwindows.org/)to access a Linux VM.
Note  
  
This tutorial uses an Oracle Linux VM environment with an AMD shape for its examples, but you can use any environment mentioned in this section.

## 1. Prepare

Prepare your environment for authenticating and running Terraform scripts. Also, gather the information your account needs to authenticate the scripts.

[Install Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

This tutorial suggests that you install the latest version of Terraform that's supported for OCI Resource Manager. Resource Manager is a service for creating Terraform templates for OCI resources. In case you want to use Resource Manager with your Terraform scripts later, then your Terraform version is supported.

- In your environment, check the Terraform version.

```

```

If you don't have the latest[supported Terraform version](https://docs.oracle.com/iaas/Content/ResourceManager/Reference/terraformversions.htm), then install the latest supported version using the following steps.
- From a browser, go to[HashiCorp List of Terraform Versions](https://releases.hashicorp.com/terraform/).
- Select the folder with the latest[supported Terraform version](https://docs.oracle.com/iaas/Content/ResourceManager/Reference/terraformversions.htm).

Example:`terraform_1.5.7`
- Copy the name of the zip file that matches your environment into a notepad.

`terraform_ <version>_<your_environment> .zip`

Example for an Oracle 64-bit Linux AMD environment:`terraform_1.5.7_linux_amd64.zip`
- In your environment, create a temp directory and change to that directory:

```

```

```

```

- Download the Terraform zip file:

```

```

Tip  
  
You can construct the URL by copying the address from the browser. Note that &lt;version&gt; doesn't include the word`terraform`.

Example:

```

```

If you see a connection error, and you're on VPN, check your proxy settings. See[Troubleshooting](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#troubleshoot).
- Unzip the file. Example:

```

```

- Move the unzipped folder to a folder that contains the binaries of the third-party apps that you install. For example, for Oracle Linux, move the unzipped folder to`/usr/local/bin`:

```

```

- Go back to your home directory:

```

```

- Check the Terraform version:

```

```

Example:`Terraform v1.5.7 on linux_amd64`

Disregard any message indicating that the version of Terraform is out of date. The important thing is to use the latest[supported Terraform version](https://docs.oracle.com/iaas/Content/ResourceManager/Reference/terraformversions.htm).
You have now successfully installed Terraform.

[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

You create RSA keys for API signing in to your Oracle Cloud Infrastructure account.
Note  
  
Skip creating RSA keys if:
- You're using Cloud Shell or Resource Manager. You're already authenticated when you sign in to the Oracle Cloud Console.
- You already created RSA keys for the tutorial[Set Up Resource Discovery](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-resource-discovery-setup.htm).

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

[Add List Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

If your username is in the`Administrators`group, then skip this section. Otherwise, ask your administrator to add the following policy to your tenancy:

```

```

With this privilege, you can list all the resources in your tenancy.

[Steps to Add the Policy](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

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

[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

Prepare the information you need to authenticate your Terraform scripts and copy the information into a notepad.

- Collect the path to the private key that you added at[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#create-rsa-keys).

Example for Oracle Linux:`/home/opc/.oci/ <your-rsa-key-name> .pem`
- Collect the user OCID, fingerprint, tenancy OCID, and region from the API key you added at[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#create-rsa-keys). (You might have this in your notepad already.)

- [Sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)to the Oracle Cloud Console.
- In the navigation menu , select the Profile menu and then select User settings .
- Select API keys .
- Find the API key that you added at[Create RSA Keys](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#create-rsa-keys).
- From the Actions menu for the key, select View configuration file .

The Configuration file preview dialog box opens. Example:
```

```

- Select Copy , then paste into your notepad.

## 2. Create Scripts

Create scripts for authentication, to fetch data from your account, and to print outputs.

[Add API Key-Based Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

First, set up a directory for Terraform scripts. Then add a provider script so your OCI account can authenticate the scripts running from this directory. Finally, add a versions script containing a`required_providers`block to declare required provider versions.

- In &lt;your-home-directory&gt; , create a directory called`tf-provider`and change to that directory.

```

```

```

```

- Create a file called`provider.tf`.
- Add the following code to`provider.tf`:

- Replace the fields with brackets with information you collected at[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#gather-info).
- Add quotation marks around string values.

```

```

- Save the`provider.tf`file.
- In the same directory, create a file called`versions.tf`.
- Add the following code to`versions.tf`:

```

```

- Save the`versions.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

Use the following variables for API Key based authentication:
- `tenancy_ocid`
- `user_ocid`
- `private_key_path`
- `fingerprint`
- `region`
For details about OCI Terraform provider, see
- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [API Key Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)
Tip  
  
You don't need to install the provider. The provider is downloaded when you run the scripts in this tutorial.

[Add a Data Source](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

In this section, you fetch a list of the availability domains in your tenancy. By fetching data, you confirm that your OCI account authenticates your`provider.tf`script and you get information from your account.

- In the`tf-provider`directory, create a file called`availability-domains.tf`.

Important  
  
Ensure that all the`*.tf`files are in the same directory. Terraform processes all the files in a directory in the correct order, based on their relationship. (For a modular approach and future reuse, put provider information in a separate file from other scripts.)
- Add the following code to`availability-domains.tf`, replacing the field with brackets, with information from[Gather Required Information](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#gather-info).

```

```

Note  
  
The data source gets a list of availability domains in your entire tenancy. The tenancy is the compartment OCID for the root compartment . Providing a specific`" <compartment-ocid> "`or the`" <tenancy-ocid> "`outputs the same list.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

In Terraform, to fetch data, you use a data source. Fetching data from a data source is similar to the GET method in REST APIs.
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`availability domains`.
- Under Identity , go to Data Sources and select oci_identity_availability_domains .

The title of the page is the resource type:`oci_identity_availability_domains`
- Find the Data Source name from the title of the page:
- Data Source:
- In the Argument Reference section, find all arguments (inputs) labeled as (Required) :
- compartment_id
- Construct a data source block:
- Declare a data source with the keyword:`data`.
- Add a label for the data source name:`"oci_identity_availability_domains"`
- Add a label of your choice for the local name:
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- This tutorial uses the local name,`"ads"`to construct`data "oci_identity_availability_domains" "ads"`.
- Inside the code block, provide values for all required arguments.
- Example:`compartment_id = " <some-compartment-ocid> "`
- For optional arguments, provide values to narrow down the fetch results. Only some data sources have optional arguments.

[Add Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

The data source`oci_identity_availability_domains`, fetches a list of availability domains. In this section, you declare an output block to print the fetched information.

- In the`tf-provider`directory, create a file called`outputs.tf`.
- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.

Important  
  
Ensure that all the`*.tf`files are in the same directory. Terraform processes all the files in a directory in the correct order, based on their relationship.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

- Go to[Attributes Reference (oci_identity_availability_domains)](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains#attributes-reference).
Note  
  
Attributes are the outputs that you can return for the`oci_identity_availability_domains`data source.
- Find the attributes:
- Attribute:`availability_domains:`
- The list of availability domains
- If you output`availability_domains:`, you get three attributes for each availability domain in the list:
- compartment_id
- id
- name
- Construct a data source output block:
- Declare an output block with the keyword:`output`
- Add a label to be printed with the output results:
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"all-availability-domains-in-your-tenancy"`
- Inside the code block, enter a value for the data source output with the expression:
- `value = data . <data-source-name> . <local-name-for-data-source> . <attribute>`
- Example:`value = data .oci_identity_availability_domains.ads. availability_domains`

## 3. Run Scripts

Run your Terraform scripts. After your account authenticates the scripts, Terraform fetches your tenancy's availability domains.

[Initialize](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

Initialize a working directory in the`tf-provider`directory.

- Run the Terraform`init`command.

```

```

Example output:
```

```

If you see a connection error or "failed to query" error, and you're on VPN, check your proxy settings. See[Troubleshooting](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#troubleshoot).
- Check the contents of the`tf-provider`directory.

```

```

You now have a folder called`.terraform`that includes the plugins for the`oci`provider.

[Plan](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

Create an execution plan to check whether the changes shown in the execution plan match your expectations, without changing the real resources.

Run the Terraform`plan`command.

```

```

Example output:
```

```

Note  
  

- You're fetching data, so the plan shows that you're only adding outputs. You're not adding, changing, or destroying any resources.
- You're using the`output.tf`file instead of the`-out`option, so you can ignore the following message:
```

```

[Apply](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

- Run your Terraform scripts and get your outputs:

```

```

- When prompted for confirmation, enter`yes`.

After you run the`apply`command, the output is displayed in the terminal.
Example output:
```

```

Congratulations! Your Oracle Cloud Infrastructure account can now authenticate your Oracle Cloud Infrastructure Terraform provider scripts.

References:

- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [Data Source: oci_identity_availability_domains](https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains)
- [Basic CLI Features](https://developer.hashicorp.com/terraform/cli/commands)

[Troubleshooting](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-provider.htm#)

You might encounter the following error messages while running your Terraform scripts.

#### 401 Errors - (Service error:NotAuthenticated)

One of the following variables has an incorrect value:
- Tenancy OCID
- User OCID
- Fingerprint
- RSA private key (the path or the key)

- In the`provider.tf`file, double-check the variable names and their values.

```

```

- Update the variables or their values as needed.
- Ensure that you added quotation marks around string values.
- Run the scripts.

#### Can not create client, bad configuration: did not find a proper configuration for private key

The Terraform scripts can't find the RSA private key.

- Repeat the steps for creating RSA keys and use the updated key.
- Ensure that in the`provider.tf`file, the variable describing the RSA is called`private_key_path`.
private_key_path = " &lt;rsa-private-key-path&gt; "
- Ensure the path to the RSA private key in the`provider.tf`file is correct. For example, ensure that the path starts with a slash and has the correct name for the private key,`<your-rsa-key-name> .pem`
- Remove environment variables from the &lt;rsa-private-key-path&gt; .

For example, in the`provider.tf`file, instead of`$HOME/.oci/< rsa-private-key-path>`, use`/home/opc/ <rsa-private-key-path>`.

Note  
  
If you're using Windows Subsystem for Linux (WSL), create the`/.oci`directory directly in the Linux environment. If you create the`/.oci`directory in a`/mnt`folder (Windows file system), you're required to use the`chmod`command to change permissions for the WSL configuration files.

#### No such host

The region identifier has an incorrect value.

- In the Console navigation bar, find your region.
See[Working in Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm).
- In the[table at Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About__The), find your region's`<region-identifier>`. Example:`us-ashburn-1`.
- In the`provider.tf`file, update the value for &lt;region-identifier&gt; and try again.

#### Failed to query available provider packages

If you're on a VPN, check the proxy settings.

- Disconnect from VPN.
- Connect to your VM or your environment without the VPN and run the following Terraform scripts.

```

```

If you don't get an error message, then the VPN proxy settings are causing the error.
- Consult with your administrator, update the proxy settings, and try again.

## What's Next

For the next Terraform: Get Started tutorial, go to:
- [Create a Compartment](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-compartment.htm)

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
