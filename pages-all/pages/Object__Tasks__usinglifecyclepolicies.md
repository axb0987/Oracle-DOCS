# Object Storage Object Lifecycle Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm
- Fetched: 2026-09-05 02:51 CDT

# Object Storage Object Lifecycle Management

Learn how to use Object Lifecycle Management to automatically manage the archiving and deletion of objects.

By using Object Lifecycle Management to manage your[Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/objectstorageoverview.htm)and[Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm)data, you can reduce your storage costs and the amount of time you spend manually managing data.

Object Lifecycle Management works by taking automated action based on rules that you define. These rules instruct Object Storage to delete uncommitted multipart uploads, move objects to a different storage tier, and delete supported resources on your behalf within a given bucket. A bucket's lifecycle rules are collectively known as an object lifecycle policy. The resources that Object Lifecycle Management supports include objects, object versions, and uncommitted or failed multipart uploads.

For example, you can define rules that automatically do the following:
- Move Standard-tier objects with a`.doc`extension to either the Infrequent Access or Archive tier 60 days after creation or last update.
- Move Standard-tier objects to the Archive tier 30 days after creation or last update, and then automatically delete those archived objects after 180 days.
- Move Standard-tier objects to the Infrequent Access tier 90 days after creation or last update.
- Delete any previous object versions 120 days after the object version transitions from the latest version to a previous version.
- Delete uncommitted or failed multipart uploads after 5 days.
- Delete all objects and object versions in a bucket in preparation for bucket deletion.

Each Object Storage or Archive Storage bucket can have a single lifecycle policy consisting of up to 1,000 rules. Object-related rules can have object name[pattern matching](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#PatternsOLM)conditions.

You can create, edit, delete, enable, and disable individual rules in the Console as needed. To update a lifecycle policy using the CLI or API, overwrite an existing policy with a new policy. Ensure that the new policy is inclusive of all the policy rules that you want to apply to the bucket.
Note  
  

Rules normally run within 10 minutes of being triggered. However, this is on a best-effort basis, and might take longer. Rules can be applied to all objects in most buckets within 24 hours, but it can take longer for very large buckets. In unusual circumstances the time could be much longer than expected, especially when a rule affects many objects at once. You continue to be billed for the tier the object is in, even after a rule has been triggered, but not yet processed.

When using Object Lifecycle Management to tier storage from Infrequent Access to Archive Storage, standard retrieval fees apply for Infrequent Access storage.

You can perform the following Object Lifecycle Management tasks:

[List the object lifecycle policies for the bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#top).

[Create the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm).

[View the details of the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm).

[Edit the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm).

[Delete or disable the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm).

## Required IAM Policies

Important  
  
You can't use Object Lifecycle Management until you authorize the Object Storage service to archive and delete objects on your behalf. See[Service Permissions](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#Service)for more information.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

### User Permissions

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators:
- The policy[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#object-storage-admins-manage-buckets-objects)lets the specified group do everything with buckets and objects, including adding and managing lifecycle policies.
- If you create more restrictive policies that grant individual permissions:
- OBJECT_VERSION_DELETE is required to delete previous object versions on your behalf using lifecycle policies.
- OBJECT_UPDATE_TIER is required to change the storage tier of an object.

For more information on Object Storage user permissions, see[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).

### Service Permissions

To execute object lifecycle policies, you must authorize the service to archive and delete objects on your behalf. To do so, create the following policy in the root compartment of your tenancy:

```

```

Because Object Storage is a regional service, you must authorize the Object Storage service in each region you use lifecycle policies. Object Storage ensures that your data isn't read from any unauthorized region.

If you don't have permissions to write policies for the root compartment of your tenancy, contact your Oracle Cloud Infrastructure administrator. To find the region identifier value of an Oracle Cloud Infrastructure region, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Instead of using the[policy verb](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-Verbs.htm)`manage`, you can grant individual permissions to the service. For example:

```

```

## Options

When creating object lifecycle policy rules, you have the following options:
- When a lifecycle rule is created, the system generates a default name for that rule, for example lifecycle-rule-20190321-1559 . This rule name identifies the current year, month, day, and time that the rule was created. You can use that system-generated name for your new rule or you can specify a different name for it.
- You can create lifecycle rules that do the following:
- Move or delete all objects in the bucket.
- Move or delete objects in the bucket that match the object name filters you specify. You can select objects using both object name prefixes and pattern matching. For details, see[Using Object Name Filters](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#namefilters).
- Delete uncommitted or failed multipart uploads. For more information, see[Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm).
If object versioning is enabled or suspended on a bucket, you can also create lifecycle rules that do the following:
- Move or delete the previous versions of all objects in the bucket.
- Move or delete the previous versions of objects in the bucket that match the name filters you specify. You can select objects using both object name prefixes and pattern matching. See[Using Object Name Filters](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#namefilters)for details. See[Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm)for more information.
- You specify the number of days until the specified action is taken.
- You decide whether a new rule is enabled or disabled upon creation.

## Using Object Name Filters

Use object name filters to specify a subset of objects, object versions, or previous object versions that a lifecycle rule applies to. Create a separate object name filter rule for each rule target (objects, object versions, or previous object versions).
Important  
  
Don't specify object name filters if you want a rule to apply to the all objects, all object versions, or all previous object versions target.

Two types of object name filters are supported:
- [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix)for details.
- [Pattern matching](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#PatternsOLM)matches on the entire object name, but supports using wildcard characters and other pattern matching constructs as needed to match zero or more characters within the object name.
Note  
  
Object name filters operate on the entire object name. Prefixes (displayed as virtual folders and subfolders in the Console) are part of the object name.

For example, for this path:`>marathon>participants>p_21.jpg`, the name of the object is`/marathon/participants/p_21.jpg`, not`p_21.jpg`.

You can add object name filters in any order. Object Lifecycle Management evaluates the precedence of the rules as follows:
- Pattern exclusions
- Pattern inclusions
- Prefix inclusions

### Using Prefix Matching to Filter Objects

You can use prefix strings for matching purposes when performing lifecycle management-related operations. Certain bulk operations can also be performed by matching on the prefix portions of the object name.
- In the following object name examples, prefixes include one or more forward slashes (/) to simulate a directory structure. The string`marathon/`or marathon / participants / can serve as a prefix for matching purposes in lifecycle rules:
```

```

- In the following object name examples, the string`gloves_27_`can serve as a prefix for matching purposes in lifecycle rules:
```

```

### Using Pattern Matching to Filter Objects

Object Storage supports the following pattern matching characters to either include or exclude objects:

Character Description Pattern Examples Matches Doesn't Match
* Matches 0 or more characters *.tmp

foo.tmp

foo/bar/baz.tmp

tmp

Atmp
temp/*.tmp

temp/working.tmp

temp/new/file.tmp

file.tmp

temp.tmp

temp/new.draft
*.xls

.xls

/home/user/file.xls

xls

.xl
/archive/*

/archive/sub/dir/

/archive/1/2/3/4/foo.txt

/src/archive/a

archive/b
? Matches any one character X?Z

XyZ

X_Z

XZ

XYYZ
\ Escapes the next character \\dir\\sub\\*

\dir\sub\ABC

\dir\sub\

dir\sub\abc

dirsub
[...]

Matches a group of characters, which can be:
- A set of characters, for example: [Zafg9@]. Matches any character in the brackets.
- A range of characters, for example: [a-f]. Matches any character in the range:
- 

[a-f] is equivalent to [abcdef].
- 

For character ranges only the CHARACTER-CHARACTER pattern is supported:
- [ab-yz] is not valid.
- [a-mn-z] is not valid.
- 

Character ranges cannot start with ^ or colon (:).
- 

To include a hyphen (-) in the range, make it the first or last character.

[-ab3]

-

a

b

3

-a

-ab

3b
backup.tar.gz.[0-9]

backup.tar.gz.0

backup.tar.gz.5

backup.tar.gz.9

backup.tar.gz10

backup.tar.gz
page-[0-9]*

page-0

page-2

page-22

page-2X

page-

page-A1
\[a-z\] [a-z]

a

z

[a-z

#### Object Name Filter Limitations

The following limits apply to object name filters:
- A maximum of 20 patterns is allowed under object name filters.
- Patterns are limited to 1024 characters. The following are examples of invalid patterns:
- \
- [^a-z]
- [z-a]
- 

[:isalpha:]

## Working with Object Lifecycle Management Policies

You can create, delete, edit, or disable lifecycle policy rules using the Console, the[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm), an SDK, or the API.

The Object Lifecycle Management delete policy operates based on the object's last modification time in UTC (Coordinated Universal Time), capturing either the creation time or the last overwrite time. The modification time is rounded up to the nearest day in UTC.

The platform runs the lifecycle policy once a day. When you configure or edit a lifecycle policy, it can take up to 24 hours for changes to go into effect and for the first execution to start. The time taken for policy actions to complete depends on the number of objects to be evaluated and operated on.
Caution  
  
Objects deleted on your behalf by lifecycle policies can't be recovered. Be sure when creating and editing your lifecycle policies that you're not unintentionally deleting data you want to retain. We recommend that you test your lifecycle policy on development data before using the policy in production.

## Listing Object Storage Object Lifecycle Policies

View a list of the object lifecycle policies for an Object Storage bucket.

### Using the Console

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Policies and find the Lifecycle policy rules section.
All lifecycle policy rules are displayed in a table.
- To view the object lifecycle policies in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

#### Filtering List Results

Use filters to limit the object lifecycle policies in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

#### Actions

In the list table, select the name of an object lifecycle policy to open its details page, where you can view its status and perform other tasks.

To perform an action on an object lifecycle policy directly from the list table, select an available option from the Actions menu in the row for that object lifecycle policy:
- Edit :[Edit the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm).
- Disable :[Disable the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm).
- Delete :[Delete the object lifecycle policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_enable_disable_or_delete_a_lifecycle_policy_rule.htm).
