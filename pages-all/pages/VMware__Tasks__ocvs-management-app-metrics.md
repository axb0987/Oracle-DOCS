# Configuring Exported Metrics in vSphere using VMware Solution Management Appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-metrics.htm
- Fetched: 2026-09-05 03:08 CDT

# Configuring Exported Metrics in vSphere using VMware Solution Management Appliance

Configure metrics in vSphere for use with VMware Solution Management Appliance.

Use the Management Appliance to configure ESXi host metrics that are sent to the[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)service.

- Sign in to the vSphere web console.
You can get the link to the vSphere web console from the[SDDC Details page](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-get.htm).
- Select OCI Integration .
- Select the Metrics tab and use the toggle switch to enable metric collection.
- Select the metrics that you want to send to the[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Authenti)service.
You can use the filter to find the metric you're looking for. You must be connected to the OCI Monitoring service.
- Select Apply changes .
For more information about resource metrics, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)
