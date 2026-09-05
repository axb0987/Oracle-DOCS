# Details for Autonomous AI Database on Dedicated Exadata Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/autonomousdb-dedicatedexadata.htm
- Fetched: 2026-09-05 02:36 CDT

# Details for Autonomous AI Database on Dedicated Exadata Infrastructure

Logging details for Autonomous AI Database on Dedicated Exadata Infrastructure logs.

## Resources
- Autonomous Container Database
- Autonomous AI Database
- Autonomous VM cluster (For CC)
- Cloud Autonomous VM Cluster (For OPC)

## Log Categories

Resource Type Console (Display Name) Description
`AutonomousContainerDatabase`Database logs

Contains content from log files:
- Attention logs: $ORACLE_BASE/diag/rdbms/ &lt;ORACLE_UNQNAME&gt; /$ORACLE_SID/log/attention.log
- Alert logs: $ORACLE_BASE/diag/rdbms/ &lt;ORACLE_UNQNAME&gt; /$ORACLE_SID/trace/alert_$ORACLE_SID.log
`AutonomousDatabase`Migration logs

Contains content from log files:
- /u02/data/dbfs/ &lt;CDB_NAME&gt; / &lt;PDBGUID&gt; /import*.log
- /u02/data/dbfs/ &lt;CDB_NAME&gt; / &lt;PDBGUID&gt; /export*.log

`CloudAutonomousVmCluster`

`AutonomousVmCluster`Mongo connection logs

Path: /u02/app/oracle/product/ords/log/mongo/*

Example:

/u02/app/oracle/product/ords/log/mongo/mongo_2025-05-30_223911.log.0

/u02/app/oracle/product/ords/log/mongo/mongo_2025-05-30_224359.log.0

/u02/app/oracle/product/ords/log/mongo/mongo_2025-06-24_023705.log.0.lck

`CloudAutonomousVmCluster`

`AutonomousVmCluster`Network Logs

Path:

$ORACLE_BASE/diag/tnslsnr/$HOSTNAME/listener/trace/listener.log

$ORACLE_BASE/diag/tnslsnr/$HOSTNAME/listener_scan2/trace/listener_scan2.log

$ORACLE_BASE/diag/tnslsnr/$HOSTNAME/listener_scan3/trace/listener_scan3.log

Example:

/u01/app/grid/diag/tnslsnr/host-x9rgw2/listener/trace/listener.log

/u01/app/grid/diag/tnslsnr/host-x9rgw2/listener_scan1/trace/listener_scan1.log

/u01/app/grid/diag/tnslsnr/host-x9rgw1/listener_scan2/trace/listener_scan2.log

/u01/app/grid/diag/tnslsnr/host-x9rgw1/listener_scan3/trace/listener_scan3.log

`CloudAutonomousVmCluster`

`AutonomousVmCluster`ORDS connection logs

Path: /u02/app/oracle/product/ords/log/access/*

Example:

/u02/app/oracle/product/ords/log/access/ords_2025_09_05.log

/u02/app/oracle/product/ords/log/access/ords_2025_09_06.log

/u02/app/oracle/product/ords/log/access/ords_2025_09_07.log

/u02/app/oracle/product/ords/log/access/ords_2025_09_08.log

## Database Log

The database log captures important system events and alerts from the Autonomous Container Database. Use these logs to monitor database health and quickly detect issues

Property Description
level The severity level of the log entry (for example,`INFO`,`ERROR`).
message The text describing what the log entry reports, often details from the alert or attention log.
resourceId The OCID of the Autonomous Container Database resource.
@version Version of this log record format.
avmClusterId OCID identifying the Autonomous VM Cluster associated with the database.
host The hostname of the machine where the log was generated.
logFileType Type of log file (for example,`syslog`,`alertlog`).
msg The actual content or technical message from the log file.
oracle.logid OCID of the log object in Logging.
path File system path of the log file on the database server.
ts Time of the log record, in epoch milliseconds.
id Unique identifier for this log record.
oracle.compartmentid OCID of the OCI compartment.
oracle.ingestedtime When the log was ingested by OCI Logging, in ISO timestamp format.
oracle.loggroupid OCID of the log group containing the log.
oracle.tenantid OCID of the tenancy owning the resource.
source The source hostname for the log record.
specversion Version of the logging event specification (example:`1.0`).
subject Description or source path associated with the log event.
time Timestamp (ISO format) when the log event occurred.
type Type of log entry, such as`ALERTLOGS`.
regionId OCI region identifier for the resource.

## Sample Autonomous Container Database Log
```

```

## Migration Log

The migration log tracks Data Pump import and export operations for your Autonomous AI Database. Use these logs to audit migrations and troubleshoot data movement.

Property Description
level The severity level of this migration log entry (for example,`INFO`,`ERROR`).
message Description of contents—typically about Data Pump import/export job results.
resourceId The OCID of the Autonomous AI Database (PDB) being migrated or operated on.
@version Version of the log record format.
avmClusterId OCID of the Autonomous VM Cluster associated with the log.
host Name of the host machine generating the log.
logFileType Type of log file (generally`syslog`for migration events).
msg Actual log content, typically the output or result of a migration (import/export) job.
oracle.logid OCID of the log in OCI Logging.
path File path of the Data Pump log (typically export/import log files).
ts Epoch timestamp for the log event.
id Unique identifier for this migration log record.
oracle.compartmentid OCID of the OCI compartment for the resource.
oracle.ingestedtime When the log event was ingested into OCI Logging (ISO timestamp).
oracle.loggroupid OCID of the log group in which this log resides.
oracle.tenantid OCID for the tenancy containing the resource.
source Source hostname for the log event.
specversion Version of the log event specification.
subject Description or identifier for the resource or file connected to this log entry.
time Time of the event (ISO date/time format).
type Type of migration log, such as`DATAPUMPLOGS`.
regionId OCI region code where the event occurred.

## Sample Autonomous AI Database Migration Log
```

```
