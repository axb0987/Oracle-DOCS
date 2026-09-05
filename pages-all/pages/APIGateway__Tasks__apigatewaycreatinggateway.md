# Creating an API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm
- Fetched: 2026-09-05 01:37 CDT

# Creating an API Gateway

Find out how to create an API gateway with the API Gateway service to process traffic from front-end clients and route it to back-end services.

You can create one or more API gateways to process traffic from API clients and route it to back-end services. After you create an API gateway, you then deploy an API on the API gateway by creating an API deployment.

You can use a single API gateway as the front end for multiple back-end services in the following ways:
- Create a single API deployment on the API gateway, with an API deployment specification that defines multiple back-end services.
- Create multiple API deployments on the same API gateway, each with an API deployment specification that defines one (or more) back-end services.

Having a single API gateway as a front end enables you to present a single cohesive API to API consumers and API clients, even if the API actually consists of smaller microservices written by different software teams using different programming languages or technologies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm#)
- 

- On the Gateways list page, select Create Gateway . If you need help finding the list page, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- 

Specify the following values for the new API gateway:
- Name: The name of the API gateway. Avoid entering confidential information.
- Compartment: The compartment in which to create the API gateway.
- Certificate: The TLS certificate that the API gateway uses. The TLS certificate that you select determines the API gateway's domain name.
- Default (*.oci.customer-oci.com) (if shown): Select this option if you want the domain name to be generated automatically for you, and you want the API gateway to use a default TLS certificate obtained by the API Gateway service. The generated default domain name will contain a random string of characters followed by`.apigateway.<region-identifier>.oci.customer-oci.com`. For example,`laksjd.apigateway.us-phoenix-1.oci.customer-oci.com`. This option is only available if your tenancy exists in the OC1 realm.
- Certificates Service category (if shown): Select an existing Certificates service certificate resource that contains the details of the custom TLS certificate that you want the API gateway to use. The API gateway uses a custom domain name associated with the certificate that you select. This category is shown only if Certificates service certificate resources are available in the selected Certificate compartment .
- API Gateway Certificates category (if shown): Select an existing API Gateway certificate resource that contains the details of the custom TLS certificate that you want the API gateway to use. The API gateway uses a custom domain name associated with the certificate you select. This category is shown only if API Gateway certificate resources are available in the selected Certificate compartment .

See[Setting Up Custom Domains and TLS Certificates](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm).
Note  
  

We recommend using a custom TLS certificate for public or production systems. We recommend using a default TLS certificate obtained by the API Gateway service only for private or non-production systems (for example, for development and testing).
- Type: The type of API gateway to create.
- Select Private if you only want the API gateway (and the APIs deployed on it) to be accessible by resources in the same private network (VCN), or by resources in other private or on-premise networks peered to that private network.
- Select Public if you want the API gateway (and the APIs deployed on it) to be publicly accessible. Public API gateways can be reached from the internet, provided an internet gateway is present in the API gateway's VCN.
- Virtual cloud network: The VCN in which to create the API gateway, from the list of VCNs in the specified compartment. The VCN can be in the same compartment as the API gateway, but doesn't have to be.
- Subnet: The public or private regional subnet in which to create the API gateway, from the list of subnets in the specified compartment. If you want to create a public API gateway, you must specify a public regional subnet.

Be aware that API Gateway communicates on port 443, which is not open by default. You have to add a new stateful ingress security rule for the regional subnet (either in a security list or in a network security group) to allow traffic on port 443. For the properties of the ingress security rule, see[Create a VCN to Use with API Gateway, If One Doesn't Already Exist](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingvcn.htm).
- Enable network security groups: Select this option to control access to and from the API gateway by using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five network security groups). You can use security rules defined for NSGs instead of, or in addition to, those defined for security lists. NSGs can belong to the same compartment as the new API gateway, but don't have to. See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
- Optionally, select Advanced options and specify the following values:
- Response caching: Options to enable and configure response caching for the API gateway to improve performance and reduce load on back-end services. See[Caching Responses to Improve Performance](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm).
- Certificate authorities: One or more Certificate Authority (CA) resources or CA bundle resources to add to the API gateway's trust store as custom CAs and custom CA bundles (in addition to the default CA bundle). Custom CAs and custom CA bundles are used to verify TLS certificates presented by API clients and back-end services. See[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm).
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
Note  
  
If you apply a defined tag to an API gateway (either directly or as a tag default for a compartment) and subsequently modify the tag definition, the API gateway can enter a failed state. Apply a defined tag to an API gateway only if the defined tag isn't going to change. If you're not sure whether a defined tag will change, we recommend that you don't apply it to an API gateway.
- 

Select Create to create the API gateway immediately.

Be aware that it can take a few minutes to create the new API gateway. While it is being created, the API gateway is shown with a state of Creating. When it has been created successfully, the API gateway is shown with a state of Active.

Also note that rather than creating the new API gateway immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the API gateway to be shown with an Active state (or if the API gateway creation operation has failed), perform the following actions:
- Select the name of the API gateway on the Gateways list page, and select the Work requests tab to see an overview of the API gateway creation operation.
- Select the Create gateway operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the API gateway creation operation has failed and you can't diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).

After you successfully create an API gateway, you can deploy an API on it. See[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
- 

To create a new API gateway using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway gateway create`to create the API gateway:

```

```

where:
- `<gateway-name>`is the name of the new API gateway. Avoid entering confidential information.
- `<compartment-ocid>`is the OCID of the compartment to which the new API gateway will belong.
- `<gateway-type>`is the type of API gateway to create. Specify`PRIVATE`if you only want the API gateway (and the APIs deployed on it) to be accessible by resources in the same private network (VCN), or by resources in other private or on-premise networks peered to that private network. Specify`PUBLIC`if you want the API gateway (and the APIs deployed on it) to be publicly accessible. Public API gateways can be reached from the internet, provided an internet gateway is present in the API gateway's VCN.
- `<subnet-ocid>`is the OCID of a public or private regional subnet in which to create the API gateway. If you want to create a public API gateway, you must specify a public regional subnet.

Note that API Gateway communicates on port 443, which is not open by default. You have to add a new stateful ingress security rule for the regional subnet (either in a security list or in a network security group) to allow traffic on port 443. For the properties of the ingress security rule, see[Create a VCN to Use with API Gateway, If One Doesn't Already Exist](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingvcn.htm).
- `--network-security-group-ids <nsg-ocids>`(optional) is the OCID of one or more network security groups. The value of`<nsg-ocids>`must be in valid JSON format (either as a string, or passed in as a file using the`file:///<filename>`syntax including a path).
- `<certificate-ocid>`(optional) is the OCID of the certificate resource created for the API gateway's custom TLS certificate (either an API Gateway certificate resource or a Certificates service certificate resource). See[Setting Up Custom Domains and TLS Certificates](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm).
- `--ca-bundles file:///<filename>`(optional) is a file containing details of one or more Certificate Authority (CA) resources or CA bundle resources to add to the API gateway's trust store as custom CAs and custom CA bundles (in addition to the default CA bundle). Custom CAs and custom CA bundles are used to verify TLS certificates presented by API clients and back-end services. See[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm).
- `--response-cache-details file:///<filename>`(optional) is the cache configuration file, including a path, to enable and configure response caching. See[Caching Responses to Improve Performance](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm).

For example:

```

```

The response to the command includes:
- The API gateway's OCID.
- 

The host name, as the domain name to use when calling an API deployed on the API gateway. If you didn't specify a certificate resource when creating the API gateway, a domain name is automatically generated in the format`<gateway-identifier>.apigateway.<region-identifier>.oci.customer-oci.com`, where:
- `<gateway-identifier>`is a string of characters that identifies the API gateway. For example,`lak...sjd`(abbreviated for readability).
- `<region-identifier>`is the identifier of the region in which the API gateway has been created. See[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayprerequisites.htm#regional-availability).

For example,`lak...sjd.apigateway.us-phoenix-1.oci.customer-oci.com`.
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to create the API gateway (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API gateway is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the API gateway until the work request has successfully created it and the API gateway is active.
- 

(Optional) To see the status of the API gateway, enter:

```

```

- 

(Optional) To see the status of the work request that is creating the API gateway, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the API gateway, enter:

```

```

- 

(Optional) If the work request that is creating the API gateway fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[CreateGateway](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/CreateGateway)
