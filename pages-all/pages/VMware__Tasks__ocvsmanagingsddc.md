# VMware Solution SDDCs
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm
- Fetched: 2026-09-05 03:09 CDT

# VMware Solution SDDCs

Learn how to create and manage SDDCs using Oracle Cloud Infrastructure VMware Solution.

The following types of SDDC configuration available:
- [Multi Host SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm#multi-host-SDDCs)
- [Single Host SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm#single-host-SDDCs)for testing and short-term development.

## Multi Host SDDCs

Multi host SDDCs provide high availability and you can use the full range of VMware Solution features to migrate and support production workloads.

You can create a multi host SDDC with up to 15 clusters, each containing up to 64 hosts. Each cluster can contain many ESXi hosts to support the specific workload requirements of the cluster. SDDCs require a unified management cluster to host the VMware management components, which is created as part of the SDDC setup workflow. See[About the VMware Software](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#aboutsoftware)for more information.

Any clusters you create after the unified management cluster are workload clusters, and don't contain any management components. The number of ESXi hosts you can create in a workload cluster depends on the compute shape you select for the cluster. See[Supported Shapes](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#shapes)for more information.

Each cluster in the SDDC has its own networking resources, which you define when you create the cluster. This lets you configure an SDDC that can meet segregated workload requirements. Workload mobility between clusters is allowed by default, but you can configure the Network Security Group (NSG) settings for each cluster VLAN to restrict workload mobility. See[VLANs](https://docs.oracle.com/iaas/Content/VMware/Tasks/ocvsmanagingl2net.htm)for more information.

When you create a cluster, you define a shape to use for the provisioning of ESXi hosts in the cluster. All the hosts are provisioned using that shape. After the cluster is provisioned, you can add hosts of different shapes, as long as all shapes in the cluster have the same processor vendor. The VMware software version is defined for the whole SDDC, but you can select different minor versions for each cluster. See[Defining Clusters](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#defining-clusters)for more information.

When you provision an SDDC and define its initial clusters, you select a pricing interval for each cluster. The pricing interval for a cluster applies to all hosts in the cluster. Different clusters can have different pricing intervals. Any clusters you add to the SDDC after initial provisioning can also have its own selected pricing interval. So you can have several clusters, all with different pricing intervals, and different shapes within a cluster. See[Billing Options](https://docs.oracle.com/iaas/Content/VMware/Concepts/billing-options.htm)for more information.

## Single Host SDDCs

Single host SDDCs are used for testing and short-term development. A single host SDDC consists of a single unified management cluster with a single EXSi host. The host is created using a OCI bare metal dense shape instance. A single host SDDC is created with a subnet and VLANs in an OCI VCN.
Use cases for a single-host SDDC:
- Faster onboarding for proof-of-concept, or testing and development.
- Migration between on-premises and OCI VMware Solution using VMware HCX, VMware vMotion for live migration, and cold migration.
- Disaster Recovery Evaluation with VMware Site Recovery (SRM) optimized for OCI VMware Solution. VMware SRM is bought separately.
- Hybrid Linked Mode support for a single view of on-premises and OCI VMware Solution resources.
- High-bandwidth, low-latency access to other Oracle services.

Limitations and Considerations for Single Host SDDCs:
- Standard shapes aren't supported.
- Production workloads aren't supported.
- No OCI supported service-level agreement (SLA) is provided.
- Oracle support is limited to commercially reasonable support. VMware support is available only for the first 60 days for a single-node SDDC deployment.
- Single host SDDCs don't expire, but they're limited to the Hourly and Monthly billing options. For more information, see[Billing Options](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#ocvsoverview_topic_billing_options).
- Single host SDDCs aren't designed as long-term solutions. If you require a long-term SDDC, you can migrate workloads to a new production SDDC using HCX. See[HCX License Types](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#aboutsoftware__hcx-license-types)for more information.
- Single host SDDCs can't be upgraded to a multiple-cluster SDDC.
- Single host SDDCs aren't backed up. If the host fails, the data is lost.
- You're limited to a global maximum of 10 single-host SDDC deployments across all tenancies and regions.
- Features that require more than one host don't work. For example:
- Distributed management components
- High-availability (HA) for VMware clustering
- Distributed Resource Management (DRM) for VMware clustering

## SDDC Tasks

You can perform the following SDDC tasks:

[Listing VMware Solution SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-list.htm)

[Creating a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm)

[Getting a VMware Solution SDDC's Details](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-get.htm)

[Editing an VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-update.htm)

[Moving a VMware Solution SDDC Between Compartments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm)

[Upgrading a VMware Solution SDDC's HCX License](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-upgrade-hcx.htm)

[Downgrading a VMware Solution SDDC's HCX License](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-downgrade-hcx.htm)

[Canceling a VMware Solution SDDC's HCX License Downgrade](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm)

[Upgrading a VMware Solution SDDC's Software](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/upgrade.htm)

[Deleting a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm)
