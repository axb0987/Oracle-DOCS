# Updating Private Endpoint Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_modifying_ekms_private_endpoint.htm
- Fetched: 2026-09-05 02:34 CDT

# Updating Private Endpoint Details

Learn how to update the details of an OCI External Key Management private endpoint.

You can update the display name and tags an External Key Management private endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_modifying_ekms_private_endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_modifying_ekms_private_endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_modifying_ekms_private_endpoint.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Private Endpoints .
- Find the Private Endpoints you want to update in the list and select the Actions menu (three dots) .
- Select Edit .
- On the Edit Private Endpoint page, update the private endpoint name.
- Select Submit .

After you change an External Key Management private endpoint, you can access the Private Endpoint Details page to see the endpoint in "ACTIVE" state. You can use the actions at the page top to rename, move resource, add tags or delete the endpoint.
- 

Use the[oci kms ekm ekms-private-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/3.63.3/oci_cli_docs/cmdref/kms/ekm/ekms-private-endpoint/update.html)to update a private endpoint.

```

```

Example
```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateEkmsPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/key/latest/EkmsPrivateEndpoint/UpdateEkmsPrivateEndpoint)API to update the private endpoint used for connecting the OCI External Key Management Service (EKMS) to an external key management system.
Note  
  
Each region has a unique endpoint for create, update, and list operations for secrets. This endpoint is referred to as the control plane URL or secret management endpoint. Each region also has a unique endpoint for operations related to retrieving secret contents. This endpoint is known as the data plane URL or the secret retrieval endpoint. For regional endpoints, see the[API Documentation](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
