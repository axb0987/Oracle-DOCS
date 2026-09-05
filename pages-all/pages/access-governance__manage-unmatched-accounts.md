# Manage Unmatched Accounts
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-unmatched-accounts.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Unmatched Accounts

## Match Unmatched Accounts to an Identity

Unmatched accounts are those accounts from a Managed System which do not match any identities in Oracle Access Governance. Unmatched accounts can be managed by administrators in the Oracle Access Governance Console.

You can match unmatched accounts to an identity in Oracle Access Governance as described in the following:
- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Unmatched Accounts page by one of the following methods:
- Select the Service Administration tab from the Oracle Access Governance service home page, and click Select on the What accounts exist that are not assigned to an identity? tile.
- On the Oracle Access Governance service home page, click on the icon, then select Service Administration → Unmatched Accounts .
- On the Unmatched Accounts page, a list of all unmatched accounts is displayed, with the following information:
- Account : the account name
- Target : the target Managed System the account was ingested from.
- Date created : the date the account was created on the target Managed System.
- Insights : insights into why the account is unmatched. These include:
- Multi-match : account matches multiple identities in Oracle Access Governance
- No match : account matches no accounts in Oracle Access Governance
- User deleted : account matches a identity in Oracle Access Governance which has been deleted in a source Managed System, but which still has accounts open on other Managed Systems.
- You can filter the list of unmatched accounts displayed in the following ways:
- Search using free text.
- Select a specific insight to filter on.
- Select a target from the Target drop down list to filter on.
- You can download a CSV file of the unmatched accounts by selecting the CSV download icon, . Selecting this download will save the unmatched accounts according to any filters which have been applied. The results are saved to a file,`unmatchedAccounts-report.csv`.
- Once you have identified an account you want to match to an existing Oracle Access Governance identity, you can manage it using the following steps:
- Select the actions menu, for the account you wish to match.
- Select the Match to identity action.
- The All identities tab will display for insight types/ Search for the identity you want to match the account to.
- Select the identity you want to match, and click Match to identity .
- If the insight type is Multi-match then an additional tab is displayed for Suggested identities . This provides suggestions for the identities you can match to your unmatched account. You can accept one of the suggestions, or navigate to the All identities tab and search as detailed in the previous steps.

## Remove Unmatched Account

In certain circumstances you may not be able to match an unmatched account with an identity. In this case, you may want to remove the orphan account from Oracle Access Governance and the Managed System it was ingested from. This prevents the unmatched account from being re-ingested in subsequent dataloads, or used in any other way in your environment.
To remove an unmatched account from your environment:

- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Unmatched Accounts page by one of the following methods:

- Select the Service Administration tab from the Oracle Access Governance service home page, and click Select on the What accounts exist that are not assigned to an identity? tile.
- On the Oracle Access Governance service home page, click on the icon, then select Service Administration → Unmatched Accounts .
- Identify the unmatched account you want to remove.

- Select the actions menu, for the account you wish to remove.
- Select the Remove action.
