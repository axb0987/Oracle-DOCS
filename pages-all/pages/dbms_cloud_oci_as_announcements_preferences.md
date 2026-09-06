# Announcements Preferences Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#dcoc-content-body)

## Announcements Preferences Functions

Package: DBMS_CLOUD_OCI_AS_ANNOUNCEMENTS_PREFERENCES

### CREATE_ANNOUNCEMENTS_PREFERENCE Function

Creates a request that specifies preferences for the tenancy regarding receiving announcements by email. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcements_preference_details`

(required) The object that contains details about tenancy preferences for receiving announcements by email.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`opc_retry_token`

(optional) Idempotency token

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ANNOUNCEMENTS_PREFERENCE Function

Gets the current preferences of the tenancy regarding receiving announcements by email. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`preference_id`

(required) The ID of the preference.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ANNOUNCEMENTS_PREFERENCES Function

Gets the current preferences of the tenancy regarding receiving announcements by email. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ANNOUNCEMENTS_PREFERENCE Function

Updates the preferences of the tenancy regarding receiving announcements by email. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`preference_id`

(required) The ID of the preference.

`announcements_preference_details`

(required) The object that contains details about tenancy preferences for receiving announcements by email.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Announcements Preferences Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#ADSDK-GUID-8730713E-668E-4F24-807D-57D7263A4DD3)
- [CREATE_ANNOUNCEMENTS_PREFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#ADSDK-GUID-E56BD6DD-4428-42B6-9033-0B9C665D4FE1)
- [GET_ANNOUNCEMENTS_PREFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#ADSDK-GUID-70314605-F82B-4210-92BC-63388B351FD1)
- [LIST_ANNOUNCEMENTS_PREFERENCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#ADSDK-GUID-92BC399D-D2CB-4CB4-8D4E-A8A20B1C1B99)
- [UPDATE_ANNOUNCEMENTS_PREFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcements_preferences.html#ADSDK-GUID-B79AD128-99C2-42B7-B494-2CE48BA9FB45)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
