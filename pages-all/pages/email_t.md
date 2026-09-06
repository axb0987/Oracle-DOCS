# Email Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#dcoc-content-body)

## Email Common Types

### DBMS_CLOUD_OCI_EMAIL_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_CHANGE_EMAIL_DOMAIN_COMPARTMENT_DETAILS_T Type

The configuration details for the move operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the specified resource to.

### DBMS_CLOUD_OCI_EMAIL_CHANGE_SENDER_COMPARTMENT_DETAILS_T Type

The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the sender should be moved.

### DBMS_CLOUD_OCI_EMAIL_CREATE_DKIM_DETAILS_T Type

Properties to create a new DKIM. The new object will be created in the same compartment as the EmailDomain.

Syntax
```

```

Fields

Field Description

`name`

(optional) The DKIM selector. This selector is required to be globally unique for this email domain. If you do not provide the selector, we will generate one for you. If you do provide the selector, we suggest adding a short region indicator to differentiate from your signing of emails in other regions you may be subscribed to. Selectors limited to ASCII characters may use alphanumeric, dash (\"-\"), and dot (\".\") characters. Non-ASCII selector names should adopt IDNA2008 normalization (RFC 5891-5892). Avoid entering confidential information. Example: `mydomain-phx-20210228`

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the EmailDomain for this DKIM.

`description`

(optional) A string that describes the details about the DKIM. It does not have to be unique, and you can change it. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_CREATE_EMAIL_DOMAIN_DETAILS_T Type

The configuration details for creating a new email domain.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the email domain in the Internet Domain Name System (DNS). The email domain name must be unique in the region for this tenancy. Domain names limited to ASCII characters use alphanumeric, dash (\"-\"), and dot (\".\") characters. The dash and dot are only allowed between alphanumeric characters. For details, please see: https://tools.ietf.org/html/rfc5321#section-4.1.2 Non-ASCII domain names should adopt IDNA2008 normalization (RFC 5891-5892).

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment for this email domain.

`description`

(optional) A string that describes the details about the domain. It does not have to be unique, and you can change it. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_CREATE_SENDER_DETAILS_T Type

The details needed for creating a sender.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the sender.

`email_address`

(required) The email address of the sender.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_CREATE_SUPPRESSION_DETAILS_T Type

The details needed for creating a single suppression.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.

`email_address`

(required) The recipient email address of the suppression.

### DBMS_CLOUD_OCI_EMAIL_DKIM_T Type

The properties that define a DKIM.

Syntax
```

```

Fields

Field Description

`name`

(required) The DKIM selector. If the same domain is managed in more than one region, each region must use different selectors.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DKIM.

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the email domain that this DKIM belongs to.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains this DKIM.

`lifecycle_state`

(optional) The current state of the DKIM.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE', 'NEEDS_ATTENTION', 'UPDATING'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource.

`description`

(optional) The description of the DKIM. Avoid entering confidential information.

`time_created`

(optional) The time the DKIM was created. Times are expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\". Example: `2021-02-12T22:47:12.613Z`

`time_updated`

(optional) The time of the last change to the DKIM configuration, due to a state change or an update operation. Times are expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\".

`dns_subdomain_name`

(optional) The name of the DNS subdomain that must be provisioned to enable email recipients to verify DKIM signatures. It is usually created with a CNAME record set to the cnameRecordValue

`cname_record_value`

(optional) The DNS CNAME record value to provision to the DKIM DNS subdomain, when using the CNAME method for DKIM setup (preferred).

`txt_record_value`

(optional) The DNS TXT record value to provision to the DKIM DNS subdomain in place of using a CNAME record. This is used in cases where a CNAME can not be used, such as when the cnameRecordValue would exceed the maximum length for a DNS entry. This can also be used by customers who have an existing procedure to directly provision TXT records for DKIM. Be aware that many DNS APIs will require you to break this string into segments of less than 255 characters.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EMAIL_DKIM_SUMMARY_T Type

The properties that define a DKIM.

Syntax
```

```

Fields

Field Description

`name`

(required) The DKIM selector. This selector is required to be globally unique for this email domain.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DKIM.

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the email domain that this DKIM belongs to.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains this DKIM.

`lifecycle_state`

(optional) The current state of the DKIM.

`description`

(optional) The description of a DKIM. Avoid entering confidential information.

`time_created`

(optional) The time the DKIM was created. Times are expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\". Example: `2021-02-12T22:47:12.613Z`

`time_updated`

(optional) The time of the last change to the DKIM configuration, due to a state change or an update operation. Times are expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\".

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EMAIL_DKIM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_email_dkim_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_DKIM_COLLECTION_T Type

Results of a search. Contains boh DkimSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of dkims.

### DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_T Type

The properties that define a email domain. A Email Domain contains configuration used to assert responsibility for emails sent from that domain.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the email domain in the Internet Domain Name System (DNS). Example: `example.net`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the email domain.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains this email domain.

`lifecycle_state`

(optional) The current state of the email domain.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETING', 'DELETED', 'FAILED', 'UPDATING'

`active_dkim_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DKIM key that will be used to sign mail sent from this email domain.

`is_spf`

(optional) Value of the SPF field. For more information about SPF, please see[SPF Authentication](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).

`description`

(optional) The description of a email domain.

`time_created`

(optional) The time the email domain was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\". Example: `2021-02-12T22:47:12.613Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_SUMMARY_T Type

The properties that define a email domain. A Email Domain contains configuration used to assert responsibility for emails sent from that domain.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the email domain in the Internet Domain Name System (DNS). Example: `example.net`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the email domain.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains this email domain.

`lifecycle_state`

(optional) The current state of the email domain.

`active_dkim_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DKIM key that is adding the DKIM signature for this email domain.

`description`

(optional) The description of a email domain.

`time_created`

(optional) The time the email domain was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format, \"YYYY-MM-ddThh:mmZ\". Example: `2021-02-12T22:47:12.613Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_email_email_domain_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_COLLECTION_T Type

Results of an EmailDomain search. Contains boh EmailDomainSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of email domains.

### DBMS_CLOUD_OCI_EMAIL_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_EMAIL_SENDER_T Type

The full information representing an approved sender.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID for the compartment.

`email_address`

(required) Email address of the sender.

`id`

(required) The unique OCID of the sender.

`is_spf`

(optional) Value of the SPF field. For more information about SPF, please see[SPF Authentication](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).

`lifecycle_state`

(optional) The sender's current lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(optional) The date and time the approved sender was added in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`email_domain_id`

(optional) The email domain used to assert responsibility for emails sent from this sender.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_SENDER_SUMMARY_T Type

The email addresses and `senderId` representing an approved sender.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID for the compartment.

`email_address`

(required) The email address of the sender.

`id`

(required) The unique ID of the sender.

`lifecycle_state`

(optional) The current status of the approved sender.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(optional) Date time the approved sender was added, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_SUPPRESSION_T Type

The full information representing an email suppression.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.

`email_address`

(required) Email address of the suppression.

`id`

(required) The unique ID of the suppression.

`reason`

(optional) The reason that the email address was suppressed. For more information on the types of bounces, see[Suppression List](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).

Allowed values are: 'UNKNOWN', 'HARDBOUNCE', 'COMPLAINT', 'MANUAL', 'SOFTBOUNCE', 'UNSUBSCRIBE'

`time_created`

(optional) The date and time the suppression was added in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`time_last_suppressed`

(optional) The last date and time the suppression prevented submission in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`message_id`

(optional) The value of the Message-ID header from the email that triggered a suppression. This value is as defined in RFC 5322 section 3.6.4, excluding angle-brackets. Not provided for all types of suppressions.

`error_detail`

(optional) The specific error message returned by a system that resulted in the suppression. This message is usually an SMTP error code with additional descriptive text. Not provided for all types of suppressions.

`error_source`

(optional) DNS name of the source of the error that caused the suppression. Will be set to either the remote-mta or reporting-mta field from a delivery status notification (RFC 3464) when available. Not provided for all types of suppressions, and not always known. Note: Most SMTP errors that cause suppressions come from software run by email receiving systems rather than from OCI email delivery itself.

### DBMS_CLOUD_OCI_EMAIL_SUPPRESSION_SUMMARY_T Type

The full information representing a suppression.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID for the compartment.

`email_address`

(required) The email address of the suppression.

`id`

(required) The unique OCID of the suppression.

`reason`

(optional) The reason that the email address was suppressed.

Allowed values are: 'UNKNOWN', 'HARDBOUNCE', 'COMPLAINT', 'MANUAL', 'SOFTBOUNCE', 'UNSUBSCRIBE'

`time_created`

(optional) The date and time a recipient's email address was added to the suppression list, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

### DBMS_CLOUD_OCI_EMAIL_UPDATE_DKIM_DETAILS_T Type

The attributes to update in the DKIM.

Syntax
```

```

Fields

Field Description

`description`

(optional) A string that describes the details about the DKIM. It does not have to be unique, and you can change it. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_UPDATE_EMAIL_DOMAIN_DETAILS_T Type

The attributes to update in the email domain.

Syntax
```

```

Fields

Field Description

`description`

(optional) A string that describes the details about the domain. It does not have to be unique, and you can change it. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_UPDATE_SENDER_DETAILS_T Type

The details allowed for updating a sender.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_RESOURCE_T Type

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

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_email_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_DKIM', 'DELETE_DKIM', 'MOVE_DKIM', 'UPDATE_DKIM', 'CREATE_EMAIL_DOMAIN', 'DELETE_EMAIL_DOMAIN', 'MOVE_EMAIL_DOMAIN', 'UPDATE_EMAIL_DOMAIN'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

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

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_email_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a workRequestError search. Contains both WorkRequestError items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestError objects.

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_email_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a workRequestLog search. Contains both workRequestLog items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestLogEntries.

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) Type of the work request

Allowed values are: 'CREATE_DKIM', 'DELETE_DKIM', 'MOVE_DKIM', 'UPDATE_DKIM', 'CREATE_EMAIL_DOMAIN', 'DELETE_EMAIL_DOMAIN', 'MOVE_EMAIL_DOMAIN', 'UPDATE_EMAIL_DOMAIN'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

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

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_email_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_COLLECTION_T Type

Results of a workRequest search. Contains both WorkRequest items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of workRequestSummary objects.

- [Email Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-38CB50DD-959B-447C-847B-217A0135B2C5)
- [DBMS_CLOUD_OCI_EMAIL_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-0DCFE575-9AD6-4611-963C-D32BE634AF62)
- [DBMS_CLOUD_OCI_EMAIL_CHANGE_EMAIL_DOMAIN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-A6503C8E-CF28-47F0-BECC-9F185CD142B9)
- [DBMS_CLOUD_OCI_EMAIL_CHANGE_SENDER_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-D2A74604-AE11-411B-BC7A-E235ED30AE60)
- [DBMS_CLOUD_OCI_EMAIL_CREATE_DKIM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-7D5BFCB9-4FE9-4A79-90AC-4E4252A6CB36)
- [DBMS_CLOUD_OCI_EMAIL_CREATE_EMAIL_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-8A283134-4C8F-454A-ABD4-2811E6F9ADCD)
- [DBMS_CLOUD_OCI_EMAIL_CREATE_SENDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-D3C2E497-7DA3-4054-9D12-E6D8F2CB0690)
- [DBMS_CLOUD_OCI_EMAIL_CREATE_SUPPRESSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-14BECA79-8F08-4027-A80E-06736166A021)
- [DBMS_CLOUD_OCI_EMAIL_DKIM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-686641D4-810E-42C8-B005-617F9A31572A)
- [DBMS_CLOUD_OCI_EMAIL_DKIM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-9099C7AE-0FD0-4845-A5BD-75CC52B75CA7)
- [DBMS_CLOUD_OCI_EMAIL_DKIM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-B51A363F-9ED1-4C41-B471-12709D521235)
- [DBMS_CLOUD_OCI_EMAIL_DKIM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-E8518474-AC69-42A3-83EB-34C1F0B8372E)
- [DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-EB220F67-657C-49AD-8151-55955CA2E921)
- [DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-2B367103-473F-4D4A-8BB6-5A17751D2936)
- [DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-B423712B-04DB-4D9C-9709-B6915F004B72)
- [DBMS_CLOUD_OCI_EMAIL_EMAIL_DOMAIN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-A61DE3A6-1A1C-4324-8905-FBC1F1BA61D3)
- [DBMS_CLOUD_OCI_EMAIL_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-8B658A21-5B19-4DD5-B08C-6F63CFF7A8F5)
- [DBMS_CLOUD_OCI_EMAIL_SENDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-6F5C0838-5848-4C3F-BA46-4C72DA3CB7F2)
- [DBMS_CLOUD_OCI_EMAIL_SENDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-70E8264F-9382-4256-B581-D5BC2BBC9E31)
- [DBMS_CLOUD_OCI_EMAIL_SUPPRESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-15F7AF81-B478-438A-8385-D88F4AE1DC2F)
- [DBMS_CLOUD_OCI_EMAIL_SUPPRESSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-84A54954-32F9-4D17-9283-A0B3FCE71A9A)
- [DBMS_CLOUD_OCI_EMAIL_UPDATE_DKIM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-FBAFF20B-3638-42E0-B378-3EF7B0F2FD06)
- [DBMS_CLOUD_OCI_EMAIL_UPDATE_EMAIL_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-EED7308C-95CF-4EE3-B614-D8563318BDC4)
- [DBMS_CLOUD_OCI_EMAIL_UPDATE_SENDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-B3505A67-6D90-4EF1-9E7A-CCD56E6D66E0)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-5CD31337-91C7-47DE-B8D9-D0B38AEA6949)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-8737AEBC-24C7-43F9-A266-0DC67A3E3CD3)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-5B84DC82-87E9-427B-9AB8-3B11224EFEE3)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-A3977F51-6112-49B7-B699-F5284A948095)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-17319A50-228B-44D2-8740-8351683235B2)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-3E9281AA-E58E-4A3D-9CA4-1C43977B7EE1)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-F466F76D-9CFD-40B8-8A8D-510877A175E7)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-40E81CC8-EADE-4037-91BF-1FECE6D6B734)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-202814B9-5A7A-431F-A6DD-75D05D6E62EB)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-376C653B-99BD-494D-A85C-DB3ACFB1CF3D)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-BC0EC4D5-3AAE-43D9-89C8-3EF44337A0FD)
- [DBMS_CLOUD_OCI_EMAIL_WORK_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/email_t.html#ADSDK-GUID-3102D01A-ACFE-4BD9-854C-0D3E528E6CED)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
