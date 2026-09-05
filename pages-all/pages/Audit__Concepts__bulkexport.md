# Bulk Export of Audit Log Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/bulkexport.htm
- Fetched: 2026-09-05 01:39 CDT

# Bulk Export of Audit Log Events

Describes how to export Audit log events in bulk.

If you make your request after June 30, 2023, use the Logging service and Service Connector Hub to request a bulk export of audit logs. For more information see,[Scenario: Archiving Logs to Object Storage](https://docs.oracle.com/iaas/Content/connector-hub/archivelogs.htm).

This page outlines the previous process of how to request a bulk export of audit logs.

## Highlights

- Administrators have full control of the buckets and can provide access to others with IAM policy statements.
- 

Exported logs remain available indefinitely.
Tip  
  
You can automatically manage archiving and deleting logs using Object Storage. See[Using Object Lifecycle Management](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm).
- Specify all the regions you want exported in your request. If you only request some regions, then decide later you want to add other regions, you must make another request.
- To disable your bulk export, contact Oracle support. New logs will stop being added to the bucket, and audit logs will only be available through the Console, based on the retention period you have defined.

## Required IAM Policy

To access the bucket where Oracle exports the audit logs, you must be a member of the Administrators group. See[The Administrators Group and Policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The)

## Requesting an Export of Audit Logs

Note  
  
If you make your request after June 30, 2023, use the Logging service and Service Connector Hub to request a bulk export of audit logs. For more information see,[Scenario: Archiving Logs to Object Storage](https://docs.oracle.com/iaas/Content/connector-hub/archivelogs.htm).

For customers that have previously used this workflow, a member of the Administrators group for your tenancy must create a ticket at[My Oracle Support](http://support.oracle.com/)and provide the following information:
- Ticket name: Export Audit Logs - &lt;your_company_name&gt;
- Tenancy OCID
- Regions

For example:
- Ticket name: Export Audit Logs - ACME
- Tenancy OCID: ocid1.tenancy.oc1. &lt;unique_ID&gt;
- Regions: US East (Ashburn), region identifier= us-ashburn-1; (US West (Phoenix)), region identifier = us-phoenix-1
Note  
  
It can take 5-10 business days before your My Oracle Support ticket is complete and the logs are available to you.

## Bucket and Object Details

This section specifies the naming conventions of the bucket and objects you receive.

### Bucket Name Format

Oracle support creates buckets for audit log exports using the following naming format:

`oci-logs`.`_audit`. &lt;compartment_OCID&gt;
- `oci-logs`identifies that Oracle created this bucket.
- `_audit`identifies that the bucket contains audit events.
- &lt;compartment_OCID&gt; identifies the compartment where the audit events were generated.

For example:
```

```

Important  
  
If the OCID of the compartment that generated the audit log contains a colon, your bucket name will not match the OCID. To create a bucket, Oracle must substitute colon characters (`:`) from the OCID with dot characters (`.`) in the bucket name.

### Object Name Format

Objects use the following naming format:

&lt;region&gt; / &lt;ad&gt; / &lt;YYYY-MM-DDTHH:MMZ&gt; [_ &lt;seqNum&gt; ].log.gz
- &lt;region&gt; identifies the region where the audit events were generated.
- &lt;ad&gt; identifies the availability domain where the audit events were generated.
- &lt;YYYY-MM-DDTHH:MMZ&gt; identifies the start time of the earliest audit event listed in the object.
- [_ &lt;seqNum&gt; ] identifies a conditional sequence number. If present, this number means that either an event came in late or the object became too large to write. Sequence numbers start at two. Apply multiple sequence numbers to the original object in the order listed.

For example:
```

```

### File Format

Files list a single audit event per line. For more information, see[Contents of an Audit Log Event](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/../Reference/logeventreference.htm).
Note
