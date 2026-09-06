# File Storage Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#dcoc-content-body)

## File Storage Common Types

### DBMS_CLOUD_OCI_FILE_STORAGE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_FILE_SYSTEM_COMPARTMENT_DETAILS_T Type

Details for changing the compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the file system to.

### DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_FILESYSTEM_SNAPSHOT_POLICY_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a file system snapshot policy.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the file system snapshot policy to.

### DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_MOUNT_TARGET_COMPARTMENT_DETAILS_T Type

Details for changing the compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the mount target to.

### DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_OUTBOUND_CONNECTOR_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of the outbound connector.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the outbound connector to.

### DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_REPLICATION_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of both replication and replication target.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the replication to. Also changes the replication target's compartment in the target region.

### DBMS_CLOUD_OCI_FILE_STORAGE_CLIENT_OPTIONS_T Type

NFS export options applied to a specified set of clients. Only governs access through the associated export. Access to the same file system through a different export (on the same or different mount target) will be governed by that export's export options.

Syntax
```

```

Fields

Field Description

`source`

(required) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block. **Note:** Access will also be limited by any applicable VCN security rules and the ability to route IP packets to the mount target. Mount targets do not have Internet-routable IP addresses.

`require_privileged_source_port`

(optional) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.

`l_access`

(optional) Type of access to grant clients using the file system through this export. If unspecified defaults to `READ_WRITE`.

Allowed values are: 'READ_WRITE', 'READ_ONLY'

`identity_squash`

(optional) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.

Allowed values are: 'NONE', 'ROOT', 'ALL'

`anonymous_uid`

(optional) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.

`anonymous_gid`

(optional) GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.

`is_anonymous_access_allowed`

(optional) Whether or not to enable anonymous access to the file system through this export in cases where a user isn't found in the LDAP server used for ID mapping. If true, and the user is not found in the LDAP directory, the operation uses the Squash UID and Squash GID.

`allowed_auth`

(optional) Array of allowed NFS authentication types.

Allowed values are: 'SYS', 'KRB5', 'KRB5I', 'KRB5P'

### DBMS_CLOUD_OCI_FILE_STORAGE_CLIENT_OPTIONS_TBL Type

Nested table type of dbms_cloud_oci_file_storage_client_options_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_EXPORT_DETAILS_T Type

Details for creating the export.

Syntax
```

```

Fields

Field Description

`export_options`

(optional) Export options for the new export. If left unspecified, defaults to: [ { \"source\" : \"0.0.0.0/0\", \"requirePrivilegedSourcePort\" : false, \"access\": \"READ_WRITE\", \"identitySquash\": \"NONE\", \"anonymousUid\": 65534, \"anonymousGid\": 65534, \"isAnonymousAccessAllowed\": false, \"allowedAuth\": [\"SYS\"] } ] **Note:** Mount targets do not have Internet-routable IP addresses. Therefore they will not be reachable from the Internet, even if an associated `ClientOptions` item has a source of `0.0.0.0/0`. **If set to the empty array then the export will not be visible to any clients.** The export's `exportOptions` can be changed after creation using the `UpdateExport` operation.

`export_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's export set.

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's file system.

`path`

(required) Path used to access the associated file system. Avoid entering confidential information. Example: `/mediafiles`

`is_idmap_groups_for_sys_auth`

(optional) Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_FILE_SYSTEM_DETAILS_T Type

Details for creating the file system.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain to create the file system in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the file system in.

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My file system`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the KMS key used to encrypt the encryption keys associated with this file system.

`source_snapshot_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot used to create a cloned file system. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated file system snapshot policy, which controls the frequency of snapshot creation and retention period of the taken snapshots. May be unset as a blank value.

### DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SCHEDULE_T Type

The snapshot schedule is a structure within a parent file system snapshot policy. It contains data about the frequency of snapshot creation and the retention time of the taken snapshots.

Syntax
```

```

Fields

Field Description

`schedule_prefix`

(optional) A name prefix to be applied to snapshots created by this schedule. Example: `compliance1`

`time_schedule_start`

(optional) The starting point used to begin the scheduling of the snapshots based upon recurrence string in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. If no `timeScheduleStart` is provided, the value will be set to the time when the schedule was created.

`period`

(required) The frequency of scheduled snapshots.

Allowed values are: 'HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'YEARLY'

`retention_duration_in_seconds`

(optional) The number of seconds to retain snapshots created with this schedule. Snapshot expiration time will not be set if this value is empty.

`time_zone`

(required) Time zone used for scheduling the snapshot.

Allowed values are: 'UTC', 'REGIONAL_DATA_CENTER_TIME'

`hour_of_day`

(optional) The hour of the day to create a DAILY, WEEKLY, MONTHLY, or YEARLY snapshot. If not set, a value will be chosen at creation time.

`day_of_week`

(optional) The day of the week to create a scheduled snapshot. Used for WEEKLY snapshot schedules.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

`day_of_month`

(optional) The day of the month to create a scheduled snapshot. If the day does not exist for the month, snapshot creation will be skipped. Used for MONTHLY and YEARLY snapshot schedules.

`month`

(optional) The month to create a scheduled snapshot. Used only for YEARLY snapshot schedules.

Allowed values are: 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'

### DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SCHEDULE_TBL Type

Nested table type of dbms_cloud_oci_file_storage_snapshot_schedule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_FILESYSTEM_SNAPSHOT_POLICY_DETAILS_T Type

Details for creating the file system snapshot policy.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain that the file system snapshot policy is in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the file system snapshot policy.

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `policy1`

`policy_prefix`

(optional) The prefix to apply to all snapshots created by this policy. Example: `acme`

`schedules`

(optional) The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy. If using the CLI, provide the schedule as a list of JSON strings, with the list wrapped in quotation marks, i.e. ``` --schedules '[{\"timeZone\":\"UTC\",\"period\":\"DAILY\",\"hourOfDay\":18},{\"timeZone\":\"UTC\",\"period\":\"HOURLY\"}]' ```

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_KERBEROS_DETAILS_T Type

Kerberos details needed to create configuration.

Syntax
```

```

Fields

Field Description

`kerberos_realm`

(required) The Kerberos realm that the mount target will join.

`key_tab_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the keytab Secret in the Vault.

`current_key_tab_secret_version`

(optional) Version of the keytab Secret in the Vault to use.

`backup_key_tab_secret_version`

(optional) Version of the keytab Secret in the Vault to use as a backup.

`is_kerberos_enabled`

(optional) Specifies whether to enable or disable Kerberos.

### DBMS_CLOUD_OCI_FILE_STORAGE_ENDPOINT_T Type

Combination of DNS server name and port.

Syntax
```

```

Fields

Field Description

`hostname`

(required) Name of the DNS server.

`port`

(required) Port of the DNS server.

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_OUTBOUND_CONNECTOR_DETAILS_T Type

Details for creating the outbound connector.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain the outbound connector is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the outbound connector.

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My outbound connector`

`connector_type`

(required) The account type of this outbound connector.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_ENDPOINT_TBL Type

Nested table type of dbms_cloud_oci_file_storage_endpoint_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_LDAP_BIND_ACCOUNT_DETAILS_T Type

Account details for the LDAP bind account to be used by mount targets that use this outbound connector.

Syntax
```

```

`dbms_cloud_oci_file_storage_create_ldap_bind_account_details_t`is a subtype of the`dbms_cloud_oci_file_storage_create_outbound_connector_details_t`type.

Fields

Field Description

`endpoints`

(required) Array of server endpoints to use when connecting with the LDAP bind account.

`bind_distinguished_name`

(required) The LDAP Distinguished Name of the bind account.

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the password for the LDAP bind account in the Vault.

`password_secret_version`

(optional) Version of the password secret in the Vault to use.

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_LDAP_IDMAP_DETAILS_T Type

Mount target details about the LDAP ID mapping configuration.

Syntax
```

```

Fields

Field Description

`schema_type`

(optional) Schema type of the LDAP account.

Allowed values are: 'RFC2307'

`cache_refresh_interval_seconds`

(optional) The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.

`cache_lifetime_seconds`

(optional) The maximum amount of time the mount target is allowed to use a cached entry.

`negative_cache_lifetime_seconds`

(optional) The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.

`user_search_base`

(optional) All LDAP searches are recursive starting at this user. Example: `CN=User,DC=domain,DC=com`

`group_search_base`

(optional) All LDAP searches are recursive starting at this group. Example: `CN=Group,DC=domain,DC=com`

`outbound_connector1_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the first connector to use to communicate with the LDAP server.

`outbound_connector2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second connector to use to communicate with the LDAP server.

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_MOUNT_TARGET_DETAILS_T Type

Details for creating the mount target.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain in which to create the mount target. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to create the mount target.

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My mount target`

`hostname_label`

(optional) The hostname for the mount target's IP address, used for DNS resolution. The value is the hostname portion of the private IP address's fully qualified domain name (FQDN). For example, `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`. Must be unique across all VNICs in the subnet and comply with[RFC 952](https://tools.ietf.org/html/rfc952)and[RFC 1123](https://tools.ietf.org/html/rfc1123). Note: This attribute value is stored in the[PrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/)resource, not in the `mountTarget` resource. To update the `hostnameLabel`, use `GetMountTarget` to obtain the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target's private IPs (`privateIpIds`). Then, you can use[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/UpdatePrivateIp)to update the `hostnameLabel` value. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). Example: `files-1`

`ip_address`

(optional) A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. Note: This attribute value is stored in the[PrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/)resource, not in the `mountTarget` resource. To update the `ipAddress`, use `GetMountTarget` to obtain the[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target's private IPs (`privateIpIds`). Then, you can use[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/UpdatePrivateIp)to update the `ipAddress` value. Example: `10.0.3.3`

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet in which to create the mount target.

`idmap_type`

(optional) The method used to map a Unix UID to secondary groups, if any.

`ldap_idmap`

(optional)

`nsg_ids`

(optional) A list of Network Security Group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

`kerberos`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_REPLICATION_DETAILS_T Type

Details for creating the replication and replication target.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the replication.

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source file system.

`target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target file system.

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. An associated replication target will also created with the same `displayName`. Example: `My replication`

`replication_interval`

(optional) Duration in minutes between replication snapshots.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_SNAPSHOT_DETAILS_T Type

Details for creating the snapshot.

Syntax
```

```

Fields

Field Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system to take a snapshot of.

`name`

(required) Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system. Avoid entering confidential information. Example: `Sunday`

`expiration_time`

(optional) The time when this snapshot will be deleted.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_ERROR_T Type

Details about an error that occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_T Type

A file system and the path that you can use to mount it. Each export resource belongs to exactly one export set. The export's path attribute is not a path in the referenced file system, but the value used by clients for the path component of the remotetarget argument when mounting the file system. The path must start with a slash (/) followed by a sequence of zero or more slash-separated path elements. For any two export resources associated with the same export set, except those in a 'DELETED' state, the path element sequence for the first export resource can't contain the complete path element sequence of the second export resource. For example, the following are acceptable: * /example and /path * /example1 and /example2 * /example and /example1 The following examples are not acceptable: * /example and /example/path * / and /example Paths may not end in a slash (/). No path element can be a period (.) or two periods in sequence (..). All path elements must be 255 bytes or less. No two non-'DELETED' export resources in the same export set can reference the same file system. Use `exportOptions` to control access to an export. For more information, see[Export Options](https://docs.oracle.com/iaas/Content/File/Tasks/exportoptions.htm).

Syntax
```

```

Fields

Field Description

`export_options`

(required) Policies that apply to NFS requests made through this export. `exportOptions` contains a sequential list of `ClientOptions`. Each `ClientOptions` item defines the export options that are applied to a specified set of clients. For each NFS request, the first `ClientOptions` option in the list whose `source` attribute matches the source IP address of the request is applied. If a client source IP address does not match the `source` property of any `ClientOptions` in the list, then the export will be invisible to that client. This export will not be returned by `MOUNTPROC_EXPORT` calls made by the client and any attempt to mount or access the file system through this export will result in an error. **Exports without defined `ClientOptions` are invisible to all clients.** If one export is invisible to a particular client, associated file systems may still be accessible through other exports on the same or different mount targets. To completely deny client access to a file system, be sure that the client source IP address is not included in any export for any mount target associated with the file system.

`export_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's export set.

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's file system.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export.

`lifecycle_state`

(required) The current state of this export.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`path`

(required) Path used to access the associated file system. Avoid entering confidential information. Example: `/accounting`

`is_idmap_groups_for_sys_auth`

(optional) Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.

`time_created`

(required) The date and time the export was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SET_T Type

A set of file systems to export through one or more mount targets. Composed of zero or more export resources.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the export set is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the export set.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My export set`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`lifecycle_state`

(required) The current state of the export set.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`max_fs_stat_bytes`

(optional) Controls the maximum `tbytes`, `fbytes`, and `abytes`, values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.

`max_fs_stat_files`

(optional) Controls the maximum `tfiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.

`time_created`

(required) The date and time the export set was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual cloud network (VCN) the export set is in.

### DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SET_SUMMARY_T Type

Summary information for an export set.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the export set is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the export set.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My export set`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the export set.

`lifecycle_state`

(required) The current state of the export set.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) The date and time the export set was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`vcn_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the virtual cloud network (VCN) the export set is in.

### DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SUMMARY_T Type

Summary information for an export.

Syntax
```

```

Fields

Field Description

`export_set_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's export set.

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export's file system.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this export.

`lifecycle_state`

(required) The current state of this export.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`path`

(required) Path used to access the associated file system. Avoid entering confidential information. Example: `/mediafiles`

`is_idmap_groups_for_sys_auth`

(optional) Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.

`time_created`

(required) The date and time the export was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_FILE_STORAGE_SOURCE_DETAILS_T Type

Source information for the file system.

Syntax
```

```

Fields

Field Description

`parent_file_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system that contains the source snapshot of a cloned file system. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`source_snapshot_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source snapshot used to create a cloned file system. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

### DBMS_CLOUD_OCI_FILE_STORAGE_FILE_SYSTEM_T Type

An NFS file system. To allow access to a file system, add it to an export set and associate the export set with a mount target. The same file system can be in multiple export sets and associated with multiple mount targets. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the file system is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`metered_bytes`

(required) The number of bytes consumed by the file system, including any snapshots. This number reflects the metered size of the file system and is updated asynchronously with respect to updates to the file system. For more information, see[File System Usage and Metering](https://docs.oracle.com/iaas/Content/File/Concepts/FSutilization.htm).

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the file system.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My file system`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`lifecycle_state`

(required) The current state of the file system.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the file system was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the KMS key which is the master encryption key for the file system.

`source_details`

(optional)

`is_clone_parent`

(optional) Specifies whether the file system has been cloned. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`is_hydrated`

(optional) Specifies whether the data has finished copying from the source to the clone. Hydration can take up to several hours to complete depending on the size of the source. The source and clone remain available during hydration, but there may be some performance impact. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm#hydration).

`lifecycle_details`

(optional) Additional information about the current 'lifecycleState'.

`is_targetable`

(optional) Specifies whether the file system can be used as a target file system for replication. The system sets this value to `true` if the file system is unexported, hasn't yet been specified as a target file system in any replication resource, and has no user snapshots. After the file system has been specified as a target in a replication, or if the file system contains user snapshots, the system sets this value to `false`.

`replication_target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication target associated with the file system. Empty if the file system is not being used as target in a replication.

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated file system snapshot policy, which controls the frequency of snapshot creation and retention period of the taken snapshots.

### DBMS_CLOUD_OCI_FILE_STORAGE_FILE_SYSTEM_SUMMARY_T Type

Summary information for a file system.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the file system is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`metered_bytes`

(required) The number of bytes consumed by the file system, including any snapshots. This number reflects the metered size of the file system and is updated asynchronously with respect to updates to the file system.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the file system.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My file system`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system.

`lifecycle_state`

(required) The current state of the file system.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The date and time the file system was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the KMS key used to encrypt the encryption keys associated with this file system.

`source_details`

(optional)

`is_clone_parent`

(optional) Specifies whether the file system has been cloned. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`is_hydrated`

(optional) Specifies whether the data has finished copying from the source to the clone. Hydration can take up to several hours to complete depending on the size of the source. The source and clone remain available during hydration, but there may be some performance impact. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm#hydration).

`lifecycle_details`

(optional) Additional information about the current 'lifecycleState'.

### DBMS_CLOUD_OCI_FILE_STORAGE_FILESYSTEM_SNAPSHOT_POLICY_T Type

A file system snapshot policy is used to automate snapshot creation and deletion. It contains a list of snapshot schedules that define the frequency of snapshot creation for the associated file systems and the retention period of snapshots taken on schedule. For more information, see[Snapshot Scheduling](https://docs.oracle.com/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the file system snapshot policy.

`availability_domain`

(required) The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value. Example: `Uocm:PHX-AD-2`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`lifecycle_state`

(required) The current state of the file system snapshot policy.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'INACTIVE', 'FAILED'

`time_created`

(required) The date and time the file system snapshot policy was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `policy1`

`policy_prefix`

(optional) The prefix to apply to all snapshots created by this policy. Example: `acme`

`schedules`

(optional) The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_FILESYSTEM_SNAPSHOT_POLICY_SUMMARY_T Type

Summary information for a file system snapshot policy.

Syntax
```

```

Fields

Field Description

`availability_domain`

(required) The availability domain that the file system snapshot policy is in. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the file system snapshot policy.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy.

`lifecycle_state`

(required) The current state of this file system snapshot policy.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'INACTIVE', 'FAILED'

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My Filesystem Snapshot Policy`

`time_created`

(required) The date and time that the file system snapshot policy was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2020-02-04T21:10:29.600Z`

`policy_prefix`

(optional) The prefix to apply to all snapshots created by this policy. Example: `acme`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_T Type

Allows administrator to configure a mount target to interact with the administrator's Kerberos infrastructure.

Syntax
```

```

Fields

Field Description

`kerberos_realm`

(required) The Kerberos realm that the mount target will join.

`key_tab_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the keytab secret in the Vault.

`current_key_tab_secret_version`

(optional) Version of the keytab secret in the Vault to use.

`backup_key_tab_secret_version`

(optional) Version of the keytab secert in the Vault to use as a backup.

`is_kerberos_enabled`

(optional) Specifies whether to enable or disable Kerberos.

### DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_KEYTAB_ENTRY_T Type

Details of each keytab entry read from the keytab file.

Syntax
```

```

Fields

Field Description

`principal`

(required) Keytab principal.

`encryption_type`

(required) Encryption type with with keytab was generated. Secure: aes128-cts-hmac-sha256-128 Secure: aes256-cts-hmac-sha384-192 Less Secure: aes128-cts-hmac-sha1-96 Less Secure: aes256-cts-hmac-sha1-96

Allowed values are: 'AES128_CTS_HMAC_SHA256_128', 'AES256_CTS_HMAC_SHA384_192', 'AES128_CTS_HMAC_SHA1_96', 'AES256_CTS_HMAC_SHA1_96'

`key_version_number`

(required) Kerberos KVNO (key version number) for key in keytab entry.

### DBMS_CLOUD_OCI_FILE_STORAGE_KEY_TAB_SECRET_DETAILS_T Type

Secret details of keytabs in Vault.

Syntax
```

```

Fields

Field Description

`key_tab_secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the keytab secret in the Vault.

`current_key_tab_secret_version`

(required) Version of the keytab secret in the Vault to use.

`backup_key_tab_secret_version`

(optional) Version of the keytab secret in the Vault to use as a backup.

### DBMS_CLOUD_OCI_FILE_STORAGE_OUTBOUND_CONNECTOR_T Type

Outbound connectors are used to help File Storage communicate with an external server, such as an LDAP server. An outbound connector contains all the information needed to connect, authenticate, and gain authorization to perform the account's required functions.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the outbound connector is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the outbound connector.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`lifecycle_state`

(required) The current state of this outbound connector.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My outbound connector`

`time_created`

(required) The date and time the outbound connector was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`connector_type`

(required) The account type of this outbound connector.

Allowed values are: 'LDAPBIND'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_BIND_ACCOUNT_T Type

Account details for the LDAP bind account used by the outbound connector.

Syntax
```

```

`dbms_cloud_oci_file_storage_ldap_bind_account_t`is a subtype of the`dbms_cloud_oci_file_storage_outbound_connector_t`type.

Fields

Field Description

`endpoints`

(required) Array of server endpoints to use when connecting with the LDAP bind account.

`bind_distinguished_name`

(required) The LDAP Distinguished Name of the account.

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the password for the LDAP bind account in the Vault.

`password_secret_version`

(optional) Version of the password secret in the Vault to use.

### DBMS_CLOUD_OCI_FILE_STORAGE_OUTBOUND_CONNECTOR_SUMMARY_T Type

Summary information for an outbound connector.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the outbound connector is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the outbound connector.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the outbound connector.

`lifecycle_state`

(required) The current state of this outbound connector.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My outbound connector`

`time_created`

(required) The date and time the outbound connector was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`connector_type`

(required) The account type of this outbound connector.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_BIND_ACCOUNT_SUMMARY_T Type

Summary information for the LDAP bind account used by the outbound connector.

Syntax
```

```

`dbms_cloud_oci_file_storage_ldap_bind_account_summary_t`is a subtype of the`dbms_cloud_oci_file_storage_outbound_connector_summary_t`type.

Fields

Field Description

`endpoints`

(required) Array of server endpoints to use when connecting with the LDAP bind account.

`bind_distinguished_name`

(required) The LDAP Distinguished Name of the account.

### DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_IDMAP_T Type

Mount target details about the LDAP ID mapping configuration.

Syntax
```

```

Fields

Field Description

`schema_type`

(optional) Schema type of the LDAP account.

Allowed values are: 'RFC2307'

`cache_refresh_interval_seconds`

(optional) The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.

`cache_lifetime_seconds`

(optional) The maximum amount of time the mount target is allowed to use a cached entry.

`negative_cache_lifetime_seconds`

(optional) The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.

`user_search_base`

(optional) All LDAP searches are recursive starting at this user. Example: `CN=User,DC=domain,DC=com`

`group_search_base`

(optional) All LDAP searches are recursive starting at this group. Example: `CN=Group,DC=domain,DC=com`

`outbound_connector1_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the first connector to use to communicate with the LDAP server.

`outbound_connector2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second connector to use to communicate with the LDAP server.

### DBMS_CLOUD_OCI_FILE_STORAGE_MOUNT_TARGET_T Type

Provides access to a collection of file systems through one or more VNICs on a specified subnet. The set of file systems is controlled through the referenced export set.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the mount target is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the mount target.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My mount target`

`export_set_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated export set. Controls what file systems will be exported through Network File System (NFS) protocol on this mount target.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`lifecycle_details`

(required) Additional information about the current 'lifecycleState'.

`lifecycle_state`

(required) The current state of the mount target.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`private_ip_ids`

(required) The OCIDs of the private IP addresses associated with this mount target.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the mount target is in.

`idmap_type`

(optional) The method used to map a Unix UID to secondary groups. If NONE, the mount target will not use the Unix UID for ID mapping.

Allowed values are: 'LDAP', 'NONE'

`ldap_idmap`

(optional)

`nsg_ids`

(optional) A list of Network Security Group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

`kerberos`

(optional)

`time_created`

(required) The date and time the mount target was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_MOUNT_TARGET_SUMMARY_T Type

Summary information for the specified mount target.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the mount target is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the mount target.

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My mount target`

`export_set_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated export set. Controls what file systems will be exported using Network File System (NFS) protocol on this mount target.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target.

`lifecycle_state`

(required) The current state of the mount target.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`private_ip_ids`

(required) The OCIDs of the private IP addresses associated with this mount target.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet the mount target is in.

`nsg_ids`

(optional) A list of Network Security Group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

`time_created`

(required) The date and time the mount target was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_T Type

Replications are the primary resource that governs the policy of cross-region replication between source and target file systems. Replications are associated with a secondary resource called a`REPLICATION_TARGET`Type located in another availability domain in the same or different region. The replication retrieves the delta of data between two snapshots of a source file system and sends it to the associated `ReplicationTarget`, which applies it to the target file system. For more information, see[File System Replication](https://docs.oracle.com/iaas/Content/File/Tasks/FSreplication.htm).

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the replication.

`availability_domain`

(optional) The availability domain that contains the replication. May be unset as a blank or `NULL` value. Example: `Uocm:PHX-AD-2`

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`lifecycle_state`

(required) The current lifecycle state of the replication.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My replication`

`time_created`

(required) The date and time the replication was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-01-04T20:01:29.100Z`

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source file system.

`target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target file system.

`replication_target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the`REPLICATION_TARGET`Type.

`replication_interval`

(optional) Duration in minutes between replication snapshots.

`last_snapshot_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last snapshot that has been replicated completely. Empty if the copy of the initial snapshot is not complete.

`recovery_point_time`

(optional) The`SNAPSHOT_TIME`Function of the most recent recoverable replication snapshot in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-04-04T20:01:29.100Z`

`delta_status`

(optional) The current state of the snapshot during replication operations.

Allowed values are: 'IDLE', 'CAPTURING', 'APPLYING', 'SERVICE_ERROR', 'USER_ERROR', 'FAILED', 'TRANSFERRING'

`lifecycle_details`

(optional) Additional information about the current 'lifecycleState'.

`delta_progress`

(optional) Percentage progress of the current replication cycle.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_ESTIMATE_T Type

Details for response from replication estimation.

Syntax
```

```

Fields

Field Description

`change_rate_in_m_bps`

(required) The rate of change on source filesystem which was used to provide the estimate in MegaBytes per second.

`is_replication_supported`

(required) Specifies whether replication can be enabled on the file system.

`minimum_supported_interval_in_minutes`

(required) The minimum supported replication interval for specified file system in minutes.

`estimated_base_copy_time_in_minutes`

(required) The approximate time required for the base sync between source and target to finish.

`allowed_target_regions`

(required) Array of allowed target region names which can be paired with source file system.

### DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_SUMMARY_T Type

Summary information for a replication.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the replication is in. The replication must be in the same availability domain as the source file system. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the replication.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`lifecycle_state`

(required) The current state of this replication. This resource can be in a `FAILED` state if replication target is deleted instead of the replication resource.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(required) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My replication`

`time_created`

(required) The date and time the replication was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2020-02-04T21:10:29.600Z`

`replication_interval`

(optional) Duration in minutes between replication snapshots.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

`recovery_point_time`

(optional) The `snapshotTime` of the most recent recoverable replication snapshot in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-04-04T20:01:29.100Z`

### DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_TARGET_T Type

Replication targets are associated with a primary resource called a`REPLICATION`Type located in another availability domain in the same or different region. The replication retrieves the delta of data between two snapshots of a source file system and sends it to the associated `ReplicationTarget`, which applies it to the target file system. All operations (except `DELETE`) must be done using the associated replication resource. Deleting a `ReplicationTarget` allows the target file system to be exported. Deleting a `ReplicationTarget` does not delete the associated `Replication` resource, but places it in a `FAILED` state. For more information, see[File System Replication](https://docs.oracle.com/iaas/Content/File/Tasks/FSreplication.htm).

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the replication resource is in. May be unset as a blank or NULL value. Example: `Uocm:PHX-AD-1`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the replication.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication.

`lifecycle_state`

(required) The current state of this replication.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(required) A user-friendly name. This name is same as the replication display name for the associated resource. Example: `My Replication`

`time_created`

(required) The date and time the replication target was created in target region. in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-01-04T20:01:29.100Z`

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of source filesystem.

`target_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of target filesystem.

`replication_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of replication.

`last_snapshot_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the last snapshot snapshot which was completely applied to the target file system. Empty while the initial snapshot is being applied.

`recovery_point_time`

(optional) The snapshotTime of the most recent recoverable replication snapshot in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-04-04T20:01:29.100Z`

`delta_status`

(optional) The current state of the snapshot during replication operations.

Allowed values are: 'IDLE', 'CAPTURING', 'APPLYING', 'SERVICE_ERROR', 'USER_ERROR', 'FAILED', 'TRANSFERRING'

`delta_progress`

(optional) Percentage progress of the current replication cycle.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

### DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_TARGET_SUMMARY_T Type

Summary information for replication target.

Syntax
```

```

Fields

Field Description

`availability_domain`

(optional) The availability domain the replication target is in. Must be in the same availability domain as the target file system. Example: `Uocm:PHX-AD-1`

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the replication.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the replication target.

`lifecycle_state`

(required) The current state of this replication.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(required) A user-friendly name. This name is the same as the associated replication name. Example: `My replication`

`time_created`

(required) The date and time the replication was created in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-02-02T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_details`

(optional) Additional information about the current 'lifecycleState'.

`recovery_point_time`

(optional) The snapshotTime of the most recent recoverable replication snapshot in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2021-04-04T20:01:29.100Z`

### DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_T Type

A point-in-time snapshot of a specified file system.

Syntax
```

```

Fields

Field Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system from which the snapshot was created.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot.

`lifecycle_state`

(required) The current state of the snapshot.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`name`

(required) Name of the snapshot. This value is immutable. Avoid entering confidential information. Example: `Sunday`

`time_created`

(required) The date and time the snapshot was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`snapshot_type`

(optional) Specifies generation type of the snapshot.

Allowed values are: 'USER', 'POLICY_BASED', 'REPLICATION'

`snapshot_time`

(optional) The date and time the snapshot was taken, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. This value might be the same or different from `timeCreated` depending on the following factors: - If the snapshot is created in the original file system directory. - If the snapshot is cloned from a file system. - If the snapshot is replicated from a file system. Example: `2020-08-25T21:10:29.600Z`

`provenance_id`

(optional) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`is_clone_source`

(optional) Specifies whether the snapshot has been cloned. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`expiration_time`

(optional) The time when this snapshot will be deleted.

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system snapshot policy that created this snapshot.

### DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SUMMARY_T Type

Summary information for a snapshot.

Syntax
```

```

Fields

Field Description

`file_system_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the file system from which the snapshot was created.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the snapshot.

`lifecycle_state`

(required) The current state of the snapshot.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`name`

(required) Name of the snapshot. This value is immutable. Avoid entering confidential information. Example: `Sunday`

`time_created`

(required) The date and time the snapshot was created, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. Example: `2016-08-25T21:10:29.600Z`

`snapshot_type`

(optional) Specifies the generation type of the snapshot.

Allowed values are: 'USER', 'POLICY_BASED', 'REPLICATION'

`snapshot_time`

(optional) The date and time the snapshot was taken, expressed in[RFC 3339](https://tools.ietf.org/rfc/rfc3339)timestamp format. This value might be the same or different from `timeCreated` depending on the following factors: - If the snapshot is created in the original file system directory. - If the snapshot is cloned from a file system. - If the snapshot is replicated from a file system. Example: `2020-08-25T21:10:29.600Z`

`expiration_time`

(optional) The time when this snapshot will be deleted.

`provenance_id`

(optional) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)identifying the parent from which this snapshot was cloned. If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value. If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`is_clone_source`

(optional) Specifies whether the snapshot has been cloned. See[Cloning a File System](https://docs.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).

`lifecycle_details`

(optional) Additional information about the current `lifecycleState`.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_EXPORT_DETAILS_T Type

Details for updating the export.

Syntax
```

```

Fields

Field Description

`is_idmap_groups_for_sys_auth`

(optional) Whether or not the export should use ID mapping for Unix groups rather than the group list provided within an NFS request's RPC header. When this flag is true the Unix UID from the RPC header is used to retrieve the list of secondary groups from a the ID mapping subsystem. The primary GID is always taken from the RPC header. If ID mapping is not configured, incorrectly configured, unavailable, or cannot be used to determine a list of secondary groups then an empty secondary group list is used for authorization. If the number of groups exceeds the limit of 256 groups, the list retrieved from LDAP is truncated to the first 256 groups read.

`export_options`

(optional) New export options for the export. **Setting to the empty array will make the export invisible to all clients.** Leaving unset will leave the `exportOptions` unchanged.

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_EXPORT_SET_DETAILS_T Type

Details for updating the export set.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My export set`

`max_fs_stat_bytes`

(optional) Controls the maximum `tbytes`, `fbytes`, and `abytes` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.

`max_fs_stat_files`

(optional) Controls the maximum `ffiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_FILE_SYSTEM_DETAILS_T Type

Details for updating the file system.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My file system`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`kms_key_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Key Management master encryption key to associate with the specified file system. If this value is empty, the Update operation will remove the associated key, if there is one, from the file system. (The file system will continue to be encrypted, but with an encryption key managed by Oracle.) If updating to a new Key Management key, the old key must remain enabled so that files previously encrypted continue to be accessible. For more information, see[Overview of Key Management](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).

`filesystem_snapshot_policy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the associated file system snapshot policy, which controls the frequency of snapshot creation and retention period of the taken snapshots. If string is empty, the policy reference (if any) would be removed.

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_FILESYSTEM_SNAPSHOT_POLICY_DETAILS_T Type

Details for updating the file system snapshot policy.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `policy1`

`policy_prefix`

(optional) The prefix to apply to all snapshots created by this policy. Example: `acme`

`schedules`

(optional) The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy. If using the CLI, provide the schedule as a list of JSON strings, with the list wrapped in quotation marks, i.e. ``` --schedules '[{\"timeZone\":\"UTC\",\"period\":\"DAILY\",\"hourOfDay\":18},{\"timeZone\":\"UTC\",\"period\":\"HOURLY\"}]' ```

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_KERBEROS_DETAILS_T Type

Kerberos details needed to update configuration.

Syntax
```

```

Fields

Field Description

`kerberos_realm`

(optional) Kerberos realm that this mount target will join.

`key_tab_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the keytab secret in the Vault.

`current_key_tab_secret_version`

(optional) Version of the keytab secret in the Vault to use.

`backup_key_tab_secret_version`

(optional) Version of the keytab secert in the Vault to use as a backup.

`is_kerberos_enabled`

(optional) Specifies whether to enable or disable Kerberos.

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_LDAP_IDMAP_DETAILS_T Type

Mount target details about the LDAP ID mapping configuration.

Syntax
```

```

Fields

Field Description

`schema_type`

(optional) Schema type of the LDAP account.

Allowed values are: 'RFC2307'

`cache_refresh_interval_seconds`

(optional) The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.

`cache_lifetime_seconds`

(optional) The maximum amount of time the mount target is allowed to use a cached entry.

`negative_cache_lifetime_seconds`

(optional) The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.

`user_search_base`

(optional) All LDAP searches are recursive starting at this user. Example: `CN=User,DC=domain,DC=com`

`group_search_base`

(optional) All LDAP searches are recursive starting at this group. Example: `CN=Group,DC=domain,DC=com`

`outbound_connector1_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the first connector to use to communicate with the LDAP server.

`outbound_connector2_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the second connector to use to communicate with the LDAP server.

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_MOUNT_TARGET_DETAILS_T Type

Details for updating the mount target.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My mount target`

`idmap_type`

(optional) The method used to map a Unix UID to secondary groups, if any.

`ldap_idmap`

(optional)

`nsg_ids`

(optional) A list of Network Security Group[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)associated with this mount target. A maximum of 5 is allowed. Setting this to an empty array after the list is created removes the mount target from all NSGs. For more information about NSGs, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

`kerberos`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_OUTBOUND_CONNECTOR_DETAILS_T Type

Details for updating the outbound connector.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information. Example: `My Outbound Connector`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_REPLICATION_DETAILS_T Type

Details for updating the replication and replication target.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information. A replication target will also updated with the same `displayName`. Example: `My replication`

`replication_interval`

(optional) Duration in minutes between replication snapshots.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_SNAPSHOT_DETAILS_T Type

Details for updating the snapshot.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`expiration_time`

(optional) The UTC time when this snapshot will be deleted. To remove the expiration time, set this field to the minimum date-time value using Date(0). Example: `Thu Jan 01 01:00:00 GMT 1970`

### DBMS_CLOUD_OCI_FILE_STORAGE_VALIDATE_KEY_TABS_DETAILS_T Type

Validate keytabs request details.

Syntax
```

```

Fields

Field Description

`mount_target_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the mount target whose keytabs are to be validated.

`key_tab_secret_details`

(optional)

### DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_KEYTAB_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_file_storage_kerberos_keytab_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FILE_STORAGE_VALIDATE_KEY_TABS_RESPONSE_DETAILS_T Type

Validate keytabs response details.

Syntax
```

```

Fields

Field Description

`current_kerberos_keytab_entries`

(required) An array of keytab entries (principal, encryptionType, keyVersionNumber).

`backup_kerberos_keytab_entries`

(optional) An array of keytab entries (principal, encryptionType, keyVersionNumber).

- [File Storage Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CA3E2DBA-AD63-41D7-B88E-22E7E8DA6892)
- [DBMS_CLOUD_OCI_FILE_STORAGE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-AE3A1217-6FE3-4808-BCDA-C4BD51129758)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_FILE_SYSTEM_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-F81AE4ED-17FB-4784-BEA0-A8E02AF9327D)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_FILESYSTEM_SNAPSHOT_POLICY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-C17FA126-15F2-4448-9FCD-D950126C8011)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_MOUNT_TARGET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-8A3C35E0-3794-4B6A-8467-C05C0AC4AF25)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_OUTBOUND_CONNECTOR_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-43B45957-C0B3-4F4F-B224-0117230C3B28)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CHANGE_REPLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CEC3EE34-A179-4DCA-A6E4-CAFDE457CC67)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CLIENT_OPTIONS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7C8DFD87-4E8D-4049-9B60-7E7B0213D312)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CLIENT_OPTIONS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-4D75A9C2-E224-40CC-B781-E8B279F7799E)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-8D133B39-72D6-4165-90DE-439790BB11BF)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_FILE_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7B3E2091-7AB8-4B7F-9D9D-F2D9C27BFBC8)
- [DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-0ABD6A6B-CB35-4D06-B16F-8FF8D60FE92D)
- [DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SCHEDULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-1EEE355F-2CB0-41FF-A8B9-D3A52ED6A223)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_FILESYSTEM_SNAPSHOT_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-D210AE5A-FC81-4431-8DE6-D10E50223A77)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_KERBEROS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-78B9107C-57CA-43BD-8E05-39EFC33A2245)
- [DBMS_CLOUD_OCI_FILE_STORAGE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-B220BE1A-9016-4E36-ADAB-DE310062B9CD)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_OUTBOUND_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-F573F8E8-E26C-4E08-A890-23112E477CDB)
- [DBMS_CLOUD_OCI_FILE_STORAGE_ENDPOINT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CD17451D-77CE-4F84-8D3B-BEA9A810DF8E)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_LDAP_BIND_ACCOUNT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-A8D61B74-5249-4778-9C9A-750BFFB21B24)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_LDAP_IDMAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-868B3AF3-8C9A-49FA-9D97-B7165D268BD4)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_MOUNT_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CCA8F441-8CF9-4040-840E-54678BCB5CAC)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_REPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-723C5A06-A2F6-4634-BD22-C1C28139BCDA)
- [DBMS_CLOUD_OCI_FILE_STORAGE_CREATE_SNAPSHOT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-A717A77F-9136-456A-8889-61F3F42085F4)
- [DBMS_CLOUD_OCI_FILE_STORAGE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-760F4DB9-FB68-4E33-BB24-02F1D4C96F43)
- [DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-9F11131D-FE84-49C0-8984-ED05A104FFE2)
- [DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-DDBC71C6-D067-413D-8D45-7AD9605365D5)
- [DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-B5472645-0F2E-4554-A282-FA51D6B39E81)
- [DBMS_CLOUD_OCI_FILE_STORAGE_EXPORT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-DCFA1AC5-2E78-411D-B715-A1DEA838F2CA)
- [DBMS_CLOUD_OCI_FILE_STORAGE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7EA46DDE-AD97-428E-ADB3-EF034DDF0BD6)
- [DBMS_CLOUD_OCI_FILE_STORAGE_FILE_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-79E6E238-07F2-4B7F-B14C-9E15ED95AF05)
- [DBMS_CLOUD_OCI_FILE_STORAGE_FILE_SYSTEM_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-E9E30CC8-D125-4262-8F28-C1F86D085443)
- [DBMS_CLOUD_OCI_FILE_STORAGE_FILESYSTEM_SNAPSHOT_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-AAA65491-3D01-4F80-8B26-BEA2EF6B87B2)
- [DBMS_CLOUD_OCI_FILE_STORAGE_FILESYSTEM_SNAPSHOT_POLICY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-F2941282-2530-4AA7-85B2-ADCB9B1705A7)
- [DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-C9885FCE-F4CE-4D0B-B671-DB38628DB1A1)
- [DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_KEYTAB_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-A0FB2FFD-4FAD-40D6-881C-E4D6703F7E80)
- [DBMS_CLOUD_OCI_FILE_STORAGE_KEY_TAB_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7DA2DD17-9D54-468F-9D1B-E8C58F69F398)
- [DBMS_CLOUD_OCI_FILE_STORAGE_OUTBOUND_CONNECTOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-DD1FE6E8-352D-4E2D-99B2-60AD3EA481E0)
- [DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_BIND_ACCOUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-128B38CB-330E-4592-B8A6-DA7686EC103B)
- [DBMS_CLOUD_OCI_FILE_STORAGE_OUTBOUND_CONNECTOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-3EB58D53-4C72-43D3-A49C-A5D8FF0E2CC9)
- [DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_BIND_ACCOUNT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-C0893B38-E3EF-4718-A2B4-6E1B8A5EBDD3)
- [DBMS_CLOUD_OCI_FILE_STORAGE_LDAP_IDMAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-AAC58544-84C5-4A8B-B451-3A1CBEBD681A)
- [DBMS_CLOUD_OCI_FILE_STORAGE_MOUNT_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-5CE1E2A5-071B-425E-AEBC-FFC5E888A90A)
- [DBMS_CLOUD_OCI_FILE_STORAGE_MOUNT_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-DA9CF6EA-0652-45E9-B83C-4C21F189268E)
- [DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-B3ABEE13-0AC5-49EF-98D2-0C8A95DBCC18)
- [DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_ESTIMATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-359E6EBC-EDAA-48CE-8696-F353965A6828)
- [DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-3DFB0CBF-27D3-409F-A0AE-A7724B6B608D)
- [DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7E79EA37-51A8-40E7-A0C0-0A6599493823)
- [DBMS_CLOUD_OCI_FILE_STORAGE_REPLICATION_TARGET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-038328F7-9D45-4062-94D1-475B28B6C336)
- [DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CDA3B312-22CF-4F2F-974E-F65B7D5FC1F0)
- [DBMS_CLOUD_OCI_FILE_STORAGE_SNAPSHOT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-7FFDBDF4-E066-4D8E-B9B4-DABDDFCA6A9C)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-CE32C156-09EC-4131-81AB-B44B9C9E9A6E)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_EXPORT_SET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-6F605D14-0787-4115-8EC9-1B692FE26168)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_FILE_SYSTEM_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-DDF288FF-BC3E-464E-A980-C6904E362A26)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_FILESYSTEM_SNAPSHOT_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-833AB763-124D-4F38-94BC-93A19E662EB7)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_KERBEROS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-1E98E781-0684-4B1A-895C-FB5F8814346E)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_LDAP_IDMAP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-F96C3061-93E5-4E29-AE6F-8787B7485138)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_MOUNT_TARGET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-59AB5392-592E-4AD4-93E3-38F9E4947F23)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_OUTBOUND_CONNECTOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-A3D6B760-37B3-4B0B-B521-0F4F6013860A)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_REPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-94027A35-ABDD-42E4-AD4D-6EF4BB9525DA)
- [DBMS_CLOUD_OCI_FILE_STORAGE_UPDATE_SNAPSHOT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-6323EBEE-CE23-4E59-8F18-ECE0A4590223)
- [DBMS_CLOUD_OCI_FILE_STORAGE_VALIDATE_KEY_TABS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-ABA48E95-A322-41B7-9148-AB8A3DF97E68)
- [DBMS_CLOUD_OCI_FILE_STORAGE_KERBEROS_KEYTAB_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-4E7E3F01-9160-4B78-8E33-B2A8B85592A2)
- [DBMS_CLOUD_OCI_FILE_STORAGE_VALIDATE_KEY_TABS_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/file_storage_t.html#ADSDK-GUID-F614838F-D0A3-4DB8-9954-A1BD6EF50774)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
