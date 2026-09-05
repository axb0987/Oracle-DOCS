# Editing a Load Balancer Rule Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Editing_Rule_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Editing a Load Balancer Rule Set

Update a rule set for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Editing_Rule_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Editing_Rule_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Editing_Rule_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Policies and find the Rule sets section.
- From the Actions menu for the rule set, select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Rule Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm).
- Select Submit .
- 

Use the[oci lb rule-set get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/rule-set/get.html)command and required parameters to Update a rule set for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateRuleSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/RuleSet/UpdateRuleSet)
