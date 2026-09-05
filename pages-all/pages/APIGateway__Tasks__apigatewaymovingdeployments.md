# Moving an API Deployment Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingdeployments.htm
- Fetched: 2026-09-05 01:38 CDT

# Moving an API Deployment Between Compartments

Find out how to move API deployments between compartments with the API Gateway service.

Having deployed an API on an API gateway by creating an API deployment, you might decide to move the API deployment from one compartment to another. An API gateway and the individual API deployments deployed on it can be in different compartments.

Note that calls to an API deployment will be disrupted while the API deployment is being moved to a different compartment. Do not call the API deployment until the move operation is complete.

- [Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingdeployments.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingdeployments.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymovingdeployments.htm#)
- 

To move an API deployment to a different compartment using the Console:
- On the Gateways list page, select the API gateway containing the API deployment that you want to move. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- Select the Deployments tab.

All API deployments in the selected API gateway are displayed in a table.
- From the Actions menu (three dots) for the API deployment, select Move resource , select the compartment to which you want to move the API deployment, and select Move resource to start the process of moving the API deployment.

Do not call an API deployment while the API deployment is in the process of being moved to the new compartment.
- 

On the API gateway details page, select the Work requests tab and confirm the move operation is complete.

When the move operation is complete, resume calls to the API deployment.
- 

To move API deployments to a different compartment using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

To move an API deployment to a different compartment:
- 

Open a command prompt and run`oci api-gateway deployment change-compartment`to move the API deployment:

```

```

where:
- `<deployment-ocid>`is the OCID of the API deployment to move. To find out the API deployment's OCID, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting.htm).
- `<compartment-ocid>`is the OCID of the compartment to which to move the API deployment.

For example:

```

```

The response to the command includes:
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to move the API deployment (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API deployment is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

- 

(Optional) To see the status of the work request that is moving the API deployment, enter:

```

```

- 

(Optional) To view the logs of the work request that is moving the API deployment, enter:

```

```

- 

(Optional) If the work request that is moving the API deployment fails and you want to review the error logs, enter:

```

```

- 

(Optional) To verify that the API deployment has been moved, enter the following command and confirm that the API deployment's new compartment OCID is as you expect:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
- 

Run the[ChangeDeploymentCompartment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Deployment/ChangeDeploymentCompartment)
