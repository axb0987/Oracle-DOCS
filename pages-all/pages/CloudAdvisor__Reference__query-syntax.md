# Creating Cloud Advisor queries
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Reference/query-syntax.htm
- Fetched: 2026-09-05 01:47 CDT

# Creating Cloud Advisor queries

Review the basics of the query language for Cloud Advisor, including an explanation of syntax and rules so you can create your own queries.

Queries apply search conditions to a set of attributes and let you sort results. If you want to search across all supported resource types and resource attributes and do not need ordered search results, you do not need to add attributes ordering.

## Required IAM Permissions

The resources that you see in query results depend on the permissions you have in place for the resource type. You do not necessarily see results for every resource in the compartment or tenancy. For example, if your user account is not associated with a policy that grants you the ability to, at a minimum,`inspect`the`optimizer-resource-action`resource type, then you can’t query for Cloud Advisor resources. (The verb`inspect`lets you list and get resources.) Instead, Cloud Advisor shows no results for queries.

For more information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm). For information about the specific permissions required for the list API operation for your required resource type, see[Creating Cloud Advisor policies](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Reference/cloudadvisorpolicyreference.htm).

## Query Basics

The following examples show the basic syntax of a Cloud Advisor query:
```

```

Or:
```

```

Cloud Advisor ignores white space, indentation, and line breaks. Sample queries include indentation to improve readability. For the purposes of demonstrating syntax only, angle brackets (&lt;&gt;) and italicized text indicate variables, which can consist of one or more keywords.

In a query, clauses include the following:
- `query`- (Required) Selects which resources to return based on subsequent clauses. Query statements always begin with the word`query`.
- `where`- Matches resources to the specified`conditions`.
- `matching`- Matches resources to the specified text regardless of whether the text matches exactly, matches the resource type, or appears in an indexed resource attribute.
- `sorted by`- Orders resources according to`fieldName`in the order specified by`order`. If you do not include this clause, Cloud Advisor lists results by creation date in descending order, with the newest resources listed first.

Clauses are optional unless indicated otherwise. For matching purposes, you can use the`where`clause and the`matching`clause either separately or together.

### Conditions

The`where`clause applies`conditions`that filter the results returned by Cloud Advisor. You can specify one or more condition statements. For more information about multiple conditions, see[Grouping Conditions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Reference/query-syntax.htm#grouping).

In a query,`conditions`consist of the following:
```

```

The`fieldName`keyword is the resource attribute against which the`operation`and chosen`value`of that attribute are evaluated. Each field is associated with a field type. The field type tells you the expected format for any value in that field. What kind of`operation`you can use in a`conditions`statement depends on the field type.

In query`conditions`, an`operation`is a comparison operator that applies to the`value`in the statement. The`value`keyword refers to the value of the`fieldName`you specified. Cloud Advisor evaluates whether the specified attribute of the chosen resource type matches or does not match the`value`, according to the operation. In a query, you must enclose any string or date-time value in opening and closing straight single quotes (ˈ) or double quotes (").

The following table describes supported operations for resource queries:

Operation Description Supported Field Types Case Sensitive? Example
`=`

Equals, or exact matching for strings

String, integer, rational, Boolean, date-time

No If the`value`was ˈ backUp ˈ, it would match "backup", "BACKUP", "BackUp", "backUp", or any other variation in casing.
`!=`

Does not equal

String, integer, rational, Boolean, date-time

No If the`value`was ˈ backUp ˈ, it would match anything that does not equal "backUp", "backup", or any other variation in casing. It also would match anything that does not contain the characters 'backup' in that order.
`==`

Strictly equals

String

Yes If the`value`was ˈ backUp ˈ, it would only match "backUp" and no other variation in casing.
`!==`

Strictly does not equal

String

Yes If the`value`was ˈ backUp ˈ, it would match "backup", "BACKup", or anything except "backUp", with that exact casing.
`=~`

Contains

String

No If the`value`was ˈ backUp ˈ, it would match anything that equals "backup", "BACKUP", "BackUp", "backUp", or any other variation in casing, or contains those characters in that order, alongside other characters.
`>=`

Greater than or equal to

Integer, rational, date-time

Not applicable For a query where you have`size >= 5`as the condition, all results have a value of 5 or greater in the field named size .
`>`

Greater than

Integer, rational, date-time

Not applicable For a query where you have`size > 5`as the condition, all results have a value of greater than 5 in the field named size .
`<=`

Less than or equal to

Integer, rational, date-time

Not applicable For a query where you have`size <= 5`as the condition, all results have a value of 5 or less in the field named size .
`<`

Less than

Integer, rational, date-time

Not applicable For a query where you have`size < 5`as the condition, all results have a value of 5 or less in the field named size .

The following table lists some examples of resource attributes that belong to each category of supported field types. The field type tells you the expected format for a given field and the kind of`operation`you can pair it with in a`conditions`statement.

The table does not include every possible example for a given field type. If you want to know what format the Cloud Advisor service expects for a specific resource attribute, you can use the command line interface or API to find out more about resource attributes. You can also consult the API documentation. The API documentation includes a reference for each supported resource type that specifies attributes, their field types, and any restrictions.

Type Example Resource Attributes
String Display names, lifecycle states, availability domains, tags, CIDR blocks, and URLs
Integer Size or length of a resource
Rational Available data storage
Boolean Whether a feature is enabled or configured, whether a resource is healthy, whether a resource is public or private, whether something is the latest version, and whether something is allowed
Date-time Creation dates, last-updated dates, last-indexed dates, and scheduled maintenance reboots

### Grouping Conditions

By including more than one condition statement in a query, you can refine results according to multiple criteria. You can group multiple conditions by using either the logical operators`&&`(ampersands, to indicate a logical AND) or`||`(vertical bars, to indicate a logical OR). For example:
```

```

You can not combine two different logical operators in the same query unless you wrap parentheses around one group of predicates. Otherwise, multiple conditions can only use the same logical operator otherwise. For example:
```

```

In the preceding example, all results returned either have Compute as the value for resourceType, Active as the value for status, and us-region-1 as the value for regionName, or the value of their status field is anything other than Implemented.

The following group is also acceptable:
```

```

In the preceding example, all results returned have Implemented as the value for status and either Compute as the value for resourceType or anything that is not FAILED for lifecycleState.

Cloud Advisor does not perform left-to-right evaluation to reduce ambiguity or clarify intent.

### Date and Time Values

You can specify date and time values by using any of the following pattern string formats:

Format Examples Comments
`<yyyy> - <MM> - <dd> <HH> : <mm> : <ss> <TimeZone>`

'2018-06-19 16:15:41 PDT', '2018-06-19 16:15:41 -08:00'`TimeZone`is optional. If`TimeZone`is omitted, UTC is used.
`<EEE> , <d> <MMM> <yyyy> <HH> : <mm> : <ss> <TimeZone>`

'Tue, 19 Jun 2018 16:15:41 +0300', '19 June 2018 16:15:41'`EEE`is optional.`MMM`can also be expressed as`MMMM`.`TimeZone`is also optional. If`TimeZone`is omitted, UTC is used.
`<yyyy> - <MM> - <dd> T <HH> : <mm> : <ss> Z`

'2018-06-19T16:15:41Z'

Time in UTC. '`T`' and '`Z`' are case-sensitive.

You must observe spacing. Interpret dashes, colons, commas, and the characters 'T' and 'Z' literally. To interpret placeholder values in the preceding table, you can refer to the following pattern syntax:

Letter Date or Time Component Presentation
`y`

Year

Year
`M`

Month of the year

Month
`d`

Day of the month

Day
`H`Hour of the day (from 00-23) Number
`m`Minute of the hour Number
`s`Seconds of the minute Number
`E`Day of the week Text

Repeating pattern letters indicate their exact presentation. For example, 'HH' means you must use '00' and not '0' to represent midnight. Similarly, 'EEE' means 'Tue' and not 'Tuesday'. Likewise, 'MM' requires '09' instead of '9' to represent the month of September.

`TimeZone`is optional, but in your chosen format, you can specify`TimeZone`in any of the following ways:
- Name . You can specify a time zone by its name, such as GMT or PDT . Values are case-insensitive.
- GMT offset value . You can specify a time zone according to its GMT offset. For example, GMT-08:00 . Values are case-insensitive.
- ISO 8601 time zone . You can specify a time zone according to ISO 8601 standards. For example, -08 , -0800 , or -08:00 .

Instead of using one of the preceding formats, you can also specify a date-time value as the constant`now`. The constant`now`represents the current time to the level of granularity of seconds in a minute.

Lastly, you can add or subtract time intervals from any date-time values. For example, you can query for resources that were created within five minutes of a specific time. Search supports the following time intervals:

Letter Date or Time Component
`s`

Seconds
`m`

Minutes
`h`

Hours
`d`Days
`w`Weeks

To specify a time interval in relation to a date-time value, use one of the following formats:
- now - 3h
- 2018-06-19 16:15:41 PDT + 1h

### Sorting

The last clause of a resource query is the`sorted by`clause and is optional. The`sorted by`clause orders the results returned by Cloud Advisor based on the field name and lists them according to the`order`you specify. By default, if you do not specify sort order, results are always sorted by date-time created in descending order.

In the`sorted by`clause, you can specify the following:
- `fieldName`- The field that Cloud Advisor uses to sort results. You can specify any field of any resource. Resources that do not contain the field you specify are listed after the resources that do.
- `order`
