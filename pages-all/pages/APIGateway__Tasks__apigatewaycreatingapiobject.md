# Creating an API Resource with an API Description
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm
- Fetched: 2026-09-05 01:37 CDT

# Creating an API Resource with an API Description

Find out how to create an API resource with the API Gateway service that you can use to deploy an API on an API gateway.

When using the API Gateway service, you have the option to create an API resource. You can use the API resource to deploy an API on an API gateway. The API resource has an API description that describes the API.

If you use an API resource to deploy an API on an API gateway, its API description prepopulates some of the properties of the API deployment specification.

You can optionally import the API description from a file (sometimes called an 'API specification', or 'API spec') written in a supported language. Currently, OpenAPI Specification version 2.0 (formerly Swagger Specification 2.0) and version 3.0 are supported.

Note that creating an API resource in the API Gateway service is optional. You can deploy an API on an API gateway without creating an API resource in the API Gateway service. Note also that you can create an API resource that doesn't have an API description initially, and then add an API description later.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingapiobject.htm#)
- 

- On the APIs list page, select Create API . If you need help finding the list page, see[Listing API Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm).
- 

Specify the following values for the API resource:
- Name: The name of the API resource. Avoid entering confidential information.
- Compartment: The compartment in which to create the API resource.
- Upload API description file: (Optional) A file that contains the API description (in a supported language) to upload and from which to create the API description. The file can be up to 1 MB in size. The file is parsed to confirm that it's in a supported language and correctly formatted. Currently, OpenAPI Specification version 2.0 (formerly Swagger Specification 2.0) and version 3.0 files are supported.
- Tags: Select this option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Create to create the API resource.

If you uploaded an API description file, an API description is created and validated. It can take a few minutes to validate the API description. While it is being validated, the API description is shown with a state of Validating on the Validatity tab. When the API description has been validated successfully, the following actions occur:
- The API description field on the Details tab shows the API description created from the API description file.
- The Validity tab shows successful validation.
- The Details tab shows any additional information about the default API deployment specification created from the API description.

Note that rather than creating the API resource immediately, you can create it later by using Resource Manager and Terraform. Select Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the API description to be shown as Valid (or if the API description validation operation has failed), follow these steps:
- Select the name of the API resource on the APIs list page, and select the Work requests tab to see an overview of the API description validation operation.
- Select the Validate API operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the API description validation operation has failed and you can't diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).
- 

If you didn't upload an API description file when you first created the API resource, or if you subsequently want to upload a different API description file, follow these steps:
- On the APIs page, select Edit from the Actions menu (three dots) for the API resource.
- Provide details of the API description file from which to create the API description.

After you have successfully created an API resource with an API description, you can deploy it on an API gateway. See[Using the Console to Create an API Deployment from an API Resource](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm#consoleapiresouce).
- 

To create an API resource using the CLI, follow these steps:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- Open a command prompt and run`oci api-gateway api create`to create the API resource:

```

```

where:
- `<api-name>`is the name of the new API resource. Avoid entering confidential information.
- `<compartment-ocid>`is the OCID of the compartment to which the new API resource will belong.
- `<api-description>`is optionally an API description (in a supported language). The value you specify for`<api-description>`can be:
- The entire API description, enclosed within double quotes. Inside the description, each double quote must be escaped with a backslash (\) character. For example (and abbreviated for readability),`--content "swagger:\"2.0\",title:\"Sample API\",..."`
- The name and location of an API description file, enclosed within double quotes and in the format`"$(< <path>/<filename>.yaml)"`. For example,`--content "$(< /users/jdoe/api.yaml)"`The description is parsed to confirm that it is in a supported language and correctly formatted. Currently, OpenAPI Specification version 2.0 (formerly Swagger Specification 2.0) and version 3.0 files are supported.

For example:

```

```

The response to the command includes:
- The API resource's OCID.
- The lifecycle state (for example, SUCCEEDED, FAILED).
- The id of the work request to create the API resource (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API resource has been created (or the request has failed), include either or both the following parameters:
- `--wait-for-state SUCCEEDED`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the API resource until the work request has successfully created it.
- 

(Optional) To see the status of the work request that is creating the API resource, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the API resource, enter:

```

```

- 

(Optional) If the work request that is creating the API resource fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[CreateAPI](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Api/CreateApi)
