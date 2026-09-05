# Adding a Cluster to a VMware Solution SDDC
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-add.htm
- Fetched: 2026-09-05 03:08 CDT

# Adding a Cluster to a VMware Solution SDDC

Add a cluster to an SDDC using VMware Solution.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-add.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-add.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-add.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the details page, select Add cluster .
- Provide information for the cluster:

- Cluster name: Enter a descriptive name for the cluster. The cluster name must be 1 to 22 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. Avoid entering confidential information.
- Availability domain: Select the Availability domain in which to create the SDDC.[If you have requested the Multi AD feature](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#host-distribution), you can deploy dense shape ESXi hosts across multiple availability domains . Standard shape ESXi hosts can be deployed only in a single Availability domain. To ensure high availability, ESXi hosts in the SDDC are distributed across the fault domains in the Availability domain. The management subnet and VLANs for this SDDC must be in this same Availability domain.
- Release name : Select an appropriate release name to match your vCenter version.
- ESXi hosts : Provide configuration information:
- Host type: A multi host SDDC can have from 3 to 64 hosts. A single-host SDDC can have only one host, and has more limited functionality. See[VMware Solution SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingsddc.htm)for a detailed feature description.
- Number of ESXi hosts: Enter the initial number of ESXi hosts to create in a multi host SDDC. A workload cluster can have 2 to 64 hosts, based on the selected shape.
- Prefix for ESXi hosts: (Optional) Enter a prefix to use for the names of the ESXi hosts to help identify them. The ESXi host prefix must be 1 to 22 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. The prefix can't end with a hyphen. Avoid entering confidential information.
Important  
  
ESXi host names can have a maximum of 25 characters including the prefix. Host FQDNs can have a maximum of 64 characters total.
- Capacity type: On-demand capacity provisions the compute capacity when the host is created. Capacity reservation uses capacity that's counted against a reservation. Select a compartment and the name of a reservation. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
Note  
  
Capacity reservation isn't supported for an SDDC that uses many Availability domains.
- SDDC hardware type: Select a shape to use for ESXi hosts in the SDDC. A shape is a template that decides the number of CPUs, amount of memory, and other resources allocated to a newly created instance. If you select a shape with an AMD processor, select the number of cores. Standard shapes require block volume storage. A management datastore is automatically created for you. If you want more storage, you can create it later in this workflow. For more information, see[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#supported-shapes).
- Enable shielded instance: Select this checkbox to enable shielded instances for all ESXi hosts created in the SDDC. You can enable this option only when you create the SDDC. You can't enable this option later, or only for specific ESXi hosts.
- Pricing interval commitment: Select the following:
- VMware Cloud Foundation License allocation compartment: Select the target compartment.
- VMware Cloud Foundation License allocation: Select the license allocation.
- VMware vDefend Firewall License allocation compartment: Select the target compartment.
- VMware vDefend Firewall License allocation: (Optional) Select the license allocation.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).

Select Terms and Conditions .
- Select Next to advance to the cluster's Networking page.
- Select a VCN for the cluster. The VCN can be in a different compartment than the cluster and its ESXi hosts.

If you enabled HCX, the selected VCN must have a NAT gateway attached to it.
- If a NAT gateway already exists for the VCN, the name, compartment, and public IP address information is displayed.
- If no NAT gateway is attached to the selected VCN, the workflow creates one for you. Enter a name and select a compartment for the NAT gateway.
- To have the workflow create the network resources for this cluster (recommended), select Create new subnet and VLANs , and then provide the following values. To use existing resources, skip to step .
- Select Create new subnet and VLANs .
- Enter an available CIDR block in the selected VCN for the cluster management CIDR. The workflow divides this CIDR into equal segments to use for the provisioning subnet and the required VLANs. The workflow creates 1 subnet and 7 VLANs for version 6. x and 1 subnet and 9 VLANs for version 7. x of the VMware software. If you enable HCX, one extra VLAN is created.
- (Optional) Select Show network details to view or edit the information for the subnet and VLANs that the workflow creates. Details include the route table and security list for the subnet, and the route table and NSG for each VLAN.

- To update the information for the subnet: From the the Actions menu (three dots) for the subnet, select Edit subnet .
- To update the information for a VLAN: From the the Actions menu (three dots) for the VLAN, select Edit VLAN .

If you have enabled HCX, another route rule is created to allow traffic from the vSphere VLAN to the NAT gateway.
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
- (Optional) Provide a cluster workload CIDR block for the workflow to create an initial logical segment for the VMs. The value must be /30 or larger and must not overlap with the VCN or the cluster network CIDRs. Note that you can add network segments for the cluster in NSX Manager after the SDDC is provisioned.
- Select Next to advance to the Datastores page.
The workflow automatically creates a management datastore with 8 TB capacity and VPUs/GB 10 (Balanced). If you want more storage for the cluster, you can create more block volumes here.
- Select Create block volume.
- Enter the required information for the block volume. For information about block volume configuration, see[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm).
- Perform one of the following actions depending on the option that you see:

- Select Save Changes .
- Select Submit .
- Select Next .
- (Optional) Enable monitoring and provide information about alarms and notifications. For more information, see[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/vmware-notifications.htm).

- (Optional) Enable instance alarms and provide information about the alarm. To see the Interval and Trigger delay fields, select Show default alarm values .
- Alarm name prefix: Each bare metal ESXi host has a separate alarm created for it. Enter a prefix that appears at the beginning of the alarm names for this SDDC.
- Alarm severity: Select a severity for the alarm: Info, Warning, Error, or Critical. All nonzero health issues for a bare metal instance triggers an alarm with the selected severity.
- Interval: Select the interval at which the metric is emitted. The default is 1 minute.
- Trigger delay: Select the number of minutes that the condition must be maintained before the alarm is in firing state. The default is 1 minute.
- Select an existing notification topic, or create a new one. If you select Create new , enter the following information:
- Topic name: Enter a friendly name for the notification topic.
- Subscription protocol: Select the protocol that you want to use to receive notifications. The default is email.
- Email address: Enter the email address or address list that you want to send notifications to.
- URL: If you select the Pager Duty protocol, enter a URL to send notifications to.
- Notification compartment: Select a compartment for the notification.
- Select events that you want to receive notifications for. By default, all available notifications are selected.
- To deselect a notification event, select the X on the notification.
- To reselect a notification event, select the selection field and select the notification from the list.
- Select Next to review the cluster configuration summary.

To make changes, select the name of the section that contains the fields you want to change, then come back to the Review section.
- When you're satisfied with the summary information, select Submit .
The cluster addition starts. You can monitor progress.
- Select Add a workload cluster to create more clusters in the SDDC.

Tip  
  
As you create workload cluster configurations, they appear in a list. You can view each cluster's configuration by selecting the expand icon on the left side. To delete the configuration, select the X on it's right side.
- 

Use the[cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/cluster/create.html)command and required parameters to create a cluster in an SDDC:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Cluster/CreateCluster)
