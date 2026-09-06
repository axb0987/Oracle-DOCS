# OCVP Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#dcoc-content-body)

## OCVP Common Types

### DBMS_CLOUD_OCI_OCVP_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_CHANGE_SDDC_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the SDDC to.

### DBMS_CLOUD_OCI_OCVP_NETWORK_CONFIGURATION_T Type

The network configurations used by Cluster, including[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management subnet and VLANs.

Syntax
```

```

Fields

Field Description

`provisioning_subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the management subnet used to provision the Cluster.

`vsphere_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the SDDC for the vSphere component of the VMware environment. This VLAN is a mandatory attribute for Management Cluster. This attribute is not guaranteed to reflect the vSphere VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the vSphere VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the vSphere component of the VMware environment, you should use`UPDATE_SDDC`Function to update the Cluster's `vsphereVlanId` with that new VLAN's OCID.

`vmotion_vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the vMotion component of the VMware environment. This attribute is not guaranteed to reflect the vMotion VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the vMotion VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the vMotion component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `vmotionVlanId` with that new VLAN's OCID.

`vsan_vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the vSAN component of the VMware environment. This attribute is not guaranteed to reflect the vSAN VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the vSAN VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the vSAN component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `vsanVlanId` with that new VLAN's OCID.

`nsx_v_tep_vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the NSX VTEP component of the VMware environment. This attribute is not guaranteed to reflect the NSX VTEP VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the NSX VTEP VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the NSX VTEP component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `nsxVTepVlanId` with that new VLAN's OCID.

`nsx_edge_v_tep_vlan_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the NSX Edge VTEP component of the VMware environment. This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the NSX Edge VTEP VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the NSX Edge VTEP component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `nsxEdgeVTepVlanId` with that new VLAN's OCID.

`nsx_edge_uplink1_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the SDDC for the NSX Edge Uplink 1 component of the VMware environment. This VLAN is a mandatory attribute for Management Cluster. This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the NSX Edge Uplink 1 component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `nsxEdgeUplink1VlanId` with that new VLAN's OCID.

`nsx_edge_uplink2_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the SDDC for the NSX Edge Uplink 2 component of the VMware environment. This VLAN is a mandatory attribute for Management Cluster. This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN currently used by the ESXi hosts in the Cluster. The purpose of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the Cluster to use a different VLAN for the NSX Edge Uplink 2 component of the VMware environment, you should use`UPDATE_CLUSTER`Function to update the Cluster's `nsxEdgeUplink2VlanId` with that new VLAN's OCID.

`replication_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the vSphere Replication component of the VMware environment.

`provisioning_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the Cluster for the Provisioning component of the VMware environment.

`hcx_vlan_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VLAN used by the SDDC for the HCX component of the VMware environment. This VLAN is a mandatory attribute for Management Cluster when HCX is enabled. This attribute is not guaranteed to reflect the HCX VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the HCX VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the HCX component of the VMware environment, you should use`UPDATE_SDDC`Function to update the SDDC's `hcxVlanId` with that new VLAN's OCID.

### DBMS_CLOUD_OCI_OCVP_VSPHERE_LICENSE_T Type

License for vSphere upgrade.

Syntax
```

```

Fields

Field Description

`license_type`

(required) vSphere license type.

`license_key`

(required) vSphere license key value.

### DBMS_CLOUD_OCI_OCVP_VSPHERE_UPGRADE_OBJECT_T Type

Binary object needed for vSphere upgrade

Syntax
```

```

Fields

Field Description

`download_link`

(required) Binary object download link.

`link_description`

(required) Binary object description.

### DBMS_CLOUD_OCI_OCVP_DATASTORE_DETAILS_T Type

Datastore summary for a getting an Sddc.

Syntax
```

```

Fields

Field Description

`block_volume_ids`

(required) A list of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of Block Storage Volumes.

`datastore_type`

(required) Type of the datastore.

Allowed values are: 'MANAGEMENT', 'WORKLOAD'

`l_capacity`

(required) Size of the Block Storage Volume in GB.

### DBMS_CLOUD_OCI_OCVP_VSPHERE_LICENSE_TBL Type

Nested table type of dbms_cloud_oci_ocvp_vsphere_license_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_VSPHERE_UPGRADE_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_ocvp_vsphere_upgrade_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_DATASTORE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_ocvp_datastore_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_CLUSTER_T Type

An[Oracle Cloud VMware Solution](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm)Cluster contains the resources required for a functional VMware environment. Instances in a Cluster (see`ESXI_HOST`Type) run in a virtual cloud network (VCN) and are preconfigured with VMware and storage. Use the vCenter utility to manage and deploy VMware virtual machines (VMs) in the Cluster. The Cluster uses a single management subnet for provisioning the Cluster. It also uses a set of VLANs for various components of the VMware environment (vSphere, vMotion, vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cluster.

`compute_availability_domain`

(required) The availability domain the ESXi hosts are running in. For Multi-AD Cluster, it is `multi-AD`. Example: `Uocm:PHX-AD-1`, `multi-AD`

`display_name`

(required) A descriptive name for the Cluster. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.

`instance_display_name_prefix`

(optional) A prefix used in the name of each ESXi host and Compute instance in the Cluster. If this isn't set, the Cluster's `displayName` is used as the prefix. For example, if the value is `MyCluster`, the ESXi hosts are named `MyCluster-1`, `MyCluster-2`, and so on.

`vmware_software_version`

(required) In general, this is a specific version of bundled VMware software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the Cluster. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer version of bundled VMware software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_CLUSTER`Function to update the Cluster's `vmwareSoftwareVersion` with that new version.

`esxi_software_version`

(optional) In general, this is a specific version of bundled ESXi software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function unless a different version is configured on the ESXi host level. Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer version of bundled ESXi software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_CLUSTER`Function to update the Cluster's `esxiSoftwareVersion` with that new version.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the Cluster.

`sddc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC that the Cluster belongs to.

`esxi_hosts_count`

(required) The number of ESXi hosts in the Cluster.

`initial_commitment`

(optional) The billing option selected during Cluster creation.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`workload_network_cidr`

(optional) The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application workloads.

`network_configuration`

(required)

`time_created`

(required) The date and time the Cluster was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the Cluster was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the Cluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`upgrade_licenses`

(optional) The vSphere licenses to use when upgrading the Cluster.

`vsphere_upgrade_objects`

(optional) The links to binary objects needed to upgrade vSphere.

`initial_host_shape_name`

(required) The initial compute shape of the Cluster's ESXi hosts.`LIST_SUPPORTED_HOST_SHAPES`Function.

`initial_host_ocpu_count`

(optional) The initial OCPU count of the Cluster's ESXi hosts.

`is_shielded_instance_enabled`

(optional) Indicates whether shielded instance is enabled at the Cluster level.

`capacity_reservation_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Capacity Reservation.

`datastores`

(optional) Datastores used for the Cluster.

`vsphere_type`

(required) vSphere Cluster types.

Allowed values are: 'MANAGEMENT', 'WORKLOAD'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_CLUSTER_SUMMARY_T Type

A summary of the Cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the Cluster.

`compute_availability_domain`

(required) The availability domain that the Cluster's ESXi hosts are running in. For Multi-AD Cluster, it is `multi-AD`.

`sddc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC that the Cluster belongs to.

`display_name`

(required) A descriptive name for the Cluster. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.

`vmware_software_version`

(required) In general, this is a specific version of bundled VMware software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the Cluster. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this Cluster in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you upgrade the existing ESXi hosts in the Cluster to use a newer version of bundled VMware software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_CLUSTER`Function to update the Cluster's `vmwareSoftwareVersion` with that new version.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the Cluster.

`esxi_hosts_count`

(required) The number of ESXi hosts in the Cluster.

`time_created`

(optional) The date and time the Cluster was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the Cluster was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the Cluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_shielded_instance_enabled`

(optional) Indicates whether shielded instance is enabled at the Cluster level.

`initial_host_shape_name`

(required) The initial compute shape of the Cluster's ESXi hosts.`LIST_SUPPORTED_HOST_SHAPES`Function.

`initial_host_ocpu_count`

(optional) The initial OCPU count of the Cluster's ESXi hosts.

`vsphere_type`

(required) vSphere Cluster types.

Allowed values are: 'MANAGEMENT', 'WORKLOAD'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_CLUSTER_COLLECTION_T Type

A list of Clusters.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Clusters.

### DBMS_CLOUD_OCI_OCVP_DATASTORE_INFO_T Type

Datastore info for creating an Sddc.

Syntax
```

```

Fields

Field Description

`block_volume_ids`

(required) A list of[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of Block Storage Volumes.

`datastore_type`

(required) Type of the datastore.

Allowed values are: 'MANAGEMENT', 'WORKLOAD'

### DBMS_CLOUD_OCI_OCVP_DATASTORE_INFO_TBL Type

Nested table type of dbms_cloud_oci_ocvp_datastore_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_CREATE_CLUSTER_DETAILS_T Type

Details of the Cluster.

Syntax
```

```

Fields

Field Description

`sddc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC that the Cluster belongs to.

`compute_availability_domain`

(required) The availability domain to create the Cluster's ESXi hosts in. For multi-AD Cluster deployment, set to `multi-AD`.

`display_name`

(optional) A descriptive name for the Cluster. Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.

`instance_display_name_prefix`

(optional) A prefix used in the name of each ESXi host and Compute instance in the Cluster. If this isn't set, the Cluster's `displayName` is used as the prefix. For example, if the value is `myCluster`, the ESXi hosts are named `myCluster-1`, `myCluster-2`, and so on.

`esxi_hosts_count`

(required) The number of ESXi hosts to create in the Cluster. You can add more hosts later (see`CREATE_ESXI_HOST`Function). **Note:** If you later delete EXSi hosts from a production Cluster to make SDDC total host count less than 3, you are still billed for the 3 minimum recommended ESXi hosts. Also, you cannot add more VMware workloads to the Cluster until the SDDC again has at least 3 ESXi hosts.

`network_configuration`

(required)

`initial_commitment`

(optional) The billing option selected during Cluster creation.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`workload_network_cidr`

(optional) The CIDR block for the IP addresses that VMware VMs in the Cluster use to run application workloads.

`initial_host_shape_name`

(optional) The initial compute shape of the Cluster's ESXi hosts.`LIST_SUPPORTED_HOST_SHAPES`Function.

`initial_host_ocpu_count`

(optional) The initial OCPU count of the Cluster's ESXi hosts.

`is_shielded_instance_enabled`

(optional) Indicates whether shielded instance is enabled for this Cluster.

`capacity_reservation_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Capacity Reservation.

`datastores`

(optional) A list of datastore info for the Cluster. This value is required only when `initialHostShapeName` is a standard shape.

`vmware_software_version`

(optional) The VMware software bundle to install on the ESXi hosts in the Cluster. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`esxi_software_version`

(optional) The ESXi software bundle to install on the ESXi hosts in the Cluster. Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_CREATE_ESXI_HOST_DETAILS_T Type

Details of the ESXi host to add to the Cluster.

Syntax
```

```

Fields

Field Description

`cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cluster to add the ESXi host to.

`display_name`

(optional) A descriptive name for the ESXi host. It's changeable. Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the Cluster. If this attribute is not specified, the Cluster's `instanceDisplayNamePrefix` attribute is used to name and incrementally number the ESXi host. For example, if you're creating the fourth ESXi host in the Cluster, and `instanceDisplayNamePrefix` is `MyCluster`, the host's display name is `MyCluster-4`. Avoid entering confidential information.

`billing_donor_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deleted ESXi Host with LeftOver billing cycle.

`current_commitment`

(optional) The billing option currently used by the ESXi host.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`next_commitment`

(optional) The billing option to switch to after the existing billing cycle ends. If `nextCommitment` is null or empty, `currentCommitment` continues to the next billing cycle.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`compute_availability_domain`

(optional) The availability domain to create the ESXi host in. If keep empty, for AD-specific Cluster, new ESXi host will be created in the same availability domain; for multi-AD Cluster, new ESXi host will be auto assigned to the next availability domain following evenly distribution strategy.

`host_shape_name`

(optional) The compute shape name of the ESXi host.`LIST_SUPPORTED_HOST_SHAPES`Function.

`host_ocpu_count`

(optional) The OCPU count of the ESXi host.

`capacity_reservation_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Capacity Reservation.

`esxi_software_version`

(optional) The ESXi software bundle to install on the ESXi host. Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_INITIAL_CLUSTER_CONFIGURATION_T Type

Details of the initial Cluster of SDDC.

Syntax
```

```

Fields

Field Description

`vsphere_type`

(required) vSphere Cluster types.

Allowed values are: 'MANAGEMENT', 'WORKLOAD'

`compute_availability_domain`

(required) The availability domain to create the Cluster's ESXi hosts in. For multi-AD Cluster deployment, set to `multi-AD`.

`display_name`

(optional) A descriptive name for the Cluster. Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.

`instance_display_name_prefix`

(optional) A prefix used in the name of each ESXi host and Compute instance in the Cluster. If this isn't set, the Cluster's `displayName` is used as the prefix. For example, if the value is `myCluster`, the ESXi hosts are named `myCluster-1`, `myCluster-2`, and so on.

`esxi_hosts_count`

(required) The number of ESXi hosts to create in the Cluster. You can add more hosts later (see`CREATE_ESXI_HOST`Function). Creating a Cluster with a ESXi host count of 1 will be considered a single ESXi host Cluster. **Note:** If you later delete EXSi hosts from a production Cluster to total less than 3, you are still billed for the 3 minimum recommended ESXi hosts. Also, you cannot add more VMware workloads to the Cluster until it again has at least 3 ESXi hosts.

`network_configuration`

(required)

`initial_commitment`

(optional) The billing option selected during Cluster creation.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`workload_network_cidr`

(optional) The CIDR block for the IP addresses that VMware VMs in the Cluster use to run application workloads.

`initial_host_shape_name`

(optional) The initial compute shape of the Cluster's ESXi hosts.`LIST_SUPPORTED_HOST_SHAPES`Function.

`initial_host_ocpu_count`

(optional) The initial OCPU count of the Cluster's ESXi hosts.

`is_shielded_instance_enabled`

(optional) Indicates whether shielded instance is enabled for this Cluster.

`capacity_reservation_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Capacity Reservation.

`datastores`

(optional) A list of datastore info for the Cluster. This value is required only when `initialHostShapeName` is a standard shape.

### DBMS_CLOUD_OCI_OCVP_INITIAL_CLUSTER_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_ocvp_initial_cluster_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_INITIAL_CONFIGURATION_T Type

Details of SDDC initial configuration

Syntax
```

```

Fields

Field Description

`initial_cluster_configurations`

(required) The configurations for Clusters initially created in the SDDC.

### DBMS_CLOUD_OCI_OCVP_CREATE_SDDC_DETAILS_T Type

Details of the SDDC.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A descriptive name for the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.

`vmware_software_version`

(required) The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`esxi_software_version`

(optional) The ESXi software bundle to install on the ESXi hosts in the SDDC. Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to contain the SDDC.

`hcx_mode`

(required) HCX configuration of the SDDC.

Allowed values are: 'DISABLED', 'ADVANCED', 'ENTERPRISE'

`initial_configuration`

(required)

`is_single_host_sddc`

(optional) Indicates whether this SDDC is designated for only single ESXi host.

`ssh_authorized_keys`

(required) One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_DOWNGRADE_HCX_DETAILS_T Type

The HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced. Downgrading from HCX Enterprise to HCX Advanced reduces the number of provided license keys from 10 to 3.

Syntax
```

```

Fields

Field Description

`reserving_hcx_on_premise_license_keys`

(required) The HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced.

### DBMS_CLOUD_OCI_OCVP_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_OCVP_ESXI_HOST_T Type

An ESXi host is a node in a Cluster. At a minimum, each Cluster has 3 ESXi hosts that are used to implement a functioning VMware environment. In terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software. Notice that an `EsxiHost` object has its own OCID (`id`), and a separate attribute for the OCID of the Compute instance (`computeInstanceId`).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host.

`display_name`

(required) A descriptive name for the ESXi host. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`sddc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC that the ESXi host belongs to.

`cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cluster that the ESXi host belongs to.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the Cluster.

`compute_instance_id`

(optional) In terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software. The `computeInstanceId` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of that Compute instance.

`time_created`

(optional) The date and time the ESXi host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the ESXi host was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the ESXi host.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`billing_donor_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deleted ESXi Host with LeftOver billing cycle.

`swap_billing_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the active ESXi Host to swap billing with current host.

`is_billing_continuation_in_progress`

(optional) Indicates whether this host is in the progress of billing continuation.

`is_billing_swapping_in_progress`

(optional) Indicates whether this host is in the progress of swapping billing.

`current_commitment`

(required) The billing option currently used by the ESXi host.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`next_commitment`

(required) The billing option to switch to after the current billing cycle ends. If `nextCommitment` is null or empty, `currentCommitment` continues to the next billing cycle.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`billing_contract_end_date`

(required) Current billing cycle end date. If the value in `currentCommitment` and `nextCommitment` are different, the value specified in `nextCommitment` becomes the new `currentCommitment` when the `contractEndDate` is reached. Example: `2016-08-25T21:10:29.600Z`

`failed_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that failed.

`replacement_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that is created to replace the failed host.

`grace_period_end_date`

(optional) The date and time when the new esxi host should start billing cycle.[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2021-07-25T21:10:29.600Z`

`vmware_software_version`

(required) The version of VMware software that Oracle Cloud VMware Solution installed on the ESXi hosts.

`esxi_software_version`

(optional) The version of ESXi software that Oracle Cloud VMware Solution installed on the ESXi hosts.

`non_upgraded_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that will be upgraded.

`upgraded_replacement_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that is newly created to upgrade the original host.

`compute_availability_domain`

(required) The availability domain of the ESXi host.

`host_shape_name`

(required) The compute shape name of the ESXi host.`LIST_SUPPORTED_HOST_SHAPES`Function.

`host_ocpu_count`

(optional) The OCPU count of the ESXi host.

`capacity_reservation_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Capacity Reservation.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_ESXI_HOST_SUMMARY_T Type

A summary of the ESXi host.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host.

`display_name`

(optional) A descriptive name for the ESXi host. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`sddc_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC that the ESXi host belongs to.

`cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cluster that the ESXi host belongs to.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the Cluster.

`compute_instance_id`

(optional) In terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software. The `computeInstanceId` is the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of that Compute instance.

`time_created`

(optional) The date and time the ESXi host was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the ESXi host was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the ESXi host.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`current_commitment`

(required) The billing option currently used by the ESXi host.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`next_commitment`

(required) The billing option to switch to after the current billing cycle ends. If `nextCommitment` is null or empty, `currentCommitment` continues to the next billing cycle.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`billing_contract_end_date`

(required) Current billing cycle end date. If the value in `currentCommitment` and `nextCommitment` are different, the value specified in `nextCommitment` becomes the new `currentCommitment` when the `contractEndDate` is reached. Example: `2016-08-25T21:10:29.600Z`

`failed_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that failed.

`replacement_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that is newly created to replace the failed host.

`grace_period_end_date`

(optional) The date and time when the new esxi host should start billing cycle.[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2021-07-25T21:10:29.600Z`

`vmware_software_version`

(required) The version of VMware software that Oracle Cloud VMware Solution installed on the ESXi hosts.

`non_upgraded_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that will be upgraded.

`upgraded_replacement_esxi_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ESXi host that is newly created to upgrade the original host.

`compute_availability_domain`

(required) The availability domain of the ESXi host.

`host_shape_name`

(required) The compute shape name of the ESXi host.`LIST_SUPPORTED_HOST_SHAPES`Function.

`host_ocpu_count`

(optional) The OCPU count of the ESXi host.

`billing_donor_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deleted ESXi Host with LeftOver billing cycle.

`swap_billing_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the active ESXi Host to swap billing with current host.

`is_billing_continuation_in_progress`

(optional) Indicates whether this host is in the progress of billing continuation.

`is_billing_swapping_in_progress`

(optional) Indicates whether this host is in the progress of swapping billing.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_ESXI_HOST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_esxi_host_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_ESXI_HOST_COLLECTION_T Type

A list of ESXi hosts.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of ESXi hosts.

### DBMS_CLOUD_OCI_OCVP_HCX_LICENSE_SUMMARY_T Type

HCX on-premise license information summary.

Syntax
```

```

Fields

Field Description

`activation_key`

(required) HCX on-premise license key value.

`status`

(required) status of HCX on-premise license.

Allowed values are: 'AVAILABLE', 'CONSUMED', 'DEACTIVATED', 'DELETED'

`system_name`

(optional) Name of the system that consumed the HCX on-premise license

### DBMS_CLOUD_OCI_OCVP_REPLACE_HOST_DETAILS_T Type

The details for replacing ESXi host.

Syntax
```

```

Fields

Field Description

`esxi_software_version`

(optional) The ESXi software bundle to install on the ESXi host. Only versions under the same vmwareSoftwareVersion and have been validate by Oracle Cloud VMware Solution will be accepted. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

### DBMS_CLOUD_OCI_OCVP_HCX_LICENSE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_hcx_license_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SDDC_T Type

An[Oracle Cloud VMware Solution](https://docs.oracle.com/iaas/Content/VMware/Concepts/ocvsoverview.htm)software-defined data center (SDDC) contains the resources required for a functional VMware environment. Instances in an SDDC (see`ESXI_HOST`Type) run in a virtual cloud network (VCN) and are preconfigured with VMware and storage. Use the vCenter utility to manage and deploy VMware virtual machines (VMs) in the SDDC. The SDDC uses a single management subnet for provisioning the SDDC. It also uses a set of VLANs for various components of the VMware environment (vSphere, vMotion, vSAN, and so on). See the Core Services API for information about VCN subnets and VLANs.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC.

`display_name`

(required) A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.

`vmware_software_version`

(required) In general, this is a specific version of bundled VMware software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer version of bundled VMware software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_SDDC`Function to update the SDDC's `vmwareSoftwareVersion` with that new version.

`esxi_software_version`

(optional) In general, this is a specific version of bundled ESXi software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function unless a different version is configured on the Cluster or ESXi host level. Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer version of bundled ESXi software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_SDDC`Function to update the SDDC's `vmwareSoftwareVersion` with that new version.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the SDDC.

`clusters_count`

(required) The number of Clusters in the SDDC.

`vcenter_fqdn`

(required) The FQDN for vCenter. Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`

`nsx_manager_fqdn`

(required) The FQDN for NSX Manager. Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`

`vcenter_private_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PrivateIp` object that is the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the Core Services API.

`nsx_manager_private_ip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PrivateIp` object that is the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the Core Services API.

`vcenter_username`

(optional) The SDDC includes an administrator username and password for vCenter. You can change this initial username to a different value in vCenter.

`nsx_manager_username`

(optional) The SDDC includes an administrator username and initial password for NSX Manager. You can change this initial username to a different value in NSX Manager.

`ssh_authorized_keys`

(required) One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file. This attribute is not guaranteed to reflect the public SSH keys currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the public SSH keys that Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different SSH keys, you should use`UPDATE_SDDC`Function to update the SDDC's `sshAuthorizedKeys` with the new public keys.

`nsx_edge_uplink_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PrivateIp` object that is the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for route table rules when setting up connectivity between the SDDC and other networks. For information about `PrivateIp` objects, see the Core Services API.

`hcx_private_ip_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `PrivateIp` object that is the virtual IP (VIP) for HCX Manager. For information about `PrivateIp` objects, see the Core Services API.

`hcx_fqdn`

(optional) The FQDN for HCX Manager. Example: `hcx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`

`hcx_mode`

(required) HCX configuration of the SDDC.

Allowed values are: 'DISABLED', 'ADVANCED', 'ENTERPRISE'

`initial_configuration`

(required)

`is_hcx_pending_downgrade`

(optional) Indicates whether SDDC is pending downgrade from HCX Enterprise to HCX Advanced.

`hcx_on_prem_licenses`

(optional) The activation licenses to use on the on-premises HCX Enterprise appliance you site pair with HCX Manager in your VMware Solution.

`time_hcx_billing_cycle_end`

(optional) The date and time current HCX Enterprise billing cycle ends, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_hcx_license_status_updated`

(optional) The date and time the SDDC's HCX on-premise license status was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`is_single_host_sddc`

(optional) Indicates whether this SDDC is designated for only single ESXi host.

`time_created`

(required) The date and time the SDDC was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the SDDC was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the SDDC.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_SDDC_SUMMARY_T Type

A summary of the SDDC.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the SDDC.

`display_name`

(required) A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.

`vmware_software_version`

(required) In general, this is a specific version of bundled VMware software supported by Oracle Cloud VMware Solution (see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function). This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with`CREATE_ESXI_HOST`Function. Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer version of bundled VMware software supported by the Oracle Cloud VMware Solution, you should use`UPDATE_SDDC`Function to update the SDDC's `vmwareSoftwareVersion` with that new version.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the SDDC.

`clusters_count`

(required) The number of ESXi hosts in the SDDC.

`hcx_fqdn`

(optional) HCX Fully Qualified Domain Name

`hcx_mode`

(optional) HCX configuration of the SDDC.

Allowed values are: 'DISABLED', 'ADVANCED', 'ENTERPRISE'

`vcenter_fqdn`

(optional) FQDN for vCenter Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`

`nsx_manager_fqdn`

(optional) FQDN for NSX Manager Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`

`time_created`

(optional) The date and time the SDDC was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_updated`

(optional) The date and time the SDDC was updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) The current state of the SDDC.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`is_single_host_sddc`

(optional) Indicates whether this SDDC is designated for only single ESXi host.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_SDDC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_sddc_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SDDC_COLLECTION_T Type

A list of SDDCs.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of SDDCs.

### DBMS_CLOUD_OCI_OCVP_SDDC_PASSWORD_T Type

SDDC vCenter/NSX/HCX password.

Syntax
```

```

Fields

Field Description

`password_type`

(required) SDDC password type.

Allowed values are: 'VCENTER', 'NSX', 'HCX'

`value`

(required) SDDC vCenter/NSX/HCX password context.

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_T Type

A specific Commitment.

Syntax
```

```

Fields

Field Description

`name`

(required) name of Commitment

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_supported_commitment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_COLLECTION_T Type

A specific Commitment.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the supported Commitments.

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_ESXI_SOFTWARE_VERSION_SUMMARY_T Type

A specific version of bundled ESXi software supported by the Oracle Cloud VMware Solution.

Syntax
```

```

Fields

Field Description

`version`

(required) A short, unique string that identifies the version of bundled software.

`description`

(required) A description of the software in the bundle.

`supported_host_shape_names`

(required) A list of ESXi host shapes supported by the version of bundled software.

### DBMS_CLOUD_OCI_OCVP_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_SUMMARY_T Type

A specific compute shape supported by the Oracle Cloud VMware Solution.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the supported compute shape.

`supported_operations`

(required) The operations where you can use the shape. The operations can be CREATE_SDDC or CREATE_ESXI_HOST.

Allowed values are: 'CREATE_SDDC', 'DELETE_SDDC', 'CREATE_CLUSTER', 'DELETE_CLUSTER', 'CREATE_ESXI_HOST', 'DELETE_ESXI_HOST', 'UPGRADE_HCX', 'DOWNGRADE_HCX', 'CANCEL_DOWNGRADE_HCX', 'REFRESH_HCX_LICENSE_STATUS', 'SWAP_BILLING', 'REPLACE_HOST', 'IN_PLACE_UPGRADE'

`shape_family`

(required) The family of the shape. ESXi hosts of one SDDC must have the same shape family.

`default_ocpu_count`

(optional) The default OCPU count of the shape.

`supported_ocpu_count`

(optional) Support OCPU count of the shape.

`is_single_host_sddc_supported`

(optional) Indicates whether the shape supports single host SDDCs.

`supported_vmware_software_versions`

(optional) The VMware software versions supported by the shape.

`description`

(optional) Description of the shape.

`is_support_shielded_instances`

(optional) Indicates whether the shape supports shielded instances.

`is_support_monthly_commitment`

(optional) Whether the shape supports \"MONTH\" Commitment.

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_supported_host_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_COLLECTION_T Type

A list of compute shapes supported by the Oracle Cloud VMware Solution.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the supported compute shapes for ESXi hosts.

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_ESXI_SOFTWARE_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_supported_esxi_software_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_SUMMARY_T Type

A specific version of bundled VMware software supported by the Oracle Cloud VMware Solution.

Syntax
```

```

Fields

Field Description

`version`

(required) A short, unique string that identifies the version of bundled software.

`description`

(required) A description of the software in the bundle.

`esxi_software_versions`

(optional) A list of supported ESXi software versions.

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_supported_vmware_software_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_COLLECTION_T Type

A list of the supported versions of bundled VMware software.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the supported versions of bundled VMware software.

### DBMS_CLOUD_OCI_OCVP_UPDATE_CLUSTER_DETAILS_T Type

The Cluster information to be updated. **Important:** Only the `displayName`, `freeFormTags`, and `definedTags` attributes affect the existing Cluster. Changing the other attributes affects the `Cluster` object, but not the VMware environment currently running on that Cluster. Those other attributes are used by the Oracle Cloud VMware Solution *only* for new ESXi hosts that you add to this Cluster in the future with`CREATE_ESXI_HOST`Function.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Cluster. Cluster name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.

`network_configuration`

(optional)

`vmware_software_version`

(optional) The version of bundled VMware software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this Cluster in the future. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`esxi_software_version`

(optional) The version of bundled ESXi software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this Cluster in the future unless a specific version is configured on the ESXi level. To get a list of the available versions, use`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_UPDATE_ESXI_HOST_DETAILS_T Type

The ESXi host information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A descriptive name for the ESXi host. It's changeable. Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the Cluster. Avoid entering confidential information.

`next_commitment`

(optional) The billing option to switch to after the existing billing cycle ends. If `nextCommitment` is null or empty, `currentCommitment` continues to the next billing cycle.`LIST_SUPPORTED_COMMITMENTS`Function.

Allowed values are: 'HOUR', 'MONTH', 'ONE_YEAR', 'THREE_YEARS'

`billing_donor_host_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deleted ESXi Host with LeftOver billing cycle.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_UPDATE_SDDC_DETAILS_T Type

The SDDC information to be updated. **Important:** Only the `displayName`, `freeFormTags`, and `definedTags` attributes affect the existing SDDC. Changing the other attributes affects the `Sddc` object, but not the VMware environment currently running on that SDDC. Those other attributes are used by the Oracle Cloud VMware Solution *only* for new ESXi hosts that you add to this SDDC in the future with`CREATE_ESXI_HOST`Function.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region.

`vmware_software_version`

(optional) The version of bundled VMware software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this SDDC in the future unless a specific version is configured on the Cluster level. For the list of versions supported by the Oracle Cloud VMware Solution, see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function).

`esxi_software_version`

(optional) The version of bundled ESXi software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you add to this SDDC in the future unless a specific version is configured on the Cluster level. For the list of versions supported by the Oracle Cloud VMware Solution, see`LIST_SUPPORTED_VMWARE_SOFTWARE_VERSIONS`Function).

`ssh_authorized_keys`

(optional) One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host, only when adding new ESXi hosts to this SDDC. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_RESOURCE_T Type

A resource that is created or operated on by an asynchronous operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource was affected by the operation that spawned the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_ocvp_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_SDDC', 'DELETE_SDDC', 'CREATE_CLUSTER', 'DELETE_CLUSTER', 'CREATE_ESXI_HOST', 'DELETE_ESXI_HOST', 'UPGRADE_HCX', 'DOWNGRADE_HCX', 'CANCEL_DOWNGRADE_HCX', 'REFRESH_HCX_LICENSE_STATUS', 'SWAP_BILLING', 'REPLACE_HOST', 'IN_PLACE_UPGRADE'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` OR `SUCCEEDED`. Format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_ocvp_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_COLLECTION_T Type

A list of work requests.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work requests.

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_ocvp_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_COLLECTION_T Type

A list of work request errors.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_ocvp_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

A list of work request logs.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request logs.

- [OCVP Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-F9ACF1E6-BFBE-4E8D-BC31-DAFE7C641F1D)
- [DBMS_CLOUD_OCI_OCVP_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-7BA030F2-D565-4740-822A-8FBF66A1BA93)
- [DBMS_CLOUD_OCI_OCVP_CHANGE_SDDC_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-4230AC86-7CFC-4FC9-8587-E808FABFE25E)
- [DBMS_CLOUD_OCI_OCVP_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-502FC65F-653C-4492-B4F6-2439CEA2F6A4)
- [DBMS_CLOUD_OCI_OCVP_VSPHERE_LICENSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-A31460BF-2BD4-423F-A8DA-D5A751E25F64)
- [DBMS_CLOUD_OCI_OCVP_VSPHERE_UPGRADE_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-73612796-3BB9-41AD-9DAE-7574C1C2A44E)
- [DBMS_CLOUD_OCI_OCVP_DATASTORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-5136AD1F-BE45-4277-9C97-82812A73B9BD)
- [DBMS_CLOUD_OCI_OCVP_VSPHERE_LICENSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-662A0BAE-C200-4DE3-BF47-E18336D0A155)
- [DBMS_CLOUD_OCI_OCVP_VSPHERE_UPGRADE_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-90518264-5121-409A-A0C1-8D7E2EE8EAAB)
- [DBMS_CLOUD_OCI_OCVP_DATASTORE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-EC565C11-C933-4D27-9E3E-C88D3370C247)
- [DBMS_CLOUD_OCI_OCVP_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-2DA0ED9D-4FF6-44CB-BD32-59F183419CF7)
- [DBMS_CLOUD_OCI_OCVP_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-77A4161D-3E25-48B9-A25F-6E1D160CC6FA)
- [DBMS_CLOUD_OCI_OCVP_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-11CBA348-B4CC-4717-857B-49ECE1661215)
- [DBMS_CLOUD_OCI_OCVP_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-80EDBF8D-FA57-44D3-86C3-95DC6E6BD4C9)
- [DBMS_CLOUD_OCI_OCVP_DATASTORE_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-AEC34B00-0413-4BF8-B893-29C1D94E111D)
- [DBMS_CLOUD_OCI_OCVP_DATASTORE_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-5E35998F-F32D-404E-81B3-74D12178C1ED)
- [DBMS_CLOUD_OCI_OCVP_CREATE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-F9288819-B7A8-4908-A3E0-2DEDCC6C44B2)
- [DBMS_CLOUD_OCI_OCVP_CREATE_ESXI_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-2A73F7F6-2352-4DD6-99F9-2203261241D7)
- [DBMS_CLOUD_OCI_OCVP_INITIAL_CLUSTER_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-4CAA7B69-1E66-4016-9350-82B96B1145DD)
- [DBMS_CLOUD_OCI_OCVP_INITIAL_CLUSTER_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-1213396A-130C-4B17-AC72-42E0DE1BCFCC)
- [DBMS_CLOUD_OCI_OCVP_INITIAL_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-7CF08222-6B39-48FA-86BA-92AD6EFD0DBA)
- [DBMS_CLOUD_OCI_OCVP_CREATE_SDDC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-FB6AC289-5FEA-45C1-AC10-F138C96B3F0E)
- [DBMS_CLOUD_OCI_OCVP_DOWNGRADE_HCX_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-144D0617-85E8-434A-9A8B-AC30514390AC)
- [DBMS_CLOUD_OCI_OCVP_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-E2F30022-2B26-49B3-ACB6-E536C2980E2C)
- [DBMS_CLOUD_OCI_OCVP_ESXI_HOST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-ADE30462-CB00-44DA-88BC-6DD6A35A4C4C)
- [DBMS_CLOUD_OCI_OCVP_ESXI_HOST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-C4F6E0CB-7F83-45B2-9EFA-76818A600ABE)
- [DBMS_CLOUD_OCI_OCVP_ESXI_HOST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-B6AEBCAD-595C-49E4-920A-4E67FBA821B4)
- [DBMS_CLOUD_OCI_OCVP_ESXI_HOST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-74658FDD-70D9-4730-9C60-7FDF1FD3929F)
- [DBMS_CLOUD_OCI_OCVP_HCX_LICENSE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-C22366CF-CEBF-48A4-9E5D-3C5DC8A2921C)
- [DBMS_CLOUD_OCI_OCVP_REPLACE_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-C73BB2E0-8D61-4D61-9715-7D9399DDB837)
- [DBMS_CLOUD_OCI_OCVP_HCX_LICENSE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-7E514372-76A6-4A47-A204-03EF444B08DE)
- [DBMS_CLOUD_OCI_OCVP_SDDC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-63578FD8-A761-4334-B8F3-D387B5478ED3)
- [DBMS_CLOUD_OCI_OCVP_SDDC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-BFE17FC9-9FC0-4A74-B9E0-F4021621304C)
- [DBMS_CLOUD_OCI_OCVP_SDDC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-495255F6-3598-443B-BB79-827E7A6E690B)
- [DBMS_CLOUD_OCI_OCVP_SDDC_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-BCF91009-B35B-4C82-964B-A0C773718FEC)
- [DBMS_CLOUD_OCI_OCVP_SDDC_PASSWORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-9B9E4777-8B62-4ED0-BE5C-FF9174EE5964)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-A5F62C88-84D3-465D-A640-1CB669989D96)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-6BB2193B-42D9-4DCF-8F1A-F234582FFAFF)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_COMMITMENT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-B2DA8F06-9988-420B-A932-1B9DF418536C)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_ESXI_SOFTWARE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-AD402525-FE97-42ED-9B24-AA006F20CBC1)
- [DBMS_CLOUD_OCI_OCVP_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-C9F969E5-CFAB-4C4F-80ED-BDE0F0B6C75A)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-98A3F02E-ACA9-464B-99E4-F04DF24D10F3)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-3B400CD7-8E0C-4EEA-9D62-5BA5AAE4E75D)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_HOST_SHAPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-920A63C4-9EC9-44E1-993F-B7BFF7A73C9D)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_ESXI_SOFTWARE_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-308C89CE-E701-4EF0-AC37-22790D397B20)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-37BAF55B-8C57-42F5-AD55-2A342E08349B)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-85E4CE2B-42E5-4608-BCCE-ABC4FCB9B3AE)
- [DBMS_CLOUD_OCI_OCVP_SUPPORTED_VMWARE_SOFTWARE_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-26136C7A-3E81-4B69-8148-50A65303F133)
- [DBMS_CLOUD_OCI_OCVP_UPDATE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-D284E7C1-6568-482A-8C24-B10AF8B11EDA)
- [DBMS_CLOUD_OCI_OCVP_UPDATE_ESXI_HOST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-706BC870-DA73-4E29-9435-530AF3C4BE36)
- [DBMS_CLOUD_OCI_OCVP_UPDATE_SDDC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-B1AF3841-8A0D-4046-9B67-8375FCF43C39)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-134A7965-9F50-429E-97B3-73C64F807F5B)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-FB23935F-7529-4EA2-AF46-5288CB62BEBE)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-55C1235A-8CF8-4819-B58F-2C31C9A09D0B)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-D0A71DD1-3060-41DF-B01E-C1801FBA2A63)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-5452F02B-9046-4875-A200-41F8DB086C65)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-34383DEF-A6CB-4452-A8D0-CE0A06C73448)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-00FE6B01-9C2D-4461-8805-F750CECDEEB4)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-1E57253D-ABA7-47F9-9ED2-8BDE6D8752CF)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-8432D8DC-EB17-47FB-9443-BFD7FE82B35A)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-F21484C5-AB88-4143-B70A-A4E93D4A09F3)
- [DBMS_CLOUD_OCI_OCVP_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ocvp_t.html#ADSDK-GUID-5A74B870-0870-4161-A7AA-3894941EFD84)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
