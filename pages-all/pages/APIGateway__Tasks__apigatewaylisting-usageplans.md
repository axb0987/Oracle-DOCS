# Listing Usage Plans
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-usageplans.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing Usage Plans

Find out how to list existing usage plans with the API Gateway service.

Having created usage plans, you might need to list the existing usage plans. For example, you might want to see which usage plans are currently active.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-usageplans.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-usageplans.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-usageplans.htm#)
- 

- Open the navigation menu and select Developer Services . Under API Management , select Gateways .
- Select Usage plans .

The Usage plans list page opens. All usage plans in the selected compartment are displayed in a table.
- To view the usage plans in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To see more detail about an individual usage plan, select the name of the usage plan on the Usage plans list page to show the usage plan details page.
- 

To list the usage plans in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the usage plans in a compartment, open a command prompt and run`oci api-gateway usage-plan list`to list the usage plans:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the usage plans.

For example:

```

```

If you want to list just those usage plans with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListUsagePlans](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/UsagePlan/ListUsagePlans)
