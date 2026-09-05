# Creating Windows Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/windowsimages.htm
- Fetched: 2026-09-05 01:49 CDT

# Creating Windows Custom Images

You can create a Windows custom image of a bare metal or virtual machine (VM) instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image. For information about custom images, see[Managing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/managingcustomimages.htm). For information about the licensing requirements for Windows images, see[Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm).

Windows supports two kinds of images: generalized and specialized. Generalized images are images that have been cleaned of instance-specific information. Specialized images are point-in-time snapshots of the boot disk of a running instance, and are useful for creating backups of an instance. Oracle Cloud Infrastructure supports bare metal and VM instances launched from both generalized and specialized custom Windows images.

Generalized images

A generalized image has a generalized OS disk, cleaned of computer-specific information. The images are generalized using Sysprep. Generalized images can be useful in scenarios such as quickly scaling an environment. Generalized images can be configured to preserve the existing`opc`user's account, including the password, at the time the image is created, or configured to recreate the`opc`user account, including generating a new, random password that you retrieve using the API. For background information, see[Sysprep (Generalize) a Windows installation](https://docs.microsoft.com/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation).

Specialized images

A specialized image has an OS disk that is already fully installed, and is essentially a copy of the original bare metal or VM instance. Specialized images are intended to be used for backups so that you can recover from a failure. Specialized images are useful when you are testing a task and may need to roll back to known good configuration. Specialized images are not recommended for cloning multiple identical bare metal instances or VMs in the same network because of issues with multiple computers having the same computer name and ID. When creating a specialized image, you must remember the`opc`user's password; a new password is not generated when the instance launches, and it cannot be retrieved from the console or API.

## Creating a Generalized Image

Caution  
  

- Creating a generalized image from an instance will render the instance non-functional, so you should first create a custom image from the instance, and then create a new instance from the custom image. The following steps describe how to do this. This is the instance that you'll generalize. Or, you can make a backup image of the instance that you can use to launch a replacement instance if needed.
- If you upgrade to PowerShell 5.0/WMF 5.0, you might encounter an issue where Sysprep fails, which prevents the image generalization process from completing. If this occurs, you might not be able to log into instances launched from the custom image.
- [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/connect-to-windows-instance.htm)by using a Remote Desktop connection and shut down the instance from the operating system.
- Create the new image using[Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/custom-images-create.htm).
- Create an instance from the new image using[launching an instance from a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks).
- [Connect to the new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/connect-to-windows-instance.htm)using a Remote Desktop client.
- 

Download the Windows Sysprep generalize file to the instance:
- File link:[oracle-cloud_windows-server_generalize_2026-01-23.SED.EXE](https://objectstorage.us-ashburn-1.oraclecloud.com/p/BGzkwZTVKefaDNpnTR4TEeMYEWU82n9Z4MFePVr3PGLeBm8bnQ8oMPTIxh0c4S-T/n/imagegen/b/images/o/oracle-cloud_windows-server_generalize_2026-01-23.SED.EXE)
- Right-click the file, and then select Run as administrator .
- 

Extract the files to C:\Windows\Panther . The following files are extracted into the Panther folder for all Windows Server versions:
- Generalize.cmd
- Specialize.cmd
- unattend.xml
- Post-Generalize.ps1
- 

Optional: If you want to preserve the`opc`user account, edit`C:\Program Files\bmcs\imageType.json`and change the`imageType`setting to`custom`. A new password is not created and the password is not retrievable from the console or API.

If you want to configure the generalized image to recreate the`opc`user account when a new instance is launched from the image, leave the`imageType`setting defaulted to`general`. You can retrieve the new account's password through the API using[GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials).
- 

Right-click Generalize.cmd , and then select Run as administrator . Keep in mind the following outcomes of running this command:

- Your connection to the Remote Desktop client might immediately be turned off and you will be signed out of the instance. If this does not occur, you should log out of the instance yourself.
- Because`sysprep generalize`turns off Remote Desktop, you won't be able to sign in to the instance again.
- Creating a generalized image essentially destroys the instance's functionality.

You should wait for a few minutes before proceeding to the following step to ensure the generalization process has completed.
- Create the new image using[Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/custom-images-create.htm).
- After you create an image from an instance that has been generalized, we recommend that you terminate the instance. Although it might appear to be running, it won't be fully operable.

## Creating a Specialized Image

Important  
  
When creating a specialized image, you must remember the`opc`user's password. It cannot be retrieved from the Console or API.

You create a specialized image the same way you create other custom images. For steps, see[Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/custom-images-create.htm)
