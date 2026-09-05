# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm
- Fetched: 2026-09-05 01:36 CDT

# Getting Started

This topic describes how to install and configure the OCI Modules for PowerShell.

This topic describes how to install and configure the OCI Modules for PowerShell.

## Prerequisites

Be sure to satisfy all the requirements listed[here](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershell.htm#one).

## Installing Modules

- Start a PowerShell session:

- On Windows, launch PowerShell from the Start Menu.
- 

On Linux or MacOS, run`pwsh`from a shell prompt:

```

```

- 

To install all OCI modules, install the base module:

`Install-Module OCI.PSModules`

Note  
  
Uninstalling the`OCI.PSModules`module will not uninstall other OCI modules. To uninstall a specific OCI module installed by this module, the`OCI.PSModules`module will have to be uninstalled first.
- You can install just the modules for an individual service. Cmdlets corresponding to each OCI service[supported](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershell.htm#Services_Supported)by OCI Modules for PowerShell are packaged into an individual Powershell module named`OCI.PSModules.<ServiceName>`.
- Continue to either[Installing from PowerShell Gallery](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_install_modules_install_from_powershell_gallery)or[Installing from GitHub](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#installing_from_github).

### Installing from PowerShell Gallery

- 

By default, PowerShell Gallery ("PS Gallery") is configured as a PSRepository. This can be verified by running the`Get-PSRepository`command:

```

```

- 

You can set PS Gallery as a trusted repository to avoid prompts every time you attempt to install a module from PS Gallery:

```

```

- 

PowerShell modules that correspond to a supported OCI service are called service modules . To install a service module run the[Install-Module](https://docs.microsoft.com/en-us/powershell/module/powershellget/install-module)command. This example installs the service module for the[OCI Identity service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm):

```

```

Note  
  
Each service module depends on the`OCI.PSModules.Common`(Common Module), which offers functionality common to all service modules. Installing a service module will also install the corresponding version of`OCI.PSModules.Common`for that service module.
- Installed modules can be found in the path specified by the`$Env:PSModulePath`environment variable, or by running the[Get-Module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module)command with the`ListAvailable`parameter.
```

```

### Installing from GitHub

To install the OCI PowerShell modules from GitHub:
- Download the latest[OCI Modules artifacts](https://github.com/oracle/oci-powershell-modules/releases)and extract them into a local directory.
Note  
  
Cmdlets corresponding to each OCI service[supported](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershell.htm#Services_Supported)by OCI Modules for PowerShell are packaged into an individual Powershell module named`OCI.PSModules.<ServiceName>`.
- Register the extracted directory as the local PowerShell repository:
```

```

- Find the modules available in the local repository:
```

```

- Install a specific module:
```

```

Note  
  
Each service module depends on the`OCI.PSModules.Common`(Common Module), which offers functionalities common to all service modules. Installing a service module will also install the corresponding version of`OCI.PSModules.Common`for that service module.
- Installed modules can be found in the path specified by the`$Env:PSModulePath`environment variable, or by running the[Get-Module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module)command with the`ListAvailable`parameter.
```

```

### Installing with Yum

If you are using Oracle Linux version 7.x, the OCI PowerShell Modules packages can be installed with yum.
- To install the OCI PowerShell modules using yum:
```

```

- Start a PowerShell Session and register the downloaded directory /usr/lib/dotnet/NuPkgs as a local PowerShell repository using the following command:
```

```

- Find the modules available in the local repository using the following command:
```

```

- Install a specific module:
```

```

Note  
  
Each service module depends on the`OCI.PSModules.Common`(Common Module), which offers functionalities common to all service modules. Installing a service module will also install the corresponding version of`OCI.PSModules.Common`for that service module.
- Installed modules can be found in the path specified by the`$Env:PSModulePath`environment variable, or by running the[Get-Module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module)command with the`ListAvailable`parameter.
```

```

## Setup

Follow[these installation steps](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_install_modules)if you haven't installed the required modules.

Before invoking cmdlets in OCI Modules, you need to[set up the configuration file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_setup_configuraion_file), and then optionally[import the required modules](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_setup_importing_modules)into a PowerShell session.

### Configuration File

A configuration file provides essential[configuration information](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm#File_Entries), like user credentials and tenancy OCID. This configuration information is used by the OCI Modules for PowerShell to authenticate and interact with Oracle Cloud services. You can create this file using a[setup cmdlet](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellgettingstarted.htm#powershellsdkgettingstarted_topic_setup_configuration_file_setociclientconfig), or manually using a text editor.

#### Set-OCIClientConfig

The`Set-OCIClientConfig`cmdlet included in the Common module will walk you through setting up a configuration file. This cmdlet prompts you for information required by the configuration file, including the key pair used to sign API requests.

For more information about how to find the required information, see:
- [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#Other)
- [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)

#### Manual Setup

If you want to set up the API signing key pair manually and write your own configuration file, see[SDK and Tool Configuration](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm)and[Required Keys](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).
Note  
  

Use the`New-OCIClientKeys`cmdlet to generate a API signing key pair to include in the configuration file.

### Importing Modules

PowerShell will automatically import the module (and its dependencies) into your session the first time you run any command from the installed module. To explicitly import a module, run the[Import-Module](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)command.

For example, to import the version 1.0.0 of the Identity service module:

```

```

To find all imported modules in your current PowerShell Session, run the`Get-Module`command:

```

```

Note  
  
Each service module depends on the`OCI.PSModules.Common`(Common Module), which offers functionalities common to all service modules. Installing a service module will also install the corresponding version of`OCI.PSModules.Common`for that service module.

## Updating Modules

New versions of the OCI PowerShell modules release weekly. To update the installed OCI PowerShell modules to the latest version, run the[Update-Module](https://docs.microsoft.com/en-us/powershell/module/powershellget/update-module)command.

Note  
  

Before updating any OCI module, you should first uninstall the module. To avoid dependency conflicts when importing modules into PowerShell session, update all installed OCI Modules to the same version.

```

```

## Uninstalling Modules

To remove any installed module, you can either use the[Uninstall-Module](https://docs.microsoft.com/en-us/powershell/module/powershellget/uninstall-module)cmdlet or delete the module folder located in the path in the`$Env:PSModulePath`environment variable.

For example:

```

```

## Next Steps

Now that you've taken care of installation and setup, you can proceed directly to[Working with Cmdlets](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts_topic_understanding_oci_cmdlets.htm), or continue to[Advanced Concepts](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/powershellconcepts.htm)
