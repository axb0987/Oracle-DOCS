# Details for Application Performance Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details-for-apm.htm
- Fetched: 2026-09-05 02:36 CDT

# Details for Application Performance Monitoring

Describes logging details for Application Performance Monitoring (APM).

## Resources
- Apm Domains

## Log Categories

API value (ID): Console (Display Name) Description
dropped-data Dropped Data The incoming ingest requests that were rejected by the APM service because of throttling, invalid data keys, or an oversized or malformed payload. This information helps customers triage dropped requests.

## Availability

Application Performance Monitoring logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

Service logs for Application Performance Monitoring logging are delivered on a best effort basis. In limited situations, a few log entries might not be delivered successfully. Furthermore, the number of log messages per minute are limited.

## Contents of an Application Performance Monitoring Log

Property Description
arrivaltime Timestamp when observation arrived, in the format of "2023-03-14T15:21:27.010Z".
content Original content of the observation. The display size limit is 4 KB.
contentlength Length of content in bytes.
dataformat Format name of the data, for example, "apm".
dataformatversion Format version.
message Human-readable string describing the rejection cause.
obstype Type of the observation, for example, "public-span".
rejectioncause Rejection cause, which can be one of the following:
- PAYLOAD_THROTTLED
- BAD_FORMAT
- OVERSIZED_PAYLOAD
- INVALID_DATA_KEY
compartmentid OCID of the compartment.
loggroupid OCID of the log group.
logid OCID of the log object.
tenantid OCID of the tenant.
id UUID of the log message.
source OCID of the APM domain.
specversion The version of the CloudEvents specification which the event uses. This enables the interpretation of the context.
time Timestamp when the log was written.
type The message type. Consumers use the`type`and`specversion`to determine how to interpret the body. Pattern:`com.oraclecloud.{service}.{resource-type}.{category}`, for example,`com.oraclecloud.compute.instance.terminated`.

## Example Application Performance Monitoring Log
```

```
