# Overview of Oracle Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/overview.htm
- Fetched: 2026-09-05 03:02 CDT

# Overview of Oracle Roving Edge Infrastructure

Learn about the Roving Edge Infrastructure service and associated devices, including how it works and what it does.

Oracle Roving Edge Infrastructure is a cloud-integrated service that puts fundamental Oracle Cloud Infrastructure services where data is generated and consumed. Roving Edge Infrastructure devices provide high-performance computing, such as analytics, machine learning, and location-based services, and storage capabilities that operate with intermittent or no internet connectivity.

Roving Edge Infrastructure is the extension of your Oracle Cloud Infrastructure tenancy. You request to have virtual machines and objects from your tenancy loaded onto Oracle Cloud Infrastructure devices by creating and configuring Oracle Cloud Infrastructure device node resources in Oracle Cloud Infrastructure. These nodes function as requests for the corresponding devices, and also indicate what Oracle Cloud Infrastructure-based content is to be loaded on them. You can synchronize your object storage datasets with your Oracle Cloud Infrastructure tenancy after establishing an internet connection between the RED and your home Oracle Cloud Infrastructure region.

## How to Use Roving Edge Infrastructure

Common uses for Roving Edge Infrastructure include:
- 

Storage and processing of large volumes of images, video, audio, and internet of things (IoT) sensor data generated in environments where WAN connection is latent or unavailable. You can pre-process, filter, compress, and secure the data locally, then transfer it to Oracle Cloud Infrastructure where it can be further processed in the cloud.
- 

Compute and IO intensive applications, where low latency is paramount, such as tactical reconnaissance or 5G communications.
- 

Machine learning, where models trained in the cloud are running in disconnected locations to improve efficiency, intelligence and productivity.
- Remote computing requiring elevated security and airtight containment of data.
- Low-latency Oracle Database and Analytics workloads, with more Oracle applications optimized over time.
Note  
  

Ordering Oracle Roving Edge Infrastructure devices requires important terms and conditions to be understood and acknowledged before taking possession. Confirm that these terms and conditions have been included as part of your Oracle Cloud agreement. After Oracle validates your request, your Roving Edge Infrastructure devices are available for your possession.

## Roving Edge Infrastructure Device Options

The physical component is the Roving Edge Infrastructure device, which allows you to transport and establish your Oracle Cloud Infrastructure environment where you need it. Roving Edge Infrastructure device options consist of the following:
- 

Roving Edge device (RED) : A portable high-powered server that has been ruggedized to operate in remote and austere environments. These devices are highly portable and can be set up and taken down as needed.
- 

Roving Edge Ultra (Ultra) : A single device contained in a backpack-like transporter that an individual can carry. Ultra doesn't require a separate power source. A single person can operate Ultra in a remote or difficult environment where establishment of REDs isn't feasible. Ultra has less storage and computing capabilities than a RED.

The Roving Edge Infrastructure devices arrive preconfigured and ready for use. Just power the devices up, configure the network settings, and connect to your local network. You can synchronize object storage data between your Roving Edge Infrastructure devices and your Oracle Cloud Infrastructure tenancy.

## Roving Edge as Data Transfer Gateway

Roving Edge as Data Transfer Gateway is a seamless, efficient solution for managing data movement, synchronization, and storage across edge locations, on-premises systems, and Oracle Cloud Infrastructure (OCI). Designed to support diverse connectivity scenarios, it facilitates data transfers of up to 45 TB between edge environments, on-premises sites, and OCI Object Storage, whether through high-speed options such as OCI FastConnect or in environments with limited network bandwidth. With advanced features such as secure data synchronization and robust protocol support, including NFS v4.1, the gateway delivers reliable connectivity and strong data security. Optimized for both connected and disconnected use cases, the solution provides high performance local storage, enabling organizations to store and transfer data effortlessly and efficiently.

For more information, see[Roving Edge as Data Transfer Gateway (PDF)](https://www.oracle.com/a/ocom/docs/roving-edge-as-data-transfer-gateway.pdf).

## Navigating the Documentation

You can access the following topics in this document set:
- 

Overview topics
- 

[Roving Edge Infrastructure Concepts](https://docs.oracle.com/en-us/iaas/Content/Rover/key_concepts.htm#Concepts)
- 

[Accessing Roving Edge Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/access.htm#access)
- 

[Device Specifications](https://docs.oracle.com/en-us/iaas/Content/Rover/device_specifications.htm#DeviceSpecifications)
- 

OCI-Based Resource Management
- 

[Roving Edge Device Nodes](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/node_management.htm#NodeManagement)
- 

[Roving Edge Ultra Nodes](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/ultra_management.htm#UltraManagement)
- 

Device Management
- 

[Device Monitoring](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Monitoring/device_monitoring.htm#NodeManagement)
- 

[Identity and Access Management (IAM)](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/identity_management.htm#IAM)
- 

[Compute Virtual Machine Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/compute_management.htm#IAM)
- 

[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/object_storage_overview.htm#ObjectStorageOverview)
- 

[Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/block_volume_management.htm#BlockVolumeManagement)
- 

[Networking](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/networking_management.htm#NetworkingManagement)
- 

[Device Software Versions](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/device_software_management.htm#software_updates_0)
- 

[Events](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/event_management.htm#EventManagement)
- On-Device Service Management
- 

[Data Sync](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm#DataSyncTaskManagement)
- 

[Returning Devices to Oracle](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/returning_devices.htm#ReturnDevice)
- 

[Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Rover/troubleshooting.htm#troubleshooting)

## Device Ordering Prerequisites

This section describes prerequisites for requesting and using the Roving Edge Infrastructure service and its associated devices.

### Knowledge Requirements

Using the Roving Edge Infrastructure service and Roving Edge Infrastructure devices has the following knowledge requirements:
- 

Experience and understanding of Oracle Cloud Infrastructure services and features. Be comfortable creating and managing service resources such as compute instances, object storage buckets, and Identity and Access Management (IAM) tasks before ordering REDs.
- 

Expertise in hardware device integration, including cabling and switching.

### Oracle Cloud Infrastructure Requirements

Before you can order and set up REDs within your environment, you must perform the following prerequisite tasks:
- 

Have an Oracle Cloud Infrastructure tenancy.
- 

Determine whether you need a single RED or a Roving Edge Ultra to meet your needs.

### Limitations of Use

You have no right to use the hardware other than to use and receive the Roving Edge Infrastructure Services. The hardware includes the hardware equipment, including components and options. Oracle retains all title and ownership to the hardware. You may not sell, lease, or transfer the hardware to any third party.

You may not open the hardware or remove, modify, or tamper with any labels or tags (including without limitation, security labels) on the hardware.

You have the right to use the operating system delivered with the hardware subject to the terms of your order and any license agreement(s) delivered with the hardware.

You have no right to repair or replace the hardware. If the hardware is defective, contact Oracle for a replacement. See[Contacting Oracle Support](https://docs.oracle.com/en-us/iaas/Content/Rover/contacting_oracle_support.htm#ContactOracleSupport).

For a complete description of terms and conditions, review the terms and conditions provided in your Oracle Cloud agreement.
Note  
  

Ordering Oracle Roving Edge Infrastructure devices requires important terms and conditions to be understood and acknowledged before taking possession. Confirm that these terms and conditions have been included as part of your Oracle Cloud agreement. After Oracle validates your request, your Roving Edge Infrastructure devices are available for your possession.

## Differences from Oracle Cloud Infrastructure

Roving Edge Infrastructure differs from Oracle Cloud Infrastructure in the following ways:
- 

All Roving Edge Infrastructure users have administrator access.
- 

These items only have a single default option:
- 

Compartment
- 

Object storage namespace
- 

Availability domain
- 

Region
- 

Tenancy
- 

User group
- 

These Oracle Cloud Infrastructure features are not supported (and not limited to) on Roving Edge Infrastructure devices:
- 

Tagging
- 

Moving resources to a different compartment (only a single default compartment is available)
- 

Object storage replication
- 

Object storage retention rules
- 

Object storage bucket re-encryption
- 

iSCSI block volumes (default is paravirtualized)
- 

Getting namespace metadata details

## Tagging Resources

Apply tags to your Roving Edge Infrastructure resources to help organize them according to your business needs. You can apply tags at the time you create a resource, or you can update the resource later with the wanted tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
