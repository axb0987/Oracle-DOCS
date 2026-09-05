# Shielded Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm
- Fetched: 2026-09-05 01:49 CDT

# Shielded Instances

Shielded instances harden the firmware security on bare metal hosts and virtual machines (VMs) to defend against malicious boot level software.

## How Shielded Instances Work

Shielded instances use the combination of[Secure Boot](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-secureboot),[Measured Boot](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-measuredboot), and the[Trusted Platform Module](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-tpm)to harden the firmware security on your instances.

### Linux and UNIX-like Operating Systems

- Secure Boot and the Trusted Platform Module (TPM) are available on all[supported](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-supported-shapes)bare metal and VM instances.
- Measured Boot is only available on VM instances. If you want to use Measured Boot on a bare metal instance, you can use an open source solution.
- On bare metal instances, you can enable Secure Boot and the TPM together or independently.
- On VM instances, you can enable:
- Secure Boot only.
- TPM and Measured Boot.
- Secure Boot with TPM and Measured Boot.

### Windows Operating Systems

- For VM shapes, Secure Boot, Measured Boot, and the TPM must be used together. Therefore, when you enable one of the three features, the other two features are also enabled.
- Shielded instances support[Windows Defender Credential Guard](https://docs.microsoft.com/windows/security/identity-protection/credential-guard/credential-guard)when running one of the following OS versions: Windows Server 2016, Windows Server 2019, Windows Server 2022, or Windows Server 2025.

### Secure Boot

[Secure Boot](https://uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf)is a Unified Extensible Firmware Interface (UEFI) feature that prevents unauthorized boot loaders and operating systems from booting. Secure Boot validates that the signed firmware's signature is correct before booting to prevent rootkits, bootkits, and unauthorized software from running before the operating system loads. Boot components that aren't properly signed are not allowed to run.

Rootkits are low-level malware that run in kernel mode. Bootkits replace the system bootloader and system boots with the bootkit instead of the bootloader. Rootkits and bootkits have the same privileges as the operating system and can capture functions like keystrokes and local sign-ins. They can use this information to make unauthorized file transfers and to compromise the operating system.

### Measured Boot

Measured Boot is complementary to Secure Boot. To provide the strongest security, enable both Measured Boot and Secure Boot.

Secure Boot ensures that every component in the boot process has a signature that is in the list of valid signatures. Signed components can embed additional signatures to provide a chain of trust. Measured Boot lets you track boot measurements in order to understand what firmware you have and when it changes. When components are updated or reconfigured (for example, during an operating system update), the relevant measurements will change. Additionally some of these measurements will be impacted by the shape and size of the instance. While it is possible to compare these measurements against a set of known measurements, OCI does not currently generate or save known measurements. However, the measurements can be used to attest that OVMF UEFI firmware has not changed since the instance was deployed. This is particularly valuable because the certificates that create the root of trust for UEFI Secure Boot are contained within the OVMF UEFI firmware. Those measurements are reflected in PCR 0 and PCR 2, which are the only PCRs that currently trigger a shield color change.

Measured Boot enhances boot security by storing measurements of boot components, such as bootloaders, drivers, and operating systems. The first time you boot a shielded instance, Measured Boot uses the initial measurements to create a baseline. The baseline measurements are also known as golden measurements.

After initial measurements are taken, when the system boots, the new boot data is compared against the baseline measurement to verify that every boot is identical. The measurement comparison guarantees that the operating system starts from a clean pre-boot environment. Measured Boot uses a Trusted Platform Module (TPM) to store its measurements securely.

### Trusted Platform Module

The[Trusted Platform Module (TPM)](https://uefi.org/sites/default/files/resources/UEFI_Plugfest_Advanced_TPM_Usage_Fall_2018.pdf)is a specialized security chip used by Measured Boot to store the boot measurements.

Measurements taken by Measured Boot are stored in Platform Configuration Registers (PCRs) inside the TPM. A PCR is a memory location in the TPM used to hold a value that summarizes all the measurement results that were presented to it in the order they were presented.[Windows Defender Credential Guard](https://docs.microsoft.com/windows/security/identity-protection/credential-guard/credential-guard)uses the TPM to protect Virtualization-Based Security (VBS) encryption keys.

## Supported Shapes and Images

[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

You can use the following[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)to create shielded instances:
Note  
  

- On Linux and UNIX-like operating systems, Measured Boot is only available on VM instances.
- Shielded instances using Windows Server 2019 don't support BM.Standard2.52 and BM.DenseIO2.52 shapes.
- Credential Guard is not supported for bare metal shapes.
- VM.Standard3.Flex
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex
- VM.Standard.E5.Flex
- VM.Standard.E6.Flex
- VM.Optimized3.Flex
- BM.Standard2.52
- BM.Standard.E3.128
- BM.Standard.E4.128
- BM.Standard.E5.192
- BM.Standard.E6.256
- BM.Dense.E4.128
- BM.Dense.E5.128
- BM.DenseIO2.52

[Supported Platform Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

Shielded instances are supported on the following[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm):
- Oracle Linux 8.x
- Oracle Linux 9.x
- Oracle Linux 10.x
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 24.04
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2025

## Limitations and Considerations

Be aware of the following information:
- Shielded instances do not support[live migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#live-migration)or[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#reboot). See[Migrating Shielded Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-migrate)for more details.
- If you enable the hardware TPM on a bare metal instance, the instance cannot be migrated, because the hardware TPM is not migratable.
- Custom images are not supported.
- Confidential computing is not supported.
- Updating Forbidden Signatures Databases (DBX) on shielded VM instances is not supported. A DBX maintains a secure boot database of signatures that are not authorized to run on the platform. Applying DBX updates on a shielded VM instance might prevent the instance from booting. To update the DBX, create a new shielded VM instance with an image that includes the DBX updates.
- When you terminate an instance, any Machine Owner Keys (MOK) are deleted. If you used a kernel signed by a MOK to boot and the instance was terminated, when you create a new instance with Secure Boot, you need to use a kernel that boots from a standard UEFI secure database key. After the instance boots, add the Machine Owner Keys, and then reboot into your MOK-signed kernel.
- When you create a shielded instance using Linux 7.x and then reboot the instance, PCR values might change, causing the red shield to appear. See[PCR values change after reboot on Linux 7.x](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../known-issues.htm#shielded-pcr-values).
- When you[edit a shielded instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/edit-instance.htm), only the name of the instance can be changed. You cannot change the shape of the instance after it is launched, and you cannot change the migration settings.

## Using Shielded Instances

When you[create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm), you specify whether the instance is a shielded instance.

[To create a shielded instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

- Follow the steps to[create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm), until the Image and shape section.
- Select Change image .
- Select an image which includes Shielded instance in the Security column.
- Choose Select image .
- Select Change shape , then select a shape which includes Shielded instance in the Security column.
- Choose Select shape .
- In the Security section, select Edit .
- Select the toggle switch at the top of the Shielded instance section. Then select from the following options.
- Secure Boot : Enable Secure Boot on the instance. Secure boot prevents unauthorized boot loaders and operating systems from booting.
- Measured Boot : Select this option to enable Measured Boot on the instance. Measured Boot enhances boot security by taking and storing measurements of boot components, such as bootloaders, drivers, and operating systems.
Note  
  
On Linux and UNIX-like operating systems, Measured Boot is available only for VM instances.
- Trusted Platform Module : Select this option to enable the TPM on the instance. A Trusted Platform Module (TPM) securely stores boot measurements.
- Finish creating the instance and then select Create .

[To enable Windows Defender Credential Guard](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

- [Create a shielded instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-create)using either Windows Server 2016 or Windows Server 2019.
- Follow the steps in the Microsoft documentation to[install the Hyper-V role on your instance](https://docs.microsoft.com/windows-server/virtualization/hyper-v/get-started/install-the-hyper-v-role-on-windows-server).
- Follow the steps in the Microsoft documentation to[enable Windows Defender Credential Guard](https://docs.microsoft.com/windows/security/identity-protection/credential-guard/credential-guard-manage).
Important  
  
If you use Group Policy to enable Windows Defender Credential Guard, in the Select Platform Security Level box, select Secure Boot . Don't select Secure Boot and DMA Protection .

To verify whether Windows Credential Guard is running, open the Microsoft System Information tool (msinfo) on your Windows Server instance. If the value for Device Guard Virtualization based security is Running , Windows Defender Credential Guard is enabled. If Credential Guard is not running, the value is Enabled but not running .

## Working with Golden Measurements

Measured Boot enhances boot security by storing the measurements of boot components, such as bootloaders, drivers, and operating systems. After initial measurements are taken, when the system boots, the new boot data is compared against the baseline measurement to verify that every boot is identical. The baseline measurements are known as golden measurements.

### Downloading PCR Values

You can download the golden measurements and Platform Configuration Register (PCR) values for your instance. The PCR is a memory location in the TPM that stores the golden measurements.

[To download PCR values](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

- Navigate to the Compute instance list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/list-instances.htm).
- Select the instance that you're interested in.
- On the Instance details page, open the Shielded instance tab.
- Under Platform Configuration Register (PCR) , select Copy PCR values . The PCR values are copied to your clipboard. Paste them into the file of your choice.

### Resetting Golden Measurements

If you update your operating system, you might need to create new golden measurements. Follow these steps to reset the golden measurements for an instance.

[To reset golden measurements](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#)

- Navigate to the Compute instance list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/list-instances.htm).
- Select the instance that you're interested in.
- On the Instance details page, open the Shielded instance tab.
- Under Platform Configuration Register (PCR) , select Reset golden measurements . Confirm when prompted.

## Migrating Shielded Instances

For general information about instance migration, see[Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm). When the instance is migrated to new hardware, the Secure Boot keys and boot measurements are retaken on the new instance.
Note  
  
You cannot migrate a non-shielded instance to a shielded instance.

Shielded instances have the following limitations on instance migration.

### VM Instances
- Shielded instances do not support[live migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#live-migration)or[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#reboot). If you need to migrate a shielded instance, you must[manually migrate](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#manual)the instance.
- If you modified the UEFI secure boot variables, migration might not be possible, because the changes are not preserved during migration.
- If you have a VM instance that uses the TPM and you migrate the instance, the TPM data is not retained during migration. The new instance will have new PCR values.
- If you have Windows Defender Credential Guard enabled, instance migration is not supported.

### Bare Metal Instances
- Shielded instances do not support[live migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#live-migration)or[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#reboot). If you need to migrate a shielded instance, you must[manually migrate](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/movinganinstance.htm#manual)the instance.
- If you modified the UEFI secure boot variables, migration might not be possible, because the changes are not preserved during migration.
- If you enable the hardware TPM on a bare metal instance, the instance cannot be migrated, because the hardware TPM is not migratable.
- If you store your own secrets in a physical TPM on a bare metal instance, Oracle Cloud Infrastructure does not have a copy of the data in the TPM. After migrating the instance and then restarting it from a stopped state, you need to reset your software to work with the new physical TPM.

## Troubleshooting Validation Failures

If Secure Boot validation fails, you won't be able to SSH into your instance or the instance won't start. If Measured Boot validation fails, the Instance Details page displays a red shield.

If you get a Secure Boot failure, you might be able to find more details about the cause of the failure in the[serial console data](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/displayingconsole.htm). If you want to troubleshoot failures, do not terminate the instance . Note the instance's OCID and capture the serial console log files.

After a successful boot, a message similar to the following appears in the console history data:
```

```

If you have Secure Boot enabled and the signed firmware's signature is not correct, the instance does not start. If Secure Boot fails because the image is not signed or is invalid, a message similar to the following appears in the console history data:
```

```

If Secure Boot fails because an unsupported kernel was loaded, choose a supported kernel and try again. If an unsupported kernel was loaded, you won't be able to SSH into your instance, and a message similar to the following appears in the console history data:
```

```

If you have Measured Boot enabled and the boot sequence is not correct, the instance boots, but a red shield appears on the Instance Details page. If you have Measured Boot enabled and new PCR values have been added, the instance boots, and a yellow shield appears on the Instance Details page. If you get a Measured Boot failure and the PCR values are correct or if new values have been added, you can[reset the golden measurements](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded-instances-reset-measurements)
