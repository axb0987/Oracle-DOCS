# Sample Queries
- Source: https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/samplequeries.htm
- Fetched: 2026-09-05 03:03 CDT

# Sample Queries

This topic provides an explanation of sample queries, including what results to expect from a particular sample query. For more information about the syntax for constructing a query, see[Search Language Syntax](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm).
Note  
  

Example Values

Sample queries show example values for resource attributes. Replace those examples with values from the tenancy that you're using.

Search provides the following sample queries in the Console:
- Query for everything
- 

Query for everything, sorted by time created
- 

Query for volumes and users
- 

Query for volumes and users, sorted by time created
- 

Query for volumes and users that have any indexed field matching "production," sorted by time created
- 

Query for all resources that have a specific freeform tag
- 

Query for all resources that have one of two specific defined tags
- 

Query for instances in a "Running" state
- 

Query for instances in either a "Terminated" or "Terminating" state
- 

Query for all resources in a specific compartment
- 

Query for all instances due for a maintenance reboot
- 

Query for all resources that are Always Free

## Query All Resources

Query name: Query for everything

Expected results: Returns all supported resources in the tenancy across all compartments. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Resources, Sort by Time Created

Query name: Query for everything, sorted by timeCreated

Expected results: Returns all supported resources in the tenancy across all compartments, listed in order of time created, from newest to oldest.

Sample query language:

```

```

## Query Volumes and Users

Query name: Query for volumes and users

Expected results: Returns all block volumes and users in the tenancy. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Volumes and Users, Sort by Time Created

Query name: Query for volumes and users, sorted by timeCreated

Expected results: Returns all block volumes and users in the tenancy, listed in order of time created, from newest to oldest

Sample query language:

```

```

## Query Volumes and Users Matching "Production," Sorted by Time Created

Query name: Query for volumes and users, with anything matching production, sorted by timeCreated

Expected results: Returns all block volumes and users in the tenancy that have any indexed fields that exactly or partially match the search string "production", irrespective of casing. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Resources With Specific Freeform Tags

Query name: Query for all resources that have specific freeform tags

Expected results: Returns all resources in the tenancy that have a freeform tag of "costcenter" with a value of "1234."

Sample query language:

```

```

## Query All Resources According to Defined Tags

Query name: Query for all resources that have one of two specific defined tags

Expected results: Returns all resources in the tenancy that have either a tag with the key "region" and value "phx" in the tag namespace "categorization," or all resources in the tenancy that have a tag with the key "region" and value "iad" in the namespace "categorization." Ignores casing for all keys and values.

Sample query language:

```

```

## Query Instances According to Specific Lifecycle State

Query name: Query for running instances

Expected results: Returns all instances in the tenancy in a "Running" state. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query Instances According to One of Two Lifecycle States

Query name: Query for terminated or terminating instances

Expected results: Returns all instances in the tenancy in either a "Terminated" or "Terminating" state. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Resources According to Compartment ID

Query name: Query for all resources in a compartment

Expected results: Returns all resources in the tenancy with a specific compartment ID. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Instances Due for Maintenance Reboot

Query name: Query for all instances which have an upcoming scheduled maintenance reboot

Expected results: Returns all instances in the tenancy with a scheduled maintenance reboot time value of "now." Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```

## Query All Always Free Resources

Query name: Query for all resources that are Always Free

Expected results: Returns all existing resources in the tenancy that are free of charge for the life of the account. Lists results, by default, in order of time created, from newest to oldest.

Sample query language:

```

```
