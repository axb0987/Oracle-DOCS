# Creating a Load Balancer Routing Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm
- Fetched: 2026-09-05 01:40 CDT

# Creating a Load Balancer Routing Policy

Create a routing policy to guide a load balancer's routing behavior.

For prerequisite information, see[Routing Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/routing-policy_management.htm).
Note  
  

To use a routing policy, you must create a listener that uses the policy. See[Creating a Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Policies and find the Routing policies section.
- Select Create routing policy .
- Enter a Name for the routing policy rule set. A name is required. The name must be unique, and can't be changed. The name can't begin with a period and can't contain any of these characters: ; ? # / % \ ] [ . The name must start with an lower- or upper- case letter or an underscore, and the rest of the name can contain numbers, underscores, and upper- or lowercase letters.
- To create a rule in the rule set:

- Select If all match (peer conditions use a logical AND) or If any match (peer conditions use a logical OR). In rules with several conditions, this selection guides whether one or all stated conditions produce an action. There can be up to five rule conditions, and you can have up to five nested conditions within a top-level condition. There can be up to 200 conditions total in a policy. Nested conditions can't have further conditions nested within them.
- Each top-level condition has a type, a match style, and a final criteria.
- Condition type : The setting can be Path , Request cookies , Request header , URL query , or Nested match . The available fields for a condition change depending on the condition type.

A Nested match also has a Nested conditions match criteria for conditions nested within, allowing you to have a mix of AND and OR in a condition. Select +Another nested condition to add another nested condition within the group. You can only nest conditions one level deep.
- The match style for Path can be: Is , Is not , Starts with , Does not start with , Ends with , or Does not end with .

The match style for Request header , Request cookies , and URL Query can be: Contains , Does not contain , Exists , or Does not exist .
- The final criteria depends on the Condition type selected, and can be a URL string (All Path conditions use this) a Key : Value pair or just a Key .
- Select the Action . If you select Route to backend set , select the destination backend set from the list of available sets.
- To create another rule, select + Another rule . You can also select Show advanced controls . An editing window opens where you can directly enter text to define rules using the[Routing Policy Language for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Concepts/routing_policy_conditions.htm).
- Select Next after you finish defining the rules. The next step is to confirm the order of the rules.
- Select next to the rule to display a summary of the conditions and actions set in a rule.
- Select Reorder to move a rule up or down in the policy order. Select from among Move to top , Move to bottom , Move up , or Move down . The last two options shift that rule up or down by one position in the order.
- Select Create routing policy .
- 

Use the[oci lb routing-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/routing-policy/create.html)command and required parameters to create a routing policy for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateRoutingPolicy](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/RoutingPolicy/CreateRoutingPolicy)
