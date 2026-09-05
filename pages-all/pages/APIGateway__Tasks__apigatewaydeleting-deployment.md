# Deleting an API Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting-deployment.htm
- Fetched: 2026-09-05 01:38 CDT

# Deleting an API Deployment

Find out how to delete API deployments that you previously created with the API Gateway service.

After you have deployed an API on an API gateway by creating an API deployment, you might decide that the API deployment is no longer required. You can delete individual API deployments on an API gateway, one at a time. When you delete an API deployment, its API deployment specification is permanently removed.

Deleted API deployments continue to be shown in the Console for 90 days, with a status of Deleted. After 90 days, deleted API deployments are no longer shown.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting-deployment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting-deployment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydeleting-deployment.htm#)
- 

- On the Gateways list page, select the API gateway containing the API deployment that you want to delete. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- Select the Deployments tab.

All API deployments in the selected API gateway are displayed in a table.
- From the Actions menu (three dots) for the API deployment, select Delete .
- Confirm that you want to delete the API deployment.

The API deployment and its API deployment specification are permanently removed.
- 

To delete API deployments using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To delete an existing API deployment:
- 

Open a command prompt and run`oci api-gateway deployment delete`to delete the API deployment:

```

```

where:
- `<deployment-ocid>`is the OCID of the API deployment to delete. To find out the API deployment's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).

For example:

```

```

The response to the command includes:
- The lifecycle state (for example, ACTIVE, DELETED).
- The id of the work request to delete the API deployment (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API deployment is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state DELETED`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is deleting the API deployment, enter:

```

```

- 

(Optional) To view the logs of the work request that is deleting the API deployment, enter:

```

```

- 

(Optional) If the work request that is deleting the API deployment fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API deployment has been deleted, enter the following command and confirm that the API deployment 's lifecycle state is DELETED:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[DeleteDeployment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/DeleteDeployment)
