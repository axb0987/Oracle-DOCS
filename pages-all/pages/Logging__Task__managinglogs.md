# Logs and Log Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm
- Fetched: 2026-09-05 02:38 CDT

# Logs and Log Groups

Use Oracle Cloud Infrastructure Logging to manage logs and log groups.

Logs contain critical diagnostic information that tells you how your resources are performing and being accessed. You can enable logging on supported resources. To see a list of supported resources grouped by service, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/service_logs.htm#supported_services).

Log groups are logical containers for organizing logs. Logs must always be inside log groups. You must create a log group to enable a log.

Use log groups to limit access to sensitive logs with IAM policy. With log groups, you don't have to rely on complex compartment hierarchies to secure your logs. For example, say the default log group in a single compartment is where you store logs for the entire tenancy. You grant access to the compartment for log administrators with IAM policy as you normally would. However, let's say some projects contain personally identifiable information (PII) and those logs can only be viewed by a select group of log administrators. Log groups allow you to put logs that contain PII into a separate log group, and then use IAM policy to restrict access so that only a selected set of log administrators have the elevated access.
[

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

Administrators : for policy samples specific to logs and log groups, see[Required Permissions for Working with Logs and Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#required_permissions_logs_groups).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). If you want to know more about writing policies for Logging, see[Details for Logging](https://docs.oracle.com/iaas/Content/Identity/policyreference/loggingpolicyreference.htm).

## Required Permissions for Working with Logs and Log Groups

To enable service logs in a resource, a user must be granted`manage`access on the log group and access to the resource. In general, inspect access on the resource is enough, but check for specific resources. Inspect access provides permission to update the resource and permission for the log group that contains the log.

Logs and log groups use the`log-group`resource-type, but to search the contents of logs you must use a different resource-type.

[Managing log groups and log objects](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

To manage groups or objects, use verbs for log-groups:
```

```

This allows users in group A to create, update, or delete log groups and log objects in compartment C.

[To provision agent configurations](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

Three different types of access are needed:
- Access to operate on configurations.
- Access to operate on log groups.
- Inspect capabilities on dynamic groups or groups.
To have access to configurations, the policy must be:
```

```

[To create, update, or delete custom logs used as a destination in a configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

This policy allows users in compartment B to create, update, or delete configurations in compartment X.
To provide a destination for the logs incoming from the configuration, you need`log-groups`access:
```

```

[To assign a configuration to a set of instances](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

To assign a configuration to a set of instances, you need inspect access to the dynamic group or group that identifies the instances:
```

```

[Enable instances to push logs into the Logging service](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

To allow instances to push logs, the instances need to have access to get a configuration and push the logs.`log-content`controls this permission (where`X`is the compartment where the configurations are located):
```

```

[To view logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

To view logs in the Console (Search), the following is required:
```

```

[Example log search policy](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

To allow a group to read the contents of indexed logs:
```

```

[Example policies for logs and log groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

In these examples, policy statements use GroupA as the name of the group.

To allow a group to view the log groups in the tenancy (or in a compartment), requires`inspect`access:
```

```

To allow a group to read metadata for logs or log groups, requires`read`access:
```

```

To allow a group to update log groups, or the logs in them, requires`use`access:
```

```

To enable a log on a resource (or to create and delete log groups and the logs in them), requires`manage`access:
```

```

To allow usage of a specific log group or groups , use a`where`clause with the`target.loggroup.id`variable. For example:
```

```

To specify multiple log groups:
```

```

[Custom logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#)

For custom logs the following is required. This policy is needed to allow the user to search logs through the Console Search page:
```

```

Note  
  
Even though this policy is described for usage with custom logs, the policy is also true for all logs.`LOG_CONTENT_READ`allows reading logs from both custom and OCI service logs. It is identical in behavior to this policy:
```

```

The following is needed for the agent that uses the instance principal on the virtual machine to send logs:
```

```

Note  
  
If a user group is being used instead of a dynamic group for pushing custom logs, replace the dynamic group name with the user group name in these policies.

For custom logs, if you use`allow dynamic-group dynamicGroup1 to use log-content in compartment c`, the instances in that dynamic group get permission to download the configuration, send logs, and can search logs.

### IAM Policy Requirements for Resources

In addition to the permissions to work with the log group, to add service logs to a resource you must have the update permission for the resource. For many resources, the update permission is granted with the`use`verb. For example, users who can`use`buckets in CompartmentA, can also enable logging on a bucket in CompartmentA.

However, some resources don't include permission to update a resource with the`use`verb. For example, to update a rule for the Events service, you must have the full`manage`permission. To enable a log on an Events rule (or any other resource that doesn't include the update permission with the`use`verb), you must have the`manage`permission.

To allow a group to enable logging for these resources, without granting the full permissions of`manage`, you can add a policy statement to grant only the`<RESOURCE> _UPDATE`permission (or, in the case of the Events service,`<RESOURCE> _MODIFY`) from the`manage`verb. For example, to allow a group EventUsers to enable logs on Events rules in CompartmentA, you could write a policy like the following:
```

```

For information about resource permissions, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).

### VCN Flow Logs IAM Policy

In addition to[Required Permissions for Working with Logs and Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#required_permissions_logs_groups), subnet read and update permissions are required for managing VCN Flow Logs.

To provide subnet permissions, use one of the following policies, listed in order from broader to narrowed privileges:

```

```

Or:

```

```

Or:

```

```

This group is similar to what is described for`EventUsers`in[IAM Policy Requirements for Resources](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#iam_policy_requirements_for_resources).

### Example Scenario

Your company has an Operations department. Within the Operations department are several costs centers. You want to be able to tag resources that belong to the Operations department with the appropriate cost center.
- Create a log group called "confidential". Avoid entering confidential information.
- Add logs with sensitive data to the "confidential" log group.

An employee named Alice already belongs to the group BucketManagers. Alice can manage buckets in CompartmentA. You want Alice and other members of BucketManagers group to be able to enable logs on buckets in CompartmentA.

To grant the BucketManagers group access to the sensitive data log group (and only the sensitive data log group), add the following statements to the BucketManagers policy:
```

```

Alice can now enable logs to bucket resources in CompartmentA.

## Log and Log Group Names

For log group names, the first character must start with a letter. Otherwise, the following guidelines apply to both log and log group names:
- Use from 1 to 256 characters.
- Valid characters are letters (upper or lowercase), numbers, hyphens, underscores, and periods.
- Log and log group names are case-sensitive. Logging handles write-log and WRITE-log as separate logs.
-
