# Downloading and Installing the Windows Client Installer
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_CLI_download_install.htm
- Fetched: 2026-09-05 02:34 CDT

# Downloading and Installing the Windows Client Installer

Complete the tasks in this topic to download and install the Windows client installer for Dedicated KMS.

## Downloading the Dedicated KMS Windows CLI Client

Oracle provides a download of the Dedicated KMS Windows client file at[Oracle Cloud Infrastructure (OCI) Dedicated Key Management Service Downloads](https://www.oracle.com/downloads/cloud/cloud-infrastructure-dedicated-kms-downloads.html).

After you download the installer, open the file and follow the instructions in the Client Setup Wizard to install the client on your local machine.

For release information on current and older DKMS Windows clients, see[Windows Clients](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_downloads.htm#dkms_downloads_windows_clients)in the[Dedicated KMS Client Changelog](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_downloads.htm)topic.

## Installing the Windows Client Service

Review the[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_cng_ksp.htm#dkms_windows_cng_ksp__cngksp-prereq)for using a KSP or CNG provider.

Complete the following steps to install Windows client server:

- Navigate to the Windows directory where you downloaded the MSI installer file.
- Run the installer by specifying the installation location. For example:`c:\Program Files\Oracle\DedicatedKMS`. Then follow the installation sequence.
- Click Finish .
- Navigate to the installation directory for the Dedicated KMS client. For example:`c:\Program Files\Oracle\DedicatedKMS`.

Note  
  
By default, Windows installs the program at`c:\Program Files\Oracle\DedicatedKMS`. However, the Windows client can be installed anywhere on your local machine.
- Run the`configure_dkms.exe`file by providing the installation path and DNS name of the HSM cluster. (or)
- Run the following command to enter the installation path and DNS name.

```

```

Note  
  

- If you're updating an existing client installer, the existing client configuration from previous installations aren't overwritten.
- As part of installation, the Windows Client Installer automatically registers the Cryptography API: Next Generation (CNG) and key storage provider (KSP). However, you can run the`Register`command to validate registration.
- After the installation is complete, you can go the[Client Service](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_windows_CLI_download_install.htm#dedicated_kms_config_client_deamon_windows),[User Management utility,](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_launch_vm_windows.htm)and[Key Management utility](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_key_mgmt_windows.htm)configuration files to verify the DNS name and configuration details.

## Configuring the Windows Client Service

Complete the following steps to configure the client service config. Ensure you have copied`pkey-c`,`cert-c`, and`partitionOwnerCert.pem`to the`data`directory of the Windows client installation. By default, the directory is at`C:\Program Files\Oracle\DedicatedKms\data`.
- Open the`client.cfg`file in a text editor to validate the installation location, DNS name of the HSM and the`client.cfg`file.
- Optional: Update the hostname field with DNS value available on the OCI Console. For more information, see[Getting HSM Cluster DNS Name.](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm)
- Optional: Update port field with the client Port value available on the OCI Console. For more information, see[Getting HSM Cluster Port Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm).
Output
```

```
