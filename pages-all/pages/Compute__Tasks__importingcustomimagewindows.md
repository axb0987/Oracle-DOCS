# Importing Custom Windows Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/importingcustomimagewindows.htm
- Fetched: 2026-09-05 01:51 CDT

# Importing Custom Windows Images

The Compute service enables you to import Windows images that were created outside of Oracle Cloud Infrastructure. For example, you can import images running on your on-premises physical or virtual machines (VMs), or VMs running in Oracle Cloud Infrastructure Classic. You can then launch your imported images on compute virtual machines.

For information about the licensing requirements for Windows images, see[Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/microsoftlicensing.htm).

## Supported Operating Systems

These Windows versions support custom image import:
- Windows Server 2016: Datacenter, Standard, Standard Core
- Windows Server 2019: Datacenter, Standard, Standard Core
- Windows Server 2022: Datacenter, Standard, Standard Core
- Windows Server 2025: Datacenter, Standard, Standard Core
Note  
  

- Oracle Cloud Infrastructure has tested the operating systems listed previously and will support customers in ensuring that instances launched from these images and built according to the guidelines in this topic are accessible using RDP.
- For OS editions not listed previously, Oracle Cloud Infrastructure provides commercially reasonable support to customers in an effort to get instances that are launched from these images accessible via RDP.
- Support from Oracle Cloud Infrastructure in launching an instance from a custom OS does not ensure that the operating system vendor also supports the instance.

## Windows Source Image Requirements

Custom images must meet the following requirements:
- 

The maximum image size is 400 GB.
- 

The image must be set up for BIOS boot. You can leave the boot type as BIOS or change it to UEFI after you import the image.
- 

Only one disk is supported, and it must be the boot drive with a valid master boot record (MBR) and boot loader. You can migrate more data volumes after you import the image's boot volume.
- The minimum boot volume size is 256 GB. For more information, see[Custom Boot Volume Sizes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom).
- 

The boot process can't require more data volumes to be present for a successful boot.
- 

The disk image can't be encrypted.
- 

The disk image must be a VMDK or QCOW2 file.
- Create the image file by cloning the source volume, not by creating a snapshot.
- VMDK files must be either the "single growable" (monolithicSparse) type or the "stream optimized" (streamOptimized) type, both of which consist of a single VMDK file. All other VMDK formats, such as those that use multiple files, split volumes, or contain snapshots, aren't supported.
- 

The network interface must use DHCP to discover the network settings. When you import a custom image, existing network interfaces aren't recreated. Any existing network interfaces are replaced with a single NIC after the import process is complete. You can attach additional VNICs after you launch the imported instance.
- 

The network configuration must not hardcode the MAC address for the network interface.

## Preparing Windows VMs for Import

Before you can import a custom Windows image, you must prepare the image to ensure that instances launched from the image can boot correctly and that network connections will work.

You can perform the tasks described in this section on the running source system. If you have concerns about modifying the live source system, you can export the image as-is, import it into Oracle Cloud Infrastructure, and then launch an instance based on the custom image. You can then[connect to the instance using the VNC console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm)and perform the preparation steps.
Important  
  
The system drive where Windows is installed will be imported to Oracle Cloud Infrastructure. All partitions on the drive will follow through the imported image. Any other drives will not be imported and you must re-create them on the instance after import. You will then need to manually move the data on the non-system drives.

To prepare a Windows VM for import:
- 

Follow your organization's security guidelines to ensure that the Windows system is secured. This can include, but is not limited to the following tasks:
- 

Install the latest security updates for the operating system and installed applications.
- 

Enable the firewall, and configure it so that you only enable the rules which are needed.
- 

Disable unnecessary privileged accounts.
- 

Use strong passwords for all accounts.
- 

Configure Remote Desktop Protocol (RDP) access to the image:
- [Enable Remote Desktop connections](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-client-faq)to the image.
- [Modify the Windows Firewall inbound port rule](https://docs.microsoft.com/windows/security/threat-protection/windows-firewall/create-an-inbound-port-rule)to allow RDP access for both Private and Public network location types. When you import the image, the Windows Network Location Awareness service will identify the network connection as a Public network type.
- 

Determine whether the current Windows license type is a volume license by running the following command in PowerShell:

```

```

If the license is not a volume license, after you import the image, you will update the license type.
- 

If you plan to launch the imported image on more than one VM instance,[create a generalized image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/windowsimages.htm#Creating)of the boot disk. A generalized image is cleaned of computer-specific information, such as unique identifiers. When you create instances from a generalized image, the unique identifiers are regenerated. This prevents two instances that are created from the same image from colliding on the same identifiers.
- 

Create a backup of the root volume.
- 

If the VM has remotely attached storage, such as NFS or block volumes, configure any services that rely on this storage to start manually. Remotely attached storage is not available the first time that an imported instance boots on Oracle Cloud Infrastructure.
- 

Ensure that all network interfaces use DHCP, and that the MAC address and IP addresses are not hard-coded. See your system documentation for steps to perform network configuration for your system.
- [Download the Oracle VirtIO Drivers for Microsoft Windows](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html).
- 

[Install the drivers](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindows.html)and then restart the instance.
- 

Stop the VM.
- 

Clone the stopped VM as a VMDK or QCOW2 file, and then export the image from your virtualization environment. See the tools documentation for your virtualization environment for steps.

## Importing a Windows-Based VM

After you prepare a Windows image for import, follow these steps to import the image:
- 

[Upload the image file to an Object Storage bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm). You can upload the file using the Console or using the[command line interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). If you use the CLI, use the following command:

```

```

- Open the navigation menu and select Compute . Under Compute , select Custom Images .
- 

Select Import image .
- 

In the Create in compartment list, select the compartment that you want to import the image to.
- 

Enter a Name for the image. Avoid entering confidential information.
- 

For the Operating system , select Windows .
- 

In the Operating system version list, select the version of Windows.
- 

Confirm that you chose the operating system version that complies with your Microsoft licensing agreement, and then select the compliance checkbox.
Important  
  
Failure to provide the correct version and SKU information could be a violation of your Microsoft Licensing Agreement.
- 

Select the Import from an Object Storage bucket option.
- Select the Bucket that you uploaded the image to.
- In the Object name list, select the image file that you uploaded.
- 

For the Image type , select the file type of the image, either VMDK or QCOW2 .
- 

In the Launch mode area, select Paravirtualized mode .
- Show tagging options: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Import image .

The imported image appears in the Custom images list for the compartment, with a state of Importing . When the import completes successfully, the state changes to Available .

If the state doesn't change, or no entry appears in the Custom images list, the import failed. Ensure that you have read access to the Object Storage object, and that the object contains a supported image.
- Complete the post-import tasks.

## Post-Import Tasks for Windows Images

After you import a custom Windows-based image, do the following:
- If you want to use the image on AMD or X6-based[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm), add the shapes to the image's[list of compatible shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm).
- [Create an instance based on the custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm). For the image source, select Custom Images , and then select the image that you imported.
- [Enable Remote Desktop Protocol (RDP) access](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#prerequisites)to the compute instance.
- [Connect to the instance using RDP](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm).
- If the instance requires any remotely attached storage, such as[block volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm)or[file storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm), create and attach it.
- [Create and attach any required secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#create_sec_vnic).
- Test that all applications are working as expected.
- Reset any services that were set to start manually.
- Configure your instance to use the Network Time Protocol (NTP). You can use the[Oracle Cloud Infrastructure NTP service](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm), or you can use the[Windows Time service (W32Time)](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-top).
Tip  
  
If you encounter a no time data was available error message when setting up NTP on Windows Server, review the information in the[Microsoft known issue](https://docs.microsoft.com/troubleshoot/windows-server/identity/error-message-run-w32tm-resync-no-time-data-available)article.
- 
Register the instance with the Oracle-provided Key Management Service (KMS) server:
Important  
  
To register the instance with the KMS server, the time on your instance must match your time zone.
- On the instance, open PowerShell as Administrator.
- 

To set the KMS endpoint, run the following command:

```

```

- 

If the Windows license type that you noted while preparing the image isn't a volume license, then you must update the license type. Run the following command:

```

```

&lt;setup key&gt; is the[KMS client setup key](https://docs.microsoft.com/windows-server/get-started/kmsclientkeys)that corresponds to the version of Windows that you imported:
Important  
  
Go to Microsoft's[Key Management Services (KMS) client activation and product keys](https://docs.microsoft.com/windows-server/get-started/kmsclientkeys)page and get the &lt;setup key&gt; for your operating system version. Entries looks similar to:

Windows Server 2025 Standard:`XXXXX-XXXXX-XXXXX-XXXXX-XXXXX`

To determine the Windows version of the VM, run the following command:

```

```

- 

To activate Windows, run the following command:

```

```

- 

To verify the license status, run the following command:

```

```

If the`LicenseStatus`is`1`
