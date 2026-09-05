# Overview of Oracle Cloud VMware Solution
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm
- Fetched: 2026-09-05 03:07 CDT

# Overview of Oracle Cloud VMware Solution

Use Oracle Cloud VMware Solution to create and manage VMware enabled software-defined data centers (SDDCs) in OCI.

## Solution Highlights

Oracle Cloud Infrastructure VMware Solution gives you access to the following features:
- vSphere Enterprise Plus

vSphere is VMware's virtualization platform for unified management of the SDDC's CPU, storage, and networking infrastructure. Two key components of vSphere are ESXi hypervisor and vCenter Server. For details about the platform, see[VMware's vSphere documentation](https://www.vmware.com/products/cloud-infrastructure/vsphere).
- NSX DC Advanced

For information about NSX 3.2.x see[Product offerings for VMware NSX-T Data Center 3.2.x](https://kb.vmware.com/s/article/86095).

For information about NSX 4.0 and above see[VMware NSX Features](https://docs.vmware.com/en/VMware-NSX/4.0/nsx-feature-and-edition-guide/GUID-1D808019-7BCC-4A47-B8CA-BC0993E36EBF.html).
- [vSAN Advanced with Encryption](https://core.vmware.com/resource/vmware-vsan-technology-overview)
- HCX Advanced (Can be upgraded to HCX Enterprise on demand)

Benefits of Oracle Cloud Infrastructure VMware Solution include:
- High availability : All VMware components are distributed across different fault domains within the OCI region's availability domains.
- Scalability : Using dense shapes, you can start with 3 ESXi hosts and scale up to 64 hosts in a single ESXi cluster. If you use standard shapes, you can start with 3 ESXi hosts and scale up to 32 hosts in a single ESXi cluster within the SDDC.
- Define clusters : Define up to 15 vSphere clusters in an SDDC. Use clusters to segregate workloads and provide for future expansion.
- Lift and shift : Migration of on-premises VMware workloads to a VMware Solution SDDC is seamless.
- Full integration : Because the SDDC resides in a virtual cloud network (VCN), it can be configured to communicate with other OCI resources such as compute instances, DB systems and Autonomous AI Databases, and so on.
- Manageability : The OCI Console provides workflows to help SDDC creation and networking configuration.
- Layer 2 networking : SDDCs are configured with VLANs, which support applications that need layer 2 networking to run in the public cloud.
Note  
  
"Bring your own hypervisor" deployment of ESXi on bare metal compute instances isn't supported.

## SDDC Details

The following types of SDDC configuration are available:
- [Multi Host SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#multi-host-SDDCs)
- [Single Host SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#single-host-SDDCs). These are typically used for testing and short-term development.

### Multi Host SDDCs

Multi host SDDCs provide high availability and you can use the full range of VMware Solution features to migrate and support production workloads.

You can create a multi host SDDC with up to 15 clusters, each containing up to 64 hosts. Each cluster can contain many ESXi hosts to support the specific workload requirements of the cluster. SDDCs require a unified management cluster to host the VMware management components, which is created as part of the SDDC setup workflow. See[About the VMware Software](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#aboutsoftware)for more information.

Any clusters you create after the unified management cluster are workload clusters, and don't contain any management components. The number of ESXi hosts you can create in a workload cluster depends on the compute shape you select for the cluster. See[Supported Shapes](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#shapes)for more information.

Each cluster in the SDDC has its own networking resources, which you define when you create the cluster. This lets you configure an SDDC that can meet segregated workload requirements. Workload mobility between clusters is allowed by default, but you can configure the Network Security Group (NSG) settings for each cluster VLAN to restrict workload mobility. See[VLANs](https://docs.oracle.com/iaas/Content/VMware/Tasks/ocvsmanagingl2net.htm)for more information.

When you create a cluster, you define a shape to use for the provisioning of ESXi hosts in the cluster. All the hosts are provisioned using that shape. After the cluster is provisioned, you can add hosts of different shapes, as long as all shapes in the cluster have the same processor vendor. The VMware software version is defined for the whole SDDC, but you can select different minor versions for each cluster. See[Defining Clusters](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm#defining-clusters)for more information.

When you provision an SDDC and define its initial clusters, you select a pricing interval for each cluster. The pricing interval for a cluster applies to all hosts in the cluster. Different clusters can have different pricing intervals. Any clusters you add to the SDDC after initial provisioning can also have its own selected pricing interval. So you can have several clusters, all with different pricing intervals, and different shapes within a cluster. See[Billing Options](https://docs.oracle.com/iaas/Content/VMware/Concepts/billing-options.htm)for more information.

### Single Host SDDCs

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

## Defining Clusters

A cluster is a group of ESXi hosts and associated resources within an SDDC. Clusters segregate workloads and provide for future expansion to shapes that suit specific business needs. For example, you might set up different clusters that meet different compliance requirements for different lines of business. Another example is setting up different clusters that contain shape types for specialized workloads or cost requirements.

When you create an SDDC, the first cluster created is always the management cluster. The management cluster contains all the resources necessary for the SDDC to function such as vCenter Server, NSX-T Manager Cluster and NSX-T Edge Nodes and services. A single set of management components is deployed for the whole SDDC. The unified management cluster can contain from 3 to 64 hosts and can also be used to host workloads.

Any clusters you create after the unified management cluster are workload clusters, and don't contain any management components. You can create up to 14 workload clusters. The number of ESXi hosts you can create in a workload cluster depends on the compute shape you select for the cluster. For dense shapes, you can have a maximum of 64 hosts. For standard shapes, you can have up to 32 hosts in the same cluster. You can have a total of 64 hosts in an SDDC.
Create clusters during initial SDDC provisioning or at any time thereafter. All clusters in the SDDC are created in the Availability domain specified during the initial SDDC provisioning. ESXi host shapes, pricing interval, VLANs, and datastores are configured separately for each cluster in the SDDC.
Important  
  
Each cluster's resources are independent of the other clusters in the SDDC, so each cluster requires its own set of prerequisite resources. Before you create clusters in an SDDC, be sure you have all the resources you need.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

You can add more ESXi hosts to a cluster any time after provisioning. When you add a host to a cluster, the host's resources become part of the cluster. You can add an ESXi host of a different shape and billing interval than was initially specified for hosts during provisioning, as long as all shapes in the cluster have the same processor vendor. You can mix different shapes, billing intervals, and ESXi host software versions within a cluster to suit your business needs.

Cluster 1 Clusters 2 to 15
Type Management and workload Workload
Shapes
- You can use any supported shape or processor family.
- Defaults to the shape selected in Cluster 1, but you can change it to any supported shape.
Cores The number of cores you can configure depends on the shape you select.
- You can configure a higher or lower number of cores than specified in Cluster 1.
- The number of cores you can configure depends on the shape you select.
Number of ESXi Hosts
- 3 to 32 standard shape hosts, constrained by tenancy limits.
- 3 to 64 dense shape hosts, constrained by tenancy limits.
- Single host SDDCs contain only one cluster with one ESXi host.
- Up to 32 standard shape hosts, constrained by tenancy limits.
- Up to 64 dense shape hosts, constrained by tenancy limits.
- Single host SDDCs contain only one cluster with one ESXi host.
Billing interval
- Any billing interval supported by the selected shape
- Defaults to the interval selected in Cluster 1, but you can change it to any interval supported by the selected shape.
Software
- Select any VMware software bundle supported by the selected shape.
- VMware software licensing is the same for all clusters in the SDDC.
Networking
- You can use existing VLANs or set them up during SDDC provisioning.
- You can use the same VLANs for all clusters, or create new VLANs for each cluster.
Storage
- Depends on the selected shape. See[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#supported-shapes).
- Depends on the selected shape. See[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#supported-shapes).
- You can create and attach more block volume storage at any time.

## Supported Shapes

VMware Solution supports standard, dense, and NVIDIA GPU shapes for ESXi hosts. Each shape type has different benefits and limitations to consider when planning a SDDC. When you create a workload cluster, the number of allowed ESXi hosts in the cluster depends on the shape you select. See each shape section for details.

### Dense Shapes

- You can have a maximum of 64 dense shape hosts in a cluster.
- Dense shapes include local NVMe storage that are used for vSAN Datatstore.
- vSAN converged storage technology replicates data across all the ESXi hosts in the SDDC.
- All pricing commitment types and HCX license types are available for Dense shapes.
- Dense shapes can be deployed across several Availability domains (Multi-AD).
- You can use a dense shape to create a single-node SDDC.

The following table shows supported Dense shape configurations available for provisioning:

Processor Type Shape OCPU Available Core Configurations Memory (GB) Network Bandwidth Limit (Gbps) Minimum VMware version
Intel BM.DenseIO2.52 52 52 768 2 x 25 Gbps ESXi 7.0U1d build 17551050 ESXi 8.0 build 20513097
AMD BM.DenselO.E4.128 128 32, 64, 128 2048 2 x 50 Gbps ESXi 7.0U1d build 17551050 ESXi 8.0 build 20513097
AMD BM.DenselO.E5.128 128 32, 64, 96, 128 1536 1 x 100 Gbps ESXi 7.0U3q build 23794027 ESXi 8.0U3 build 24022510

See[Compute Dense I/O Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#bm-dense)for more detail.

#### Mixed Dense Shape Considerations

When creating a mixed cluster that contains both BM.DenseIO.E5 and BM.DenseIO.E4 shapes, it's important to evaluate the differences in networking and storage configurations, and their impact on workload performance.

#### Networking Considerations

The Dense E4 shape has two host NIC ports (2*50 Gbps), and the Dense E5 shape has one host NIC port (1*100 Gbps). In a mixed cluster, this difference can create variations in network performance across the cluster infrastructure, which might cause bottlenecks or inefficient usage of resources within the environment.

#### Storage Considerations

The Dense E4 shape has 8 NVMe based SSDs, while the Dense E5 shape has 12 NVMe based SSDs. In a mixed cluster, we recommend that the configuration align with the Dense E4. A single disk group can be configured for each host, comprising 1 cache device and 7 capacity devices. This means that although the Dense E5 shape has 12 disks, only 8 of the 12 disks on the Dense E5 are used in a mixed cluster. Four E5 disks remain unused. Mixed-disk configurations can result in variable performance depending on the workload architecture.

While vSAN supports heterogeneous configurations, we recommend maintaining consistent configurations across hosts to avoid performance bottlenecks, imbalances, and increased administrative complexity. Running mixed workloads in a cluster requires careful planning to ensure the best resource usage and minimize latency or throughput issues. Differences in memory capacity between Dense E4 and Dense E5 shapes, despite sometimes having similar OCPU configurations, can also impact workload performance.

### Standard Shapes

- You can have up to 32 standard shape hosts in a cluster.
- Standard shapes provide a lower-cost option than Dense shapes.
- Standard shapes require block volume storage. See the following section for more detail.
- Standard shapes are only available for a single Availability domain.
- Monthly pricing commitment isn't available for standard shapes.
- Limits for memory, bandwidth, and number of VNICs.
- Single-node SDDCs using standard shapes aren't supported.

The following table shows supported Standard shape configurations available for provisioning:

Processor Type Shape OCPU Available Core Configurations Memory (GB) Network Bandwidth Limit (Gbps) Minimum VMware version
Intel BM.Standard2.52 52 12, 26, 38, 52 768 50 ESXi 7.0U1d build 17551050 ESXi 8.0 build 20513097
Intel BM.Standard3.64 64 16, 32, 48, 64 1024 100 ESXi 7.0U1d build 17551050 ESXi 8.0 build 20513097
Intel BM.Optimized3.36 36 18, 26 512 100 ESXi 7.0U3q build 23794027 ESXi 8.0U2b build 23305546
AMD BM.Standard.E4.128 128 32, 64, 96, 128 2048 100 ESXi 7.0U1d build 17551050 ESXi 8.0 build 20513097
AMD (4th generation EPYC Processors™) BM.Standard.E5.192 192 48, 96, 144, and 192 2304 100 ESXi 7.0U3q build 23794027 ESXi 8.0U2b build 23305546

See[Compute Standard Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#bm-standard)for more detail.

### NVIDIA GPU Shapes

- GPU shape with an Intel® Xeon® processor and NVIDIA Tensor Core A10 GPU.
- You can have a maximum of 64 GPU shapes if you're working with a homogenous shape cluster.
- Provides local NVME 11.52 TB as a primary datastore and don't require block volume storage.
- vSAN converged storage technology replicates data across all the ESXi hosts in the SDDC.
- GPU shapes support all pricing commitments except Hourly .
- All HCX license types are available for GPU shapes.
- GPU shapes can be deployed across several Availability domains (Multi-AD).
- You can use a GPU shape to create a single-node SDDC.
- Shielded instances aren't supported.
- NVIDIA licenses need to be obtained from NVIDIA.

Processor Type Shape OCPU OCPU RAM (GB) GPU GPU RAM Available Core Configurations Network Bandwidth Limit (Gbps) Max VNIC Limit (Linux*) Minimum VMware version
Intel X9 BM.GPU.A10.4 64 1024 4 x A10 96 GB (24 GB each) 64 100 256 ESXi 7.0U3q build 23794027 ESXi 8.0U2 build 22380479

See[Compute GPU Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#bm-gpu)for more detail.

### Data Storage

Standard shape SDDCs leverage the Block Volume service for durability. All volumes are automatically replicated for you, helping to protect against data loss. Many copies of data are stored redundantly across many storage servers with built-in repair mechanisms. See[Block Volume Durability](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#Durability)for more information.
If you select a standard shape when you create an SDDC, the workflow automatically creates a management datastore block volume with the following characteristics:
- Capacity: 8 TB
- Default VPUs/GB: 10 (Balanced)
If you want more storage, you can create more volumes during the create SDDC workflow or using the[Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm)service. You're charged for all storage at regular block volume rates. The following limits apply to the SDDC data storage pool:
- Maximum volumes: 32
- Minimum volume size: 50 GB
- Maximum volume size: 32,768 GB (32 TB)

## Shielded Instances

When you create an SDDC and define its clusters, you can choose to use shielded instances for ESXi hosts. Shielded instances harden the firmware security on ESXi hosts to defend against malicious boot level software. Shielded instances for VMware Solution provide the following features:
- Secure boot checks the signature of each piece of boot software, including firmware drivers, EFI applications and the OS. If the signature is valid, the server boots and the firmware gives control to the OS. If the signature isn't found in the valid signatures database, the system doesn't boot. See the[VMware Secure Boot Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5D5EE0D1-2596-43D7-95C8-0B29733191D9.html)for more information.
- Trusted Platform Module (TPM) is a computer chip that can securely store artifacts like signatures, certificates and encryption keys used to authenticate the platform. See the[VMware TPM Documentation](https://blogs.vmware.com/vsphere/2018/04/vsphere-6-7-esxi-tpm-2-0.html)for more information.
Important  
  
Shielded instances must be enabled when you create the cluster. All hosts created in the cluster are shielded instances. You can't enable this option later, or for specific ESXi hosts. If you have already created a cluster without enabling shielded instances, and later want to use shielded instances, you must re-create the cluster.

For general information about shielded compute instances in OCI, see[Shielded Instances](https://docs.oracle.com/iaas/Content/Compute/References/shielded-instances.htm).

## Using Reserved Capacity

When you create a new ESXi host, you can choose to create it with reserved capacity, or create it with on-demand capacity.

On-demand capacity means that the compute capacity required to create the host is provisioned at the time of the request. You start paying for the capacity when it's provisioned.

Capacity reservations enable you to reserve instances in advance so that the capacity is available for workloads when you need it. Capacity reservations provide the following benefits:
- Assurance that you have the capacity necessary to manage the workload. Reserved capacity is available for the tenancy to consume at any time.
- No size or time commitments. Create a reservation with as little or as much capacity as you need, and delete the reservation at any time to stop paying for it.
- When instances that use reserved capacity are deleted, the capacity is returned to the reservation.
Note  
  
Capacity reservation isn't supported for an SDDC that uses more than one Availability domain.
Important  
  

When a host is still in a reserved capacity pool, billing is based on Reserved Capacity SKU pricing. After the host is provisioned from reserved capacity pool to an SDDC, the host switches to VMware Solution SKU pricing based on the commitment interval you select.

If the host is deleted before the commitment period ends, you continue to be billed for the host for the duration of the commitment.

Inactive hosts in a reserve capacity pool are billed independently of VMware Solution.

To use reserved capacity for VMware hosts, you must first set up a capacity reservation. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).

## Oracle Cloud VMware Solution Architecture

The following diagram shows how the various components of the Oracle Cloud VMware Solution SDDC are deployed on OCI bare metal compute instances, and how the solution is integrated into the OCI environment.

[

The diagram shows three ESXi hosts of an SDDC that resides in an OCI VCN. The center host shows the installed VMware software components for compute (vSphere), network (NSX-T), and storage (vSAN) support. The NSX overlay manages the flow of traffic between the VMs, and between the VMs and the rest of the resources in the solution. The VCN here includes various gateways that allow connectivity between the SDDC and an on-premises network, the internet, and the Oracle Services Network.

### Host Distribution and Availability Domains

To provide for high throughput and low latency, Oracle Cloud Infrastructure VMware Solution SDDCs are deployed by default across a minimum of three fault domains within a single Availability domain in a region. This architecture provides for low latency, high throughput connections to provide maximum performance and reliability.

If the SDDCs require deployment across many availability domains, the Multi AD feature is available at request. Considerations and potential limitations for Multi AD solutions:

- A Multi AD solution can prevent data loss in the event of a single AD becoming unavailable. If a host is lost in the SDDC, VMs are restarted on an available host in another Availability domain.
- Careful consideration must be taken when requesting to provision an SDDC across many availability domains. Performance might be impacted because of the possibility of increased network latency and storage throughput when compared with a single Availability domain deployment.
- As a Multi AD SDDC scales upward, demand on the network also grows. Replicating data across hosts in different availability domains impacts such functions as vSAN storage synchronization, and rebuild and resync times. More management functions can also impact performance of customer workloads.
- We recommend VMware SDDCs deployed across availability domains within a region don't exceed a maximum of 16 ESXi hosts .

To use the Multi AD feature, first[contact the Oracle Cloud VMware Solution team and request enablement of Multi AD for your tenancy](mailto:oci_ocvs_product_ww_grp@oracle.com). Then, when you[create a cluster, specify deployment of dense shape ESXi hosts across multiple availability domains .

For general information, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

### HCX Manager

When you provision an SDDC, you can enable HCX Manager (not shown in the diagram). HCX is an application mobility platform that simplifies application migration, workload rebalancing, and business continuity across data centers and clouds.

For HCX to function correctly in VMware solution, connectivity to a VMware SaaS portal provided by a[NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)is required. For more information, see[Why does HCX Manager require connectivity for activation and updates?](https://kb.vmware.com/s/article/74888).

A[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm)connection for intersite communication is recommended but not required.

## About the VMware Software

OCI's VMware software bundle contains vSphere, vSAN, NSX, vCenter, and HCX components to support compute, storage, and network needs for a fully functional VMware environment.
- vSphere: vSphere is VMware's virtualization platform for unified management of the SDDC's CPU, storage, and networking infrastructure. Two key components of vSphere are ESXi hypervisor and vCenter Server.
- NSX-T: NSX-T Data Center provides the SDDC with its virtual networking and security capabilities. The NSX-T deployment includes NSX Manager unified appliances with NSX-T Local Manager and NSX-T Controller, and NSX-T Edge nodes.
- vSAN: Oracle Cloud VMware Solution SDDCs use VMware's vSAN storage technology, which provides a single shared datastore for compute andx management workloads (VMs).
- HCX: The Hybrid Cloud Extension is an application mobility platform that removes complexity from application and workload migration. HCX is optionally installed as a plugin when you set up an SDDC. You can install HCX Advanced at no extra cost, or HCX Enterprise as a billed upgrade. See[HCX License Types](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#HCX-license-types)for more information.

When you provision the SDDC, you select the initial version of this software bundle to install on the ESXi hosts created during provisioning. You can change the default software version of the SDDC later. When you add ESXi hosts to the SDDC, you don't need to use the SDDC default version. You can select any ESXi software version under the major version deployed with the SDDC.
Note  
  
Changes that you make to the SDDC by using the Oracle Cloud InfrastructureConsole, API, or CLI aren't automatically made in vCenter. For example, if you change the software version or the SSH keys, the change applies only to ESXi hosts that you add to the SDDC. To change these properties for existing hosts, you must make the applicable updates in vCenter manually.
The following tables list the components and versions for current VMware software bundles:

vSphere 8.0
Component Version Build
VMware ESXi ESXi 8.0 Update 3j 25429389
VMware vCenter Server Appliance vCenter Server 8.0 Update 3j 25413364
VMware NSX-T Data Center 4.2.4.0 25410638
HCX Cloud 4.11.5.0 25438872
HCX Connector 4.11.5.0 25438871

vSphere 7.0
Component Version Build
VMware ESXi ESXi 7.0U3w 24784741
VMware vCenter Server Appliance vCenter Server 7.0 U3s 24201990
VMware NSX-T Data Center 3.2.4 23653566
HCX Cloud 4.10.2.0 24404455
HCX Connector 4.10.2.0 24404455

The following table shows versions of the software bundle that have reached an End of support state.

Software Version vSphere vSAN NSX-T

6.7 update 3* 6.7 U3

6.7 U3 3.2.0.1

6.5 update 3* 6.5 U3

6.5 U3 3.2.0.1
Note  
  
* vSphere 6.5 and vSphere 6.7 reached the End of General Support from VMware Solution on October 15, 2022. Oracle provides commercially reasonable support for provisioning of vSphere 6.5 and 6.7 environments when they enter the Technical Guidance phase after that date. We recommend that you use the latest version of vSphere when you create an SDDC.

### Upgrading VMware Software

When a new version of the VMware software becomes available, VMware Solution notifies you and provides a workflow that guides you through the upgrade process step-by-step. The workflow is different depending on which version you're upgrading. For information about available upgrades by version, see[Upgrading a VMware Solution SDDC's Software](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade.htm).

### HCX License Types

The Hybrid Cloud Extension (HCX) is an application mobility platform that simplifies application migration, workload rebalancing, and business continuity across data centers and clouds. To run HCX, each physical socket at the destination must have at least one license key assigned. The number of on-premises keys provided depends on the HCX license type.

License Number of Keys Standard Shape SDDCs Dense Shape SDDCs Notes
Advanced 3 Not supported Included at no extra cost This license type lets you migrate fewer workloads with some application downtime.
Enterprise 10 Enterprise license included at no extra cost. No option to downgrade to an Advanced license. Billed upgrade. You can choose to downgrade to an Advanced license later.

This license type lets you migrate many mission-critical workloads with zero downtime.

Any HCX Enterprise charges applied are billed monthly and are independent from host billing intervals. After SDDC provisioning is complete, you can view the HCX Monthly Billing Cycle End Date on the Details page.
If you're using dense shapes for an SDDC, you can change the HCX license type:
- Updgrading to Enterprise: Increases the number of on-premises connection keys issued from 3 to 10. The upgrade work request starts immediately. The HCX Enterprise billing cycle begins as soon as the work request is complete.
- Downgrading to Advanced: Decreases the number of on-premises connection keys from 10 to 3. You must specify 3 license keys to retain after the downgrade. The downgrade request remains in a pending state until the HCX Monthly Billing Cycle End Date. You can cancel the downgrade request as long as it's still in a`pending`state.

Note  
  
Standard shapes include the Enterprise license type at no cost, and are free. You can't change the license type in SDDCs that use standard shapes.

For more information, see[Upgrading a VMware Solution SDDC's HCX License](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-upgrade-hcx.htm)and[Downgrading a VMware Solution SDDC's HCX License](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-downgrade-hcx.htm).

## Billing Options

OCI's VMware Solution bundle offers flexible billing options that you can select from.
- Pricing interval: Define a pricing interval for ESXi hosts in an SDDC or cluster. Each cluster in an SDDC can have a different pricing interval. Select from hourly, monthly, yearly, or every three years.
- Swap billing commitments: You can transfer the billing commitment, HCX commitment, and billing end date from one ESXi host to another. Billing commitments can be transferred from a deleted host or an existing host.

For more detail, see[VMware Solution Billing Options](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/billing-options.htm)and[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/swap-billing.htm).

## Running Network Load Balancers on Oracle Cloud VMware Solution

Virtual machine instances that reside within Oracle Cloud VMware Solution (OCVS) can't communicate to VM instances outside of OCVS if both OCVS and the network load balancer are on the same VCN. For workarounds, see[Communicating Between Virtual Machine Instances](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm#communicate-vm).

## Working with SDDCs

You use the OCI Console, API, or CLI to provision and manage SDDC resources. You use VMware's vCenter utility to create and manage workloads in the SDDC.

See the following topics for information and instructions on how to create and manage Oracle Cloud VMware Solution resources:
- [Creating a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvssettingupsddc.htm)
- [Managing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvsmanagingsddc.htm)
- [Managing ESXi Hosts](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsmanaging-esxi-hosts.htm)
- [Configuring VMware Solution SDDC Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvsconfigconnectivity.htm)
- [Managing VLANs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvsmanagingl2net.htm)

## Additional Documentation Resources

The following Oracle Cloud VMware Solution playbooks and white papers are available:
- [Deploy Zerto to protect your VMware SDDC in the cloud against disasters](https://docs.oracle.com/en/solutions/deploy-zerto-for-ocvs/index.html#GUID-53CCF4BB-DF8D-4200-9382-89154A0B8BE3)

Learn how to deploy Zerto to protect Oracle Cloud VMware SDDC data in the cloud.
- [Deploy Veeam to protect your VMware SDDC in the cloud against disasters](https://docs.oracle.com/en/solutions/deploy-veeam-for-ocvs/index.html#GUID-8109D7EA-F842-4339-B8B7-8AA1F11F10AE)

Learn how to deploy Veeam to protect Oracle Cloud VMware SDDC data in the cloud.
- [Deploy Actifio to protect your VMware SDDC in the cloud against disasters](https://docs.oracle.com/en/solutions/deploy-actifio-oracle-vmware-solution/index.html#GUID-C5720B62-045F-418F-9E8C-FFE3799FB103)

Learn how you can configure Actifio backup and disaster recovery solution for guest VMs in Oracle Cloud VMware Solution.
- [Deploy a highly available SDDC to the cloud](https://docs.oracle.com/en/solutions/deploy-vmware-sddc-oci/index.html)

Shows you how to deploy a VMware SDDC on Oracle Cloud Infrastructure and then integrate it with other Oracle services running on Oracle Cloud.
- [Migrate your on-premises VMware workloads to the cloud](https://docs.oracle.com/en/solutions/migrate-vmware-workloads-oraclecloud/index.html)

Outlines the process of online, or live, migration of VMware workloads from an on-premises data center environment to Oracle Cloud VMware Solution.
- [Build a hybrid SDDC by extending your on-premises VMware deployment to Oracle Cloud](https://docs.oracle.com/en/solutions/hybrid-ocvs-sddc-onprem-sddc-cloud/index.html)

Describes how to set up a hybrid VMware SDDC between an on-premises environment and OCI by using Oracle Cloud VMware Solution.
- [Learn about connecting to Oracle Cloud and VMware resources](https://docs.oracle.com/en/solutions/connect-oraclecloud-vmware-resources/index.html)

Describes several methods for connecting to Oracle Cloud and VMware resources, plus their benefits, limitations, and how to get started.
- [Implement disaster recovery for an Oracle Cloud VMware Solution SDDC on the cloud](https://docs.oracle.com/en/solutions/implement-dr-for-ocvs/index.html)

Describes how Oracle Cloud VMware Solution uses VMware Site Recovery Manager (SRM) to implement an automated, reliable, and flexible disaster recovery solution for a VMware SDDC.
- [Deploy a multitier application stack on a VMware SDDC connected to an autonomous database](https://docs.oracle.com/en/solutions/ocvs-oci/index.html)
