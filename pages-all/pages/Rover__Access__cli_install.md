# Using the Command Line Interface with a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm
- Fetched: 2026-09-05 02:57 CDT

# Using the Command Line Interface with a Roving Edge Infrastructure Device

Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.

The Oracle Cloud Infrastructure Command Line Interface (CLI) provides a set of commands for configuring and running Roving Edge Infrastructure tasks. Use the CLI as an alternative to running commands from the Device Console. Sometimes you must use the CLI to complete certain tasks where no Device Console equivalent is available.

Use CLIs to perform Roving Edge Infrastructure service tasks within the Oracle Cloud Infrastructure cloud. These tasks can include requesting nodes, and running tasks directly on device nodes. Install the CLI separately on each device. CLIs installed on devices run locally within your environment and don't require internet access.

## Minimum Required CLI Version

The minimum CLI version required for Roving Edge Infrastructure is 2.12.1.

## Determining CLI Versions

Access the following URL to see the currently available version of the CLI:

[https://github.com/oracle/oci-cli/blob/master/CHANGELOG.rst](https://github.com/oracle/oci-cli/blob/master/CHANGELOG.rst)

Enter the following command at the prompt to see the version of the CLI currently installed on your machine:

```

```

If you have a version on your machine older than the version currently available, install the latest version.
Note  
  

Always update to the latest version of the CLI. The CLI is not updated automatically, and you can only access new or updated CLI features by installing the current version.

## Updating Your Hosts File

Open your`/etc/hosts`file and add an`ip_address host_name`entry for your RED.

Where`ip_address`is the IP address of the Roving Edge Infrastructure device, and`host_name`is the name of the Roving Edge Infrastructure host on which you are running the CLI.

For example:

`10.0.1.8 rover.mycompany.com`

Access the hostname by running the following commands:
- 

Download the`redroot.pem`certificate:

`echo -n | openssl s_client -showcerts -connect ip_address:8015 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > redroot.pem`
- 

Then display the DNS hostnames:

`openssl x509 -in redroot.pem -text -noout | grep DNS`

In the command's return, the following appears:
- 

`DNS:*.certcommonname.com`: This indicates a wildcard certificate. Prefix the certificate with the subdomain of your choice "ex: rover" and open your`/etc/hosts`file and add a line with the following:

`10.145.140.5 rover.certcommonname.com`
- 

`DNS:rover-install-red-1, DNS:…,`: Choose any of the DNS outputs and add the following line to your`/etc/hosts`file:

`10.145.140.5 rover-install-red-1`

Open your`/etc/hosts`file and add a line with the following:

`10.145.140.5 rover.mycompany.com otec-console-local rover-install-red-1`

If the required parameter value is listed as a variable, for example`name`, then you must provide a value. Enter the command as it appears in the documentation.

The inclusion of`[OPTIONS]`in the command syntax indicates optional parameters. Access the CLI's online help for a list of optional parameters and their usage.

## Installing the CLI

Installation and configuration of the CLIs is described in detail in[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)topic in the Oracle Cloud Infrastructure documentation.

## Setting Up the Config File

Before setting up the config file, you need to gather the following information:
- 

Roving Edge Infrastructure tenancy OCID. Obtain the tenancy OCID using the following command:
```

```

where`ip_address`is the IP address of the Roving Edge Infrastructure device. The tenancy OCID is contained in the return, for example:
```

```

Alternatively, enter the following URL into your Device Console web browser:
```

```

The tenancy OCID is returned in your web browser.
- 

Roving Edge Infrastructure user Identity and Access Management (IAM) OCID. Obtain the tenancy OCID using the following steps:
- 

Access the Device Console for your device node.
- 

Open the navigation menu and select Identity Management &gt; Users .

The Users page appears. All users are listed in tabular form.
- 

Select the user whose details you want to get. The user's Details page appears.
- 

Find the OCID line under User Information in the Details page and copy link and save this information.

Keep the IAM User web page open as you need it to upload the public key in PEM format.
- 

Create an`.oci`directory in the home directory on the host where you have OCI CLI installed. For example:
- 

Linux and Macintosh:
```

```

- 

Windows PowerShell:
```

```

- 

RSA Key Pair in PEM format: In a Linux or Macintosh terminal, or Windows PowerShell window, switch to the`.oci`directory and run:
```

```

The command creates the following files in the`.oci`directory:
- 

`oci_api_key_public.pem`
- 

`oci_api_key.pem`

Return to Device Console and go to the IAM User Details page. Select API Keys on the left side of the window, then select Add Public Key and select the`oci_api_key_public.pem`file for upload.

After uploading the key, record the Fingerprint value as you will need it later for updating the configuration file.

In the`.oci`directory, create the`config`file and populate it with the following:
```

```

If you included a passphrase when creating the PEM key, add a line with:
```

```

Note  
  

Roving Edge Infrastructure OCIDs, such as for`user`and`tenancy`, contain`orei`in the values.

If you already have a`config`file with a`DEFAULT`profile, you can create more entries with a profile with the name of your choice.

Each Roving Edge Infrastructure tenancy (device) needs its own profile. You can use a base name and increment the number for each device. The following example uses the profile name`ROVINGEDGE1`from the base name`ROVINGEDGE`:

The following example uses the profile`ROVINGEDGE1`:
```

```

Note  
  

All Roving Edge Infrastructure OCIDS contain the string`orei`.

If you're using a non-default profile name, include the`--profile profile_name`option in all CLI commands. For this example, using the`ROVINGEDGE1`profile requires you include`--profile ROVINGEDGE1`in your CLI syntax. The following section "Setting Up the OCI CLI RC File" describes an optional method of eliminating this requirement.

Each Roving Edge Infrastructuredevice requires its own profile. Pick a base name such as`ROVINGEDGE`and increment the number for each device. For example:`ROVINGEDGE1`.

## Setting Up the OCI CLI RC File

Oracle strongly recommends setting up an optional OCI CLI RC file when using Roving Edge Infrastructure devices. Setting up an OCI CLI RC file makes running CLI commands easier by eliminating the need to include the`--profile profile_name`option in all CLI commands.

The OCI CLI RC file needs to match the profile set in the`config`file. If you are using a`DEFAULT`profile in the`config`file, the OCI CLI RC file also uses`DEFAULT`. If you created a profile with another name, such as`ROVINGEDGE1`, use`ROVINGEDGE1`profile for the OCI CLI RC file.

Before setting up the OCI CLI RC file, perform the following tasks to get the following information:
- 

Create a cert bundle:

Return to where you generated your PEM keys and run the following command:
```

```

A file with three certificates is created in the`.oci`directory. Record the path for future use.
- 

Create a file called`oci_cli_rc`in the`.oci`directory with the following contents:
```

```

If you already have an`oci_cli_rc`file configured with a`DEFAULT`entry, match the name used in the`config`file. If you use another profile name (for example,`ROVINGEDGE1`), the`oci_cli_rc`file includes that name. For example:
```

```

## Using the CLI

You can specify CLI options using the following commands:
- 

`--option value`

or
- 

`--option= value`

Not using the OCI CLI RC File

If you're not using an`oci_cli_rc`file, the basic CLI syntax for Roving Edge Infrastructure is:
```

```

This syntax is applied to the following:
- 

`oci`is the shortened CLI command name
- 

`os bucket`is an example of a`resource`
- 

`create`is an example of an`action`
- 

Other strings are`options`

Resource endpoints are:
- 

Object Storage :`https://otec-console-local:8019`

Object Storage commands also need to include the`--namespace rover-namespace`option.
- 

Compute :`https://otec-console-local:19060`
- 

Block Storage :`https://otec-console-local:5012`
- 

IAM :`https://otec-console-local:12050`
- 

Network :`https://otec-console-local:18336`
- 

Data Sync :`https://otec-console-local:21060`
- 

System Upgrade :`https://otec-console-local:23060`
- Events :`https://otec-console-local:18000`
- Monitoring :`https://otec-console-local:22060`
- Diagnostic Tooling :`https://otec-console-local:31060`

Include the value`otec-console-local`for the`IP address`line entry in the`/etc/hosts`file to use the`oci_cli_rc`file functionality.

If you're using an Oracle Cloud Infrastructure certificate, resource endpoints are:

`Ex: DNS:*.commonname.com`
- 

Object Storage :`https://rover.commonname.com:8019`

Object Storage commands also need to include the`--namespace rover-namespace`option.
- 

Compute :`https://rover.commonname.com:19060`
- 

Block Storage :`https://rover.commonname.com:5012`
- 

IAM :`https://rover.commonname.com:12050`
- 

Network :`https://rover.commonname.com:18336`
- 

Data Sync :`https://rover.commonname.com:21060`
- 

System Upgrade :`https://rover.commonname.com:23060`
- 

Events :`https://rover.commonname.com:18000`
- 

Monitoring :`https://rover.commonname.com:22060`
- 

Diagnostic Tooling :`https://rover.commonname.com:31060`
Note  
  

If the device certificate is self-signed, Include the value`otec-console-local`for the IP address line entry in the /etc/hosts file to use the`oci_cli_rc`file functionality.

This is an example of a CLI command:
```

```

If your`config`file entry for the Roving Edge Infrastructure environment is not`DEFAULT`, include the`--profile profile_name`option in your CLI syntax. For example:
```

```

Note  
  

Avoid entering confidential information as part of the display name.

Using the OCI CLI RC File

If you are using`the oci_cli_rc`file, the basic CLI syntax for Roving Edge Infrastructure is:
```

```

This syntax is applied to the following:
- 

`oci`is the shortened CLI command name
- 

`os bucket`is an example of a`resource`
- 

`list`is an example of an`action`
- 

Other strings are`options`

The following command line example shows a typical CLI command construct for listing the buckets in a specified compartment:
```

```

If your`config`file entry for the Roving Edge Infrastructure environment is not`DEFAULT`, you must also include the`--profile profile_name`option in your CLI syntax. For example:
```

```

## Required and Optional Parameters

Most command line utilities have both required and optional parameters that are included with the command. Required parameters are included in the command's syntax, for example:
```

```

If the required parameter value is listed as a variable, for example`name`, then you must provide a value. Enter the command as it appears in the documentation.

The inclusion of`[OPTIONS]`in the command syntax indicates optional parameters. Access the CLI's online help for a list of optional parameters and their usage.

## Running CLI Commands on Device Hosted Instances

Follow these guidelines to run CLI commands on compute instances hosted by Roving Edge devices.

Note  
  

The instructions in this topic are for Oracle Linux host computers.
- 

Have the instance go through the following local IP:

`169.254.169.254`

Have the instance refer to the Roving Edge device as`otec-console-local`.
- 

Employ the following IP Tables rules:
```

```

See[Service Ports](https://docs.oracle.com/iaas/Content/Rover/device_specifications.htm#ServicePorts)for a list of available ports.
Note  
  

On some OSs, the`BareMetalInstanceServices`chain might instead be`InstanceServices`. Use the iptables -L command to see what applies to your OS.

Save the iptable so that the rules persist after a reboot:
```

```

## Unsupported CLI Commands

The following CLI commands are currently not supported. Workarounds are provided where available.
- 

Object Storage CLIs :`oci os list`

You can only use the`oci os list`command when you include the`--fields`option. For example:
```

```

- 

Compute CLIs :`oci compute instance list-vnics`

The`oci compute instance list-vnics`command lists the VNICs that are attached to the specified instance and is often used to get the public IP for a compute node. This CLI is not currently supported in Roving Edge Infrastructure. You can get VNIC information, including IP address associated with a VNIC attached to a compute node, using any of the following methods:

- 

Device Console : Go to the following location:

Compute &gt; Instances &gt; Instance Details &gt; Attached VNICs

The IP addresses for the VNICs are listed in the dialog box that appears.
- 

CLI :`oci compute instance list-vnics`

First, run the following command to list all the VNIC's attachments:
```

```

Next, run the following command for the specific VNIC for which you want to get details:
```

```

The following example shows these two commands run together with their respective returns:
```

```

If only one VNIC is attached, you can combine these CLI commands with other Linux tools to limit the output to just the public IP address using the following command:
```

```

For example:
```

```

## Accessing Command Line Interface Help

All CLI help commands have an associated help component you can access from the command line. To view the help, enter any command followed by the`--help`or`-h`option. For example:
```

```
