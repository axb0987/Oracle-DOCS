# CIMS Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#dcoc-content-body)

## CIMS Common Types

### DBMS_CLOUD_OCI_CIMS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_CATEGORY_T Type

Details about the service category associated with the support ticket.

Syntax
```

```

Fields

Field Description

`category_key`

(optional) Unique identifier for the service category.

`name`

(optional) The name of the service category. For example, `Compute` or `Identity`.

### DBMS_CLOUD_OCI_CIMS_SUB_CATEGORY_T Type

Details about the service subcategory associated with the support ticket.

Syntax
```

```

Fields

Field Description

`sub_category_key`

(optional) Unique identifier for the service subcategory.

`name`

(optional) The name of the service subcategory. For example, `Backup Count` or `Custom Image Count`.

### DBMS_CLOUD_OCI_CIMS_ISSUE_TYPE_T Type

Details about the issue type associated with the support ticket.

Syntax
```

```

Fields

Field Description

`issue_type_key`

(optional) Unique identifier for the issue type.

`label`

(optional) The label for the issue type. For example, `Instance Performance`.

`name`

(optional) The URL for the contextual documentation.

### DBMS_CLOUD_OCI_CIMS_ITEM_T Type

Details about the item object.

Syntax
```

```

Fields

Field Description

`item_key`

(required) Unique identifier for the item.

`name`

(optional) The display name of the item. Avoid entering confidential information.

`l_type`

(optional) The type of the item.

`category`

(optional)

`sub_category`

(optional)

`issue_type`

(optional)

### DBMS_CLOUD_OCI_CIMS_ACCOUNT_ITEM_T Type

Details about the AccountItem object.

Syntax
```

```

`dbms_cloud_oci_cims_account_item_t`is a subtype of the`dbms_cloud_oci_cims_item_t`type.

### DBMS_CLOUD_OCI_CIMS_ACTIVITY_ITEM_T Type

Details about the ActivityItem object.

Syntax
```

```

`dbms_cloud_oci_cims_activity_item_t`is a subtype of the`dbms_cloud_oci_cims_item_t`type.

Fields

Field Description

`comments`

(required) Comments added with the activity on the support ticket.

`time_created`

(required) The time when the activity was created, in milliseconds since epoch time.

`time_updated`

(required) The time when the activity was updated, in milliseconds since epoch time.

`activity_type`

(required) The type of activity occuring on the support ticket.

Allowed values are: 'NOTES', 'PROBLEM_DESCRIPTION', 'UPDATE', 'CLOSE', 'REOPEN'

`activity_author`

(required)

Allowed values are: 'CUSTOMER', 'ORACLE'

`item_type`

(optional)

Allowed values are: 'ATTACHMENTS', 'COMMENTS'

`item_status`

(optional) Who updates the activity on the support ticket.

Allowed values are: 'PROCESSING', 'ATTACHED', 'REMOVED', 'FAILED'

### DBMS_CLOUD_OCI_CIMS_ISSUE_TYPE_TBL Type

Nested table type of dbms_cloud_oci_cims_issue_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_CLASSIFIER_T Type

Details about the incident classifier object.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier of the classifier.

`name`

(optional) The display name of the classifier.

`label`

(optional) The label associated with the classifier.

`description`

(optional) The description of the classifier.

`issue_type_list`

(optional) The list of issues.

`scope`

(optional) The scope of the service category or resource.

Allowed values are: 'AD', 'REGION', 'TENANCY', 'NONE'

`unit`

(optional) The unit to use to measure the service category or resource.

Allowed values are: 'COUNT', 'GB', 'NONE'

### DBMS_CLOUD_OCI_CIMS_CONTACT_T Type

Contact details for the customer. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`contact_name`

(optional) The name of the contact person.

`contact_email`

(optional) The email of the contact person.

`email`

(optional) The email of the contact person.

`contact_phone`

(optional) The phone number of the contact person.

`contact_type`

(optional) The type of contact, such as primary or alternate.

Allowed values are: 'PRIMARY', 'ALTERNATE', 'SECONDARY', 'ADMIN', 'MANAGER'

### DBMS_CLOUD_OCI_CIMS_CONTACT_TBL Type

Nested table type of dbms_cloud_oci_cims_contact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_CONTACT_LIST_T Type

The list of contacts for the ticket.

Syntax
```

```

Fields

Field Description

`contact_list`

(required) The list of contacts.

### DBMS_CLOUD_OCI_CIMS_CONTEXTUAL_DATA_T Type

Information collected from user context during ticket creation.

Syntax
```

```

Fields

Field Description

`client_id`

(required) The unique identifier for the client.

`schema_name`

(required) The name assigned to the schema.

`schema_version`

(required) The version of the schema.

`payload`

(required) The payload for the contextual data.

### DBMS_CLOUD_OCI_CIMS_CREATE_CATEGORY_DETAILS_T Type

Details for creating the category of the support ticket.

Syntax
```

```

Fields

Field Description

`category_key`

(optional) Unique identifier for the service category.

### DBMS_CLOUD_OCI_CIMS_CREATE_SUB_CATEGORY_DETAILS_T Type

Details for creating the service subcategory of the support ticket.

Syntax
```

```

Fields

Field Description

`sub_category_key`

(optional) Unique identifier for the service subcategory.

### DBMS_CLOUD_OCI_CIMS_CREATE_ISSUE_TYPE_DETAILS_T Type

Details for creating the issue type of the support ticket.

Syntax
```

```

Fields

Field Description

`issue_type_key`

(optional) Unique identifier for the issue type.

### DBMS_CLOUD_OCI_CIMS_CREATE_ITEM_DETAILS_T Type

Details gathered during ticket creation.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of the ticket.

`category`

(optional)

`sub_category`

(optional)

`issue_type`

(optional)

`name`

(optional) The display name of the ticket. Avoid entering confidential information.

### DBMS_CLOUD_OCI_CIMS_CREATE_ACCOUNT_ITEM_DETAILS_T Type

Details about the issue that the account support ticket relates to. Avoid entering confidential information.

Syntax
```

```

`dbms_cloud_oci_cims_create_account_item_details_t`is a subtype of the`dbms_cloud_oci_cims_create_item_details_t`type.

### DBMS_CLOUD_OCI_CIMS_CREATE_RESOURCE_DETAILS_T Type

Details about the resource that the support ticket relates to.

Syntax
```

```

Fields

Field Description

`item`

(optional)

`l_region`

(optional) The list of available Oracle Cloud Infrastructure regions.

### DBMS_CLOUD_OCI_CIMS_CREATE_RESOURCE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_cims_create_resource_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_CREATE_TICKET_DETAILS_T Type

Details relevant to the support ticket.

Syntax
```

```

Fields

Field Description

`severity`

(required) The severity of the support ticket.

Allowed values are: 'HIGHEST', 'HIGH', 'MEDIUM', 'LOW'

`resource_list`

(optional) The list of resources.

`title`

(required) The title of the support ticket. Avoid entering confidential information.

`description`

(required) The description of the support ticket. Avoid entering confidential information.

`contextual_data`

(optional)

### DBMS_CLOUD_OCI_CIMS_CREATE_INCIDENT_T Type

Details gathered during the creation of the support ticket.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy.

`ticket`

(required)

`csi`

(optional) The Customer Support Identifier (CSI) number associated with the support account. The CSI is required for technical support tickets and optional for limits and billing tickets.

`problem_type`

(required) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

`contacts`

(optional) The list of contacts.

`referrer`

(optional) The incident referrer. This value is often the URL that the customer used when creating the support ticket.

### DBMS_CLOUD_OCI_CIMS_CREATE_LIMIT_ITEM_DETAILS_T Type

Details about the service limit increase request. Avoid entering confidential information.

Syntax
```

```

`dbms_cloud_oci_cims_create_limit_item_details_t`is a subtype of the`dbms_cloud_oci_cims_create_item_details_t`type.

Fields

Field Description

`current_limit`

(optional) The limit of the resource currently available.

`current_usage`

(optional) The current usage of the resource.

`requested_limit`

(optional) The new service limit being requested.

`limit_status`

(optional) The current status of the request.

Allowed values are: 'APPROVED', 'PARTIALLY_APPROVED', 'NOT_APPROVED'

### DBMS_CLOUD_OCI_CIMS_CREATE_TECH_SUPPORT_ITEM_DETAILS_T Type

Details about the issue that the technical support ticket relates to. Avoid entering confidential information.

Syntax
```

```

`dbms_cloud_oci_cims_create_tech_support_item_details_t`is a subtype of the`dbms_cloud_oci_cims_create_item_details_t`type.

### DBMS_CLOUD_OCI_CIMS_CREATE_USER_DETAILS_T Type

Details for creating a new user.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy.

`first_name`

(required) First name of the user.

`last_name`

(required) Last name of the user.

`csi`

(required) CSI associated with the user.

`phone`

(required) Contact number of the user.

`timezone`

(required) Timezone of the user.

`organization_name`

(required) Organization of the user.

`problem_type`

(required) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

### DBMS_CLOUD_OCI_CIMS_ERROR_T Type

Details about an error that occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

Allowed values are: 'CONTENT_EMPTY', 'CLIENT_EXCEPTION', 'INVALID_FORMAT', 'INVALID_JSON_INPUT', 'SSL_AUTHORIZATION', 'AUTH_FAILED', 'AUTHZ_FAILED', 'CSI_NOT_AUTHORIZED', 'USER_POLICY_NOT_AUTHORIZED', 'EMAIL_NOT_VERIFIED', 'EMAIL_NOT_FOUND', 'OCI_EMAIL_NOT_FOUND', 'MOS_EMAIL_NOT_FOUND', 'IDCS_EMAIL_NOT_VALID', 'INVALID_PATH', 'METHOD_NOT_ALLOWED', 'JSON_PROCESSING', 'GENERIC_EXCEPTION', 'EXTERNAL_SERVICE_PROVIDER_UNAVAILABLE', 'EXTERNAL_SERVICE_PROVIDER_TIMEOUT', 'TOO_MANY_REQUESTS', 'IDP_SCIM_NOT_SETUP', 'INCIDENT_NOT_FOUND', 'INVALID_USER_CSI', 'DATA_ALREADY_EXISTS', 'AUTH_USER_NOT_MATCHING', 'CONTACT_NOT_APPROVED', 'CREATE_PROFILE_MOS_FAILURE', 'CREATE_PROFILE_CREATE_OSSO_FAILURE', 'CREATE_PROFILE_IDENTITY_FAILURE', 'CREATE_PROFILE_VERIFY_OSSO_FAILURE', 'PROFILE_ACCOUNT_NOT_VERIFIED', 'SUPPORT_ACCOUNT_NOT_FOUND', 'SUPPORT_ACCOUNT_PENDING_CSI_APPROVAL', 'FREE_TIER_CUSTOMER_SLI_UNSUPPORTED', 'PROFILE_ACCOUNT_VERIFIED', 'PROFILE_VERIFIED_CSI_REQUEST_PENDING', 'PROFILE_VERIFIED_CSI_REQUEST_NOT_FOUND', 'CREATE_PROFILE_ORGANIZATION_NAME_INVALID', 'CREATE_PROFILE_EMAIL_INVALID'

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_CIMS_TENANCY_INFORMATION_T Type

Details about the tenancy.

Syntax
```

```

Fields

Field Description

`customer_support_key`

(required) The Customer Support Identifier (CSI) number associated with the tenancy.

`tenancy_id`

(required) The OCID of the tenancy.

### DBMS_CLOUD_OCI_CIMS_RESOURCE_T Type

Details about the ticket item object.

Syntax
```

```

Fields

Field Description

`item`

(optional)

`l_region`

(optional) The list of available Oracle Cloud Infrastructure regions.

### DBMS_CLOUD_OCI_CIMS_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_cims_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_TICKET_T Type

Details about the ticket created.

Syntax
```

```

Fields

Field Description

`ticket_number`

(optional) Unique identifier for the ticket.

`severity`

(required) The severity assigned to the ticket.

Allowed values are: 'HIGHEST', 'HIGH', 'MEDIUM', 'LOW'

`resource_list`

(optional) The list of resources associated with the ticket.

`title`

(required) The title of the ticket.

`description`

(required) The description of the issue addressed in the ticket.

`time_created`

(optional) The time when the ticket was created, in milliseconds since epoch time.

`time_updated`

(optional) The time when the ticket was updated, in milliseconds since epoch time.

`lifecycle_state`

(optional) The current state of the ticket.

Allowed values are: 'ACTIVE', 'CLOSED'

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

Allowed values are: 'PENDING_WITH_ORACLE', 'PENDING_WITH_CUSTOMER', 'CLOSE_REQUESTED', 'CLOSED'

### DBMS_CLOUD_OCI_CIMS_CLASSIFIER_TBL Type

Nested table type of dbms_cloud_oci_cims_classifier_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_INCIDENT_TYPE_T Type

Details about the incident type associated with the support ticket.

Syntax
```

```

Fields

Field Description

`id`

(optional) Unique identifier for the incident type.

`name`

(optional) The name of the incident type.

`label`

(optional) The label associated with the incident type.

`description`

(optional) The description of the incident type.

`classifier_list`

(optional) The list of classifiers.

### DBMS_CLOUD_OCI_CIMS_INCIDENT_T Type

Details about the support ticket.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier for the support ticket.

`compartment_id`

(optional) The OCID of the tenancy.

`contact_list`

(optional)

`tenancy_information`

(optional)

`ticket`

(optional)

`incident_type`

(optional)

`problem_type`

(optional) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

`referrer`

(optional) The incident referrer. This value is often the URL that the customer used when creating the support ticket.

### DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORY_T Type

Information about the support ticket classifier.

Syntax
```

```

Fields

Field Description

`key`

(optional) The unique ID that identifies a classifier.

`name`

(optional) The name of the classifier.

`label`

(optional) The label for the classifier.

`description`

(optional) The text describing the classifier.

`issue_type_list`

(optional) The list of issues.

`scope`

(optional) The scope of the incident.

Allowed values are: 'AD', 'REGION', 'TENANCY', 'NONE'

`unit`

(optional) The unit to use to measure the service category or resource.

Allowed values are: 'COUNT', 'GB', 'NONE'

`limit_id`

(optional) The unique ID for the limit.

### DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORIES_T Type

List of Service Categories of a Service for MOS Taxonomy.

Syntax
```

```

Fields

Field Description

`service_category`

(optional) Service Category list.

`schema`

(optional) Schema of a Service Category.

`issue_type`

(optional) Issue type list.

### DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORY_TBL Type

Nested table type of dbms_cloud_oci_cims_service_category_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORIES_TBL Type

Nested table type of dbms_cloud_oci_cims_service_categories_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CIMS_INCIDENT_RESOURCE_TYPE_T Type

Details about the resource associated with the support request.

Syntax
```

```

Fields

Field Description

`resource_type_key`

(optional) A unique identifier for the resource.

`name`

(optional) The display name of the resource.

`label`

(required) The label associated with the resource.

`description`

(optional) The description of the resource.

`service_category_list`

(optional) The service category list.

`service`

(optional) The map of services for MOS Taxonomy.

`service_categories`

(optional) The service categories list for MOS Taxonomy.

### DBMS_CLOUD_OCI_CIMS_INCIDENT_SUMMARY_T Type

Details about the support ticket.

Syntax
```

```

Fields

Field Description

`key`

(required) Unique identifier of the incident.

`compartment_id`

(optional) The OCID of the tenancy.

`contact_list`

(optional)

`tenancy_information`

(optional)

`ticket`

(optional)

`incident_type`

(optional)

`problem_type`

(required) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

### DBMS_CLOUD_OCI_CIMS_LIMIT_ITEM_T Type

Details about the LimitItem object.

Syntax
```

```

`dbms_cloud_oci_cims_limit_item_t`is a subtype of the`dbms_cloud_oci_cims_item_t`type.

Fields

Field Description

`current_limit`

(optional) The current service limit for the resource.

`current_usage`

(optional) The current resource usage.

`requested_limit`

(optional) The new service limit being requested for the resource.

`limit_status`

(optional) The status of the request.

Allowed values are: 'APPROVED', 'PARTIALLY_APPROVED', 'NOT_APPROVED'

### DBMS_CLOUD_OCI_CIMS_STATUS_T Type

Details about the status of the support ticket.

Syntax
```

```

Fields

Field Description

`code`

(required) The code unique to this ticket status.

`message`

(required) The status message for this ticket.

### DBMS_CLOUD_OCI_CIMS_TECH_SUPPORT_ITEM_T Type

Details about the TechSupportItem object.

Syntax
```

```

`dbms_cloud_oci_cims_tech_support_item_t`is a subtype of the`dbms_cloud_oci_cims_item_t`type.

### DBMS_CLOUD_OCI_CIMS_UPDATE_ITEM_DETAILS_T Type

Details for updating an item.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of the ticket.

### DBMS_CLOUD_OCI_CIMS_UPDATE_ACTIVITY_ITEM_DETAILS_T Type

Details for updating the support ticket activity.

Syntax
```

```

`dbms_cloud_oci_cims_update_activity_item_details_t`is a subtype of the`dbms_cloud_oci_cims_update_item_details_t`type.

Fields

Field Description

`comments`

(optional) Comments updated at the time that the activity occurs.

`activity_type`

(optional) The type of activity occurring.

Allowed values are: 'NOTES', 'PROBLEM_DESCRIPTION', 'UPDATE', 'CLOSE', 'REOPEN'

### DBMS_CLOUD_OCI_CIMS_UPDATE_TICKET_DETAILS_T Type

Details about the ticket updated.

Syntax
```

```

Fields

Field Description

`l_resource`

(required) The list of resources.

### DBMS_CLOUD_OCI_CIMS_UPDATE_INCIDENT_T Type

Details about the support ticket being updated.

Syntax
```

```

Fields

Field Description

`ticket`

(required)

`problem_type`

(optional) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

### DBMS_CLOUD_OCI_CIMS_UPDATE_RESOURCE_DETAILS_T Type

Details about updates to the resource.

Syntax
```

```

Fields

Field Description

`item`

(optional)

### DBMS_CLOUD_OCI_CIMS_USER_T Type

Details about the user.

Syntax
```

```

Fields

Field Description

`key`

(required) A unique identifier for the user.

`first_name`

(optional) The user's first name.

`last_name`

(optional) The user's last name.

`country`

(optional) The country of the user.

`csi`

(optional) The CSI associated with the user.

`phone`

(optional) The user's contact phone number.

`timezone`

(optional) The timezone of the user.

`organization_name`

(optional) The company that the user belongs to.

`compartment_id`

(optional) The OCID of the tenancy.

`contact_email`

(optional) The email of the contact person.

`problem_type`

(optional) The kind of support ticket, such as a technical support request or a limit increase request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

### DBMS_CLOUD_OCI_CIMS_VALIDATION_RESPONSE_T Type

The validation response returned when checking whether the requested user is valid.

Syntax
```

```

Fields

Field Description

`is_valid_user`

(optional) Boolean value that indicates whether the requested user is valid.

- [CIMS Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-B509FE0E-7B17-4864-94BD-5E4B52AFA6BE)
- [DBMS_CLOUD_OCI_CIMS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-ABF430D7-0FF6-4521-9186-58D50FC915DE)
- [DBMS_CLOUD_OCI_CIMS_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-D4619288-229F-4926-8801-30ACD100CC4B)
- [DBMS_CLOUD_OCI_CIMS_SUB_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-AB0498DB-6EB1-45B1-B273-5C7808508AEF)
- [DBMS_CLOUD_OCI_CIMS_ISSUE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-F9962BD7-6CD4-4E2D-A5D7-9B839394C672)
- [DBMS_CLOUD_OCI_CIMS_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-F4BCD4B8-487B-472E-B99B-D0F734D01A7E)
- [DBMS_CLOUD_OCI_CIMS_ACCOUNT_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-4887C0FD-1139-4260-B517-2F62AE5A241C)
- [DBMS_CLOUD_OCI_CIMS_ACTIVITY_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-89627E6C-B1FB-4CE6-BE83-771AD1556943)
- [DBMS_CLOUD_OCI_CIMS_ISSUE_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-1CCEBF2B-7473-438A-BA50-E04631E25ACC)
- [DBMS_CLOUD_OCI_CIMS_CLASSIFIER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-505C75F2-0C7C-4647-A58E-F0110AB9FA1F)
- [DBMS_CLOUD_OCI_CIMS_CONTACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-630BBDE6-6630-4A63-8C69-AEB551B47B73)
- [DBMS_CLOUD_OCI_CIMS_CONTACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-F0FB46AF-5F43-455C-B922-65FBD9EABE76)
- [DBMS_CLOUD_OCI_CIMS_CONTACT_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-CCCD9649-D4AA-4101-AA4F-CF29D4EE4FF7)
- [DBMS_CLOUD_OCI_CIMS_CONTEXTUAL_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-974A5A87-FF0D-43AB-BE9A-B81E916735A2)
- [DBMS_CLOUD_OCI_CIMS_CREATE_CATEGORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-BC8DED78-6235-4AAA-9E8C-7BA8436B0072)
- [DBMS_CLOUD_OCI_CIMS_CREATE_SUB_CATEGORY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-BC08537F-79C1-41D1-9E0D-8731FF0912C8)
- [DBMS_CLOUD_OCI_CIMS_CREATE_ISSUE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-01BAE255-EAD3-4A48-8A9E-38CD7D930C5C)
- [DBMS_CLOUD_OCI_CIMS_CREATE_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-3F9BD4C5-638D-4044-A8F6-CAD1D6CECCB2)
- [DBMS_CLOUD_OCI_CIMS_CREATE_ACCOUNT_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-3A1FC3A9-C0D2-42EA-AD98-C4CF09FB51AD)
- [DBMS_CLOUD_OCI_CIMS_CREATE_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-C42B039E-2043-4007-ABED-D24667F10807)
- [DBMS_CLOUD_OCI_CIMS_CREATE_RESOURCE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-CA8A62CB-06B6-4F2E-82D3-ADB6FD22AAB6)
- [DBMS_CLOUD_OCI_CIMS_CREATE_TICKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-00A99730-8554-453A-87C0-58B001489C70)
- [DBMS_CLOUD_OCI_CIMS_CREATE_INCIDENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-1342D548-A013-42A0-8A4B-DA2F922830A0)
- [DBMS_CLOUD_OCI_CIMS_CREATE_LIMIT_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-4A900E7B-A11D-46CD-9A19-2EBA68D6B0EC)
- [DBMS_CLOUD_OCI_CIMS_CREATE_TECH_SUPPORT_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-36C08651-34E6-48C6-868C-6B0CCE4C7C48)
- [DBMS_CLOUD_OCI_CIMS_CREATE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-F28010FA-0B1F-4E22-A9AC-D36387C7C6FF)
- [DBMS_CLOUD_OCI_CIMS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-CE8C6AF2-8125-41C6-A812-C5A035115EE6)
- [DBMS_CLOUD_OCI_CIMS_TENANCY_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-B0B69B18-8356-48FB-A1BC-C12BF9891CD9)
- [DBMS_CLOUD_OCI_CIMS_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-30969107-2721-493C-91FF-477534EDB95C)
- [DBMS_CLOUD_OCI_CIMS_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-1A750E52-4652-45A4-8CE0-4186F322775A)
- [DBMS_CLOUD_OCI_CIMS_TICKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-4B1BA857-11D0-4CC5-A82D-778A2EB82D8D)
- [DBMS_CLOUD_OCI_CIMS_CLASSIFIER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-0A6A1B3E-D87F-4CAE-9E49-99242772F26F)
- [DBMS_CLOUD_OCI_CIMS_INCIDENT_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-5DF5DE47-AAFB-4979-B5C0-C9AA0DA3FBBE)
- [DBMS_CLOUD_OCI_CIMS_INCIDENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-4B6C6475-0EB4-4C52-B9BB-DF439DFE8268)
- [DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-C354FE05-EDEB-41F1-B280-236C4718D924)
- [DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-640421B0-A61F-4F8F-9136-C118419E85A2)
- [DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-29F96D2B-F255-4CD0-BDDA-8C5901E7D4B1)
- [DBMS_CLOUD_OCI_CIMS_SERVICE_CATEGORIES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-0885D5B7-0171-4657-8B4F-2CFB113CEC25)
- [DBMS_CLOUD_OCI_CIMS_INCIDENT_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-7B93AF55-CAF0-4176-A948-9D8006DF9FDA)
- [DBMS_CLOUD_OCI_CIMS_INCIDENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-B246DCAB-9CBB-4172-ABCE-E92AA21014A4)
- [DBMS_CLOUD_OCI_CIMS_LIMIT_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-FC1CE907-3AF6-4B6C-9213-4AAE0225DDC6)
- [DBMS_CLOUD_OCI_CIMS_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-DC890BE4-0CB0-43A3-A7B5-AD79CDA992DD)
- [DBMS_CLOUD_OCI_CIMS_TECH_SUPPORT_ITEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-B29AB7CA-44AB-4ED5-9D16-61A095B95F7F)
- [DBMS_CLOUD_OCI_CIMS_UPDATE_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-54D0A818-6398-414F-9AF9-9B812347CA35)
- [DBMS_CLOUD_OCI_CIMS_UPDATE_ACTIVITY_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-62133E64-7E74-45D1-80E5-47249956EAF0)
- [DBMS_CLOUD_OCI_CIMS_UPDATE_TICKET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-027CA547-4819-450E-9800-8DD9BA0E3E95)
- [DBMS_CLOUD_OCI_CIMS_UPDATE_INCIDENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-79C88AD7-BA99-4B91-B1D2-F588DD74B413)
- [DBMS_CLOUD_OCI_CIMS_UPDATE_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-691B0889-08D7-4A0E-88CE-30C7E39DBC7C)
- [DBMS_CLOUD_OCI_CIMS_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-37858BFB-FD9E-49AB-91FB-B80431EE4538)
- [DBMS_CLOUD_OCI_CIMS_VALIDATION_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/cims_t.html#ADSDK-GUID-2892E414-4708-4DD1-AD94-74A4539C4F24)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
