# Using Cloud Guard
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-using_cloud-guard.htm
- Fetched: 2026-09-05 03:04 CDT

# Using Cloud Guard

Use Cloud Guard to detect users who don't have MFA enabled, and local users who have authenticated without using MFA.

We recommend that you[enable Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/../Concepts/security_features.htm#Cloud_Guard)in your tenancy. The OCI Configuration Detector Recipe (Oracle managed) has two detector rules to help you maintain a good security posture:
- User does not have MFA enabled

Alert when a user doesn't have multifactor authentication (MFA) enabled. Risk level is CRITICAL. See[User does not have MFA enabled](https://docs.oracle.com/iaas/Content/cloud-guard/using/detect-recipes.htm#detect-recipes-ref-config__NO_MFA_ENABLED_FOR_USER)in the Cloud Guard service documentation.
- Local user authenticated without MFA

Alert when a local user who doesn't have multifactor authentication (MFA) enabled is authenticated. Risk level is HIGH. See[Local user authenticated without MFA](https://docs.oracle.com/iaas/Content/cloud-guard/using/detect-recipes.htm#detect-recipes-ref-activity__NON_MFA_USER_LOGIN)in the Cloud Guard service documentation.

In Cloud Guard, filter the list of problems detected to find out the users who triggered these alerts so that you can take the appropriate actions to ensure that MFA is enabled and being used by all users. See[Processing and Resolving Problems on the Problems Page](https://docs.oracle.com/iaas/Content/cloud-guard/using/problems-page.htm)in the Cloud Guard documentation.

- Open the navigation menu and click Identity &amp; Security . Under Cloud Guard , select Problems . All problems are listed.
- Click in Filters and choose Problem name , then choose = , then choose the name of the rule:

- User does not have MFA enabled
- Local user authenticated without MFA
Note  
  
You can only list incidences for one problem name at a time.
-
