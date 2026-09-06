# Tenant Manager Control Plane Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#dcoc-content-body)

## Tenant Manager Control Plane Common Types

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ACTIVATE_ORDER_DETAILS_T Type

The parameters for activating an order subscription in a tenancy.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Tenant ID to activate the order.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_T Type

Assigned subscription type, which carries shared properties for any assigned subscription version.

Syntax
```

```

Fields

Field Description

`entity_version`

(required) The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).

Allowed values are: 'V1', 'V2'

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the subscription.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the owning compartment. Always a tenancy OCID.

`service_name`

(required) The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.

`time_created`

(required) The date and time of creation, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) The date and time of update, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type

Assigned subscription summary type, which carries shared properties for any assigned subscription summary version.

Syntax
```

```

Fields

Field Description

`entity_version`

(required) The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).

Allowed values are: 'V1', 'V2'

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the subscription.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the owning compartment. Always a tenancy OCID.

`service_name`

(required) The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.

`time_created`

(required) The date and time of creation, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) The date and time of update, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_COLLECTION_T Type

Collection of assigned subscription summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing assigned subscription summary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_SUMMARY_T Type

Summary of the line item in an assigned subscription.

Syntax
```

```

Fields

Field Description

`id`

(required) Subscription line item identifier.

`product_code`

(required) Product code.

`quantity`

(required) Product number.

`billing_model`

(required) Billing model supported by the associated line item.

Allowed values are: 'COMMITMENT', 'PAYGO', 'PROMOTION'

`time_started`

(required) The time the subscription item and associated products should start. An RFC 3339 formatted date and time string.

`time_ended`

(required) The time the subscription item and associated products should end. An RFC 3339 formatted date and time string.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_line_item_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_COLLECTION_T Type

Collection of line item summaries in an assigned subscription.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing line item summaries in an assigned subscription.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_SUMMARY_T Type

The summary of region availability for a subscription.

Syntax
```

```

Fields

Field Description

`region_name`

(required) Region availability for the subscription.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_available_region_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_COLLECTION_T Type

List of available regions.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing available region items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SKU_T Type

SKU information.

Syntax
```

```

Fields

Field Description

`sku`

(required) Stock Keeping Unit (SKU) ID.

`quantity`

(optional) Quantity of the stock units.

`description`

(optional) Description of the stock units.

`gsi_order_line_id`

(optional) Sales order line identifier.

`license_part_description`

(optional) Description of the covered product belonging to this SKU.

`metric_name`

(optional) Base metric for billing the service.

`is_base_service_component`

(optional) Specifies if the SKU is considered as a parent or child.

`is_additional_instance`

(optional) Specifies if an additional test instance can be provisioned by the SaaS application.

`start_date`

(optional) Date and time when the SKU was created.

`end_date`

(optional) Date and time when the SKU ended.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_PROMOTION_T Type

Promotion information for a subscription.

Syntax
```

```

Fields

Field Description

`duration`

(optional) Specifies how long the promotion related to the subscription, if any, is valid in duration units.

`duration_unit`

(optional) Unit for the duration.

`amount`

(optional) If a subscription is present, indicates the total amount of promotional subscription credits.

`status`

(optional) If a subscription is present, indicates the current status of the subscription promotion.

Allowed values are: 'INITIALIZED', 'ACTIVE', 'EXPIRED'

`is_intent_to_pay`

(optional) Speficies whether or not the customer intends to pay after the promotion has expired.

`currency_unit`

(optional) Currency unit associated with the promotion.

`time_started`

(optional) Date and time when the promotion starts.

`time_expired`

(optional) Date and time when the promotion ends.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SKU_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_subscription_sku_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_PROMOTION_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_promotion_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_ASSIGNED_SUBSCRIPTION_T Type

Assigned subscription information.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_classic_assigned_subscription_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_t`type.

Fields

Field Description

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`classic_subscription_id`

(required) Subscription ID.

`is_classic_subscription`

(optional) Specifies whether or not the subscription is legacy.

`region_assignment`

(optional) Region for the subscription.

`skus`

(optional) List of SKUs linked to the subscription.

`order_ids`

(optional) List of subscription order OCIDs that contributed to this subscription.

`program_type`

(optional) Specifies any program that is associated with the subscription.

`customer_country_code`

(optional) The country code for the customer associated with the subscription.

`cloud_amount_currency`

(optional) The currency code for the customer associated with the subscription.

`csi_number`

(optional) Customer service identifier for the customer associated with the subscription.

`subscription_tier`

(optional) Tier for the subscription, whether a free promotion subscription or a paid subscription.

`is_government_subscription`

(optional) Specifies whether or not the subscription is a government subscription.

`promotion`

(optional) List of promotions related to the subscription.

`purchase_entitlement_id`

(optional) Purchase entitlement ID associated with the subscription.

`start_date`

(optional) Subscription start time.

`end_date`

(optional) Subscription end time.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type

Summary of assigned subscription information.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_classic_assigned_subscription_summary_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_summary_t`type.

Fields

Field Description

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`classic_subscription_id`

(required) Subscription ID.

`is_classic_subscription`

(optional) Specifies whether or not the subscription is legacy.

`region_assignment`

(optional) Region for the subscription.

`start_date`

(optional) Subscription start time.

`end_date`

(optional) Subscription end time.

`csi_number`

(optional) Customer service identifier for the customer associated with the subscription.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_T Type

Base subscription type, which carries shared properties for any subscription version.

Syntax
```

```

Fields

Field Description

`entity_version`

(required) The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).

Allowed values are: 'V1', 'V2'

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the subscription.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the owning compartment. Always a tenancy OCID.

`service_name`

(required) The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.

`time_created`

(required) The date and time of creation, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) The date and time of update, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_SUBSCRIPTION_T Type

Subscription information for the compartmentId. Only root compartments are allowed.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_classic_subscription_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_subscription_t`type.

Fields

Field Description

`classic_subscription_id`

(required) Classic subscription ID.

`is_classic_subscription`

(optional) Specifies whether or not the subscription is from classic systems.

`payment_model`

(optional) The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.

`region_assignment`

(optional) Region for the subscription.

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`skus`

(optional) List of SKUs linked to this subscription.

`program_type`

(optional) Specifies any program that is associated with the subscription.

`customer_country_code`

(optional) The country code for the customer associated with the subscription.

`cloud_amount_currency`

(optional) The currency code for the customer associated with the subscription.

`csi_number`

(optional) Customer service identifier for the customer associated with the subscription.

`subscription_tier`

(optional) Tier for the subscription, whether a free promotion subscription or a paid subscription.

`is_government_subscription`

(optional) Specifies whether or not the subscription is a government subscription.

`promotion`

(optional) List of promotions related to the subscription.

`purchase_entitlement_id`

(optional) Purchase entitlement ID associated with the subscription.

`start_date`

(optional) Subscription start time.

`end_date`

(optional) Subscription end time.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SUMMARY_T Type

Base subscription summary type, which carries shared properties for any subscription summary version.

Syntax
```

```

Fields

Field Description

`entity_version`

(required) The entity version of the subscription, whether V1 (the legacy schema version), or V2 (the latest 20230401 API version).

Allowed values are: 'V1', 'V2'

`id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the subscription.

`compartment_id`

(required) The Oracle ID ([OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the owning compartment. Always a tenancy OCID.

`service_name`

(required) The type of subscription, such as 'UCM', 'SAAS', 'ERP', 'CRM'.

`time_created`

(required) The date and time of creation, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) The date and time of update, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_SUBSCRIPTION_SUMMARY_T Type

Summary of subscription.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_classic_subscription_summary_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_subscription_summary_t`type.

Fields

Field Description

`classic_subscription_id`

(required) Classic subscription ID.

`is_classic_subscription`

(optional) Specifies whether or not the subscription is from classic systems.

`payment_model`

(optional) The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.

`region_assignment`

(optional) Region for the subscription.

`lifecycle_state`

(optional) Lifecycle state of the subscription.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`start_date`

(optional) Subscription start time.

`end_date`

(optional) Subscription end time.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_ASSIGNED_SUBSCRIPTION_T Type

Assigned subscription information.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_cloud_assigned_subscription_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_t`type.

Fields

Field Description

`subscription_number`

(required) Unique Oracle Cloud Subscriptions identifier that is immutable on creation.

`currency_code`

(required) Currency code. For example USD, MXN.

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'NEEDS_ATTENTION', 'ACTIVE', 'INACTIVE', 'FAILED', 'CREATING'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type

Summary of assigned subscription information.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_cloud_assigned_subscription_summary_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_assigned_subscription_summary_t`type.

Fields

Field Description

`subscription_number`

(required) Unique Oracle Cloud Subscriptions identifier that is immutable on creation.

`currency_code`

(required) Currency code. For example USD, MXN.

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'NEEDS_ATTENTION', 'ACTIVE', 'INACTIVE', 'FAILED', 'CREATING'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_SUBSCRIPTION_T Type

Subscription information for compartment ID. Only root compartments are allowed.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_cloud_subscription_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_subscription_t`type.

Fields

Field Description

`subscription_number`

(required) Unique Oracle Cloud Subscriptions identifier that is immutable on creation.

`currency_code`

(required) Currency code. For example USD, MXN.

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'NEEDS_ATTENTION', 'ACTIVE', 'INACTIVE', 'FAILED', 'CREATING'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_SUBSCRIPTION_SUMMARY_T Type

Summary of subscription.

Syntax
```

```

`dbms_cloud_oci_tenant_manager_control_plane_cloud_subscription_summary_t`is a subtype of the`dbms_cloud_oci_tenant_manager_control_plane_subscription_summary_t`type.

Fields

Field Description

`subscription_number`

(required) Unique Oracle Cloud Subscriptions identifier that is immutable on creation.

`currency_code`

(required) Currency code. For example USD, MXN.

`lifecycle_state`

(required) Lifecycle state of the subscription.

Allowed values are: 'NEEDS_ATTENTION', 'ACTIVE', 'INACTIVE', 'FAILED', 'CREATING'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_CHILD_TENANCY_DETAILS_T Type

The parameters for creating a child tenancy.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The tenancy ID of the parent tenancy.

`tenancy_name`

(required) The tenancy name to use for the child tenancy.

`home_region`

(required) The home region to use for the child tenancy. This must be a region where the parent tenancy is subscribed.

`admin_email`

(required) Email address of the child tenancy administrator.

`policy_name`

(optional) The name to use for the administrator policy in the child tenancy. Must contain only letters and underscores.

`governance_status`

(optional) The governance status of the child tenancy.

Allowed values are: 'OPTED_IN', 'OPTED_OUT'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_DOMAIN_DETAILS_T Type

The parameters for creating a domain.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the tenancy.

`domain_name`

(required) The domain name.

`subscription_email`

(optional) Email address to be used to notify the user, and that the ONS subscription will be created with.

`is_governance_enabled`

(optional) Indicates whether governance should be enabled for this domain. Defaults to false.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_DOMAIN_GOVERNANCE_DETAILS_T Type

The parameters for creating a domain governance entity.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the tenancy.

`domain_id`

(required) OCID of the domain.

`subscription_email`

(required) Email address to be used to notify the user, and that the ONS subscription will be created with.

`ons_topic_id`

(required) The ONS topic associated with this domain governance entity.

`ons_subscription_id`

(required) The ONS subscription associated with this domain governance entity.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_SENDER_INVITATION_DETAILS_T Type

The parameters for creating a sender invitation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the sender tenancy.

`recipient_tenancy_id`

(required) OCID of the recipient tenancy.

`recipient_email_address`

(optional) Email address of the recipient.

`display_name`

(optional) A user-created name to describe the invitation. Avoid entering confidential information.

`subjects`

(optional) The list of subjects this invitation contains.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_SUBSCRIPTION_MAPPING_DETAILS_T Type

CreateSubscriptionMappingDetails contains subscription and compartment identified by the tenancy, and OCID information.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment. Always a tenancy OCID.

`subscription_id`

(required) OCID of Subscription.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_T Type

The domain model that is associated with a tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the domain.

`domain_name`

(required) The domain name.

`owner_id`

(required) The OCID of the tenancy that has started the registration process for this domain.

`lifecycle_state`

(required) Lifecycle state of the domain.

Allowed values are: 'ACTIVE', 'DELETED', 'FAILED'

`status`

(required) Status of the domain.

Allowed values are: 'PENDING', 'RELEASING', 'RELEASED', 'EXPIRING', 'REVOKING', 'REVOKED', 'ACTIVE', 'FAILED'

`txt_record`

(required) The code that the owner of the domain will need to add as a TXT record to their domain.

`time_created`

(optional) Date-time when this domain was created. An RFC 3339-formatted date and time string.

`time_updated`

(optional) Date-time when this domain was last updated. An RFC 3339-formatted date and time string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_SUMMARY_T Type

The summary of a domain owned by a tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the domain.

`domain_name`

(required) The domain name.

`owner_id`

(required) The OCID of the tenancy that has started the registration process for this domain.

`lifecycle_state`

(required) The lifecycle state of the domain.

`status`

(required) Status of the domain.

`txt_record`

(required) The code that the owner of the domain will need to add as a TXT record to their domain.

`time_created`

(optional) Date-time when this domain was created. An RFC 3339-formatted date and time string.

`time_updated`

(optional) Date-time when this domain was last updated. An RFC 3339-formatted date and time string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_domain_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_COLLECTION_T Type

Result of a query request for a list of domains. Contains DomainSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing DomainSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_T Type

The model for a domain governance entity.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the domain governance entity.

`owner_id`

(required) The OCID of the tenancy that owns this domain governance entity.

`domain_id`

(required) The OCID of the domain associated with this domain governance entity.

`lifecycle_state`

(required) Lifecycle state of the domain governance entity.

Allowed values are: 'ACTIVE', 'INACTIVE'

`is_governance_enabled`

(optional) Indicates whether governance is enabled for this domain.

`subscription_email`

(optional) Email address to be used to notify the user, and that the ONS subscription will be created with.

`ons_topic_id`

(required) The ONS topic associated with this domain governance entity.

`ons_subscription_id`

(required) The ONS subscription associated with this domain governance entity.

`time_created`

(optional) Date-time when this domain governance was created. An RFC 3339-formatted date and time string.

`time_updated`

(optional) Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_SUMMARY_T Type

The summary of a domain govenance entity owned by a tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the domain governance entity.

`owner_id`

(required) The OCID of the tenancy that owns this domain governance entity.

`domain_id`

(required) The OCID of the domain associated with this domain governance entity.

`lifecycle_state`

(required) The lifecycle state of the domain governance entity.

`is_governance_enabled`

(required) Indicates whether governance is enabled for this domain.

`subscription_email`

(optional) Email address to be used to notify the user, and that the ONS subscription will be created with.

`ons_topic_id`

(required) The ONS topic associated with this domain governance entity.

`ons_subscription_id`

(required) The ONS subscription associated with this domain governance entity.

`time_created`

(optional) Date-time when this domain governance was created. An RFC 3339-formatted date and time string.

`time_updated`

(optional) Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_domain_governance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_COLLECTION_T Type

Result of a query request for a list of domain governance entities. Contains DomainGovernanceSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing DomainGovernanceSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_T Type

A link between a parent tenancy and a child tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the link.

`parent_tenancy_id`

(required) OCID of the parent tenancy.

`child_tenancy_id`

(required) OCID of the child tenancy.

`lifecycle_state`

(optional) Lifecycle state of the link.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`time_created`

(required) Date-time when this link was created.

`time_updated`

(optional) Date-time when this link was last updated.

`time_terminated`

(optional) Date-time when this link was terminated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_SUMMARY_T Type

The summary of a link between a parent tenancy and a child tenancy.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the link.

`parent_tenancy_id`

(required) OCID of the parent tenancy.

`child_tenancy_id`

(required) OCID of the child tenancy.

`lifecycle_state`

(optional) Lifecycle state of the link.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`time_created`

(required) Date-time when this link was created

`time_updated`

(optional) Date-time when this link was last updated.

`time_terminated`

(optional) Date-time when this link was terminated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_link_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_COLLECTION_T Type

Result of a query request for a list of links. Contains Link items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing LinkSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SKU_T Type

A single subscription SKU.

Syntax
```

```

Fields

Field Description

`l_number`

(optional) SKU number.

`name`

(optional) SKU name.

`quantity`

(optional) SKU quantity.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SKU_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_sku_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_INFO_T Type

A single subscription's details.

Syntax
```

```

Fields

Field Description

`spm_subscription_id`

(required) Subscription ID.

`service`

(required) Subscription service name.

`start_date`

(required) Subscription start date. An RFC 3339-formatted date and time string.

`end_date`

(required) Subscription end date. An RFC 3339-formatted date and time string.

`skus`

(required) List of SKUs the subscription contains.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_INFO_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_subscription_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORDER_T Type

Order details.

Syntax
```

```

Fields

Field Description

`order_number`

(required) Immutable and unique order number holding customer subscription information.

`data_center_region`

(optional) Order's data center region.

`admin_email`

(required) Email address of the administrator who owns the subscription.

`order_state`

(required) State of the order.

`subscriptions`

(required) Array of subscriptions associated with the order.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_T Type

An organization entity.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the organization.

`display_name`

(optional) A display name for the organization. Avoid entering confidential information.

`compartment_id`

(required) OCID of the compartment containing the organization. Always a tenancy OCID.

`parent_name`

(optional) The name of the tenancy that is the organization parent.

`default_ucm_subscription_id`

(required) OCID of the default Universal Credits Model subscription. Any tenancy joining the organization will automatically get assigned this subscription, if a subscription is not explictly assigned.

`lifecycle_state`

(required) Lifecycle state of the organization.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) Date and time when the organization was created.

`time_updated`

(optional) Date and time when the organization was last updated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_SUMMARY_T Type

An organization entity.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the organization.

`display_name`

(optional) A display name for the organization. Avoid entering confidential information.

`compartment_id`

(required) OCID of the compartment containing the organization. Always a tenancy OCID.

`parent_name`

(optional) The name of the tenancy that is the organization parent.

`default_ucm_subscription_id`

(required) OCID of the default Universal Credits Model subscription. Any tenancy joining the organization will automatically get assigned this subscription, if a subscription is not explictly assigned.

`lifecycle_state`

(required) Lifecycle state of the organization.

`time_created`

(required) Date and time when the organization was created.

`time_updated`

(optional) Date and time when the organization was last updated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_organization_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_COLLECTION_T Type

Result of a query request for a list of organizations. Contains OrganizationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing OrganizationSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_T Type

The information about the organization tenancy.

Syntax
```

```

Fields

Field Description

`tenancy_id`

(required) OCID of the tenancy.

`name`

(optional) Name of the tenancy.

`lifecycle_state`

(optional) Lifecycle state of the organization tenancy.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETED', 'FAILED', 'DELETING'

`role`

(optional) Role of the organization tenancy.

Allowed values are: 'PARENT', 'CHILD', 'NONE'

`time_joined`

(optional) Date and time when the tenancy joined the organization.

`time_left`

(optional) Date and time when the tenancy left the organization.

`is_approved_for_transfer`

(optional) Parameter to indicate the tenancy is approved for transfer to another organization.

`governance_status`

(required) The governance status of the tenancy.

Allowed values are: 'OPTED_IN', 'OPTED_OUT'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_SUMMARY_T Type

An organization tenancy summary entity.

Syntax
```

```

Fields

Field Description

`tenancy_id`

(required) OCID of the tenancy.

`name`

(optional) Name of the tenancy.

`lifecycle_state`

(optional) Lifecycle state of the organization tenancy.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETED', 'FAILED', 'DELETING'

`role`

(optional) Role of the organization tenancy.

Allowed values are: 'PARENT', 'CHILD', 'NONE'

`time_joined`

(optional) Date and time when the tenancy joined the organization.

`time_left`

(optional) Date and time when the tenancy left the organization.

`is_approved_for_transfer`

(optional) Parameter to indicate the tenancy is approved for transfer to another organization.

`governance_status`

(required) The governance status of the tenancy.

Allowed values are: 'OPTED_IN', 'OPTED_OUT'

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_organization_tenancy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_COLLECTION_T Type

Result of a query request for a list of organization tenancies. Contains OrganizationTenancySummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing OrganizationTenancySummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_T Type

The invitation model that the recipient owns.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the recipient invitation.

`compartment_id`

(required) OCID of the recipient tenancy.

`subjects`

(required) The list of subjects the invitation contains.

`sender_invitation_id`

(required) OCID of the corresponding sender invitation.

`sender_tenancy_id`

(required) OCID of the sender tenancy.

`lifecycle_state`

(required) Lifecycle state of the recipient invitation.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(required) Status of the recipient invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'IGNORED', 'EXPIRED', 'FAILED'

`display_name`

(optional) A user-created name to describe the invitation. Avoid entering confidential information.

`time_created`

(required) Date and time when the recipient invitation was created.

`time_updated`

(optional) Date and time when the recipient invitation was last updated.

`recipient_email_address`

(optional) Email address of the recipient.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_SUMMARY_T Type

The summary of the invitation model that the recipient owns.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the recipient invitation.

`compartment_id`

(required) OCID of the recipient tenancy.

`display_name`

(required) A user-created name to describe the invitation. Avoid entering confidential information.

`subjects`

(required) The list of subjects the invitation contains.

`sender_invitation_id`

(required) OCID of the corresponding sender invitation.

`sender_tenancy_id`

(required) OCID of the sender tenancy.

`lifecycle_state`

(required) Lifecycle state of the recipient invitation.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(required) Status of the recipient invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'IGNORED', 'EXPIRED', 'FAILED'

`time_created`

(required) Date and time when the recipient invitation was created.

`time_updated`

(optional) Date and time when the recipient invitation was last updated.

`recipient_email_address`

(optional) Email address of the recipient.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_recipient_invitation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_COLLECTION_T Type

Result of a query request for a list of recipient invitations. Contains RecipientInvitationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing RecipientInvitationSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_REVIVE_WORKFLOW_INSTANCE_DETAILS_T Type

The parameters for reviving failed workflow

Syntax
```

```

Fields

Field Description

`workflow_instance_id`

(optional) Id of failed workflow

`workflow_instance_name`

(optional) Service specific workflow instance name

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_T Type

The invitation model that the sender owns.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the sender invitation.

`compartment_id`

(required) OCID of the sender tenancy.

`subjects`

(required) The list of subjects the invitation contains.

`recipient_invitation_id`

(optional) OCID of the corresponding recipient invitation.

`recipient_tenancy_id`

(required) OCID of the recipient tenancy.

`lifecycle_state`

(required) Lifecycle state of the sender invitation.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(required) Status of the sender invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'EXPIRED', 'FAILED'

`display_name`

(optional) A user-created name to describe the invitation. Avoid entering confidential information.

`time_created`

(required) Date and time when the sender invitation was created.

`time_updated`

(optional) Date and time when the sender invitation was last updated.

`recipient_email_address`

(optional) Email address of the recipient.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_SUMMARY_T Type

The summary of the invitation model that the sender owns.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the sender invitation.

`compartment_id`

(required) OCID of the sender tenancy.

`display_name`

(required) A user-created name to describe the invitation. Avoid entering confidential information.

`subjects`

(required) The list of subjects the invitation contains.

`recipient_invitation_id`

(optional) OCID of the corresponding recipient invitation.

`recipient_tenancy_id`

(required) OCID of the recipient tenancy.

`lifecycle_state`

(required) Lifecycle state of the sender invitation.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(required) Status of the sender invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'EXPIRED', 'FAILED'

`time_created`

(required) Date and time when the sender invitation was created.

`time_updated`

(optional) Date and time when the sender invitation was last updated.

`recipient_email_address`

(optional) Email address of the recipient.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_sender_invitation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_COLLECTION_T Type

Result of a query request for a list of sender invitations. Contains SenderInvitationSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing SenderInvitationSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_subscription_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_COLLECTION_T Type

List of subscription summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing subscription summary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_SUMMARY_T Type

Summary of line items in a subscription.

Syntax
```

```

Fields

Field Description

`id`

(required) Subscription line item identifier.

`product_code`

(required) Product code.

`quantity`

(required) Product number.

`billing_model`

(required) Billing model supported by the associated line item.

Allowed values are: 'COMMITMENT', 'PAYGO', 'PROMOTION'

`time_started`

(required) The time the subscription item and associated products should start. An RFC 3339 formatted date and time string.

`time_ended`

(required) The time the subscription item and associated products should end. An RFC 3339 formatted date and time string.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_subscription_line_item_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_COLLECTION_T Type

Collection of line item summaries in a subscription.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing line item summaries in a subscription.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_T Type

Subscription mapping information.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the mapping between subscription and compartment identified by the tenancy.

`subscription_id`

(required) OCID of the subscription.

`compartment_id`

(required) OCID of the compartment. Always a tenancy OCID.

`is_explicitly_assigned`

(required) Denotes if the subscription is explicity assigned to the root compartment or tenancy.

`lifecycle_state`

(required) Lifecycle state of the subscriptionMapping.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`time_terminated`

(optional) Date-time when subscription mapping was terminated.

`time_created`

(required) Date-time when subscription mapping was created.

`time_updated`

(required) Date-time when subscription mapping was updated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_SUMMARY_T Type

Subscription mapping information.

Syntax
```

```

Fields

Field Description

`id`

(required) OCID of the mapping between subscription and compartment identified by the tenancy.

`subscription_id`

(required) OCID of the subscription.

`compartment_id`

(required) OCID of the compartment. Always a tenancy OCID.

`is_explicitly_assigned`

(required) Denotes if the subscription is explicity assigned to the root compartment or tenancy.

`lifecycle_state`

(required) Lifecycle state of the subscription mapping.

`time_terminated`

(optional) Date-time when subscription mapping was terminated.

`time_created`

(required) Date-time when subscription mapping was created.

`time_updated`

(required) Date-time when subscription mapping was updated.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_subscription_mapping_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_COLLECTION_T Type

List of subscription mappings.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing subscription mapping items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_DOMAIN_DETAILS_T Type

The parameters for updating a domain.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_DOMAIN_GOVERNANCE_DETAILS_T Type

The parameters for updating a domain govenance entity.

Syntax
```

```

Fields

Field Description

`subscription_email`

(optional) Email address to be used to notify the user, and that the ONS subscription will be created with. The ONS subscription for the previous email will also be deleted.

`is_governance_enabled`

(optional) Indicates whether governance is enabled for this domain.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_ORGANIZATION_DETAILS_T Type

The parameters for updating an organization.

Syntax
```

```

Fields

Field Description

`default_ucm_subscription_id`

(required) OCID of the default Universal Credits Model subscription. Any tenancy joining the organization will automatically get assigned this subscription, if a subscription is not explictly assigned.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_RECIPIENT_INVITATION_DETAILS_T Type

The parameters for updating a recipient invitation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-created name to describe the invitation. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_SENDER_INVITATION_DETAILS_T Type

The parameters for updating a sender invitation.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-created name to describe the invitation. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) Indicates how the resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource, at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path so that the user can do a GET to access the resource metadata.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_T Type

A description of the work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_SENDER_INVITATION', 'ACCEPT_RECIPIENT_INVITATION', 'CANCEL_SENDER_INVITATION', 'COMPLETE_ORDER_ACTIVATION', 'ACTIVATE_ORDER_EXISTING_TENANCY', 'REGISTER_DOMAIN', 'RELEASE_DOMAIN', 'CREATE_CHILD_TENANCY', 'ASSIGN_DEFAULT_SUBSCRIPTION', 'MANUAL_LINK_CREATION', 'TERMINATE_ORGANIZATION_TENANCY', 'UPDATE_SAAS_CAPABILITY', 'SOFT_TERMINATE_TENANCY', 'HARD_TERMINATE_TENANCY', 'RESTORE_TENANCY', 'LOG_TENANCY_TERMINATION_REQUEST', 'SELF_OPT_IN', 'SELF_OPT_OUT'

`status`

(required) Status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources affected by the work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_SUMMARY_T Type

A summary of work request status.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request.

Allowed values are: 'CREATE_SENDER_INVITATION', 'ACCEPT_RECIPIENT_INVITATION', 'CANCEL_SENDER_INVITATION', 'COMPLETE_ORDER_ACTIVATION', 'ACTIVATE_ORDER_EXISTING_TENANCY', 'REGISTER_DOMAIN', 'RELEASE_DOMAIN', 'CREATE_CHILD_TENANCY', 'ASSIGN_DEFAULT_SUBSCRIPTION', 'MANUAL_LINK_CREATION', 'TERMINATE_ORGANIZATION_TENANCY', 'UPDATE_SAAS_CAPABILITY', 'SOFT_TERMINATE_TENANCY', 'HARD_TERMINATE_TENANCY', 'RESTORE_TENANCY', 'LOG_TENANCY_TERMINATION_REQUEST', 'SELF_OPT_IN', 'SELF_OPT_OUT'

`status`

(required) Status of the current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains the work request.

`resources`

(required) The resources affected by the work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_COLLECTION_T Type

Result of a query request for a list of work requests. Contains WorkRequestSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing WorkRequestSummary items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed in[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC 3339 formatted date and time string.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_COLLECTION_T Type

Result of a query request for a list of work request errors. Contains WorkRequestError items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing WorkRequestError items.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC 3339 formatted date and time string.

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_tenant_manager_control_plane_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Result of a query request for a list of work request log entries. Contains WorkRequestLogEntry items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array containing WorkRequestLogEntry items.

- [Tenant Manager Control Plane Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-5F8DAEB1-57E0-4B74-8846-7887AD050791)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A6F459CD-C650-47AD-B4B2-7116E0CB77FC)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ACTIVATE_ORDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A52598FE-98AA-436A-B325-31490148196E)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-796F12E8-70AA-484C-A058-137540144C45)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-C63B88D8-982E-456B-8C79-37AACB58459A)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-424E0195-A295-43E8-8814-EBF07F9B1943)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-41404A3C-B5AB-405D-8731-B9CF441C2710)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-E5F407A7-55E2-43AD-9BB6-E9670D8DEE35)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-5021D506-8E95-4A9E-A85C-C3414B7EB321)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ASSIGNED_SUBSCRIPTION_LINE_ITEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A5B0CFB3-B18A-481C-8017-0CE4721C6067)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-E491512B-1BFB-460F-88F4-0DCCCC948B1A)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-B37930FD-6F1C-4CB3-B946-C0B832E2A377)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_AVAILABLE_REGION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-212763F9-E89C-4DC4-93A6-2A97148D69B1)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SKU_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-081AEEC6-75DF-4240-AC05-DA50B1D54C4D)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_PROMOTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A3431F5B-839F-4AAD-82E4-0E7E0099176E)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SKU_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-DCFA7E06-4408-4745-BE87-C7AFFBB2FB7C)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_PROMOTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9E673F2A-F308-4AF1-B0A3-50A3E158E5D5)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_ASSIGNED_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-C307403B-631E-41DC-B5F8-474704642563)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-F7900073-BCF6-4D0E-9766-997A2A0C5E37)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9BE7985F-9798-40AF-BB73-5CA912571C08)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-989A2B13-8F51-4E14-93DA-DCA12DF0AB4E)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-0892FCD1-7F1E-4C8F-AC1C-D3EFD57B49A0)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLASSIC_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-63F3BBE3-2AB5-43CC-A44F-58AF79FE8F22)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_ASSIGNED_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-C80F911A-4605-42A3-9B72-FC81A03594A5)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_ASSIGNED_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-6FAE9B72-F619-4B8C-9619-0B19ADDAE9FA)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-1766A54D-4542-4254-9AC1-07B85AE71DB3)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CLOUD_SUBSCRIPTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-90BC4496-23E7-4CD2-99A6-64FF97E32E59)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_CHILD_TENANCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-7C222CAB-0AA1-4DEC-BEBD-7A98AD953B51)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-01E2170E-F95F-45DC-B793-5D6863E801BF)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_DOMAIN_GOVERNANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-EFB4DAEC-ACB4-47F1-AE21-749735AAB303)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_SENDER_INVITATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-5A29E85E-8D44-4264-A1CE-7B3D4BA04764)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_CREATE_SUBSCRIPTION_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-0DD9FC09-5BCD-4D1B-8C66-9F5436B9B835)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-FF301179-F52A-4650-8D28-B049180E82C9)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-75B7435B-A956-423B-8AF1-F1FB56AC43FC)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A8E17B88-51DA-4472-B222-9EC9601F6575)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A9C6292E-6B1C-4E19-B6B7-DB53906EF8BC)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-34FDDBF9-C898-4562-99FA-EDB2D51DD2DA)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-38B9A241-3061-4314-A47D-1839D30A69CF)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-3D9FE3B2-5320-454C-8D8A-F0CD1A2A1E9D)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_DOMAIN_GOVERNANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-6B3129A4-F261-45F7-BAFA-DAC87CDD763F)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-7D36F340-BE33-4A5C-AC71-7F6F5EA4AC58)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-003BA655-901C-4D0F-BFA6-6D86D7382014)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-5BD40F7B-6D01-416B-AD8D-C360523F184B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-1825F6C4-5134-4663-8B0C-30262F0992C0)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_LINK_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-B00DCF91-B007-4006-B31D-621DDF1A494F)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SKU_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-34A9F154-04CF-4201-8DE3-FDF73F508B71)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SKU_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-7302033C-2F6F-491E-B411-075BE0D9E04F)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-F90B2CC7-9688-4AC5-A7A8-0FCDF323307C)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-58BCAF18-A119-4CAC-BDD0-9B6FF935E0D3)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-CF63ABC5-EC0B-4557-8BD0-F3040286E2A0)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-0DE2DB4C-430F-47C2-BEB6-D3014C848744)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-53ECB808-1F29-4FAE-8FB3-8A66BB3A3145)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-404966ED-CBAD-4FB1-848E-8711673C8635)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-D330AB20-363A-4B2C-B2F7-F83B2C555F0B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9BFCA57C-844F-408A-B06F-D919136F6E57)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-D14A70F4-88D7-404C-ADB5-F14456F85535)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-8D449E9B-F52F-41AD-916B-71804A9E86F4)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_ORGANIZATION_TENANCY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-C5C4148E-F347-46F8-94AC-0F734E1C1163)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9FA07A36-D47A-40F2-9670-E148F5A7C27A)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-DB1D74B5-B324-45AB-A0B4-F396B162BEF2)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-4B49DE19-76A9-4F79-8B74-6E63FFE37314)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_RECIPIENT_INVITATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-D3B32854-0849-4828-8768-5E71AEF9D744)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_REVIVE_WORKFLOW_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-4A71774D-4DC2-42F1-A2DC-81A82547814A)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-779907BE-4147-43B8-88A8-1A721E655F91)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-6C3A4DE6-EA22-4EEB-A898-16A28F6E1F4B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-13F3CAF6-8B8C-4574-A178-88E5A419ED8B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SENDER_INVITATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-5003426D-7CBA-4E13-BB49-88A5D1C54380)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-DF929DCB-7E4C-4D23-835D-D7AE07B42C1B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A0945F13-CD04-40D5-8286-43C334B24CE0)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9123C065-7E18-4995-BB2B-D58545D8DF02)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-E5834562-F040-4CA9-9B56-F5CA190C1F1B)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_LINE_ITEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-AE05E034-C252-4E1E-8C34-C92966B2F5A5)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-962EDD9B-7A7D-4100-94AE-9D5AA0A320F7)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-4A77BAE6-1D43-4CE0-9F80-F3190C181994)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-EFA6126D-5B38-4806-8324-7C83460130A8)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_SUBSCRIPTION_MAPPING_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-C0B8D51E-49CB-4E5D-BF36-FDF94F8471F2)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-AA3ADADF-56F2-410C-BCDA-620E139904E8)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_DOMAIN_GOVERNANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-7522B29F-6629-4CE1-8D36-F1F888447E83)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_ORGANIZATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-8854F8B6-02D0-4346-9DE9-37CB070C44AF)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_RECIPIENT_INVITATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-6662B745-0CB7-41C1-BDE3-A8E83EFF9279)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_UPDATE_SENDER_INVITATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-71FED2A9-6304-4D9E-A99A-F2DC950154CB)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-976B1AE9-C1EC-4D97-8AC6-E30A2CC2326E)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-151A43D1-DFBE-4AE4-B5CB-9CCBB007EC3A)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-733EFA35-0C84-4852-B0F7-4FBBE5E6FD7C)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-746BE332-73C6-4CA8-BC09-BDFE6EE25129)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9CF56CE5-5297-4B50-9781-FCFBAB8F513F)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-70579AC2-3AED-4920-A035-7F975AC9209C)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-A7A04555-3E1B-484F-9C19-0067E067B103)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-2590CFDC-85EC-409A-B35C-A15E78FAC121)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-9F9748DE-A96B-4ABA-9281-1978D1697A55)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-62E29F2C-D859-4877-BD57-0072897B6E63)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-1C99731E-AC53-4341-90B3-1B222CFEB8BD)
- [DBMS_CLOUD_OCI_TENANT_MANAGER_CONTROL_PLANE_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/tenant_manager_control_plane_t.html#ADSDK-GUID-36B2E4DC-D248-4647-A2E4-6D2E313FBA10)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
