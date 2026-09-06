# JMS Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#dcoc-content-body)

## JMS Common Types

### DBMS_CLOUD_OCI_JMS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_NEW_INSTALLATION_SITE_T Type

The properties of a new Java installation site.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`release_version`

(required) The release version of the Java Runtime.

`artifact_content_type`

(optional) Artifact content type for the Java version.

Allowed values are: 'JDK', 'JRE', 'SERVER_JRE'

`installation_path`

(optional) Custom path to install new Java installation site.

`headless_mode`

(optional) Flag to install headless or headful Java installation. Only valid for Oracle Linux in OCI.

`force_install`

(optional) Forces the installation request even if a more recent release is already present in the host.

### DBMS_CLOUD_OCI_JMS_NEW_INSTALLATION_SITE_TBL Type

Nested table type of dbms_cloud_oci_jms_new_installation_site_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_ADD_FLEET_INSTALLATION_SITES_DETAILS_T Type

The list of Java installation sites to add.

Syntax
```

```

Fields

Field Description

`installation_sites`

(required) The list of installation sites to add.

`post_installation_actions`

(optional) Optional list of post java installation actions

### DBMS_CLOUD_OCI_JMS_ADVANCED_USAGE_TRACKING_T Type

AdvancedUsageTracking configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) AdvancedUsageTracking flag to store enabled or disabled status.

### DBMS_CLOUD_OCI_JMS_PLUGIN_T Type

Information about the plugin.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the plugin.

`version`

(required) The version of the plugin.

### DBMS_CLOUD_OCI_JMS_PLUGIN_TBL Type

Nested table type of dbms_cloud_oci_jms_plugin_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_AGENT_T Type

Information about the agent.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the agent.

`l_type`

(required) The agent type.

Allowed values are: 'OMA', 'OCA'

`java_version`

(required) The java version.

`java_security_status`

(required) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`plugins`

(required) A list of plugins installed on this agent.

### DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_SUMMARY_T Type

An summary of a announcement on Console Overview page

Syntax
```

```

Fields

Field Description

`key`

(required) Unique id of the announcement

`summary`

(required) Summary text of the announcement

`url`

(required) URL to the announcement web page

`time_released`

(required) Date time on which the announcement was released

### DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_announcement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_COLLECTION_T Type

Results of list announcements call. Contains AnnouncementSummary items

Syntax
```

```

Fields

Field Description

`items`

(required) List of AnnouncementSummary items

### DBMS_CLOUD_OCI_JMS_OPERATING_SYSTEM_T Type

Operating System of the platform on which the Java Runtime was reported.

Syntax
```

```

Fields

Field Description

`family`

(required) The operating system type, such as Windows or Linux

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`name`

(required) The name of the operating system as provided by the Java system property os.name.

`version`

(required) The version of the operating system as provided by the Java system property os.version.

`architecture`

(required) The architecture of the operating system as provided by the Java system property os.arch.

`managed_instance_count`

(optional) Number of instances running the operating system.

### DBMS_CLOUD_OCI_JMS_OPERATING_SYSTEM_TBL Type

Nested table type of dbms_cloud_oci_jms_operating_system_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_T Type

Summarizes application installation usage information during a specified time period. The main difference between ApplicationUsage and ApplicationInstallationUsageSummary is the presence of installation information. ApplicationUsage provides only aggregated information for an application regardless of the installation paths. Therefore, two different applications with the same application name installed in two different paths will be aggregated to a single application. This aggregation makes it difficult to focus actions to single application installed on a known path. An application installation is independent of the Java Runtime on which it's running or the Managed Instance where it's installed.

Syntax
```

```

Fields

Field Description

`application_installation_key`

(required) An internal identifier for the application installation that is unique to a Fleet.

`application_key`

(required) An internal identifier for the application that is unique to a Fleet. ApplicationKey will be identical for applications with different installation information.

`display_name`

(required) The name of the application.

`application_type`

(required) The type of the application, denoted by how the application was started.

`installation_path`

(optional) The full path on which the application installation was detected.

`full_class_path`

(optional) List of full paths where the application last searched for classes. Contains full paths to all items from module-list and class path list.

`operating_systems`

(optional) The operating systems running this application.

`approximate_installation_count`

(optional) The approximate count of installations running this application.

`approximate_jre_count`

(optional) The approximate count of Java Runtimes running this application.

`approximate_managed_instance_count`

(optional) The approximate count of managed instances reporting this application.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_application_installation_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_COLLECTION_T Type

Results of an application installation search. Contains ApplicationInstallationUsageSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of application installations.

### DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_T Type

Application usage during a specified time period. An application is a Java application that can be executed by a Java Runtime installation. An application is independent of the Java Runtime or its installation.

Syntax
```

```

Fields

Field Description

`application_id`

(required) An internal identifier for the application that is unique to a Fleet.

`display_name`

(required) The name of the application.

`application_type`

(required) The type of the application, denoted by how the application was started.

`operating_systems`

(optional) The operating systems running this application.

`approximate_installation_count`

(optional) The approximate count of installations running this application.

`approximate_jre_count`

(optional) The approximate count of Java Runtimes running this application.

`approximate_managed_instance_count`

(optional) The approximate count of managed instances reporting this application.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_application_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_COLLECTION_T Type

Results of an application search. Contains ApplicationUsage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of applications.

### DBMS_CLOUD_OCI_JMS_WORK_ITEM_DETAILS_T Type

The minimum details of a work item.

Syntax
```

```

Fields

Field Description

`kind`

(required) The kind of work item details.

Allowed values are: 'BASIC', 'APPLICATION', 'LCM'

`work_item_type`

(optional) The work item type.

Allowed values are: 'LCM', 'JFR_CAPTURE', 'JFR_UPLOAD', 'CRYPTO_ANALYSIS', 'CRYPTO_ANALYSIS_MERGE', 'ADVANCED_USAGE_TRACKING', 'ADV_USAGE_SERVER_METADATA', 'ADV_USAGE_SERVER_LIBRARIES', 'ADV_USAGE_JAVA_LIBRARIES', 'PERFORMANCE_TUNING', 'JMIGRATE_ANALYSIS', 'JMIGRATE_CREATE_REPORT', 'DRS'

### DBMS_CLOUD_OCI_JMS_APPLICATION_WORK_ITEM_DETAILS_T Type

The work item details with JFR related information.

Syntax
```

```

`dbms_cloud_oci_jms_application_work_item_details_t`is a subtype of the`dbms_cloud_oci_jms_work_item_details_t`type.

Fields

Field Description

`application_key`

(required) The unique key of the application of the JFR.

`application_installation_key`

(optional) The unique key of the application installation of the JFR.

`application_name`

(required) The application name.

`application_installation_path`

(optional) The full path on which application installation was detected.

### DBMS_CLOUD_OCI_JMS_BASIC_WORK_ITEM_DETAILS_T Type

The common work item details.

Syntax
```

```

`dbms_cloud_oci_jms_basic_work_item_details_t`is a subtype of the`dbms_cloud_oci_jms_work_item_details_t`type.

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_TARGET_T Type

A resource to blocklist for certain operation.

Syntax
```

```

Fields

Field Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the fleet.

`managed_instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`installation_key`

(optional) The unique identifier for the installation of Java Runtime at a specific path on a specific operating system.

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_T Type

The blocklist record to prevent a target resource from certain operation with reason.

Syntax
```

```

Fields

Field Description

`key`

(required) The unique identifier of this blocklist record.

`target`

(required)

`operation`

(required) The operation type

Allowed values are: 'CREATE_FLEET', 'DELETE_FLEET', 'MOVE_FLEET', 'UPDATE_FLEET', 'UPDATE_FLEET_AGENT_CONFIGURATION', 'DELETE_JAVA_INSTALLATION', 'CREATE_JAVA_INSTALLATION', 'COLLECT_JFR', 'REQUEST_CRYPTO_EVENT_ANALYSIS', 'REQUEST_PERFORMANCE_TUNING_ANALYSIS', 'REQUEST_JAVA_MIGRATION_ANALYSIS', 'DELETE_JMS_REPORT', 'SCAN_JAVA_SERVER_USAGE', 'SCAN_LIBRARY_USAGE', 'EXPORT_DATA_CSV', 'CREATE_DRS_FILE', 'UPDATE_DRS_FILE', 'DELETE_DRS_FILE', 'ENABLE_DRS', 'DISABLE_DRS'

`reason`

(optional) The reason why the operation is blocklisted.

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_TBL Type

Nested table type of dbms_cloud_oci_jms_blocklist_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_COLLECTION_T Type

Results of a blocklist search that contain Blocklist records.

Syntax
```

```

Fields

Field Description

`items`

(required) The blocklist

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_ENTRY_T Type

An entry for blocklist to describe blocked operation and reason.

Syntax
```

```

Fields

Field Description

`operation`

(required) The operation type.

Allowed values are: 'CREATE_FLEET', 'DELETE_FLEET', 'MOVE_FLEET', 'UPDATE_FLEET', 'UPDATE_FLEET_AGENT_CONFIGURATION', 'DELETE_JAVA_INSTALLATION', 'CREATE_JAVA_INSTALLATION', 'COLLECT_JFR', 'REQUEST_CRYPTO_EVENT_ANALYSIS', 'REQUEST_PERFORMANCE_TUNING_ANALYSIS', 'REQUEST_JAVA_MIGRATION_ANALYSIS', 'DELETE_JMS_REPORT', 'SCAN_JAVA_SERVER_USAGE', 'SCAN_LIBRARY_USAGE', 'EXPORT_DATA_CSV', 'CREATE_DRS_FILE', 'UPDATE_DRS_FILE', 'DELETE_DRS_FILE', 'ENABLE_DRS', 'DISABLE_DRS'

`reason`

(required) The reason why the operation is blocklisted.

### DBMS_CLOUD_OCI_JMS_CHANGE_FLEET_COMPARTMENT_DETAILS_T Type

Attributes to change the compartment of a Fleet.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the Fleet should be moved.

### DBMS_CLOUD_OCI_JMS_CREATE_BLOCKLIST_DETAILS_T Type

The blocklist record details.

Syntax
```

```

Fields

Field Description

`target`

(required)

`operation`

(required) The operation type

Allowed values are: 'CREATE_FLEET', 'DELETE_FLEET', 'MOVE_FLEET', 'UPDATE_FLEET', 'UPDATE_FLEET_AGENT_CONFIGURATION', 'DELETE_JAVA_INSTALLATION', 'CREATE_JAVA_INSTALLATION', 'COLLECT_JFR', 'REQUEST_CRYPTO_EVENT_ANALYSIS', 'REQUEST_PERFORMANCE_TUNING_ANALYSIS', 'REQUEST_JAVA_MIGRATION_ANALYSIS', 'DELETE_JMS_REPORT', 'SCAN_JAVA_SERVER_USAGE', 'SCAN_LIBRARY_USAGE', 'EXPORT_DATA_CSV', 'CREATE_DRS_FILE', 'UPDATE_DRS_FILE', 'DELETE_DRS_FILE', 'ENABLE_DRS', 'DISABLE_DRS'

`reason`

(optional) The reason why the operation is blocklisted

### DBMS_CLOUD_OCI_JMS_CREATE_DRS_FILE_DETAILS_T Type

Details of the request to create DRS file in a Fleet.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket name where the DRS file is located.

`namespace`

(required) The namespace for Object Storage.

`drs_file_name`

(required) The name of the DRS file in Object Store.

### DBMS_CLOUD_OCI_JMS_CUSTOM_LOG_T Type

Custom Log for inventory or operation log.

Syntax
```

```

Fields

Field Description

`log_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log group.

`log_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log.

### DBMS_CLOUD_OCI_JMS_CREATE_FLEET_DETAILS_T Type

Attributes to create a Fleet.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the Fleet. The displayName must be unique for Fleets in the same compartment.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of the Fleet.

`description`

(optional) The Fleet's description. If nothing is provided, the Fleet description will be null.

`inventory_log`

(required)

`operation_log`

(optional)

`is_advanced_features_enabled`

(optional) Whether or not advanced features are enabled in this Fleet. Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

### DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_T Type

Metadata for the result of a crypto event analysis. The analysis result is stored in an Object Storage bucket.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID to identify this analysis results.

`work_request_id`

(optional) The OCID of the work request to start the analysis.

`aggregation_mode`

(required) The result aggregation mode

Allowed values are: 'JFR', 'MANAGED_INSTANCE'

`fleet_id`

(required) The fleet OCID.

`managed_instance_id`

(optional) The managed instance OCID.

`host_name`

(optional) The hostname of the managed instance.

`time_first_event`

(optional) Time of the first event in the analysis.

`time_last_event`

(optional) Time of the last event in the analysis.

`total_event_count`

(required) Total number of events in the analysis.

`summarized_event_count`

(required) Total number of summarized events. Summarized events are deduplicated events of interest.

`finding_count`

(required) Total number of findings with the analysis.

`non_compliant_finding_count`

(required) Total number of non-compliant findings with the analysis. A non-compliant finding means the application won't work properly with the changes introduced by the Crypto Roadmap version used by the analysis.

`time_created`

(optional) The time the result is compiled.

`crypto_roadmap_version`

(required) The Crypto Roadmap version used to perform the analysis.

`namespace`

(required) The Object Storage namespace of this analysis result.

`bucket_name`

(required) The Object Storage bucket name of this analysis result.

`object_name`

(required) The Object Storage object name of this analysis result.

### DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_SUMMARY_T Type

Summary of a crypto analysis result. The actual output of the analysis is stored in the Object Storage object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID to identify this analysis results.

`work_request_id`

(optional) The OCID of the work request to start the analysis.

`aggregation_mode`

(required) The result aggregation mode

Allowed values are: 'JFR', 'MANAGED_INSTANCE'

`fleet_id`

(required) The fleet OCID.

`managed_instance_id`

(optional) The managed instance OCID.

`host_name`

(optional) The hostname of the managed instance.

`time_first_event`

(optional) Time of the first event in the analysis.

`time_last_event`

(optional) Time of the last event in the analysis.

`total_event_count`

(required) Total number of events in the analysis.

`summarized_event_count`

(required) Total number of summarized events. Summarized events are deduplicated events of interest.

`finding_count`

(required) Total number of findings with the analysis.

`non_compliant_finding_count`

(required) Total number of non-compliant findings with the analysis. A non-compliant finding means the application won't work properly with the changes introduced by the Crypto Roadmap version used by the analysis.

`time_created`

(optional) The time the result is compiled.

`crypto_roadmap_version`

(required) The Crypto Roadmap version used to perform the analysis.

`namespace`

(required) The Object Storage namespace of this analysis result.

`bucket_name`

(required) The Object Storage bucket name of this analysis result.

`object_name`

(required) The Object Storage object name of this analysis result.

### DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_crypto_analysis_result_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_COLLECTION_T Type

List of Crypto event analysis results.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Crypto Event Analysis results.

### DBMS_CLOUD_OCI_JMS_SUMMARIZED_EVENTS_LOG_T Type

Summarized events log for advanced feature.

Syntax
```

```

Fields

Field Description

`log_group_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log group.

`log_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the log.

### DBMS_CLOUD_OCI_JMS_CRYPTO_EVENT_ANALYSIS_T Type

CryptoEventAnalysis configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) CryptoEventAnalysis flag to store enabled or disabled status.

`summarized_events_log`

(optional)

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_T Type

Summarize usage information about an application deployed on Java servers including installation information during a specified time period. The main difference between DeployedApplicationInstallationUsageSummary and DeployedApplicationUsage is the presence of the applicationSourcePath. DeployedApplicationUsage provides only an aggregated view to the deployed applications without installation information. It therefore doesn’t distinguish between applications with the identical deployment information deployed to different paths. DeployedApplicationInstallationUsageSummary contains installation information, and it’s therefore possible to target actions.

Syntax
```

```

Fields

Field Description

`application_installation_key`

(required) The internal identifier of the deployed application installation.

`application_key`

(required) The internal identifier of the deployed application. ApplicationKey will be identical for deployed applications with different applicationSourcePaths.

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related fleet.

`application_name`

(required) The name of the deployed application.

`application_type`

(optional) The type of the deployed application.

`application_source_path`

(optional) The full path to source WAR or EAR file for deployed application.

`is_clustered`

(optional) Whether or not the deployed application is clustered.

`approximate_java_server_instance_count`

(optional) The approximate count of Java Server instances running the deployed application installations.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_deployed_application_installation_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_COLLECTION_T Type

Results of a deployed application installation usage search. Contains deployed application installation usage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of deployed application installation usages.

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_T Type

Deployed application usage during a specified time period.

Syntax
```

```

Fields

Field Description

`application_key`

(required) The internal identifier of the deployed application.

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related fleet.

`application_name`

(required) The name of the deployed application.

`application_type`

(optional) The type of the deployed application.

`is_clustered`

(optional) Whether or not the deployed application is clustered.

`approximate_java_server_instance_count`

(optional) The approximate count of Java Server instances running the deployed application.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_deployed_application_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_COLLECTION_T Type

Results of a deployed application usage search. Contains deployed application usage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of deployed application usages.

### DBMS_CLOUD_OCI_JMS_DRS_TARGET_T Type

The target to manage DRS distribution. A target is a managed instance.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) OCID of the managed instance to manage DRS distribution.

### DBMS_CLOUD_OCI_JMS_DRS_TARGET_TBL Type

Nested table type of dbms_cloud_oci_jms_drs_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_MANAGE_DRS_DETAILS_T Type

Details of the request to manage DRS in active managed instance(s) in a Fleet. When the targets aren't specified, then all active managed instance(s) currently in the Fleet are selected.

Syntax
```

```

Fields

Field Description

`targets`

(optional) The targets to manage DRS.

### DBMS_CLOUD_OCI_JMS_DISABLE_DRS_DETAILS_T Type

Details of the request to disable DRS file from active managed instance(s) in a Fleet. When the targets aren't specified, then all active managed instance(s) currently in the Fleet are selected.

Syntax
```

```

Fields

Field Description

`manage_drs_details`

(optional)

### DBMS_CLOUD_OCI_JMS_DRS_FILE_T Type

A Deployment Rule Set(DRS) is a JAR (Java ARchive) file used in Java applications to enforce security and manage compatibility between different versions of Java applets and web start applications (https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/deployment_rules.html).

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket name where the DRS file is located.

`namespace`

(required) The namespace for Object Storage.

`drs_file_name`

(required) The name of the DRS file in Object Store.

`drs_file_key`

(required) The unique identifier of the DRS file in Object Storage.

`checksum_type`

(required) The checksum type for the DRS file in Object Storage.

Allowed values are: 'SHA256'

`checksum_value`

(required) The checksum value for the DRS file in Object Storage.

`is_default`

(required) To check if the DRS file is the detfault ones.

### DBMS_CLOUD_OCI_JMS_DRS_FILE_SUMMARY_T Type

A Deployment Rule Set(DRS) is a JAR (Java ARchive) file used in Java applications to enforce security and manage compatibility between different versions of Java applets and web start applications (https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/deployment_rules.html).

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket name where the DRS file is located.

`namespace`

(required) The namespace for Object Storage.

`drs_file_name`

(required) The name of the DRS file in Object Store.

`drs_file_key`

(required) The unique identifier of the DRS file in Object Storage.

`checksum_type`

(required) The checksum type for the DRS file in Object Storage.

Allowed values are: 'SHA256'

`checksum_value`

(required) The checksum value for the DRS file in Object Storage.

`is_default`

(required) To check if the DRS file is the detfault ones.

### DBMS_CLOUD_OCI_JMS_DRS_FILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_drs_file_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_DRS_FILE_COLLECTION_T Type

List of DRS details.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of DRS details.

### DBMS_CLOUD_OCI_JMS_ENABLE_DRS_DETAILS_T Type

Details of the request to enable DRS in active managed instance(s) in a Fleet. When the targets aren't specified, then all active managed instance(s) currently in the Fleet are selected.

Syntax
```

```

Fields

Field Description

`manage_drs_details`

(optional)

### DBMS_CLOUD_OCI_JMS_ERROR_T Type

An error code and message from an API request failure.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that describes the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_JMS_EXISTING_INSTALLATION_SITE_ID_T Type

The essential properties to identity a Java installation site.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`installation_key`

(required) The unique identifier for the installation of a Java Runtime at a specific path on a specific operating system.

### DBMS_CLOUD_OCI_JMS_EXPORT_SETTING_T Type

An export settings for JMS fleets.

Syntax
```

```

Fields

Field Description

`export_setting_key`

(optional) The internal identifier of the export setting.

`fleet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the fleet.

`export_duration`

(optional) The duration of data to be exported for fleets.

Allowed values are: 'LAST_30_DAYS', 'LAST_60_DAYS', 'LAST_90_DAYS'

`export_resources`

(optional) Resource to export data associated from the fleets.

Allowed values are: 'MANAGED_INSTANCE', 'MANAGED_INSTANCE_PLUS_JAVA_RUNTIME', 'MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION'

`is_cross_region_acknowledged`

(optional) Acknowledgement for cross region target bucket configuration.

`target_bucket_name`

(optional) The name of the bucket where data will be exported.

`target_bucket_namespace`

(optional) The namespace of the bucket where data will be exported.

`target_bucket_region`

(optional) The namespace of the bucket where data will be exported.

`export_frequency`

(optional) Schedule at which data will be exported.

Allowed values are: 'DAILY', 'WEEKLY', 'MONTHLY'

`is_enabled`

(required) ExportSetting flag to store enabled or disabled status.

`time_created`

(optional) The creation date and time of the export setting (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_last_modified`

(optional) The update date and time of the export setting (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_EXPORT_STATUS_T Type

Attributes of fleet's export status.

Syntax
```

```

Fields

Field Description

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the fleet.

`time_last_run`

(required) The date and time of the last export run.

`time_next_run`

(required) The date and time of the next export run.

`latest_run_status`

(required) The status of the latest export run.

Allowed values are: 'SCHEDULED', 'PENDING', 'IN_PROGRESS', 'FAILED', 'RETRYING', 'SUCCEEDED'

### DBMS_CLOUD_OCI_JMS_FLEET_T Type

A Fleet is the primary collection with which users interact when using Java Management Service.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`display_name`

(required) The name of the Fleet.

`description`

(required) The Fleet's description.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of the Fleet.

`approximate_jre_count`

(required) The approximate count of all unique Java Runtimes in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_installation_count`

(required) The approximate count of all unique Java installations in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_application_count`

(required) The approximate count of all unique applications in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_managed_instance_count`

(required) The approximate count of all unique managed instances in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_java_server_count`

(required) The approximate count of all unique Java servers in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`inventory_log`

(optional)

`operation_log`

(optional)

`is_advanced_features_enabled`

(optional) Whether or not advanced features are enabled in this Fleet. Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.

`is_export_setting_enabled`

(optional) Whether or not export setting is enabled in this Fleet.

`time_created`

(required) The creation date and time of the Fleet (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`lifecycle_state`

(required) The lifecycle state of the Fleet.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_KEY_SIZE_ALGORITHM_T Type

The algorithm object with name and key size properties.

Syntax
```

```

Fields

Field Description

`name`

(optional) The algorithm name.

Allowed values are: 'RSA', 'DSA', 'EC', 'DH'

`key_size`

(optional) Key size for the encryption algorithm. Allowed values: 256 for EC, 2048 for DH/DSA/RSA

### DBMS_CLOUD_OCI_JMS_KEY_SIZE_ALGORITHM_TBL Type

Nested table type of dbms_cloud_oci_jms_key_size_algorithm_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_MINIMUM_KEY_SIZE_SETTINGS_T Type

test

Syntax
```

```

Fields

Field Description

`tls`

(optional) Updates the minimum key size for the specified encryption algorithm. The JDK property jdk.tls.disabledAlgorithms will be updated with the following supported actions: - Changing minimum key length for Diffie-Hellman

`jar`

(optional) Updates the minimum key size for the specified encryption algorithm. The JDK property jdk.jar.disabledAlgorithms will be updated with the following supported actions: - Changing minimum key length for RSA signed jars - Changing minimum key length for EC - Changing minimum key length for DSA

`certpath`

(optional) Updates the minimum key size for the specified encryption algorithm. The JDK property jdk.certpath.disabledAlgorithms will be updated with the following supported actions: - Changing minimum key length for RSA signed jars - Changing minimum key length for EC - Changing minimum key length for DSA

### DBMS_CLOUD_OCI_JMS_PROXIES_T Type

List of proxy properties to be configured in net.properties file.

Syntax
```

```

Fields

Field Description

`use_system_proxies`

(optional) Sets \"java.net.useSystemProxies=true\" in net.properties when they exist.

`http_proxy_host`

(optional) Http host to be set in net.properties file.

`http_proxy_port`

(optional) Http port number to be set in net.properties file.

`https_proxy_host`

(optional) Https host to be set in net.properties file.

`https_proxy_port`

(optional) Https port number to be set in net.properties file.

`ftp_proxy_host`

(optional) Ftp host to be set in net.properties file.

`ftp_proxy_port`

(optional) Ftp port number to be set in net.properties file.

`socks_proxy_host`

(optional) Socks host to be set in net.properties file.

`socks_proxy_port`

(optional) Socks port number to be set in net.properties file.

### DBMS_CLOUD_OCI_JMS_POST_INSTALLATION_ACTION_SETTINGS_T Type

List of available post actions you can execute after the successful Java installation.

Syntax
```

```

Fields

Field Description

`disabled_tls_versions`

(optional) The following post JRE installation actions are supported by the field: - Disable TLS 1.0 , TLS 1.1

`should_replace_certificates_operating_system`

(optional) Restores JDK root certificates with the certificates that are available in the operating system. The following action is supported by the field: - Replace JDK root certificates with a list provided by the operating system.

`minimum_key_size_settings`

(optional)

`add_logging_handler`

(optional) Sets FileHandler and ConsoleHandler as handlers in logging.properties file.

`global_logging_level`

(optional) Sets the logging level in logging.properties file.

Allowed values are: 'ALL', 'SEVERE', 'WARNING', 'INFO', 'CONFIG', 'FINE', 'FINER', 'FINEST', 'OFF'

`proxies`

(optional)

### DBMS_CLOUD_OCI_JMS_LCM_T Type

Enable lifecycle management and set post action configurations.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Lifecycle management flag to store enabled or disabled status.

`post_installation_actions`

(optional)

### DBMS_CLOUD_OCI_JMS_JFR_RECORDING_T Type

JfrRecording configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) JfrRecording flag to store enabled or disabled status.

### DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_T Type

Performance tuning analysis configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) PerformanceTuningAnalysis flag to store enabled or disabled status

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_T Type

JavaMigrationAnalysis configuration

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) JavaMigrationAnalysis flag to store enabled or disabled status.

### DBMS_CLOUD_OCI_JMS_FLEET_ADVANCED_FEATURE_CONFIGURATION_T Type

Metadata for the advanced features in the Fleet.

Syntax
```

```

Fields

Field Description

`analytic_namespace`

(required) Namespace for the Fleet advanced feature.

`analytic_bucket_name`

(required) Bucket name required to store JFR and related data.

`lcm`

(required)

`crypto_event_analysis`

(required)

`advanced_usage_tracking`

(required)

`jfr_recording`

(required)

`performance_tuning_analysis`

(required)

`java_migration_analysis`

(required)

`time_last_modified`

(required) The date and time of the last modification to the Fleet Agent Configuration (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_FLEET_AGENT_OS_CONFIGURATION_T Type

Management Agent Configuration for list of include/exclude file system paths (specific to operating system).

Syntax
```

```

Fields

Field Description

`include_paths`

(required) An array of file system paths (environment variables supported).

`exclude_paths`

(required) An array of file system paths (environment variables supported).

### DBMS_CLOUD_OCI_JMS_FLEET_AGENT_CONFIGURATION_T Type

Management Agent Configuration for a Fleet. Includes JRE scanning frequency and a list of include/exclude file system paths.

Syntax
```

```

Fields

Field Description

`jre_scan_frequency_in_minutes`

(required) The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)

`java_usage_tracker_processing_frequency_in_minutes`

(required) The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)

`work_request_validity_period_in_days`

(optional) The validity period in days for work requests.

`agent_polling_interval_in_minutes`

(optional) Agent polling interval in minutes

`linux_configuration`

(required)

`windows_configuration`

(required)

`mac_os_configuration`

(required)

`time_last_modified`

(required) The date and time of the last modification to the Fleet Agent Configuration (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_FLEET_SUMMARY_T Type

The summary of the Fleet. A Fleet is the primary collection with which users interact when using Java Management Service.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Fleet.

`display_name`

(required) The name of the Fleet. The displayName must be unique for Fleets in the same compartment.

`description`

(required) The Fleet's description.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment of the Fleet.

`approximate_jre_count`

(required) The approximate count of all unique Java Runtimes in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_installation_count`

(required) The approximate count of all unique Java Installations in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_application_count`

(required) The approximate count of all unique applications in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_managed_instance_count`

(required) The approximate count of all unique managed instances in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`approximate_java_server_count`

(required) The approximate count of all unique Java servers in the Fleet in the past seven days. This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.

`inventory_log`

(optional)

`operation_log`

(optional)

`is_advanced_features_enabled`

(optional) Whether or not advanced features are enabled in this Fleet. This flag is true if any one of the advanced features is turned on.

`is_export_setting_enabled`

(optional) Whether or not export setting is enabled in this Fleet.

`time_created`

(required) The creation date and time of the Fleet (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`lifecycle_state`

(required) The lifecycle state of the Fleet.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_JMS_FLEET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_fleet_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_FLEET_COLLECTION_T Type

Results of a Fleet search. Contains FleetSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Fleets.

### DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_SUMMARY_T Type

Diagnosis of a resource needed by the fleet.

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The type of the resource needed by the fleet. This is the role of a resource in the fleet. Use the OCID to determine the actual OCI resource type such as log group or log.

Allowed values are: 'INVENTORY_LOG', 'OPERATION_LOG', 'CRYPTO_SUMMARIZED_LOG', 'ANALYSIS_OSS_BUCKET'

`resource_id`

(optional) The OCID of the external resouce needed by the fleet.

`resource_state`

(optional) The state of the resource. The resource state is ACTIVE when it works properly for the fleet. In case it would cause an issue for the fleet function, the state is INACTIVE. When JMS can't locate the resource, the state is NOT_FOUND. OTHER covers other cases, such as a temporarily network issue that prevents JMS from detecting the resource. Check the resourceDiagnosis for details.

Allowed values are: 'ACTIVE', 'INACTIVE', 'NOT_FOUND', 'OTHER'

`resource_diagnosis`

(optional) The diagnosis message.

### DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_fleet_diagnosis_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_COLLECTION_T Type

List of the fleet resource diagnosis.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the fleet resource diagnosis.

### DBMS_CLOUD_OCI_JMS_GENERATE_AGENT_DEPLOY_SCRIPT_DETAILS_T Type

Attributes to generate agent deploy script for a Fleet.

Syntax
```

```

Fields

Field Description

`install_key_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the install key for which to generate the script.

`os_family`

(required) The operating system type for the script. Currently only 'LINUX' and 'WINDOWS' are supported.

Allowed values are: 'LINUX', 'WINDOWS', 'MACOS', 'UNKNOWN'

`is_user_name_enabled`

(required) Enable/disable user name collection on agent.

### DBMS_CLOUD_OCI_JMS_JAVA_RUNTIME_ID_T Type

The essential properties to identify a Java Runtime.

Syntax
```

```

Fields

Field Description

`version`

(required) The version of the Java Runtime.

`vendor`

(required) The vendor of the Java Runtime.

`distribution`

(required) The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.

`jre_key`

(optional) The unique identifier for a Java Runtime.

### DBMS_CLOUD_OCI_JMS_BLOCKLIST_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_jms_blocklist_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_T Type

Installation site of a Java Runtime. An installation site is a Java Runtime installed at a specific path on a managed instance.

Syntax
```

```

Fields

Field Description

`installation_key`

(required) The unique identifier for the installation of a Java Runtime at a specific path on a specific operating system.

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`jre`

(required)

`path`

(required) The file system path of the installation.

`operating_system`

(required)

`approximate_application_count`

(optional) The approximate count of applications running on this installation

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

`blocklist`

(optional) The list of operations that are blocklisted.

`lifecycle_state`

(optional) The lifecycle state of the installation site.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

`managed_instance_type`

(optional) The type of the source of events.

Allowed values are: 'ORACLE_MANAGEMENT_AGENT'

`hostname`

(optional) The hostname of the managed instance (if applicable).

### DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_SUMMARY_T Type

Installation site of a Java Runtime. An installation site is a Java Runtime installed at a specific path on a managed instance.

Syntax
```

```

Fields

Field Description

`installation_key`

(required) The unique identifier for the installation of Java Runtime at a specific path on a specific operating system.

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`jre`

(optional)

`security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`path`

(optional) The file system path of the installation.

`operating_system`

(optional)

`approximate_application_count`

(optional) The approximate count of applications running on this installation

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

`blocklist`

(optional) The list of operations that are blocklisted.

`lifecycle_state`

(optional) The lifecycle state of the installation site.

Allowed values are: 'ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'UPDATING'

### DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_installation_site_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_COLLECTION_T Type

Results of an installation site search. Contains installation sites.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java installation sites.

### DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_T Type

Installation usage during a specified time period. An installation is a collection of deployed instances of a specific Java Runtime that share the same install path.

Syntax
```

```

Fields

Field Description

`installation_key`

(optional) The unique identifier for the installation of a Java Runtime at a specific path on a specific operating system.

`jre_vendor`

(required) The vendor of the Java Runtime that is deployed with the installation.

`jre_distribution`

(required) The distribution of the Java Runtime that is deployed with the installation.

`jre_version`

(required) The version of the Java Runtime that is deployed with the installation.

`path`

(required) The file system path of the Java installation.

`os`

(required) The Operating System for the installation. Deprecated, use `operatingSystem` instead.

`architecture`

(required) The architecture of the operating system for the installation. Deprecated, use `operatingSystem` instead.

`operating_system`

(optional)

`approximate_application_count`

(optional) The approximate count of applications running on this installation

`approximate_managed_instance_count`

(optional) The approximate count of managed instances reporting this installation

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_installation_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_COLLECTION_T Type

Results of an installation search. Contains InstallationUsage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of installations.

### DBMS_CLOUD_OCI_JMS_JAVA_ARTIFACT_T Type

Information about a binary artifact of Java.

Syntax
```

```

Fields

Field Description

`artifact_id`

(required) Unique identifier for the artifact.

`artifact_description`

(required) Description of the binary artifact. Typically includes the OS, architecture, and installer type.

`artifact_content_type`

(required) Product content type of this artifact.

Allowed values are: 'JDK', 'JRE', 'SERVER_JRE'

`approximate_file_size_in_bytes`

(required) Approximate compressed file size in bytes.

`sha256`

(required) SHA256 checksum of the artifact.

`artifact_file_name`

(optional) The file name of the artifact.

`os_family`

(required) The target Operating System family for the artifact.

`architecture`

(required) The target Operating System architecture for the artifact.

`package_type`

(required) The package type(typically the file extension) of the artifact.

`package_type_detail`

(optional) Additional information about the package type.

`download_url`

(required) The endpoint that returns a short-lived artifact download URL in the response payload. This download url can then be used for downloading the artifact. See this[API](https://docs.oracle.com/iaas/api/#/en/jms/20230601/JavaArtifact/GenerateArtifactDownloadUrl)for more details.

`script_download_url`

(required) The endpoint for downloading this artifact from command line, automatically in scripts and dockerfiles. Depending on the context, this can point to the archive or latest update release version artifact in the specified family.

`script_checksum_url`

(required) The URL for retrieving the checksum for the artifact. Depending on the context, this can point to the checksum of the archive or latest update release version artifact.

### DBMS_CLOUD_OCI_JMS_JAVA_ARTIFACT_TBL Type

Nested table type of dbms_cloud_oci_jms_java_artifact_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_T Type

Metadata associated with a specific Java release family. A Java release family is typically a major version in the Java version identifier.

Syntax
```

```

Fields

Field Description

`latest_release_artifacts`

(optional) List of artifacts for the latest Java release version in this family. The script URLs in the response can be used from a command line, or in scripts and dockerfiles to always get the artifacts corresponding to the latest update release version.

`family_version`

(required) The Java release family identifier.

`display_name`

(required) The display name of the release family.

`support_type`

(required) This indicates the support category for the Java release family.

Allowed values are: 'LTS', 'NON_LTS'

`end_of_support_life_date`

(required) The End of Support Life (EOSL) date of the Java release family (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`doc_url`

(required) Link to access the documentation for the release.

`latest_release_version`

(required) Latest Java release version in the family.

`is_supported_version`

(required) Whether or not this Java release family is under active support. Refer[Java Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)for more details.

### DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_SUMMARY_T Type

A summary of the Java release family information. A Java release family is typically a major version in the Java version identifier.

Syntax
```

```

Fields

Field Description

`family_version`

(required) The Java release family identifier.

`display_name`

(required) The display name of the release family.

`support_type`

(required) This indicates the support category for the Java release family.

Allowed values are: 'LTS', 'NON_LTS'

`end_of_support_life_date`

(required) The End of Support Life (EOSL) date of the Java release family (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`doc_url`

(required) Link to access the documentation for the release.

`latest_release_version`

(required) Latest Java release version in the family.

`is_supported_version`

(required) Whether or not this Java release family is under active support. Refer[Java Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)for more details.

### DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_family_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_COLLECTION_T Type

Collection of the Java release family summary. A Java release family is typically a major version in the Java version identifier.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the Java Release family summary.

### DBMS_CLOUD_OCI_JMS_JAVA_LICENSE_T Type

Information about a license type for Java.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Commonly used name for the license type.

`license_type`

(required) License Type

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`license_url`

(required) Publicly accessible license URL containing the detailed terms and conditions.

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_T Type

Result of the Java migration analysis. The analysis result is stored in an Object Storage bucket.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the migration analysis report.

`work_request_id`

(optional) The OCID of the work request of this analysis.

`fleet_id`

(required) The fleet OCID.

`application_key`

(optional) The unique key that identifies the application.

`application_name`

(required) The name of the application for which the Java migration analysis was performed.

`application_path`

(required) The installation path of the application for which the Java migration analysis was performed.

`application_execution_type`

(required) Execution type of the application for an application type, such as WAR and EAR, that is deployed or installed.

Allowed values are: 'INSTALLED', 'DEPLOYED'

`source_jdk_version`

(required) The source JDK version of the application that's currently running.

`target_jdk_version`

(required) The target JDK version of the application to be migrated.

`managed_instance_id`

(optional) The managed instance OCID.

`host_name`

(optional) The hostname of the managed instance that hosts the application for which the Java migration analysis was performed.

`time_created`

(optional) The time the result is compiled.

`namespace`

(required) The object storage namespace that contains the results of the migration analysis.

`bucket_name`

(required) The name of the object storage bucket that contains the results of the migration analysis.

`object_storage_upload_dir_path`

(required) The directory path of the object storage bucket that contains the results of the migration analysis.

`object_list`

(required) The names of the object storage objects that contain the results of the migration analysis.

`metadata`

(required) Additional info reserved for future use.

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_SUMMARY_T Type

Summary of a Java migration analysis result. The output of the analysis is stored in the Object Storage object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the migration analysis report.

`work_request_id`

(optional) The OCID of the work request of this analysis.

`fleet_id`

(required) The fleet OCID.

`application_key`

(optional) The unique key that identifies the application.

`application_name`

(required) The name of the application for which the Java migration analysis was performed.

`application_path`

(required) The installation path of the application for which the Java migration analysis was performed.

`application_execution_type`

(required) Execution type of the application for an application type, such as WAR and EAR, that is deployed or installed.

Allowed values are: 'INSTALLED', 'DEPLOYED'

`source_jdk_version`

(required) The source JDK version of the application that's currently running.

`target_jdk_version`

(required) The target JDK version of the application to be migrated.

`managed_instance_id`

(optional) The managed instance OCID.

`host_name`

(optional) The hostname of the managed instance that hosts the application for which the Java migration analysis was performed.

`time_created`

(optional) The time the result is compiled.

`namespace`

(required) The object storage namespace that contains the results of the migration analysis.

`bucket_name`

(required) The name of the object storage bucket that contains the results of the migration analysis.

`object_storage_upload_dir_path`

(required) The directory path of the object storage bucket that contains the results of the migration analysis.

`object_list`

(required) The names of the object storage objects that contain the results of the migration analysis.

`metadata`

(required) Additional info reserved for future use.

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_migration_analysis_result_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_COLLECTION_T Type

List of Java migration analysis results.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java migration analysis results.

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_TARGET_T Type

The target describes the input data for Java migration analysis. A target contains a managed instance, application Installation Key, sourceJdkVersion, and targetJdkVersion.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) The OCID of the managed instance that hosts the application for which the Java migration analysis was performed.

`application_installation_key`

(required) The unique key that identifies the application's installation path that is to be used for the Java migration analysis.

`source_jdk_version`

(required) The JDK version the application is currently running on.

`target_jdk_version`

(required) The JDK version against which the migration analysis was performed to identify effort required to move from source JDK.

### DBMS_CLOUD_OCI_JMS_PATCH_DETAIL_T Type

My Oracle Support(MoS) patch details for the Java release.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Commonly used name for the MoS release.

`patch_url`

(required) MoS URL to access the artifacts for the Java release.

### DBMS_CLOUD_OCI_JMS_PATCH_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_jms_patch_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_T Type

Metadata associated with a specific release of Java. Includes the artifact details.

Syntax
```

```

Fields

Field Description

`artifacts`

(optional) List of Java artifacts.

`release_version`

(required) Java release version identifier.

`family_version`

(required) Java release family identifier.

`parent_release_version`

(optional) Parent Java release version identifier. This is applicable for BPR releases.

`security_status`

(required) The security status of the Java version.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`release_type`

(required) Release category of the Java version.

Allowed values are: 'CPU', 'FEATURE', 'BPR', 'PATCH_RELEASE'

`license_type`

(required) License type for the Java version.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`family_details`

(optional)

`license_details`

(optional)

`release_date`

(required) The release date of the Java version (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`release_notes_url`

(required) Release notes associated with the Java version.

`artifact_content_types`

(required) Artifact content types for the Java version.

Allowed values are: 'JDK', 'JRE', 'SERVER_JRE'

`mos_patches`

(optional) List of My Oracle Support(MoS) patches available for this release. This information is only available for `BPR` release type.

`days_under_security_baseline`

(optional) The number of days since this release has been under the security baseline.

### DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_SUMMARY_T Type

A summary of the Java release properties.

Syntax
```

```

Fields

Field Description

`release_version`

(required) Java release version identifier.

`family_version`

(required) Java release family identifier.

`parent_release_version`

(optional) Parent Java release version identifier. This is applicable for BPR releases.

`security_status`

(required) The security status of the Java version.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`release_type`

(required) Release category of the Java version.

Allowed values are: 'CPU', 'FEATURE', 'BPR', 'PATCH_RELEASE'

`license_type`

(required) License type for the Java version.

Allowed values are: 'OTN', 'NFTC', 'RESTRICTED'

`family_details`

(optional)

`license_details`

(optional)

`release_date`

(required) The release date of the Java version (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`release_notes_url`

(required) Release notes associated with the Java version.

`artifact_content_types`

(required) Artifact content types for the Java version.

Allowed values are: 'JDK', 'JRE', 'SERVER_JRE'

`mos_patches`

(optional) List of My Oracle Support(MoS) patches available for this release. This information is only available for `BPR` release type.

`days_under_security_baseline`

(optional) The number of days since this release has been under the security baseline.

### DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_java_release_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_COLLECTION_T Type

Collection of Java releases information.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of the Java release information.

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_T Type

Java Server instance usage during a specified time period.

Syntax
```

```

Fields

Field Description

`server_instance_key`

(required) The internal identifier of the Java Server instance.

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related Fleet.

`server_instance_name`

(required) The name of the Java Server instance.

`server_key`

(required) The internal identifier of the related Java Server.

`server_name`

(optional) The name of the Java Server.

`server_version`

(optional) The version of the Java Server.

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`host_name`

(optional) The host name of the related managed instance.

`jvm_key`

(optional) The internal identifier of the related Java Runtime.

`jvm_vendor`

(optional) The vendor of the Java Runtime.

`jvm_distribution`

(optional) The distribution of the Java Runtime.

`jvm_version`

(optional) The version of the Java Runtime.

`jvm_security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`approximate_deployed_application_count`

(optional) The approximate count of deployed applications in the Java Server instance.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_java_server_instance_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_COLLECTION_T Type

Results of a Java Server instance usage search. Contains Java Server usage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java Server instance usages.

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_T Type

Java Server usage during a specified time period.

Syntax
```

```

Fields

Field Description

`server_key`

(required) The internal identifier of the Java Server.

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related fleet.

`server_name`

(required) The name of the Java Server.

`server_version`

(optional) The version of the Java Server.

`server_instance_count`

(optional) The count of server instances of the Java Server.

`approximate_deployed_application_count`

(optional) The approximate count of deployed applications in the Java Server.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_java_server_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_COLLECTION_T Type

Results of a Java Server usage search. Contains Java Server usage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java Server usages.

### DBMS_CLOUD_OCI_JMS_JFR_ATTACHMENT_TARGET_T Type

The target to collect JFR data. A target is a managed instance, with options to further limit to specific application and/or Java Runtime. When the applicationKey isn't specified, then all applications are selected. When the jreKey isn't specified, then all supported Java Runtime versions are selected. When the applicationInstallationKey isn't specified, then all application installations are selected. Keys applicationKey and applicationInstallationKey are mutually exclusive.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) OCID of the Managed Instance to collect JFR data.

`application_key`

(optional) Unique key that identifies the application for JFR data collection.

`application_installation_key`

(optional) Unique key that identifies the application installation for JFR data collection.

`jre_key`

(optional) Unique key that identify the JVM for JFR data collection.

### DBMS_CLOUD_OCI_JMS_JRE_USAGE_T Type

Java Runtime usage during a specified time period. A Java Runtime is identified by its vendor and version.

Syntax
```

```

Fields

Field Description

`id`

(optional) The internal identifier of the Java Runtime.

`fleet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related fleet.

`managed_instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance. This property value is present only for /listJreUsage.

`security_status`

(optional) The security status of the Java Runtime.

Allowed values are: 'EARLY_ACCESS', 'UNKNOWN', 'UP_TO_DATE', 'UPDATE_REQUIRED', 'UPGRADE_REQUIRED'

`release_date`

(optional) The release date of the Java Runtime (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`end_of_support_life_date`

(optional) The End of Support Life (EOSL) date of the Java Runtime (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`vendor`

(required) The vendor of the Java Runtime.

`distribution`

(required) The distribution of a Java Runtime is the name of the lineage of product to which it belongs, for example _Java(TM) SE Runtime Environment_.

`version`

(required) The version of the Java Runtime.

`days_under_security_baseline`

(optional) The number of days since this release has been under the security baseline.

`operating_systems`

(optional) The operating systems that have this Java Runtime installed.

`approximate_installation_count`

(optional) The approximate count of installations that are installations of this Java Runtime.

`approximate_application_count`

(optional) The approximate count of the applications running on this Java Runtime.

`approximate_managed_instance_count`

(optional) The approximate count of the managed instances that report this Java Runtime.

`approximate_pending_work_request_count`

(optional) The approximate count of work requests working on this Java Runtime.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_JRE_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_jre_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_JRE_USAGE_COLLECTION_T Type

Results of a Java Runtime search. Contains JreUsage items

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Java Runtimes.

### DBMS_CLOUD_OCI_JMS_LCM_WORK_ITEM_DETAILS_T Type

The work item details with LCM related information.

Syntax
```

```

`dbms_cloud_oci_jms_lcm_work_item_details_t`is a subtype of the`dbms_cloud_oci_jms_work_item_details_t`type.

Fields

Field Description

`post_installation_actions`

(optional)

### DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_T Type

Library usage during a specified time period.

Syntax
```

```

Fields

Field Description

`library_key`

(required) The internal identifier of the library.

`fleet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related fleet.

`library_name`

(required) The name of the library.

`library_version`

(optional) The version of the library.

`cvss_score`

(optional) The Common Vulnerability Scoring System (CVSS) score.

`approximate_application_count`

(optional) The approximate count of applications using the library.

`approximate_java_server_instance_count`

(optional) The approximate count of Java Server instances using the library.

`approximate_deployed_application_count`

(optional) The approximate count of deployed applications using the library.

`approximate_managed_instance_count`

(optional) The approximate count of managed instances using the library.

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_library_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_COLLECTION_T Type

Results of a library usage search. Contains library usage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of library usages.

### DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_T Type

Managed instance usage during a specified time period. An entity that emits usage events to Java Management Service (JMS) is represented as a managed instance. A managed instance has a unique identity which is used by JMS to distinguish it from other managed instances. Currently, JMS supports only one kind of managed instance, a Management Agent.

Syntax
```

```

Fields

Field Description

`managed_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`managed_instance_type`

(required) The type of the source of events.

Allowed values are: 'ORACLE_MANAGEMENT_AGENT'

`hostname`

(optional) The hostname of the managed instance (if applicable).

`host_id`

(optional) The host[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related managed instance.

`operating_system`

(optional)

`agent`

(optional)

`approximate_application_count`

(optional) The approximate count of applications reported by this managed instance.

`approximate_installation_count`

(optional) The approximate count of installations reported by this managed instance.

`approximate_jre_count`

(optional) The approximate count of Java Runtimes reported by this managed instance.

`drs_file_status`

(optional) DRS file status

Allowed values are: 'PRESENT', 'ABSENT', 'MISMATCH', 'NOT_CONFIGURED'

`time_start`

(optional) Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_end`

(optional) Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.

`time_first_seen`

(optional) The date and time the resource was _first_ reported to JMS. This is potentially _before_ the specified time period provided by the filters. For example, a resource can be first reported to JMS before the start of a specified time period, if it is also reported during the time period.

`time_last_seen`

(optional) The date and time the resource was _last_ reported to JMS. This is potentially _after_ the specified time period provided by the filters. For example, a resource can be last reported to JMS before the start of a specified time period, if it is also reported during the time period.

### DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_TBL Type

Nested table type of dbms_cloud_oci_jms_managed_instance_usage_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_COLLECTION_T Type

Results of a managed instance search. Contains ManagedInstanceUsage items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of managed instances.

### DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_T Type

Metadata of a Performance Tuning Analysis result. The analysis result is stored as the Object Storage object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID to identify this analysis results.

`work_request_id`

(optional) The OCID of the work request to start the analysis.

`fleet_id`

(required) The fleet OCID.

`application_id`

(required) The OCID of the application for which the report has been generated.

`application_installation_id`

(required) The internal identifier of the application installation for which the report has been generated.

`application_installation_path`

(required) The installation path of the application for which the report has been generated.

`warning_count`

(required) Total number of warnings reported by the analysis.

`result`

(required) Result of the analysis based on whether warnings have been found or not.

Allowed values are: 'ACTION_RECOMMENDED', 'NO_WARNINGS'

`managed_instance_id`

(required) The managed instance OCID.

`host_name`

(required) The hostname of the managed instance.

`application_name`

(required) The name of the application for which the report has been generated.

`namespace`

(required) The Object Storage namespace of this analysis result.

`bucket_name`

(required) The Object Storage bucket name of this analysis result.

`object_name`

(required) The Object Storage object name of this analysis result.

`time_created`

(required) The time the result is compiled.

`time_started`

(required) The time the JFR capture started.

`time_finished`

(required) The time the JFR capture finished.

### DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_SUMMARY_T Type

Summary of a performance tuning analysis result. The actual output of the analysis is stored in the Object Storage object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID to identify this analysis results.

`work_request_id`

(optional) The OCID of the work request to start the analysis.

`fleet_id`

(required) The fleet OCID.

`application_id`

(required) The OCID of the application for which the report has been generated.

`application_installation_id`

(required) The internal identifier of the application installation for which the report has been generated.

`application_installation_path`

(required) The installation path of the application for which the report has been generated.

`warning_count`

(required) Total number of warnings reported by the analysis.

`result`

(required) Result of the analysis based on whether warnings have been found or not.

Allowed values are: 'ACTION_RECOMMENDED', 'NO_WARNINGS'

`managed_instance_id`

(required) The managed instance OCID.

`host_name`

(required) The hostname of the managed instance.

`application_name`

(required) The name of the application for which the report has been generated.

`namespace`

(required) The Object Storage namespace of this analysis result.

`bucket_name`

(required) The Object Storage bucket name of this analysis result.

`object_name`

(required) The Object Storage object name of this analysis result.

`time_created`

(required) The time the result is compiled.

`time_started`

(required) The time the JFR capture started.

`time_finished`

(required) The time the JFR capture finished.

### DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_performance_tuning_analysis_result_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_COLLECTION_T Type

List of Performance Tuning Analysis results.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of Performance Tuning Analysis results.

### DBMS_CLOUD_OCI_JMS_PRINCIPAL_T Type

An authorized principal.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the principal.

`display_name`

(required) The name of the principal.

### DBMS_CLOUD_OCI_JMS_EXISTING_INSTALLATION_SITE_ID_TBL Type

Nested table type of dbms_cloud_oci_jms_existing_installation_site_id_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_REMOVE_FLEET_INSTALLATION_SITES_DETAILS_T Type

The list of Java installation sites to remove.

Syntax
```

```

Fields

Field Description

`installation_sites`

(required) The list of installation sites to remove.

### DBMS_CLOUD_OCI_JMS_JFR_ATTACHMENT_TARGET_TBL Type

Nested table type of dbms_cloud_oci_jms_jfr_attachment_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_REQUEST_CRYPTO_ANALYSES_DETAILS_T Type

Details of the request to start a JFR crypto event analysis. When the targets aren't specified, then all managed instances currently in the fleet are selected.

Syntax
```

```

Fields

Field Description

`targets`

(optional) The attachment targets to start JFR.

`recording_duration_in_minutes`

(optional) Duration of the JFR recording in minutes.

`waiting_period_in_minutes`

(optional) Period to looking for JVMs. In addition to attach to running JVMs when given the command, JVM started within the waiting period will also be attached for JFR. The value should be larger than the agent polling interval setting for the fleet to ensure agent can get the instructions. If not specified, the agent polling interval for the fleet is used.

### DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_TARGET_TBL Type

Nested table type of dbms_cloud_oci_jms_java_migration_analysis_target_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_REQUEST_JAVA_MIGRATION_ANALYSES_DETAILS_T Type

Details of the request to start a Java migration analysis. The analysis requires the managed instance OCID, application installation key, source JDK version, and target JDK version of each selected application.

Syntax
```

```

Fields

Field Description

`targets`

(required) An array of migration analysis requests.

### DBMS_CLOUD_OCI_JMS_REQUEST_JFR_RECORDINGS_DETAILS_T Type

Details of the request to start JFR recordings. When the targets aren't specified, then all managed instances currently in the Fleet are selected.

Syntax
```

```

Fields

Field Description

`targets`

(optional) The attachment targets to start JFR.

`jfc_profile_name`

(required) The profile used for JFR events selection. If the name isn't recognized, the settings from jfcV1 or jfcV2 will be used depending on the JVM version. Both jfcV2 and jfcV1 should be provided to ensure JFR collection on different JVM versions.

`jfc_v1`

(optional) The BASE64 encoded string of JFR settings XML with schema used by JDK 8.

`jfc_v2`

(optional) The BASE64 encoded string of JFR settings XML with[schema used by JDK 9 and after](https://raw.githubusercontent.com/openjdk/jdk/master/src/jdk.jfr/share/classes/jdk/jfr/internal/jfc/jfc.xsd).

`recording_duration_in_minutes`

(optional) Duration of the JFR recording in minutes.

`recording_size_in_mb`

(optional) The maximum size limit for the JFR file collected.

`waiting_period_in_minutes`

(optional) Period to looking for JVMs. In addition to attach to running JVMs when given the command, JVM started within the waiting period will also be attached for JFR. The value should be larger than the agent polling interval setting for the fleet to ensure agent can get the instructions. If not specified, the agent polling interval for the fleet is used.

### DBMS_CLOUD_OCI_JMS_REQUEST_PERFORMANCE_TUNING_ANALYSES_DETAILS_T Type

Details of the request to start a JFR performance tuning analysis.

Syntax
```

```

Fields

Field Description

`targets`

(optional) The attachment targets to start JFR.

`recording_duration_in_minutes`

(required) Duration of the JFR recording in minutes.

`waiting_period_in_minutes`

(optional) Period to looking for JVMs. In addition to attach to running JVMs when given the command, JVM started within the waiting period will also be attached for JFR. The value should be larger than the agent polling interval setting for the fleet to ensure agent can get the instructions. If not specified, the agent polling interval for the fleet is used.

### DBMS_CLOUD_OCI_JMS_RESOURCE_INVENTORY_T Type

Inventory of JMS resources in a compartment during a specified time period.

Syntax
```

```

Fields

Field Description

`active_fleet_count`

(required) The number of _active_ fleets.

`managed_instance_count`

(required) The number of managed instances.

`jre_count`

(required) The number of Java Runtimes.

`installation_count`

(required) The number of Java installations.

`application_count`

(required) The number of applications.

### DBMS_CLOUD_OCI_JMS_SCAN_JAVA_SERVER_USAGE_DETAILS_T Type

The list of managed instances to scan.

Syntax
```

```

Fields

Field Description

`managed_instance_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of managed instances to scan.

### DBMS_CLOUD_OCI_JMS_SCAN_LIBRARY_USAGE_DETAILS_T Type

The list of managed instances to scan.

Syntax
```

```

Fields

Field Description

`managed_instance_ids`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of managed instances to scan.

### DBMS_CLOUD_OCI_JMS_UPDATE_DRS_FILE_DETAILS_T Type

Details of the request to update DRS file in a Fleet.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket name where the DRS file is located.

`namespace`

(required) The namespace for Object Storage.

`drs_file_name`

(required) The name of the DRS file in Object Store.

### DBMS_CLOUD_OCI_JMS_UPDATE_EXPORT_SETTING_DETAILS_T Type

Attributes to update a Export setting.

Syntax
```

```

Fields

Field Description

`export_duration`

(optional) The duration of data to be exported for fleets.

Allowed values are: 'LAST_30_DAYS', 'LAST_60_DAYS', 'LAST_90_DAYS'

`export_resources`

(optional) Resource to export data associated from the fleets.

Allowed values are: 'MANAGED_INSTANCE', 'MANAGED_INSTANCE_PLUS_JAVA_RUNTIME', 'MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION'

`is_cross_region_acknowledged`

(optional) Acknowledgement for cross region target bucket configuration.

`target_bucket_name`

(optional) The name of the bucket where data will be exported.

`target_bucket_namespace`

(optional) The namespace of the bucket where data will be exported.

`target_bucket_region`

(optional) The namespace of the bucket where data will be exported.

`export_frequency`

(optional) Schedule at which data will be exported.

Allowed values are: 'DAILY', 'WEEKLY', 'MONTHLY'

`is_enabled`

(required) ExportSetting flag to store enabled or disabled status.

### DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_ADVANCED_FEATURE_CONFIGURATION_DETAILS_T Type

Details object containing advanced feature configurations to be updated. Ensure that the namespace and bucket storage are created prior to turning on the JfrRecording or CryptoEventAnalysis feature.

Syntax
```

```

Fields

Field Description

`analytic_namespace`

(optional) Namespace for the Fleet advanced feature.

`analytic_bucket_name`

(optional) Bucket name required to store JFR and related data.

`lcm`

(optional)

`crypto_event_analysis`

(optional)

`advanced_usage_tracking`

(optional)

`jfr_recording`

(optional)

`performance_tuning_analysis`

(optional)

`java_migration_analysis`

(optional)

### DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_AGENT_CONFIGURATION_DETAILS_T Type

Attributes to update a Fleet Agent Configuration.

Syntax
```

```

Fields

Field Description

`jre_scan_frequency_in_minutes`

(optional) The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)

`java_usage_tracker_processing_frequency_in_minutes`

(optional) The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)

`work_request_validity_period_in_days`

(optional) The validity period in days for work requests.

`agent_polling_interval_in_minutes`

(optional) Agent polling interval in minutes

`linux_configuration`

(optional)

`windows_configuration`

(optional)

`mac_os_configuration`

(optional)

### DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_DETAILS_T Type

Attributes to update a Fleet.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name of the Fleet. The displayName must be unique for Fleets in the same compartment.

`description`

(optional) The Fleet's description.

`inventory_log`

(optional)

`operation_log`

(optional)

`is_advanced_features_enabled`

(optional) Whether or not advanced features are enabled in this Fleet. Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See[Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)).

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).)

### DBMS_CLOUD_OCI_JMS_WORK_ITEM_SUMMARY_T Type

Work item to complete a work request.

Syntax
```

```

Fields

Field Description

`id`

(required) The unique ID of ths work item.

`work_request_id`

(required) The OCID of the work request created this work item.

`installation_site`

(required)

`details`

(required)

`status`

(required) The status of the work item.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'NEEDS_ATTENTION', 'RETRYING'

`retry_count`

(required) Number of times this work item is retried.

`time_last_updated`

(optional) The date and time the work item was last updated. (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_WORK_ITEM_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_jms_work_item_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_WORK_ITEM_COLLECTION_T Type

A list of WorkItem.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request items.

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_RESOURCE_T Type

A resource that is created or operated on by an asynchronous operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type affected by the work request.

`action_type`

(required) The way in which this resource was affected by the operation that spawned the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'DELETED', 'IN_PROGRESS', 'RELATED', 'UPDATED', 'FAILED'

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier of the resource affected by the work request.

`entity_uri`

(optional) The URI path that the user can perform a GET operation to access the resource metadata.

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_jms_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_T Type

An asynchronous work request. See[Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm).

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_FLEET', 'DELETE_FLEET', 'MOVE_FLEET', 'UPDATE_FLEET', 'UPDATE_FLEET_AGENT_CONFIGURATION', 'DELETE_JAVA_INSTALLATION', 'CREATE_JAVA_INSTALLATION', 'COLLECT_JFR', 'REQUEST_CRYPTO_EVENT_ANALYSIS', 'REQUEST_PERFORMANCE_TUNING_ANALYSIS', 'REQUEST_JAVA_MIGRATION_ANALYSIS', 'DELETE_JMS_REPORT', 'SCAN_JAVA_SERVER_USAGE', 'SCAN_LIBRARY_USAGE', 'EXPORT_DATA_CSV', 'CREATE_DRS_FILE', 'UPDATE_DRS_FILE', 'DELETE_DRS_FILE', 'ENABLE_DRS', 'DISABLE_DRS'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'CANCELED', 'CANCELING', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources aren't in the same compartment, it's up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources that are affected by this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the request was created (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_started`

(optional) The date and time the work request transitioned from _ACCEPTED_ to _IN_PROGRESS_ (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`time_finished`

(optional) The date and time the work request reached a terminal state, either _FAILED_ or _SUCCEEDED_ (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`created_by`

(optional)

`time_last_updated`

(optional) The date and time the work request percentage was last updated. (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

`total_task_count`

(optional) The total number of tasks to be executed for this work request.

`completed_task_count`

(optional) The number of tasks had been executed to a terminal state.

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_jms_work_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_COLLECTION_T Type

Results of a work request search. Contains WorkRequest items

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work requests.

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed at[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The date and time the error occured (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_jms_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a work request error search. Contains WorkRequestError items

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written (formatted according to[RFC3339](https://datatracker.ietf.org/doc/html/rfc3339)).

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_jms_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

Results of a work request log entry search. Contains WorkRequestLogEntry items

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request log entries.

- [JMS Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-40DE7663-17DC-4472-BA94-3C2EDA22E481)
- [DBMS_CLOUD_OCI_JMS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-33EEEC76-798A-47C6-88F9-736F88704DCB)
- [DBMS_CLOUD_OCI_JMS_NEW_INSTALLATION_SITE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-576856D6-CE21-4AA6-831B-06CBD8BA1BDE)
- [DBMS_CLOUD_OCI_JMS_NEW_INSTALLATION_SITE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-6D536C0B-53AE-47D0-8A81-512DF7E2AE15)
- [DBMS_CLOUD_OCI_JMS_ADD_FLEET_INSTALLATION_SITES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7CAE79EB-E87C-4F07-B345-BA98FC791B4E)
- [DBMS_CLOUD_OCI_JMS_ADVANCED_USAGE_TRACKING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B95CBE70-2B25-47B6-AD2C-ED3662FD947B)
- [DBMS_CLOUD_OCI_JMS_PLUGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1F754498-02BC-4F42-A6CF-999FB97823E1)
- [DBMS_CLOUD_OCI_JMS_PLUGIN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D07B19C0-84C4-460A-AC07-E9E0ED4B4E9C)
- [DBMS_CLOUD_OCI_JMS_AGENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-15A11E10-284B-459D-9D20-E6BAF425F2D3)
- [DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0A8D7452-C21B-4407-BD39-5F3BA5E221BE)
- [DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1861AF19-04B1-42E0-8040-D3BE0D846861)
- [DBMS_CLOUD_OCI_JMS_ANNOUNCEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-32CBEB5E-79B8-4EBC-9D36-79C3D9758654)
- [DBMS_CLOUD_OCI_JMS_OPERATING_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A75FBF66-4BF4-4EBE-8FF3-D68C8F093DBC)
- [DBMS_CLOUD_OCI_JMS_OPERATING_SYSTEM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0E8F4DDC-A11C-42F6-A5B4-AB958368ED9D)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-95FB8F66-E81D-4D24-BB2A-E7820F3A0A68)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-E570FE04-61FE-4074-A72C-962AFE2C6F5B)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_INSTALLATION_USAGE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A1AC38B5-24C2-441A-BF16-11576ED606CB)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-70971632-26F7-42A2-A9EC-35D2D31A0365)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-722F2A02-D48C-4BD7-A5AD-19E6177466C8)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-79C72404-EC31-4E0C-89CC-549B39A7CEC5)
- [DBMS_CLOUD_OCI_JMS_WORK_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-ED5D9F91-6BAF-4700-8F89-B4DCCE9CF15B)
- [DBMS_CLOUD_OCI_JMS_APPLICATION_WORK_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C527C2CC-9D72-406F-9E0B-FB71B9E3512F)
- [DBMS_CLOUD_OCI_JMS_BASIC_WORK_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-AF8A0F8C-10D6-4BC0-814A-8FC094028EC2)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-937304E5-A526-4357-8B98-B1FF58F5DD3E)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-40C0A4C0-43C2-4DB9-9FFD-970032F7137F)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1E605B8D-FEE9-4707-9597-D886C7C81147)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-59CDA64B-E29B-4C6D-ABB1-D9BCBCF5BEC8)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B07D446E-F492-429B-A866-F3A405E1765D)
- [DBMS_CLOUD_OCI_JMS_CHANGE_FLEET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-40FAA801-FF59-4D86-B3EF-068978C8C16A)
- [DBMS_CLOUD_OCI_JMS_CREATE_BLOCKLIST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D9AA8898-7A36-42A8-BF2B-98468D20BDD3)
- [DBMS_CLOUD_OCI_JMS_CREATE_DRS_FILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-31277426-F7C9-438F-8C06-B2581817A1CF)
- [DBMS_CLOUD_OCI_JMS_CUSTOM_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C3D5C87A-3296-4731-B10B-2FF7B483BEF9)
- [DBMS_CLOUD_OCI_JMS_CREATE_FLEET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-DF925427-F4D9-409E-AF2E-D6F2D80DC613)
- [DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-410BDE72-07EA-47D5-9B3B-9445F5477339)
- [DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D20DD834-F84C-48FF-8792-BCF21AD21F91)
- [DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-71ACDA17-1CFA-498D-BB3D-7B5FB2852AFF)
- [DBMS_CLOUD_OCI_JMS_CRYPTO_ANALYSIS_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-3A642F98-0168-4753-90DD-79A9EA5CCB55)
- [DBMS_CLOUD_OCI_JMS_SUMMARIZED_EVENTS_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-337F3DD7-5867-4107-90B3-7068B51E29C6)
- [DBMS_CLOUD_OCI_JMS_CRYPTO_EVENT_ANALYSIS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-EF2FA20B-34B6-4544-9EE0-78C66E5DEA0E)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7271AC94-6640-4189-81EB-83DB8E332C1C)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-061EFABA-53B5-491E-B636-7C93D7E85719)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_INSTALLATION_USAGE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-2D7E6D74-8459-4D85-967E-A6EF8663898D)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7A6416D5-18F3-48AE-89ED-7DEE19E520E7)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-50660939-0ED3-4434-BAF4-E082CED3C24D)
- [DBMS_CLOUD_OCI_JMS_DEPLOYED_APPLICATION_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7E3F8D61-B8B2-452A-886D-0CECCFCEAE6B)
- [DBMS_CLOUD_OCI_JMS_DRS_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C9FE0140-36FD-487A-95D9-0E50C7E82229)
- [DBMS_CLOUD_OCI_JMS_DRS_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-3DCFB071-64D7-46A4-8F6A-D1C2D5DEE054)
- [DBMS_CLOUD_OCI_JMS_MANAGE_DRS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B4ED56BB-4E51-45A3-8812-EF994ED9A676)
- [DBMS_CLOUD_OCI_JMS_DISABLE_DRS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-AA77EAF3-518D-43D9-A152-FC051C9443CD)
- [DBMS_CLOUD_OCI_JMS_DRS_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A4DAB967-990B-44BF-A0AC-63308DE158D1)
- [DBMS_CLOUD_OCI_JMS_DRS_FILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1B0B3856-51C7-4E19-A9D1-3612C95D2066)
- [DBMS_CLOUD_OCI_JMS_DRS_FILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-EA60FC39-9A3B-4258-8176-858585E501A8)
- [DBMS_CLOUD_OCI_JMS_DRS_FILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-2555F06B-A793-4CD3-A520-5E9661FA88D7)
- [DBMS_CLOUD_OCI_JMS_ENABLE_DRS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-CCF73FFE-7C1B-41F5-A6C9-37F977533C6E)
- [DBMS_CLOUD_OCI_JMS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4D1D34E3-D01E-4638-8795-436745321C3C)
- [DBMS_CLOUD_OCI_JMS_EXISTING_INSTALLATION_SITE_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-553050D8-C3F9-4537-BF95-CF6878223914)
- [DBMS_CLOUD_OCI_JMS_EXPORT_SETTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7BB39B05-DB6F-486C-B678-D0F584996BA6)
- [DBMS_CLOUD_OCI_JMS_EXPORT_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C31E8BE3-48D8-4535-A052-22337554C922)
- [DBMS_CLOUD_OCI_JMS_FLEET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-34DF6DF6-1882-4696-8992-BD1B48F9834D)
- [DBMS_CLOUD_OCI_JMS_KEY_SIZE_ALGORITHM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-6F5F5B45-38D5-4738-8A0E-2A89C20EA4F0)
- [DBMS_CLOUD_OCI_JMS_KEY_SIZE_ALGORITHM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-CAAF7DB5-D98C-4C48-BE6F-33E3E1C2D158)
- [DBMS_CLOUD_OCI_JMS_MINIMUM_KEY_SIZE_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C15C2E19-CE54-49AC-AAB3-E034137CE7B9)
- [DBMS_CLOUD_OCI_JMS_PROXIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-29991F9F-D4FE-4689-B389-BE5DCB3C1B92)
- [DBMS_CLOUD_OCI_JMS_POST_INSTALLATION_ACTION_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-E89C69F1-E487-4FF6-BF07-996669CE42B5)
- [DBMS_CLOUD_OCI_JMS_LCM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4D6090DC-C10A-4EB4-8C1F-77EB2D9EB4C1)
- [DBMS_CLOUD_OCI_JMS_JFR_RECORDING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A43D2CC1-CCBD-44F8-B319-1FDF1A547C91)
- [DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-CC9AB1B7-F042-4BA6-A6F3-9DB16ACA7D23)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B9C16F49-2970-4573-A236-5D7BF314D244)
- [DBMS_CLOUD_OCI_JMS_FLEET_ADVANCED_FEATURE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-EE747680-5B33-498E-8646-10932BA83D35)
- [DBMS_CLOUD_OCI_JMS_FLEET_AGENT_OS_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0506250A-4A34-4BC7-86FC-EB7BC09F8A02)
- [DBMS_CLOUD_OCI_JMS_FLEET_AGENT_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-696723AB-2D26-4289-9467-8186A24DAC13)
- [DBMS_CLOUD_OCI_JMS_FLEET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1F6577A9-CA2B-4A4C-8FE9-C997EBED3F12)
- [DBMS_CLOUD_OCI_JMS_FLEET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-6CF80BE0-75B6-4BA3-AE21-780FEBA3BFBF)
- [DBMS_CLOUD_OCI_JMS_FLEET_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B5E728DD-475D-4035-BD07-85AA99B3ED27)
- [DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-402DD539-6252-485E-944D-3DA30E41DB2D)
- [DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-73351A55-9C3B-4A6E-9627-EAF28711F953)
- [DBMS_CLOUD_OCI_JMS_FLEET_DIAGNOSIS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-8E930AD6-D8A3-47D4-8936-D054C7A1CB7A)
- [DBMS_CLOUD_OCI_JMS_GENERATE_AGENT_DEPLOY_SCRIPT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-193FE213-58F3-4047-88B1-E501F5107C2A)
- [DBMS_CLOUD_OCI_JMS_JAVA_RUNTIME_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4BF678D2-3D6C-40A3-B05D-267DF85BF0B2)
- [DBMS_CLOUD_OCI_JMS_BLOCKLIST_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-55035F0C-0375-4256-89EE-1F062F4E07D4)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4DFBE7BD-A345-4DD3-B90C-8BD95C7B8A33)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0987CE0F-8A63-4F1C-B1D4-00F4A5274CA3)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4030709D-4FDE-4F92-ABC5-91E7C1B2E698)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_SITE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-666C1BD5-03BE-439A-8A29-36DFB3E23285)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-533F8086-18B8-4EF9-8863-14C5912A23B6)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-66E796AD-49A5-479F-A487-C85393F67D4F)
- [DBMS_CLOUD_OCI_JMS_INSTALLATION_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B78D66EF-B1B2-4145-B942-E6998D5E5789)
- [DBMS_CLOUD_OCI_JMS_JAVA_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-90D7F127-F8AE-4E26-8E1D-89E693CE211C)
- [DBMS_CLOUD_OCI_JMS_JAVA_ARTIFACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-670E3866-E7F3-4B0B-97E5-2C46C8968B76)
- [DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-72A4F1CD-033E-4EF8-8F1D-5A1A3AC45612)
- [DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-87C0A1D3-6C1F-4D45-B6B8-0EA46F44A4A4)
- [DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7E80F015-66E5-42EE-808E-335BEADD7EB2)
- [DBMS_CLOUD_OCI_JMS_JAVA_FAMILY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-43000B8A-BEF7-403F-B0AB-937878DB0D0D)
- [DBMS_CLOUD_OCI_JMS_JAVA_LICENSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-F7146EDD-F62E-4462-975F-DDCEBBE13506)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-645B35D8-B423-4498-A459-58DE2DD831C0)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-9E2A12AA-1F6A-4421-8F02-71784E3834A0)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-E10945BE-AD0A-4A23-A951-F2F4AE0AE612)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0744E17D-CE36-4EAF-B401-8BA60FC44510)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-95CEB66D-24F8-4B8B-9C73-08EE480DD397)
- [DBMS_CLOUD_OCI_JMS_PATCH_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-2CDD8131-9B07-4BD4-AA65-D86FFF95E38E)
- [DBMS_CLOUD_OCI_JMS_PATCH_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D897AD83-DD3B-4CD3-99E2-9024FC2C4F25)
- [DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-156D3C6D-A86A-4A4A-9FA3-D55B3E0B3411)
- [DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-2C5AC576-958B-4BA9-ADA7-B7E865C2BD35)
- [DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-87246CE4-035C-438F-9DA6-BB0AF7C7B2B9)
- [DBMS_CLOUD_OCI_JMS_JAVA_RELEASE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-9A666A1E-9416-495B-B4AA-1A9B6C94DAC9)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-F0EDE765-6B43-4ABC-B88D-D20C8C4FE0FD)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-F008947D-83E9-4174-8B47-D7F60FA7A913)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_INSTANCE_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D641A4C7-CEF1-4B79-A827-FB6B06E25D00)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-5B4709B8-67E4-441C-98DC-84060306028F)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-9511A4ED-6F99-46B1-A6E5-12493B8FBF58)
- [DBMS_CLOUD_OCI_JMS_JAVA_SERVER_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4B2A67B4-ECE8-4C08-BEBE-44555826CD62)
- [DBMS_CLOUD_OCI_JMS_JFR_ATTACHMENT_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-2C42911F-CD85-4E0F-BDD7-CA7DED04763B)
- [DBMS_CLOUD_OCI_JMS_JRE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-07E42652-C84A-46D6-BAA7-1441FA27C317)
- [DBMS_CLOUD_OCI_JMS_JRE_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-3AA31B1D-9942-4EC0-9B88-B73DFDDF3CBD)
- [DBMS_CLOUD_OCI_JMS_JRE_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A3E24030-E1D0-4661-957F-1E76474B6D7C)
- [DBMS_CLOUD_OCI_JMS_LCM_WORK_ITEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-3030A1BF-F7B6-45E5-98A7-C07EB5E926FC)
- [DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-05B5C445-8168-4801-A9EB-E6C0708A6282)
- [DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-7C88DF8D-4E96-4C59-8669-8112738CC09E)
- [DBMS_CLOUD_OCI_JMS_LIBRARY_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-10946971-15C7-41D8-AB78-50CF47EA3FFF)
- [DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-0B646C6C-001A-44FB-BB8A-D3F22E3D2277)
- [DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-859EC47E-024E-4717-9749-A51D0214C2C1)
- [DBMS_CLOUD_OCI_JMS_MANAGED_INSTANCE_USAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-165F885C-3F64-402F-93B2-30FEBA2110F1)
- [DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-49FC9CA3-DD90-466B-9A98-D12CB9F52DDC)
- [DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C2CE2509-5ED4-4948-9F55-64A3ACB2504B)
- [DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1C37E450-DBFF-493E-AB19-5212810365A3)
- [DBMS_CLOUD_OCI_JMS_PERFORMANCE_TUNING_ANALYSIS_RESULT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-86462620-7337-4059-93A5-2A094120356E)
- [DBMS_CLOUD_OCI_JMS_PRINCIPAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-F2F3CAC0-F67C-4BB6-A7AE-FB8BC21FB935)
- [DBMS_CLOUD_OCI_JMS_EXISTING_INSTALLATION_SITE_ID_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-33E6348E-589C-4630-AB55-AA57650F7EF6)
- [DBMS_CLOUD_OCI_JMS_REMOVE_FLEET_INSTALLATION_SITES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-F182AD87-742F-492E-BCC0-6BCBF1F3FF09)
- [DBMS_CLOUD_OCI_JMS_JFR_ATTACHMENT_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-BCB7C2CB-410C-4B35-979F-FD99ACB10604)
- [DBMS_CLOUD_OCI_JMS_REQUEST_CRYPTO_ANALYSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-38B50D94-CCA8-4589-B77A-476D90A3AF9B)
- [DBMS_CLOUD_OCI_JMS_JAVA_MIGRATION_ANALYSIS_TARGET_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-73F5686F-6C7A-46E9-8E70-88D071C2157E)
- [DBMS_CLOUD_OCI_JMS_REQUEST_JAVA_MIGRATION_ANALYSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-3A8EBE31-43C8-45A5-8428-D287FB4C9422)
- [DBMS_CLOUD_OCI_JMS_REQUEST_JFR_RECORDINGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-64534D8F-0631-432C-9A84-171B81E42D00)
- [DBMS_CLOUD_OCI_JMS_REQUEST_PERFORMANCE_TUNING_ANALYSES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C93FE8A1-8CEA-469D-B4C0-691C2033B246)
- [DBMS_CLOUD_OCI_JMS_RESOURCE_INVENTORY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-926083C9-14E4-49A6-8F78-43694EB6F56F)
- [DBMS_CLOUD_OCI_JMS_SCAN_JAVA_SERVER_USAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A575509C-59C9-4569-8189-3300476DF7F5)
- [DBMS_CLOUD_OCI_JMS_SCAN_LIBRARY_USAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-24995588-EB3A-4946-8A95-233B54B25B94)
- [DBMS_CLOUD_OCI_JMS_UPDATE_DRS_FILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-A15CB68A-2928-43C4-BEAA-1C242D8C9276)
- [DBMS_CLOUD_OCI_JMS_UPDATE_EXPORT_SETTING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-D00D338C-3C44-4BF4-9EFF-2B019B13B9A2)
- [DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_ADVANCED_FEATURE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-C83C6975-6476-4954-9F93-6BF9281A3516)
- [DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_AGENT_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-54F4D388-7BDF-47B6-BCA5-2AB10611B61C)
- [DBMS_CLOUD_OCI_JMS_UPDATE_FLEET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-812855AA-D135-4D81-916A-03744C13B195)
- [DBMS_CLOUD_OCI_JMS_WORK_ITEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-BECAF66B-1566-4494-B5FB-CE424BDDE8A0)
- [DBMS_CLOUD_OCI_JMS_WORK_ITEM_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-6859969A-588D-40D6-B49C-E623CF6DDDC4)
- [DBMS_CLOUD_OCI_JMS_WORK_ITEM_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-AC3BAB80-2858-4EC9-8037-ABB7D811D96B)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-1FE2BF20-5DEC-43D5-9FF8-34BF972A5087)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-9263676E-7121-4F18-9BF7-824E1589FA49)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-92D2B54D-B506-4975-A92B-0DAD619C051E)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-50DE92BE-BDD4-4A23-8E30-2440887CDBF8)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-B72A38BB-54CC-4107-A1E0-EBFE3806F409)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-FDED34BF-B9B5-4E7F-9778-72A201B1E8EA)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-635394A0-EB8D-4325-A968-9B66D2ADC1D0)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-4242A746-685E-42F1-B86C-58CF14F3905E)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-FED784BA-BC53-4C1B-AA30-B5FC5AF30E5C)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-5348C905-1DC6-4D16-9EF5-DA203D84D554)
- [DBMS_CLOUD_OCI_JMS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/jms_t.html#ADSDK-GUID-157F3C32-7B52-4C76-A95D-E72BBF77328F)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
