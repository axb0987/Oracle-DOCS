# Routing Policies for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/routing-policy_management.htm
- Fetched: 2026-09-05 01:41 CDT

# Routing Policies for Load Balancers

Use routing policies to apply a named ordered list of routing rules to a load balancer's listener.

A routing policy is a named ordered list of routing rules that's applied to a listener. Request routing policies allow you to route ingress traffic requests based on whether they match certain conditions you define. These rule conditions can use Boolean and near-match operations. The rules are evaluated in the order you define and the evaluation stops at the first match. You can attach one such request routing rule set to your HTTP or HTTPS listeners. A well-formed request routing rule is made up of one or more match conditions and a single corresponding route action. You can create multiple routing rules. If an incoming request doesn't match any of the rules you created, the request is routed to a default backend set attached to the listener. See[Routing Policy Language](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Concepts/routing_policy_conditions.htm)for an explanation of the routing policy language.

You can perform the following routing policy management tasks:

[List the routing policies for the load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-routing-policy.htm)

[Create a new routing policy for the load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm)

[Get a routing policy's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_routing-policy.htm)

[Edit a routing policy's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_routing-policy.htm)

[Delete a routing policy's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_routing-policy.htm)

## Supported Match Types

For HTTP headers, query data parameters, and cookies, the following match types are supported:
- Contains : &lt;key&gt; equals &lt;value&gt;
- Does not contain : &lt;key&gt; equals &lt;value&gt;
- Exists : &lt;key&gt;
- Does not exist : &lt;key&gt;

Routing policies also support rules that match against request URL paths. This behavior is similar to path route sets, but offers different match options. The following match types are supported in routing policies for path matching:
- Is : An exact match of the path, such as /videos or /images .
- Is not : Any path that doesn't exactly match the specified path.
- Starts with : A match happens if the path begins with the input value. If the parameter provided was /videos , then a request for /videos/images would still produce a match.
- Does not start with : A match happens if the path begins with anything other than the parameter provided. If the parameter provided was /videos , then a request for /images/stills would still produce a match.
- Ends with : A match happens if the path ends with the parameter. If the parameter provided was /videos , then a request for both /images/videos or /previews/videos would both produce a match.
- Does not end with : A match happens if the path ends with anything other than the parameter provided. So if the parameter provided was /videos , then a request for /videos/images would produce a match.

The only supported routing rule action is:
