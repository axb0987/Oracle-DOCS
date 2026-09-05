# Quickstart
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
- Fetched: 2026-09-05 01:36 CDT

# Quickstart

This section documents how to quickly install and configure the OCI Command Line Interface (CLI).

## Installing the CLI

### What's In This Section
This section contains quick installation instructions for the following environments:
- [Oracle Linux 9](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__oraclelinux9)
- [Oracle Linux 8](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__oraclelinux8)
- [Oracle Linux 7](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__oraclelinux7)
- [Mac OS](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__macos_homebrew)
- [Windows](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__windows)
- [Linux and Unix](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__linux_and_unix)
- [Other Environments](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__other_environments)
- [Verifying the Install](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__verifying_the_cli_install)
- [Setting Up the Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile)

### Oracle Linux 9

If you're using Oracle Linux 9, you can use`dnf`to install the CLI.
Note  
  
We strongly recommend running`sudo dnf update`regularly to ensure your system is up-to-date by installing available updated RPMs.

To use`dnf`to install the CLI:

```

```

The CLI will be installed to the Python site packages:
- `/usr/lib/python3.9/site-packages/oci_cli`
- `/usr/lib/python3.9/site-packages/services`

Documentation and examples will be installed in the`/usr/share/doc/python39-oci-cli-<version>/`directory.

To uninstall the CLI:

```

```

### Oracle Linux 8

If you're using Oracle Linux 8, you can use`dnf`to install the CLI.
Tip  
  
Oracle Linux 8 uses Python 3.6 by default. For improved performance, we recommend that you upgrade to Python version 3.9 or later and install a compatible version of the CLI. For detailed instructions, see the[manual installation instructions](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro).
Note  
  
We strongly recommend running`sudo dnf update`regularly to ensure your system is up-to-date by installing available updated RPMs.

To use`dnf`to install the CLI:

```

```

The CLI will be installed to the Python site packages:
- `/usr/lib/python3.6/site-packages/oci_cli`
- `/usr/lib/python3.6/site-packages/services`

Documentation and examples will be installed in the`/usr/share/doc/python36-oci-cli-<version>/`directory.

To uninstall the CLI:

```

```

### Oracle Linux 7

If you're using Oracle Linux 7, you can use yum to install the CLI.
Tip  
  
Oracle Linux 7 uses Python 3.6 by default. For improved performance, we recommend that you upgrade to Python version 3.9 or later and install a compatible version of the CLI. For detailed instructions, see the[manual installation instructions](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro).

To use yum to install the CLI:

```

```

The CLI will be installed to the Python site packages:
- `/usr/lib/python3.6/site-packages/oci_cli`
- `/usr/lib/python3.6/site-packages/services`

Documentation and examples will be installed in the`/usr/share/doc/python36-oci-cli-<version>/`directory.

To uninstall the CLI:

```

```

### Mac OS

You can use[Homebrew](https://docs.brew.sh/Installation)to install, upgrade, and uninstall the CLI on Mac OS.

To install the CLI on Mac OS with Homebrew:

```

```

To upgrade your CLI install on Mac OS using Homebrew:

```

```

To uninstall the CLI on Mac OS using Homebrew:

```

```

### Windows

You can install the CLI on Windows by using the MSI installer or by using PowerShell.
To install the CLI on Windows using the MSI installer:
Note  
  
The MSI CLI installer will overwrite any existing versions of the CLI on your Windows system. If you need to install multiple versions of the CLI, for subsequent installs create a virtual environment and use the manual installation method. For more information, see[Manual and Offline Installations](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro).
- Download the OCI CLI MSI installer for Windows from[GitHub](https://github.com/oracle/oci-cli/releases).
- Run the downloaded installer executable.
- Select the local directory on your system where you want to install the CLI, and then select Next .
- When the installer is finished, select Finish .

To install the CLI on Windows using PowerShell:
- Open the PowerShell console using the Run as Administrator option.
- 

The installer enables auto-complete by installing and running a script. To allow this script to run, you must enable the RemoteSigned execution policy.

To configure the remote execution policy for PowerShell, run the following command.

```

```

- Force PowerShell to use TLS 1.2 for Windows 2012 and Windows 2016:

```

```

- Download the installer script:

```

```

- Run the installer script with or without prompts:
- To run the installer script with prompts, run the following command:

```

```

Respond to the[Installation Script Prompts](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__PromptsInstall).
- 
To run the installer script without prompting the user, accepting the default settings, run the following command:

```

```

### Linux and UNIX

Note  
  
The installer script automatically installs the CLI and its dependencies, Python and virtualenv. Before running the installer, be sure you meet the[requirements](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements).
Note  
  
Oracle Linux 8 and Oracle Linux Cloud Developer 7 have the CLI pre-installed.
- Open a terminal.
- To run the installer script, run the following command:

```

```

Note  
  
To run a 'silent' install that accepts all default values with no prompts, use the`--accept-all-defaults`parameter.
- Respond to the[Installation Script Prompts](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__PromptsInstall).

### Other Environments

To install the CLI in an environment not listed here, see[Manual and Offline Installations](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/climanualinst.htm).

### Verifying the OCI CLI Installation
- From a command prompt, run the following command:
```

```

### Installation Script Prompts

The installation script prompts you for the following information.

- If you don't have a compatible version of Python installed:
- Windows and Linux: You're prompted to provide a location for installing the binaries and executables. The script will install Python for you.
- MacOS: You're notified that your version of Python is incompatible. You must upgrade before you can proceed with the installation. The script will not install Python for you.
- When prompted to upgrade the CLI to the newest version, respond with Y to overwrite an existing installation.
- When prompted to update your PATH, respond with Y to be able to invoke the CLI without providing the full path to the executable. This will add`oci.exe`to your PATH.

## Setting up the Configuration File

Before using the CLI, you must create a configuration file that contains the required credentials for working with Oracle Cloud Infrastructure. You can create this file using a setup dialog or manually using a text editor.

### Use the Setup Dialog
To have the CLI guide you through the first-time setup process, use the`setup config`command:
```

```
This command prompts you for the information required to create the configuration file and the API public and private keys. The setup dialog uses this information to generate an API key pair and creates the configuration file. After API keys are created,[upload the public key using the Console](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm#three).

For more information about how to find the required information, see:
- [Required Keys and OCIDs.](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm)
- [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm#five)
- [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)

### Manual Setup

If you want to set up the API public/private keys yourself and write your own config file, see[SDK and Tool Configuration](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).
Tip  
  

Use the`oci setup keys`command to generate a key pair to include in the config file.

### Verifying the Configuration File

Make Sure Your Configuration File Is Complete

A proper configuration file should have at least one profile name (such as`[DEFAULT]`) and the entries specified in the[File Entries](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm#File_Entries)section: user, fingerprint, key_file, tenancy, region, and an optional pass_phrase.

Note  
  
See the[Example Configuration](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm#Example_Configuration)section for an example configuration file.

Confirm Your User and Fingerprint Information

You can confirm your user and fingerprint information by signing in to the OCI Console, opening the profile menu in the upper right, and then selecting your user name.

After you select your user name, the User Information panel displays your OCID. This OCID should be the user entry in your configuration file.

You can find your fingerprint by navigating to the API Keys section under the Resources column on the lower left.

Adding Comments to the Configuration File
Be sure not to add in-line comments to your configuration file. Add all comments on a new line. For example:
```

```

### Other Authentication Methods

The CLI also supports token-based, instance principal and resource principal authentication for some services. For more information, see[SDK Authentication Methods](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdk_authentication_methods.htm).

## Next Steps

- [Getting Started with the Command Line Interface](https://docs.oracle.com/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm)provides an end-to-end walk-through of using the CLI to launch an instance.
- [Using the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm)
