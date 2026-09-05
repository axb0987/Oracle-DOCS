# Storing and Viewing Function Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm
- Fetched: 2026-09-05 02:08 CDT

# Storing and Viewing Function Logs

Find out how to store and view function logs with OCI Functions.

When a function is invoked, you'll typically want to access the function's logs for troubleshooting. The Oracle Cloud Infrastructure Logging service is the default and recommended option for accessing, searching, and storing function logs. If you enable Oracle Cloud Infrastructure Logging for an application, default invocation logs are created whenever functions in the application are invoked. See[Using the Console to Enable and View Function Logs in Oracle Cloud Infrastructure Logging](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm#usingconsole). For more information about the contents of function logs, see[Details for Functions](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_functions.htm).

Alternatively, there might be occasions when you want to send function logs to an external logging destination like Papertrail. To send logs to an external logging destination instead of the Oracle Cloud Infrastructure Logging service, you use the Fn Project CLI to specify a syslog URL. See[Using Fn Project CLI Commands to Specify a syslog URL](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm#usingfncli).
Note that to store and view logs for a function (other than default invocation logs stored in the Oracle Cloud Infrastructure Logging service), the function must include print statements. For example:
- For node.js:`console.log('Entering Hello Node.js function');`
- For java:`System.err.println("Entering Java Hello World Function");`
- For go:`fmt.Println("Entering Hello Go function")`

## Using the Console to Enable and View Function Logs in Oracle Cloud Infrastructure Logging

To enable and view function logs in the Oracle Cloud Infrastructure Logging service:
- On the Applications list page, select the application with functions for which you want to create, enable, and view logs. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- Select the Monitoring tab and go to the Logs section.
- To create and enable a new function log in the Oracle Cloud Infrastructure Logging service:
- From the the Actions menu (three dots) for the Function Invocation Logs category, select Enable Log and specify:
- Compartment: The compartment in which to create the new log. By default, the current compartment.
- Log Group: The log group in which to create the new log. Select an existing log group, or select Create new group to create a new log group with a name and description that you provide.
- Log Name: The name of the new log. By default, &lt;application-name&gt;_invoke .
- Log Retention: The length of time to retain log data.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Enable Log to create the new log (and the new log group, if you specified one).
- To enable an existing function log that is currently inactive, from the the Actions menu (three dots) for the Function Invocation Logs category, select Enable Log .
- To view the data in an existing function log, select the name of the log group containing the log you want to view in the Log Group column.

The log opens in the log group's Log Details page, enabling you to view log data, and sort and filter log data by time.
- Select the down arrow beside a log event to see log data for that event.
- Select Explore with Log Search to search log data.

### Tip: Filtering logs by request id

When searching log data, you can use the`data.opcRequestId`field to filter logs by request id. If an API deployment in API Gateway invokes a function on an OCI Functions back end, you can see logs relating to both the API Gateway request and the OCI Functions request by using the same`data.opcRequestId`field together with a wildcard, as follows:
- On the Logging Search page, select the down arrow beside a log event to see log data for that event.
- Select the`"data.opcRequestId"`field in the function log and select Filter matching from the popup menu.

For example, assume the function log contains the field`"data.opcRequestId": "/01FJA5VCVM0000000000025M1Z/01FJA5VCVM0000000000025M20"`. The field`"data.opcRequestId": "/01FJA5VCVM0000000000025M1Z/01FJA5VCVM0000000000025M20"`is copied into the Log Search (Basic Mode) page as a filter.
- On the Log Search (Basic Mode) page, select Show Advanced Mode and replace the second half of the`"data.opcRequestId"`field value shown in the Query field with the * (asterisk) wildcard.

For example, so that it reads`data.opcRequestId: '/01FJA5VCVM0000000000025M1Z/*'`
[
- Select Search .

### Tip: Configuring the format of log lines

You can specify that you want log lines that are sent to the Oracle Cloud Infrastructure Logging service to be in plain text format (the default) or in JSON format.

When functions emit log lines in JSON format, sending the log lines as JSON rather than as plain text enables you to use structured fields in the Oracle Cloud Infrastructure Logging service to perform advanced filtering and querying.

To specify the format of log lines that are sent to the Oracle Cloud Infrastructure Logging service:
- On the Applications list page, select the application with functions for which you want to specify the log line format. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- On the Details tab, select the Edit button beside Logging line format .
- Select a log line format as follows:
- Plain text (default): Select this option when functions in the application emit unstructured log lines. Log line values are sent to the Oracle Cloud Infrastructure Logging service as strings. Note that log lines are treated as plain text and sent as strings, even if they are valid JSON.
- JSON: Select this option when functions in the application emit log lines in JSON format. Log line values that are valid JSON are sent to the Oracle Cloud Infrastructure Logging service as JSON. Note that log lines that are not valid JSON are treated as plain text and are sent as strings.

## Using Fn Project CLI Commands to Specify a syslog URL

Tip  
  
From time to time, new versions of the Fn Project CLI are released. We recommend you regularly check that the latest version is installed. For more information, see[Steps to upgrade the Fn Project CLI](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsupgradingfncli.htm#functionsupgradingfncli_topic-Steps-to-upgrade-Fn-Project-CLI).

The Oracle Cloud Infrastructure Logging service is the default and recommended option for accessing, searching, and storing function logs.

Alternatively, you can send function logs to an external logging destination like Papertrail instead by using the Fn Project CLI to specify a syslog URL. Note that to use an external logging destination, you must have set up a VCN with public subnets and an internet gateway (see[Creating the VCN and Subnets to Use with OCI Functions, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingvcn.htm)).

To send function logs to an external logging destination by setting the syslog URL:
- Log in to your development environment as a functions developer.
- 

To create a new application and specify that all functions in the application send their logs to an external logging destination, enter:

```

```

where:
- `<app-name>`is the name of the new application. Avoid entering confidential information.
- `<logging-service-url>`is the syslog URL to which to send logs.
- `<subnet-ocid>`is the OCID of the public subnet (or subnets, up to a maximum of three) in which to run functions. If a regional subnet has been defined, best practice is to select that subnet to make failover across availability domains simpler to implement. If a regional subnet has not been defined and you need to meet high availability requirements, specify multiple subnets (up to three) by including`--subnet-id <subnet-ocid>`in the command multiple times. We recommend that the public subnets are in the same region as the Docker registry that's specified in the Fn Project CLI context (see[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)).

For example:

```

```

Note that if you subsequently set up Oracle Cloud Infrastructure Logging to store logs, the existing syslog URL details are retained. So if you later decide to resume sending function logs to the external logging destination, you simply have to disable Oracle Cloud Infrastructure Logging and logs will be sent to the syslog URL again.
- 

To update an existing application and specify that all functions in the application send their logs to an external logging destination, enter:

```

```

where:
- `<app-name>`is the name of the application to update
- `<logging-service-url>`is the syslog URL to which to send logs

For example:

```

```

- 

To update an existing application and remove the external logging destination specified for the syslog URL, enter:

```

```

where:
- `<app-name>`is the name of the application to update

For example:

```

```

## Previously Supported Logging Options

In earlier OCI Functions releases (prior to the release of the Oracle Cloud Infrastructure Logging service), you could specify where OCI Functions stores a function's logs by setting up a 'logging policy' for the application containing the function. Previously, you could use the Console to set up a logging policy to:
- 

Store logs as objects in a storage bucket in Oracle Cloud Infrastructure Object Storage by selecting the OCI Logging option.

To view function logs in a storage bucket, the group to which you belong must have been granted access with the following identity policy statements:
- `Allow group <group-name> to manage object-family in compartment <compartment-name>`
- `Allow group <group-name> to read objectstorage-namespaces in compartment <compartment-name>`(Usually created when configuring your tenancy for function development. See[Policy Statements to Give OCI Functions Users Access to Oracle Cloud Infrastructure Registry Repositories](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingpolicies.htm#userregistrypolicy).)
- Store logs by sending them to an external logging destination like Papertrail by selecting the Syslog URL option.

For an existing application where you have previously already set up a logging policy, the above functionality is still supported and the existing logging policy is applied. However, note the following:
- You cannot use the Console to set up a new logging policy or edit an existing logging policy.
- If the existing logging policy specified storing function logs as objects in a storage bucket in Oracle Cloud Infrastructure Object Storage:
- The ability to store logs in Object Storage will be deprecated in a future release.
- We recommend you switch to storing logs using Oracle Cloud Infrastructure Logging.
- If you do switch to using Oracle Cloud Infrastructure Logging to store logs, you cannot revert to storing the logs in Object Storage.
- Logs stored in Object Storage will continue to exist (with each log name including the OCID of the associated function, as before).
- If the existing logging policy specified a syslog URL:
- If you switch to using Oracle Cloud Infrastructure Logging to store logs, the existing syslog URL details are retained. So if you later decide to resume sending function logs to the external logging destination, you simply have to disable Oracle Cloud Infrastructure Logging and logs will be sent to the syslog URL again.
-
