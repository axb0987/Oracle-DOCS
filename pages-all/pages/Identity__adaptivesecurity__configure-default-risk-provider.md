# Updating the Default Risk Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/configure-default-risk-provider.htm
- Fetched: 2026-09-05 02:16 CDT

# Updating the Default Risk Provider

Update the default risk provider for an identity domain in IAM.

- On the Adaptive security list page, find the current default risk provider. If you need help finding the list page, see[Listing Risk Providers.](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/list-risk-provider.htm#console)
- Select the Actions menu (three dots) in the Default risk provider row and then select Edit risk provider .
- Change the description or risk range. To learn about risk ranges, see[Creating a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/add-third-party-risk-provider.htm).
- Select or clear a checkbox to enable or disable the event. You can't disable all events for the default risk provider.

Note  
  

To set the maximum number of unsuccessful logins for the Too many unsuccessful login attempts event, see[Modifying the Custom Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/../passwordpolicies/modify-custom-password-policy.htm).

To set the maximum number of unsuccessful MFA logins for the Too many unsuccessful MFA attempts event, see[Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/../mfa/configure-multi-factor-authentication-settings.htm).
- Set a value (Weighting) for each event that corresponds to the risk range for this risk provider.

For example, you can set the Low risk range for the risk provider to be 0 to 10, the Medium risk range to be 11 to 80, and the High risk range to be 81 to 100.

If you set the weighting of the Access from an unknown device event to 20, and a low-risk user accesses an identity domain with an unknown device, the user's risk range changes to Medium.
- Select Save changes .
-
