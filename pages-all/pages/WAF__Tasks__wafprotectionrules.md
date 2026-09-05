# WAF Protection Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/wafprotectionrules.htm
- Fetched: 2026-09-05 03:11 CDT

# WAF Protection Rules

Learn how protection rules match web traffic to rule conditions and determine the action to be taken when the conditions are met.

Protection Rule Settings allow you to define the parameters for enforcement any time a protection rule is matched. Recommendations aid in the optimization of your WAF security profile. The Security Operations team proactively monitors all events to provide recommendations about the action of a specific ruleset. See[Supported Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Reference/protectionruleids.htm#Supported_Protection_Rules)for additional information. Edge policy has approximately[680](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Reference/protectionruleids.htm#rules)rules. Because of Edge policy maturity, multiple versions of the core ruleset (CRS) are included.

Note  
  
We continuously update and optimize existing rules, in addition to creating rules. Because of vulnerability concerns, we can't provide the mitigation pattern for rules.

WAF policies are kept up to date with CRS and CVEs releasing new and updated definitions on a quarterly basis. Rule definitions in use aren't updated since they could cause unexpected behavior. New definitions are always pushed in an off state.

You can enable a maximum of 100 rules per WAF policy.

For more information, see[Supported Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/../Reference/protectionruleids.htm#Supported_Protection_Rules).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Listing and Accepting Protection Rule Recommendations

Use the following operations to get the list of protection rules and settings:
- [GetProtectionSettings](https://docs.oracle.com/iaas/api/#/en/waas/latest/ProtectionSettings/GetProtectionSettings)
- [GetProtectionRule](https://docs.oracle.com/iaas/api/#/en/waas/latest/ProtectionRule/GetProtectionRule)
- [ListProtectionRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/ProtectionRule/ListProtectionRules)
- [ListRecommendations](https://docs.oracle.com/iaas/api/#/en/waas/latest/Recommendation/ListRecommendations)
```

```

Using the key values from the output of the GET call above, you can accept one or more of the recommendations using the following operation passing an array of the keys:
- [AcceptRecommendations](https://docs.oracle.com/iaas/api/#/en/waas/latest/Recommendation/AcceptRecommendations)Body:
```

```

## Protection Rule Specific Settings

Several protection rule settings are settings for specific protection rules.

Setting Rule ID Rule Name
Allowed HTTP Methods 911100 Restrict HTTP Request Methods
Max Total Argument Length 960341 Total Arguments Limits
Max Number of Arguments 960335 Number of Arguments Limits
Max Length of Argument 960208 Values Limits

The term "Arguments" refers to either query parameters or body parameters in a PUT/POST request. For instance, if the Max Number of Arguments is 2 and RuleID 960335 is set to BLOCK, any of the following requests would be blocked:
```

```

```

```

```

```

Max Length of Argument is the length of either a name or the value of the argument. Total Argument Length refers to the sum of the name and value length.

## Exclusions

Configure an exception in the Web Application Firewall service.

Sometimes a protection rule can trigger a false positive. You can configure an exception if the request(s) generating the false positive have a particular argument or cookie that can be used to identify that request be excluded from the action normally taken on the rule. The following exclusion parameters can be used:

Exclusion Parameters

Name

Description

Request Parameters

List of parameter values (by parameter name) from form-urlencoded, XML, JSON, AMP, or POST payloads to exclude from inspecting.

Request Cookies
