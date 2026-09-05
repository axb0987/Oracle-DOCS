# Supported Terraform Versions
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/terraformversions.htm
- Fetched: 2026-09-05 02:54 CDT

# Supported Terraform Versions

Review the Terraform versions supported by the Resource Manager service.

## Terraform Versions Supported by Resource Manager

Resource Manager supports the following[versions of Terraform](https://releases.hashicorp.com/terraform/)and Terraform CLI versions.
Note  
  
The`terraform_`version prefix (seen in[the Terraform list](https://releases.hashicorp.com/terraform/)) is omitted in the table. The`.x`suffix indicates coverage of minor versions. Patch versions aren't supported.

Terraform Version (CLI Version) Date That Support Began Comments
1.5.x (1.5.7) July 30, 2024 None
1.2.x (1.2.9) February 24, 2023 See footnotes 1 and 2.
1.1.x (1.1.3) May 7, 2022 See footnotes 1 and 2.
1.0.x (1.0.0) June 24, 2021 See footnotes 1 and 2.

1. Deprecation is planned for Terraform versions earlier than 1.5.x. To continue managing the provisioned infrastructure using Resource Manager,[upgrade the associated stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/../Tasks/upgradingstacks.htm)to Terraform version 1.5.x.

2. On April 30, 2026, Resource Manager will make the following changes:
- Stop allowing creation of stacks with Terraform versions earlier than 1.5.x.
- Stop allowing creation of jobs on stacks that have Terraform versions earlier than 1.5.x.
- Stop taking support requests for stacks on Terraform versions earlier than 1.5.x.

## Terraform Versions Previously Supported by Resource Manager

Resource Manager previously supported the following[versions of Terraform](https://releases.hashicorp.com/terraform/).
Note  
  
The`terraform_`version prefix (seen in[the Terraform list](https://releases.hashicorp.com/terraform/)) is omitted in the table. The`.x`suffix indicates coverage of minor versions.

Terraform Version Date That Support Ended Comments
0.14.x April 7, 2025 See footnotes 1 through 3.
0.13.x April 7, 2025 See footnotes 1 through 3.
0.12.x April 7, 2025 See footnotes 1 through 3.
0.11.x September 1, 2021 None

1. Deprecation is planned for Terraform versions earlier than 1.5.x. To continue managing the provisioned infrastructure using Resource Manager,[upgrade the associated stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/../Tasks/upgradingstacks.htm)to Terraform version 1.5.x.

2. Partial support exists for this version. You can run jobs on existing stacks, but you can't create new stacks with this version.

3. On September 1, 2025, Resource Manager will make the following changes:

- Stop support for running jobs with this version.
-
