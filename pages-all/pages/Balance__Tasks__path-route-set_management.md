# Path Route Sets for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/path-route-set_management.htm
- Fetched: 2026-09-05 01:41 CDT

# Path Route Sets for Load Balancers

Use path route sets to apply a set of path routes to a load balancer.
Note  
  

The path route sets retirement date has been updated from March 24, 2022 to a future date. Oracle will provide new guidance on this retirement timeline 12 months before it takes effect.

We recommend that you use routing policies instead of path route sets when creating new routing configurations for your load balancer. See[Routing Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/routing-policy_management.htm)for more information.

A path route is a string that the load balancer matches against an incoming URI to decide the appropriate destination backend set. Some applications have multiple endpoints or content types, each distinguished by a unique URI path. For example,`/admin/`,`/data/`,`/video/`, or`/cgi/`. You can use path route rules to route traffic to the correct backend set without using several listeners or load balancers.

A path route set includes all path route rules that define the data routing for a particular listener.

Note the following about path route sets:
- You can't use asterisks in path route strings.
- You can't use regular expressions.
- Path route string matching is case-insensitive.
- You can specify up to 20 path route rules per path route set.
- You can have one path route set per listener. The maximum number of listeners limits the number of path route sets you can specify for a load balancer.
Note  
  
Browsers often add an ending slash to the path in a request. If you specify a path such as`/admin`, you might want to configure the path both with and without the trailing slash. For example,`/admin`and`/admin/`.

A path route rule consists of a path route string and a pattern match type.

Pattern match types include:
- EXACT_MATCH

Looks for a path string that exactly matches the incoming URI path.

Applies case-insensitive regex:
```

```

- FORCE_LONGEST_PREFIX_MATCH

Looks for the path string with the best, longest match of the beginning portion of the incoming URI path.

Applies case-insensitive regex:
```

```

- PREFIX_MATCH

Looks for a path string that matches the beginning portion of the incoming URI path.

Applies case-insensitive regex:
```

```

- SUFFIX_MATCH

Looks for a path string that matches the ending portion of the incoming URI path.

Applies case-insensitive regex:
```

```

Path route rules apply only to HTTP and HTTPS requests and have no effect on TCP requests.

For more information on creating and managing path route sets, see[Path Route Sets](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/path-route-set_management.htm).

To apply path route rules to a listener, you first create a path route set that contains the rules. The path route set becomes a part of the load balancer's configuration. You then specify the path route set to use when you create or update a listener for the load balancer. To remove a path route set from a listener,[edit the listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm#console)and select None as the Path Route Set option.

You can perform the following path route set management tasks:
- [List the path route sets for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/path-route-set_management.htm#top)
- [Create a new path route set for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest_topic-Creating_Path_Route_Sets.htm)
- [Get a path route set's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_path-route-set.htm)
- [Edit a path route set's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_path-route-set.htm)
- [Delete a path route set from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_path-route-set.htm)

## Rule Priority

The system applies the following priorities, based on match type, to the path route rules within a set:
- For one path route rule that specifies the EXACT_MATCH type, no cascade of priorities occurs. The listener looks for an exact match only.
- For two path route rules, one that specifies the EXACT_MATCH type and one that specifies any other match type, the exact match rule is evaluated first. If no match is found, then the system looks for the second match type.
- For multiple path route rules specifying various match types, the system applies the following priority cascade:
- EXACT_MATCH
- FORCE_LONGEST_PREFIX_MATCH
- PREFIX_MATCH or SUFFIX_MATCH
- The order of the rules within the path route set doesn't matter for EXACT_MATCH and FORCE_LONGEST_PREFIX_MATCH. The system applies the priority cascade no matter where these match types appear in the path route set.
- If matching cascades down to prefix or suffix matching, the order of the rules within the path route set DOES matter. The system chooses the first prefix or suffix rule that matches the incoming URI path.

See[Rule Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm)for more information on creating and managing rule sets.

To apply path route rules to a listener, you first create a path route set that contains the rules. The path route set becomes a part of the load balancer's configuration. You then specify the path route set to use when you create or update a listener for the load balancer. To remove a path route set from a listener,[edit the listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm#console)
