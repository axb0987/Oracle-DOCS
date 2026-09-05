# Monitoring Key Usage
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys-usage.htm
- Fetched: 2026-09-05 02:35 CDT

# Monitoring Key Usage

Learn how to monitor key usage in Oracle Cloud Infrastructure using log data.

Monitoring the use of keys for encrypt and decrypt operations can be valuable for several use cases, including the following:
- Lifecycle management: Understanding when a key was last used is critical for making informed retention decisions. Infrequently used keys, such as those supporting database workloads, might still be operationally important despite limited activity. Extending log retention through OCI[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)enables deeper visibility into historical usage patterns, letting teams make risk-aware decisions about whether to retain, rotate, or retire keys.
- Security: Monitoring key usage can alert you to unusual activity.
- Monitoring or investigating application behavior: Correlating application behavior with key usage can give you useful information for resolving issues with your applications or improving their performance.

This topic details how you can use Oracle Cloud Infrastructure (OCI) logs to monitor key usage.

## Available Logging Data

The OCI[Logging Service](https://docs.oracle.com/iaas/Content/Logging/home.htm)provides several kinds of logs, including the following:

### Audit Logs

[Audit Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm): Use audit logs to monitor management operations such as:
- Create, update, and delete operations for managing keys and vaults
- Rotate operations for keys

Audit logs do not record cryptographic operations such as`Decrypt`or`GenerateDataEncryptionKey`(data plane activity), which are instead optionally recorded in Service Logs.

### Service Logs

[Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm)must be enabled by the customer to be used. When enabled for Key Management, service logs capture metadata including:
- Calling principal (the user, function, or instance that instigates the key operation)
- Key OCID
- Key version
- Operation type (for example,`Decrypt`)
- Timestamp
- Vault and compartment details
Important  
  
Service logs don't record sensitive information that would compromise data security for your organization or your customers. See[Details for Key Management](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_kms.htm)for complete details on the data that service logs collect for Key Management.

## Enabling Service Logs for a Vault

To enable service logs, you need the required IAM permissions. See[Details for Logging](https://docs.oracle.com/iaas/Content/Identity/policyreference/loggingpolicyreference.htm)in the IAM Service documentation for information.

Note that service logs are enabled at the vault level. Repeat the steps in this topic for each regional vault for which you want to enable logging.

See[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm)in the Logging Service documentation for more information.

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Select Enable Service Log .
- Configure the log as follows:

- Compartment: Select the compartment containing the vault for which you're enabling logging.
- Service: Key Management
- Resource: Select the vault you want to monitor using service logs.
- Log Category: Crypto Operations.
- Log Name: Enter a name for the log.
- Select Enable Logging .

## View and Query KMS Logs

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Navigate to a service log you have created for a vault in the list view of logs. See[Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm)if you need instructions.
- Use the Sort and Filter by time controls to control which log entries display in the Explore Log list of entries. The type column displays the type of crypto operation that the entry represents. For example, an entry for a decrypt operation has the following entry type:

`keymanagementservice.vault.crypto.decrypt`

The following image shows an example log with a list of log entries:
[
- To see the full details for a log entry, select the arrow at the end of the row for the entry to expand the entry and view a JSON-formatted view of the entry details.

The following image shows an example of the details for a log entry in the JSON format:
[
```

```

- To search for entries by a custom query, select Actions , then select Explore with Log Search . The Basic Mode for log search is displayed by default and lets you type keywords (such as "encrypt") or unique values or strings (such as a`principalId`value) into the Custom filters field. You can also select Advanced Mode and use query syntax to search the log. See[Getting a Log's Details](https://docs.oracle.com/iaas/Content/Logging/Task/get-logging-log.htm)and[Logging Search](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm)for more information on searching logs.

## Sending Logs to Object Storage or External Platforms Such as SIEM

By default, service logs are stored for 30 days. For long-term retention or external analysis, use[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)to forward logs to target destinations such:
- Object Storage
- Log Analytics
- External targets such as SIEM

See the following topics for more information:
- [Creating a Connector with a Logging Source](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-logging-source.htm)
- [Log Analytics](https://docs.oracle.com/iaas/log-analytics/home.htm)
- [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)
