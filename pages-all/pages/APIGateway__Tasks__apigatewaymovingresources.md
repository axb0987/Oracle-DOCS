# Moving an API Gateway Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingresources.htm
- Fetched: 2026-09-05 01:38 CDT

# Moving an API Gateway Between Compartments

Find out how to move API gateways between compartments with the API Gateway service.

Having created an API gateway, you might decide to move the API gateway from one compartment to another. An API gateway and the individual API deployments deployed on it can be in different compartments.

Note that calls to an API deployment will be disrupted while the API gateway on which it is deployed is being moved to a different compartment. Do not call an API deployment until the move operation is complete.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingresources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingresources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingresources.htm#)
- 

- On the Gateways list page, find the API gateway that you want to move. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- From the Actions menu (three dots) for the API gateway, select Move resource , select the compartment to which you want to move the API gateway, and select Move resource to start the process of moving the API gateway. Note that API deployments on the API gateway are not moved to the new compartment.

Do not call API deployments while the API gateway on which they are deployed is in the process of being moved to the new compartment.
- 

On the API gateway details page, select the Work requests tab and confirm the move operation is complete.

When the move operation is complete, resume calls to API deployments deployed on the API gateway.
- 

To move API gateways to a different compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To move an API gateway to a different compartment:
- 

Open a command prompt and run`oci api-gateway gateway change-compartment`to move the API gateway:

```

```

where:
- `<gateway-ocid>`is the OCID of the API gateway to move. To find out the API gateway's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- `<compartment-ocid>`is the OCID of the compartment to which to move the API gateway.

For example:

```

```

Note that API deployments on the API gateway are not moved.

The response to the command includes:
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to move the API gateway (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API gateway is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is moving the API gateway, enter:

```

```

- 

(Optional) To view the logs of the work request that is moving the API gateway, enter:

```

```

- 

(Optional) If the work request that is moving the API gateway fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API gateway has been moved, enter the following command and confirm that the API gateway's new compartment OCID is as you expect:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ChangeGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/ChangeGatewayCompartment)
