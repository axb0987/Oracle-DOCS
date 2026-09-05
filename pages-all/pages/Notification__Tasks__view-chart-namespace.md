# Viewing Default Metric Charts for All Topics
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/view-chart-namespace.htm
- Fetched: 2026-09-05 02:50 CDT

# Viewing Default Metric Charts for All Topics

Go to the Service Metrics page in the Console to view metric charts that use predefined service queries for`oci_notification`. The charts show metric data for all messages sent to topics in the selected compartment and region.

For more information about these metrics, see[Notifications Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Reference/notificationmetrics-reference.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
The Service Metrics page opens.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- To view the resources in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To view the resources in a different compartment, use the Compartment filter to switch compartments.
The page lists metric namespaces for the selected region and compartment. You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- For Metric namespace , select oci_notification .

The Service Metrics page displays default charts for messages sent to topics in the selected region and compartment.

You can update the query by[selecting dimensions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-dimensions.htm)or by[opening the chart in the Metrics Explorer page for advanced query updates . You can also[create an alarm based on the query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-create-alarm.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm)
