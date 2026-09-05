# Details for Compute Cloud@Customer Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_compute_cloud_at_customer.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Compute Cloud@Customer Logs

Logging details for Compute Cloud@Customer logs.

For more information, see[Logging for Compute Cloud@Customer](https://docs.oracle.com/iaas/compute-cloud-at-customer/ccc/logging.htm).

## Resources
- CCCInfrastructure

## Log Categories

API value (ID): Console (Display Name) Description
service_logs Service Logs The Compute Cloud@Customer log category

## Availability

Compute Cloud@Customer logs are available in all regions in[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

You can enable logs for the Compute Cloud@Customer resources. This provides logs for various activities on your Compute Cloud@Customer resources.

## Contents of a CCCInfrastructure Log

Property Description Example

specversion

Oracle Cloud Infrastructure Logging schema version.

`1.0`
source The C3 infrastructure short id

&lt;unique_ID&gt;
type The log category

`com.oraclecloud.ccc.cccinfrastructure.service_log`
id A source-unique identifier for this message.

`UUID`
time The time the message was generated.

`2021-02-18T18:21:52.024Z`
oracle.logid The OCID of the log object the message was sent to.

`ocid1.logid.oc1. <region_ID> . <unique_ID>`

oracle.compartmentId The OCID of the compartment the log object resided in at the time the message was ingested.`ocid1.compartmentid.oc1.`&lt;unique_ID&gt;

oracle.loggroupid The OCID of the log group the object resides in.`ocid1.loggroupid.oc1.`&lt;region_ID&gt;`.`&lt;unique_ID&gt;

oracle.tenantid The OCID of the tenant that owns the log object.`ocid1.tenancy.oc1.`&lt;unique_ID&gt;
data.requestMethod The HTTP request method.

`GET`
data.requestPath The full path of the API request.

`/20160918/compartments?compartmentId=ocid1.tenancy.oc1. <unique_ID>`
data.opcRequestId The Oracle identifier for the request.

```

```

data.actorId The OCID of the resource that performed the action.

`ocid1.user.oc1. <unique_ID>`
data.actorType The type of resource that performed the action.

For example,`USER`or`INSTANCE`
data.message Log message

`ListCompartments success`
data.summary The name of the API operation that generated this activity.

`ListCompartments`
data.success The result, 1 for success and 0 for failure.

`1`

## Example CCInfrastructure Log
```

```
