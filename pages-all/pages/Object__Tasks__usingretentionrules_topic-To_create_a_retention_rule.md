# Creating an Object Storage Data Retention Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm
- Fetched: 2026-09-05 02:52 CDT

# Creating an Object Storage Data Retention Rule

Create a retention rule for an Object Storage bucket.
Important  
  
Locking a retention rule is an irreversible operation. Not even a tenancy administrator or Oracle Support can delete a locked rule. A mandatory 14-day delay exists before a rule is locked. This delay lets you test, update, or delete the rule or the rule lock before the rule is permanently locked.

A rule is active at the time of creation. The lock only controls whether the rule itself can be changed. After a rule is locked, only increases in the duration are allowed. Object modification is prevented and the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.

We recommend you set up notices for yourself for 7 days and 3 days before the 14-day period ends to remove the rule if you're not sure about using it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Retention rules section.
- Select Create rule .
- Enter the following information:

- 

Name : Enter a name for the rule. The system generates a rule name that reflects the current year, month, day, and time, for example, retention-rule-20200229-1002 . If you change this name, use letters, numbers, dashes, underscores, and periods.
- 

Retention rule type : Select the retention rule type that you want to create:
- 

Time-bound rules have a user-defined duration. Object modification is prevented for the duration specified. Duration is applied to each object individually, and is based on the object's Last modified timestamp. Enter values for the Retention duration settings that appear.
- 

Indefinite rules have no duration or expiration. Object modification is prevented until an indefinite rule is deleted.
- 

Retention duration : (Time-bound type rules only) Enter values for the Retention time amount time amount and Retention time unit time unit in Days or Years .
- 

Enable retention rule lock : (optional) Select the checkbox to lock the rule. When a rule is locked, only an increase in the retention duration is allowed and the rule can only be deleted by deleting the bucket. A bucket must be empty to be deleted.
- Select Create rule .
The rule is displayed in the Retention rules list.
- 

Use the[oci os retention-rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/create.html)command and required parameters to create a retention rule for a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Giving the Retention Rule a Display Name

Include the`display-name`parameter to give a user-specified name for the retention rule. Names can be helpful in identifying retention rules. For example:
```

```

## Creating a Time-Bound Retention Rule

Include the`time-amount`and`time-unit`parameters to set a time period in days or years for how long the retention rule applies. For example:
```

```

If you don't specify a time amount and unit, there is no time limit and the objects in the bucket are preserved indefinitely.

## Locking the Retention Rule

Include the`time-rule-locked`parameter and a date timestamp after which this rule is locked and can only be deleted by deleting the bucket. For example:
```

```

See[oci os retention-rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/create.html)for the supported date timestamp formats you can use with this parameter.

After a rule is locked, only increases in the duration are allowed and no other properties can be changed. You can't update this property for rules that are in a locked state. Specifying it when a duration isn't specified is considered an error.
- 

Run the[CreateRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/CreateRetentionRule)
