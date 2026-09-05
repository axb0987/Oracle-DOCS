# Deleting a Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_ekms_private_endpoint.htm
- Fetched: 2026-09-05 02:34 CDT

# Deleting a Private Endpoint

Learn how to delete an External Key Management private endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_ekms_private_endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_ekms_private_endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_ekms_private_endpoint.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Private Endpoints .
- On the Private Endpoints page, find a private endpoint in the list and select the Actions menu (three dots) for the Private Endpoint entry in the list.
- Select Delete .
- In the Confirm dialog box, select Delete to confirm.
- 

Use the[oci kms ekm ekms-private-endpoint delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/ekm/ekms-private-endpoint/delete.html)command to delete a private endpoint:

```

```

Example
```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[DeleteEkmsPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/key/latest/EkmsPrivateEndpoint/DeleteEkmsPrivateEndpoint)API to delete a private endpoint in the OCI External Key Management Service (EKMS).
Note  
  
Each region has a unique endpoint for create, update, and list operations for secrets. This endpoint is referred to as the control plane URL or secret management endpoint. Each region also has a unique endpoint for operations related to retrieving secret contents. This endpoint is known as the data plane URL or the secret retrieval endpoint. For regional endpoints, see the[API Documentation](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
