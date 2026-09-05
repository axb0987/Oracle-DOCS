# Listing Subscribers
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-subscribers.htm
- Fetched: 2026-09-05 01:38 CDT

# Listing Subscribers

Find out how to list existing subscribers with the API Gateway service.

Having created subscribers, you might need to list the existing subscribers. For example, you might want to see which subscribers are currently active.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-subscribers.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-subscribers.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-subscribers.htm#)
- 

- Open the navigation menu and select Developer Services . Under API Management , select Gateways .
- Select Subscribers .

The Subscribers list page opens. All subscribers in the selected compartment are displayed in a table.
- To view the subscribers in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To see more detail about an individual subscriber, select the name of the subscriber on the Subscribers list page to show the subscriber details page.
- 

To list the subscribers in a compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To list all the subscribers in a compartment, open a command prompt and run`oci api-gateway subscriber list`to list the subscribers:

```

```

where:
- `<compartment-ocid>`is the OCID of the compartment containing the subscribers.

For example:

```

```

If you want to list just those subscribers with a status of Active, include the`--lifecycle-state ACTIVE`parameter in the request. For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ListSubscribers](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Subscriber/ListSubscribers)
