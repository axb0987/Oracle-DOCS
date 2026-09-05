# Requesting and Receiving Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/requesting-and-receiving-devices.htm
- Fetched: 2026-09-05 03:02 CDT

# Requesting and Receiving Devices

Learn how to request and receive Roving Edge Compute, GPU, Storage, and Ultra devices.
Note  
  

Some OCI realms are eligible for self-provisioning where devices are shipped with a very small installer OS that enables you to self-provision the latest Roving Edge OS on-site. If you're not in an eligible realm, you receive a device with the Roving Edge OS preinstalled.

Task Description Links
1 Review device ordering requirements and usage guidelines.
- [Device Ordering Requirements](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/device_ordering_requirements.htm#DeviceOrderingRequirements)
- [Roving Edge Infrastructure Device Usage Guidelines](https://docs.oracle.com/en-us/iaas/Content/Rover/usage_guidelines.htm#DeviceUsageGuidelines)
2

Work with your Oracle account representative to have a Roving Edge device shipped to your location.

The representative provides you with a unique activation code. Save the code. You need the code to self-provision the device.

For Roving Edge Ultras: Depending on your OCI realm, the representative might not provide you with a unique activation code. If provided, save the code, otherwise, go to the next task.
3

(Before you receive the device)

Decide if you want to use the default generated self-signed certificate, or if you want to use another certificate management service such as the[OCI Certificate Management service](https://docs.oracle.com/iaas/Content/certificates/managing-certificate-authorities.htm).[Establishing the Certificate Authority for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/certificate_authority.htm#SettingPolicies)
4

(Before you receive the device)

Prepare your tenancy to support new devices:
- 

Identify or create compartments for the devices.
- Create IAM groups and policies for the devices. Even if you've previously configured Roving Edge policies, review the required policies. There's a new policy required for self-provisioning a device.
- [Identify or Create Compartments for Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/create-or-identify-compartments.htm#create-or-identify-compartments)
- [Create Required IAM Groups and Policies](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#policies)

Create a device node in your OCI tenancy for each device that you've requested.

Submit the node request to Oracle.
- 

For Roving Edge devices, see[Creating and Submitting a Node for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Node2/create_node2.htm#top).
- 

For Roving Edge Ultras, see the following sections:
- [Creating a Roving Edge Ultra Node](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/create_ultra.htm#top)
- [Submitting a Roving Edge Ultra Node Request](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/request_ultra.htm#top)
5 Receive the device.
6

Set up the device. This includes inspecting, cabling, connecting to a host, powering on, and self-provisioning the device.[Setting Up an Oracle Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/install-overview.htm#SettingUpDevices)
