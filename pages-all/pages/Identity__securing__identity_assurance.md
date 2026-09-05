# Using Identity Assurance
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/securing/identity_assurance.htm
- Fetched: 2026-09-05 02:28 CDT

# Using Identity Assurance

Learn the tasks you can perform with Identity Assurance.

## Listing Identity Assurance Policies

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Domain , Domain Policies , find the Identity Assurance policy section to view a list of verification policies.

## Adding an Identity Assurance Policy

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Domain , Domain Policies , find the Identity Assurance policy section and select the default policy name to add a rule, or select Create policy .
- (Optional) Enter a Name and Description for the policy.
- Create a rule for the Identity Assurance Policy.
- Add a Name and Description for the rule.
- In the Groups section, select groups that you want to add to this rule.
- In the Facial biometrics section, switch on Enable facial biometrics .

- Set the Verification frequency (for example, Every 7 to 14 days). This determines how often the periodic facial scan occurs.
- Select a predefined reenrollment frequency. This determines how often users are prompted to reenroll.
- Switch on Mandate inline enrollment to force users to enroll during their next sign-in. If disabled, users must enroll manually by using their My profile page.
- Enable Identity verification provider. Select the identity verification provider you created and activated in this identity domain.
- Select Add Rule .
- (Optional) (Optional) In the Policy Rules section, select Add rule again to add another workforce verification rule to this policy.

Note  
  
If you added multiple rules to this policy, then you can change the order in which they will be evaluated. Select Edit priority and then use the arrows to change the order of the rules.
- The Identity Assurance policy is saved in a deactivated state. When you finish creating the policy, you must activate the policy to use it.

## Getting an Identity Assurance Policy's Details

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Select one of the Identity Assurance policies to view the details.

## Activate an Identity Assurance Policy

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Select the Identity Assurance policy you want to activate.
- In the Details page, from the Actions menu (three dots) , select Activate policy .
- To confirm the activation, select Activate policy .

## Deactivate an Identity Assurance Policy

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Select the Identity Assurance policy you want to deactivate.
- In the details page, from the Actions menu (three dots), select Deactivate policy .
-
