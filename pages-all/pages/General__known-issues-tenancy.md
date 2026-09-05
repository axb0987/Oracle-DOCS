# Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/General/known-issues-tenancy.htm
- Fetched: 2026-09-05 02:11 CDT

# Known Issues

These known issues have been identified in Tenancy Management.

## Product categories disallowed from tenancy renaming

Details The following product categories can't use the[tenancy renaming](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/renamecloudaccount.htm)feature:
- [Oracle Enterprise Performance Management](https://www.oracle.com/performance-management/)
- [Oracle Analytics Platform](https://www.oracle.com/business-analytics/analytics-platform/)Workaround We're working on a resolution.

## Tags attributes incorrectly exposed

Details The definedTags , freeformTags , and systemTags attributes in the[AssignedSubscription](https://docs.oracle.com/iaas/api/#/en/organizations/latest/AssignedSubscription),[Subscription](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Subscription/),[SubscriptionSummary](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/SubscriptionSummary), and[AssignedSubscriptionSummary](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/AssignedSubscriptionSummary)references of the[Organizations API](https://docs.oracle.com/iaas/api/#/en/organizations/latest/)
