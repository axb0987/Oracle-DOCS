# VMware Solution SDDC Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/clusters.htm
- Fetched: 2026-09-05 03:08 CDT

# VMware Solution SDDC Clusters

A cluster is a group of ESXi hosts and associated resources within a VMware Solution SDDC. Clusters segregate workloads and provide for future expansion to shapes that suit specific business needs.

For example, you might set up different clusters that meet different compliance requirements for different lines of business. Another example is setting up different clusters that contain shape types for specialized workloads or cost requirements.

When you create an SDDC, the first cluster created is always the management cluster. The management cluster contains all the resources necessary for the SDDC to function such as vCenter Server, NSX-T Manager Cluster and NSX-T Edge Nodes and services. A single set of management components is deployed for the whole SDDC. The unified management cluster can contain from 3 to 64 hosts and can also be used to host workloads.

Any clusters you create after the unified management cluster are workload clusters, and don't contain any management components. You can create up to 14 workload clusters. The number of ESXi hosts you can create in a workload cluster depends on the compute shape you select for the cluster. For dense shapes, you can have a maximum of 64 hosts. For standard shapes, you can have up to 32 hosts in the same cluster.
Create clusters during initial SDDC provisioning or at any time thereafter. All clusters in the SDDC are created in the Availability domain specified during the initial SDDC provisioning. ESXi host shapes, pricing interval, VLANs, and datastores are configured separately for each cluster in the SDDC.
Important  
  
Each cluster's resources are independent of the other clusters in the SDDC, so each cluster requires its own set of prerequisite resources. Before you create clusters in an SDDC, be sure you have all the resources you need.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

You can add more ESXi hosts to a cluster any time after provisioning. When you add a host to a cluster, the host's resources become part of the cluster. You can add an ESXi host of a different shape and billing interval than was initially specified for hosts during provisioning, as long as all shapes in the cluster have the same processor vendor. You can mix different shapes, billing intervals, and ESXi host software versions within a cluster to suit your business needs.

## Cluster Tasks

You can perform the following cluster tasks:

[Viewing Clusters in a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-list.htm)

[Adding a Cluster to a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-add.htm)

[Getting a VMware Solution SDDC Cluster's Details](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-get.htm)

[Editing a VMware Solution SDDC Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-edit.htm)

[Deleting a VMware Solution SDDC Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-delete.htm)
