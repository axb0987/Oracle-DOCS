# Listing API Gateway Certificate Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-certificates.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing API Gateway Certificate Resources

Find out how to list existing API Gateway certificate resources with the API Gateway service.

Having created API Gateway certificate resources, you might need to list the existing API Gateway certificate resources. For example, you might want to see which API Gateway certificate resources are currently active.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-certificates.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-certificates.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-certificates.htm#)
- 

- Open the navigation menu and select Developer Services . Under API Management , select Gateways .
- Select Certificates .

The Certificates list page opens. All API Gateway certificate resources in the selected compartment are displayed in a table.
- To view the API Gateway certificate resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

To list the API Gateway certificate resources in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the API Gateway certificate resources in a compartment, open a command prompt and run`oci api-gateway certificate list`:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the API Gateway certificate resources.

For example:

```

```

If you want to list just those API Gateway certificate resources with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListCertificates](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/ListCertificates)
