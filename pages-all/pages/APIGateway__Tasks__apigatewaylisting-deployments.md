# Listing API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-deployments.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing API Deployments

Find out how to list existing API deployments with the API Gateway service.

Having deployed APIs on API gateways by creating API deployments, you might need to list the existing API deployments. For example, you might want to obtain the OCID of an API deployment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-deployments.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-deployments.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-deployments.htm#)
- 

- On the Gateways list page, select the API gateway containing the API deployments that you want to see. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- Select the Deployments tab.

All API deployments in the selected API gateway are displayed in a table.
- 

To list the API deployments in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the API deployments in a compartment, open a command prompt and run`oci api-gateway deployment list`to list the API deployments:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the API deployments.

For example:

```

```

If you want to list just those API deployments with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

If you want to list all the API deployments on a particular API gateway in a compartment, include the`--gateway-id`parameter in the request and specify the API gateway's OCID. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListDeployments](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/DeploymentSummary/ListDeployments)
