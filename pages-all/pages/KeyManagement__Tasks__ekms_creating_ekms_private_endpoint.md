# Creating a Private Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm
- Fetched: 2026-09-05 02:34 CDT

# Creating a Private Endpoint

Learn how to create a private endpoint in a VCN so that the external key manager can access the OCI External Key Management Service (EKMS).
Note  
  
Ensure you explicitly delete failed Private Endpoints to avoid memory allocation issues. If a memory allocation issue persists, it might limit exhaustion even when no active private endpoints exist.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Private Endpoints .
- In the Private Endpoints page, select Create private endpoint .
- In the Create Private Endpoint workflow, provide the following details:

- Type: Use "External." This is the only endpoint type that OCI KMS supports.
- Name: Enter a name for the external key management private endpoint.
- Description: Provide a short description.
- Virtual Private Network: Select a VCN from the dropdown list.
- Subnet: Select the subnet or confirm the displayed value for the VCN you are using.
- External Key Manager Private IP: Based on your TLS connectivity configuration, provide either the static IP address of the external key manager, or the API Gateway private IP address.
- External Key Manager Port: Enter the external key management resource port number. For static IP address based TLS connectivity, provide the port number of external key manager server. For example, 443. For FQDN based TLS connectivity, leave the field blank.
- Certificate: Use Upload Certificate or Paste Certificate to provide the Key Management CA bundle. The external CA is a PEM-formatted certificate file. .
Note  
  
Based on your TLS connectivity configuration, use the CA bundle of the external key manager or the OCI API Gateway.
- Select Create .

After you create a private endpoint for external key management, you can access the Private Endpoint Details page and confirm that the endpoint in the "ACTIVE" state.
- 

Use the[oci kms ekm ekms-private-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/ekm/ekms-private-endpoint/create.html)command to create a new private endpoint:

```

```

For example:
```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateEkmsPrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/key/latest/EkmsPrivateEndpoint/CreateEkmsPrivateEndpoint)API to create private endpoint for connecting OCI External Key Management to an external key management system.
Note  
  
Each region has a unique endpoint for create, update, and list operations for secrets. This endpoint is referred to as the control plane URL or secret management endpoint. Each region also has a unique endpoint for operations related to retrieving secret contents. This endpoint is known as the data plane URL or the secret retrieval endpoint. For regional endpoints, see the[API Documentation](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
