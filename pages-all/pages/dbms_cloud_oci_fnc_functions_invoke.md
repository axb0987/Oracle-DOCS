# Functions Invoke Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_invoke.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_invoke.html#dcoc-content-body)

## Functions Invoke Functions

Package: DBMS_CLOUD_OCI_FNC_FUNCTIONS_INVOKE

### INVOKE_FUNCTION Function

Invokes a function

Syntax
```

```

Parameters

Parameter Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this function.

`invoke_function_body`

(optional) The body of the function invocation. Note: The maximum size of the request is limited. This limit is currently 6MB and the endpoint will not accept requests that are bigger than this limit.

`fn_intent`

(optional) An optional intent header that indicates to the FDK the way the event should be interpreted. E.g. 'httprequest', 'cloudevent'.

Allowed values are: 'httprequest', 'cloudevent'

`fn_invoke_type`

(optional) Indicates whether Oracle Functions should execute the request and return the result ('sync') of the execution, or whether Oracle Functions should return as soon as processing has begun ('detached') and leave result handling to the function.

Allowed values are: 'detached', 'sync'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Functions Invoke Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_invoke.html#ADSDK-GUID-6BF702BE-F100-492F-81A1-820F93421AC0)
- [INVOKE_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_invoke.html#ADSDK-GUID-EE3C29B3-5F5F-4DBE-B686-359275500AB2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
