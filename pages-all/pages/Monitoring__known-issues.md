# Known Issues for Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/known-issues.htm
- Fetched: 2026-09-05 02:40 CDT

# Known Issues for Monitoring

Known issues have been identified in Monitoring.

See also[Troubleshooting Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/troubleshooting.htm).

## Alarm messages aren't received in Oracle Platform Services managed compartments
Details[Alarm messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)sent to topics in[Oracle Platform Services managed compartments (named "ManagedCompartmentForPaas")](https://docs.oracle.com/iaas/Content/General/Reference/PaaSprereqs.htm#resources)aren't received. This issue occurs when the Monitoring service doesn't have permission to use topics in that compartment. Workaround To work around this issue,[move the alarm to a non-managed compartment](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm)
