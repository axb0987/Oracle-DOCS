# Policy Attachment
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm
- Fetched: 2026-09-05 02:26 CDT

# Policy Attachment

When you create an IAM policy, you must attach it to a compartment in IAM.

When you write a policy in the root compartment, the policy applies to the entire tenancy. Typically the Administrators group, or a similar group you create, manages policies. If you attach a policy to a tenancy, anyone who can manage policies in the tenancy can then change or delete the policy for the entire tenancy. Users with access only to a child compartment can't change or delete a policy attached to the root compartment.
