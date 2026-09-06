# Container Engine Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#dcoc-content-body)

## Container Engine Common Types

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADD_ON_OPTIONS_T Type

The properties that define options for supported add-ons.

Syntax
```

```

Fields

Field Description

`is_kubernetes_dashboard_enabled`

(optional) Whether or not to enable the Kubernetes Dashboard add-on.

`is_tiller_enabled`

(optional) Whether or not to enable the Tiller add-on.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_CONFIGURATION_T Type

Defines the configuration of available addons for a cluster

Syntax
```

```

Fields

Field Description

`key`

(optional) configuration key name

`value`

(optional) configuration value name

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_ERROR_T Type

The error info of the addon.

Syntax
```

```

Fields

Field Description

`code`

(optional) A short error code that defines the upstream error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(optional) A human-readable error string of the upstream error.

`status`

(optional) The status of the HTTP response encountered in the upstream error.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_container_engine_addon_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_T Type

The properties that define an addon.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the addon.

`version`

(optional) selected addon version, or null indicates autoUpdate

`current_installed_version`

(optional) current installed version of the addon

`time_created`

(optional) The time the cluster was created.

`lifecycle_state`

(required) The state of the addon.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'UPDATING', 'NEEDS_ATTENTION', 'FAILED'

`configurations`

(optional) Addon configuration details.

`addon_error`

(optional) The error info of the addon.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KUBERNETES_VERSIONS_FILTERS_T Type

The range of kubernetes versions an addon can be configured.

Syntax
```

```

Fields

Field Description

`minimal_version`

(optional) The earliest kubernetes version.

`maximum_version`

(optional) The latest kubernetes version.

`exact_kubernetes_versions`

(optional) The exact version of kubernetes that are compatible.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSION_CONFIGURATION_T Type

Addon version configuration details.

Syntax
```

```

Fields

Field Description

`is_required`

(optional) If the the configuration is required or not.

`key`

(optional) Addon configuration key

`value`

(optional) Addon configuration value

`display_name`

(optional) Display name of addon version.

`description`

(optional) Information about the addon version configuration.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSION_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_container_engine_addon_version_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSIONS_T Type

The properties that define a work request resource.

Syntax
```

```

Fields

Field Description

`status`

(optional) Current state of the addon, only active will be visible to customer, visibility of versions in other status will be filtered based on limits property.

Allowed values are: 'ACTIVE', 'DEPRECATED', 'PREVIEW', 'RECALLED'

`version_number`

(optional) Version number, need be comparable within an addon.

`description`

(optional) Information about the addon version.

`kubernetes_version_filters`

(optional) The range of kubernetes versions an addon can be configured.

`configurations`

(optional) Addon version configuration details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSIONS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_addon_versions_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_OPTION_SUMMARY_T Type

The properties that define addon summary.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the addon and it would be unique.

`addon_schema_version`

(optional) Addon definition schema version to validate addon.

`addon_group`

(optional) Addon group info, a namespace concept that groups addons with similar functionalities.

`lifecycle_state`

(required) The life cycle state of the addon.

Allowed values are: 'ACTIVE', 'INACTIVE'

`description`

(optional) Description on the addon.

`is_essential`

(required) Is it an essential addon for cluster operation or not.

`versions`

(required) The resources this work request affects.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(optional) The time the work request was created.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_SUMMARY_T Type

The properties that define an addon summary.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the addon.

`version`

(optional) selected addon version, or null indicates autoUpdate

`current_installed_version`

(optional) current installed version of the addon

`time_created`

(optional) The time the cluster was created.

`lifecycle_state`

(required) The state of the addon.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'UPDATING', 'NEEDS_ATTENTION', 'FAILED'

`addon_error`

(optional) The error info of the addon.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADMISSION_CONTROLLER_OPTIONS_T Type

The properties that define supported admission controllers.

Syntax
```

```

Fields

Field Description

`is_pod_security_policy_enabled`

(optional) Whether or not to enable the Pod Security Policy admission controller.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_ENDPOINT_CONFIG_T Type

The properties that define the network configuration for the Cluster endpoint.

Syntax
```

```

Fields

Field Description

`subnet_id`

(optional) The OCID of the regional subnet in which to place the Cluster endpoint.

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`is_public_ip_enabled`

(optional) Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster provisioning will fail.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KUBERNETES_NETWORK_CONFIG_T Type

The properties that define the network configuration for Kubernetes.

Syntax
```

```

Fields

Field Description

`pods_cidr`

(optional) The CIDR block for Kubernetes pods. Optional, defaults to 10.244.0.0/16.

`services_cidr`

(optional) The CIDR block for Kubernetes services. Optional, defaults to 10.96.0.0/16.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_PERSISTENT_VOLUME_CONFIG_DETAILS_T Type

Configuration to be applied to block volumes created by Kubernetes Persistent Volume Claims (PVC)

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SERVICE_LB_CONFIG_DETAILS_T Type

Configuration to be applied to load balancers created by Kubernetes services

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_CREATE_OPTIONS_T Type

The properties that define extra options for a cluster.

Syntax
```

```

Fields

Field Description

`service_lb_subnet_ids`

(optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`kubernetes_network_config`

(optional) Network configuration for Kubernetes.

`add_ons`

(optional) Configurable cluster add-ons

`admission_controller_options`

(optional) Configurable cluster admission controllers

`persistent_volume_config`

(optional)

`service_lb_config`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_METADATA_T Type

The properties that define meta data for a cluster.

Syntax
```

```

Fields

Field Description

`time_created`

(optional) The time the cluster was created.

`created_by_user_id`

(optional) The user who created the cluster.

`created_by_work_request_id`

(optional) The OCID of the work request which created the cluster.

`time_deleted`

(optional) The time the cluster was deleted.

`deleted_by_user_id`

(optional) The user who deleted the cluster.

`deleted_by_work_request_id`

(optional) The OCID of the work request which deleted the cluster.

`time_updated`

(optional) The time the cluster was updated.

`updated_by_user_id`

(optional) The user who updated the cluster.

`updated_by_work_request_id`

(optional) The OCID of the work request which updated the cluster.

`time_credential_expiration`

(optional) The time until which the cluster credential is valid.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_ENDPOINTS_T Type

The properties that define endpoints for a cluster.

Syntax
```

```

Fields

Field Description

`kubernetes`

(optional) The non-native networking Kubernetes API server endpoint.

`public_endpoint`

(optional) The public native networking Kubernetes API server endpoint, if one was requested.

`private_endpoint`

(optional) The private native networking Kubernetes API server endpoint.

`vcn_hostname_endpoint`

(optional) The FQDN assigned to the Kubernetes API private endpoint. Example: 'https://yourVcnHostnameEndpoint'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_DETAILS_T Type

The properties that define the kms keys used by OKE for Image Signature verification.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(optional) The OCIDs of the KMS key that will be used to verify whether the images are signed by an approved source.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_key_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_IMAGE_POLICY_CONFIG_T Type

The properties that define a image verification policy.

Syntax
```

```

Fields

Field Description

`is_policy_enabled`

(optional) Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at runtime.

`key_details`

(optional) A list of KMS key details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type

The CNI type and relevant network details potentially applicable to the node pools of the cluster

Syntax
```

```

Fields

Field Description

`cni_type`

(required) The CNI used by the node pools of this cluster

Allowed values are: 'OCI_VCN_IP_NATIVE', 'FLANNEL_OVERLAY'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_POD_NETWORK_OPTION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_cluster_pod_network_option_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_T Type

A Kubernetes cluster. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the cluster.

`name`

(optional) The name of the cluster.

`compartment_id`

(optional) The OCID of the compartment in which the cluster exists.

`endpoint_config`

(optional) The network configuration for access to the Cluster control plane.

`vcn_id`

(optional) The OCID of the virtual cloud network (VCN) in which the cluster exists.

`kubernetes_version`

(optional) The version of Kubernetes running on the cluster masters.

`kms_key_id`

(optional) The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`options`

(optional) Optional attributes for the cluster.

`metadata`

(optional) Metadata about the cluster.

`lifecycle_state`

(optional) The state of the cluster masters.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`lifecycle_details`

(optional) Details about the state of the cluster masters.

`endpoints`

(optional) Endpoints served up by the cluster masters.

`available_kubernetes_upgrades`

(optional) Available Kubernetes versions to which the clusters masters may be upgraded.

`image_policy_config`

(optional) The image verification policy for signature validation.

`cluster_pod_network_options`

(optional) Available CNIs and network options for existing and new node pools of the cluster

`l_type`

(optional) Type of cluster

Allowed values are: 'BASIC_CLUSTER', 'ENHANCED_CLUSTER'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_MIGRATE_TO_NATIVE_VCN_DETAILS_T Type

The properties that define a request to migrate a cluster to Native VCN.

Syntax
```

```

Fields

Field Description

`endpoint_config`

(required) The network configuration for access to the Cluster control plane.

`decommission_delay_duration`

(optional) The optional override of the non-native endpoint decommission time after migration is complete. Defaults to 30 days.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_MIGRATE_TO_NATIVE_VCN_STATUS_T Type

Information regarding a cluster's move to Native VCN.

Syntax
```

```

Fields

Field Description

`time_decommission_scheduled`

(optional) The date and time the non-native VCN is due to be decommissioned.

`state`

(required) The current migration status of the cluster.

Allowed values are: 'NOT_STARTED', 'REQUESTED', 'IN_PROGRESS', 'PENDING_DECOMMISSION', 'COMPLETED'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_OPTIONS_T Type

Options for creating or updating clusters.

Syntax
```

```

Fields

Field Description

`kubernetes_versions`

(optional) Available Kubernetes versions.

`cluster_pod_network_options`

(optional) Available CNIs and network options for existing and new node pools of the cluster

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_SUMMARY_T Type

The properties that define a cluster summary.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the cluster.

`name`

(optional) The name of the cluster.

`compartment_id`

(optional) The OCID of the compartment in which the cluster exists.

`endpoint_config`

(optional) The network configuration for access to the Cluster control plane.

`vcn_id`

(optional) The OCID of the virtual cloud network (VCN) in which the cluster exists

`kubernetes_version`

(optional) The version of Kubernetes running on the cluster masters.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`options`

(optional) Optional attributes for the cluster.

`metadata`

(optional) Metadata about the cluster.

`lifecycle_state`

(optional) The state of the cluster masters.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`lifecycle_details`

(optional) Details about the state of the cluster masters.

`endpoints`

(optional) Endpoints served up by the cluster masters.

`available_kubernetes_upgrades`

(optional) Available Kubernetes versions to which the clusters masters may be upgraded.

`image_policy_config`

(optional) The image verification policy for signature validation.

`cluster_pod_network_options`

(optional) Available CNIs and network options for existing and new node pools of the cluster

`l_type`

(optional) Type of cluster. Values can be BASIC_CLUSTER or ENHANCED_CLUSTER. For more information, see[Cluster Types](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm)

Allowed values are: 'BASIC_CLUSTER', 'ENHANCED_CLUSTER'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_ENDPOINT_CONFIG_DETAILS_T Type

The properties that define the network configuration for the Cluster endpoint.

Syntax
```

```

Fields

Field Description

`subnet_id`

(optional) The OCID of the regional subnet in which to place the Cluster endpoint.

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`is_public_ip_enabled`

(optional) Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster provisioning will fail.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_IMAGE_POLICY_CONFIG_DETAILS_T Type

The properties that define a image verification policy.

Syntax
```

```

Fields

Field Description

`is_policy_enabled`

(optional) Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at runtime.

`key_details`

(optional) A list of KMS key details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_DETAILS_T Type

The properties that define a request to create a cluster.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the cluster. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment in which to create the cluster.

`endpoint_config`

(optional) The network configuration for access to the Cluster control plane.

`vcn_id`

(required) The OCID of the virtual cloud network (VCN) in which to create the cluster.

`kubernetes_version`

(required) The version of Kubernetes to install into the cluster masters.

`kms_key_id`

(optional) The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption. When used, `kubernetesVersion` must be at least `v1.13.0`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`options`

(optional) Optional attributes for the cluster.

`image_policy_config`

(optional) The image verification policy for signature validation. Once a policy is created and enabled with one or more kms keys, the policy will ensure all images deployed has been signed with the key(s) attached to the policy.

`cluster_pod_network_options`

(optional) Available CNIs and network options for existing and new node pools of the cluster

`l_type`

(optional) Type of cluster

Allowed values are: 'BASIC_CLUSTER', 'ENHANCED_CLUSTER'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_KUBECONFIG_CONTENT_DETAILS_T Type

The properties that define a request to create a cluster kubeconfig.

Syntax
```

```

Fields

Field Description

`token_version`

(optional) The version of the kubeconfig token. Supported value 2.0.0

`expiration`

(optional) Deprecated. This field is no longer used.

`endpoint`

(optional) The endpoint to target. A cluster may have multiple endpoints exposed but the kubeconfig can only target one at a time.

Allowed values are: 'LEGACY_KUBERNETES', 'PUBLIC_ENDPOINT', 'PRIVATE_ENDPOINT', 'VCN_HOSTNAME'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_DETAILS_T Type

The details of the node's source.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type for the node. Use `IMAGE` when specifying an OCID of an image.

Allowed values are: 'IMAGE'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration of the nodes.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to each node in the node pool. See[here](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Shape/)for details.

`memory_in_g_bs`

(optional) The total amount of memory available to each node, in gigabytes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_VALUE_T Type

The properties that define a key value pair.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the pair.

`value`

(optional) The value of the pair.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_PREEMPTION_ACTION_T Type

The action to run when the preemptible node is interrupted for eviction.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of action to run when the instance is interrupted for eviction.

Allowed values are: 'TERMINATE'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_PREEMPTIBLE_NODE_CONFIG_DETAILS_T Type

Configuration options for preemptible nodes.

Syntax
```

```

Fields

Field Description

`preemption_action`

(required)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_PLACEMENT_CONFIG_DETAILS_T Type

The location where a node pool will place nodes.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain in which to place nodes. Example: `Uocm:PHX-AD-1`

`subnet_id`

(required) The OCID of the subnet in which to place nodes.

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation in which to place the compute instance.

`preemptible_node_config`

(optional)

`fault_domains`

(optional) A list of fault domains in which to place nodes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type

The CNI type and relevant network details for the pods of a given node pool

Syntax
```

```

Fields

Field Description

`cni_type`

(required) The CNI plugin used by this node pool

Allowed values are: 'OCI_VCN_IP_NATIVE', 'FLANNEL_OVERLAY'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_PLACEMENT_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_node_pool_placement_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_POOL_NODE_CONFIG_DETAILS_T Type

The size and placement configuration of nodes in the node pool.

Syntax
```

```

Fields

Field Description

`l_size`

(required) The number of nodes that should be in the node pool.

`nsg_ids`

(optional) The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`kms_key_id`

(optional) The OCID of the Key Management Service key assigned to the boot volume.

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`placement_configs`

(required) The placement configurations for the node pool. Provide one placement configuration for each availability domain in which you intend to launch a node. To use the node pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

`node_pool_pod_network_option_details`

(optional) The CNI related configuration of pods in the node pool.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_EVICTION_NODE_POOL_SETTINGS_T Type

Node Eviction Details configuration

Syntax
```

```

Fields

Field Description

`eviction_grace_duration`

(optional) Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M

`is_force_delete_after_grace_duration`

(optional) If the underlying compute instance should be deleted if you cannot evict all the pods in grace period

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_CYCLING_DETAILS_T Type

Node Pool Cycling Details

Syntax
```

```

Fields

Field Description

`maximum_unavailable`

(optional) Maximum active nodes that would be terminated from nodepool during the cycling nodepool process. OKE supports both integer and percentage input. Defaults to 0, Ranges from 0 to Nodepool size or 0% to 100%

`maximum_surge`

(optional) Maximum additional new compute instances that would be temporarily created and added to nodepool during the cycling nodepool process. OKE supports both integer and percentage input. Defaults to 1, Ranges from 0 to Nodepool size or 0% to 100%

`is_node_cycling_enabled`

(optional) If nodes in the nodepool will be cycled to have new changes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_VALUE_TBL Type

Nested table type of dbms_cloud_oci_container_engine_key_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_POOL_DETAILS_T Type

The properties that define a request to create a node pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment in which the node pool exists.

`cluster_id`

(required) The OCID of the cluster to which this node pool is attached.

`name`

(required) The name of the node pool. Avoid entering confidential information.

`kubernetes_version`

(optional) The version of Kubernetes to install on the nodes in the node pool.

`node_metadata`

(optional) A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.

`node_image_name`

(optional) Deprecated. Use `nodeSourceDetails` instead. If you specify values for both, this value is ignored. The name of the image running on the nodes in the node pool.

`node_source_details`

(optional) Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.

`node_shape`

(required) The name of the node shape of the nodes in the node pool.

`node_shape_config`

(optional) Specify the configuration of the shape to launch nodes in the node pool.

`initial_node_labels`

(optional) A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`ssh_public_key`

(optional) The SSH public key on each node in the node pool on launch.

`quantity_per_subnet`

(optional) Optional, default to 1. The number of nodes to create in each subnet specified in subnetIds property. When used, subnetIds is required. This property is deprecated, use nodeConfigDetails instead.

`subnet_ids`

(optional) The OCIDs of the subnets in which to place nodes for this node pool. When used, quantityPerSubnet can be provided. This property is deprecated, use nodeConfigDetails. Exactly one of the subnetIds or nodeConfigDetails properties must be specified.

`node_config_details`

(optional) The configuration of nodes in the node pool. Exactly one of the subnetIds or nodeConfigDetails properties must be specified.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`node_eviction_node_pool_settings`

(optional)

`node_pool_cycling_details`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_INITIAL_VIRTUAL_NODE_LABEL_T Type

The properties that define a key value pair.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the pair.

`value`

(optional) The value of the pair.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_TAINT_T Type

taints

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the pair.

`value`

(optional) The value of the pair.

`effect`

(optional) The effect of the pair.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_PLACEMENT_CONFIGURATION_T Type

The information of virtual node placement in the virtual node pool.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain in which to place virtual nodes. Example: `Uocm:PHX-AD-1`

`fault_domain`

(optional) The fault domain of this virtual node.

`subnet_id`

(optional) The OCID of the subnet in which to place virtual nodes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_CONFIGURATION_T Type

The pod configuration for pods run on virtual nodes of this virtual node pool.

Syntax
```

```

Fields

Field Description

`subnet_id`

(required) The regional subnet where pods' VNIC will be placed.

`nsg_ids`

(optional) List of network security group IDs applied to the Pod VNIC.

`shape`

(required) Shape of the pods.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_TAGS_T Type

The tags associated to the virtual nodes in this virtual node pool.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_INITIAL_VIRTUAL_NODE_LABEL_TBL Type

Nested table type of dbms_cloud_oci_container_engine_initial_virtual_node_label_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_TAINT_TBL Type

Nested table type of dbms_cloud_oci_container_engine_taint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_PLACEMENT_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_container_engine_placement_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_VIRTUAL_NODE_POOL_DETAILS_T Type

The properties that define a request to create a virtual node pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Compartment of the virtual node pool.

`cluster_id`

(required) The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.

`display_name`

(required) Display name of the virtual node pool. This is a non-unique value.

`initial_virtual_node_labels`

(optional) Initial labels that will be added to the Kubernetes Virtual Node object when it registers.

`taints`

(optional) A taint is a collection of &lt;key, value, effect&gt;. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes scheduling.

`l_size`

(optional) The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.

`placement_configurations`

(required) The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability domains. The size attribute determines how many we evenly spread across these placement configurations

`nsg_ids`

(optional) List of network security group id's applied to the Virtual Node VNIC.

`pod_configuration`

(optional) The pod configuration for pods run on virtual nodes of this virtual node pool.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`virtual_node_tags`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_WORKLOAD_MAPPING_DETAILS_T Type

The properties that define a workloadMapping

Syntax
```

```

Fields

Field Description

`namespace`

(required) The namespace of the workloadMapping.

`mapped_compartment_id`

(required) The OCID of the mapped customer compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREDENTIAL_ROTATION_STATUS_T Type

Information regarding cluster's credential rotation.

Syntax
```

```

Fields

Field Description

`time_auto_completion_scheduled`

(optional) The time by which retirement of old credentials should start.

`status`

(required) Credential rotation status of a kubernetes cluster IN_PROGRESS: Issuing new credentials to kubernetes cluster control plane and worker nodes or retiring old credentials from kubernetes cluster control plane and worker nodes. WAITING: Waiting for customer to invoke the complete rotation action or the automcatic complete rotation action. COMPLETED: New credentials are functional on kuberentes cluster.

Allowed values are: 'IN_PROGRESS', 'WAITING', 'COMPLETED'

`status_details`

(required) Details of a kuberenetes cluster credential rotation status: ISSUING_NEW_CREDENTIALS: Credential rotation is in progress. Starting to issue new credentials to kubernetes cluster control plane and worker nodes. NEW_CREDENTIALS_ISSUED: New credentials are added. At this stage cluster has both old and new credentials and is awaiting old credentials retirement. RETIRING_OLD_CREDENTIALS: Retirement of old credentials is in progress. Starting to remove old credentials from kubernetes cluster control plane and worker nodes. COMPLETED: Credential rotation is complete. Old credentials are retired.

Allowed values are: 'ISSUING_NEW_CREDENTIALS', 'NEW_CREDENTIALS_ISSUED', 'RETIRING_OLD_CREDENTIALS', 'COMPLETED'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_ERROR_T Type

The properties that define an error.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_FLANNEL_OVERLAY_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type

Network options specific to using the flannel (FLANNEL_OVERLAY) CNI

Syntax
```

```

`dbms_cloud_oci_container_engine_flannel_overlay_cluster_pod_network_option_details_t`is a subtype of the`dbms_cloud_oci_container_engine_cluster_pod_network_option_details_t`type.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_FLANNEL_OVERLAY_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type

Network options specific to using the flannel (FLANNEL_OVERLAY) CNI

Syntax
```

```

`dbms_cloud_oci_container_engine_flannel_overlay_node_pool_pod_network_option_details_t`is a subtype of the`dbms_cloud_oci_container_engine_node_pool_pod_network_option_details_t`type.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_INSTALL_ADDON_DETAILS_T Type

The properties that define to install/enable addon on a cluster

Syntax
```

```

Fields

Field Description

`addon_name`

(required) The name of the addon.

`version`

(optional) The version of addon to be installed.

`configurations`

(optional) Addon configuration details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_ERROR_T Type

The properties that define an upstream error while managing a node.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the upstream error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string of the upstream error.

`status`

(optional) The status of the HTTP response encountered in the upstream error.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request, please provide the request ID.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_T Type

The properties that define a node.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the compute instance backing this node.

`name`

(optional) The name of the node.

`kubernetes_version`

(optional) The version of Kubernetes this node is running.

`availability_domain`

(optional) The name of the availability domain in which this node is placed.

`subnet_id`

(optional) The OCID of the subnet in which this node is placed.

`node_pool_id`

(optional) The OCID of the node pool to which this node belongs.

`fault_domain`

(optional) The fault domain of this node.

`private_ip`

(optional) The private IP address of this node.

`public_ip`

(optional) The public IP address of this node.

`node_error`

(optional) An error that may be associated with the node.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`lifecycle_state`

(optional) The state of the node.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILING', 'INACTIVE'

`lifecycle_details`

(optional) Details about the state of the node.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SHAPE_CONFIG_T Type

The shape configuration of the nodes.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to each node in the node pool. See[here](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Shape/)for details.

`memory_in_g_bs`

(optional) The total amount of memory available to each node, in gigabytes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_OPTION_T Type

The source option for the node.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type of this option. `IMAGE` means the OCID is of an image.

Allowed values are: 'IMAGE'

`source_name`

(optional) The user-friendly name of the entity corresponding to the OCID.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_NODE_CONFIG_DETAILS_T Type

The size and placement configuration of nodes in the node pool.

Syntax
```

```

Fields

Field Description

`l_size`

(optional) The number of nodes in the node pool.

`nsg_ids`

(optional) The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`kms_key_id`

(optional) The OCID of the Key Management Service key assigned to the boot volume.

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`placement_configs`

(optional) The placement configurations for the node pool. Provide one placement configuration for each availability domain in which you intend to launch a node. To use the node pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

`node_pool_pod_network_option_details`

(optional) The CNI related configuration of pods in the node pool.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_TBL Type

Nested table type of dbms_cloud_oci_container_engine_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_T Type

A pool of compute nodes attached to a cluster. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the node pool.

`lifecycle_state`

(optional) The state of the nodepool.

Allowed values are: 'DELETED', 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED', 'INACTIVE', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the nodepool.

`compartment_id`

(optional) The OCID of the compartment in which the node pool exists.

`cluster_id`

(optional) The OCID of the cluster to which this node pool is attached.

`name`

(optional) The name of the node pool.

`kubernetes_version`

(optional) The version of Kubernetes running on the nodes in the node pool.

`node_metadata`

(optional) A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.

`node_image_id`

(optional) Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.

`node_image_name`

(optional) Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.

`node_shape_config`

(optional) The shape configuration of the nodes.

`node_source`

(optional) Deprecated. see `nodeSourceDetails`. Source running on the nodes in the node pool.

`node_source_details`

(optional) Source running on the nodes in the node pool.

`node_shape`

(optional) The name of the node shape of the nodes in the node pool.

`initial_node_labels`

(optional) A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`ssh_public_key`

(optional) The SSH public key on each node in the node pool on launch.

`quantity_per_subnet`

(optional) The number of nodes in each subnet.

`subnet_ids`

(optional) The OCIDs of the subnets in which to place nodes for this node pool.

`nodes`

(optional) The nodes in the node pool.

`node_config_details`

(optional) The configuration of nodes in the node pool.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`node_eviction_node_pool_settings`

(optional)

`node_pool_cycling_details`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_OPTION_TBL Type

Nested table type of dbms_cloud_oci_container_engine_node_source_option_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_OPTIONS_T Type

Options for creating or updating node pools.

Syntax
```

```

Fields

Field Description

`kubernetes_versions`

(optional) Available Kubernetes versions.

`shapes`

(optional) Available shapes for nodes.

`images`

(optional) Deprecated. See sources. When creating a node pool using the `CreateNodePoolDetails` object, only image names contained in this property can be passed to the `nodeImageName` property.

`sources`

(optional) Available source of the node.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_SUMMARY_T Type

The properties that define a node pool summary.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the node pool.

`lifecycle_state`

(optional) The state of the nodepool.

Allowed values are: 'DELETED', 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED', 'INACTIVE', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the nodepool.

`compartment_id`

(optional) The OCID of the compartment in which the node pool exists.

`cluster_id`

(optional) The OCID of the cluster to which this node pool is attached.

`name`

(optional) The name of the node pool.

`kubernetes_version`

(optional) The version of Kubernetes running on the nodes in the node pool.

`node_image_id`

(optional) Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.

`node_image_name`

(optional) Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.

`node_shape_config`

(optional) The shape configuration of the nodes.

`node_source`

(optional) Deprecated. see `nodeSourceDetails`. Source running on the nodes in the node pool.

`node_source_details`

(optional) Source running on the nodes in the node pool.

`node_shape`

(optional) The name of the node shape of the nodes in the node pool.

`initial_node_labels`

(optional) A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`ssh_public_key`

(optional) The SSH public key on each node in the node pool on launch.

`quantity_per_subnet`

(optional) The number of nodes in each subnet.

`subnet_ids`

(optional) The OCIDs of the subnets in which to place nodes for this node pool.

`node_config_details`

(optional) The configuration of nodes in the node pool.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`node_eviction_node_pool_settings`

(optional)

`node_pool_cycling_details`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_VIA_IMAGE_DETAILS_T Type

Details of the image running on the node.

Syntax
```

```

`dbms_cloud_oci_container_engine_node_source_via_image_details_t`is a subtype of the`dbms_cloud_oci_container_engine_node_source_details_t`type.

Fields

Field Description

`image_id`

(required) The OCID of the image used to boot the node.

`boot_volume_size_in_g_bs`

(optional) The size of the boot volume in GBs. Minimum value is 50 GB. See[here](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm)for max custom boot volume sizing and OS-specific requirements.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_VIA_IMAGE_OPTION_T Type

An image can be specified as the source of nodes when launching a node pool using the `nodeSourceDetails` object.

Syntax
```

```

`dbms_cloud_oci_container_engine_node_source_via_image_option_t`is a subtype of the`dbms_cloud_oci_container_engine_node_source_option_t`type.

Fields

Field Description

`image_id`

(optional) The OCID of the image.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_OCI_VCN_IP_NATIVE_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type

Network options specific to using the OCI VCN Native CNI

Syntax
```

```

`dbms_cloud_oci_container_engine_oci_vcn_ip_native_cluster_pod_network_option_details_t`is a subtype of the`dbms_cloud_oci_container_engine_cluster_pod_network_option_details_t`type.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_OCI_VCN_IP_NATIVE_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type

Network options specific to using the OCI VCN Native CNI

Syntax
```

```

`dbms_cloud_oci_container_engine_oci_vcn_ip_native_node_pool_pod_network_option_details_t`is a subtype of the`dbms_cloud_oci_container_engine_node_pool_pod_network_option_details_t`type.

Fields

Field Description

`max_pods_per_node`

(optional) The max number of pods per node in the node pool. This value will be limited by the number of VNICs attachable to the node pool shape

`pod_nsg_ids`

(optional) The OCIDs of the Network Security Group(s) to associate pods for this node pool with. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`pod_subnet_ids`

(required) The OCIDs of the subnets in which to place pods for this node pool. This can be one of the node pool subnet IDs

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_OCPU_OPTIONS_T Type

Properties of OCPUs.

Syntax
```

```

Fields

Field Description

`l_min`

(optional) The minimum number of OCPUs.

`l_max`

(optional) The maximum number of OCPUs.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_MEMORY_OPTIONS_T Type

Memory properties.

Syntax
```

```

Fields

Field Description

`min_in_g_bs`

(optional) The minimum amount of memory, in gigabytes.

`max_in_g_bs`

(optional) The maximum amount of memory, in gigabytes.

`default_per_ocpu_in_g_bs`

(optional) The default amount of memory per OCPU available for this shape, in gigabytes.

`min_per_ocpu_in_g_bs`

(optional) The minimum amount of memory per OCPU available for this shape, in gigabytes.

`max_per_ocpu_in_g_bs`

(optional) The maximum amount of memory per OCPU available for this shape, in gigabytes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_NETWORK_BANDWIDTH_OPTIONS_T Type

Properties of network bandwidth.

Syntax
```

```

Fields

Field Description

`min_in_gbps`

(optional) The minimum amount of networking bandwidth, in gigabits per second.

`max_in_gbps`

(optional) The maximum amount of networking bandwidth, in gigabits per second.

`default_per_ocpu_in_gbps`

(optional) The default amount of networking bandwidth per OCPU, in gigabits per second.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_OCPU_OPTIONS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_shape_ocpu_options_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_MEMORY_OPTIONS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_shape_memory_options_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_NETWORK_BANDWIDTH_OPTIONS_TBL Type

Nested table type of dbms_cloud_oci_container_engine_shape_network_bandwidth_options_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_SHAPE_T Type

Pod shape.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the identifying shape.

`processor_description`

(optional) A short description of the VM's processor (CPU).

`ocpu_options`

(optional) Options for OCPU shape.

`memory_options`

(optional) ShapeMemoryOptions.

`network_bandwidth_options`

(optional) ShapeNetworkBandwidthOptions.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_SHAPE_SUMMARY_T Type

Pod shape.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the identifying shape.

`processor_description`

(optional) A short description of the VM's processor (CPU).

`ocpu_options`

(optional) Options for OCPU shape.

`memory_options`

(optional) ShapeMemoryOptions.

`network_bandwidth_options`

(optional) ShapeNetworkBandwidthOptions.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_START_CREDENTIAL_ROTATION_DETAILS_T Type

Properties that define a request to start credential rotation on a kubernetes cluster.

Syntax
```

```

Fields

Field Description

`auto_completion_delay_duration`

(required) The duration in days(in ISO 8601 notation eg. P5D) after which the old credentials should be retired. Maximum delay duration is 14 days.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_TERMINATE_PREEMPTION_ACTION_T Type

Terminates the preemptible instance when it is interrupted for eviction.

Syntax
```

```

`dbms_cloud_oci_container_engine_terminate_preemption_action_t`is a subtype of the`dbms_cloud_oci_container_engine_preemption_action_t`type.

Fields

Field Description

`is_preserve_boot_volume`

(optional) Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_ADDON_DETAILS_T Type

The properties that define to update addon details.

Syntax
```

```

Fields

Field Description

`version`

(optional) The version of the installed addon.

`configurations`

(optional) Addon configuration details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_OPTIONS_DETAILS_T Type

The properties that define extra options updating a cluster.

Syntax
```

```

Fields

Field Description

`admission_controller_options`

(optional) Configurable cluster admission controllers

`persistent_volume_config`

(optional)

`service_lb_config`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_IMAGE_POLICY_CONFIG_DETAILS_T Type

The properties that define a image verification policy.

Syntax
```

```

Fields

Field Description

`is_policy_enabled`

(optional) Whether the image verification policy is enabled. Defaults to false. If set to true, the images will be verified against the policy at runtime.

`key_details`

(optional) A list of KMS key details.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_DETAILS_T Type

The properties that define a request to update a cluster.

Syntax
```

```

Fields

Field Description

`name`

(optional) The new name for the cluster. Avoid entering confidential information.

`kubernetes_version`

(optional) The version of Kubernetes to which the cluster masters should be upgraded.

`options`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`image_policy_config`

(optional) The image verification policy for signature validation. Once a policy is created and enabled with one or more kms keys, the policy will ensure all images deployed has been signed with the key(s) attached to the policy.

`l_type`

(optional) Type of cluster

Allowed values are: 'BASIC_CLUSTER', 'ENHANCED_CLUSTER'

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_ENDPOINT_CONFIG_DETAILS_T Type

The properties that define a request to update a cluster endpoint config.

Syntax
```

```

Fields

Field Description

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to apply to the cluster endpoint. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`is_public_ip_enabled`

(optional) Whether the cluster should be assigned a public IP address. Defaults to false. If set to true on a private subnet, the cluster update will fail.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_POOL_NODE_CONFIG_DETAILS_T Type

The size and placement configuration of nodes in the node pool.

Syntax
```

```

Fields

Field Description

`l_size`

(optional) The number of nodes in the node pool.

`nsg_ids`

(optional) The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`kms_key_id`

(optional) The OCID of the Key Management Service key assigned to the boot volume.

`is_pv_encryption_in_transit_enabled`

(optional) Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`placement_configs`

(optional) The placement configurations for the node pool. Provide one placement configuration for each availability domain in which you intend to launch a node. To use the node pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

`node_pool_pod_network_option_details`

(optional) The CNI related configuration of pods in the node pool.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_SHAPE_CONFIG_DETAILS_T Type

The shape configuration of the nodes.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs available to each node in the node pool. See[here](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Shape/)for details.

`memory_in_g_bs`

(optional) The total amount of memory available to each node, in gigabytes.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_POOL_DETAILS_T Type

The properties that define a request to update a node pool.

Syntax
```

```

Fields

Field Description

`name`

(optional) The new name for the cluster. Avoid entering confidential information.

`kubernetes_version`

(optional) The version of Kubernetes to which the nodes in the node pool should be upgraded.

`initial_node_labels`

(optional) A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

`quantity_per_subnet`

(optional) The number of nodes to have in each subnet specified in the subnetIds property. This property is deprecated, use nodeConfigDetails instead. If the current value of quantityPerSubnet is greater than 0, you can only use quantityPerSubnet to scale the node pool. If the current value of quantityPerSubnet is equal to 0 and the current value of size in nodeConfigDetails is greater than 0, before you can use quantityPerSubnet, you must first scale the node pool to 0 nodes using nodeConfigDetails.

`subnet_ids`

(optional) The OCIDs of the subnets in which to place nodes for this node pool. This property is deprecated, use nodeConfigDetails instead. Only one of the subnetIds or nodeConfigDetails properties can be specified.

`node_config_details`

(optional) The configuration of nodes in the node pool. Only one of the subnetIds or nodeConfigDetails properties should be specified. If the current value of quantityPerSubnet is greater than 0, the node pool may still be scaled using quantityPerSubnet. Before you can use nodeConfigDetails, you must first scale the node pool to 0 nodes using quantityPerSubnet.

`node_metadata`

(optional) A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.

`node_source_details`

(optional) Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.

`ssh_public_key`

(optional) The SSH public key to add to each node in the node pool on launch.

`node_shape`

(optional) The name of the node shape of the nodes in the node pool used on launch.

`node_shape_config`

(optional) Specify the configuration of the shape to launch nodes in the node pool.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`node_eviction_node_pool_settings`

(optional)

`node_pool_cycling_details`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_VIRTUAL_NODE_POOL_DETAILS_T Type

The properties that define a request to update a virtual node pool.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the virtual node pool. This is a non-unique value.

`initial_virtual_node_labels`

(optional) Initial labels that will be added to the Kubernetes Virtual Node object when it registers.

`taints`

(optional) A taint is a collection of &lt;key, value, effect&gt;. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes scheduling.

`l_size`

(optional) The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.

`placement_configurations`

(optional) The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability domains. The size attribute determines how many we evenly spread across these placement configurations

`nsg_ids`

(optional) List of network security group id's applied to the Virtual Node VNIC.

`pod_configuration`

(optional) The pod configuration for pods run on virtual nodes of this virtual node pool.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`virtual_node_tags`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_WORKLOAD_MAPPING_DETAILS_T Type

The properties that define a workloadMapping

Syntax
```

```

Fields

Field Description

`mapped_compartment_id`

(optional) The OCID of the mapped customer compartment.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_T Type

The properties that define a virtual node.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid of the virtual node.

`display_name`

(required) The name of the virtual node.

`kubernetes_version`

(optional) The version of Kubernetes this virtual node is running.

`virtual_node_pool_id`

(required) The ocid of the virtual node pool this virtual node belongs to.

`availability_domain`

(optional) The name of the availability domain in which this virtual node is placed

`fault_domain`

(optional) The fault domain of this virtual node.

`subnet_id`

(optional) The OCID of the subnet in which this Virtual Node is placed.

`nsg_ids`

(optional) NSG Ids applied to virtual node vnic.

`private_ip`

(optional) The private IP address of this Virtual Node.

`virtual_node_error`

(optional) An error that may be associated with the virtual node.

`lifecycle_state`

(optional) The state of the Virtual Node.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the Virtual Node.

`time_created`

(optional) The time at which the virtual node was created.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_POOL_T Type

A pool of virtual nodes attached to a cluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the virtual node pool.

`compartment_id`

(required) Compartment of the virtual node pool.

`cluster_id`

(required) The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.

`display_name`

(required) Display name of the virtual node pool. This is a non-unique value.

`kubernetes_version`

(required) The version of Kubernetes running on the nodes in the node pool.

`initial_virtual_node_labels`

(optional) Initial labels that will be added to the Kubernetes Virtual Node object when it registers. This is the same as virtualNodePool resources.

`taints`

(optional) A taint is a collection of &lt;key, value, effect&gt;. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes scheduling.

`l_size`

(optional) The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.

`placement_configurations`

(required) The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability domains. The size attribute determines how many we evenly spread across these placement configurations

`nsg_ids`

(optional) List of network security group id's applied to the Virtual Node VNIC.

`pod_configuration`

(optional) The pod configuration for pods run on virtual nodes of this virtual node pool.

`lifecycle_state`

(optional) The state of the Virtual Node Pool.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the Virtual Node Pool.

`time_created`

(optional) The time the virtual node pool was created.

`time_updated`

(optional) The time the virtual node pool was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`virtual_node_tags`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_POOL_SUMMARY_T Type

The properties that define a virtual node pool summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the virtual node pool.

`compartment_id`

(required) Compartment of the virtual node pool.

`cluster_id`

(required) The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.

`display_name`

(required) Display name of the virtual node pool. This is a non-unique value.

`kubernetes_version`

(required) The version of Kubernetes running on the nodes in the node pool.

`initial_virtual_node_labels`

(optional) Initial labels that will be added to the Kubernetes Virtual Node object when it registers. This is the same as virtualNodePool resources.

`taints`

(optional) A taint is a collection of &lt;key, value, effect&gt;. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes scheduling.

`l_size`

(optional) The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.

`placement_configurations`

(required) The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability domains. The size attribute determines how many we evenly spread across these placement configurations

`nsg_ids`

(optional) List of network security group id's applied to the Virtual Node VNIC.

`pod_configuration`

(optional) The pod configuration for pods run on virtual nodes of this virtual node pool.

`lifecycle_state`

(optional) The state of the Virtual Node Pool.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the Virtual Node Pool.

`time_created`

(optional) The time the virtual node pool was created.

`time_updated`

(optional) The time the virtual node pool was updated.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`virtual_node_tags`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_SUMMARY_T Type

The properties that define a virtual node summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid of the virtual node.

`display_name`

(required) The name of the virtual node.

`kubernetes_version`

(optional) The version of Kubernetes this virtual node is running.

`virtual_node_pool_id`

(required) The ocid of the virtual node pool this virtual node belongs to.

`availability_domain`

(optional) The name of the availability domain in which this virtual node is placed

`fault_domain`

(optional) The fault domain of this virtual node.

`subnet_id`

(optional) The OCID of the subnet in which this Virtual Node is placed.

`nsg_ids`

(optional) NSG Ids applied to virtual node vnic.

`private_ip`

(optional) The private IP address of this Virtual Node.

`virtual_node_error`

(optional) An error that may be associated with the virtual node.

`lifecycle_state`

(optional) The state of the Virtual Node.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`lifecycle_details`

(optional) Details about the state of the Virtual Node.

`time_created`

(optional) The time at which the virtual node was created.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_RESOURCE_T Type

The properties that define a work request resource.

Syntax
```

```

Fields

Field Description

`action_type`

(optional) The way in which this resource was affected by the work tracked by the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS', 'FAILED', 'CANCELED_CREATE', 'CANCELED_UPDATE', 'CANCELED_DELETE'

`entity_type`

(optional) The resource type the work request affects.

`identifier`

(optional) The OCID of the resource the work request affects.

`entity_uri`

(optional) The URI path on which the user can issue a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_container_engine_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the work request.

`operation_type`

(optional) The type of work the work request is doing.

Allowed values are: 'CLUSTER_CREATE', 'CLUSTER_UPDATE', 'CLUSTER_DELETE', 'NODEPOOL_CREATE', 'NODEPOOL_UPDATE', 'NODEPOOL_DELETE', 'NODEPOOL_RECONCILE', 'NODEPOOL_CYCLING', 'WORKREQUEST_CANCEL', 'VIRTUALNODEPOOL_CREATE', 'VIRTUALNODEPOOL_UPDATE', 'VIRTUALNODEPOOL_DELETE', 'VIRTUALNODE_DELETE', 'ENABLE_ADDON', 'UPDATE_ADDON', 'DISABLE_ADDON', 'RECONCILE_ADDON'

`status`

(optional) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(optional) The OCID of the compartment in which the work request exists.

`resources`

(optional) The resources this work request affects.

`time_accepted`

(optional) The time the work request was accepted.

`time_started`

(optional) The time the work request was started.

`time_finished`

(optional) The time the work request was finished.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_ERROR_T Type

Errors related to a specific work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_LOG_ENTRY_T Type

Log entries related to a specific work request.

Syntax
```

```

Fields

Field Description

`message`

(optional) The description of an action that occurred.

`l_timestamp`

(optional) The date and time the log entry occurred.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_SUMMARY_T Type

The properties that define a work request summary.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the work request.

`operation_type`

(optional) The type of work the work request is doing.

Allowed values are: 'CLUSTER_CREATE', 'CLUSTER_UPDATE', 'CLUSTER_DELETE', 'NODEPOOL_CREATE', 'NODEPOOL_UPDATE', 'NODEPOOL_DELETE', 'NODEPOOL_RECONCILE', 'NODEPOOL_CYCLING', 'WORKREQUEST_CANCEL', 'VIRTUALNODEPOOL_CREATE', 'VIRTUALNODEPOOL_UPDATE', 'VIRTUALNODEPOOL_DELETE', 'VIRTUALNODE_DELETE', 'ENABLE_ADDON', 'UPDATE_ADDON', 'DISABLE_ADDON', 'RECONCILE_ADDON'

`status`

(optional) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(optional) The OCID of the compartment in which the work request exists.

`resources`

(optional) The resources this work request affects.

`time_accepted`

(optional) The time the work request was accepted.

`time_started`

(optional) The time the work request was started.

`time_finished`

(optional) The time the work request was finished.

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORKLOAD_MAPPING_T Type

The properties that define an workloadMapping.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid of the workloadMapping.

`cluster_id`

(required) The OCID of the cluster.

`namespace`

(required) The namespace of the workloadMapping.

`mapped_tenancy_id`

(required) The OCID of the mapped customer tenancy.

`mapped_compartment_id`

(required) The OCID of the mapped customer compartment.

`time_created`

(required) The time the cluster was created.

`lifecycle_state`

(required) The state of the workloadMapping.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORKLOAD_MAPPING_SUMMARY_T Type

The properties that define an workloadMapping summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid of the workloadMapping.

`cluster_id`

(required) The OCID of the cluster.

`namespace`

(required) The namespace of the workloadMapping.

`mapped_tenancy_id`

(required) The OCID of the mapped customer tenancy.

`mapped_compartment_id`

(required) The OCID of the mapped customer compartment.

`time_created`

(required) The time the cluster was created.

`lifecycle_state`

(required) The state of the workloadMapping.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Container Engine Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-55994E97-5E77-4113-B05D-829A358B6EA3)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E3F658BD-F0F7-4CE5-AA21-2A3F427B96CC)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADD_ON_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3A5922D6-37ED-4CD0-AA32-214498519C38)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E9688A07-1F26-4A5E-A7D4-F7E1482AF623)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-BD86CD7C-31A3-4517-AE11-CBDE05B7E735)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-881BF533-59D3-4CA8-AAA3-BF58710EE78B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-D0045BC3-1CE9-4996-BF9E-0A2FEC0D15FB)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KUBERNETES_VERSIONS_FILTERS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-0772AA54-0018-41EF-88DE-C6EDB380D0B5)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSION_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DA6AD261-4FD4-4F18-B717-74ED2C08615B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSION_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-F7E4813D-54EC-46AD-835D-380F5886FB35)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9346A452-5BBD-408D-8092-B0CD4CA6C52D)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_VERSIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-174CC7BC-22AF-4CD3-80DF-9CCBA96F5EFE)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_OPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-B7CCE726-B9DD-4171-9A9D-90B16EF04365)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADDON_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-FB1D9D0B-82B9-4352-9453-8DCCC1F5CD8A)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ADMISSION_CONTROLLER_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-754AE283-535B-4F7E-A357-9978240F3E0E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_ENDPOINT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E83436B2-C978-4124-9C9C-504FE6EF0957)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KUBERNETES_NETWORK_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-24743A82-8727-428F-A662-BA398382A925)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_PERSISTENT_VOLUME_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-71B73269-8587-4AE0-BE92-162186165E8E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SERVICE_LB_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-0EBD702B-756B-4369-BC35-3F57CF2E4B9A)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_CREATE_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-00D3F242-F7BD-4508-B2B0-C85B009DAE68)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E41CDDC4-B8A4-4AC8-98C8-D9DFE1BA6E98)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_ENDPOINTS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C4FBB519-F137-46A9-802D-EF3A992FC72E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-1086434C-F1BA-49BE-BE1A-59AE85C9D12B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-A1343887-AA55-4AF0-89DD-1645A1BE58C3)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_IMAGE_POLICY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-532FBA71-4568-4725-B197-DC2C17844FA9)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E6CF9A9A-B12B-4CC3-B726-830605AF9DD0)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_POD_NETWORK_OPTION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-554D8F3E-B4F3-4AC5-8BD5-5D15CB7DE339)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-094D27A7-BBCE-4CD0-82F8-1FCF522370D2)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_MIGRATE_TO_NATIVE_VCN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C3829AAF-63DC-4052-AB14-A6DB78C898FB)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_MIGRATE_TO_NATIVE_VCN_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-107902B3-25C5-4479-B882-23D225B56AD6)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DBA2F86B-04E0-4174-BDCB-4EBC90833F23)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-B027D460-24BE-4E53-B746-FBE07129E604)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_ENDPOINT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C7CC04D6-8EBE-46F9-BDE7-7337BD016785)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_IMAGE_POLICY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-CAE40B72-F006-48B5-85B1-58AF21B46714)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-CC09BF27-4141-49DE-9FCF-4BF1DFF4337D)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_CLUSTER_KUBECONFIG_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-AAAD47C6-BF89-464B-B1CE-23FFCE150A80)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-E2743D7F-C88A-4358-8D54-5D789FF73C8B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-F60BB1DB-E6DC-4CA2-BB9F-A503BDBBE85E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-83D16A50-9DB7-4C4B-B86A-AC7BCE44CDC0)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-46CE2130-A987-43AC-A98D-218110F82A81)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_PREEMPTIBLE_NODE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-CD0B522E-55DF-4275-9FDA-31F224518612)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_PLACEMENT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-BAE511BB-8996-440D-8A8B-4855C69EF317)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-D16FF73D-1673-4F2D-B3DF-19EB91F8D101)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_PLACEMENT_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-157DFDD5-7D27-44B4-BA59-8F3E0356E2F4)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_POOL_NODE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-0C81914E-C8B6-4920-A016-6656502C550C)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_EVICTION_NODE_POOL_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-625D6C6F-E7C0-41AD-A2EF-DF3D5A600EA9)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_CYCLING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C36FBAB3-85FD-4913-BEB1-DDC7E05E44B0)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_KEY_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-97ECB9AD-70E7-4D01-A5F3-93E9F669C0EA)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_NODE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-BBC600B9-3D6E-4FE5-80E4-BB5A72BA3ACF)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_INITIAL_VIRTUAL_NODE_LABEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3D7E6B23-7CFB-4451-AFD7-4440CF8D02A0)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_TAINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9F03A511-E8BB-4096-BA28-6B5EB31BCDBE)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_PLACEMENT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-01BFC9C8-AFB1-4B93-9531-7F96EE3A9B95)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-0A4B80E1-8FE9-4594-94E8-87F9568F3328)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_TAGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C13BF768-5162-4B95-AC10-3AFBA20667B9)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_INITIAL_VIRTUAL_NODE_LABEL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-A12AAABE-B8B1-46CB-AE44-BEB524F8D9DB)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_TAINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-8889276D-6847-4677-80C3-A9D6C6166FAD)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_PLACEMENT_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-21F0ED5E-58F0-472C-A987-A9CEA6DD1C6A)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_VIRTUAL_NODE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-5ADD8702-024D-489B-935C-5D80A2526367)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREATE_WORKLOAD_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DE2072FB-D71E-47D4-BE45-1F130256F709)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_CREDENTIAL_ROTATION_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3A2F99F6-A785-4A5F-AAC9-668110B1066B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-4200A464-9F11-4700-8D69-B14D587C9A1C)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_FLANNEL_OVERLAY_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DE5A4282-AE08-4996-80E4-053164731215)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_FLANNEL_OVERLAY_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-5F89E1E9-8712-4A2D-8111-B00EA6725E69)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_INSTALL_ADDON_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-117F1572-F772-4689-BABF-22217C7B74D9)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C20ADFF3-BEFB-4D43-A1B8-72CB70F73C22)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-6AF50C67-7D59-4276-AB4D-10D458BD7132)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-408673E3-A65F-4227-B577-F8B64BCD17AE)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-0ED98A1C-9AE6-454E-A3F2-7F250813A528)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_NODE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-B6EFFB97-79D1-4FE1-AA39-E15135549063)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-40B8DEC3-428F-4B29-A2C6-A30ACC6B23A7)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-952DC37A-41D0-4AF6-8D73-B417F98E6568)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_OPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-F1ACB5E2-E8AE-4CB2-B604-84C5F11B5F30)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-C00F135A-0EF9-4A48-8328-A6F888B3DB95)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-476F4457-880A-4725-9EF5-17D6ED739FFB)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_VIA_IMAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3A4CD2C4-9512-4916-AC2E-AEA86F62F265)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_NODE_SOURCE_VIA_IMAGE_OPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-76A2B2A6-E955-4F2D-B2FD-851D6D32651C)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_OCI_VCN_IP_NATIVE_CLUSTER_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3FDE8FA4-8578-4DF0-8D1F-4242092DA4AE)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_OCI_VCN_IP_NATIVE_NODE_POOL_POD_NETWORK_OPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9C1B63C6-A336-4F3F-97D5-B6B2E4D16B42)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_OCPU_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-5AC19012-50A3-449D-AF0A-6A6692AAC6AF)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_MEMORY_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-8D9D3B67-319A-4735-A416-A3BC5A85645E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_NETWORK_BANDWIDTH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9746E09F-A285-4C36-B66A-F386EA5D28D4)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_OCPU_OPTIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-43BCCC9A-3899-43A5-B041-D9B513235EC2)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_MEMORY_OPTIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9F4DAA51-8634-49FA-A178-546786F066CD)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_SHAPE_NETWORK_BANDWIDTH_OPTIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-6251FF78-A6E2-4964-A1F4-BE2BDB1FDF41)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-49A3E4E7-4DCA-4E5A-953D-2FBD9F9DDBDC)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_POD_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-63847CEB-AC68-4A70-AD56-2DE5821B6D3B)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_START_CREDENTIAL_ROTATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-42BF8C87-ABC7-47BA-B184-9D50F67D1456)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_TERMINATE_PREEMPTION_ACTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-F26063D6-7737-454E-BAFE-F44FA0007389)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_ADDON_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-56CAF84C-D403-4F02-A88A-71E70122ADF8)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_OPTIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-75BD2294-5493-48E8-9AD9-FFCFBCD00049)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_IMAGE_POLICY_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DDDB1622-F55E-4463-BFD2-A836D47F6DF7)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-B0D7EEBA-53F6-4C7F-A1F7-C7A83E7E9285)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_CLUSTER_ENDPOINT_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-A970C14C-46A5-41D2-B09D-5515BC08F537)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_POOL_NODE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-28673DAD-B25E-4BC5-9856-9A10359AB084)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-71C2BC7B-2696-4140-B7CE-CAF4ECF9B064)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_NODE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-919F5A20-7E24-4921-B3B2-C969CA1FFE98)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_VIRTUAL_NODE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-09BACF53-2223-4FED-A6CA-444208E063A0)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_UPDATE_WORKLOAD_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-9E32D435-C2C7-4B27-B68B-5EB81C3DB662)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-D0B3BDE1-9527-4F2D-BF2E-3E8F1A3814DC)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-16E2BF44-D360-4E06-88AC-3A7BA663871F)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-EEB0D6CE-7CA3-49EB-B1B9-E3050CEAAC6D)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_VIRTUAL_NODE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-7C040CFE-D68C-42CD-A99B-05DDDD81DC9E)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-A44E5AB4-E08E-4883-A795-6514704CB436)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-992C06BE-E38E-47BC-B7BD-713923823EAE)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-AFC20EAB-BFD0-4688-9231-688BDFBB405F)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-3392B287-0E73-4B45-8C3C-DE23DF8CDDB8)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-600F6719-3785-4A73-9EE2-00D0FF61BE26)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-7DC097E2-F4AD-4DC8-A974-C4B50195E668)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORKLOAD_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-34B59A98-7904-4CDB-9A8D-92290F210D7D)
- [DBMS_CLOUD_OCI_CONTAINER_ENGINE_WORKLOAD_MAPPING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_engine_t.html#ADSDK-GUID-DDE1FFD3-62EA-4A4E-AE17-825CD7428144)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
