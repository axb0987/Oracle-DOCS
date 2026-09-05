# Viewing Web Application Firewall Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/view_firewall_metrics.htm
- Fetched: 2026-09-05 03:10 CDT

# Viewing Web Application Firewall Metrics

View the metrics for a firewall contained within a web application policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Firewalls .
The Firewalls list opens. All firewalls are displayed in a table.
- Select the firewall that you want to work with.
The firewall's details page opens.
- From the details page, select Monitoring .
- Find the Metrics section.
- Select Applied filters and specify the date-time group range covered by the metrics by completing the following:

- Start time
- End time

Alternatively, select a time span from the Quick Selects list. The time spans available range from the previous hour to 90 days in the future from that moment.
The Metrics list shows panels displaying metric information on areas such as blocked requests, detected requests, traffic, and response code groups.

For each panel, you can select commands from the Actions menu (three dots) . These commands include viewing the query in the Metrics Explorer , copying the chart URL, copying the query, and viewing the metric information in table view. You can also specify the Interval and Statistic for each chart.

For more information on monitoring and the Metrics Explorer , see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm). When prompted to provide a monitoring namespace, select or enter the`oci_waf`
