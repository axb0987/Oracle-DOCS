# Updating a Third-Party Risk Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/modify-third-party-risk-provider.htm
- Fetched: 2026-09-05 02:16 CDT

# Updating a Third-Party Risk Provider

Update the values for a third-party risk provider in an identity domain in IAM.

- On the Adaptive security list page, find the risk provider that you want to see detailed. If you need help finding the list page, see[Listing Risk Providers.](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/list-risk-provider.htm#console)
- Select the Actions menu (three dots) of the risk provider that you want to update and then select Edit risk provider .
The risk provider details and risk ranges are displayed. To learn about risk ranges, see[Creating a Third-Party Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/add-third-party-risk-provider.htm).
Note  
  
If you select the default risk provider, you see a third section: Events. To learn more about events, see[Updating the Default Risk Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/configure-default-risk-provider.htm).
- Make any necessary changes.
- Select Validate risk provider .
- Verify that you see the message, The connection to the {risk_provider_name} risk provider has been validated. . If you receive an error message, check the values that you changed for the Risk provider URL and Authentication type fields.
- Select Save changes .
-
