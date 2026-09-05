# Policy Statements Limit per Compartment Hierarchy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/policy-limits-compartment-hierarchy.htm
- Fetched: 2026-09-05 02:26 CDT

# Policy Statements Limit per Compartment Hierarchy

Oracle Cloud Infrastructure enforces a limit on the number of policy statements that can exist along a single compartment path, from the root compartment down to any leaf compartment.

The maximum number of policy statements allowed from the root compartment to any leaf compartment is 500. This limit includes all policy statements defined at every level of the compartment hierarchy along that path.
For example, if a tenancy has a compartment hierarchy such as:
- Root
- Compartment A
- Compartment B
- Compartment C then the total number of policy statements across all four compartments (Root, Compartment A, Compartment B and Compartment C) must not exceed 500.
However, if a tenancy has peer compartments such as:
- Root
- Compartment A
- Compartment B
- Compartment C then Root + Compartment A must not exceed 500, Root + Compartment B must not exceed 500, and Root + Compartment C must not exceed 500. The total statements across all compartments don't impact this limit.
Note  
  

The limit of 500 policy statements per compartment hierarchy is a hard limit that can't be increased. To avoid breaching policy limits, we recommend using Tag-Based Access Control (TBAC), which allows you to write one policy for many scenarios with a single statement. To learn more about TBAC, see[Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm)
