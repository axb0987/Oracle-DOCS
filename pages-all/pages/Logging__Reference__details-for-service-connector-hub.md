# Details for Connector Hub
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details-for-service-connector-hub.htm
- Fetched: 2026-09-05 02:36 CDT

# Details for Connector Hub

Review details of service logs for Connector Hub.

## Resources
- [Service connectors](https://docs.oracle.com/iaas/Content/connector-hub/managingconnectors.htm)

## Log Categories

API value (ID) Console (Display Name) Description
runlog Connector Tracking Information about a service connector run, indicating success or failure.

## Availability

Connector Hub logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a Connector Hub Log

Property Description
`logContent`/`data`/`log`Log level. Available values:
- `INFO`
- `ERROR`
`logContent`/`data`/`message`Summary of the log event.
`logContent`/`data`/`messageType`Type of log message. Available values:
- `CONNECTOR_RUN_STARTED`
- `CONNECTOR_RUN_COMPLETED`
`logContent`/`oracle`/`compartmentOCID`Compartment that the service connector belongs to.
`logContent`/`oracle`/`connectorId`OCID of the service connector.

See also[Logging Format Overview](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/top_level_logging_format.htm).

## Example Success Log
```

```

## Example Error Log
```

```

## What's Next

- [Enabling Service Logs for a Connector](https://docs.oracle.com/iaas/Content/connector-hub/enable-logs.htm)
- [Troubleshooting Connectors](https://docs.oracle.com/iaas/Content/connector-hub/troubleshooting.htm)
