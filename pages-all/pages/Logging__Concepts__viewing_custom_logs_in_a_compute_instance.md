# Viewing Custom Logs in a Compute Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/viewing_custom_logs_in_a_compute_instance.htm
- Fetched: 2026-09-05 02:36 CDT

# Viewing Custom Logs in a Compute Instance

Use the Custom logs resource on a Compute instance details page to view logging details for the instance in the selected compartment.

Logging Search APIs are called and any available logs are pulled for the instance. Instances can have a customer application running on them (for example, a gaming server), and they can configure logs from the gaming server to be collected by the Unified Monitoring Agent, and then be pushed into the Logging service and be indexed there. Logs are pulled and displayed on the Logs resource. As such, when a customer views their compute instance, they can see that their application is pushing logs to the Logging service. Logs, however, can't be enabled or created from this interface.

In a Compute instance's details page, in the Custom logs resource, you can sort log entries ( Newest , the default, or Oldest ), or filter by time (the default Past 5 minutes , Past 15 minutes , Past hour , Past 3 hours , Today , Custom ).

Click Explore with Log Search to open the main[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm)page, where you can add or remove filters and so on. The Search page loads with`instanceid`of the instance already set as a filter under Filters .

Open the Logs page to[create](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/create-logging-log.htm)custom logs for the instance. Custom logs are sent from Oracle Cloud Infrastructure compute VM instances.

For the Custom logs resource to be available on a Compute instance, the following is required:
- The Custom Logs Monitoring plugin must be enabled, and all plugins must be running. For more information, see[Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm).
- The instance must have a supported OS:
- Oracle Linux 7, 8, 9, and 10
- CentOS 7
- Windows Server 2016, 2019, 2022, and 2025
- Ubuntu 16.04, 18.04, 20.04, and 24.04
