# Configure Risk Management Cloud (RMC) for Segregation of Duties (SoD) Check
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-rmc-segregation-of-duties.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Risk Management Cloud (RMC) for Segregation of Duties (SoD) Check

You can evaluate permissions or roles of users within Oracle Fusion Cloud Applications to ensure that permission assignment is valid and doesn't violate SoD checks.

Complete the prerequisites and run mandatory jobs periodically.

Mandatory Role : Risk Administrator Role . With this role, Oracle Access Governance can run Global User Synchronization job periodically before Preventive SoD analysis request. For more information, see[Configure Global Users](https://docs.oracle.com/en/cloud/saas/risk-management-and-compliance/25c/farrm/configure-global-users.html).

## Associate Worker Information with User
A user account must have associated worker information. On the Security Console → Users page, verify that a linked account shows Associated Worker Information .
Note  
  
If you receive an error such as " Applying List binding LOV_PersonNumber " while linking PersonNumber to the user account, run the following HCM jobs: Compute Users ACL by Events, Compute Users ACL, Compute Users With Large ACL . For steps, see[Schedule ACL Processes](https://docs.oracle.com/en/cloud/saas/human-resources/faeos/schedule-acl-processes.html).

## Run Mandatory Background Jobs

In Oracle Fusion Cloud Applications, after creating or updating the user account, run the following jobs in the order:
- Import User and Role Application Security Data. For more information, see[Run the Import User and Role Application Security Data Process](https://docs.oracle.com/en/cloud/saas/human-resources/ochus/import-users-and-roles-into-applications-security.html).
- Security Synchronization. For more information, see[Predefined Security Jobs](https://docs.oracle.com/en/cloud/saas/risk-management-and-compliance/25c/fasor/predefined-security-jobs.html).
Note  
  
Run these jobs after creating or changing the service account's security configuration periodically or on demand to avoid errors during SoD Checks.

## Verify User Visibility in Risk Management

After running the jobs, verify the results:
- Navigate to Risk Management → Setup and Administration → Global User Configuration .
- Search for the user for whom you want to run the SoD violations check.

## Workflow Configuration

You must attach an approval workflow with an access bundle to process violation checks. If an access bundle has no approval workflow assigned, Oracle Access Governance triggers the SoD violations check but the provisioning proceeds immediately even if potential violations exist. When an approval workflow is attached, Oracle Access Governance pauses the request until the SoD analysis completes.

For more information, see[Preventive Segregation of Duties](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#preventive-segregation-of-duties)
