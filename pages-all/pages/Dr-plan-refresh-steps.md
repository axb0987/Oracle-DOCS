# Understanding the DR Plan Refresh Process
- Source: https://docs.oracle.com/iaas/disaster-recovery/doc/Dr-plan-refresh-steps.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/disaster-recovery/doc/Dr-plan-refresh-steps.html#dcoc-content-body)

# Understanding the DR Plan Refresh Process

During a DR plan refresh, the plan is updated to add new groups and steps and remove the existing groups and steps to reflect updates made to the primary or standby DR protection group.

Full Stack DR performs the following steps to refresh the DR plan:
- If you add a new member to the DR protection group and a member of the same type already exists, the new steps for the newly added members will be added to existing plan groups. The existing plan groups to which the new steps were added will be labeled as Group Modified , and the new steps will be labeled as Step Added .
- If you add a new member to the DR protection group and a member of the same type doesn't exist, the new steps for the newly added members will be added to new plan groups. All the newly added plan groups will be labeled as Group Added , and the newly added steps in those plan groups will be labeled Step Added .
- If you delete an existing member from the DR protection group and other members of the same type still remain in the DR protection group, the steps for the deleted member will be removed from existing plan groups. The plan groups from which the steps were deleted will be labeled as Group Modified , and the deleted steps will be labeled as Step Deleted .
- If you delete an existing member from the DR protection group and no other members of the same type remain in the DR protection group, the steps for the deleted member and the group containing those steps will be removed. The deleted plan groups will be labeled as Group Deleted , and the deleted steps will be labeled as Step Deleted .
- If you remove an existing member from the DR protection group, any associated user-defined step and its pre-check steps are also removed from the plan. The steps will be labeled as Step Deleted .
- When Full Stack DR refreshes the plan and adds new plan groups or deletes existing group, if a user-defined pause group is either the first or last group in the plan, it will be deleted from the plan. These deleted user-defined pause plan groups will be labeled as Group Deleted .
- New plan groups are inserted into the plan based on the pre-determined group order. See[Default Order of DR Plan Groups](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/iaas/disaster-recovery/cssgm&id=CSSGM-GUID-58D37DDF-C64A-43C3-A96B-5520EAB11E87)for more information.
- Full Stack DR attempts to insert new plan groups based on the[Default Order of DR Plan Groups](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/iaas/disaster-recovery/cssgm&id=CSSGM-GUID-58D37DDF-C64A-43C3-A96B-5520EAB11E87). However, if the existing plan has significant changes to the default ordering of the plan groups, Full Stack DR may not be able to insert new plan groups in the correct order. In this situation new plan groups are inserted closest to where their other peer plan groups would be in the default order.
- When a DR protection group has plans in an Active state; Needs attention state and Needs refresh sub-state; or Needs attention state and Needs verification sub-state, and you update the DR protection group, all plans will move to Needs attention state and Needs refresh sub-state.

Parent topic:[Refresh a Disaster Recovery Plan](https://docs.oracle.com/iaas/disaster-recovery/doc/refresh-plan.html#GUID-AF9001EB-C62B-4FFF-835A-5A635D71CBD3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
