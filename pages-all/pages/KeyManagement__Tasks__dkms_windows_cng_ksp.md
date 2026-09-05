# Windows Next Generation (CNG) and Key Storage Providers (KSP)
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_cng_ksp.htm
- Fetched: 2026-09-05 02:34 CDT

# Windows Next Generation (CNG) and Key Storage Providers (KSP)

Learn how to secure Windows-based applications with CNG and KSPs.

OCI Dedicated Key Management supports[Cryptography API: Next Generation](https://learn.microsoft.com/windows/win32/seccng/cng-portal)(CNG) and Key Storage Providers (KSP) for Microsoft Windows applications.

Key Storage Providers (KSPs) manage the storage and retrieval of cryptographic keys. When setting up the Microsoft Active Directory Certificate Services (AD CS) role on a Windows server and generating a new private key for your Certificate Authority, you can select a KSP to manage key storage.

CNG is a cryptographic API developed for Microsoft Windows to secure Windows-based applications. OCI's Dedicated KMS implementation of CNG provides the following key functionality: fundamental cryptographic operations, key import and export for managing asymmetric keys, and secure key storage and retrieval for isolating the private key of an asymmetric key pair. See[About CNG](https://learn.microsoft.com/windows/win32/seccng/about-cng)in the Microsoft documentation for more information.

The following topics give you details about the tools for installing and configuring the Windows client service and then configuring the User Management utility and Key Management utility to use CNG and KSPs.
- [Downloading and Installing the Windows Client Installer](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_CLI_download_install.htm)
- [Client Parameters](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_configure_client_component_parameters.htm)
- [Starting Windows Client Service](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_start_windows_client_installer.htm)
- [Registering CNG Provider](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_register_cng.htm)
- [Registering KSP Provider](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_register_ksp.htm)

For information on configuring the user and key management utilities in Windows, see the following topics in[Dedicated KMS command line tools for Windows](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_install_windows_client.htm):
- [Configure the Dedicated KMS User Management Utility in Windows](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_launch_vm_windows.htm)
- [Configuring the Dedicated Key Management Utility in Windows](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_key_mgmt_windows.htm)

## Prerequisites

Before using a KSP or CNG provider, complete the following configuration:

On you local Windows machine, configure the credentials for the Windows client service using a Windows system environment variable. Use any of the following methods to create the environment variable:
- Run the`setx`command to set up the system environment variables
- Run permanent system environment variables[programmatically](https://msdn.microsoft.com/en-us/library/system.environment.setenvironmentvariable(v=vs.110).aspx)
- In the Windows System Properties dialog, configure the Advanced tab

Create the following Windows system environment variable:`n3fips_password= <username> : <password>`

Example setx command :`setx /m n3fips_password test_user:password123`
