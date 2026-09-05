# Customizing Trust Stores for TLS Certificate Verification
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm
- Fetched: 2026-09-05 01:38 CDT

# Customizing Trust Stores for TLS Certificate Verification

Find out how to add Certificate Authorities (CAs) and CA bundles to custom trust stores with API Gateway.

The API gateways you create with the API Gateway service verify TLS certificates presented to them using a trust store. The trust store can contain Certificate Authority (CA) root certificates, and CA bundles of root and intermediate certificates. A default CA bundle is added to each API gateway's trust store, containing certificates of well-known public CAs. The default CA bundle enables the API gateway to verify TLS certificates presented by back-end services.

In addition to the default CA bundle, you can choose to add the root certificates of other CAs, and other CA bundles, to an API gateway's trust store. These additional CAs and CA bundles are referred to as custom CAs and custom CA bundles. To add a custom CA or CA bundle to an API gateway's trust store, you have to first create a CA resource or CA bundle resource in the Certificates service. Having created the resource in the Certificates service, you can then add it to the API gateway's trust store. Adding custom CAs and CA bundles enables you to customize the trust store to meet your requirements.

Having added custom CAs and CA bundles to the trust store, TLS connections to the API gateway (including from HTTPS back ends, and from the response cache) are verified using both the default CA bundle, and the custom CAs and CA bundles. In addition, if you have specified mTLS support for an API deployment, the API gateway uses custom CAs and custom CA bundles to verify API client certificates. Note that the API gateway does not use the default CA bundle to verify API client certificates during an mTLS handshake. So if you want an API gateway to support mTLS, you must add custom CAs and CA bundles to the API gateway's trust store

For some customers, it's obligatory for security reasons to use custom trust stores that contain only private CAs, and no public CAs. For other customers, use of custom trust stores is likely to be driven by commercial requirements.

## Adding Custom CAs and CA Bundles to an API Gateway's Trust Store

To customize an API gateway's trust store by adding a custom Certificate Authority (CA) or CA bundle, first create a Certificate Authority (CA) resource or CA bundle resource in the Certificates service, and then add it to the API gateway's trust store.

[Step 1: Create a CA Resource and/or a CA Bundle Resource in Certificates Service](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm#)

Follow the instructions in the Certificates service documentation to create a Certificate Authority (CA) resource and/or a CA bundle resource
- [Creating a Certificate Authority](https://docs.oracle.com/iaas/Content/certificates/creating-certificate-authority.htm)
- [Creating a CA bundle](https://docs.oracle.com/iaas/Content/certificates/creating-CAbundle.htm)

[Step 2: Add the CA Resource or CA Bundle resource to an API Gateway's Trust Store](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm#)

To add a Certificate Authority (CA) resource or CA bundle resource to an API gateway's trust store when creating or updating the API gateway:
- Follow the instructions in[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)or[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm)to create or update an API gateway using either the Console or the CLI.
- 

Specify the CA resource and/or CA bundle resource from the Certificates service to add to the API gateway's trust store, as described in the following instructions:
- If using the Console: In the Advanced options section of the Create gateway or Edit gateway dialog, select Additional certificate authorities and select one or more CA resources or CA bundle resources to add to the API gateway's trust store as custom CAs and custom CA bundles (in addition to the default CA bundle).
- If using the CLI: Set the`--ca-bundles file:///<filename>`argument to the name of a file containing details of one or more CA resources or CA bundle resources to add to the API gateway's trust store as custom CAs and custom CA bundles (in addition to the default CA bundle). Specify the details in valid JSON, in the following format:

```

```

The API Gateway service creates or updates the API gateway with a trust store containing the custom CA and/or CA bundle that you specified, in addition to the default CA bundle.

## Removing Custom CAs and CA Bundles from an API Gateway's Trust Store

Having added a custom Certificate Authority (CA) or CA bundle to an API gateway's trust store, you might decide that the CA or CA bundle is no longer required.

You can remove some or all custom CAs and CA bundles from an API gateway's trust store, provided there are no mTLS-enabled APIs deployed on the API gateway. If there are one or more mTLS-enabled APIs deployed on the API gateway, there must always be at least one custom CA or CA bundle in the API gateway's trust store.

### Using the Console

To remove a custom CA or CA bundle from an API gateway's trust store using the Console:
- On the Gateways list page, select the API gateway from which you want to remove the custom CA or CA bundle. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- Select the Certificate authorities tab to see the custom CA and CA bundles in the API gateway's trust store.
- 

Select the Actions menu (three dots) beside the custom CA or CA bundle you want to remove, and select Remove .

Note that you cannot remove all custom CAs and CA bundles from an API gateway's trust store if there are one or more mTLS-enabled APIs deployed on the API gateway.
- 

Confirm that you want to remove the custom CA or CA bundle from the API gateway's trust store.

### Using the CLI

To remove a custom CA or CA bundle from an API gateway's trust store using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To remove a custom CA or CA bundle from an API gateway's trust store:
- 

Open a command prompt and run`oci api-gateway gateway update`to remove the custom CA or CA bundle from the API gateway's trust store:

```

```

where`<filename>`is the name of a file containing details of just those custom CAs and custom CA bundles to retain in the API gateway's trust store (in addition to the default CA bundle). Any CAs or CA bundles not contained in the file are removed from the trust store.

For example:

```

```

Note that you cannot remove all custom CAs and CA bundles from an API gateway's trust store if there are one or more mTLS-enabled APIs deployed on the API gateway.

The response to the command includes:
- The lifecycle state (for example, DELETED, FAILED).
- The id of the work request to remove the custom CAs or CA bundles (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the custom CAs or CA bundles have been removed (or the request has failed), include either or both the following parameters:
- `--wait-for-state DELETED`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is removing the custom CA or CA bundle, enter:

```

```

- 

(Optional) To view the logs of the work request that is removing the custom CA or CA bundle, enter:

```

```

- 

(Optional) If the work request that is removing the custom CA or CA bundle fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the custom CA or CA bundle has been removed from the API gateway's trust store, enter the following command and confirm that the custom CA or CA bundle is no longer shown:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

### Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateGateway](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/UpdateGateway)
