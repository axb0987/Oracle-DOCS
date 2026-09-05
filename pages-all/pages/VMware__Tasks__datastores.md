# VMware Solution Datastore Management
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastores.htm
- Fetched: 2026-09-05 03:08 CDT

# VMware Solution Datastore Management

Use VMware Solution Datastore Management to configure datastores and manage related block volumes that are located in OCI.

Datastore Management serves as a bridge between OCI and Oracle Cloud VMware Solution representations of your environment. It provides a unified interface, helping you to manage datastores and datastore clusters more efficiently. The feature is intended for VMware Solution users who use the Block Volume service as VMFS datastores, providing a more simplified and automated approach to block volume management.

Datastore Management is the recommended way to create and manage datastores and datastore clusters for your OCVS SDDC. Previously, attaching and detaching block volumes to Compute instances required manual steps, but now you can perform these operations more efficiently through Datastore Management. Datastores act as logical entities that organize block volumes, and this feature allows you to attach block volumes to multiple Compute instances in OCI, streamlining the provisioning process. It also provides a unified view of block volume locations, giving you a more comprehensive understanding of your infrastructure and eliminating the need to switch between different services and screens.

You can perform the following tasks for datastore management associated with VMware Solution:
- [Managing Datastores](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastores-managing.htm)
- [Managing Datastore Clusters](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-clusters-managing.htm)

## Datastore Management Limits

Datastore Management manages only the OCI side of block storage management. It doesn't manage block storage management in vCenter.

## Permissions
