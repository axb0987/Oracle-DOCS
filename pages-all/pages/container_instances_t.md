# Container Instances Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#dcoc-content-body)

## Container Instances Common Types

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_IMAGE_PULL_SECRET_T Type

The image pull secrets for accessing private registry to pull images for containers

Syntax
```

```

Fields

Field Description

`secret_type`

(required) The type of ImagePullSecret.

Allowed values are: 'BASIC', 'VAULT'

`registry_endpoint`

(required) The registry endpoint of the container image.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_BASIC_IMAGE_PULL_SECRET_T Type

A BasicImagePullSecret is a ImagePullSecret which accepts username and password as credentials information.

Syntax
```

```

`dbms_cloud_oci_container_instances_basic_image_pull_secret_t`is a subtype of the`dbms_cloud_oci_container_instances_image_pull_secret_t`type.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CHANGE_CONTAINER_INSTANCE_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the container instance to.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VOLUME_MOUNT_T Type

Define the mapping from volume to a mount path in container.

Syntax
```

```

Fields

Field Description

`mount_path`

(required) Describes the volume access path.

`volume_name`

(required) The name of the volume.

`sub_path`

(optional) A sub-path inside the referenced volume.

`is_read_only`

(optional) Whether the volume was mounted in read-only mode. By default, the volume is mounted with write access.

`partition`

(optional) If there is more than one partition in the volume, reference this number of partitions. Here is an example: Number Start End Size File system Name Flags 1 1049kB 106MB 105MB fat16 EFI System Partition boot, esp 2 106MB 1180MB 1074MB xfs 3 1180MB 50.0GB 48.8GB lvm

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HEALTH_CHECK_T Type

Type of container health check which could be either HTTP, TCP, or Command.

Syntax
```

```

Fields

Field Description

`name`

(optional) Health check name.

`health_check_type`

(required) Container health check type.

Allowed values are: 'HTTP', 'TCP', 'COMMAND'

`initial_delay_in_seconds`

(optional) The initial delay in seconds before start checking container health status.

`interval_in_seconds`

(optional) Number of seconds between two consecutive runs for checking container health.

`failure_threshold`

(optional) Number of consecutive failures at which we consider the check failed.

`success_threshold`

(optional) Number of consecutive successes at which we consider the check succeeded again after it was in failure state.

`timeout_in_seconds`

(optional) Length of waiting time in seconds before marking health check failed.

`status`

(optional) Status of container

Allowed values are: 'HEALTHY', 'UNHEALTHY', 'UNKNOWN'

`status_details`

(optional) A message describing the current status in more details.

`failure_action`

(optional) The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default action is KILL. If failure action is KILL, the container will be subject to the container restart policy.

Allowed values are: 'KILL', 'NONE'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_RESOURCE_CONFIG_T Type

The resource configuration for a container. The resource configuration determines the amount of resources allocated to the container and the maximum allowed resources for a container.

Syntax
```

```

Fields

Field Description

`vcpus_limit`

(optional) The maximum amount of CPUs that can be consumed by the container's process. If you do not set a value, then the process may use all available CPU resources on the container instance. CPU usage is defined in terms of logical CPUs. This means that the maximum possible value on an E3 ContainerInstance with 1 OCPU is 2.0.

`memory_limit_in_g_bs`

(optional) The maximum amount of memory that can be consumed by the container's process. If you do not set a value, then the process may use all available memory on the instance.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SECURITY_CONTEXT_T Type

Security context for container.

Syntax
```

```

Fields

Field Description

`security_context_type`

(optional) The type of security context

Allowed values are: 'LINUX'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VOLUME_MOUNT_TBL Type

Nested table type of dbms_cloud_oci_container_instances_volume_mount_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HEALTH_CHECK_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_health_check_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_T Type

A single container on a container instance. If you delete a container, the record remains visible for a short period of time before being permanently removed.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment that contains the container.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

`availability_domain`

(required) The availability domain where the container instance that hosts the container runs.

`fault_domain`

(optional) The fault domain of the container instance that hosts the container runs.

`lifecycle_state`

(required) The current state of the container.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message that describes the current state of the container in more detail. Can be used to provide actionable information.

`exit_code`

(optional) The exit code of the container process when it stopped running.

`time_terminated`

(optional) The time when the container last deleted (terminated), in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_created`

(required) The time the container was created, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The time the container was updated, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`container_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container instance that the container is running on.

`image_url`

(required) The container image information. Currently only supports public Docker registry. You can provide either the image name (containerImage), image name with version (containerImagev1), or complete Docker image URL `docker.io/library/containerImage:latest`. If you do not provide a registry, the registry defaults to public Docker hub `docker.io/library`. The registry used for the container image must be reachable over the VNIC of the container instance.

`command`

(optional) This command overrides ENTRYPOINT process of the container. If you do not specify this command, the existing ENTRYPOINT process defined in the image is the default.

`arguments`

(optional) A list of string arguments for the ENTRYPOINT process of the container. Many containers use an ENTRYPOINT process pointing to a shell `/bin/bash`. For those containers, you can use the argument list to specify the main command in the container process.

`working_directory`

(optional) The working directory within the container's filesystem for the container process. If not specified, the default working directory from the image is used.

`environment_variables`

(optional) A map of additional environment variables to set in the environment of the ENTRYPOINT process of the container. These variables are in addition to any variables already defined in the container's image.

`volume_mounts`

(optional) List of the volume mounts.

`health_checks`

(optional) List of container health checks

`is_resource_principal_disabled`

(optional) Determines if the container will have access to the container instance resource principal. This method utilizes resource principal version 2.2. For more information on how to use the exposed resource principal elements, see https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal.

`resource_config`

(optional)

`container_restart_attempt_count`

(optional) The number of container restart attempts. Depending on the restart policy, a restart might be attempted after a health check failure or a container exit.

`security_context`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_SUMMARY_T Type

Summary information about a container.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

`availability_domain`

(required) The availability domain where the container instance that hosts this container runs.

`fault_domain`

(optional) The fault domain where the container instance that hosts the container runs.

`lifecycle_state`

(required) The current state of the container.

`lifecycle_details`

(optional) A message that describes the current state of the container in more detail. Can be used to provide actionable information.

`time_created`

(required) The time the the container was created in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The time the container was updated in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`container_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the container instance on which the container is running.

`resource_config`

(optional)

`image_url`

(required) A URL identifying the image that the container runs in, such as docker.io/library/busybox:latest. If you do not provide a tag, the tag will default to latest. If no registry is provided, will default the registry to public docker hub `docker.io/library`. The registry used for container image must be reachable over the Container Instance's VNIC.

`is_resource_principal_disabled`

(optional) Determines whether the container will have access to the container instance resource principal. This method utilizes resource principal version 2.2. For information on how to use the exposed resource principal elements, see https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal.

`security_context`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_COLLECTION_T Type

A list of containers.

Syntax
```

```

Fields

Field Description

`items`

(required) List of containers.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_COMMAND_HEALTH_CHECK_T Type

Container Health Check with command type.

Syntax
```

```

`dbms_cloud_oci_container_instances_container_command_health_check_t`is a subtype of the`dbms_cloud_oci_container_instances_container_health_check_t`type.

Fields

Field Description

`command`

(required) The list of strings that will be simplified to a single command for checking the status of the container.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_T Type

The file that is mounted on a container instance through a volume mount.

Syntax
```

```

Fields

Field Description

`file_name`

(required) The name of the file. The fileName should be unique across the volume.

`data`

(required) The base64 encoded contents of the file. The contents are decoded to plain text before mounted as a file to a container inside container instance.

`path`

(optional) (Optional) Relative path for this file inside the volume mount directory. By default, the file is presented at the root of the volume mount path.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VOLUME_T Type

A volume represents a directory with data that is accessible across multiple containers in a container instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the volume. This must be unique within a single container instance.

`volume_type`

(required) The type of volume.

Allowed values are: 'EMPTYDIR', 'CONFIGFILE'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_config_file_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_VOLUME_T Type

The volume based on configuration files received during container creation.

Syntax
```

```

`dbms_cloud_oci_container_instances_container_config_file_volume_t`is a subtype of the`dbms_cloud_oci_container_instances_container_volume_t`type.

Fields

Field Description

`configs`

(optional) Contains string key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded. It is decoded to plain text before the mount.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_DNS_CONFIG_T Type

DNS settings for containers.

Syntax
```

```

Fields

Field Description

`nameservers`

(optional) IP address of the name server..

`searches`

(optional) Search list for hostname lookup.

`options`

(optional) Options allows certain internal resolver variables to be modified.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_EMPTY_DIR_VOLUME_T Type

The empty directory volume of a container instance. You can create up to 64 EmptyDir per container instance.

Syntax
```

```

`dbms_cloud_oci_container_instances_container_empty_dir_volume_t`is a subtype of the`dbms_cloud_oci_container_instances_container_volume_t`type.

Fields

Field Description

`backing_store`

(optional) The volume type of the empty directory, can be either File Storage or Memory.

Allowed values are: 'EPHEMERAL_STORAGE', 'MEMORY'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_HEALTH_CHECK_HTTP_HEADER_T Type

Container Http headers for Http health check.

Syntax
```

```

Fields

Field Description

`name`

(required) Container HTTP header Key.

`value`

(required) Container HTTP header value.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_HEALTH_CHECK_HTTP_HEADER_TBL Type

Nested table type of dbms_cloud_oci_container_instances_health_check_http_header_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HTTP_HEALTH_CHECK_T Type

Container Health Check HTTP type.

Syntax
```

```

`dbms_cloud_oci_container_instances_container_http_health_check_t`is a subtype of the`dbms_cloud_oci_container_instances_container_health_check_t`type.

Fields

Field Description

`path`

(required) Container health check HTTP path.

`port`

(required) Container health check HTTP port.

`headers`

(optional) Container health check HTTP headers.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_CONTAINER_T Type

A container on a container instance.

Syntax
```

```

Fields

Field Description

`container_id`

(required) The OCID of the container.

`display_name`

(optional) Display name for the Container.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_CONFIG_T Type

The shape configuration for a container instance. The shape configuration determines the resources thats are available to the container instance and its containers.

Syntax
```

```

Fields

Field Description

`ocpus`

(required) The total number of OCPUs available to the container instance.

`memory_in_g_bs`

(required) The total amount of memory available to the container instance, in gigabytes.

`processor_description`

(required) A short description of the container instance's processor (CPU).

`networking_bandwidth_in_gbps`

(required) The networking bandwidth available to the container instance, in gigabits per second.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VNIC_T Type

An interface to a virtual network available to containers on a container instance.

Syntax
```

```

Fields

Field Description

`vnic_id`

(optional) The identifier of the virtual network interface card (VNIC) over which the containers accessing this network can communicate with the larger virtual cloud network.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VOLUME_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_volume_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_CONTAINER_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_instance_container_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VNIC_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_vnic_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_IMAGE_PULL_SECRET_TBL Type

Nested table type of dbms_cloud_oci_container_instances_image_pull_secret_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_T Type

A container instance to host containers. If you delete a container instance, the record remains visible for a short period of time before being permanently removed.

Syntax
```

```

Fields

Field Description

`id`

(required) An OCID that cannot be changed.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

`availability_domain`

(required) The availability domain to place the container instance.

`fault_domain`

(optional) The fault domain to place the container instance.

`lifecycle_state`

(required) The current state of the container instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message that describes the current state of the container in more detail. Can be used to provide actionable information.

`volumes`

(optional) A volume is a directory with data that is accessible across multiple containers in a container instance.

`volume_count`

(optional) The number of volumes that are attached to the container instance.

`containers`

(required) The containers on the container instance.

`container_count`

(required) The number of containers on the container instance.

`time_created`

(required) The time the container instance was created, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_updated`

(optional) The time the container instance was updated, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`shape`

(required) The shape of the container instance. The shape determines the number of OCPUs, amount of memory, and other resources that are allocated to a container instance.

`shape_config`

(required)

`vnics`

(required) The virtual networks available to the containers in the container instance.

`dns_config`

(optional)

`graceful_shutdown_timeout_in_seconds`

(optional) The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a container instance. After the timeout is reached, the processes are sent a signal to be deleted.

`image_pull_secrets`

(optional) The image pulls secrets so you can access private registry to pull container images.

`container_restart_policy`

(required) The container restart policy is applied for all containers in container instance.

Allowed values are: 'ALWAYS', 'NEVER', 'ON_FAILURE'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SUMMARY_T Type

A set of details about a single container instance returned by list APIs.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID that cannot be changed.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment to create the container instance in.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

`availability_domain`

(required) The availability domain where the container instance runs.

`fault_domain`

(optional) The fault domain where the container instance runs.

`lifecycle_state`

(required) The current state of the container instance.

`lifecycle_details`

(optional) A message that describes the current state of the container instance in more detail. Can be used to provide actionable information.

`time_created`

(required) The time the container instance was created, in the format defined by RFC3339.

`time_updated`

(optional) The time the container instance was updated, in the format defined by RFC3339.

`shape`

(required) The shape of the container instance. The shape determines the resources available to the container instance.

`shape_config`

(required)

`container_count`

(required) The number of containers in the container instance.

`graceful_shutdown_timeout_in_seconds`

(optional) The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a container instance. After the timeout is reached, the processes are sent a signal to be deleted.

`volume_count`

(optional) The number of volumes that are attached to the container instance.

`container_restart_policy`

(required) Container Restart Policy

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_COLLECTION_T Type

Summary information about a list of container instances.

Syntax
```

```

Fields

Field Description

`items`

(required) List of container instances.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_OCPU_OPTIONS_T Type

For a flexible shape, the number of OCPUs available for container instances that use this shape.

Syntax
```

```

Fields

Field Description

`l_min`

(required) The minimum number of OCPUs.

`l_max`

(required) The maximum number of OCPUs.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_MEMORY_OPTIONS_T Type

For a flexible shape, the amount of memory available for container instances that use this shape.

Syntax
```

```

Fields

Field Description

`min_in_g_bs`

(required) The minimum amount of memory (GB).

`max_in_g_bs`

(required) The maximum amount of memory (GB).

`default_per_ocpu_in_g_bs`

(required) The default amount of memory per OCPU available for this shape (GB).

`min_per_ocpu_in_g_bs`

(required) The minimum amount of memory per OCPU available for this shape (GB).

`max_per_ocpu_in_g_bs`

(required) The maximum amount of memory per OCPU available for this shape (GB).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_NETWORKING_BANDWIDTH_OPTIONS_T Type

For a flexible shape, the amount of networking bandwidth available for container instances that use this shape.

Syntax
```

```

Fields

Field Description

`min_in_gbps`

(required) The minimum amount of networking bandwidth, in gigabits per second.

`max_in_gbps`

(required) The maximum amount of networking bandwidth, in gigabits per second.

`default_per_ocpu_in_gbps`

(required) The default amount of networking bandwidth per OCPU, in gigabits per second.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_SUMMARY_T Type

Details about a shape for a container instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name identifying the shape.

`processor_description`

(required) A short description of the container instance's processor (CPU).

`ocpu_options`

(optional)

`memory_options`

(optional)

`networking_bandwidth_options`

(optional)

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_container_instances_container_instance_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_COLLECTION_T Type

A collection of container instance shapes.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of shapes.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_TCP_HEALTH_CHECK_T Type

Container Health Check with TCP type.

Syntax
```

```

`dbms_cloud_oci_container_instances_container_tcp_health_check_t`is a subtype of the`dbms_cloud_oci_container_instances_container_health_check_t`type.

Fields

Field Description

`port`

(required) Container health check port.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_IMAGE_PULL_SECRET_DETAILS_T Type

The image pull secrets for accessing private registry to pull images for containers

Syntax
```

```

Fields

Field Description

`secret_type`

(required) The type of ImagePullSecret.

Allowed values are: 'BASIC', 'VAULT'

`registry_endpoint`

(required) The registry endpoint of the container image.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_BASIC_IMAGE_PULL_SECRET_DETAILS_T Type

A CreateBasicImagePullSecretDetails is a ImagePullSecret which accepts username and password as credentials information.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_basic_image_pull_secret_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_image_pull_secret_details_t`type.

Fields

Field Description

`username`

(required) The username which should be used with the registry for authentication. The value is expected in base64 format.

`password`

(required) The password which should be used with the registry for authentication. The value is expected in base64 format.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HEALTH_CHECK_DETAILS_T Type

Container Health Check is used to check and report the status of a container.

Syntax
```

```

Fields

Field Description

`name`

(optional) Health check name.

`health_check_type`

(required) Container health check type.

Allowed values are: 'HTTP', 'TCP', 'COMMAND'

`initial_delay_in_seconds`

(optional) The initial delay in seconds before start checking container health status.

`interval_in_seconds`

(optional) Number of seconds between two consecutive runs for checking container health.

`failure_threshold`

(optional) Number of consecutive failures at which we consider the check failed.

`success_threshold`

(optional) Number of consecutive successes at which we consider the check succeeded again after it was in failure state.

`timeout_in_seconds`

(optional) Length of waiting time in seconds before marking health check failed.

`failure_action`

(optional) The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default action is KILL. If failure action is KILL, the container will be subject to the container restart policy.

Allowed values are: 'KILL', 'NONE'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_COMMAND_HEALTH_CHECK_DETAILS_T Type

Container Health Check Command type.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_container_command_health_check_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_container_health_check_details_t`type.

Fields

Field Description

`command`

(required) The list of strings that will be simplified to a single command for checking the status of the container.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VOLUME_DETAILS_T Type

A volume represents a directory with data that is accessible across multiple containers in a container instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the volume. This must be unique within a single container instance.

`volume_type`

(required) The type of volume.

Allowed values are: 'EMPTYDIR', 'CONFIGFILE'

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_CONFIG_FILE_VOLUME_DETAILS_T Type

The configuration files to pass to the container using volume mounts.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_container_config_file_volume_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_container_volume_details_t`type.

Fields

Field Description

`configs`

(optional) Contains key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded. It is decoded to plain text before the mount.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VOLUME_MOUNT_DETAILS_T Type

Defines the mapping from volume to a mount path in a container.

Syntax
```

```

Fields

Field Description

`mount_path`

(required) The volume access path.

`volume_name`

(required) The name of the volume. Avoid entering confidential information.

`sub_path`

(optional) A subpath inside the referenced volume.

`is_read_only`

(optional) Whether the volume was mounted in read-only mode. By default, the volume is not read-only.

`partition`

(optional) If there is more than one partition in the volume, reference this number of partitions. Here is an example: Number Start End Size File system Name Flags 1 1049kB 106MB 105MB fat16 EFI System Partition boot, esp 2 106MB 1180MB 1074MB xfs 3 1180MB 50.0GB 48.8GB lvm

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_RESOURCE_CONFIG_DETAILS_T Type

The size and amount of resources available to the container.

Syntax
```

```

Fields

Field Description

`vcpus_limit`

(optional) The maximum amount of CPUs that can be consumed by the container's process. If you do not set a value, then the process can use all available CPU resources on the instance. CPU usage is defined in terms of logical CPUs. This means that the maximum possible value on an E3 ContainerInstance with 1 OCPU is 2.0. A container with a 2.0 vcpusLimit could consume up to 100% of the CPU resources available on the container instance. Values can be fractional. A value of \"1.5\" means that the container can consume at most the equivalent of 1 and a half logical CPUs worth of CPU capacity.

`memory_limit_in_g_bs`

(optional) The maximum amount of memory that can be consumed by the container's process. If you do not set a value, then the process may use all available memory on the instance.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_SECURITY_CONTEXT_DETAILS_T Type

Security context for container.

Syntax
```

```

Fields

Field Description

`security_context_type`

(optional) The type of security context

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VOLUME_MOUNT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_volume_mount_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HEALTH_CHECK_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_container_health_check_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DETAILS_T Type

Information to create a new container within a container instance. The container created by this call contains both the tags specified in this object and any tags specified in the parent container instance. The container is created in the same compartment, availability domain, and fault domain as its container instance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. If you don't provide a name, a name is generated automatically.

`image_url`

(required) A URL identifying the image that the container runs in, such as docker.io/library/busybox:latest. If you do not provide a tag, the tag will default to latest. If no registry is provided, will default the registry to public docker hub `docker.io/library`. The registry used for container image must be reachable over the Container Instance's VNIC.

`command`

(optional) An optional command that overrides the ENTRYPOINT process. If you do not provide a value, the existing ENTRYPOINT process defined in the image is used.

`arguments`

(optional) A list of string arguments for a container's ENTRYPOINT process. Many containers use an ENTRYPOINT process pointing to a shell (/bin/bash). For those containers, this argument list specifies the main command in the container process. The total size of all arguments combined must be 64 KB or smaller.

`working_directory`

(optional) The working directory within the container's filesystem for the container process. If not specified, the default working directory from the image is used.

`environment_variables`

(optional) A map of additional environment variables to set in the environment of the container's ENTRYPOINT process. These variables are in addition to any variables already defined in the container's image. The total size of all environment variables combined, name and values, must be 64 KB or smaller.

`volume_mounts`

(optional) List of the volume mounts.

`is_resource_principal_disabled`

(optional) Determines if the container will have access to the container instance resource principal. This method utilizes resource principal version 2.2. For information on how to use the exposed resource principal elements, see https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal.

`resource_config`

(optional)

`health_checks`

(optional) list of container health checks to check container status and take appropriate action if container status is failed. There are three types of health checks that we currently support HTTP, TCP, and Command.

`security_context`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DNS_CONFIG_DETAILS_T Type

Allow customers to define DNS settings for containers. If this is not provided, the containers use the default DNS settings of the subnet.

Syntax
```

```

Fields

Field Description

`nameservers`

(optional) IP address of a name server that the resolver should query, either an IPv4 address (in dot notation), or an IPv6 address in colon (and possibly dot) notation. If null, uses nameservers from subnet dhcpDnsOptions.

`searches`

(optional) Search list for host-name lookup. If null, we will use searches from subnet dhcpDnsOptios.

`options`

(optional) Options allows certain internal resolver variables to be modified. Options are a list of objects in https://man7.org/linux/man-pages/man5/resolv.conf.5.html. Examples: [\"ndots:n\", \"edns0\"].

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_EMPTY_DIR_VOLUME_DETAILS_T Type

The empty directory for the container instance.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_container_empty_dir_volume_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_container_volume_details_t`type.

Fields

Field Description

`backing_store`

(optional) The volume type of the empty directory, can be either File Storage or Memory.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HTTP_HEALTH_CHECK_DETAILS_T Type

Container Health Check HTTP type.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_container_http_health_check_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_container_health_check_details_t`type.

Fields

Field Description

`path`

(required) Container health check HTTP path.

`port`

(required) Container health check HTTP port.

`headers`

(optional) Container health check HTTP headers.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_INSTANCE_SHAPE_CONFIG_DETAILS_T Type

The size and amount of resources available to the container instance.

Syntax
```

```

Fields

Field Description

`ocpus`

(required) The total number of OCPUs available to the container instance.

`memory_in_g_bs`

(optional) The total amount of memory available to the container instance (GB).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VNIC_DETAILS_T Type

Information to create a virtual network interface card (VNIC) which gives the containers on this container instance access to a virtual client network (VCN). You use this object when creating the primary VNIC during container instance launch or when creating a secondary VNIC. This VNIC is created in the same compartment as the specified subnet on behalf of the customer. The VNIC created by this call contains both the tags specified in this object as well as any tags specified in the parent container instance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.

`hostname_label`

(optional) The hostname for the VNIC's primary private IP. Used for DNS.

`is_public_ip_assigned`

(optional) Whether the VNIC should be assigned a public IP address.

`skip_source_dest_check`

(optional) Whether the source/destination check is disabled on the VNIC.

`nsg_ids`

(optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to.

`private_ip`

(optional) A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR.

`subnet_id`

(required) The OCID of the subnet to create the VNIC in.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VOLUME_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_container_volume_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_container_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VNIC_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_container_vnic_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_IMAGE_PULL_SECRET_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_container_instances_create_image_pull_secret_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_INSTANCE_DETAILS_T Type

Information to create a container instance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. If you don't provide a name, a name is generated automatically.

`compartment_id`

(required) The compartment OCID.

`availability_domain`

(required) The availability domain where the container instance runs.

`fault_domain`

(optional) The fault domain where the container instance runs.

`shape`

(required) The shape of the container instance. The shape determines the resources available to the container instance.

`shape_config`

(required)

`volumes`

(optional) A volume is a directory with data that is accessible across multiple containers in a container instance. You can attach up to 32 volumes to single container instance.

`containers`

(required) The containers to create on this container instance.

`vnics`

(required) The networks available to containers on this container instance.

`dns_config`

(optional)

`graceful_shutdown_timeout_in_seconds`

(optional) The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a container instance. After the timeout is reached, the processes are sent a signal to be deleted.

`image_pull_secrets`

(optional) The image pulls secrets so you can access private registry to pull container images.

`container_restart_policy`

(optional) Container restart policy

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_TCP_HEALTH_CHECK_DETAILS_T Type

Container Health Check TCP type.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_container_tcp_health_check_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_container_health_check_details_t`type.

Fields

Field Description

`port`

(required) Container health check port.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_LINUX_SECURITY_CONTEXT_DETAILS_T Type

Security context for Linux container.

Syntax
```

```

`dbms_cloud_oci_container_instances_create_linux_security_context_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_security_context_details_t`type.

Fields

Field Description

`run_as_user`

(optional) The user ID (UID) to run the entrypoint process of the container. Defaults to user specified UID in container image metadata if not provided. This must be provided if runAsGroup is provided.

`run_as_group`

(optional) The group ID (GID) to run the entrypoint process of the container. Uses runtime default if not provided.

`is_non_root_user_check_enabled`

(optional) Indicates if the container must run as a non-root user. If true, the service validates the container image at runtime to ensure that it is not going to run with UID 0 (root) and fails the container instance creation if the validation fails.

`is_root_file_system_readonly`

(optional) Determines if the container will have a read-only root file system. Default value is false.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VAULT_IMAGE_PULL_SECRET_DETAILS_T Type

A CreateVaultImagePullSecretDetails is a ImagePullSecret which accepts secretId as credentials information. **Sample Format for username and password in Vault Secret** ``` { \"username\": \"this-is-not-the-secret\", \"password\": \"example-password\" } ```

Syntax
```

```

`dbms_cloud_oci_container_instances_create_vault_image_pull_secret_details_t`is a subtype of the`dbms_cloud_oci_container_instances_create_image_pull_secret_details_t`type.

Fields

Field Description

`secret_id`

(required) The OCID of the secret for registry credentials.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_LINUX_SECURITY_CONTEXT_T Type

Security context for Linux container.

Syntax
```

```

`dbms_cloud_oci_container_instances_linux_security_context_t`is a subtype of the`dbms_cloud_oci_container_instances_security_context_t`type.

Fields

Field Description

`run_as_user`

(optional) The user ID (UID) to run the entrypoint process of the container. Defaults to user specified UID in container image metadata if not provided. This must be provided if runAsGroup is provided.

`run_as_group`

(optional) The group ID (GID) to run the entrypoint process of the container. Uses runtime default if not provided.

`is_non_root_user_check_enabled`

(optional) Indicates if the container must run as a non-root user. If true, the service validates the container image at runtime to ensure that it is not going to run with UID 0 (root) and fails the container instance creation if the validation fails.

`is_root_file_system_readonly`

(optional) Determines if the container will have a read-only root file system. Default value is false.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_UPDATE_CONTAINER_DETAILS_T Type

The container information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_UPDATE_CONTAINER_INSTANCE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VAULT_IMAGE_PULL_SECRET_T Type

A VaultImagePullSecret is a ImagePullSecret which accepts secretId as credentials information.

Syntax
```

```

`dbms_cloud_oci_container_instances_vault_image_pull_secret_t`is a subtype of the`dbms_cloud_oci_container_instances_image_pull_secret_t`type.

Fields

Field Description

`secret_id`

(required) The OCID of the secret for registry credentials.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted remains in the IN_PROGRESS state until work is complete for that resource, at which point it updates to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'FAILED'

`identifier`

(required) The ID of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_container_instances_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_CONTAINER_INSTANCE', 'UPDATE_CONTAINER_INSTANCE', 'DELETE_CONTAINER_INSTANCE', 'MOVE_CONTAINER_INSTANCE', 'START_CONTAINER_INSTANCE', 'STOP_CONTAINER_INSTANCE', 'RESTART_CONTAINER_INSTANCE', 'UPDATE_CONTAINER'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm)for a list of error codes.

`message`

(required) A description of the issue encountered.

`l_timestamp`

(required) The time the error occured, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_container_instances_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_T Type

A log message from a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written, in the format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_container_instances_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of work request.

Allowed values are: 'CREATE_CONTAINER_INSTANCE', 'UPDATE_CONTAINER_INSTANCE', 'DELETE_CONTAINER_INSTANCE', 'MOVE_CONTAINER_INSTANCE', 'START_CONTAINER_INSTANCE', 'STOP_CONTAINER_INSTANCE', 'RESTART_CONTAINER_INSTANCE', 'UPDATE_CONTAINER'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_container_instances_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Container Instances Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-5E2A1E91-0A72-43D7-ABDF-4744AAD29DDD)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-18145AD5-8FF6-44CB-B102-A2CB8252305A)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_IMAGE_PULL_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-636898EC-5B49-4497-BE75-7BF4D9462D24)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_BASIC_IMAGE_PULL_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-9569DCC4-0683-4287-BB3B-FC639545865F)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CHANGE_CONTAINER_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-7587A115-FB03-49A1-AD36-F7D905F15F29)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VOLUME_MOUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-FAE4ACCD-2CA5-46A4-8AAF-20647DFBC177)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HEALTH_CHECK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-988D484B-2AA3-4A60-87B5-C009B2234470)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_RESOURCE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-3AE31E1F-99BC-47ED-A3A5-8F2869262311)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SECURITY_CONTEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-02086FFE-1619-4B74-A867-08C9CE841E3A)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VOLUME_MOUNT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-10B009E3-05D9-45AC-99B8-0C5759B5600B)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HEALTH_CHECK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-B5A4C9A9-392E-43EB-AD8B-824E2467BB14)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-D655FA43-39F4-44B7-BE20-21FDCD634CB5)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-03423594-164B-4758-8212-BC64B2E75153)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-BA9C1912-833D-4AA7-B8AE-FAECBC7AB615)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-DCBCA518-5A57-4EB9-B308-B492505A1ABA)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_COMMAND_HEALTH_CHECK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-1D351A66-EB62-4923-BEC2-498E2E717D56)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-D1CEA832-C909-4E59-BB70-FFEC6A209306)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-AAD296C9-A0B5-4CF0-80AF-2965E5872A99)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-4F8C95A8-F90F-4A8F-A690-CAC2DC172981)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_CONFIG_FILE_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A41D6198-7721-4D09-8FD5-7157EFE069AF)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_DNS_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-60C11FCC-A56E-4131-B438-FD1A24C86459)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_EMPTY_DIR_VOLUME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-8FB62BCA-411E-4481-90F0-DCF51D7BB27A)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_HEALTH_CHECK_HTTP_HEADER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-32789DC5-374F-43A5-A706-9AFC73329F22)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_HEALTH_CHECK_HTTP_HEADER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-BA047AC1-4CA6-434F-B28A-A804F1F0D045)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_HTTP_HEALTH_CHECK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-EDD5C1B9-A9D3-46D9-B9FA-BCDADD8B8216)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_CONTAINER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-62D5DDEE-77CF-471D-BD85-2A0CC080A81B)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-389382E0-6B22-4E4D-9BCE-8E7E1933D08B)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VNIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-7E9E1D23-CDA0-4707-830C-EAFD34943AEA)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VOLUME_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A86EF773-A959-4AF2-B590-C71DE40BA9BC)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_CONTAINER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-5D92FCB7-79FA-48D4-80E0-F62AAD698E53)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_VNIC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-EAF14402-2F2A-488E-9C12-C073057A48A8)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_IMAGE_PULL_SECRET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-10FF0B54-F87F-4812-BE76-3F8FC7AD4D83)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-78551C39-1D8B-45AB-91C8-AD4041F48011)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-277F8BA1-6868-49AE-BEAB-479B41DCC5B2)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-0B238C7F-85BD-4185-A4EC-114FC20669FD)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-6798BD86-B0B0-477E-B547-AB675042C773)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_OCPU_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-6D0AC115-C9AC-4998-95E6-FC7DF8B9EB94)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_MEMORY_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-69831FC3-898A-4FC5-A75A-44E35789D8A9)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_SHAPE_NETWORKING_BANDWIDTH_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-359014FE-5269-4E57-B0CB-CD9253BBC713)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-AF7CF474-1502-4F66-A83F-7DD30F4742CC)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-554EDBE2-F10B-441C-B5F4-D1297B40B4B3)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_INSTANCE_SHAPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-F0FF6B9B-FED5-4805-A0C7-10A585982D54)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CONTAINER_TCP_HEALTH_CHECK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-1BA37FF3-409E-48E8-B786-5C689520F5DD)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_IMAGE_PULL_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-B772E600-6B4F-47F1-9923-F5A9047EC15F)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_BASIC_IMAGE_PULL_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-3016F398-ABDA-4EE1-9485-C9240FB1E756)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HEALTH_CHECK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-14ECBB73-256B-4DC2-9441-C6A5801282B7)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_COMMAND_HEALTH_CHECK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-4D6FE639-7A57-477F-8852-12CD6839E150)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-947C493D-5192-4C94-89C4-AE2044952740)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_CONFIG_FILE_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-98152B2E-89BD-42A5-80D0-85F02DE5B9DB)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VOLUME_MOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-26C2C0BF-E896-412C-A57D-EA9736FB7D46)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_RESOURCE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-B952D2FB-3F45-47B9-8CB8-2EFE2561E427)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_SECURITY_CONTEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-B53B8A74-1593-4B63-8A2F-A19AA6A78E59)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VOLUME_MOUNT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-E3B18B0C-4D09-42F7-BFA3-03E8849B488F)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HEALTH_CHECK_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A2C64343-D041-4E2D-9B05-43695ADF01AE)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A88FAD9B-E074-4DA3-9379-1A6712103CDF)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DNS_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-CFBE9AD9-64A8-4543-A5E3-CE4FA7B7CF07)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_EMPTY_DIR_VOLUME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-F1B777F1-09FC-4FF8-A924-A5EFC9C19605)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_HTTP_HEALTH_CHECK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A5CA4991-75A3-44A2-85C0-780F5ADB84D0)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_INSTANCE_SHAPE_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-BE9675A4-36B6-455A-947E-4C3B18375361)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VNIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-1C476137-6A8F-4084-8C3A-E4B84E7C4490)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VOLUME_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-265FFA15-38C9-4DE8-A7C8-7D7A297EE77D)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-608FD984-BBE8-4FFE-B17E-FE3287769BF2)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_VNIC_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-F6FCDC8E-6E4D-4828-95F5-5D860A8322E0)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_IMAGE_PULL_SECRET_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-6754E840-6AA6-4015-BB30-E121405F6F32)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-9A603DDD-E04D-4AC1-A862-F9596F5804FA)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_CONTAINER_TCP_HEALTH_CHECK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-4C2ECAD2-DC67-4F3B-9CC4-1779D870E483)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_LINUX_SECURITY_CONTEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-043DBFB2-3A58-4C03-932A-8B1E56219DC8)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_CREATE_VAULT_IMAGE_PULL_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-84339602-C9D4-4743-AFFB-441FA4E1311D)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-0007F9D0-6C56-4831-A036-3EB54DFC4A56)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_LINUX_SECURITY_CONTEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A6B54FD2-1397-4972-B108-BED312EE869D)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_UPDATE_CONTAINER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-25F59E2F-ECB1-4BA9-92E7-942166072958)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_UPDATE_CONTAINER_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-F3BC9919-1AA2-44D3-BEA4-0D3D3745E1FD)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_VAULT_IMAGE_PULL_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-D2E871BC-08D2-4743-808E-865FA83EBD50)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-16A90F63-0920-4A55-B05F-7723982A6CC2)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-E894E7B5-12BF-4897-B153-6E671234BA59)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-E8BCFA73-8465-411E-AA89-BAA7B8E52B5C)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-71ED7C82-7FD7-4CC3-8625-3898BC2A318A)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-DE0FF858-721A-4ACE-85EB-41AEDE9EA761)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-56CE4E7B-FAFC-4D12-BE17-7E5826E69EAC)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-DAE01301-259F-485D-B72B-41120536840D)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-D649E2CF-1777-4EC1-8C6A-750E06890B9C)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-A836130F-3DCB-4557-AA0F-49242F88941D)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-EF184D61-02EA-43EB-A393-B96AF6FF4E7B)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-67CB95F5-27F1-4A4C-B043-193D03DC84CD)
- [DBMS_CLOUD_OCI_CONTAINER_INSTANCES_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/container_instances_t.html#ADSDK-GUID-DEA8EFFD-9D5C-408E-A622-3BB224E43172)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
