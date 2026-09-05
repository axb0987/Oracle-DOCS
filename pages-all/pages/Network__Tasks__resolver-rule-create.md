# Creating a Resolver Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-rule-create.htm
- Fetched: 2026-09-05 02:47 CDT

# Creating a Resolver Rule

You can create a resolver rule that's used to answer queries that aren't answered by a resolver's views.

Note  
  
Endpoints are used in the rule, and they must exist before you create a resolver rule.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)and[Resolver Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-resolver_endpoints.htm)for more information about resolvers and endpoints in the VCN.

## Using the Console

- From the Private Resolver Details screen, select Rules in the Resources column. Select Manage Rules . The Manage Rules screen appears.
- You can have up to 50 rules per resolver. For each rule, select:

- Rule condition: Sets whether routing decisions are made based on the query's originating CIDR Block or Domain (up to 10 hostnames), or neither (Select None to match any CIDR Block or Domain).
- Client CIDR blocks or Domains: Up to 10 CIDR blocks or domains.
- Rule action: This field is read-only. Forward is the only option.
- Source endpoint: The private endpoint used to forward queries when the rule condition is met.
- Destination IP address: The address to forward the query to if the rule condition is met.
- Select +Additional Rule to create another rule.
-
