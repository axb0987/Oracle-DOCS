# Details for Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_functions.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Functions

Logging details for Functions logs.

## Resources
- applications

## Log Categories

API value (ID): Console (Display Name) Description
invoke Function Invocation Logs Logs entries each time a function in an application is invoked.

## Availability

Functions logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

If you enable logging for an application, default invocation logs are created whenever functions in the application are invoked, as follows:
- 

The default invocation start log contains the following message:
```

```

- 

The default invocation end log contains the following message (an error code is only included if errors occur):
```

```

To store and view logs for a function (other than the default invocation logs), you must add print statements to your function. For example:
- 

For node js:

```

```

- 

For java:

```

```

- 

For go:

```

```

## Contents of a Functions Log

Property Description
specversion Oracle Cloud Infrastructure logging schema version of the log.
type Category of log, following convention`com.oraclecloud.{service}.{resource-type}.{log-category}`. Currently only:
```

```

source Display name of the application the log is associated with.
subject Display name of the function the log is associated with.
id Random UUID, unique to each log entry.
time Time the function output was generated, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
oracle.logid OCID of the Oracle Cloud Infrastructure Logging log object.
oracle.loggroupid OCID of the Oracle Cloud Infrastructure Logging log group.
oracle.compartmentid OCID of the compartment the function/application is in.
oracle.tenantid OCID of the tenancy the function/application is in.
oracle.ingestedtime Time the log line was ingested by Oracle Cloud Infrastructure logging, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
data.applicationId OCID of the application the log line is associated with.
data.containerId FaaS service-specific ID of the function's container.
data.functionId OCID of the function the log line is associated with.
data.requestId Oracle RID of the function invocation the log line is associated with. Deprecated, use data.opcRequestId instead.
data.opcRequestId Oracle RID of the function invocation the log line is associated with.
data.src I/O stream origin of data.message. Either STDOUT or STDERR.
data.message User-generated line of output from the function.

## An Example Functions Log
```

```

## Functions Log Object Name

Objects that store Functions log data use the following naming format:
```

```

For example:
```

```

## Using the Command Line Interface (CLI)

See[Functions Example](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Task/functions_eg.htm)
