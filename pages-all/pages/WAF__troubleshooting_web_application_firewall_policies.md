# Troubleshooting Web Application Firewall Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/troubleshooting_web_application_firewall_policies.htm
- Fetched: 2026-09-05 03:12 CDT

# Troubleshooting Web Application Firewall Policies

Use troubleshooting information to identify and address common issues that can occur while working with Web Application Firewall policies.

## Error Trying to Create More Than 100 Policies

Web Application Firewall (WAF) has a limit of[100 policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#GetStartedPolicy)per tenancy.

If you try to create more than 100 policies, you get an error. If needed, you can submit a service request asking to increase this limit. If multiple web apps need to use the same configuration, a single policy can be applied to different load balancers. If several load balancers require the same protections, you can use a single WAF policy. For example, you would need only 10 WAF policies or less to protect 50 load balancers.

## Identifying the Oracle-Defined Log Source

In Log Analytics, the name of the Oracle-defined log source is[Oracle-Defined Sources](https://docs.oracle.com/iaas/log-analytics/doc/oracle-defined-sources.html).

## Identifying the Oracle-Defined Parser

In Log Analytics, the oracle-defined parser for WAF is[OCI Parser Details](https://docs.oracle.com/iaas/log-analytics/doc/oci-parser-details.html)
