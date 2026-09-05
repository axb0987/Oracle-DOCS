# Microsoft Licensing on Oracle Cloud Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm
- Fetched: 2026-09-05 01:49 CDT

# Microsoft Licensing on Oracle Cloud Infrastructure

This topic provides information about the licensing requirements to use Microsoft products on Oracle Cloud Infrastructure. Oracle provides two options for using Windows Server licenses, OCI provided, and Microsoft bring your own license (BYOL).
Important  
  
Microsoft bring your own license is not available on Free Tier or trial tenancies.

## Using Microsoft Products on OCI

Oracle Cloud Infrastructure is licensed to provide Microsoft software offerings. Oracle is a member of the[Microsoft Partner Network](https://partner.microsoft.com), licensed to sell Microsoft software under the Service Provider License Agreement (SPLA). Oracle is also an authorized Microsoft Authorized Mobility Partner.

For the latest Microsoft licensing requirements, refer to the[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/).

If you can't find the answer to your question here, or you need more assistance running Microsoft products on Oracle Cloud Infrastructure, contact[Oracle Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup_topic-Sign_Up_for_Free_Oracle_Cloud_Promotion.htm).

## Using Microsoft Windows Server Licenses on OCI

For Microsoft Windows Server on OCI, you can choose Microsoft BYOL or use an OCI provided Windows Server license. OCI Provided OCI provides the Windows Server licenses for the compute instance for a fee. See the[Oracle Cloud Price List: Operating Systems](https://www.oracle.com/cloud/price-list/#compute-os)for prices. Microsoft Bring Your Own License

With Microsoft BYOL, OCI customers can take advantage of their Microsoft Flexible Virtualization Benefit by using their own Microsoft Server subscription licenses or Software Assurance licenses. With this benefit, customers are no longer limited to dedicated hosts, now customers can leverage BYOL on shared infrastructure in the cloud. Converting from an OCI Provided license to a Microsoft Bring Your Own License will require customers to activate their own licenses. For more information on the Flexible Virtualization Benefit see:[Using software products under the Flexible Virtualization Benefit](https://www.microsoft.com/licensing/docs/documents/download/Flexible_Virtualization_Benefit_licensing_guidance.pdf).

All Microsoft licenses used at OCI must comply with the terms provided by Microsoft as described here:[Microsoft Licensing Use Rights](https://www.microsoft.com/licensing/docs/view/Licensing-Use-Rights).

For instructions on how to launch instances with Windows Server, see:[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm).

For instructions on how to change your Windows Server license type, by selecting either OCI Provided or Microsoft Bring Your Own License, see:[Changing the Windows License Type of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/changewinlicense.htm).

### OCI License Models

The following table describes the licensing models that are available for using Microsoft Windows Server images on OCI.

Image License Additional Requirements
[Platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm)
- OCI provided
- Microsoft BYOL

VM instances on a shared host and VM instances launched on a dedicated host are permitted.

Bare metal instances.

For Microsoft BYOL, verify eligibility under the Flexible Virtualization Benefit.
[Bring your own image (BYOI)](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm)
- OCI provided
- Microsoft BYOL

VM instances on a shared host and VM instances launched on a dedicated host are all permitted.

For Microsoft BYOL, verify eligibility under the Flexible Virtualization Benefit.
[Bring your own Hyper-V](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#hypervisor)
- Issued by Oracle

Instances must be launched on a dedicated host.

[Create a bare metal instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm)using the[Windows Server Datacenter platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm). Then, copy your on-premises guest OS to Hyper-V on the bare metal instance.

### Microsoft Windows Server Licensing FAQ

[What is Microsoft BYOL?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Microsoft bring your own license (BYOL) lets you use Microsoft Server software licenses that you already own to deploy software on Oracle Cloud Infrastructure, without any additional licensing fees.

Customers provide their own Microsoft Server subscription licenses or Software Assurance licenses and can use the new Flexible Virtualization Benefit. With the new benefit, customers are no longer limited to deploying on dedicated hosts, now customers can deploy to shared services in the cloud. The new benefit applies broadly to all products including Windows Server, desktop applications, developer tools and other server applications. For more information on the Flexible Virtualization Benefit see:[Using software products under the Flexible Virtualization Benefit](https://www.microsoft.com/licensing/docs/documents/download/Flexible_Virtualization_Benefit_licensing_guidance.pdf).

[What OS editions of Microsoft Windows Server are supported?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Platform images

These Windows Server versions are available for[platform images:](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm)
- Windows Server 2016: Datacenter, Standard, Standard Core
- Windows Server 2019: Datacenter, Standard, Standard Core
- Windows Server 2022: Datacenter, Standard, Standard Core

Bring Your Own Image (BYOI)

These Windows versions support custom image import:
- Windows Server 2016: Datacenter, Standard, Standard Core
- Windows Server 2019: Datacenter, Standard, Standard Core
- Windows Server 2022: Datacenter, Standard, Standard Core
- Windows Server 2025: Datacenter, Standard, Standard Core

[Is Windows Server 2025 available as a platform image?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, Windows Server 2025 is available as a[platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm).

[Is Windows Server 2022 available as a Bring Your Own Image (BYOI) image?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, you can import your own Windows Server 2022 image for virtual machines only. For source image requirements and steps to import an image, see[Importing Custom Windows Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/importingcustomimagewindows.htm).

[Does Oracle Cloud Infrastructure support Bring Your Own Image (BYOI) for Windows Server?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, you are permitted to import your own generalized custom image of Windows Server.

[How am I charged for Windows Server on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

The cost of a Microsoft Windows Server license is an additional cost, on top of the underlying compute instance price. You pay separately for the compute instance and the Windows Server license. For more information about Microsoft Windows Server pricing, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html).

Billing for the Windows Server license is based on per-OCPU, per-second usage. Billing starts when an instance is in the "running" state and ends when you[terminate (delete) the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/terminatinginstance.htm).

When an[instance is stopped](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/restartinginstance.htm), billing for the Windows Server license depends on the[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)that was used to create the instance. Billing pauses for instances that use a Standard shape or a shape in the VM.GPU.A10 series. Billing continues for instances that use a Dense I/O shape, HPC shape, or any other GPU shape.

Depending on the shape, you might also be[billed for the underlying compute instance when the instance is stopped](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/resource-billing-stopped-instances.htm).

For Microsoft BYOL licensing, you will not be charged. See[Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm).

[How does Windows Server get updated with the latest patches?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

You must[update your VCN's security list](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)to enable egress traffic for port 80 (HTTP) and port 443 (HTTPS) to install patches from Microsoft. Oracle Cloud Infrastructure enables automatic updates for Microsoft Windows Server and uses the default settings for applying Windows Server patches.

[Can I take a snapshot image after customizing a running Window Server instance?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, there are several options available:
- [Create a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/windowsimages.htm): Creates a custom image that you can use to launch other instances. Instances that you launch from your image include the customizations, configuration, and software installed when you created the image.
- [Clone a boot volume](https://docs.oracle.com/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm): Makes a copy of an existing boot volume without needing to go through the backup and restore process. A boot volume clone is a point-in-time direct disk-to-disk deep copy of the source boot volume, so all the data that is in the source boot volume when the clone is created is copied to the boot volume clone.
- [Back up a block volume](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm): Makes a point-in-time backup of data on a block volume. You can restore a backup to a new volume either immediately after a backup or at a later time that you choose.
- [Back up a boot volume](https://docs.oracle.com/iaas/Content/Block/Tasks/create-bv-boot-volume-backup.htm): Makes a backup of a boot volume. Boot volume backup capabilities are the same as block volume backup capabilities and are in-region only. Windows boot volume backups cannot be copied across regions.

[Can I export a custom Windows Server image?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, exporting custom Windows Server operating system images is supported.

When exporting Windows-based images, you are responsible for complying with the[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/)and all product use conditions, as well as verifying your compliance with Microsoft.

For steps to export an image, see[Importing and Exporting Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/imageimportexport.htm).

[What support is available for Microsoft Windows Server on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

[Oracle Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)provides limited assistance for Microsoft Windows Server platform images if the Windows Server version has not reached end of support with Microsoft. All other Microsoft software is supported directly by[Microsoft Support](https://support.microsoft.com/).

Oracle Support can help verify that the operating system boots, that the operating system connects to the network, and that attached storage connects and performs as expected. If you encounter other issues with Microsoft Windows Server, work directly with Microsoft Support to resolve the issue. For more information, see[Support Options for Microsoft Windows](https://docs.oracle.com/en-us/iaas/Content/Compute/References/support_options_microsoft.htm).

[How do I upgrade to a newer version of Windows Server?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

To upgrade to a newer version of Windows Server, you can do either of the following things:
- Obtain the installation media from Microsoft or your Microsoft reseller, and then upgrade the existing compute instance. The license issued by Oracle Cloud Infrastructure remains in effect.
- Create a new compute instance using the desired version of the Windows Server platform image, and then migrate your applications and data to the new instance.

[Can I change the license type of an instance based on a custom image that was incorrectly marked as Linux?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes. Follow these steps change to a Windows Server license from a Linux custom image.
- Open the navigation menu and select Compute . Under Compute , select Custom Images .
- Click the custom image that you're interested in.
- Under Custom image information locate the Operating system field.
- Click Edit . The Edit operating system dialog is displayed.
- Select Windows .

Next:
- Select the Windows version.
- Certify that you are following Windows license requirements.
- 

Click Save changes .
Important  
  
After saving the changes, follow these steps to complete the change.
- Navigate back to the instance details page.
- Wait a couple of minutes for the change to take effect on instance detail page.
- Then edit the instance's Windows Server license as described here:[Changing the Windows License Type of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/changewinlicense.htm)

[Are there user data capabilities when launching Windows Server images?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes,[Windows Server platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm)include cloudbase-init installed by default. You can use cloudbase-init to run PowerShell scripts, batch scripts, or other user data content on instance launch. Cloudbase-init is the equivalent of cloud-init on Linux-based images.

[Can I use Windows Remote Management on OCI?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, Microsoft Windows Remote Management (WinRM) is enabled by default on[Windows Server platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm). WinRM enables you to remotely manage the operating system.

[What is Microsoft end of support?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Microsoft establishes the support lifecycle policy for its products. When a product reaches the end of its support lifecycle, Microsoft no longer provides security updates for the product. You should upgrade to the latest version to remain secure.

[Can I use Windows Server 2012 R2 even though it's past the end-of-support date?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Windows Server 2012 R2 reached the[end of its support life cycle](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#lifecycle)on October 10, 2023. Although you can continue to import your own Windows 2012 R2 images and run your existing instances, you are at a higher risk of security issues, incompatibility, or failures. Oracle does not provide any operating system support for end-of-support operating systems. See[Operating System Lifecycle and Support Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#lifecycle)

OCI does not provide new platform images after the end-of-support date. However, you can import your own image and launch it on a shared host VM.

There are no restrictions to running end-of-support operating systems on bare metal machines on a dedicated host. You may bring your own image (BYOI) of a Windows Server 2012 R2 image, but you must import a custom OS image and run the image on a dedicated host.

[Can I purchase Microsoft Extended Security Updates for end-of-support Windows Server OSs?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, you can purchase Extended Security Updates (ESUs) from Microsoft for use on Oracle Cloud Infrastructure.

For VMs on shared infrastructure, you must have an enterprise agreement in place with Microsoft. With that agreement in place, you can purchase ESUs per virtual core matching the number of OCPUs per VM instance, with a minimum requirement of 16 virtual core licenses per VM instance.

For bare metal machines, you must have an enterprise agreement in place with Microsoft. With that agreement in place, you can purchase ESUs per physical core of the dedicated bare metal host.

Oracle Cloud Infrastructure cannot purchase ESUs on your behalf.

You are fully responsible for purchasing the correct number of ESUs for your instances. Oracle Cloud Infrastructure does not keep track of whether you have enough ESUs.

## Using Other Microsoft Software Licenses on OCI

With Microsoft BYOL, you can bring your own license for Microsoft software licenses subject to the[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/)and[Microsoft Flexible Virtualization Benefit](https://www.microsoft.com/licensing/docs/documents/download/Flexible_Virtualization_Benefit_licensing_guidance.pdf). You are responsible for managing your own licenses to maintain compliance with Microsoft licensing terms.

The following table shows the BYOL requirements for Microsoft Software licenses on Oracle Cloud Infrastructure.

Microsoft License Bare Metal Machines and Dedicated Virtual Machine Hosts Virtual Machines (Multi-Tenant Shared Host)

SQL Server

Subject to the Microsoft Product Terms

Eligible 1

Eligible 1
Visual Studio (MSDN)

Eligible

Non-production use only.

Eligible

Non-production use only.
Microsoft 365 Apps for enterprise (Office 365 ProPlus) and Office Professional Plus

Eligible 1 Eligible 1
Windows 7, Windows 8, and Windows 10, Windows 11

Eligible 1 Eligible 1
Other Microsoft applications

Eligible 1

Subject to the Microsoft Product Terms.

Eligible 1

You must have License Mobility through Software Assurance.

1 Direct questions about your licensing rights to Microsoft or your Microsoft reseller. You are responsible for verifying eligibility.

### Other Microsoft Software Licensing FAQ

[Is Oracle a Microsoft Authorized Mobility Partner?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, Oracle is an Authorized Mobility Partner.

[What other Microsoft applications can I bring to OCI?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Any Microsoft Server licenses permitted on Oracle Cloud Infrastructure must be eligible according to the latest[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/). It is your responsibility to verify that the licensing agreements with Microsoft permit you to bring on-premises perpetual Microsoft licenses to Oracle Cloud Infrastructure (see:[Microsoft Flexible Virtualization Benefit](https://www.microsoft.com/licensing/docs/documents/download/Flexible_Virtualization_Benefit_licensing_guidance.pdf)) and are eligible licensed products according to the latest[Microsoft Product Terms](https://www.microsoft.com/licensing/terms/).

[How does pricing work for Microsoft SQL Server?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Important  
  
Please ensure you understand the minimum billing requirement before launching a Microsoft SQL Server instance.

Charges for Windows Server and Oracle Cloud Infrastructure Compute instances apply separately. Billing continues for Microsoft SQL Server Standard, whether it is stopped or terminated, until the minimum is reached. Compute Instance and Windows Server License billing halts when an instance is stopped or terminated. Minimum 744 Hours Billing Requirement

If the Microsoft SQL Server instance is terminated within 744 hours of launch, billing for Microsoft SQL Server Standard or Enterprise continues until 744 hours are reached. The billing stops for the Compute instance and Windows Server License when the instance is stopped or terminated. Billing for boot or block volume storage stops when the instance is terminated. If multiple instances are terminated within 744 hours of launch, billing for Microsoft SQL Server Standard or Enterprise will continue for each instance until 744 hours are reached. The minimum 744 hour service applies and continues each time a Microsoft SQL Server Standard or Enterprise instance is scaled up or down. Beyond the 744 hour minimum service term billing for Microsoft SQL Server Standard or Enterprise is hourly.
Important  
  
In effect, if you launch a Microsoft SQL Server instance you are billed for 744 hours of usage. Even if the instance is terminated immediately, you are still billed for 744 hours of usage.

Total minimum Microsoft SQL Server Standard charges per each instance can be calculated as follows:`Per hour price from Marketplace listing * Num OCPUs in Instance * 744`.

[Does my OCI Marketplace Microsoft SQL Enterprise license give me access to Power BI?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

The Microsoft SQL Enterprise listing in the Oracle Cloud Infrastructure Marketplace does not include licenses for Power BI. Oracle's reseller agreement doesn't allow Power BI licenses to be included with Microsoft SQL Enterprise.

You can purchase Power BI licenses in the Oracle Cloud Infrastructure Marketplace separately from Microsoft SQL Enterprise.

[Can I use my Visual Studio (MSDN) license on Microsoft Windows Server on OCI?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Yes, you can use your Visual Studio (MSDN) subscription license for non-production purposes on Oracle Cloud Infrastructure on either bare metal or virtual machine instances. You are responsible for complying with the Visual Studio subscription terms.

[Can I buy a Visual Studio (MSDN) subscription from OCI?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

No, Oracle does not sell Visual Studio (MSDN) subscriptions. Contact Microsoft or your Microsoft reseller.

[Can I use a Visual Studio (MSDN) license for a production environment?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

No, Visual Studio (MSDN) subscription licenses are for development, testing, or demonstration purposes only.

[How can I remote access to a Windows Server instance on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#)

Follow the steps to[connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/connect-to-windows-instance.htm). Windows operating systems permit remote access for a maximum of two users using Remote Desktop Services (RDS) for Administration purposes.
