# Listing API Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing API Resources

Find out how to list existing API resources with the API Gateway service.

Having created API resources, you might need to list the existing API resources. For example, you might want to see which API resources have been successfully validated.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-apis.htm#)
- 

- Open the navigation menu and select Developer Services . Under API Management , select APIs .

The APIs list page opens. All API resources in the selected compartment are displayed in a table.
- To view the API resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To see more detail about an individual API resource, select the name of the API resource on the APIs list page to show the API details page.
- 

To list the API resources in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the API resources in a compartment, open a command prompt and run`oci api-gateway api list`to list the API resources:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the API resources.

For example:

```

```

If you want to list just those API resources with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListApis](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Api/ListApis)
