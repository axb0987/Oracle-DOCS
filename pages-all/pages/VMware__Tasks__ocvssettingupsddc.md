# Creating a VMware Solution SDDC
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm
- Fetched: 2026-09-05 03:09 CDT

# Creating a VMware Solution SDDC

Create a multi host SDDC with 3 to 64 ESXi hosts or a single-host SDDC on supported Oracle Cloud Infrastructure (OCI) bare metal Compute instances by using the VMware Solution service.

Available SDDC types include multi-host and single-host. A single-host SDDC is typically used for testing and short-term development. For more information about SDDC types, see[VMware Solution SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm).

## Before You Begin

- You need an existing VCN with an IP address CIDR of /24 or larger available for running the cluster. The following list shows the allowed CIDR sizes and the number of nodes you can create in each:
- CIDR block size /24 , segment size /28 , number of nodes in cluster 3-12 .
- CIDR block size /23 , segment size /27 , number of nodes in cluster 3-28 .
- CIDR block size /22 , segment size /26 , number of nodes in cluster 3-60 .
- CIDR block size /21 , segment size /25 , number of nodes in cluster 3-64 .
Note  
  
If you're adding several clusters, be sure to plan the required CIDR blocks for each that fit your needs.
- We recommend that you set up connectivity between the VCN and the on-premises network before provisioning an SDDC. See[Access to Your On-Premises Network](https://docs.oracle.com/iaas/Content/Network/Concepts/connectivityonprem.htm).
- You can quickly create a VCN for an SDDC and set up an IPSec connection between an on-premises network and the VCN by using the Site-to-Site VPN workflow. To learn how, see[Site-to-Site VPN Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartIPsec.htm).
- You must create a[Datastore Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-clusters-create.htm)with the required[Datastores](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-create.htm)before starting the SDDC creation using Standard shapes. The SDDC creation workflow prompts you to attach an existing[Datastore Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-clusters-create.htm). New Block Volumes can't be created during this process, unlike the previous workflow.
- The Create SDDC workflow can automatically create and configure the SDDC's networking resources for you. Or, you can use existing networking resources that you created manually before you create the SDDC. SDDC provisioning requires the following resources:
- A provisioning subnet with a route table. For instructions about how to create these manually, see[Overview of VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm).
- Security rules for the provisioning subnet as detailed in[VMware Solution SDDC Security Rules](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Reference/ocvssecurityrules.htm).
- For a list of required VLANs and instructions about how to create them, see[Creating a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm).
Note  
  
If you're adding many clusters, be sure to plan for several subnets and VLANs dedicated to each cluster.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvssettingupsddc.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

On the Software-Defined Data Centers list page, select Create SDDC . If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).

The Create SDDC page opens.

## Basic information

Specify the VMware software version, HCX license type, and other basic information for the new SDDC.
- 

SDDC name : Enter a descriptive name for the SDDC. This name must be unique among all SDDCs in the creating, active, or updating state across all compartments in the region. The SDDC name must be 1 to 16 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. The name is not case-sensitive. For example,`test`and`Test`are treated as the same name. Avoid entering confidential information.
- SDDC compartment : Select the compartment in which to create the SDDC. All ESXi hosts for this SDDC are placed in this compartment.
- VMware software version : Select the version of VMware software to install on the ESXi hosts. Although the VMware software bundle includes vSphere, vSAN, NSX, and vCenter components, the version you specify here is the version of vSphere. Compatible versions of the other components are installed with the version of vSphere that you select. For details about the vSAN, NSX, or vCenter component versions installed, see[About the VMware Software](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#about-vmware). You can change this software version after provisioning.
- SSH Key : Provide the public key part of the SSH key. This key is required for remote connections to the ESXi hosts.

Select Add management cluster or Add workload cluster to open the Clusters page.

### Tags

Select Tags to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)for details.

### Pricing interval commitment

Select a license model. The HCX information is displayed only if License-included is selected.

License Model
- Bring Your Own License: License purchased from Broadcom.

Optional:
- VMware Avi Load Balancer License allocation compartment: Select the target compartment.
- VMware Avi Load Balancer License allocation: Select the license allocation.
- Instances: Number of assigned instances.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).
- License-included: License from OCI.

#### HCX

To use HCX, you must enable it during SDDC creation. You can't install this plugin later. When installed, the HCX Manager plugin is integrated with vCenter in the SDDC. HCX Advanced and HCX Enterprise[license types](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#HCX-license-types)are free for standard shapes. You're charged if you use HCX Enterprise licenses with dense shapes.
- Don't enable HCX : Don't install the HCX Manager plugin. You can't install this plugin later.
- Advanced license : Install the Advanced license of the HCX Manager plugin. You can change the license type after provisioning if you're using dense shapes.
- Enterprise license : Install the Enterprise license of the HCX Manager plugin. You can change the license type after provisioning if you're using dense shapes.

## Clusters

When creating a new SDDC, you must define at least one management cluster and one or more workload clusters.

### 1. Hosts

Configure the cluster's ESXi hosts.
- Cluster name : Enter a descriptive name for the cluster. The cluster name must be 1 to 22 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. Avoid entering confidential information.
- Availability domain : Select the availability domain in which to create the SDDC. You can deploy dense shape ESXi hosts across many availability domains. Standard shape ESXi hosts can be deployed only in a single availability domain. To ensure high availability, ESXi hosts in the SDDC are distributed across the fault domains in the availability domain. The management subnet and VLANs for this SDDC must be in this same availability domain.

#### Host Type

Configure the host type.
Host Type : For a detailed feature description, see[VMware Solution SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm).
- Multi host SDDC : Select for 3 to 64 hosts.
- Single host SDDC : Select for only one host, with more limited functionality.

Number of ESXi hosts : (Multi host SDDC only) Enter the initial number of ESXi hosts to create in a multi host SDDC. Specify at least 3 hosts and at most 64 hosts.
Prefix for ESXi hosts : (Optional) Enter a prefix to use for the names of the ESXi hosts to help identify them. The ESXi host prefix must be 1 to 22 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. The prefix can't end with a hyphen. Avoid entering confidential information.
Important  
  
ESXi host names can have a maximum of 25 characters including the prefix. Host FQDNs can have a maximum of 64 characters total.
Capacity type:
- On-demand capacity : Provisions the compute capacity when the host is created.
- Capacity reservation : Uses capacity that's counted against a reservation. Select a compartment and the name of a reservation. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
Note  
  
Capacity reservation isn't supported for an SDDC that uses many availability domains.

#### Cluster hardware type

Configure the hardware for the cluster.

Cluster hardware type : Select Change shape to select a shape to use for ESXi hosts in the SDDC. A shape is a template that decides the number of CPUs, amount of memory, and other resources allocated to a newly created instance. Some shapes let you select the number of cores. Standard shapes require block volume storage. A management datastore is automatically created for you. If you want more storage, you can create it later in this workflow. For more information, see[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#supported-shapes).

Shielded instance : Select this checkbox to enable shielded instances for all ESXi hosts created in the SDDC. You can enable this option only when you create the SDDC. You can't enable this option later, or only for specific ESXi hosts.

#### Pricing Interval Commitment

The dialog you see depends on the license type selected.

##### Bring your own license

Select the BYOL details.
- Compartment : Select the compartment that contains your license allocation.
- License allocation: Select the license allocation for this resource.

Select You are responsible at all times for maintaining active and compliant VMware software licenses and versions on all OCVS hosts .

##### License-included

Select the pricing interval to apply to the ESXi hosts. Choices include:
- Hourly
- Monthly
- One year
- Three year

Select Pricing interval must be confirmed to continue .

For more information about available pricing intervals, see[Billing Options](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#billing-options).

#### Proceed to Next Step

Select Next .

### 2. Networking

Select a VCN and specify a subnet and VLANs for the cluster's ESXi hosts.

- Virtual Cloud Network (VCN) : Select a VCN for the cluster. The VCN can be in a different compartment than the cluster and its ESXi hosts.

If you enabled HCX, the selected VCN must have a NAT gateway attached to it.
- If a NAT gateway already exists for the VCN, the name, compartment, and public IP address information is displayed.
- If no NAT gateway is attached to the selected VCN, the workflow creates one for you. Enter a name and select a compartment for the NAT gateway.
- To create the network resources for this cluster (recommended):
- Select Create new subnet and VLANs .
- Enter an available CIDR block in the selected VCN for the cluster management CIDR. The workflow divides this CIDR into equal segments to use for the provisioning subnet and the required VLANs. The workflow creates 1 subnet and 7 VLANs for version 6. x and 1 subnet and 9 VLANs for version 7. x of the VMware software. If you enable HCX, one extra VLAN is created.
- (Optional) To view information about the subnet and VLANs that the workflow creates, select Show network details . Details include the route table and security list for the subnet, and the route table and NSG for each VLAN.

- To update the information for the subnet: From the Actions menu (three dots) for the subnet, select Edit subnet .
- To update the information for a VLAN: From the Actions menu (three dots) for a VLAN, select Edit VLAN .

If you have enabled HCX, another route rule is created to allow traffic from the vSphere VLAN to the NAT gateway.
If you enabled HCX, the selected VCN must have a NAT gateway attached to it.
- If a NAT gateway already exists for the VCN, the name, compartment, and public IP address information is displayed.
- If no NAT gateway is attached to the selected VCN, the workflow creates one for you. Enter a name and select a compartment for the NAT gateway.
- To use existing network resources for this cluster, select Select existing subnet and VLANs , and then provide the following values:

- Select the compartment and provisioning subnet for the cluster management network. You can't change the subnet after provisioning.

The CIDR value shown is the private address space for the chosen subnet.
- Select the compartment and VLAN for each function of the management network.

The VLAN gateway CIDRs shown are the CIDR blocks from which to derive IP addresses for each VLAN's layer 3 traffic. These CIDR blocks also provide the private IP addresses that Oracle uses as attachment objects for public IP addresses when ESXi hosts require internet access.
- NSX Edge Uplink 1: Uplink used for communication between the VMware SDDC and OCI.
- NSX Edge Uplink 2: Reserved for future use to deploy public-facing applications on the VMware SDDC.
- NSX Edge VTEP: Used for data plane traffic between the ESXi host and NSX Edge.
- NSX VTEP: Used for data plane traffic between ESXi hosts.
- vMotion: Used for vMotion (VMware migration tool) management and workload.
- vSAN: Used for vSAN (VMware storage) data traffic.
- vSphere: Used for management of the SDDC components (ESXi, vCenter, NSX-T, and NSX Edge). If you selected the Enable HCX checkbox in step 3, verify that the VLAN selected for vSphere contains a route table rule that allows traffic to the NAT gateway. For more information, see[Managing Layer 2 Networking Resources for a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingl2net.htm)
- HCX: Used for HCX traffic. This VLAN appears only if you selected the Enable HCX checkbox.
- Replication Net: Used for the vSphere Replication engine. (VMware version 7. x only)
- Provisioning Net: Used for virtual machine cold migration, cloning, and snapshot migration.
- (Optional) Cluster Workload Network : Provide a cluster workload CIDR block for the workflow to create an initial logical segment for the VMs. The value must be /30 or larger and must not overlap with the VCN or the cluster network CIDRs. Note that you can add network segments for the cluster in NSX Manager after the SDDC is provisioned.
Select Next .

### 3. Datastores

The workflow automatically creates a management datastore with 8 TB capacity and VPUs/GB 10 (Balanced).

If you want more storage for the cluster, you can create more block volumes here.
Note  
  
Datastores are relevant to standard shapes (typically related to clusters and ESXi hosts).

- Select Create block volume.
The Create block volume panel opens.
- Enter the required information for the block volume. For information about block volume configuration, see[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm).
- Select Save Changes .
Select Next .

### 4. Notifications

Optionally enable monitoring and provide information about alarms and notifications. For more information, see[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/vmware-notifications.htm).

- Enable monitoring : Select to get notifications of selected events.
- Instance alarms : (Optional) Enable instance alarms and provide information about the alarm.

- Alarm name prefix: Each bare metal ESXi host has a separate alarm created for it. Enter a prefix to appear at the beginning of the alarm names for this SDDC.
- Alarm severity: Select a severity for the alarm: Info, Warning, Error, or Critical. All nonzero health issues for a bare metal instance triggers an alarm with the selected severity.
- Show default alarm values : View and edit the interval and trigger delay for each alarm.
- Interval: Select the interval at which the metric is emitted. The default is 1 minute.
- Trigger delay: Select the number of minutes that the condition must be maintained before the alarm is in firing state. The default is 1 minute.
- Topic source : Select an existing notification topic, or create a new one. If you select Create new , enter the following information:

- Topic name: Enter a friendly name for the notification topic.
- Subscription protocol: Select the protocol that you want to use to receive notifications. The default is email.
- Email address: Enter the email address or address list that you want to send notifications to.
- URL: If you select the Pager Duty protocol, enter a URL to send notifications to.
- Notification compartment: Select a compartment for the notification.
- Events : Select events that you want to receive notifications for. By default, all available notifications are selected.
Select Next .

### Review and Tag

Review the cluster configuration summary and optionally tag the SDDC. If you need to review or update an item, such as a VLAN or datastore, select the appropriate option from the Actions menu (three dots) .
- 

Select Submit .

The Create SDDC window opens, showing the new clusters and the previously entered basic information for the SDDC.
- 

(Optional) Tagging: To tag the SDDC, select one of the following options, depending on what you see:
- Advanced options
- Show advanced options

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. Any tags that you specify are applied to all the resources in the SDDC.

## Creating the SDDC

Review the SDDC configuration summary. If you need to review or update an item, such as a cluster, select the appropriate option from the Actions menu (three dots) .

Select Create SDDC .

The page shows the provisioning status of each resource.

When provisioning is complete, the SDDC's details page includes a username and an initial password that lets you access the vCenter management utility for the SDDC.
Note  
  
The password value displayed in the Console isn't updated after you change it.
- 

Use the[sddc create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/create.html)command and required parameters to create an SDDC:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
Important  
  
An SDDC or ESXi host which has failed provisioning doesn't get billed until provisioning succeeds.
- 

Run the[CreateSddc](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/CreateSddc)operation to create a new SDDC and ESXi hosts.
Important  
  
An SDDC or ESXi host which has failed provisioning doesn't get billed until provisioning succeeds.

## Next Steps

After provisioning your SDDC, you might want to perform some of the following tasks:
- Configure network connectivity between the SDDC and resources in your on-premises network, the Oracle Services Network, the internet through a NAT gateway, or other resources in the VCN. For information and instructions, see[Configuring VMware Solution SDDC Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity.htm).
- Modify resources or properties of your SDDC. For example, add ESXi hosts. See[VMware Solution SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm).
-
