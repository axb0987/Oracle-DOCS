# Notifications Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/notificationmetrics.htm
- Fetched: 2026-09-05 02:49 CDT

# Notifications Metrics

View metric charts, create queries, and review details about Notifications service metrics.

Use the Notifications service metrics to measure the number and size of[messages](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#concepts__messagedefinition)that are in initial requests, are delivered, and are not delivered.

The following pages describe tasks you can perform with Notifications service metrics:
- [Viewing Default Metric Charts for Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Tasks/viewingcharts.htm)
- [Viewing Default Metric Charts for All Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Tasks/view-chart-namespace.htm)
- [Viewing Default Metric Charts for a Single Topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Tasks/view-chart-resource.htm)
- [Creating a Query for Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Tasks/query-metric.htm)

You can[create an alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)to notify you when a Notifications metric meets a specified trigger. For example, you can create an alarm to notify you when messages aren't delivered because of email suppressions, by selecting the`FailedMessageCount`metric and the`resultCode`dimension with the value`4702`. Note that you can only select this metric and dimension when a message failed and a valid value is emitted in the selected compartment. If the metric or dimension isn't available for selection using Basic mode in the Console, then use Advanced mode, or use CLI or API instead.

For details about the Notifications service metrics, see[Notifications Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/notificationmetrics-reference.htm)
