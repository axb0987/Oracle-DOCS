# Deleting a Network Perimeter
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/remove-network-perimeters.htm
- Fetched: 2026-09-05 02:25 CDT

# Deleting a Network Perimeter

Delete one or more network perimeters in an identity domain in IAM.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../domains/to-view-identity-domains.htm).
- Select Security and then Network perimeters .

A list of existing network perimeters is displayed.
- From the Actions menu (three dots) of the network perimeter that you want to update, select Delete network perimeter .
You can't delete Oracle-managed (seeded) perimeters.
- Confirm the deletion when prompted.

Note  
  

If you receive an error stating that you can't delete the Network Perimeter because it's referenced by one or more Sign-On Policies, you must edit each referenced Sign-On Policy and remove the Network Perimeter from its conditions or rules. Save the updated policy, then try deleting the Network Perimeter again. For more information about removing a Network Perimeter from conditions or rules, see[Updating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../signonpolicies/modify-sign-policy.htm)
