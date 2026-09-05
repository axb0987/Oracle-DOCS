# Creating an Object Storage Object Lifecycle Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm
- Fetched: 2026-09-05 02:51 CDT

# Creating an Object Storage Object Lifecycle Policy

Create the object lifecycle policy for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Policies and find the Lifecycle policy rules section.
All lifecycle policy rules are displayed in a table.
- Select Create rule .
The Create lifecycle rule panel opens.

The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you have the required policies in place, create the lifecycle policy rule.
- Enter the following information:

- Name : Enter a name or accept the default system name. The system generates a rule name that reflects the current year, month, day, and time, for example, lifecycle-rule-20190321-1559 . If you change this name, use letters, numbers, dashes, underscores, and periods.
- Target : Select the target to which the lifecycle rule applies:
- If object versioning is disabled, select Objects or Uncommitted multipart uploads .
- If object versioning is enabled or suspended, select Latest version of objects , Previous versions of objects , or Uncommitted multipart Uploads .
- Lifecycle action : Select one of the following actions:
- If the rule target is Objects , Latest version of objects , or Previous versions of objects , select Move to archive , Move to Infrequent Access, or Delete . If auto-tiering is enabled on the bucket, Move to infrequent access isn't available for selection.
- If the rule target is Uncommitted multipart uploads , Delete is the only option and is selected by default.
- Number of days : Enter the number of days until the specified action is taken.

Note  
  
If the rule archives or deletes a previous object version, the "number of days" countdown is based on when the object version transitioned from being the latest object version to being a previous object version. You can determine this time by looking at the "last modified" time of the previous most recent version of the object.
- Use the State switch to specify whether the rule is enabled or disabled after it's created.
- If the rule target is Objects , Latest version of objects , or Previous versions of objects , you can optionally add one or more object name filters to specify which objects the lifecycle rule applies to. You can select objects or object versions by using[pattern matching](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#PatternsOLM). If no object name filters are specified, the rule applies to all objects in the bucket.
To create an object name filter:
- Select Add filter .
- Select the Filter type .
- Enter the Filter value .
- Select Create rule .

Tip  
  
From the Actions menu for the lifecycle policy rule you want, select Enable or Disable to enable or disable the rule.
The rule appears in the Lifecycle policy rules list.
- 

Use the[oci os object-lifecycle-policy put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/put.html)command and required parameters to create the object lifecycle policy for a bucket:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Specifying the Lifecycle Policy Rules

Use the`items`parameter to specify the bucket's set of lifecycle policy rules:
```

```

The`items`parameter requires that you provide key-value pair input as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.
The`items`key-value pair input must specify the following:
```

```

Specify one of the following values for`action`:

Value Description
`ARCHIVE`Specify this action to move objects, object versions, or previous object versions to the[Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)tier.
`INFREQUENT_ACCESS`Specify this action to move objects, object versions, or previous object versions to the[Infrequent Access](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access)tier. If Auto-Tiering is enabled on the bucket, you can't specify`INFREQUENT_ACCESS`.
`DELETE`Specify this action to delete objects, object versions, or object versions.
`ABORT`Use this action to delete failed or incomplete multipart uploads.
Specify one of the following values for`target`:

Value Description
`objects`Use this action to move objects, object versions, or previous object versions to the[Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)tier.
`object-versions`Use this action to move objects, object versions, or previous object versions to the[Infrequent Access](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access)tier.
`multipart-uploads`Use this action to delete objects, object versions, or previous object versions.

Specify`timeUnit`in days.

The following example creates or replaces a lifecycle policy that includes a rule for moving previous object versions with names that include the pattern`*.doc`from the Standard tier to the Archive tier after 60 days. The policy also includes a rule that deletes previous object versions after 180 days.

```

```

The following example creates or replaces a lifecycle policy that includes a rule for moving all objects from the Standard tier to the Infrequent Access tier after 45 days. The policy also includes a rule that moves all objects to the Archive tier after 90 days.

```

```

The following example creates or replaces a lifecycle policy rule that deletes previous object versions from the Archive tier after 240 days.
```

```

The following example creates or replaces a lifecycle policy rule that deletes all uncommitted or failed multipart uploads after 5 days:
```

```

Instead of using the`items`option, you can pass the JSON key-value pairs in a file. For example:

```

```

### Using Windows

On Windows, to pass complex input to the CLI as a JSON string, you must enclose the entire block in double quotes. Inside the block, each double quote for the key and value strings must be escaped with a backslash (\) character.

For example:

```

```

- 

Run the[PutObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/PutObjectLifecyclePolicy)
