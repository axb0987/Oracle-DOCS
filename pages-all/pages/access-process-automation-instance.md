# Access the Process Automation Instance
- Source: https://docs.oracle.com/iaas/process-automation/oci-process-automation/access-process-automation-instance.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/process-automation/oci-process-automation/access-process-automation-instance.html#dcoc-content-body)

# Access the Process Automation Instance

After you've provisioned a Oracle Cloud Infrastructure Process Automation instance, you can access it from the Oracle Cloud Console.

Note  
  

From January 2026 release, any newly provisioned Oracle Cloud Infrastructure Process Automation instances do not have a process specific identity application. However, the new Process Automation instances use the identity application used by Oracle Integration. To work in Process Automation Designer, users need access to ServiceDeveloper role in Oracle Integration. To use the administration capabilities of Process Automation Workspace, users need access to ServiceAdministrator role in Oracle Integration.

If a user in Oracle Integration has ServiceDeveloper and ServiceAdministrator roles, then the user has by default access to process components when a new Process Automation instance is provisioned.
- Sign in to the Oracle Cloud Console.
- Open the navigation menu and click Developer Services . Under Application Integration , click Process Automation .
- From the Compartment drop-down list, select the compartment in which you created your Process Automation instance.
The existing instances in the selected compartment are listed.
- You can filter down further by instance states. Under Filters, select Active from the State drop-down list.
- Click the instance to open the instance details page.
- On the instance details page, click Open console to access the Process Automation instance login page.

If a message appears that access was denied, you don't have access to Process Automation Designer (design-time).
For users to access the Process Automation Designer, they have to be assigned the ServiceDeveloper IDCS application role. See:
- [Assign IDCS Application Roles to Groups](https://docs.oracle.com/iaas/process-automation/oci-process-automation/assign-idcs-application-roles-groups.html#GUID-6F82B385-01A5-40BF-97D8-2F7543516B70)
- [Assign IDCS Application Roles to Groups in an Identity Domain](https://docs.oracle.com/iaas/process-automation/oci-process-automation/assign-idcs-application-roles-groups-identity-domain.html#GUID-E7F7993C-BE58-4CAE-9999-63A3FD010B83)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
