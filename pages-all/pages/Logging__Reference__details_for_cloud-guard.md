# Details for Cloud Guard
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_cloud-guard.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Cloud Guard

Logging details for Cloud Guard.

## Resources
- Cloud Guard - Raw Logs, produced by Instance Security.
- Cloud Guard - Query Results Logs, produced by scheduled queries.

## Availability

Cloud Guard logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a Cloud Guard Raw Log

Cloud Guard logs capture detailed information returned from Instance Security rules. Details appear as values in the`data`field.

Property Description
`type`Shows the type of Cloud Guard log.
`executionTime`Time the output was generated, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`result`The result of the query.

## Sample Cloud Guard Raw Log
```

```

## Contents of a Cloud Guard Query Results Log

Cloud Guard logs capture detailed information returned from Cloud Guard queries. Each log entry contains information such as the time the request was received and the results of the query. Details appear as values in the`data`field. This value is a JSON-formatted data with the following fields.

Property Description
`type`Shows the type of Cloud Guard log.
`executionTime`Time the output was generated, in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`result`The result of the query.

## Sample Cloud Guard Query Results Log
```

```
