# Log Inputs and Parsers
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/log_inputs_and_parsers.htm
- Fetched: 2026-09-05 02:36 CDT

# Log Inputs and Parsers

Use agent configurations to select which types of logs you want to ingest, and how to parse them.

You can configure a parser when you're[creating a custom log](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/create-logging-log.htm#console)and are setting up the[agent configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/agent-configuration-management.htm)(in the Create custom log panel, Create agent config step 2, see under Agent configuration , Configure log inputs , and click Advanced parser options ).

The following are the supported log inputs in agent configurations:
- Windows Event Logs
- Log Directory (Tail)
Important  
  
Any log data field can't be more than 10,000 characters. If the data exceeds this limit, the field is truncated during ingestion. For more information, see[Logging Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#servicelimits_topic_Logging_Limits).

For Log Directory inputs, you can specify parsers to structure your logs. The following are the list of supported parsers:
- None
- Auditd ([https://github.com/linux-audit/audit-documentation/wiki](https://github.com/linux-audit/audit-documentation/wiki))
- CRI ([https://github.com/fluent/fluent-plugin-parser-cri](https://github.com/fluent/fluent-plugin-parser-cri))
- JSON ([https://docs.fluentd.org/parser/json](https://docs.fluentd.org/parser/json))
- CSV ([https://docs.fluentd.org/parser/csv](https://docs.fluentd.org/parser/csv))
- TSV ([https://docs.fluentd.org/parser/tsv](https://docs.fluentd.org/parser/tsv))
- Syslog ([https://docs.fluentd.org/parser/syslog](https://docs.fluentd.org/parser/syslog))
- Apache2 ([https://docs.fluentd.org/parser/apache2](https://docs.fluentd.org/parser/apache2))
- Apache_Error ([https://docs.fluentd.org/parser/apache_error](https://docs.fluentd.org/parser/apache_error))
- Msgpack ([https://docs.fluentd.org/parser/msgpack](https://docs.fluentd.org/parser/msgpack))
- Regexp ([https://docs.fluentd.org/parser/regexp](https://docs.fluentd.org/parser/regexp))
- Multiline ([https://docs.fluentd.org/parser/multiline](https://docs.fluentd.org/parser/multiline)
