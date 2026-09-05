# Setting Up Firewall Logging for a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/setting_up_logging_analytics.htm
- Fetched: 2026-09-05 03:11 CDT

# Setting Up Firewall Logging for a Web Application Firewall Policy

Set up logging for a firewall contained within a web application policy.

The web application uses the OCI Logging service for logging needs. See[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)for more information.
- Enable web application firewall logs in the[Logging](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)service.
- Create a log group in the[Log Analytics](https://docs.oracle.com/iaas/log-analytics/home.htm)service.
- Set up a connector in[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)to send logs from the Logging service to the Log Analytics group.

For an example of a connector configuration that sends logs to Log Analytics, see[Scenario: Analyzing Logs](https://docs.oracle.com/iaas/Content/connector-hub/analyzelogs.htm).

In Log Analytics, the Oracle-defined log source for web application firewall is[Oracle-Defined Sources](https://docs.oracle.com/iaas/log-analytics/doc/oracle-defined-sources.html). The Oracle-defined parser for web application firewall is[OCI Parser Details](https://docs.oracle.com/iaas/log-analytics/doc/oci-parser-details.html)
