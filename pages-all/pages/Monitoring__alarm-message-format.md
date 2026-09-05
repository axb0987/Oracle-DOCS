# Alarm Message Format
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm
- Fetched: 2026-09-05 02:40 CDT

# Alarm Message Format

Look up parameters that appear in alarm messages sent by Monitoring. Review parameter descriptions and example values, dynamic variables, and default appearance in formatted messages.

Parameters are listed in the order they appear in[pretty JSON](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-pretty-json)and[raw](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-raw)formats of email messages.

## Parameters in Alarm Messages

The following tables describe parameters in[alarm messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm)and provide example values.

### Alarm

Alarm parameter Description and example value
`dedupekey`

string

Unique identifier of the alarm (grouped message), or of the metric stream in the alarm (split message).

Example value:`exampleuniqueid`

Comments on usage:

For grouped messages (`notificationType`:`Group notifications across metric streams`), use`dedupekey`to group messages belonging to the same alarm.

For split messages (`notificationType`:`Split messages per metric stream`), use`dedupekey`to group messages belonging to the same alarm and same metric stream.

To deduplicate multiple occurrences of the same message, use`dedupekey`and`timestamp`together.
`title`

string

The alarm's notification title ( Notification subject in the Console form for creating and updating alarms). If not specified, then the alarm's display name is used.

Note: Insert dynamic variables that respect the maximum length for all supported use cases. Dynamic variables that exceed the maximum are considered invalid. For example, consider a dynamic variable for use in`title`. A supported use case for`title`is an email subject line, at a maximum length of 250 characters. In this case, the dynamic variable for a resource name (`{{dimensions.<dimension-name>}}`) is invalid because it's 256 characters and thus exceeds the maximum.

Example value using[dynamic variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm):`{{severity}} alarm triggered at {{timestamp}}`

Example value (alarm's display name):`High CPU Utilization`
`body`

string

The alarm's configured message body ( Alarm body in the Console form for creating and updating alarms). Null if not specified.

Example value using[dynamic variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm):`{{severity}} alarm triggered because threshold got breached due to {{metricValues}} at {{timestamp}}`

Example value (text):`Follow runbook at http://example.com/runbooks`
`type`

string

The reason for sending the notification message.

Valid values: See[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes).

Example value:`OK_TO_FIRING`
`severity`

string

The highest severity level of the listed alarms.

Valid values:`CRITICAL`,`ERROR`,`WARNING`, and`INFO`
`timestampEpochMillis`

long

The evaluation timestamp, in milliseconds since epoch time.

Example value:`1684337663852`
`timestamp`

string

The evaluation timestamp, in ISO-8601 format.

Example value:`2023-05-17T15:34:23.852Z`
`alarmMetaData`

array of objects

List of alarms related to this notification message.

For example values, see child parameters in the following table,[Alarm Metadata](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm#alarm-metadata).
`version`

int

The version of the alarm message format.

Example value:`1.5`

### Alarm Metadata

Alarm parameter Description and example value
`id`

string

The alarm OCID .

Example value:`ocid1.alarm.oc1.. exampleuniqueID`
`status`

string

The alarm state.

Valid values:`OK`,`FIRING`
`severity`

string

The alarm severity level.

Valid values:`CRITICAL`,`ERROR`,`WARNING`,`INFO`
`namespace`

string

The metric namespace.

Example value:`oci_computeagent`
`query`

string

The alarm's configured query, or MQL expression.

Example value:`CpuUtilization[1m].mean() > 90`
`totalMetricsFiring`

int

The number of[metric streams](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricstreamdefinition)represented in this notification message.

Example value:`3`
`dimensions`

array of objects

List of dimension key-value pairs that identify each[metric stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricstreamdefinition). The list is limited to a hundred entries.

Example value:`{ "instancePoolId": "Default", "resourceDisplayname": "oke-0", "faultDomain": "FAULT-DOMAIN-1", "resourceId": "ocid1.instance.oc1.iad.exampleid", "availabilityDomain": "sOZD:US-ASHBURN-AD-2", "imageId": "ocid1.image.oc1.iad.exampleid", "region": "us-ashburn-1", "shape": "VM.Standard.E3.Flex" }, { "instancePoolId": "Default", "resourceDisplayname": "oke-2", "faultDomain": "FAULT-DOMAIN-3", "resourceId": "ocid1.instance.oc1.iad.exampleid", "availabilityDomain": "sOZD:US-ASHBURN-AD-1", "imageId": "ocid1.image.oc1.iad.exampleid", "region": "us-ashburn-1", "shape": "VM.Standard.E3.Flex" }, { "instancePoolId": "Default", "resourceDisplayname": "oke-1", "faultDomain": "FAULT-DOMAIN-2", "resourceId": "ocid1.instance.oc1.iad.exampleid", "availabilityDomain": "sOZD:US-ASHBURN-AD-3", "imageId": "ocid1.image.oc1.iad.exampleid", "region": "us-ashburn-1", "shape": "VM.Standard.E3.Flex" }`
`metricValues`

array of objects

List of metric values for dimension key-value pairs ([metric streams](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricstreamdefinition)). The list is limited to a hundred entries.

Example value:`[{"CpuUtilization[1m].mean()":"92"},{"CpuUtilization[1m].mean()":"95"},{"CpuUtilization[1m].mean()":"93"}]`
`alarmUrl`

string

Link to the[alarm details page](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm)in the Console.

Example value:`https://cloud.oracle.com/monitoring/alarms/ocid1.alarm.oc1.iad. exampleuniqueid ?region=us-ashburn-1`
`alarmSummary`

string

The alarm's configured alarm summary ( Alarm summary in the Console form for creating and updating alarms). If not configured, a system-generated message that summarizes the state is used.

Example value using[dynamic variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm):`{{severity}} alarm triggered because threshold got breached due to {{metricValues}} at {{timestamp}}`

The content of the system-generated message (used when alarm summary isn't configured) depends on`notificationType`:
- 

For`Grouped messages across metric streams`:`Alarm <alarm-name> is in a <alarm-state> state; because <number-of-metric-streams> metrics meet the trigger rule: " mql-expression ", with a trigger delay of <number-of-minutes>`

Example:`Alarm High CPU Utilization is in a FIRING state; because 4 metrics meet the trigger rule: CpuUtilization[1m].mean() >90, with a trigger delay of 1 minute`
- 

For`Split messages per metric stream`:`Alarm <alarm-name> is in a <alarm-state> state; because the resources with dimensions listed below meet the trigger rule: " mql-expression ", with a trigger delay of <number-of-minutes>`
`notificationType`

string

Type of notification (grouped or split).

Valid values:`Grouped messages across metric streams`or`Split messages per metric stream`

## Dynamic Variables

The following tables list dynamic variables available for each parameter.

Use the indicated[dynamic variable](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)to render the value of a parameter in alarm messages.
Tip  
  

HTML escaping occurs for the primary (shorter) dynamic variable. For example, when you use the primary dynamic variable`{{title}}`for the`title`parameter value`alarm for successRate < 0.99`, the`<`character is rendered as`<`.

To disable HTML escaping, use the secondary (longer) dynamic variable. For example, when you use the secondary dynamic variable`{{{title}}}`for the`title`parameter value`alarm for successRate < 0.99`, the`<`character is preserved.

### Alarm

Alarm parameter[Dynamic variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)*
`dedupekey`
- `{{dedupekey}}`
- `{{{dedupekey}}}`
`title`
- `{{title}}`
- `{{{title}}}`
`body`(none)
`type`
- `{{type}}`
- `{{{type}}}`
`severity`

See the child parameter`severity`in the following table,[Alarm Metadata](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm#alarm-metadata).
`timestampEpochMillis`
- `{{timestampEpochMillis}}`
- `{{{timestampEpochMillis}}}`
`timestamp`
- `{{timestamp}}`
- `{{{timestamp}}}`
`alarmMetaData`

See the child parameters in the following table,[Alarm Metadata](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm#alarm-metadata).
`version`
- `{{version}}`
- `{{{version}}}`

*The primary (shorter) dynamic variable performs HTML escaping. The secondary (longer) dynamic variable preserves input characters.

### Alarm Metadata

Alarm parameter[Dynamic variables](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)*
`id`
- `{{id}}`
- `{{{id}}}`
`status`
- `{{status}}`
- `{{{status}}}`
`severity`
- `{{severity}}`
- `{{{severity}}}`
`namespace`
- `{{namespace}}`
- `{{{namespace}}}`
`query`
- `{{query}}`
- `{{{query}}}`
`totalMetricsFiring`
- `{{totalMetricsFiring}}`
- `{{{totalMetricsFiring}}}`
`dimensions`
- `{{dimensions. <dimension-name> }}`
- `{{{dimensions. <dimension-name> }}}`

&lt;dimension-name&gt; is the name of the dimension.

The dimension name must be valid for the dynamic variable to be rendered in the alarm message.

The dynamic variable renders the first returned value. That is, if multiple distinct values are returned, the first value is selected for rendering.

Example 1: Multiple distinct values from the`target`dimension
- `{{dimensions.target}}`
- `{{{dimensions.target}}}`

Values:`target1`,`target2`

Associated raw message content:
```

```

In this example, the first returned value`target1`is selected for rendering.

Example 2: Single value from the`faultdomain`dimension
- `{{dimensions.faultdomain}}`
- `{{{dimensions.faultdomain}}}`

Value:`FAULT-DOMAIN-3`

Associated raw message content:
```

```

`metricValues`
- `{{metricValues}}`
- `{{{metricValues}}}`

Example value:`[{CpuUtilization[1m].mean():92,disUtil[1m].mean():95}]`

Associated raw message content:`metricValues:[{CpuUtilization[1m].mean():92,disUtil[1m].mean():95}]`
`alarmUrl`
- `{{alarmUrl}}`
- `{{{alarmUrl}}}`
`alarmSummary`
- `{{alarmSummary}}`
- `{{{alarmSummary}}}`
`notificationType`
- `{{notificationType}}`
- `{{{notificationType}}}`

*The primary (shorter) dynamic variable performs HTML escaping. The secondary (longer) dynamic variable preserves input characters.

## Default Formatted Message Appearance

The following tables list default appearance of each alarm message parameter in formatted[alarm messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm).

### Alarm

Alarm parameter Default formatted[message](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm)appearance
`dedupekey`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Dedupe key
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Dedupe key
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`title`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Name
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Unlabeled, part of title
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Unlabeled, part of message
`body`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Body
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Unlabeled, part of title
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`type`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Type
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Type
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Unlabeled, part of message
`severity`Omitted by default
`timestampEpochMillis`Omitted by default
`timestamp`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Time
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Time
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Unlabeled, part of message
`alarmMetaData`

See the child parameters in the following table,[Alarm Metadata](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-format.htm#alarm-metadata).
`version`Omitted by default

### Alarm Metadata

Alarm parameter Default formatted[message](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm)appearance
`id`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Alarm OCID
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Alarm OCID
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`status`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): State
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Status
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`severity`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Severity
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Severity
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Unlabeled, part of message
`namespace`Omitted by default
`query`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Query
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Query
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`totalMetricsFiring`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Number of metrics breaching threshold
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Number of metric streams breaching threshold
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`dimensions`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Dimensions
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Dimensions
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`metricValues`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Metric values, ordered by dimension
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Metric values, ordered by dimension
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`alarmUrl`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): View Alarm in Console
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Unlabeled, part of title
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`alarmSummary`
- [Email (formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#email-formatted): Alarm Summary (button at bottom of message)
- [Slack](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#slack): Omitted by default
- [SMS](https://docs.oracle.com/en-us/iaas/Content/Monitoring/alarm-message-examples.htm#sms): Omitted by default
`notificationType`
