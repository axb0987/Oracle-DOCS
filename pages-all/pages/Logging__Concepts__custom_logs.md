# Custom Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs.htm
- Fetched: 2026-09-05 02:36 CDT

# Custom Logs

Custom logs are logs that contain diagnostic information from custom applications, other cloud providers, or an on-premise environment.
Custom logs can be ingested in the following ways:
- 

By using[PutLogs](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/LogEntry/PutLogs)to ingest custom logs directly. See the[Logging Ingestion API](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/)and[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)for more information. Also see[Ingesting Custom Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/using_the_api_customlogs.htm)for an example log entry payload that can be used with[PutLogs](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/LogEntry/PutLogs).
- 

By configuring the Unified Monitoring Agent. See[Installing the Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/installing_the_agent.htm)for instructions.
Note  
  
When managing Oracle Cloud Agent plugins, the Unified Monitoring Agent is referred to as "Custom Logs Monitoring".

Custom logs can be viewed in the Oracle Cloud Infrastructure Compute instance page, and have an associated Logs resource. They can also be viewed on the Logging Search page, Logs page, or within an associated Log Groups detail page. Custom logs are also supported in bare metal instances.
Note  
  
You can also view the rate at which custom logs are being accepted and ingested by using the Oracle Cloud Infrastructure Monitoring service. See[Viewing the Custom Logs Acceptance Rate](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/viewing_custom_logs_acceptance_rate.htm)for more information.

The Unified Monitoring Agent can be installed on many machines, and it pulls logs from local directories, where your apps or systems emit logs. The agent can also parse your logs for you. All of this is configured in Agent Configurations . You can create an agent configuration separately, and then associate a custom log with it, or create a custom log and then later create its agent configuration.
An agent configuration is the central mechanism for defining:
- What hosts you want logs from.
- What specific logs you want from the hosts.
- Additional parsers.
- The custom log destination.

Creating a custom log is a two-step process, in that you create the custom log object first, and then second, create its associated agent configuration. See[Creating a Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/create-logging-log.htm)for more information on creating custom logs and agent configurations, and[Agent Management Overview](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/agent_management.htm)for more information on setting up and managing the agent.
Note  
  
For the agent to run correctly, ensure that your firewall settings allow the following URI endpoints:
- https://auth. &lt;your region&gt; .oraclecloud.com
- https://ingestion.logging. &lt;your region&gt; .oci.oraclecloud.com.

## Custom Log Metadata and Storage Charging

Custom log metadata is added during ingestion in two places to optimize storage costs:
- At the request level
- At the log line level

A request is a collection of log lines, and the request can include one or more log lines in it. These requests can include a batch of log lines that were ingested, and then subsequent calls to ingest additional log lines can occur. A request can also have a different amount of log lines, depending on how customers are sending data. Customers are only charged one time for the metadata at the request level. As additional log lines in a request are ingested, no additional charges are incurred at this level. The request metadata applies to all the log lines in a request at the request level, instead of adding additional metadata to each log line, which helps save on storage costs.

The following is example request level metadata:
```

```

The minimum request metadata size is 500 bytes , but the amount can vary depending on the size of customer data in the`source`,`subject`, and`type`fields. The total metadata size can vary depending on the customer's particular data in these fields.

At the log line level, which contains the actual log payload, the following 100 byte metadata is added for each log line:
```

```

The`id`and`time`are mandatory, and indicate the corresponding log event, along with creation time.
For example (assuming empty data in the`source`,`subject`, and`type`fields), if the Oracle Cloud Infrastructure Logging Unified Monitoring Agent received a request with 100 log lines, where each log line was 1 KB in size, then the total added metadata size is around 10.5 KB per the following calculation:
- Request level: 500 bytes
- Log line level: 100 (number of log lines in a request) * 100 bytes (each log line metadata) = 10 KB
