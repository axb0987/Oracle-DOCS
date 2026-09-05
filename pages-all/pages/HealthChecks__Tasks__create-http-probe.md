# Creating an HTTP On-Demand Probe
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm
- Fetched: 2026-09-05 02:13 CDT

# Creating an HTTP On-Demand Probe

Create an HTTP on-demand probe in Health Checks.

On-demand probes are available through SDK, CLI, and API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci health-checks http-probe create-on-demand](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-probe/create-on-demand.html)command and required parameters to create an HTTP on-demand probe:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[CreateOnDemandHttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe/CreateOnDemandHttpProbe)operation to create an HTTP on-demand probe.

[Example](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#)

The following example request creates an HTTP on-demand probe to check the health of`www.example.com`using`GET`requests over HTTP protocol.
```

```

Following is an example`200`response for successful creation of the previously defined HTTP on-demand probe. The`resultsUrl`field indicates the URL for retrieving results.

```

```
