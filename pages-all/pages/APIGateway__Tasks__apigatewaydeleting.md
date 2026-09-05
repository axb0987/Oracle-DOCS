# Deleting an API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting.htm
- Fetched: 2026-09-05 01:38 CDT

# Deleting an API Gateway

Find out how to delete API gateways that you previously created with the API Gateway service.

After you have created an API gateway, you might decide that the API gateway is no longer required. You can delete an API gateway from the API Gateway service, provided there are no API deployments on it.

Deleted API gateways continue to be shown in the Console for 90 days, with a status of Deleted. After 90 days, deleted API gateways are no longer shown.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting.htm#)
- 

- On the Gateways list page, find the API gateway that you want to delete. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- From the Actions menu (three dots) for the API gateway, select Delete
- Confirm that you want to delete the API gateway.

The API gateway is permanently removed. Note that you cannot delete an API gateway if it still has API deployments on it. You must delete the API deployments first.
- 

To delete API gateways using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To delete an existing API gateway:
- 

Open a command prompt and run`oci api-gateway gateway delete`to delete the API gateway:

```

```

where:
- `<gateway-ocid>`is the OCID of the API gateway to delete. To find out the API gateway's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).

For example:

```

```

Note that you cannot delete an API gateway if it still has API deployments on it (including API deployments that are in different compartments to the API gateway itself). You must delete the API deployments first.

The response to the command includes:
- The lifecycle state (for example, DELETED, FAILED).
- The id of the work request to delete the API gateway (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API gateway has been deleted (or the request has failed), include either or both the following parameters:
- `--wait-for-state DELETED`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is deleting the API gateway, enter:

```

```

- 

(Optional) To view the logs of the work request that is deleting the API gateway, enter:

```

```

- 

(Optional) If the work request that is deleting the API gateway fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API gateway has been deleted, enter the following command and confirm that the API gateway's lifecycle state is DELETED:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[DeleteGateway](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Gateway/DeleteGateway)
