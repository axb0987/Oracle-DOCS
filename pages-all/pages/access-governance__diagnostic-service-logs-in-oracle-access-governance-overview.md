# Diagnostic Service Logs in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/diagnostic-service-logs-in-oracle-access-governance-overview.htm
- Fetched: 2026-09-05 03:14 CDT

# Diagnostic Service Logs in Oracle Access Governance

Service logs provide critical diagnostic information that enables you to perform effective troubleshooting.

You can now leverage the Oracle Cloud Infrastructure (OCI) Logging service to access diagnostic service logs for Oracle Access Governance. For instance, you can view the log details in JSON format in the OCI Console when an operation like campaign creation fails, indicated by “ System ended ” status message in the Oracle Access Governance Service Instance Console.

## Authorized Users for Diagnostic Service Log Configuration

By default, the tenancy Administrator can configure the Oracle Access Governance service logs for your service instance.

Additionally, any user with the required permissions to create an Oracle Access Governance service instance can configure these service logs.

## Prerequisite for Enabling Diagnostic Service Logs

To enable and manage service logs in a compartment, you need to create a log group first.

If a log group is not present when enabling service logs, you can create one using the Show Advanced Options feature on the Enable Service Log panel during the enabling process. See[Enable Service Log for a Resource in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-diagnostic-service-logs-in-oracle-access-governance.htm#enable-service-log-for-a-resource-in-oracle-access-governance)
