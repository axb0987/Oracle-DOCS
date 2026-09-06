# Email Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#dcoc-content-body)

## Email Functions

Package: DBMS_CLOUD_OCI_EM_EMAIL

### CHANGE_EMAIL_DOMAIN_COMPARTMENT Function

Moves a email domain into a different compartment. When provided, If-Match is checked against ETag value of the resource. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). **Note:** All Dkim objects associated with this email domain will also be moved into the provided compartment.

Syntax
```

```

Parameters

Parameter Description

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this email domain.

`change_email_domain_compartment_details`

(required) The configuration details for the move operation.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SENDER_COMPARTMENT Function

Moves a sender into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`sender_id`

(required) The unique OCID of the sender.

`change_sender_compartment_details`

(required) Details for moving a sender into a different compartment.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DKIM Function

Creates a new DKIM for a email domain. This DKIM will sign all approved senders in the tenancy that are in this email domain. Best security practices indicate to periodically rotate the DKIM that is doing the signing. When a second DKIM is applied, all senders will seamlessly pick up the new key without interruption in signing.

Syntax
```

```

Parameters

Parameter Description

`create_dkim_details`

(required) The DKIM details.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EMAIL_DOMAIN Function

Creates a new email domain. Avoid entering confidential information.

Syntax
```

```

Parameters

Parameter Description

`create_email_domain_details`

(required) The email domain to create.

`opc_request_id`

(optional) The request ID for tracing from the system

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SENDER Function

Creates a sender for a tenancy in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`create_sender_details`

(required) Create a sender.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SUPPRESSION Function

Adds recipient email addresses to the suppression list for a tenancy. Addresses added to the suppression list via the API are denoted as \"MANUAL\" in the `reason` field. *Note:* All email addresses added to the suppression list are normalized to include only lowercase letters.

Syntax
```

```

Parameters

Parameter Description

`create_suppression_details`

(required) Adds a single email address to the suppression list for a compartment's tenancy.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DKIM Function

Deletes a DKIM. If this key is currently the active key for the email domain, deleting the key will stop signing the domain's outgoing mail. DKIM keys are left in DELETING state for about a day to allow DKIM signatures on in-transit mail to be validated. Consider instead of deletion creating a new DKIM for this domain so the signing can be rotated to it.

Syntax
```

```

Parameters

Parameter Description

`dkim_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this DKIM.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EMAIL_DOMAIN Function

Deletes a email domain.

Syntax
```

```

Parameters

Parameter Description

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this email domain.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SENDER Function

Deletes an approved sender for a tenancy in a given compartment for a provided `senderId`.

Syntax
```

```

Parameters

Parameter Description

`sender_id`

(required) The unique OCID of the sender.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SUPPRESSION Function

Removes a suppressed recipient email address from the suppression list for a tenancy in a given compartment for a provided `suppressionId`.

Syntax
```

```

Parameters

Parameter Description

`suppression_id`

(required) The unique OCID of the suppression.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DKIM Function

Retrieves the specified DKIM.

Syntax
```

```

Parameters

Parameter Description

`dkim_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this DKIM.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EMAIL_DOMAIN Function

Retrieves the specified email domain.

Syntax
```

```

Parameters

Parameter Description

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this email domain.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SENDER Function

Gets an approved sender for a given `senderId`.

Syntax
```

```

Parameters

Parameter Description

`sender_id`

(required) The unique OCID of the sender.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SUPPRESSION Function

Gets the details of a suppressed recipient email address for a given `suppressionId`. Each suppression is given a unique OCID.

Syntax
```

```

Parameters

Parameter Description

`suppression_id`

(required) The unique OCID of the suppression.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the status of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DKIMS Function

Lists DKIMs for a email domain.

Syntax
```

```

Parameters

Parameter Description

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the email domain to which this DKIM belongs.

`opc_request_id`

(optional) The request ID for tracing from the system

`id`

(optional) A filter to only return resources that match the given id exactly.

`name`

(optional) A filter to only return resources that match the given name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending or descending order.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) Filter returned list by specified lifecycle state. This parameter is case-insensitive.

`sort_by`

(optional) Specifies the attribute with which to sort the DKIMs. Default: `TIMECREATED` * **TIMECREATED:** Sorts by timeCreated. * **NAME:** Sorts by name. * **ID:** Sorts by id.

Allowed values are: 'TIMECREATED', 'ID', 'NAME'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EMAIL_DOMAINS Function

Lists email domains in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID for the compartment.

`opc_request_id`

(optional) The request ID for tracing from the system

`id`

(optional) A filter to only return resources that match the given id exactly.

`name`

(optional) A filter to only return resources that match the given name exactly.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending or descending order.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) Filter returned list by specified lifecycle state. This parameter is case-insensitive.

`sort_by`

(optional) Specifies the attribute with which to sort the email domains. Default: `TIMECREATED` * **TIMECREATED:** Sorts by timeCreated. * **NAME:** Sorts by name. * **ID:** Sorts by id.

Allowed values are: 'TIMECREATED', 'ID', 'NAME'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENDERS Function

Gets a collection of approved sender email addresses and sender IDs.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID for the compartment.

`opc_request_id`

(optional) The request ID for tracing from the system

`lifecycle_state`

(optional) The current state of a sender.

`domain`

(optional) A filter to only return resources that match the given domain exactly.

`email_address`

(optional) The email address of the approved sender.

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.

Allowed values are: 'TIMECREATED', 'EMAILADDRESS'

`sort_order`

(optional) The sort order to use, either ascending or descending order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUPPRESSIONS Function

Gets a list of suppressed recipient email addresses for a user. The `compartmentId` for suppressions must be a tenancy OCID. The returned list is sorted by creation time in descending order.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID for the compartment.

`opc_request_id`

(optional) The request ID for tracing from the system

`email_address`

(optional) The email address of the suppression.

`time_created_greater_than_or_equal_to`

(optional) Search for suppressions that were created within a specific date range, using this parameter to specify the earliest creation date for the returned list (inclusive). Specifying this parameter without the corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for suppressions that were created within a specific date range, using this parameter to specify the latest creation date for the returned list (exclusive). Specifying this parameter without the corresponding `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. The `TIMECREATED` value returns the list in in descending order by default. The `EMAILADDRESS` value returns the list in ascending order by default. Use the `SortOrderQueryParam` to change the direction of the returned list of items.

Allowed values are: 'TIMECREATED', 'EMAILADDRESS'

`sort_order`

(optional) The sort order to use, either ascending or descending order.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The request ID for tracing from the system

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The request ID for tracing from the system

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID for the compartment.

`work_request_id`

(optional) The ID of the asynchronous work request.

`opc_request_id`

(optional) The request ID for tracing from the system

`page`

(optional) For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. `1` is the minimum, `1000` is the maximum. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DKIM Function

Modifies a DKIM.

Syntax
```

```

Parameters

Parameter Description

`dkim_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this DKIM.

`update_dkim_details`

(required) The new DKIM attributes to apply.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EMAIL_DOMAIN Function

Modifies a email domain.

Syntax
```

```

Parameters

Parameter Description

`email_domain_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this email domain.

`update_email_domain_details`

(required) The new email domain attributes to apply.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SENDER Function

Replaces the set of tags for a sender with the tags provided. If either freeform or defined tags are omitted, the tags for that set remain the same. Each set must include the full set of tags for the sender, partial updates are not permitted. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

Syntax
```

```

Parameters

Parameter Description

`sender_id`

(required) The unique OCID of the sender.

`update_sender_details`

(required) update details for sender.

`if_match`

(optional) Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The request ID for tracing from the system

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://ctrl.email.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Email Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-AE764505-8806-4964-862A-BCED0F751BE7)
- [CHANGE_EMAIL_DOMAIN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-CB89CE94-2DB5-4934-8981-6D942459576C)
- [CHANGE_SENDER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-682153EC-1D51-4818-A5DC-DD4F192A7A6E)
- [CREATE_DKIM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-C78ACA91-17EB-4509-91AD-25ACE4755994)
- [CREATE_EMAIL_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-96AFA639-43EE-4654-B13E-C2F86A784F08)
- [CREATE_SENDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-512BD3BF-B5C2-42B5-8E38-C3395F9643F5)
- [CREATE_SUPPRESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-2CE0A970-4652-4173-8F47-0AD26D06CB7D)
- [DELETE_DKIM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-8BBA75A8-4546-433A-A2F8-3AC4068DD68E)
- [DELETE_EMAIL_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-59F4D7B6-F860-4F6F-B126-59BFF7B7EC61)
- [DELETE_SENDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-B1CA1330-0904-47B9-908A-13BBAE0FA688)
- [DELETE_SUPPRESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-2568E58B-FA7A-4E35-925E-3B56FFB28AC9)
- [GET_DKIM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-46C9C607-1601-426E-9037-8BF6E5FFE831)
- [GET_EMAIL_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-E7227D2F-03CE-4DEF-AEAD-9621BD3294B1)
- [GET_SENDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-939BF115-E5BD-4E4E-A176-CE7967D3D8A6)
- [GET_SUPPRESSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-0D03E25C-8DCD-4A8A-B437-745E04389569)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-5543464E-1E3B-4AAF-B6F2-B6228002DC23)
- [LIST_DKIMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-D618EB17-6FE3-4DE2-9B7A-E6A971C7D76A)
- [LIST_EMAIL_DOMAINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-F4D6AAD4-C4B5-42DF-B19B-975B1F9CCEA4)
- [LIST_SENDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-6542CFEE-A100-4DAE-BB09-50FEFC88109C)
- [LIST_SUPPRESSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-BC43267F-B3C0-4B41-9B7C-3B9D5825D7C1)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-A5375D64-BE41-48FB-A8C7-7FCE7B9660BF)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-AEC2FF6B-8115-4AF2-AB7F-FBEAF079F5C8)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-FA8C8591-A622-42EF-94DC-52D3E0BFB3F8)
- [UPDATE_DKIM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-1AD17449-613C-47A8-8814-B2F0CA88F032)
- [UPDATE_EMAIL_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-384EAB05-051E-4129-8E94-2A249EE6238F)
- [UPDATE_SENDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_em_email.html#ADSDK-GUID-60D88FF8-B83E-4E66-9C14-005A78B1B691)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
