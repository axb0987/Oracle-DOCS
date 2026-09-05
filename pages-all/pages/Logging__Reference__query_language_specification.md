# Logging Query Language Specification
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm
- Fetched: 2026-09-05 02:37 CDT

# Logging Query Language Specification

Use query syntax components with Advanced mode custom searches on the Logging Search page.

Also see[Advanced Search Queries](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Concepts/searchinglogs.htm#advanced_search_queries)and[saved searches](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Task/log-saved-search-management.htm)for more information.

## Query Components

The logging query language processing is based on a data flow model. Each query can reference one or more logs, and produces a table dataset as a result. The query language provides several operators for searching, filtering, and aggregating structured and unstructured logs.

A logging query includes the following components:
- [Log streams](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__logging_query_logstreams)
- [Fields](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__logging_query_fields)
- [Data types](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__logging_query_datatypes)
- [Stream expressions](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__stream_expressions)
- [Pipe expressions](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__pipe_expressions)
- [Operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__operators)

## Log Streams
To begin your search, you must first define the set of logs you want to search. You can choose to search specific log objects, log groups, or compartments. You can mix and match as many logs as you need. The search scope is defined using the following pattern:
```

```

The query language fetches log entries from the scope you provide, and constructs a log stream that you can filter, aggregate, and visualize.

Log stream:
```

```

Examples:
```

```

```

```

```

```

```

```

## Fields
All fields in log streams are case-sensitive. Although actual logs have indexed fields in lower case only, you can also create new fields in the query with mixed case:
```

```

Fields are in JSON notation, therefore, special characters must be in quotes.
```

```

For[Identifier](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__identifiers):
```

```

Examples:
- type
- data.message
- data.request.URL
- "type"
- "data"."message"
- "data.message" (not the same as "data"."message")
- data."$event"
- data."first name"
- data."an example of escaped ("") double quotes"

## Data Types

The following key data types are supported by the query language. These are (long and double) 8 bytes.

For details about the representation of the values of the corresponding types, see[Literals](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__section_logging_query_literals).
- Strings
- Numbers (integer, float-point)
- Arrays
- Booleans
- Timestamps
- Intervals

## Stream Expressions

All expressions which produce a stream are stream expressions. Stream expressions can be formed using the following operators:
- [Tabular operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__tabular_operators)
- [Aggregate operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__aggregate_operators)

## Pipe Expressions

A pipe (|) applies an operator on the left side to a stream expression on the right side. The pipe expression is a stream expression.

The operator on the right side of a pipe must consume only one stream (for example, aggregate operations, filters).
The left side becomes the "current stream" for the right side expression, making all fields in the current stream available according to short names. For example:
```

```

## Operators
The following are supported when performing advanced queries:
- [Tabular operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__tabular_operators)
- [Scalar operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__scalar_operators)
- [Aggregate operators](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__aggregate_operators)

## Tabular Operators

A tabular operator creates or modifies a log stream by filtering out or changing log entries. Also refer to BNF syntax notation. The following are tabular operators:
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_search)search`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_where)where`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_top)top`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_sort)sort`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_dedup)dedup`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_select)select`
- `[](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__taboperator_extend)extend`
`search`
Constructs a log stream from actual log objects. Also see[Log Streams](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__logging_query_logstreams)for details, and[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/../Task/using_the_cli_logsearch.htm)for additional examples.
```

```

`where`

Filters the current log stream using a Boolean expression.
```

```

`where`is optional:
```

```

Some example comparisons with numbers and Boolean field comparisons are the following:
```

```

```

```

You can perform a full text search by specifying a filter on the entire content of the log. A search on`logContent`returns any log line where a value matches your string. This functionality supports wildcards. For example:
```

```

```

```

`top`
Fetches only a specified number of rows from the current log stream, sorted based on some expression.
```

```

Examples:
- `top 3 by datetime`
- `top 3 by *`
- `top 3 by (a + b)`

A number of rows must be a constant positive integer, and a sorting expression must be provided.
```

```

`sort`

Sorts the current log stream by the specified columns, in either ascending (default) or descending order. The operator uses the "DESC" and "ASC" keywords to specify the type of the order. The default sort order is`asc`.
```

```

Example:
```

```

More than one column can be used to specify the order:
```

```

`dedup`

Processes the current log stream by filtering out all duplicates by specified columns. If more than one column is specified, all columns have to be delimited by commas.
```

```

Examples:
```

```

```

```

`select`

Applies a series of named scalar expressions to the current log stream. See[`summarize`](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/query_language_specification.htm#query_language_specification__operator_summarize)for an aggregation version of`select`.
```

```

Example:
```

```

`extend`

Extends the current log stream with a computed column.
```

```

Example:
```

```

## Scalar Operators

Scalar operators are applicable to individual values.

Arithmetic operations are the following:
- `+`
- `-`
- `*`
- `/`

Boolean operators are the following:
- `and`
- `or`

Unary operator:
- `-(<expr>)`

Comparison operators are the following (numeric expressions only):
- `<expr> > <expr>`
- `<expr> >= <expr>`
- `<expr> <= <expr>`
- `<expr> < <expr>`
- `<expr> = <expr>`
- `<expr> != <expr>`

String comparison:
- `<expr> = <expr>`

Functions:
- `not (<expr>)`
- `contains_ci/contains_cs (<expr>, <expr>, (true | false))`

The last parameter is case-sensitive.
- `rounddown (<expr>, '[0-9]+(d | h | m | s)')`

The last parameter is the time interval in days, hours, minutes, or seconds.

`time_format(datetime, <format>)`

Format a time to a string
- `concat (<axpr>, <expr>)`
- `upper (<expr>)`
- `lower (<expr>)`
- `substr (<expr>, [0-9]+ (, [0-9]+)?)`

The second argument is the start index, while the third argument is optional, namely, how many characters to take.
- `isnull (<expr>)`
- `isnotnull (<expr>)`

## Aggregate Operators
`count`

Calculates a number of rows in the current log stream:
```

```

`summarize`

Groups the current log stream by the specified columns and time interval, and aggregates using named expressions. If grouping columns are not specified,`summarize`aggregates over the whole stream.
```

```

## Special Columns
`logContent`

`logContent`is a special column which represents the text of the whole original message. For example:
```

```

## Comments

Both single line and multi-line comments are supported, for example:
```

```

```

```

## Identifiers

Identifiers are the names of all available entities in the query. An identifier can reference a field in the current log stream, or a parameter defined in the beginning of the query. Identifiers have the following format:
```

```

For example:`level`,`app_severity`,`$level`.

The quoted form allows special symbols in the names (except double quotes):
```

```

For example:`"opc-request-id"`,`"-level"`.

All parameter references start with a dollar sign (`$`), for example:`$level`.

## Literals

Type Examples
string 'hello', 'world\'!'
wildcard pattern "acc-*"
integer -1, 0, +200
float 1.2, 0.0001, 1.2e10
array [1,2,3,4], []
interval 3h, 2m
nullable null

## Functions

Scalar functions are the following:
- `isnull(expr1)`
- `concat(expr1, ...)`

Aggregate functions are the following:
- `sum(expr1)`
- `avg(expr1)`
- `min(expr1)`
- `max(expr1)`
- `count()`: Counts a number of rows.
- `count(expr)`: Counts a number of non-null`expr`values.
- `first(expr1)`
- `last(expr1)`

## System parameters

All parameters with the`prefex`"query." are reserved. The following parameters are supported:

Name Type Example Description
`query.from`String with date time in ISO 8601 format. '2007-04-05T14:30' Specifies starting time of the query window.
`query.to`
