# Viewing Load Balancer Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics_topic-Using_the_Console.htm
- Fetched: 2026-09-05 01:40 CDT

# Viewing Load Balancer Metrics

View the various metrics associated with a load balancer's performance.

You can view the following types of metrics for load balancers:
- [A single load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics_topic-Using_the_Console.htm#view-single-load-balancer).
- [All the load Balancers contained in a compartment](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/loadbalancermetrics_topic-Using_the_Console.htm#view-all-metrics).

## Viewing Metrics for a Single Load Balancer

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page,
- In the Metrics section, enter the following:

- Start time : The date-time group for when the metric period starts.
- End time : The date-time group for when the metric period ends.
- Quick selects : Select a predetermined time period for the metric period from the list.
- Under Applied Filters , enter the UTC-based date-time group covered by the metrics. Instead of entering time and day, you can specify the range of hours and days covered by the metrics. Select Apply filter . The metrics charts request to reflect the timeframe you specified.
- For each metric displayed on the page, you can apply the following commands from the Action menu in the upper-right corner:

- View query in Metrics Explorer : View the metric in the Monitoring service's Metrics Explorer. See[Viewing a Custom Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm)for more information.
- Copy chart URL : Copy the URL of the metric chart to your computer's clipboard, where you can paste it into another source.
- Copy query (MQL) : Copy the Monitoring Query Language query to your computer's clipboard, where you can paste it into another source. See[Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm)for more information.
- Create an alarm on this query : Create an alarm. See[Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)for more information.
- Table/Chart view : Display the metrics in the opposite format to what is current used.

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Viewing Metrics for All Load Balancers in a Compartment

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics . The Service metrics page appears.
- Select the Compartment from the list.
- Select oci_lbass from the Metric namespace list.
A default set of charts for the selected metric namespace appears in the Service Metrics page. For more information about the emitted metrics, see the foregoing table. You can also use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm)
