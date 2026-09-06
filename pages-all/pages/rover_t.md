# Roving Edge Infrastructure Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#dcoc-content-body)

## Roving Edge Infrastructure Common Types

### DBMS_CLOUD_OCI_ROVER_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_CA_DETAILS_T Type

Information about the detailed CA bundle content of the rover node.

Syntax
```

```

Fields

Field Description

`ca_bundle_pem`

(optional) Plain text certificate chain in PEM format for the subordinate CA associated with given roverNode.

`certificate_max_validity_duration`

(optional) Max validity of leaf certificates issued by the CA associated with given node, in days, in ISO 8601 format, example \"P365D\".

### DBMS_CLOUD_OCI_ROVER_CA_BUNDLE_RESPONSE_T Type

Information about the CA Bundle of the rover node.

Syntax
```

```

Fields

Field Description

`rover_node_id`

(required) rover node ocid

`ca_details`

(optional)

### DBMS_CLOUD_OCI_ROVER_CERTIFICATE_DETAILS_T Type

The details of Oracle Cloud Infrastructure certificate created

Syntax
```

```

Fields

Field Description

`certificate_id`

(optional) The id of the certificate.

`certificate_name`

(optional) The name of the certificate.

### DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_CLUSTER_COMPARTMENT_DETAILS_T Type

Object for moving a cluster to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resources should be moved.

### DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_ENTITLEMENT_COMPARTMENT_DETAILS_T Type

Object for moving an entitlement to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resources should be moved.

### DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_NODE_COMPARTMENT_DETAILS_T Type

Object for moving a node to a different compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID]](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resources should be moved.

### DBMS_CLOUD_OCI_ROVER_SHIPPING_ADDRESS_T Type

Shipping address for rover devices.

Syntax
```

```

Fields

Field Description

`addressee`

(required) Addressee in shipping address.

`care_of`

(optional) CareOf for shipping address.

`address1`

(required) Address line 1.

`address2`

(optional) Address line 2.

`address3`

(optional) Address line 3.

`address4`

(optional) Address line 4.

`city_or_locality`

(required) city or locality for shipping address.

`state_or_region`

(required) state or region for shipping address.

`zipcode`

(required) zipcode for shipping address.

`country`

(required) country for shipping address.

`phone_number`

(required) recipient phone number.

`email`

(optional) recipient email address.

### DBMS_CLOUD_OCI_ROVER_ROVER_WORKLOAD_T Type

Information about a RoverWorkload.

Syntax
```

```

Fields

Field Description

`name`

(optional) Name of the Rover Workload

`compartment_id`

(required) The OCID of the compartment containing the workload.

`id`

(required) The Unique Oracle ID (OCID) that is immutable on creation.

`l_size`

(optional) Size of the workload.

`object_count`

(optional) Number of objects in a workload.

`prefix`

(optional) Prefix to filter objects in case it is a bucket.

`range_start`

(optional) Start of the range in a bucket.

`range_end`

(optional) End of the range in a bucket.

`workload_type`

(required) The type of workload

`work_request_id`

(optional) The compute work request id to track progress of custom image exports.

### DBMS_CLOUD_OCI_ROVER_ROVER_WORKLOAD_TBL Type

Nested table type of dbms_cloud_oci_rover_rover_workload_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_CLUSTER_DETAILS_T Type

The information required to create a RoverCluster.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment containing the RoverCluster.

`cluster_size`

(required) Number of nodes desired in the cluster, in standalone clusters, between 5 and 15 inclusive. In station clusters, between 15 and 30 inclusive.

`customer_shipping_address`

(optional)

`cluster_workloads`

(optional) List of existing workloads that should be provisioned on the nodes.

`cluster_type`

(optional) Type of cluster.

Allowed values are: 'STANDALONE', 'STATION'

`super_user_password`

(optional) Root password for the rover cluster.

`enclosure_type`

(optional) The type of enclosure rover nodes in this cluster are shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`unlock_passphrase`

(optional) Password to unlock the rover cluster.

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the cluster if they chose customer pickup.

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped Rover Cluster.

`subscription_id`

(optional) ID provided to customer after successful subscription to Rover Stations.

`lifecycle_state`

(optional) The current state of the RoverCluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover cluster return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover cluster return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`master_key_id`

(optional) Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_ENTITLEMENT_DETAILS_T Type

Information required to create a RoverEntitlement.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the RoverEntitlement.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`requestor_name`

(required) Requestor name for the entitlement.

`requestor_email`

(required) Requestor email for the entitlement.

`entitlement_details`

(optional) Details about the entitlement.

`lifecycle_state`

(optional) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`tenant_id`

(optional) tenant Id.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_NODE_DETAILS_T Type

The information required to create a RoverNode.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment containing the RoverNode.

`shape`

(optional) The shape of the node.

`customer_shipping_address`

(optional)

`node_workloads`

(optional) List of existing workloads that should be provisioned on the node.

`super_user_password`

(optional) Root password for the rover node.

`unlock_passphrase`

(optional) Passphrase to unlock the rover node.

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the device if they chose customer pickup.

`public_key`

(optional) The public key of the resource principal

`time_return_window_starts`

(optional) Start time for the window to pickup the device from customer.

`time_return_window_ends`

(optional) End time for the window to pickup the device from customer.

`lifecycle_state`

(optional) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`enclosure_type`

(optional) The type of enclosure rover nodes in this cluster are shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`serial_number`

(optional) Serial number of the node.

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped FmsRoverNode.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover node return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover node return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover node return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`master_key_id`

(optional) Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.

`certificate_authority_id`

(optional) The certificateAuthorityId of subordinate/intermediate certificate authority.

`time_cert_validity_end`

(optional) The time after which leaf certificate will invalid.

`common_name`

(optional) The common name for the leaf certificate.

`cert_compartment_id`

(optional) The compartmentId of the leaf certificate.

`cert_key_algorithm`

(optional) key algorithm for issuing leaf certificate.

Allowed values are: 'RSA2048', 'RSA4096', 'ECDSA_P256', 'ECDSA_P384'

`cert_signature_algorithm`

(optional) signature algorithm for issuing leaf certificate.

Allowed values are: 'SHA256_WITH_RSA', 'SHA384_WITH_RSA', 'SHA512_WITH_RSA', 'SHA256_WITH_ECDSA', 'SHA384_WITH_ECDSA', 'SHA512_WITH_ECDSA'

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_CURRENT_ROVER_BUNDLE_DETAILS_T Type

Information required to list all available valid rover bundle versions that can be upgraded based on current bundle version.

Syntax
```

```

Fields

Field Description

`current_rover_bundle_version`

(required) The version of current rover bundle on customer's roverNode or roverCluster device.

### DBMS_CLOUD_OCI_ROVER_ERROR_T Type

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

### DBMS_CLOUD_OCI_ROVER_GENERATE_CERTIFICATE_RESPONSE_T Type

The information of rover node certificate generated by Oracle Cloud Infrastructure certificate service.

Syntax
```

```

Fields

Field Description

`rover_node_id`

(required) The id of the rover node.

`certificate_details`

(optional)

### DBMS_CLOUD_OCI_ROVER_LEAF_CERTIFICATE_DETAILS_T Type

The details of leaf certificate

Syntax
```

```

Fields

Field Description

`certificate_id`

(optional) The id of the certificate

`certificate_pem`

(optional) The certificate content in PEM format

### DBMS_CLOUD_OCI_ROVER_LEAF_CERTIFICATE_RESPONSE_T Type

The information for a left certificate for a rover node

Syntax
```

```

Fields

Field Description

`rover_node_id`

(required) The id of the rover node.

`leaf_certificate_details`

(optional)

### DBMS_CLOUD_OCI_ROVER_RENEW_CERTIFICATE_RESPONSE_T Type

The information of renewed rover node certificate.

Syntax
```

```

Fields

Field Description

`rover_node_id`

(required) The id of the rover node.

`certificate_details`

(optional)

### DBMS_CLOUD_OCI_ROVER_REPLACE_CA_DETAILS_T Type

Information about the detailed CA bundle replacement of the rover node.

Syntax
```

```

Fields

Field Description

`ca_bundle_pem`

(optional) Plain text certificate chain in PEM format for the subordinate CA associated with given roverNode.

`certificate_max_validity_duration`

(optional) Max validity of leaf certificates issued by the CA associated with given node, in days, in ISO 8601 format, example \"P365D\".

`cert_key_algorithm`

(optional) key algorithm for issuing leaf certificate.

Allowed values are: 'RSA2048', 'RSA4096', 'ECDSA_P256', 'ECDSA_P384'

`cert_signature_algorithm`

(optional) signature algorithm for issuing leaf certificate.

Allowed values are: 'SHA256_WITH_RSA', 'SHA384_WITH_RSA', 'SHA512_WITH_RSA', 'SHA256_WITH_ECDSA', 'SHA384_WITH_ECDSA', 'SHA512_WITH_ECDSA'

### DBMS_CLOUD_OCI_ROVER_REPLACE_CERTIFICATE_AUTHORITY_RESPONSE_T Type

Information about the replace CA Bundle of the rover node.

Syntax
```

```

Fields

Field Description

`rover_node_id`

(required) rover node ocid

`replace_ca_details`

(optional)

### DBMS_CLOUD_OCI_ROVER_REQUEST_ADDITIONAL_NODES_DETAILS_T Type

Object for request additional nodes for a roverCluster

Syntax
```

```

Fields

Field Description

`number_of_additional_nodes`

(required) Number of additional nodes to be requested for a roverCluster.

### DBMS_CLOUD_OCI_ROVER_REQUEST_ROVER_BUNDLE_DETAILS_T Type

Information required by Object Storage to process a request to copy an object to another bucket.

Syntax
```

```

Fields

Field Description

`destination_compartment_id`

(required) The compartment OCID of destination compartment that the bundle will be copied to.

`destination_bucket_name`

(required) The destination bucket name the bundle will be copied to.

`bundle_version`

(required) The bundle version that customer wants to upgrade to.

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_SUMMARY_T Type

Summary of the RoverBundleRequest

Syntax
```

```

Fields

Field Description

`id`

(required) The unique identifier of roverBundleRequest.

`destination_compartment_id`

(optional) The OCID of destination compartment that the bundle will be copied to.

`destination_bucket_name`

(optional) The destination bucket name the bundle will be copied to.

`bundle_version`

(optional) The bundle version that customer wants to upgrade to.

`work_request_id`

(required) The work request id for an async copyObject operation.

`time_task_created`

(optional) The time of the task was created. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_rover_bundle_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_COLLECTION_T Type

All the roverBundleRequests associated to this roverNode or roverCluster.

Syntax
```

```

Fields

Field Description

`items`

(required) List of roverBundleRequests.

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_STATUS_T Type

The status of the rover bundle status by a specified work request id.

Syntax
```

```

Fields

Field Description

`status`

(required) The progress of the workflow.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'COMPLETED', 'CANCELING', 'CANCELED'

`percent_complete`

(optional) Percentage of the work request completed.

`time_accepted`

(optional) The date and time the work request was created. An RFC3339 formatted datetime string.

`time_started`

(optional) The date and time the work request was started. An RFC3339 formatted datetime string.

`time_finished`

(optional) The date and time the work request was finished. An RFC3339 formatted datetime string.

`bundle_name`

(optional) The full name of the bundle.

`error_message`

(optional) The error message if work request fails.

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_STATUS_DETAILS_T Type

Information required to retrieve rover bundle status of a copyObject operation.

Syntax
```

```

Fields

Field Description

`work_request_id`

(required) The workRequestId for an async copyObject operation.

### DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_VERSION_T Type

Description of rover bundle version.

Syntax
```

```

Fields

Field Description

`bundle_version`

(required) The version of the rover bundle.

`compartment_id`

(optional) The compartment OCID of roverNode/roverCluster that needs to be upgraded.

`bundle_name`

(optional) The full name of the bundle.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SUMMARY_T Type

Summary of the RoverNode.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the RoverNode.

`compartment_id`

(required) The OCID of the compartment containing the RoverNode.

`cluster_id`

(optional) The cluster ID if the node is part of a cluster.

`serial_number`

(optional) Serial number of the node.

`node_type`

(optional) The type of node indicating if it belongs to a cluster

Allowed values are: 'STANDALONE', 'CLUSTERED', 'STATION'

`shape`

(optional) The shape of the node.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time the the RoverNode was created. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_rover_node_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_T Type

Description of RoverCluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of RoverCluster.

`compartment_id`

(required) The OCID of the compartment containing the RoverCluster.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`cluster_size`

(required) Size of the cluster.

`time_created`

(optional) The time the the RoverCluster was created. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the RoverCluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`customer_shipping_address`

(optional)

`nodes`

(optional) The summary of nodes that are part of this cluster.

`enclosure_type`

(optional) The type of enclosure rover nodes in this cluster are shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`time_customer_received`

(optional) Time when customer received the cluster.

`time_customer_returned`

(optional) Time when customer returned the cluster.

`delivery_tracking_info`

(optional) Tracking information for device shipping.

`cluster_workloads`

(optional) List of existing workloads that should be provisioned on the nodes.

`cluster_type`

(optional) Type of cluster.

Allowed values are: 'STANDALONE', 'STATION'

`subscription_id`

(optional) ID provided to customer after successful subscription to Rover Stations.

`exterior_door_code`

(optional) Service generated code for the exterior trailer door of the trailer.

`interior_alarm_disarm_code`

(optional) Service generated code to disarm the interior alarm of the trailer.

`super_user_password`

(optional) Root password for the rover cluster.

`unlock_passphrase`

(optional) Password to unlock the rover cluster.

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped Rover Cluster.

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the device if they chose customer pickup.

`time_return_window_starts`

(optional) Start time for the window to pickup the device from customer.

`time_return_window_ends`

(optional) End time for the window to pickup the device from customer.

`return_shipping_label_uri`

(optional) Uri to download return shipping label.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover cluster return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover cluster return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`image_export_par`

(optional) The link to pre-authenticated request for a bucket where image workloads are moved.

`master_key_id`

(optional) Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.

`tags`

(optional) The tags associated with tagSlug.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_CERTIFICATE_T Type

The certificate response

Syntax
```

```

Fields

Field Description

`certificate`

(required) The certificate that can be installed on a client to do TLS communication to the cluster

### DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_SUMMARY_T Type

Summary of the RoverCluster.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of RoverCluster.

`compartment_id`

(required) The OCID of the compartment containing the RoverCluster.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time the the RoverCluster was created. An RFC3339 formatted datetime string

`nodes`

(optional) The nodes that are part of this cluster.

`cluster_size`

(optional) Size of the cluster.

`cluster_type`

(optional) Type of cluster.

Allowed values are: 'STANDALONE', 'STATION'

`lifecycle_state`

(required) The current state of the RoverCluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_rover_cluster_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_COLLECTION_T Type

Results of a roverCluster search. Contains both RoverClusterSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of roverClusterSummary.

### DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_T Type

Information about a RoverEntitlement.

Syntax
```

```

Fields

Field Description

`tenant_id`

(optional) tenant Id.

`id`

(required) A property that can uniquely identify the rover entitlement.

`compartment_id`

(required) The compartment Id for the entitlement.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`requestor_name`

(required) Requestor name for the entitlement.

`requestor_email`

(required) Requestor email for the entitlement.

`lifecycle_state`

(required) Lifecyclestate for the entitlement.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETED'

`entitlement_details`

(optional) Details about the entitlement.

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`time_created`

(optional) Time of creation for the entitlement.

`time_updated`

(optional) Time when the entitlement was last updated.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_SUMMARY_T Type

Rover entitlement summary.

Syntax
```

```

Fields

Field Description

`id`

(optional) Id of the entitlement.

`compartment_id`

(required) The compartment Id.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`requestor_name`

(optional) Requestor name for the entitlement.

`requestor_email`

(optional) Email id of the requestor for entitlement.

`lifecycle_state`

(required) Lifecyclestate for the entitlement.

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_rover_entitlement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_COLLECTION_T Type

Results of a roverEntitlement search. Contains RoverEntitlementSummary.

Syntax
```

```

Fields

Field Description

`items`

(required) List of RoverEntitlementSummary.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_T Type

Information about a RoverNode.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of RoverNode.

`cluster_id`

(optional) The cluster ID if the node is part of a cluster.

`compartment_id`

(required) The OCID of the compartment containing the RoverNode.

`node_type`

(optional) The type of node indicating if it belongs to a cluster

Allowed values are: 'STANDALONE', 'CLUSTERED', 'STATION'

`shape`

(optional) The shape of the node.

`enclosure_type`

(optional) The type of enclosure rover node is shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`serial_number`

(optional) Serial number of the node.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`time_created`

(optional) The time the the RoverNode was created. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`customer_shipping_address`

(optional)

`node_workloads`

(optional) List of existing workloads that should be provisioned on the node.

`time_customer_receieved`

(optional) Date and time when customer received tne node.

`time_customer_returned`

(optional) Date and time when customer returned the node.

`delivery_tracking_info`

(optional) Tracking information for device shipping.

`super_user_password`

(optional) Root password for the rover node.

`unlock_passphrase`

(optional) Password to unlock the rover node.

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the device if they chose customer pickup.

`time_return_window_starts`

(optional) Start time for the window to pickup the device from customer.

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped RoverNode.

`time_return_window_ends`

(optional) End time for the window to pickup the device from customer.

`return_shipping_label_uri`

(optional) Uri to download return shipping label.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover node return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover node return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover node return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`public_key`

(optional) The public key of the resource principal

`image_export_par`

(optional) The link to pre-authenticated request for a bucket where image workloads are moved.

`master_key_id`

(optional) Customer provided master key ID to encrypt secret information. If not provided, Rover's master key will be used for encryption.

`certificate_authority_id`

(optional) The certificateAuthorityId of subordinate/intermediate certificate authority.

`time_cert_validity_end`

(optional) The time after which leaf certificate will invalid.

`common_name`

(optional) The common name for the leaf certificate.

`cert_compartment_id`

(optional) The compartmentId of the leaf certificate.

`certificate_version_number`

(optional) The version number of the leaf certificate.

`certificate_id`

(optional) The id of the leaf certificate.

`cert_key_algorithm`

(optional) key algorithm for issuing leaf certificate.

Allowed values are: 'RSA2048', 'RSA4096', 'ECDSA_P256', 'ECDSA_P384'

`cert_signature_algorithm`

(optional) signature algorithm for issuing leaf certificate.

Allowed values are: 'SHA256_WITH_RSA', 'SHA384_WITH_RSA', 'SHA512_WITH_RSA', 'SHA256_WITH_ECDSA', 'SHA384_WITH_ECDSA', 'SHA512_WITH_ECDSA'

`tags`

(optional) The tags associated with tagSlug.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_ACTION_SET_KEY_DETAILS_T Type

The information required to update a rover node's set key details.

Syntax
```

```

Fields

Field Description

`public_key`

(optional) The public key of the resource principal

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_CERTIFICATE_T Type

The certificate response

Syntax
```

```

Fields

Field Description

`certificate`

(required) The certificate that can be installed on a client to do TLS communication to the node

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_COLLECTION_T Type

Results of a roverNode search. Contains both RoverNodeSummary items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of roverNodes.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_ENCRYPTION_KEY_T Type

The response containing encryption key for a rover node.

Syntax
```

```

Fields

Field Description

`encryption_key`

(required) The encryption key key for a rover node.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_GENERATE_CERTIFICATE_DETAILS_T Type

The information required to generate a certificate for a roverNode.

Syntax
```

```

Fields

Field Description

`csr`

(required) The certificate signing request (in PEM format), max size 10240.

`time_cert_validity_end`

(required) Time when the generated certificate's validity will end.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_GET_RPT_T Type

The resource principal token response.

Syntax
```

```

Fields

Field Description

`resource_principal_token`

(required) The resource principal token blob that contains claims about the resource.

`service_principal_session_token`

(optional) The service principal session token

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_RENEW_CERTIFICATE_DETAILS_T Type

The information required to renew a certificate for a roverNode.

Syntax
```

```

Fields

Field Description

`csr`

(required) The certificate signing request (in PEM format), max size 10240.

`time_cert_validity_end`

(required) Time when the renewed certificate's validity will end.

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_REPLACE_CERTIFICATE_AUTHORITY_DETAILS_T Type

The information required to replace a certificate authority details for a roverNode.

Syntax
```

```

Fields

Field Description

`certificate_authority_id`

(required) The certificate authority id.

`cert_key_algorithm`

(optional) key algorithm for issuing leaf certificate.

Allowed values are: 'RSA2048', 'RSA4096', 'ECDSA_P256', 'ECDSA_P384'

`cert_signature_algorithm`

(optional) signature algorithm for issuing leaf certificate.

Allowed values are: 'SHA256_WITH_RSA', 'SHA384_WITH_RSA', 'SHA512_WITH_RSA', 'SHA256_WITH_ECDSA', 'SHA384_WITH_ECDSA', 'SHA512_WITH_ECDSA'

### DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SET_KEY_T Type

Information about the success of setting a rover node's resource principal public key.

Syntax
```

```

Fields

Field Description

`is_successful`

(required) Whether the node's resource principal public key was set correctly

### DBMS_CLOUD_OCI_ROVER_SHAPE_SUMMARY_T Type

A shape of a node on a Rover device.

Syntax
```

```

Fields

Field Description

`gpu_description`

(optional) A short description of the graphics processing unit (GPU) available for this shape.

`gpus`

(optional) The number of GPUs available for this shape.

`memory_in_g_bs`

(optional) The default amount of memory available for this shape, in gigabytes.

`networking_bandwidth_in_gbps`

(optional) The networking bandwidth available for this shape, in gigabits per second.

`ocpus`

(optional) The default number of OCPUs available for this shape.

`processor_description`

(optional) A short description of the shape's processor (CPU).

`shape`

(required) The name of the shape.

`usb_controller_description`

(optional) A short description of the USB controller available for this shape.

`number_of_usb_controllers`

(optional) The number of USB controllers available for this shape.

`tags`

(optional) The tags associated with tagSlug.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_SHAPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_shape_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_SHAPE_COLLECTION_T Type

Results of a listShape search. Contains both Shape items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of shapeSummary objects.

### DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_CLUSTER_DETAILS_T Type

The information required to update a RoverCluster.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`cluster_size`

(optional) Number of nodes desired in the cluster, in standalone clusters, between 5 and 15 inclusive. In station clusters, between 15 and 30 inclusive.

`customer_shipping_address`

(optional)

`cluster_workloads`

(optional) List of existing workloads that should be provisioned on the nodes.

`super_user_password`

(optional) Root password for the rover cluster.

`lifecycle_state`

(optional) The current state of the RoverCluster.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`unlock_passphrase`

(optional) Password to unlock the rover cluster.

`enclosure_type`

(optional) The type of enclosure rover nodes in this cluster are shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped Rover Cluster.

`subscription_id`

(optional) ID provided to customer after successful subscription to Rover Stations.

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the device if they chose customer pickup.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover cluster return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover cluster return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover cluster return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_ENTITLEMENT_DETAILS_T Type

Information required to update a RoverEntitlement.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`tenant_id`

(optional) tenant Id.

`requestor_name`

(optional) Requestor name for the entitlement.

`requestor_email`

(optional) Requestor email for the entitlement.

`entitlement_details`

(optional) Details about the entitlement.

`lifecycle_state`

(optional) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_NODE_DETAILS_T Type

The information required to update a RoverNode.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`shape`

(optional) The shape of workloads in the node.

`serial_number`

(optional) Serial number of the node.

`customer_shipping_address`

(optional)

`node_workloads`

(optional) List of existing workloads that should be provisioned on the node.

`super_user_password`

(optional) Root password for the rover node.

`unlock_passphrase`

(optional) Password to unlock the rover node.

`point_of_contact`

(optional) Name of point of contact for this order if customer is picking up.

`point_of_contact_phone_number`

(optional) Phone number of point of contact for this order if customer is picking up.

`oracle_shipping_tracking_url`

(optional) Tracking Url for the shipped FmsRoverNode.

`shipping_preference`

(optional) Preference for device delivery.

Allowed values are: 'ORACLE_SHIPPED', 'CUSTOMER_PICKUP'

`shipping_vendor`

(optional) Shipping vendor of choice for orace to customer shipping.

`time_pickup_expected`

(optional) Expected date when customer wants to pickup the device if they chose customer pickup.

`lifecycle_state`

(optional) The current state of the RoverNode.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`enclosure_type`

(optional) The type of enclosure rover nodes in this cluster are shipped in.

Allowed values are: 'RUGGADIZED', 'NON_RUGGADIZED'

`lifecycle_state_details`

(optional) A property that can contain details on the lifecycle.

`time_return_window_starts`

(optional) Start time for the window to pickup the device from customer.

`time_return_window_ends`

(optional) End time for the window to pickup the device from customer.

`is_import_requested`

(optional) The flag indicating that customer requests data to be imported to OCI upon Rover node return.

`import_compartment_id`

(optional) An OCID of a compartment where data will be imported to upon Rover node return.

`import_file_bucket`

(optional) Name of a bucket where files from NFS share will be imported to upon Rover node return.

`data_validation_code`

(optional) Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.

`public_key`

(optional) The public key of the resource principal

`certificate_authority_id`

(optional) The certificateAuthorityId of subordinate/intermediate certificate authority.

`time_cert_validity_end`

(optional) The time after which leaf certificate will invalid.

`common_name`

(optional) The common name for the leaf certificate.

`cert_compartment_id`

(optional) The compartmentId of the leaf certificate.

`cert_key_algorithm`

(optional) key algorithm for issuing leaf certificate.

Allowed values are: 'RSA2048', 'RSA4096', 'ECDSA_P256', 'ECDSA_P384'

`cert_signature_algorithm`

(optional) signature algorithm for issuing leaf certificate.

Allowed values are: 'SHA256_WITH_RSA', 'SHA384_WITH_RSA', 'SHA512_WITH_RSA', 'SHA256_WITH_ECDSA', 'SHA384_WITH_ECDSA', 'SHA512_WITH_ECDSA'

`freeform_tags`

(optional) The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'IN_PROGRESS', 'FAILED', 'CREATED', 'UPDATED'

`identifier`

(required) The unique identifier (OCID) of the resource that the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

`metadata`

(optional) Additional information that helps to explain the resource.

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_rover_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_T Type

A description of workRequest status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'ADD_NODES'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`status_details`

(optional) The fine-grained sub-state of a work request.

`id`

(required) The unique identifier (OCID) of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_SUMMARY_T Type

A summary of the work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'ADD_NODES'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'NEEDS_ATTENTION', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`status_details`

(optional) The fine-grained sub-state of a work request.

`id`

(required) The unique identifier (OCID) of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

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

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_rover_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_COLLECTION_T Type

Results of a workRequest search. Contains both workRequest items and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequests.

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occurred. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_rover_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_COLLECTION_T Type

Collection of work request errors.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request errors.

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_TBL Type

Nested table type of dbms_cloud_oci_rover_work_request_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_COLLECTION_T Type

Collection of work request logs.

Syntax
```

```

Fields

Field Description

`items`

(required) Work request logs.

- [Roving Edge Infrastructure Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-C1E8971C-7239-4BF3-9536-91E922384295)
- [DBMS_CLOUD_OCI_ROVER_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-152FDF96-6D08-40DB-9C2A-292388A79D32)
- [DBMS_CLOUD_OCI_ROVER_CA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-E0E79A6A-820D-4F18-9609-D289AF97F62E)
- [DBMS_CLOUD_OCI_ROVER_CA_BUNDLE_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-FEFD7E87-0649-4AD6-AED2-63ACDDDB6C16)
- [DBMS_CLOUD_OCI_ROVER_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-57D3E478-0689-4B7D-9D9C-B259E9D6EBCB)
- [DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_CLUSTER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-0F13E9B9-B39A-429B-BA87-7945B944CD13)
- [DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_ENTITLEMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-597D78A9-7232-4530-8EFD-3718877E16BD)
- [DBMS_CLOUD_OCI_ROVER_CHANGE_ROVER_NODE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-5701B406-8B3C-4A5B-8965-09F87D1CF52C)
- [DBMS_CLOUD_OCI_ROVER_SHIPPING_ADDRESS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-F306E62E-8EA6-4D79-9903-F7FD67454C4B)
- [DBMS_CLOUD_OCI_ROVER_ROVER_WORKLOAD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-FEF23E07-12AF-4203-8F00-9DBEB19201DC)
- [DBMS_CLOUD_OCI_ROVER_ROVER_WORKLOAD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-18828755-C6F1-4AF8-976D-90EF5DFB94FA)
- [DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-64DE4AB2-C6FB-4AFD-A316-0CF3E8B05D1C)
- [DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_ENTITLEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-59343526-1E18-4255-AABF-38B0CF16E551)
- [DBMS_CLOUD_OCI_ROVER_CREATE_ROVER_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-DCBF9446-5EC7-40DA-8683-11607E5F3A5E)
- [DBMS_CLOUD_OCI_ROVER_CURRENT_ROVER_BUNDLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-AC7F27ED-C0EB-45B0-827A-9BD6463E4F18)
- [DBMS_CLOUD_OCI_ROVER_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-82FBF3CB-F24B-4393-9FDE-D5B79BE11DEA)
- [DBMS_CLOUD_OCI_ROVER_GENERATE_CERTIFICATE_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-92C46AB8-EC94-468E-AC6C-CA28569E36F6)
- [DBMS_CLOUD_OCI_ROVER_LEAF_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-5F6B7F79-A09A-497E-8DB1-BE31B9611C48)
- [DBMS_CLOUD_OCI_ROVER_LEAF_CERTIFICATE_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-1DDC47C1-ADCC-4F40-94FE-CBD484F174C2)
- [DBMS_CLOUD_OCI_ROVER_RENEW_CERTIFICATE_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-A077CED6-9E03-4D81-A2A4-EFC0D7AE0B97)
- [DBMS_CLOUD_OCI_ROVER_REPLACE_CA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-215427F2-7F00-4760-8329-1343E93865BA)
- [DBMS_CLOUD_OCI_ROVER_REPLACE_CERTIFICATE_AUTHORITY_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-81AE232F-AF02-4D01-BBB7-53FEAB0D3CB4)
- [DBMS_CLOUD_OCI_ROVER_REQUEST_ADDITIONAL_NODES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-B401BAA2-41CF-4ACB-B49D-041D239864CB)
- [DBMS_CLOUD_OCI_ROVER_REQUEST_ROVER_BUNDLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-6018AB60-6CCB-4A40-A274-ADD15E4FC657)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-379C6D79-7E52-4A53-AE0B-F6DEFC0A9DF4)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-795421C0-37B4-49FE-9A88-6A84456BBC4E)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-30AE5649-FD50-42C7-81E6-6A0A8653809C)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-472621CD-202B-4C99-84BB-73BB81E4C2F0)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-2772C1DE-798F-4BF8-B64E-6BB65B9FBD69)
- [DBMS_CLOUD_OCI_ROVER_ROVER_BUNDLE_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-6D6A1376-4AA8-45E5-84F9-25DC27CFBB73)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-B8E54C92-BAE2-41BC-BE6B-C425C83DF96A)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-11CF0AC3-F920-4511-8475-A787843BAEB1)
- [DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-43E6ACE4-418A-4968-B05A-3C2E18FDB66D)
- [DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-5041BF63-4FC6-418F-976B-265E47926591)
- [DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-E25AB3FB-3728-4A73-9928-AC661D388E6C)
- [DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-36FAF97A-EA78-48BC-A0EB-81AEB475EC89)
- [DBMS_CLOUD_OCI_ROVER_ROVER_CLUSTER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-53048EE1-41C6-4EFD-B663-BF26FDFB90C7)
- [DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-A0E3F74C-DA18-4540-AEC1-888506DCE573)
- [DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-4BAC4874-ED97-4643-9D87-B5C086346ADC)
- [DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-DFC6563A-5639-41C8-8A61-49DF0065676D)
- [DBMS_CLOUD_OCI_ROVER_ROVER_ENTITLEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-D0A71363-0AEE-498A-AA09-F6B743721160)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-FEBC4E86-A09C-48E1-AD39-813E1F8B9993)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_ACTION_SET_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-DCC47533-856C-4DBF-A0A9-888E8256FAA3)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-6E1C2162-9E38-4EC8-9B24-704D41119D0B)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-9320EBBF-60AF-4753-9F5E-7D068C30603F)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_ENCRYPTION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-875EBEA9-E866-45CA-9D96-CCC6F0296C5E)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_GENERATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-FA0FBED0-C6C8-4820-BB30-FE1174777AAE)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_GET_RPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-579B4B56-9718-4283-B0FB-C53C127EDFEA)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_RENEW_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-421D2C35-79B4-4E22-B80A-74E467DB5573)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_REPLACE_CERTIFICATE_AUTHORITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-27F886C7-E30F-4A04-9B2B-B21A20040C24)
- [DBMS_CLOUD_OCI_ROVER_ROVER_NODE_SET_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-975DCA24-4468-46FB-9D5D-9819E66D1F77)
- [DBMS_CLOUD_OCI_ROVER_SHAPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-BBF6D365-F121-42FB-B79A-DEB90E4CFCEC)
- [DBMS_CLOUD_OCI_ROVER_SHAPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-F0EEF320-622D-41C7-8AB7-4849C033213C)
- [DBMS_CLOUD_OCI_ROVER_SHAPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-D39F16BC-E5AC-44E3-A3D3-06F38204D574)
- [DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_CLUSTER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-3D0D5685-798C-414A-8E56-5F527D3A4930)
- [DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_ENTITLEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-EBED4F87-92AD-4FDA-84F2-F30DFC4ED355)
- [DBMS_CLOUD_OCI_ROVER_UPDATE_ROVER_NODE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-B055810C-63F0-4156-923B-A0C64D77CE80)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-D9B08B14-2F0B-4F21-AFBD-291125E7EB53)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-25313209-2981-41BF-92DE-FA8400C87586)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-DF7887EB-1F55-4957-BEA6-643660012A90)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-104BC287-4208-463B-A249-5632CD2198BB)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-BE5881D2-4885-44B2-A766-B9CDE735A1E0)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-D9DAC4DA-B359-48C6-900C-B3056983EDAC)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-04810CB7-CF79-4BA0-93E7-810ADAA6E65B)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-A84B4FE5-2B8A-472B-A506-78DB746A02DF)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-181ADB1C-1F4F-4434-8FFB-F82DF21D0615)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-83DC7436-2182-4BF4-A0BD-7AE3E387E368)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-50E6DA12-9D3E-4221-A565-82AC596F2559)
- [DBMS_CLOUD_OCI_ROVER_WORK_REQUEST_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/rover_t.html#ADSDK-GUID-F8BE8BA1-D4F8-461F-A056-B5F3CFDF81AE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
