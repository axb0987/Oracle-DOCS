# Resource Search Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#dcoc-content-body)

## Resource Search Common Types

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_ERROR_T Type

The representation of an error.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_SEARCH_DETAILS_T Type

A base request type that contains common criteria for searching for resources.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of SearchDetails, whether `FreeText` or `Structured`.

`matching_context_type`

(optional) The type of matching context returned in the response. If you specify `HIGHLIGHTS`, then the service will highlight fragments in its response. (For more information, see ResourceSummary.searchContext and SearchContext.) The default setting is `NONE`.

Allowed values are: 'NONE', 'HIGHLIGHTS'

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_FREE_TEXT_SEARCH_DETAILS_T Type

A request containing arbitrary text that must be present in the resource.

Syntax
```

```

`dbms_cloud_oci_resource_search_free_text_search_details_t`is a subtype of the`dbms_cloud_oci_resource_search_search_details_t`type.

Fields

Field Description

`text`

(required) The text to search for.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_ABS_T

An individual field that can be used as part of a query filter.

Syntax
```

```

Fields

Field Description

`field_type`

(required) The type of the field, which dictates what semantics and query constraints you can use when searching or querying.

Allowed values are: 'IDENTIFIER', 'STRING', 'INTEGER', 'RATIONAL', 'BOOLEAN', 'DATETIME', 'IP', 'OBJECT'

`field_name`

(required) The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.

`is_array`

(optional) Indicates that this field is actually an array of the specified field type.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_ABS_TBL Type

Nested table type of dbms_cloud_oci_resource_search_queryable_field_description_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_T Type

An individual field that can be used as part of a query filter.

Syntax
```

```

Fields

Field Description

`object_properties`

(optional) If the field type is `OBJECT`, then this property will provide all the individual properties of the object that can be queried.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_TBL Type

Nested table type of dbms_cloud_oci_resource_search_queryable_field_description_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_SEARCH_CONTEXT_T Type

Contains search context, such as highlighting, for found resources.

Syntax
```

```

Fields

Field Description

`highlights`

(optional) Describes what in each field matched the search criteria by showing highlighted values, but only for free text searches or for structured queries that use a MATCHING clause. The list of strings represents fragments of values that matched the query conditions. Highlighted values are wrapped with &amp;lt;h1&amp;gt;..&amp;lt;/h1&amp;gt; tags. All values are HTML-encoded (except &amp;lt;h1&amp;gt; tags).

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_T Type

A resource that exists in the cloud network that you're querying.

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The resource type name.

`identifier`

(required) The unique identifier for this particular resource, usually an OCID.

`compartment_id`

(required) The OCID of the compartment that contains this resource.

`time_created`

(optional) The time that this resource was created.

`display_name`

(optional) The display name (or name) of this resource, if one exists.

`availability_domain`

(optional) The availability domain where this resource exists, if applicable.

`lifecycle_state`

(optional) The lifecycle state of this resource, if applicable.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) System tags associated with this resource, if any. System tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`search_context`

(optional)

`identity_context`

(optional) Additional identifiers to use together in a \"Get\" request for a specified resource, only required for resource types that explicitly cannot be retrieved by using a single identifier, such as the resource's OCID.

`additional_details`

(optional) Additional resource attribute fields of this resource that match queries with a return clause, if any. For example, if you ran a query to find the private IP addresses, public IP addresses, and isPrimary field of the VNIC attachment on instance resources, that field would be included in the ResourceSummary object as: {\"additionalDetails\": {\"attachedVnic\": [{\"publicIP\" : \"172.110.110.110\",\"privateIP\" : \"10.10.10.10\",\"isPrimary\" : true}, {\"publicIP\" : \"172.110.110.111\",\"privateIP\" : \"10.10.10.11\",\"isPrimary\" : false}]}. The structure of the additional details attribute fields depends on the matching resource.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_resource_search_resource_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_COLLECTION_T Type

A summary representation of resources that matched the search criteria.

Syntax
```

```

Fields

Field Description

`items`

(optional) A list of resources.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_TYPE_T Type

Defines a type of resource that you can find with a search or query.

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name of the resource type, which matches the value returned as part of the ResourceSummary object.

`fields`

(required) List of all the fields and their value type that are indexed for querying.

### DBMS_CLOUD_OCI_RESOURCE_SEARCH_STRUCTURED_SEARCH_DETAILS_T Type

A request that uses Search's structured query language to specify filter conditions to apply to search results. For more information about writing queries, see[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).

Syntax
```

```

`dbms_cloud_oci_resource_search_structured_search_details_t`is a subtype of the`dbms_cloud_oci_resource_search_search_details_t`type.

Fields

Field Description

`query`

(required) The structured query describing which resources to search for.

- [Resource Search Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-C508CF49-2092-45FC-B350-10057D1C9B08)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-1CCB15FA-FB5A-484D-A6EA-BD436964081A)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-10DBBE8F-3078-48DB-BCC9-3877B791F334)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-4B1B3C10-6D4B-4DE0-BFC1-74DD7C87FD24)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_FREE_TEXT_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-63420011-82D3-4373-94C1-77A6AE4811A3)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-B9FD9B86-CF1A-4A62-A8A2-6DDB90E5C5D0)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-7334DCF6-C4D0-47F6-BE4C-9395709025E1)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-4B263657-7EC1-4458-A27C-33813E79428D)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_QUERYABLE_FIELD_DESCRIPTION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-B7A36EB2-77D7-47B9-888A-DDF92196E547)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_SEARCH_CONTEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-67DBFB70-EA05-42D0-91BC-FF34D917AFD2)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-8FB31CAF-3381-482F-8889-E389A29CD2FA)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-368A4354-A984-4630-B18C-3F33EB02B20E)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-8A92BB75-D03D-4FE9-A4DA-27E05018C6AF)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-E8296B3E-29CF-4DB0-AA09-8B010FB6199D)
- [DBMS_CLOUD_OCI_RESOURCE_SEARCH_STRUCTURED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/resource_search_t.html#ADSDK-GUID-A3CFCB99-08F2-4FA3-8073-CB806FD432B8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
