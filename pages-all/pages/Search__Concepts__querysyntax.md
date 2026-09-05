# Search Language Syntax
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm
- Fetched: 2026-09-05 03:03 CDT

# Search Language Syntax

This topic describes the basics of the query language for Search, including an explanation of syntax and rules so you can create your own queries. Queries apply search conditions to specific resource types and let you sort results. Query language gives you more nuanced and explicit control over search parameters, making it especially useful in cases where precise changes to a query might yield different results.

If you want to search across all supported resource types and resource attributes and don't need ordered search results, or if you prefer to use the Console interface to specify search parameters, you don't need to construct a query. Instead, you can search for a partial or exact match of free-form text without applying query language syntax to the search.

When you're ready to run a query, see[Querying Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/../Tasks/queryingresources.htm)for instructions.

## Query Basics

The following examples show the basic syntax of a query.

To query for resources that meet one or more conditions described by a condition statement that uses comparison operators:
```

```

To query for resources that meet one or more conditions and to include sorted resource attributes in the results:
```

```

Or, to query for resources that have any attribute with a value that matches what you specify:
```

```

Search ignores white space, indentation, and line breaks. Sample queries include indentation to improve readability. For the purposes of demonstrating syntax only, angle brackets (&lt;&gt;) and italicized text indicate variables, which can consist of one or more keywords.

In a query, clauses include the following:
- `query`- (Required) Selects which resources to return based on later clauses. Query statements always begin with the word`query`.
- `return`- Specifies which resource attributes to include in the expanded or enhanced view of search results. For more information, see[Return Attributes](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm#return).
- `where`- Matches resources to the specified`conditions`. For more information, see[Conditions](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm#conditions).
- `matching`- Matches resources to the specified text regardless of whether the text matches exactly, matches the resource type, or appears in an indexed resource attribute. For more information, see[Matching](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm#matching).
- `sorted by`- Orders resources according to`fieldName`in the order specified by`order`. Without this clause, Search lists results by creation date in descending order, with the newest resources listed first. For more information, see[Sorting](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm#sorting).

Clauses are optional unless indicated otherwise. For matching purposes, you can use the`where`clause and the`matching`clause either separately or together.

In the`query`clause, you specify the following information:
- `resourceType`- (Required) Specifies the resource type to which the next clauses apply when you run the query. You can specify either the resource type name (for example,`database`or`group`) or`all`. If you specify`all`, Search searches for matches to the specified`conditions`across all resource types. You can query for individual resource types, but not family types. For a list of supported resource types, see the[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm#resourcetypes)section of[Overview of Search](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm).
- `resources`- (Required) Specifies that the text you're submitting is a resource query.

## Return Attributes

For users of the SDK or CLI, the`return`clause indicates what extended resource attributes you want to see included with search results returned by the query. You can use the`return`clause to force the return of specific resource attributes or all resource attributes in search results, giving you more details about each resource.

By default, search results display a limited, common set of resource attributes for any matching resource. In the Console, these resource attributes include the display name, resource type, OCID, compartment, lifecycle state, and time created. In the SDK or CLI, basic resource search results also include the availability domain and any tags associated with the resource. When a query finds a match outside the common resource attributes, then expanded search results include and highlight the specific, matching attributes alongside the basic results. With the`return`clause, you can get more details about matching search results even if the query doesn't otherwise elicit a match in the resource attributes you want to see.

In a query, the`return`clause consists of the following:
```

```

The`fieldName`keyword identifies an attribute of a resource. For example, when the resource type targeted by the query is an instance, specifying`shape`indicates that you want to see the shape of all matching instances. (In the case of instances only, the`fieldName`can identify an attribute of a related resource, such as the private IP address on an instance's VNIC attachment. Specifying`attachedVnic.privateIp`indicates that you want to see the private IP address of the attachment between a VNIC and an instance.)

The additional details available for a particular resource depends on what resource attributes were indexed for the resource type. To find the names of all indexed resource attributes for a resource type, use the SDK or CLI to run a query that includes the`return`clause, but instead of specifying the field name, specify that you want to see`allAdditionalFields`. For example:
```

```

This query produces a response that shows all indexed resource attributes for the instance resource type. (The Console can't display these other fields, except for instance resources when you apply the resource type filter, which is why you must use the SDK or CLI to retrieve the information.) In search results, the available additional details (and the structure of that information) depends on the matching resource type. Furthermore, you must have the necessary permission to see the resource attributes that you requested to see with your query.
You can combine the`return`clause with the`where`clause to get results with specific details while also applying one or more conditions. For example:
```

```

This query produces a response that shows all indexed resource attributes for all instance resources that have an`assignedEntityType`field with a value of`PRIVATE_IP`.

### Restrictions

You can only use the`return`clause against one resource type at a time. The query can't specify multiple resource types if you include the`return`clause. If you want, though, you can specify more than one field to return for a particular resource type.

You can't include both the`allAdditionalFields`keyword and individual field names in the same query. You can either specify the`allAdditionalFields`keyword or you can specify or more individual field names, separated by commas.

## Conditions

The`where`clause applies`conditions`that filter the results returned by Search. You can specify one or more condition statements. For more information about multiple conditions, see[Grouping Conditions](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm#groupconditions).

In a query,`conditions`consist of the following:
```

```

The`fieldName`keyword is the resource attribute against which the`operation`and chosen`value`of that attribute are evaluated. Each field is associated with a field type. The field type tells you the expected format for any value in that field. What kind of`operation`you can use in a`conditions`statement depends on the field type.

### 

In query`conditions`, an`operation`is a comparison operator that applies to the`value`in the statement. The`value`keyword refers to the value of the`fieldName`you specified. Search evaluates whether the specified attribute of the chosen resource type matches or does not match the`value`, according to the operation. In a query, you must enclose any string or date-time value in opening and closing straight single quotes (ˈ) or double quotes (").

The following table describes supported operations for resource queries:

Operation Description Supported Field Types Case-sensitive? Example
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

The following table lists some examples of resource attributes that belong to each category of supported field types. (As previously described, the field type tells you the expected format for a given field and the kind of`operation`you can pair it with in a`conditions`statement.)

The table does not include every possible example for a given field type nor does it include examples from every resource-type. If you want to know what format the Search service expects for a specific resource attribute, you can use the command line interface or API to find out more about resource attributes. You can also consult the API documentation. The API documentation includes a reference for each supported resource type that specifies attributes, their field types, and any restrictions. For more information, see the[Supported Resources](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm#resourcetypes)section of[Overview of Search](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm).

Type Example Resource Attributes
String Display names, lifecycle states, availability domains, tags, CIDR blocks, and URLs
Integer Size or length of a resource
Rational Available data storage
Boolean Whether a feature is enabled or configured, whether a resource is healthy, whether a resource is public or private, whether something is the latest version, and whether something is allowed
Date-time Creation dates, last-updated dates, last-indexed dates, and scheduled maintenance reboots

## Grouping Conditions

By including more than one condition statement in a query, you can refine results according to several criteria. You can group conditions by using the logical operators`&&`(ampersands, to indicate a logical AND),`||`(vertical bars, to indicate a logical OR), or the logical IN operator. For example:
```

```

In the preceding example, all results have`LICENSE_INCLUDED`as the value in the field named`licenseModel`, a value greater than 40 for the field named`dataStoragePercentage`, and a value in the`lifecycleState`field that's anything other than`FAILED`.

You can't combine two different logical operators in the same query unless you wrap parentheses around one group of predicates. (Multiple conditions can only use the same logical operator otherwise.) For example:
```

```

In the preceding example, all results returned have either`LICENSE_INCLUDED`as the value in the field named`licenseModel`and a value greater than`40`for the field named`dataStoragePercentage`or the value of their`lifecycleState`field is anything other than`FAILED`.

The following group is also acceptable:
```

```

In the preceding example, all results returned have`LICENSE_INCLUDED`as the value in the field named`licenseModel`and either a value greater than`40`as the value for the field named`dataStoragePercentage`or anything that's not`FAILED`for the value of the field named`lifecycleState`.
To apply multiple conditions where each condition accepts more than one possible value, using a logical IN operator can simplify a query. For example, you can use the following conditions:
```

```

In the preceding example, all results returned have either`LICENSE_INCLUDED`or`BRING_YOUR_OWN_LICENSE`as the value in the field named`licenseModel`and a value of`OLTP`,`DW`,`AJD`, or`APEX`as the value in the field named`dbWorkload`. The preceding example can take the place of more complex query conditions, such as the following:
```

```

Or even the following:
```

```

Both of these examples use the logical OR operator to effectively express the same conditions in more verbose terms than the example that uses the logical IN operator instead.

Search doesn't perform left-to-right evaluation to reduce ambiguity or clarify intent.

## Date and Time Values

You can specify date and time values by using any of the following pattern string formats:

Format Examples Comments
`<yyyy> - <MM> - <dd> <HH> : <mm> : <ss> <TimeZone>`

'2018-06-19 16:15:41 PDT', '2018-06-19 16:15:41 -08:00'`TimeZone`is optional. If`TimeZone`is omitted, UTC is used.
`<EEE> , <d> <MMM> <yyyy> <HH> : <mm> : <ss> <TimeZone>`

'Tue, 19 Jun 2018 16:15:41 +0300', '19 June 2018 16:15:41'`EEE`is optional.`MMM`can also be expressed as`MMMM`.`TimeZone`is also optional. If`TimeZone`is omitted, UTC is used.
`<yyyy> - <MM> - <dd> T <HH> : <mm> : <ss> Z`

'2018-06-19T16:15:41Z'

Time in UTC. '`T`' and '`Z`' are case-sensitive.

You must observe spacing. Interpret dashes, colons, commas, and the characters 'T' and 'Z' literally. To interpret placeholder values in the preceding table, see the following pattern syntax:

Letter Date or Time Component Presentation
`y`

Year

Year
`M`

Month in year

Month
`d`

Day in month

Day
`H`Hour in day (from 00-23) Number
`m`Minute in hour Number
`s`Seconds in minute Number
`E`Day in week Text

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

## Matching

For matching purposes, instead of or in addition to using a`where`clause with`conditions`, you might want to use the`matching`clause. The`matching`clause obviates the need to specify`conditions`(that contain a field name, operation, and value). A`matching`clause effectively queries all indexed fields by applying the`=`(equals) operator along with the text you specify. However, it does so without requiring an exact match. For example, the following query uses a`matching`clause to behave the same way as a free text search:
```

```

The query produces results that match all resources and resource attributes that contain the word "instance".

The`matching`clause queries all indexed fields for matches, but ignores special characters, including any punctuation.

## Sorting

The last clause of a resource query is the`sorted by`clause and is optional. The`sorted by`clause orders the results returned by Search based on the field name and lists them according to the`order`you specify. By default, if you don't specify sort order, results are always sorted by date-time created in descending order.

In the`sorted by`clause, you can specify the following:
- `fieldName`- The field that Search uses to sort results. You can specify any field of any resource. Resources that don't contain the field you specify are listed after the resources that do.
- `order`- You can specify either asc or desc . Specifying asc lists results in ascending order. Specifying desc lists results in descending order.

## Querying Multiple Resource Types

You can query more than one resource types at a time by joining queries. Each query can have its own conditional clause. If the queries that you want to join have different "where" conditions, then the syntax is different from when you have queries for several resource types that share the same "where" condition.

The basic syntax for a query for multiple resource types is as follows:
```

```

For example:
```

```

The preceding example query returns all groups and all users in the tenancy.

The following shows the syntax for a query for several resource types with conditions, but where the conditions are the same for all resource types:
```

```

For example:
```

```

The preceding example query returns all groups with the display name "administrator" and all users with the display name "administrator," with any variation in casing.

If you need to apply differing conditions to any resource type, you must use a`union`keyword instead of comma separation between the joined queries. The following shows the syntax for a query for several resource types where some resource types share conditions while others don't:
```

```

For example:
```

```

The preceding example returns all groups with the display name "administrator" and all users with the display name "administrator," with any variation in casing, and all compartment resources.

Or, for example:
```

```

The preceding example returns all groups and all compartments. It also returns all users with the display name "administrator," with any variation in casing.

Optionally, you can add the`sorted by`
