# Adding Logging to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Logging to API Deployments

Find out how to add logging policies to API specifications that you previously created with API Gateway.

Having created an API gateway and deployed one or more APIs on it, there will likely be occasions when you'll need to see more detail about the flow of traffic into and out of the API gateway. For example, you might want to review responses returned to API clients, or to troubleshoot errors. You can specify that the API Gateway service stores information about requests and responses going through an API gateway, and information about processing within an API gateway, as logs in the Oracle Cloud Infrastructure Logging service.
You can define and store two kinds of logs for API deployments in the Oracle Cloud Infrastructure Logging service:
- Access logs, that record a summary of every request and response that goes through the API gateway to and from an API deployment. For more information about access log content, see[API Deployment Access Log](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_api_gateway.htm).
- Execution logs, that record information about processing within the API gateway for an API deployment. For more information about execution log content, see[API Deployment Execution Log](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_api_gateway.htm). You can specify a log level for execution logs as one of the following:
- Information, to record a summary of every processing stage.
- Warning, to record only transient errors that occur during processing. For example, a connection reset.
- Error, to record only persistent errors that occur during processing. For example, an internal error, or a call to a function that returns a 404 message.

You can set an execution log level for an API deployment, and also set different execution log levels for individual routes to override the execution log level inherited from the API deployment.

You can add logging to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add Logging

### Using the Console to Configure and Enable Logs in Oracle Cloud Infrastructure Logging

To configure and enable API deployment logs using the Console to store logs in Oracle Cloud Infrastructure Logging:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API logging policies section of the Basic information page, specify one of the following options as the Execution log level to record information about processing within the API gateway:
- Information: Record a summary of every processing stage. This is the default option.
- Warning: Record only transient errors that occur during processing. For example, a connection reset.
- Error: Record only persistent errors that occur during processing. For example, an internal error, or a call to a function that returns a 404 message.
- 

Select Next twice to enter details for individual routes in the API deployment on the Routes page, select Add route , and select Show Route Logging Policies .
- 

Specify one of the following options as the Execution Log Level Override that applies to an individual route:
- Inherited from deployment: Inherit the execution log level from the API deployment.
- Information: Record a summary of every processing stage.
- Warning: Record only transient errors that occur during processing. For example, a connection reset.
- Error: Record only persistent errors that occur during processing. For example, an internal error, or a call to a function that returns a 404 message.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.

The API deployment is shown on the API deployment details page.
- On the Logs tab, select Enable log from the Actions menu (three dots) beside the log category (either Execution Logs or Access Logs ) for which you want to create and enable a new API deployment log in the Oracle Cloud Infrastructure Logging service in the Create Log entry panel:
- Compartment: By default, the current compartment.
- Log group: By default, the first log group in the compartment.
- Log name: By default,`<deployment-name>_execution`or`<deployment-name>_access`, depending on which category you select.
- Log retention: The default retention period for the log in 30-day increments, up to a maximum of 180 days. For more information, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).
- Select Enable log to create the new log and enable it.

## Editing a JSON File to Add Logging

### Editing a JSON File to Set Execution Log Level for Logs Stored in Oracle Cloud Infrastructure Logging

To edit the API deployment specification in a JSON file to set the log level for execution logs stored in Oracle Cloud Infrastructure Logging:
- 

Using your preferred JSON editor, edit the existing API deployment specification in which you want to set the log level for execution logs stored in Oracle Cloud Infrastructure Logging, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

At a minimum, the API deployment specification will include a`routes`section containing:
- A path. For example,`/hello`
- One or more methods. For example,`GET`
- A definition of a back end. For example, a URL, or the OCID of a function in OCI Functions.

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

(Optional) To set the log level for execution logs that applies globally to all routes in the API deployment specification:
- 

Insert a`loggingPolicies`section before the`routes`section. For example:

```

```

- 

Specify the level of detail to record about processing within the API gateway for all routes by including the`executionLog`policy in the`loggingPolicies`section, and setting the`logLevel`property to one of the following:
- `INFO`to record a summary of every processing stage.
- `WARN`to record only transient errors that occur during processing. For example, a connection reset.
- `ERROR`to record only persistent errors that occur during processing. For example, an internal error, or a call to a function that returns a 404 message.

For example:

```

```

- 

(Optional) To set the log level for execution logs for a particular route (overriding the global execution log level inherited from the API deployment):
- 

Insert a`loggingPolicies`section after the route's`backend`section. For example:

```

```

- 

Specify the level of detail to record about processing within the API gateway for the route by including the`executionLog`policy in the`loggingPolicies`section, and setting the`logLevel`property to one of the following:
- `INFO`to record a summary of every processing stage.
- `WARN`to record only transient errors that occur during processing. For example, a connection reset.
- `ERROR`to record only persistent errors that occur during processing. For example, an internal error, or a call to a function that returns a 404 message.

For example:

```

```

- 

Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
- Having set the log level for execution logs, follow the instructions in[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm)to create and enable a new API deployment log in the Oracle Cloud Infrastructure Logging service.

## Viewing Logs

Having added logging to an API deployment specification and deployed the API on an API gateway, the API Gateway service writes logs accordingly.

### Viewing Logs in Oracle Cloud Infrastructure Logging

You can view the content of an API deployment log in Oracle Cloud Infrastructure Logging from the API deployment details page. On the Logs tab, select the name of the log you want to view.

Alternatively, you can view the content of an API deployment log from the Oracle Cloud Infrastructure Logging Log Search page. See[Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm).

For more information about the content of access and execution logs, see:
- [API Deployment Access Log](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_api_gateway.htm)
- [API Deployment Execution Log](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_api_gateway.htm)
