# Concepts and Terminology
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/key_concepts.htm
- Fetched: 2026-09-05 03:02 CDT

# Concepts and Terminology

Describes Roving Edge Infrastructure concepts related to its features and functionality.

Be familiar with these concepts before setting up and using your Roving Edge Infrastructure service and devices.

## General
- 

Oracle Cloud Infrastructure (OCI) : The Infrastructure as a Service (IaaS) platform within which the Roving Edge Infrastructure and the other services operate.
- 

Oracle Cloud Console : The web browser-based user interface for interacting with Oracle Cloud Infrastructure.
- 

Command Line Interface (CLI) : The method of running the Oracle Cloud Infrastructure service features and functionality using text-based commands from a command prompt window.
- 

API : The method of running Oracle Cloud Infrastructure service features and functionality programmatically application programming interface (API) commands.
- 

Roving Edge Infrastructure Device Console : The web browser-based user interface for interacting with your Roving Edge Infrastructure device.

## Roving Edge Infrastructure

The following resources and concepts are related to the Roving Edge Infrastructure service and Roving Edge Infrastructure devices.
- 

Roving Edge Infrastructure : The Oracle Cloud Infrastructure service that allows you to operate cloud-based workloads outside of the data center.
- 

Roving Edge device (RED) : A high-powered and portable server that can run core IaaS services optimized for remote computing and storage.
- 

Roving Edge Ultra (Ultra) : A single battery-powered Roving Edge Infrastructure device capable of being carried by an individual. Ultra provides a highly-portable and rugged edge computing device you can use in indoor and outdoor environments. The device requires minimal protection from the elements, and is able to operate without consistent access to power. Ultra has less storage and computing capabilities than a traditional RED.
- 

Provisioning : The process of loading the required data on to the device and configuring the device with parameters that are specific to your environment.
- 

Node : The Roving Edge Infrastructure service resource in OCI that represents a single RED or Ultra device. See[Roving Edge Device Nodes](https://docs.oracle.com/en-us/iaas/Content/Rover/Node/node_management.htm#NodeManagement)and[Roving Edge Ultra Nodes](https://docs.oracle.com/en-us/iaas/Content/Rover/Ultra/ultra_management.htm#UltraManagement).
- 

Workload : The object storage bucket or compute custom image that's in your Oracle Cloud Infrastructure tenancy.
- 

Data Sync : Transmission of object storage data between buckets on your Roving Edge Infrastructure devices and your Oracle Cloud Infrastructure tenancy. This update allows you to synchronize data between the RED and Oracle Cloud Infrastructure cloud, and perform software updates. See[Data Sync Tasks](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).
- 

Device Software Version Management : The process of updating the operating system version of your device to a later version. You can also revert your device software to the previously-installed version. See[Device Software Versions](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/device_software_management.htm#software_updates_0).

## Identity and Access

The following identity and access resources have been optimized for use with Roving Edge Infrastructure:
- 

User : A user account that can access Roving Edge Infrastructure device features and functionality. See[Users](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User/user_management.htm#UserManagement).
- 

Group : A collection of users. Features and functionality applied to a group affects all member users. See[User Groups for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/Group/group_management.htm#GroupManagement).
- 

Policies : A document that specifies who can access which resources, and how. Access is granted at the group and compartment level, which means you can write a policy that gives a group a specific type of access within a specific compartment, or to the tenancy itself. See[Create Required IAM Groups and Policies](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_policies.htm#policies).

## Compute Virtual Machine

The following compute virtual machine (VM) resources have been optimized for use with Roving Edge Infrastructure:
- 

Instance : A virtual machine (VM) host running in a RED. See[Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance_management.htm#ComputeInstanceManagement).
- 

Image : A template of a virtual hard drive. The image determines the operating system and other software for an instance. See[Images](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/image_management.htm#ImageManagement).
- 

Shape : A template that determines the number of CPUs, amount of memory, and other resources that are allocated to an instance.
- 

Boot Volume : A detachable boot volume device that contains the image used to boot a compute instance. See[Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/boot_volume_management.htm#BootVolumeManagement).
- 

Console History Capture : The capture of serial console data for an instance. The data is useful for checking the status of the instance or diagnosing problems. See[Console History Capture](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Console_History/console-history_management.htm#ConsoleHistoryManagement).

## Object Storage

The following object storage resources have been optimized for use with Roving Edge Infrastructure:
- 

Bucket : A repository for storing objects in a compartment within an object storage namespace. See[Buckets](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/bucket_management.htm#BucketManagement).
- 

Object : A file or unstructured data you upload to a bucket. See[Objects](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/object_management.htm#ObjectManagement).

## Block Storage

The following block storage resources have been optimized for use with Roving Edge Infrastructure:
- 

Block Volume : A detachable block storage device that allows you to dynamically expand the storage capacity of an instance. See[Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/block_volume_management.htm#BlockVolumeManagement).

## Virtual Networking

The following virtual networking resources have been optimized for use with Roving Edge Infrastructure:

- 

Virtual Cloud Network (VCN) : A virtual, private network that you set up in Oracle data centers. See[Virtual Cloud Networks](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/vcn_management.htm#VCNManagement).
- 

Subnet : Subdivisions you define in a VCN (for example, 10.0.0.0/24 and 10.0.1.0/24). Subnets contain virtual network interface cards (VNICs), which attach to instances. See[Subnets](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/subnet_management.htm#SubnetManagement)
