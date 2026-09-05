# Resolver Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm
- Fetched: 2026-09-05 02:41 CDT

# Resolver Rules

Rules are used to answer queries that aren't answered by a resolver's views. They're checked in order, and each can optionally have conditions that limit which queries they apply to.
When a rule condition is matched, it results in the forwarding action and no later rule is evaluated.
Important  
  
Forwarding redundancy isn't achieved using duplicate forwarding rules, because only the first matching rule is used. Instead, consider creating a network Load Balancer (NLB) with redundant backends, and use the NLB IP address with a single forwarding rule.

Queries not matched by any view or rule are resolved from internet DNS. You can have up to 50 rules per resolver.
Note  
  
Endpoints are used in the rule, and they must exist before you create a resolver rule.

The most common application is to have one or more rules that follow this general form:
```

```

Followed by a final rule that follows this form:
```

```

So if the query is looking for example.com, the resolver internally forwards it to`X.X.X.X`through the specified forwarding endpoint and responds with the answer it receives. For any other query, it forwards to`Y.Y.Y.Y`through the same forwarding endpoint and responds with that answer it gets from`Y.Y.Y.Y`.

## Resolver Rule Tasks

- [Creating a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-rule-create.htm)
- [Editing a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-rule-edit.htm)
- [Removing a Resolver Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-rule-remove.htm)
