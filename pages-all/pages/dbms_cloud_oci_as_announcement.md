# Announcement Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#dcoc-content-body)

## Announcement Functions

Package: DBMS_CLOUD_OCI_AS_ANNOUNCEMENT

### GET_ANNOUNCEMENT Function

Gets the details of a specific announcement. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_id`

(required) The OCID of the announcement.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ANNOUNCEMENT_USER_STATUS Function

Gets information about whether a specific announcement was acknowledged by a user. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_id`

(required) The OCID of the announcement.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ANNOUNCEMENTS Function

Gets a list of announcements for the current tenancy. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

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

`announcement_type`

(optional) The type of announcement.

`lifecycle_state`

(optional) The announcement's current lifecycle state.

Allowed values are: 'ACTIVE', 'INACTIVE'

`is_banner`

(optional) Whether the announcement is displayed as a console banner.

`sort_by`

(optional) The criteria to sort by. You can specify only one sort order.

Allowed values are: 'timeOneValue', 'timeTwoValue', 'timeCreated', 'referenceTicketNumber', 'summary', 'announcementType'

`sort_order`

(optional) The sort order to use. (Sorting by `announcementType` orders the announcements list according to importance.)

Allowed values are: 'ASC', 'DESC'

`time_one_earliest_time`

(optional) The boundary for the earliest `timeOneValue` date on announcements that you want to see.

`time_one_latest_time`

(optional) The boundary for the latest `timeOneValue` date on announcements that you want to see.

`environment_name`

(optional) A filter to return only announcements that match a specific environment name.

`service`

(optional) A filter to return only announcements affecting a specific service.

`platform_type`

(optional) A filter to return only announcements affecting a specific platform.

Allowed values are: 'IAAS', 'SAAS'

`exclude_announcement_types`

(optional) Exclude The type of announcement.

`should_show_only_latest_in_chain`

(optional) A filter to display only the latest announcement in a chain.

`chain_id`

(optional) A filter to return only announcements belonging to the specified announcement chain ID.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ANNOUNCEMENT_USER_STATUS Function

Updates the status of the specified announcement with regard to whether it has been marked as read. This call is subject to an Announcements limit that applies to the total number of requests across all read or write operations. Announcements might throttle this call to reject an otherwise valid request when the total rate of operations exceeds 20 requests per second for a given user. The service might also throttle this call to reject an otherwise valid request when the total rate of operations exceeds 100 requests per second for a given tenancy.

Syntax
```

```

Parameters

Parameter Description

`announcement_id`

(required) The OCID of the announcement.

`status_details`

(required) The information to use to update the announcement's read status.

`if_match`

(optional) The locking version, used for optimistic concurrency control.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the complete request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://announcements.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Announcement Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#ADSDK-GUID-69C7E884-42F0-48F8-871E-9DD4A189671D)
- [GET_ANNOUNCEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#ADSDK-GUID-36C988B8-F749-4BF7-8A1C-3B2220617A35)
- [GET_ANNOUNCEMENT_USER_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#ADSDK-GUID-25CC9E0C-40D9-4D83-A518-D40CF8E55E66)
- [LIST_ANNOUNCEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#ADSDK-GUID-6659AE89-CA56-477D-BD72-6C38B2F05194)
- [UPDATE_ANNOUNCEMENT_USER_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_as_announcement.html#ADSDK-GUID-C9A3F350-C9D6-48EA-AD38-BABB6E4C5D5E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
