# Updating an API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm
- Fetched: 2026-09-05 01:39 CDT

# Updating an API Gateway

Find out how to modify API gateways that you previously created with the API Gateway service.

After you have created an API gateway, you might decide to change the API gateway. For example, you might want to change the API gateway's name or the tags applied to it.

Note that there are some properties of API gateways for which you can't change the original values.

You can update API gateways by using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm#)
- 

- On the Gateways list page, find the API gateway that you want to update. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- From the Actions menu (three dots) for the API gateway:
- Select Edit to change any of the following API gateway properties:
- Change the API gateway's name. Avoid entering confidential information.
- Change the TLS certificate and domain name used by the API gateway. Note that API Gateway certificate resources and Certificates service certificate resources are shown only if they are available in the selected compartment. See[Setting Up Custom Domains and TLS Certificates](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm).
- Enable or disable the use of network security groups (NSGs) to control access to and from the API gateway by using security rules defined for the NSGs that you specify (up to a maximum of five network security groups). You can use security rules defined for NSGs instead of, or in addition to, those defined for security lists. NSGs can belong to the same compartment as the API gateway, but don't have to. See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
- Change response cache configuration settings. See[Caching Responses to Improve Performance](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm).
- Change the Certificate Authorities (CAs) and CA bundles included in the API gateway's trust store as custom CAs and custom CA bundles (in addition to the default CA bundle). See[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm).
- Select Move resource to move the API gateway to a different compartment.
- Select Manage tags to view and edit the tags applied to the API gateway, and select Add tag to apply more tags to the API gateway.
- 

To update existing API gateways using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To update an existing API gateway:
- 

Open a command prompt and run`oci api-gateway gateway update`to update the API gateway:

```

```

where:
- `<gateway-ocid>`is the OCID of the API gateway to update. To find out the API gateway's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- `<property-to-update>`is the property to update. Note that you can only change the values for`display-name`,`--response-cache-details`,`--network-security-group-ids`,`--ca-bundles`,`freeform-tags`and`defined-tags`(and`certificate-id>`if this was originally set for the API gateway). All other values must be identical to values in the original gateway definition.
- `<property-value>`is the new value of the property you want to change.

For example:

```

```

The response to the command includes:
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to update the API gateway (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API gateway is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is updating the API gateway, enter:

```

```

- 

(Optional) To view the logs of the work request that is updating the API gateway, enter:

```

```

- 

(Optional) If the work request that is updating the API gateway fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API gateway has been updated, enter the following command and confirm that the API gateway's properties are as you expect:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[UpdateGateway](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/UpdateGateway)
