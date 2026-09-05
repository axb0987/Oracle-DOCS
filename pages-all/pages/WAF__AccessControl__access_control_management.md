# Access Controls for Web Application Firewall Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/access_control_management.htm
- Fetched: 2026-09-05 03:09 CDT

# Access Controls for Web Application Firewall Policies

Learn about how to add and manage the access controls for web application firewall policies.

Web application firewall access control consists of creating and managing access rules for the following controls:
- Request controls : Rules controlling the inspection of HTTP request properties and the return a defined HTTP response. See[Request Access Rules for a Web Application Firewall Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/request_control_management.htm#RequestControlManagement)for more information.
- Response controls : Rules controlling the inspection of HTTP response properties and the return a defined HTTP response. See[Response Control for a Web Application Firewall Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/response_control_management.htm#ResponseControlManagement)for more information.

## Access Rules

As a WAF administrator, you can define explicit actions for requests that meet various conditions. Conditions use various operations. A rule action can be set to allow, check, and return HTTP response for all matched requests. See[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Actions/actions_management.htm#RateLimitinglManagement)for more information on actions.

If a WAF policy resource has multiple access rules configured, the rules are run in order. You can reorder these rules as needed.

The available conditions for an access rule are listed and described in[Understanding Conditions](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Concepts/understanding_conditions.htm#understanding_conditions).

Access rules are distinct for request control and response control of a WAF policy. The same access rule cannot be shared between the two types of controls. Management of access rules, such as adding, editing, and deleting an access rule, is described in the[Request Access Rules for a Web Application Firewall Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/request_control_management.htm#RequestControlManagement)and[Response Control for a Web Application Firewall Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/response_control_management.htm#ResponseControlManagement)sections.

You can explicitly set up a block of all traffic that doesn't meet access control rules conditions by configuring a[default action](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/get_access_rule_request_control.htm#top)
