# Viewing Default Metric Charts for All Block Volume Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-charts-namespace.htm
- Fetched: 2026-09-05 01:45 CDT

# Viewing Default Metric Charts for All Block Volume Resources

Go to the Service Metrics page in the Console to view metric charts that use predefined service queries for`oci_blockstore`. The charts show metric data for all resources in the selected compartment and region.

For more information about these metrics, see[Block Volume Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
The Service Metrics page opens.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- To view the resources in a different compartment, use the Compartment filter to switch compartments.
The page lists metric namespaces for the selected region and compartment. You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- For Metric namespace , select oci_blockstore .

The Service Metrics page displays default charts for all Block Volume resources in the selected region and compartment that emit metric data to the`oci_blockstore`metric namespace.

You can update the query by[selecting dimensions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-dimensions.htm)or by[opening the chart in the Metrics Explorer page for advanced query updates . You can also[create an alarm based on the query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-create-alarm.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm)
