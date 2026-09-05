# Accepting Recommendations for Protection Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/accepting_recommendations.htm
- Fetched: 2026-09-05 03:11 CDT

# Accepting Recommendations for Protection Rules

Use Web Application Firewall to accept recommendations for protection rules.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/accepting_recommendations.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/accepting_recommendations.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/accepting_recommendations.htm#)
- 

Recommendations begin appearing after enough traffic has gone through a web application firewall (WAF) to profile the correct security posture.
- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:
- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy that you want to configure rule settings for.

The edge policy's details page opens.
- On the policy details page, under Edge policy , select Protection rules .
- Select the Recommendations tab.
- Select the protection rules that you want to accept.

You can use the Recommended action filter to find a recommendation by Detect or Block .
- Select Accept recommendation .

The accepted protection rules are added to the list to be published. For more information, see[WAF Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/wafprotectionrules.htm#WAF_Protection_Rules).
- 

This task is not available in the CLI.
- 

Run the[AcceptRecommendations](https://docs.oracle.com/iaas/api/#/en/waas/latest/Recommendation/AcceptRecommendations)
