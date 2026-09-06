# Core Compute Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#dcoc-content-body)

## Core Compute Functions

Package: DBMS_CLOUD_OCI_CR_COMPUTE

### ACCEPT_SHIELDED_INTEGRITY_POLICY Function

Accept the changes to the PCR values in the measured boot report.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function

Adds a shape to the compatible shapes list for the image.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`shape_name`

(required) Shape name.

`add_image_shape_compatibility_entry_details`

(optional) Image shape compatibility details

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_BOOT_VOLUME Function

Attaches the specified boot volume to the specified instance.

Syntax
```

```

Parameters

Parameter Description

`attach_boot_volume_details`

(required) Attach boot volume request

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_VNIC Function

Creates a secondary VNIC and attaches it to the specified instance. For more information about secondary VNICs, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

Syntax
```

```

Parameters

Parameter Description

`attach_vnic_details`

(required) Attach VNIC details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ATTACH_VOLUME Function

Attaches the specified storage volume to the specified instance.

Syntax
```

```

Parameters

Parameter Description

`attach_volume_details`

(required) Attach volume request

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CAPTURE_CONSOLE_HISTORY Function

Captures the most recent serial console data (up to a megabyte) for the specified instance. The `CaptureConsoleHistory` operation works with the other console history operations as described below. 1. Use `CaptureConsoleHistory` to request the capture of up to a megabyte of the most recent console history. This call returns a `ConsoleHistory` object. The object will have a state of REQUESTED. 2. Wait for the capture operation to succeed by polling `GetConsoleHistory` with the identifier of the console history metadata. The state of the `ConsoleHistory` object will go from REQUESTED to GETTING-HISTORY and then SUCCEEDED (or FAILED). 3. Use `GetConsoleHistoryContent` to get the actual console history data (not the metadata). 4. Optionally, use `DeleteConsoleHistory` to delete the console history metadata and the console history data.

Syntax
```

```

Parameters

Parameter Description

`capture_console_history_details`

(required) Console history details

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_COMPUTE_CAPACITY_RESERVATION_COMPARTMENT Function

Moves a compute capacity reservation into a different compartment. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`capacity_reservation_id`

(required) The OCID of the compute capacity reservation.

`change_compute_capacity_reservation_compartment_details`

(required) The configuration details for the move operation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_COMPUTE_CAPACITY_TOPOLOGY_COMPARTMENT Function

Moves a compute capacity topology into a different compartment. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`change_compute_capacity_topology_compartment_details`

(required) The configuration details for the move operation.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_COMPUTE_CLUSTER_COMPARTMENT Function

Moves a compute cluster into a different compartment within the same tenancy. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`compute_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

`change_compute_cluster_compartment_details`

(required) The request to move the compute cluster to a different compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_COMPARTMENT Function

Moves a compute image capability schema into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`compute_image_capability_schema_id`

(required) The id of the compute image capability schema or the image ocid

`change_compute_image_capability_schema_compartment_details`

(required) Compute Image Capability Schema change compartment details

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DEDICATED_VM_HOST_COMPARTMENT Function

Moves a dedicated virtual machine host from one compartment to another.

Syntax
```

```

Parameters

Parameter Description

`dedicated_vm_host_id`

(required) The OCID of the dedicated VM host.

`change_dedicated_vm_host_compartment_details`

(required) The request to move the dedicated virtual machine host to a different compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_IMAGE_COMPARTMENT Function

Moves an image into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`change_image_compartment_details`

(required) Request to change the compartment of a given image.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_INSTANCE_COMPARTMENT Function

Moves an instance into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). When you move an instance to a different compartment, associated resources such as boot volumes and VNICs are not moved.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`change_instance_compartment_details`

(required) Request to change the compartment of a given instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APP_CATALOG_SUBSCRIPTION Function

Create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.

Syntax
```

```

Parameters

Parameter Description

`create_app_catalog_subscription_details`

(required) Request for the creation of a subscription for listing resource version for a compartment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPUTE_CAPACITY_REPORT Function

Generates a report of the host capacity within an availability domain that is available for you to create compute instances. Host capacity is the physical infrastructure that resources such as compute instances run on. Use the capacity report to determine whether sufficient capacity is available for a shape before you create an instance or change the shape of an instance.

Syntax
```

```

Parameters

Parameter Description

`create_compute_capacity_report_details`

(required) Details for creating a new compute capacity report.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPUTE_CAPACITY_RESERVATION Function

Creates a new compute capacity reservation in the specified compartment and availability domain. Compute capacity reservations let you reserve instances in a compartment. When you launch an instance using this reservation, you are assured that you have enough space for your instance, and you won't get out of capacity errors. For more information, see[Reserved Capacity](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).

Syntax
```

```

Parameters

Parameter Description

`create_compute_capacity_reservation_details`

(required) Details for creating a new compute capacity reservation. **Caution:** Avoid using any confidential information when you use the API to supply string values.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPUTE_CAPACITY_TOPOLOGY Function

Creates a new compute capacity topology in the specified compartment and availability domain. Compute capacity topologies provide the RDMA network topology of your bare metal hosts so that you can launch instances on your bare metal hosts with targeted network locations. Compute capacity topologies report the health status of your bare metal hosts.

Syntax
```

```

Parameters

Parameter Description

`create_compute_capacity_topology_details`

(required) Details for creating a new compute capacity topology.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPUTE_CLUSTER Function

Creates an empty[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm). A compute cluster is a remote direct memory access (RDMA) network group. After the compute cluster is created, you can use the compute cluster's OCID with the`LAUNCH_INSTANCE`Function operation to create instances in the compute cluster. The instances must be created in the same compartment and availability domain as the cluster. Use compute clusters when you want to manage instances in the cluster individually, or when you want to use different types of instances in the RDMA network group. If you want predictable capacity for a specific number of identical instances that are managed as a group, create a cluster network that uses instance pools by using the`CREATE_CLUSTER_NETWORK`Function operation.

Syntax
```

```

Parameters

Parameter Description

`create_compute_cluster_details`

(required) The data for creating a[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm). A compute cluster is an empty remote direct memory access (RDMA) network group. After the compute cluster is created, you can use the compute cluster's OCID with the`LAUNCH_INSTANCE`Function operation to create instances in the compute cluster. The instances must be created in the same compartment and availability domain as the cluster. Use compute clusters when you want to manage instances in the cluster individually, or when you want to use different types of instances in the RDMA network group. For details about creating a cluster network that uses instance pools to manage groups of identical instances, see`CREATE_CLUSTER_NETWORK_DETAILS`Function.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function

Creates compute image capability schema.

Syntax
```

```

Parameters

Parameter Description

`create_compute_image_capability_schema_details`

(required) Compute Image Capability Schema creation details

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEDICATED_VM_HOST Function

Creates a new dedicated virtual machine host in the specified compartment and the specified availability domain. Dedicated virtual machine hosts enable you to run your Compute virtual machine (VM) instances on dedicated servers that are a single tenant and not shared with other customers. For more information, see[Dedicated Virtual Machine Hosts](https://docs.oracle.com/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm).

Syntax
```

```

Parameters

Parameter Description

`create_dedicated_vm_host_details`

(required) The details for creating a new dedicated virtual machine host.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IMAGE Function

Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service. When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and the OCID of the compartment containing that instance. For more information about images, see[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm). When importing an exported image from Object Storage, you specify the source information in`IMAGE_SOURCE_DETAILS`Function. When importing an image based on the namespace, bucket name, and object name, use`IMAGE_SOURCE_VIA_OBJECT_STORAGE_TUPLE_DETAILS`Function. When importing an image based on the Object Storage URL, use`IMAGE_SOURCE_VIA_OBJECT_STORAGE_URI_DETAILS`Function. See[Object Storage URLs](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs)and[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for constructing URLs for image import/export. For more information about importing exported images, see[Image Import/Export](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm). You may optionally specify a *display name* for the image, which is simply a friendly name or description. It does not have to be unique, and you can change it. See`UPDATE_IMAGE`Function. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_image_details`

(required) Image creation details

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_INSTANCE_CONSOLE_CONNECTION Function

Creates a new console connection to the specified instance. After the console connection has been created and is available, you connect to the console using SSH. For more information about instance console connections, see[Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

Syntax
```

```

Parameters

Parameter Description

`create_instance_console_connection_details`

(required) Request object for creating an InstanceConsoleConnection

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APP_CATALOG_SUBSCRIPTION Function

Delete a subscription for a listing resource version for a compartment.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The OCID of the listing.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`resource_version`

(required) Listing Resource Version.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COMPUTE_CAPACITY_RESERVATION Function

Deletes the specified compute capacity reservation.

Syntax
```

```

Parameters

Parameter Description

`capacity_reservation_id`

(required) The OCID of the compute capacity reservation.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COMPUTE_CAPACITY_TOPOLOGY Function

Deletes the specified compute capacity topology.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COMPUTE_CLUSTER Function

Deletes a compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group. Before you delete a compute cluster, first delete all instances in the cluster by using the`TERMINATE_INSTANCE`Function operation.

Syntax
```

```

Parameters

Parameter Description

`compute_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function

Deletes the specified Compute Image Capability Schema

Syntax
```

```

Parameters

Parameter Description

`compute_image_capability_schema_id`

(required) The id of the compute image capability schema or the image ocid

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONSOLE_HISTORY Function

Deletes the specified console history metadata and the console history data.

Syntax
```

```

Parameters

Parameter Description

`instance_console_history_id`

(required) The OCID of the console history.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEDICATED_VM_HOST Function

Deletes the specified dedicated virtual machine host. If any VM instances are assigned to the dedicated virtual machine host, the delete operation will fail and the service will return a 409 response code.

Syntax
```

```

Parameters

Parameter Description

`dedicated_vm_host_id`

(required) The OCID of the dedicated VM host.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IMAGE Function

Deletes an image.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_INSTANCE_CONSOLE_CONNECTION Function

Deletes the specified instance console connection.

Syntax
```

```

Parameters

Parameter Description

`instance_console_connection_id`

(required) The OCID of the instance console connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_BOOT_VOLUME Function

Detaches a boot volume from an instance. You must specify the OCID of the boot volume attachment. This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_attachment_id`

(required) The OCID of the boot volume attachment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_VNIC Function

Detaches and deletes the specified secondary VNIC. This operation cannot be used on the instance's primary VNIC. When you terminate an instance, all attached VNICs (primary and secondary) are automatically detached and deleted. **Important:** If the VNIC has a`PRIVATE_IP`Type that is the[target of a route rule](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip), deleting the VNIC causes that route rule to blackhole and the traffic will be dropped.

Syntax
```

```

Parameters

Parameter Description

`vnic_attachment_id`

(required) The OCID of the VNIC attachment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DETACH_VOLUME Function

Detaches a storage volume from an instance. You must specify the OCID of the volume attachment. This is an asynchronous operation. The attachment's `lifecycleState` will change to DETACHING temporarily until the attachment is completely removed.

Syntax
```

```

Parameters

Parameter Description

`volume_attachment_id`

(required) The OCID of the volume attachment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_IMAGE Function

Exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to. For more information about exporting images, see[Image Import/Export](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm). To perform an image export, you need write access to the Object Storage bucket for the image, see[Let Users Write Objects to Object Storage Buckets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#Let4). See[Object Storage URLs](https://docs.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs)and[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for constructing URLs for image import/export.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`export_image_details`

(required) Details for the image export.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APP_CATALOG_LISTING Function

Gets the specified listing.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The OCID of the listing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APP_CATALOG_LISTING_AGREEMENTS Function

Retrieves the agreements for a particular resource version of a listing.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The OCID of the listing.

`resource_version`

(required) Listing Resource Version.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APP_CATALOG_LISTING_RESOURCE_VERSION Function

Gets the specified listing resource version.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The OCID of the listing.

`resource_version`

(required) Listing Resource Version.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BOOT_VOLUME_ATTACHMENT Function

Gets information about the specified boot volume attachment.

Syntax
```

```

Parameters

Parameter Description

`boot_volume_attachment_id`

(required) The OCID of the boot volume attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_CAPACITY_RESERVATION Function

Gets information about the specified compute capacity reservation.

Syntax
```

```

Parameters

Parameter Description

`capacity_reservation_id`

(required) The OCID of the compute capacity reservation.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_CAPACITY_TOPOLOGY Function

Gets information about the specified compute capacity topology.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_CLUSTER Function

Gets information about a compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

Syntax
```

```

Parameters

Parameter Description

`compute_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA Function

Gets the specified Compute Global Image Capability Schema

Syntax
```

```

Parameters

Parameter Description

`compute_global_image_capability_schema_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute global image capability schema

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION Function

Gets the specified Compute Global Image Capability Schema Version

Syntax
```

```

Parameters

Parameter Description

`compute_global_image_capability_schema_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute global image capability schema

`compute_global_image_capability_schema_version_name`

(required) The name of the compute global image capability schema version

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function

Gets the specified Compute Image Capability Schema

Syntax
```

```

Parameters

Parameter Description

`compute_image_capability_schema_id`

(required) The id of the compute image capability schema or the image ocid

`is_merge_enabled`

(optional) Merge the image capability schema with the global image capability schema

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONSOLE_HISTORY Function

Shows the metadata for the specified console history. See`CAPTURE_CONSOLE_HISTORY`Function for details about using the console history operations.

Syntax
```

```

Parameters

Parameter Description

`instance_console_history_id`

(required) The OCID of the console history.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONSOLE_HISTORY_CONTENT Function

Gets the actual console history data (not the metadata). See`CAPTURE_CONSOLE_HISTORY`Function for details about using the console history operations.

Syntax
```

```

Parameters

Parameter Description

`instance_console_history_id`

(required) The OCID of the console history.

`offset`

(optional) Offset of the snapshot data to retrieve.

`length`

(optional) Length of the snapshot data to retrieve.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEDICATED_VM_HOST Function

Gets information about the specified dedicated virtual machine host.

Syntax
```

```

Parameters

Parameter Description

`dedicated_vm_host_id`

(required) The OCID of the dedicated VM host.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IMAGE Function

Gets the specified image.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function

Retrieves an image shape compatibility entry.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`shape_name`

(required) Shape name.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INSTANCE Function

Gets information about the specified instance. **Note:** To retrieve public and private IP addresses for an instance, use the`LIST_VNIC_ATTACHMENTS`Function operation to get the VNIC ID for the instance, and then call`GET_VNIC`Function with the VNIC ID.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INSTANCE_CONSOLE_CONNECTION Function

Gets the specified instance console connection's information.

Syntax
```

```

Parameters

Parameter Description

`instance_console_connection_id`

(required) The OCID of the instance console connection.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INSTANCE_MAINTENANCE_REBOOT Function

Gets the maximum possible date that a maintenance reboot can be extended. For more information, see[Infrastructure Maintenance](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm).

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MEASURED_BOOT_REPORT Function

Gets the measured boot report for this shielded instance.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VNIC_ATTACHMENT Function

Gets the information for the specified VNIC attachment.

Syntax
```

```

Parameters

Parameter Description

`vnic_attachment_id`

(required) The OCID of the VNIC attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VOLUME_ATTACHMENT Function

Gets information about the specified volume attachment.

Syntax
```

```

Parameters

Parameter Description

`volume_attachment_id`

(required) The OCID of the volume attachment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WINDOWS_INSTANCE_INITIAL_CREDENTIALS Function

Gets the generated credentials for the instance. Only works for instances that require a password to log in, such as Windows. For certain operating systems, users will be forced to change the initial credentials.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INSTANCE_ACTION Function

Performs one of the following power actions on the specified instance: - **START** - Powers on the instance. - **STOP** - Powers off the instance. - **RESET** - Powers off the instance and then powers it back on. - **SOFTSTOP** - Gracefully shuts down the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off. If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, manually shut down the instance using the commands available in the OS before you softstop the instance. - **SOFTRESET** - Gracefully reboots the instance by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instance is powered off and then powered back on. - **SENDDIAGNOSTICINTERRUPT** - For advanced users. **Caution: Sending a diagnostic interrupt to a live system can cause data corruption or system failure.** Sends a diagnostic interrupt that causes the instance's OS to crash and then reboot. Before you send a diagnostic interrupt, you must configure the instance to generate a crash dump file when it crashes. The crash dump captures information about the state of the OS at the time of the crash. After the OS restarts, you can analyze the crash dump to diagnose the issue. For more information, see[Sending a Diagnostic Interrupt](https://docs.oracle.com/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm). - **DIAGNOSTICREBOOT** - Powers off the instance, rebuilds it, and then powers it back on. Before you send a diagnostic reboot, restart the instance's OS, confirm that the instance and networking settings are configured correctly, and try other[troubleshooting steps](https://docs.oracle.com/iaas/Content/Compute/References/troubleshooting-compute-instances.htm). Use diagnostic reboot as a final attempt to troubleshoot an unreachable instance. For virtual machine (VM) instances only. For more information, see[Performing a Diagnostic Reboot](https://docs.oracle.com/iaas/Content/Compute/Tasks/diagnostic-reboot.htm). - **REBOOTMIGRATE** - Powers off the instance, moves it to new hardware, and then powers it back on. For more information, see[Infrastructure Maintenance](https://docs.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm). For more information about managing instance lifecycle states, see[Stopping and Starting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`action`

(required) The action to perform on the instance.

Allowed values are: 'STOP', 'START', 'SOFTRESET', 'RESET', 'SOFTSTOP', 'SENDDIAGNOSTICINTERRUPT', 'DIAGNOSTICREBOOT', 'REBOOTMIGRATE'

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`instance_power_action_details`

(optional) Instance Power Action details

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LAUNCH_INSTANCE Function

Creates a new instance in the specified compartment and the specified availability domain. For general information about instances, see[Overview of the Compute Service](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm). For information about access control and compartments, see[Overview of the IAM Service](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API. All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. To launch an instance using an image or a boot volume use the `sourceDetails` parameter in`LAUNCH_INSTANCE_DETAILS`Type. When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the`LIST_VNIC_ATTACHMENTS`Function operation to get the VNIC ID for the instance, and then call`GET_VNIC`Function with the VNIC ID. You can later add secondary VNICs to an instance. For more information, see[Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm). To launch an instance from a Marketplace image listing, you must provide the image ID of the listing resource version that you want, but you also must subscribe to the listing before you try to launch the instance. To subscribe to the listing, use the`GET_APP_CATALOG_LISTING_AGREEMENTS`Function operation to get the signature for the terms of use agreement for the desired listing resource version. Then, call`CREATE_APP_CATALOG_SUBSCRIPTION`Function with the signature. To get the image ID for the LaunchInstance operation, call`GET_APP_CATALOG_LISTING_RESOURCE_VERSION`Function. To determine whether capacity is available for a specific shape before you create an instance, use the`CREATE_COMPUTE_CAPACITY_REPORT`Function operation.

Syntax
```

```

Parameters

Parameter Description

`launch_instance_details`

(required) Instance details

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APP_CATALOG_LISTING_RESOURCE_VERSIONS Function

Gets all resource versions for a particular listing.

Syntax
```

```

Parameters

Parameter Description

`listing_id`

(required) The OCID of the listing.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APP_CATALOG_LISTINGS Function

Lists the published listings.

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`publisher_name`

(optional) A filter to return only the publisher that matches the given publisher name exactly.

`publisher_type`

(optional) A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APP_CATALOG_SUBSCRIPTIONS Function

Lists subscriptions for a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`listing_id`

(optional) A filter to return only the listings that matches the given listing id.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BOOT_VOLUME_ATTACHMENTS Function

Lists the boot volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, boot volume OCID, or both.

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(required) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`instance_id`

(optional) The OCID of the instance.

`boot_volume_id`

(optional) The OCID of the boot volume.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPES Function

Lists the shapes that can be reserved within the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCES Function

Lists the instances launched under a capacity reservation. You can filter results by specifying criteria.

Syntax
```

```

Parameters

Parameter Description

`capacity_reservation_id`

(required) The OCID of the compute capacity reservation.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_RESERVATIONS Function

Lists the compute capacity reservations that match the specified criteria and compartment. You can limit the list by specifying a compute capacity reservation display name (the list will include all the identically-named compute capacity reservations in the compartment).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_TOPOLOGIES Function

Lists the compute capacity topologies in the specified compartment. You can filter the list by a compute capacity topology display name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_BARE_METAL_HOSTS Function

Lists compute bare metal hosts in the specified compute capacity topology.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`compute_hpc_island_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`compute_network_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute network block.

`compute_local_block_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute local block.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_HPC_ISLANDS Function

Lists compute HPC islands in the specified compute capacity topology.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_NETWORK_BLOCKS Function

Lists compute network blocks in the specified compute capacity topology.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`compute_hpc_island_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute HPC island.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_CLUSTERS Function

Lists the compute clusters in the specified compartment. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSIONS Function

Lists Compute Global Image Capability Schema versions in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compute_global_image_capability_schema_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute global image capability schema

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMAS Function

Lists Compute Global Image Capability Schema in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) A filter to return only resources that match the given compartment OCID exactly.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTE_IMAGE_CAPABILITY_SCHEMAS Function

Lists Compute Image Capability Schema in the specified compartment. You can also query by a specific imageId.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) A filter to return only resources that match the given compartment OCID exactly.

`image_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an image.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONSOLE_HISTORIES Function

Lists the console history metadata for the specified compartment or instance.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`instance_id`

(optional) The OCID of the instance.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEDICATED_VM_HOST_INSTANCE_SHAPES Function

Lists the shapes that can be used to launch a virtual machine instance on a dedicated virtual machine host within the specified compartment. You can filter the list by compatibility with a specific dedicated virtual machine host shape.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`dedicated_vm_host_shape`

(optional) Dedicated VM host shape name

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEDICATED_VM_HOST_INSTANCES Function

Returns the list of instances on the dedicated virtual machine hosts that match the specified criteria.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`dedicated_vm_host_id`

(required) The OCID of the dedicated VM host.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEDICATED_VM_HOST_SHAPES Function

Lists the shapes that can be used to launch a dedicated virtual machine host within the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`instance_shape_name`

(optional) The name for the instance's shape.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEDICATED_VM_HOSTS Function

Returns the list of dedicated virtual machine hosts that match the specified criteria in the specified compartment. You can limit the list by specifying a dedicated virtual machine host display name. The list will include all the identically-named dedicated virtual machine hosts in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`instance_shape_name`

(optional) The name for the instance's shape.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`remaining_memory_in_g_bs_greater_than_or_equal_to`

(optional) The remaining memory of the dedicated VM host, in GBs.

`remaining_ocpus_greater_than_or_equal_to`

(optional) The available OCPUs of the dedicated VM host.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMAGE_SHAPE_COMPATIBILITY_ENTRIES Function

Lists the compatible shapes for the specified image.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMAGES Function

Lists a subset of images available in the specified compartment, including[platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)and[custom images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm). The list of platform images includes the three most recently published versions of each major distribution. The list does not support filtering based on image tags. The list of images returned is ordered to first show the recent platform images, then all of the custom images. **Caution:** Platform images are refreshed regularly. When new images are released, older versions are replaced. The image OCIDs remain available, but when the platform image is replaced, the image OCIDs are no longer returned as part of the platform image list.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`operating_system`

(optional) The image's operating system. Example: `Oracle Linux`

`operating_system_version`

(optional) The image's operating system version. Example: `7.2`

`shape`

(optional) Shape name.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INSTANCE_CONSOLE_CONNECTIONS Function

Lists the console connections for the specified compartment or instance. For more information about instance console connections, see[Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`instance_id`

(optional) The OCID of the instance.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INSTANCE_DEVICES Function

Gets a list of all the devices for given instance. You can optionally filter results by device availability.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`is_available`

(optional) A filter to return only available devices or only used devices.

`name`

(optional) A filter to return only devices that match the given name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INSTANCES Function

Lists the instances in the specified compartment and the specified availability domain. You can filter the results by specifying an instance name (the list will include all the identically-named instances in the compartment). **Note:** To retrieve public and private IP addresses for an instance, use the`LIST_VNIC_ATTACHMENTS`Function operation to get the VNIC ID for the instance, and then call`GET_VNIC`Function with the VNIC ID.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`capacity_reservation_id`

(optional) The OCID of the compute capacity reservation.

`compute_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SHAPES Function

Lists the shapes that can be used to launch an instance within the specified compartment. You can filter the list by compatibility with a specific image.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`image_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of an image.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VNIC_ATTACHMENTS Function

Lists the VNIC attachments in the specified compartment. A VNIC attachment resides in the same compartment as the attached instance. The list can be filtered by instance, VNIC, or availability domain.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`instance_id`

(optional) The OCID of the instance.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`vnic_id`

(optional) The OCID of the VNIC.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VOLUME_ATTACHMENTS Function

Lists the volume attachments in the specified compartment. You can filter the list by specifying an instance OCID, volume OCID, or both. Currently, the only supported volume attachment type are`I_SCSI_VOLUME_ATTACHMENT`Type and`PARAVIRTUALIZED_VOLUME_ATTACHMENT`Type.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`availability_domain`

(optional) The name of the availability domain. Example: `Uocm:PHX-AD-1`

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`instance_id`

(optional) The OCID of the instance.

`volume_id`

(optional) The OCID of the volume.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function

Removes a shape from the compatible shapes list for the image.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`shape_name`

(required) Shape name.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TERMINATE_INSTANCE Function

Permanently terminates (deletes) the specified instance. Any attached VNICs and volumes are automatically detached when the instance terminates. To preserve the boot volume associated with the instance, specify `true` for `PreserveBootVolumeQueryParam`. To delete the boot volume when the instance is deleted, specify `false` or do not specify a value for `PreserveBootVolumeQueryParam`. This is an asynchronous operation. The instance's `lifecycleState` changes to TERMINATING temporarily until the instance is completely deleted. After the instance is deleted, the record remains visible in the list of instances with the state TERMINATED for at least 12 hours, but no further action is needed.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`preserve_boot_volume`

(optional) Specifies whether to delete or preserve the boot volume when terminating an instance. When set to `true`, the boot volume is preserved. The default value is `false`.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COMPUTE_CAPACITY_RESERVATION Function

Updates the specified capacity reservation and its associated capacity configurations. Fields that are not provided in the request will not be updated. Capacity configurations that are not included will be deleted. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`capacity_reservation_id`

(required) The OCID of the compute capacity reservation.

`update_compute_capacity_reservation_details`

(required) Update compute capacity reservation details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COMPUTE_CAPACITY_TOPOLOGY Function

Updates the specified compute capacity topology. Fields that are not provided in the request will not be updated.

Syntax
```

```

Parameters

Parameter Description

`compute_capacity_topology_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute capacity topology.

`update_compute_capacity_topology_details`

(required) Update compute capacity topology details.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COMPUTE_CLUSTER Function

Updates a compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group. To create instances within a compute cluster, use the`LAUNCH_INSTANCE`Function operation. To delete instances from a compute cluster, use the`TERMINATE_INSTANCE`Function operation.

Syntax
```

```

Parameters

Parameter Description

`compute_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compute cluster. A[compute cluster](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)is a remote direct memory access (RDMA) network group.

`update_compute_cluster_details`

(required) Details for updating the compute cluster.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function

Updates the specified Compute Image Capability Schema

Syntax
```

```

Parameters

Parameter Description

`compute_image_capability_schema_id`

(required) The id of the compute image capability schema or the image ocid

`update_compute_image_capability_schema_details`

(required) Updates the freeFormTags, definedTags, and display name of the image capability schema

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONSOLE_HISTORY Function

Updates the specified console history metadata.

Syntax
```

```

Parameters

Parameter Description

`instance_console_history_id`

(required) The OCID of the console history.

`update_console_history_details`

(required) Update instance fields

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEDICATED_VM_HOST Function

Updates the displayName, freeformTags, and definedTags attributes for the specified dedicated virtual machine host. If an attribute value is not included, it will not be updated.

Syntax
```

```

Parameters

Parameter Description

`dedicated_vm_host_id`

(required) The OCID of the dedicated VM host.

`update_dedicated_vm_host_details`

(required) Update dedicated VM host details

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IMAGE Function

Updates the display name of the image. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`image_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the image.

`update_image_details`

(required) Updates the image display name field. Avoid entering confidential information.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INSTANCE Function

Updates certain fields on the specified instance. Fields that are not provided in the request will not be updated. Avoid entering confidential information. Changes to metadata fields will be reflected in the instance metadata service (this may take up to a minute). The OCID of the instance remains the same.

Syntax
```

```

Parameters

Parameter Description

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`update_instance_details`

(required) Update instance fields

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INSTANCE_CONSOLE_CONNECTION Function

Updates the defined tags and free-form tags for the specified instance console connection.

Syntax
```

```

Parameters

Parameter Description

`instance_console_connection_id`

(required) The OCID of the instance console connection.

`update_instance_console_connection_details`

(required) Update instanceConsoleConnection tags

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VOLUME_ATTACHMENT Function

Updates information about the specified volume attachment.

Syntax
```

```

Parameters

Parameter Description

`volume_attachment_id`

(required) The OCID of the volume attachment.

`update_volume_attachment_details`

(required) Update information about the specified volume attachment.

`opc_request_id`

(optional) Unique identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Core Compute Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-47FF02E2-308A-40EF-B6B2-4FAD577FF9D3)
- [ACCEPT_SHIELDED_INTEGRITY_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-37764F2D-F38A-4ED2-B5B4-394CDB2D72CC)
- [ADD_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-4B2193A3-4367-4A88-9EB7-1AA68C2E137A)
- [ATTACH_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-DB3A82CE-3FEB-4473-A37B-1B54A5889751)
- [ATTACH_VNIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-D63580D2-A1BB-4A2C-8467-AF42CE510720)
- [ATTACH_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-FAF7F92D-5158-4B4F-B205-D3DE73691E63)
- [CAPTURE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-9DE09DA3-2635-4A2D-90F9-B3A5A47214E9)
- [CHANGE_COMPUTE_CAPACITY_RESERVATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-F6068301-7786-4D36-9F98-98DD07ED3D4B)
- [CHANGE_COMPUTE_CAPACITY_TOPOLOGY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-FC769BED-62F9-4CA0-85AB-540A05F7CE21)
- [CHANGE_COMPUTE_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-C5670E32-40B2-4CCF-8331-C887ABBE64AF)
- [CHANGE_COMPUTE_IMAGE_CAPABILITY_SCHEMA_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-DC2C1558-2420-453B-8FE3-7D4CF08053EC)
- [CHANGE_DEDICATED_VM_HOST_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-19ED1FE4-F1B4-4AEC-B62C-F23B58E1E2FE)
- [CHANGE_IMAGE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-EE433472-D6DF-44FC-B870-5A7337F79648)
- [CHANGE_INSTANCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-92A69B5B-4F9B-4B8A-AEE1-87589A555022)
- [CREATE_APP_CATALOG_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-7BE00F20-8D21-4E5E-A9AA-63165E443396)
- [CREATE_COMPUTE_CAPACITY_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-07615A53-E7CB-4795-995F-7EF401CD16DC)
- [CREATE_COMPUTE_CAPACITY_RESERVATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-FD7CEE70-CC8B-4EC3-87C2-E77FA2ABA996)
- [CREATE_COMPUTE_CAPACITY_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-4943DA46-7CF6-42ED-8F2B-023169EA897F)
- [CREATE_COMPUTE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-0D137A13-36A1-4756-999D-BF4A0A59D82E)
- [CREATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-2130C013-9B2A-49A5-85EF-06A34654560A)
- [CREATE_DEDICATED_VM_HOST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-0D6E106F-48B8-46CB-B409-88F9DFBB058F)
- [CREATE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-55D171C5-EC99-41A2-8B9D-C9664D7A034C)
- [CREATE_INSTANCE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-68EAB783-42CC-468F-9396-105F2C7566A7)
- [DELETE_APP_CATALOG_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-F0CC5FCF-241D-45E5-BCFE-F91E1B242D7B)
- [DELETE_COMPUTE_CAPACITY_RESERVATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-369FABFD-A742-4C01-9C54-045C7EE2DD80)
- [DELETE_COMPUTE_CAPACITY_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-41014907-8366-49EE-92A4-359B25725A95)
- [DELETE_COMPUTE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-B2F1DC05-6E55-4860-B517-7AC14116647C)
- [DELETE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-68A7ABC6-6E76-490E-866B-F5947AF8E9D6)
- [DELETE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-8BFE3F6D-9598-4CCC-85E2-71D0076BF1DD)
- [DELETE_DEDICATED_VM_HOST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-D4F6A5E7-4E23-46F4-9C68-43077B83E7C4)
- [DELETE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-90EE3D2C-0813-4A5C-A84A-9211A0B6BE4E)
- [DELETE_INSTANCE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-FC0E89C9-6F3B-4C0B-9EF4-BB9752A74BC2)
- [DETACH_BOOT_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-6A9E3EED-9A21-487D-9634-D92F3B2CEE84)
- [DETACH_VNIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-BB2BE93F-18DF-42D2-BCD9-AB1EC8F94D91)
- [DETACH_VOLUME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-667D0DDC-B1B1-4FF3-A299-72412A3FAD3D)
- [EXPORT_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-DB5E1F64-AAE1-4E85-AF0F-B7E8878E5F84)
- [GET_APP_CATALOG_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-896166FD-2991-4C93-BC62-AB9676744A08)
- [GET_APP_CATALOG_LISTING_AGREEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-B96CFB08-E14B-43C3-BE1F-82B563470A17)
- [GET_APP_CATALOG_LISTING_RESOURCE_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-5B1A8CDF-877F-447D-B925-D1EBEB44BBD4)
- [GET_BOOT_VOLUME_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-91EACDF4-C5C6-44EE-B4FA-34758AF04376)
- [GET_COMPUTE_CAPACITY_RESERVATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-EF3DD442-E5F0-42BB-84CA-C5C53486BCA5)
- [GET_COMPUTE_CAPACITY_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-C4F5D8A9-5232-48C6-8138-4AEAB3B08583)
- [GET_COMPUTE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-000618B8-E148-40F0-8A58-1DE12F9470FF)
- [GET_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-22CBE695-0F70-4B0F-8566-F441FBB5BF35)
- [GET_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-3F3918A8-F46C-489A-A42A-04F06ABE17D8)
- [GET_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-1339F618-A482-4971-BFE2-6D284F3B0F5E)
- [GET_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-5360241C-4B69-4186-A3A7-4999563E1ADD)
- [GET_CONSOLE_HISTORY_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-15026AB6-F307-4EE9-98EB-00BBE2474FAA)
- [GET_DEDICATED_VM_HOST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-44456A06-7ECE-4A74-9CF3-5E705CB3D3DF)
- [GET_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-3F58BE64-0A9C-4E61-B35B-62868EC4208E)
- [GET_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-8F928CE6-93CA-4063-A088-D9A12A633D05)
- [GET_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-8CC65D09-1787-44CF-9EC2-474741BFA49F)
- [GET_INSTANCE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-56120811-FD93-4147-A663-3326DB096614)
- [GET_INSTANCE_MAINTENANCE_REBOOT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-362C61FE-5D05-4BD3-913D-E237AAE6767C)
- [GET_MEASURED_BOOT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-49D0BFFC-8EED-42F2-9F28-052CC6D71AF0)
- [GET_VNIC_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-477C6979-5876-4904-95A4-BD6FC29B27DD)
- [GET_VOLUME_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-1A05E356-147C-469C-A576-05E895B127D6)
- [GET_WINDOWS_INSTANCE_INITIAL_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-6CC2408C-A7F5-4D02-B2C1-0D7A83C0A948)
- [INSTANCE_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-7136A36E-224F-4B2E-925C-828190066493)
- [LAUNCH_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-F13294B0-36E0-471E-874B-F26E7A689751)
- [LIST_APP_CATALOG_LISTING_RESOURCE_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-805D9E4D-30AC-4CBC-AB8A-DA3AE6FDA158)
- [LIST_APP_CATALOG_LISTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-D0408FF4-1AA9-4CD1-94AF-8E0B3E8AF71B)
- [LIST_APP_CATALOG_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-05B5E604-2A11-432E-B075-EA770C8A3668)
- [LIST_BOOT_VOLUME_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-92A86BB9-7EF7-4420-870E-14C49AC959EE)
- [LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCE_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-36347C4B-4D6E-44A4-8037-6C2A0F70072B)
- [LIST_COMPUTE_CAPACITY_RESERVATION_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-FD45E38D-1503-4237-8C66-2BD826126131)
- [LIST_COMPUTE_CAPACITY_RESERVATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-DA163D4E-DFD5-4F03-BD3C-4BC734F1BA44)
- [LIST_COMPUTE_CAPACITY_TOPOLOGIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-41FF5574-3A72-44BE-B65C-798C32ABB471)
- [LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_BARE_METAL_HOSTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-BA3D74F5-AD9D-4142-9B5C-92559BBB5FEE)
- [LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_HPC_ISLANDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-ABF329DE-9EBE-471E-8C4E-1BEEF8B63445)
- [LIST_COMPUTE_CAPACITY_TOPOLOGY_COMPUTE_NETWORK_BLOCKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-E03CFAE8-E1DE-4082-A5AA-88165CDEAF6F)
- [LIST_COMPUTE_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-6882DA91-D983-4F25-A7BE-71C882E7DDBD)
- [LIST_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-09C77DFF-617F-4907-8CDF-2E8F397D525C)
- [LIST_COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-9FEC0BE8-1FD4-4BAE-9226-41E3C6C50695)
- [LIST_COMPUTE_IMAGE_CAPABILITY_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-389550AB-4A9A-4942-BC30-5ACF35F52045)
- [LIST_CONSOLE_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-701B4259-AA53-49D6-81CC-DA7FE0E8B0F1)
- [LIST_DEDICATED_VM_HOST_INSTANCE_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-1C6028C8-F131-40E6-BA69-BF897987B09A)
- [LIST_DEDICATED_VM_HOST_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-8695B5D8-4D3F-4E75-93FD-7C345ADA60DA)
- [LIST_DEDICATED_VM_HOST_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-20BAC26C-6583-4EB3-8AE3-C653F0A46649)
- [LIST_DEDICATED_VM_HOSTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-30A43714-C34C-45E4-A3C3-AC54C91C73FC)
- [LIST_IMAGE_SHAPE_COMPATIBILITY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-93299B08-5970-4905-9760-66864CC2E600)
- [LIST_IMAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-55B9A4A7-17A6-49A9-BA4E-ACF79F636E2B)
- [LIST_INSTANCE_CONSOLE_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-465CC167-B8AF-46DF-A8C5-405A1361F823)
- [LIST_INSTANCE_DEVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-5F9B4BF0-12CC-4133-8DB7-62692AEA4B3C)
- [LIST_INSTANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-AD2415C1-97D5-4D96-AAC1-7BBEAB22A34F)
- [LIST_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-B9FB835C-56F0-45F0-AAA0-F61EF5D823DF)
- [LIST_VNIC_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-42F5014D-FCEC-4D98-A618-D5FB23A8B7CF)
- [LIST_VOLUME_ATTACHMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-06156626-B06A-446F-BA9F-5D263A4A2CC7)
- [REMOVE_IMAGE_SHAPE_COMPATIBILITY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-3778FF7F-01E7-4145-A4F4-4108000CCD4F)
- [TERMINATE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-B26412BE-FD9B-4F36-95BE-AEDE1409C88B)
- [UPDATE_COMPUTE_CAPACITY_RESERVATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-E241E3E6-DBA4-4AA4-A911-4848878409C5)
- [UPDATE_COMPUTE_CAPACITY_TOPOLOGY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-95FE4206-9071-4ABA-BA06-6242994FFDED)
- [UPDATE_COMPUTE_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-47DDECF9-743B-4664-A90E-4267B6255A31)
- [UPDATE_COMPUTE_IMAGE_CAPABILITY_SCHEMA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-66DC00FC-F38A-4FF4-94C5-ED09DC026FAD)
- [UPDATE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-4C7845A1-B384-4E52-A2BD-145A8B8C16DC)
- [UPDATE_DEDICATED_VM_HOST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-46190424-18C4-4CD7-9394-0660F89FAB17)
- [UPDATE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-2207D066-469E-47ED-9DB7-58C195C9E573)
- [UPDATE_INSTANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-6E4D035F-A206-4F2B-AD3F-0E137CBB1237)
- [UPDATE_INSTANCE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-6FF324D7-93C6-47BF-99D5-6F70C01FB4DA)
- [UPDATE_VOLUME_ATTACHMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cr_compute.html#ADSDK-GUID-8C916066-0A0B-4F5E-B1E6-AE25D9836822)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
