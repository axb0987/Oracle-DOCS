# Updating an API Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating-deployments.htm
- Fetched: 2026-09-05 01:39 CDT

# Updating an API Deployment

Find out how to modify API deployments that you previously created with the API Gateway service.

After you have deployed an API on an API gateway by creating an API deployment, you might decide to change the API deployment. For example, you might want to change an API deployment specification to add additional back ends to the API deployment.

Note that there are some properties of API deployments for which you can't change the original values.

You can update API deployments by using the Console, the CLI, and the API. You can update an API deployment specification by using the Console or by editing a JSON file.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating-deployments.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating-deployments.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating-deployments.htm#)
- 

- On the Gateways list page, select the API gateway containing the API deployment that you want to update. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- Select the Deployments tab.

All API deployments in the selected API gateway are displayed in a table.
- From the Actions menu (three dots) for the API deployment that you want to update:
- 

Select Edit to change API deployment properties by entering new values.
- 

Select Upload an existing deployment API to change API deployment properties by uploading a JSON file to replace the original API deployment specification.

For more information about defining API deployment specifications, see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm). Avoid entering confidential information.
- Select Move resource to move the API deployment to a different compartment.
- Select Manage tags to view and edit the tags applied to the API deployment, and select Add tag to apply more tags to the API gateway.
- 

To update existing API deployments using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To update an existing API deployment:
- 

Open a command prompt and run`oci api-gateway deployment update`to update the API deployment:

```

```

where:
- `<deployment-ocid>`is the OCID of the API deployment to update. To find out the API deployment's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- `<filename>`is the relative location and filename of the JSON file containing the replacement API deployment specification. For example,`replacement-specification.json`. For more information about defining API deployment specifications, see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm).

For example:

```

```

The response to the command includes:
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to update the API deployment (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API deployment is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is updating the API deployment, enter:

```

```

- 

(Optional) To view the logs of the work request that is updating the API deployment, enter:

```

```

- 

(Optional) If the work request that is updating the API deployment fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API deployment has been updated, enter the following command and confirm that the API deployment's properties are as you expect:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[UpdateDeployment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/UpdateDeployment)
