# Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/logs.htm
- Fetched: 2026-09-05 03:11 CDT

# Logs

Logs displays log activity and the details of each logged event within a specified time frame. Logs enable you to understand what rules and countermeasures are triggered by requests and are used as a basis to move request handling into block mode. Logs can come from Access Control, Protection Rules, or Bot events.
Note  
  

If you have concerns about General Data Protection Regulation (GDPR) requirements, Logs can be disabled for the WAF service. You can use My Oracle Support to file a service request to disable Logs.

When working with the WAF service, consider the following information:

- The log retention policy for the WAF service is seven days; however, you can request to set up an S3 bucket and have more logs delivered to it. The logs in your bucket can be kept as long as you want.
- Only "Standard" OCI buckets are supported. The "Archive" storage tier isn't supported.
- Log delivery to ELK Stack is only supported to OCI and S3 buckets. Raw logs are sent to the buckets. From the buckets, you can implement them into elastic search.

## Viewing Logs

Describes the different methods to view logs for an edge policy.

You can filter logs by the following log types:
- Access Rules
- CAPTCHA Challenge
- JavaScript Challenge
- Protection Rules
- Human Interaction Challenge
- Device Fingerprinting Challenge
- Threat Intelligence Feeds
- Address Rate Limiting
- Access

Use one of the following methods to view logs for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/logs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/logs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/logs.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the WAF policies displayed:

- 

Name
- 

Policy Type
- 

Status
- Select the edge policy whose logs you want to view.
The Edge Policy Details dialog box appears.
- Select Logs under Resources .

The Logs list appears.
- (Optional) Complete one or more of the following Filters to limit the log information to the values you enter:

- 

Start date
- 

Start time
- 

End date
- 

End time
- 

Request URL
- 

Client IP address
- 

Country name
- (Optional) Check one or more of the following Action filters to limit the log information to the selected options:

- 

Detect
- 

Block
- 

Bypass
- 

Log
- 

Redirected
- (Optional) Check one or more of the following Log type filters to limit the log information to the selected options:

- 

Access rules
- 

CAPTCHA challenge
- 

JavaScript challenge
- 

Protection rules
- 

Human interaction challenge
- 

Device fingerprinting challenge
- 

Threat intelligence feeds
- 

Address rate limiting
- 

Access

Only log information containing the checked actions is displayed.
- Select the plus sign next to the Alert Type you want to view.
Log entries are displayed based on the options you chose.
- 

This task can't be performed using the CLI.
- 

Run the[ListWafLogs](https://docs.oracle.com/iaas/api/#/en/waas/latest/WafLog/ListWafLogs)operation to view log activity.

You can filter logs by the following logType options:
- 

ACCESS_RULES
- 

CAPTCHA_CHALLENGE
- 

JAVASCRIPT_CHALLENGE
- 

PROTECTION_RULES
- 

HUMAN_INTERACTION_CHALLENGE
- 

DEVICE_FINGERPRINT_CHALLENGE
- 

THREAT_INTELLIGENCE_FEEDS
- 

ADDRESS_RATE_LIMITING
- 

ACCESS

Logs can be filtered by logType by making the following request:
```

```

For example:
```

```

The following response output for the filtered logs is returned:
```

```

## Delivering WAF Logs to Object Storage

Describes how to deliver WAF logs to an object storage bucket for longer-term storage and access.

This task requires creating an object storage bucket or using an existing one. Familiarize yourself with object storage buckets and how to create and manage them before proceeding with delivering WAF log data. See[Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm).

WAF logs have a limited retention rate. You can save them indefinitely by delivering your WAF log data to an object storage bucket within your tenancy. Create and configure your object storage bucket first, then submit a support request to Oracle with the required information to have your WAF logs delivered to the bucket.

- Access the Object Storage service and create a bucket with`manage-object-family`permissions.

Only Standard object storage buckets are supported. The Archive storage tier is not supported. Decide on Oracle or user-managed keys. User-managed keys must be in KMS. See[Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm)for more information.
- Set the bucket's Visibility to Public.
- Create or configure a user with a customer secret key.

The WAF needs a key and secret to authenticate to OCI bucket for writing. This key is attached to a user. This user must have write permission on the bucket for WAF logs. Record the access key and secret for the user and store in a save location.
- Add a user to a group, and create an identity policy to grant permission for that group to be able to write to bucket.

For example, if the bucket is in compartment`MSSpoc`and group name is`wafBucketLogGroup`, the identity statement would be:
```

```

The policy is created in the compartment`MSSpoc`.
- Create a file in the bucket that includes the following credentials:

- 

Web App (domain name for WAF policy):
- 

SecretKey :
- 

AccessKey :
- 

Object storage bucket_region :
- 

Object storage bucket_name :
- 

Namespace :
- 

Endpoint Url :`https:// namespace .compat.objectstorage. region .oraclecloud.com`
- 

Upload prefix (file format for the logs. Default is`%{[webapp_domain]}_/%{+YYYY}/%{+MM}/%{+dd})`:
Note  
  

All logs for the web application (including other domains) go into a single folder named based on the main domain. You cannot set the log delivery only for the main domain or only for the additional domain.
- Create a pre-authenticated request for a specific object as follows:
- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Select the compartment where the bucket is located.
- Select the bucket name.
- Select Objects under Resources to display the list of objects.
- Select the file that contains bucket credentials, and then select Pre- Authenticated Requests under Resources .
- Select Create Pre-Authenticated Request .
- Create an Oracle Support request (My Oracle Support) to have your WAF logs delivered to the object storage bucket. Your support request must contain the Pre-Authenticated Request URL with the file you created that contains the bucket credentials.
