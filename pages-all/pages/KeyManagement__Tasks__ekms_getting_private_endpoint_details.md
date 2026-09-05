# Getting Private Endpoint Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_getting_private_endpoint_details.htm
- Fetched: 2026-09-05 02:34 CDT

# Getting Private Endpoint Details

Get information about the external key manager private endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_getting_private_endpoint_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_getting_private_endpoint_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_getting_private_endpoint_details.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Private Endpoints .
- In the Private Endpoints page, select a private endpoint name to open its details page.
The Private Endpoint Information section displays the following information:
- Compartment: The name of the compartment that contains the private endpoint.
- OCID: The unique, Oracle-assigned ID of the vault.
- Created: The date and time when you initially created the private endpoint.
- Update: The date and time when you updated the private endpoint.
- VCN: VCN identifier.
- Subnet: Subnet identifier.
- External Key Manager IP address: IP address identifier for the external key manager.
- External Key Manager Port: Port identifier for the external key manager.
- 

Use the[oci kms ekm ekms-private-endpoint get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/ekm/ekms-private-endpoint/get.html)command to get private endpoint details:

```

```

For example:
```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetEkmsPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/key/latest/EkmsPrivateEndpoint/GetEkmsPrivateEndpoint)API to get private endpoint details for the private endpoint used for connecting the OCI External Key Management Service (EKMS) to an external key management system.
Note  
  
Each region has a unique endpoint for create, update, and list operations for secrets. This endpoint is referred to as the control plane URL or secret management endpoint. Each region also has a unique endpoint for operations related to retrieving secret contents. This endpoint is known as the data plane URL or the secret retrieval endpoint. For regional endpoints, see the[API Documentation](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
