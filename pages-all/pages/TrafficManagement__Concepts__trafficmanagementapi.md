# Traffic Management Steering Policies API Guide
- Source: https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm
- Fetched: 2026-09-05 03:07 CDT

# Traffic Management Steering Policies API Guide

Use the Oracle Cloud Infrastructure DNS REST API to build and configure Traffic Management policies.

Use the following guide to learn how policies are constructed using the[DNS REST API](https://docs.oracle.com/iaas/api/#/en/dns/latest/).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Traffic Management Steering Policy Components

The following list describes the components used to build a Traffic Management Steering Policy. STEERING POLICIES An overall framework to define the traffic management behavior for zones. Steering policies contain rules that help to intelligently serve DNS answers. ATTACHMENTS Allows you to link a steering policy to zones. An attachment of a steering policy to a zone occludes all records at its domain that are of a covered record type, constructing DNS responses from its steering policy rather than from those domain's records. A domain can have at most one attachment covering any particular record type. RULES The guidelines steering policies use to filter answers based on the properties of a DNS request, such as the requests geolocation or the health of endpoints. ANSWERS Answers contain the DNS record data and metadata to be processed in a steering policy. TEMPLATES Templates are predefined rule sequences that create a policy type and its intended behavior. Example: The`FAILOVER`template serves answers by checking DNS query against a`FILTER`rule first, then the following rules in succession:`HEALTH`,`PRIORITY`, and`LIMIT`. This gives the domain dynamic failover capability. Policies that define the`template`field with any policy other than`CUSTOM`, must follow the rule sequence outlined for that policy type, otherwise, a`400`status code error is returned upon policy creation. CASES A rule can optionally include a sequence of cases defining alternate configurations for how it behaves during processing for any particular DNS query. When a rule has no sequence of cases, it's always evaluated with the same configuration during processing. When a rule has an empty sequence of cases, it's always ignored during processing. When a rule has a non-empty sequence of cases, its behavior during processing is configured by the first matching case in the sequence. A rule case with no`caseCondition`always matches. A rule case with a`caseCondition`matches only when that expression evaluates to true for the specific query.

## Create Steering Policies Using Templates

The following section explains the rule configuration for each type of steering policy template followed by an example POST request ([CreateSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/CreateSteeringPolicy)) displaying how to configure each template.

### FAILOVER

User failover policies to prioritize the order in which answers are served in a policy (for example, Primary and Secondary). Oracle Cloud Infrastructure Health Checks monitors and on-demand probes are leveraged to evaluate the health of answers in the policy. If the Primary Answer is found to be unhealthy, DNS traffic is automatically steered to the Secondary Answer. Each of the following rules must be defined in the order specified in the`rules`field of the request body when using a`FAILOVER`template:

Order Rule Restrictions Comments
`1``FILTER`
- No cases are allowed.
- 

Answer data must be defined in`defaultAnswerData`using the following JSON:
```

```

`2``HEALTH`
- No cases are allowed. Only included if`healthCheckMonitorId`is defined for the policy.
`3``PRIORITY`
- No cases are allowed.
- Answer data must be defined in the`defaultAnswerData`property for the rule.
- 

Every answer must have a pool property.
- `defaultAnswerData`restrictions:
- Answers can't be referenced by their name property in`answerCondition`expressions, they must be referenced by their pool property.
- Every answer pool must be referenced once and only once.
- Every answer pool must have a unique value property.
- Each answer pool reference must match the pool property on one or more answers defined in the answer list for the policy.
`4``LIMIT`
- No cases are allowed.

Example of a`POST /steeringPolicies`policy using the`FAILOVER`template:

```

```

### LOAD_BALANCE

Load Balancer policies distribute traffic across many endpoints. You can assign equal weights to endpoints to distribute traffic evenly across the endpoints or you can assign custom weights for ratio load balancing. Oracle Cloud Infrastructure Health Checks monitors and on-demand probes are leveraged to evaluate the health of the endpoint. DNS traffic is be automatically distributed to the other endpoints, if an endpoint is found to be unhealthy. Each of the following rules must be defined in the order specified in the`rules`field of the request body when using a`LOAD_BALANCE`template:

Order Rule Restrictions Comments
`1``FILTER`
- No cases are allowed.
- 

Answer data must be defined in`defaultAnswerData`using the following JSON:
```

```

`2``HEALTH`
- No cases are allowed. Only included if`healthCheckMonitorId`is defined for the policy.
`3``WEIGHTED`
- No cases are allowed.
- Answer data must be defined in the defaultAnswerData property for the rule.
- Answers can't be referenced by their pool property in answerCondition expressions, they must be referenced by their name property.
`4``LIMIT`
- No cases are allowed.

Example of a`POST /steeringPolicies`policy using the`LOAD_BALANCE`template:

```

```

### ROUTE_BY_GEO

Geolocation-based steering policies distribute DNS traffic to different endpoints based on the location of the end user. Customers can define geographic regions composed of originating continent, countries or states/provinces (North America) and define a separate endpoint or set of endpoints for each region. Each of the following rules must be defined in the order specified in the`rules`field of the request body when using a`ROUTE_BY_GEO`template:

Order Rule Restrictions Comments
`1``FILTER`
- No cases are allowed.
- 

Answer data must be defined in`defaultAnswerData`using the following JSON:
```

```

`2``HEALTH`
- No cases are allowed. Only included if`healthCheckMonitorId`is defined for the policy.
`3``PRIORITY`
- The`defaultAnswerData`property can't be used on this rule.
- At least one case must be defined. If there are many cases, the final case can provide a "catch-all" case.
- The`caseCondition`property on cases can only use`query.client.geoKey`in the conditional expression.
- Answers can't be referenced by their name property in`answerCondition`expressions, they must be referenced by their pool property.
- Every answer must have a pool property.
- 

For each case's`answerData`:
- Every answer pool must be referenced once and only once.
- Every answer pool must have a unique value property (within the case).
- Each answer pool reference must match the pool property on one or more answers defined in the answer list for the policy.
`4``LIMIT`
- No cases are allowed.

Example of a`POST /steeringPolicies`request body using the`ROUTE_BY_GEO`template:

```

```

### ROUTE_BY_ASN

ASN-based steering policies enable you to steer DNS traffic based on Autonomous System Numbers (ASN). DNS queries originating from a specific ASN or set of ASNs can be steered to a specified endpoint. Each of the following rules must be defined in the order specified in the`rules`field of the request body when using a`ROUTE_BY_ASN`template:

Order Rule Restrictions Comments
`1``FILTER`
- No cases are allowed.
- 

Answer data must be defined in`defaultAnswerData`using the following JSON:
```

```

`2``HEALTH`
- No cases are allowed. Only included if`healthCheckMonitorId`is defined for the policy.
`3``PRIORITY`
- The defaultAnswerData property can't be used on this rule.
- At least one case must be defined. If there are many cases, the final case can provide a "catch-all" case.
- The caseCondition property on cases can only use query.client.asn in the conditional expression.
- Answers can't be referenced by their name property in answerCondition expressions, they must be referenced by their pool property.
- Every answer must have a pool property.
- 

For each case's answerData:
- Every answer pool must be referenced once and only once.
- Every answer pool must have a unique value property (within the case).
- Each answer pool reference must match the pool property on one or more answers defined in the answer list for the policy.
`4``LIMIT`
- No cases are allowed.

Example of a`POST /steeringPolicies`request body using the`ROUTE_BY_ASN`template:

```

```

### ROUTE_BY_IP

IP Prefix-based steering policies enable customers to steer DNS traffic based on the IP Prefix of the originating query. Each of the following rules must be defined in the order specified in the`rules`field of the request body when using a`ROUTE_BY_IP`template:

Order Rule Restrictions Comments
`1``FILTER`
- No cases are allowed.
- 

Answer data must be defined in`defaultAnswerData`using the following JSON:
```

```

`2``HEALTH`
- No cases are allowed. Only included if`healthCheckMonitorId`is defined for the policy.
`3``PRIORITY`
- The`defaultAnswerData`property can't be used on this rule.
- At least one case must be defined. If there are many cases, the final case can provide a "catch-all" case.
- The`caseCondition`property on cases can only use query.client.address in the conditional expression.
- Answers can't be referenced by their name property in`answerCondition`expressions, they must be referenced by their pool property.
- Every answer must have a pool property.
- 

For each case's`answerData`:
- Every answer pool must be referenced once and only once.
- Every answer pool must have a unique value property (within the case).
- Each answer pool reference must match the pool property on one or more answers defined in the answer list for the policy.
`4``LIMIT`
- No cases are allowed.

Example of a`POST /steeringPolicies`request body using the`ROUTE_BY_IP`template:

```

```

### CUSTOM

Use custom policies to create complex policies combining the capabilities of failover, load balancing, geolocation, ASN and IP prefix steering. Custom templates to not require a regimented sequence of rules and we recommend that you contact Oracle Cloud Infrastructure support before creating a custom policy.

## Rule Types
FILTER Uses boolean data associated with answers, keeping answers only if the rule's`shouldKeep`value is`true`. HEALTH Uses OCI Health Checks monitors and on-demand probes to evaluate the health of endpoints and add and remove answers from the policy as needed. A health check monitor must be referenced in a health rule to affect the policy. For more information about Health Checks, see[Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/Concepts/healthchecks.htm)
