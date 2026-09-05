# Listing API Gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing API Gateways

Find out how to list existing API gateways with the API Gateway service.

Having created API gateways, you might need to list the existing API gateways. For example, you might want to see whether there are any API gateways that are no longer required, or quickly locate an API gateway by its OCID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm#)
- 

- Open the navigation menu and select Developer Services . Under API Management , select Gateways .

The Gateways list page opens. All API gateways in the selected compartment are displayed in a table.
- To view the API gateways in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To see more detail about an individual API gateway, select the name of the API gateway on the Gateways list page to show the API gateway details page.
- 

To list the API gateways in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the API gateways in a compartment, open a command prompt and run`oci api-gateway gateway list`to list the API gateways:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the API gateway.

For example:

```

```

If you want to list just those API gateways with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListGateways](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/GatewaySummary/ListGateways)
