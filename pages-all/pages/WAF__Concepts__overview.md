# Overview of Web Application Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm
- Fetched: 2026-09-05 03:10 CDT

# Overview of Web Application Firewall

Learn about Oracle Cloud Infrastructure Oracle Cloud Infrastructure Web Application Firewall, a regional-based and edge enforcement service that's attached to an enforcement point, such as a load balancer or a web application domain name.

WAF protects applications from malicious and unwanted internet traffic. WAF can protect any internet facing endpoint, providing consistent rule enforcement across a customer's applications.
Note  
  

To use WAF for edge enforcement, see[Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../EdgePolicyResources/legacy_waf.htm#legacy_waf).

WAF provides you with the ability to create and manage rules for internet threats including Cross-Site Scripting (XSS), SQL Injection, and other OWASP-defined vulnerabilities. Access rules can limit based on geography or the signature of the request.

[WAF policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm#Overview_of_the_Web_Application_Firewall_Service)is a regional solution that works as a plug-in for your load balancer.

[Edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#GettingStartedEdgePolicies)is a global solution. To use this solution, allowlist Oracle nodes throughout the world and use DNS to point your application to the CNAME that we provide.

You can convert an Edge policy to a WAF policy and vice a versa, by manually recreating the settings and policy. No automated method or tool exists for this conversion.

## WAF Concepts

Describes concepts associated with a web application firewall (WAF). Access Control Access control encompasses request and response controls. Action

Actions are objects that represent one of the following:
- Allow : An action, which upon matching rule, skips all remaining rules in the current module.
- Check : An action which does not stop the execution of rules in current module. Instead it generates a log message documenting result of rule execution.
- Return HTTP response : An action which returns a defined HTTP response. Condition Each rule accepts a JMESPath expression as the condition. HTTP requests or HTTP responses (depending on the type of rule) trigger WAF rules. Firewall The Firewall resource is a logical link between a WAF policy and an enforcement point, such as a load balancer. Network Address List Network address lists are collections of individual public IP addresses and CIDR IP ranges or private IP addresses used by WAF policies. Origin Your web application's origin host server. Protection Rule Protection rules are sets of protection capabilities that are used to determine if traffic should be logged, allowed, or blocked. The WAF will observe traffic to your web application. To view a list of available WAF rules, see[Protection Capabilities](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Protections/protections_management.htm#ProtectionRulesWAF). Rate Limiting Rate limiting allows inspection of HTTP connection properties and limits the frequency of requests for a given key. Request Control Request control allows inspection of HTTP request properties and the return of a defined HTTP response. Request Protection Rules Request protection rules enable the checking of HTTP requests for malicious content and the return of a defined HTTP response. Response Control Response control allows inspection of HTTP response properties and the return of a defined HTTP response. Web Application Firewall (WAF)

WAF is a Payment Card Industry (PCI) compliant, global security service that protects applications from malicious and unwanted internet traffic.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in your organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. These policies control who can create users, create and manage the cloud network, launch instances, create buckets, download objects, and similar tasks. For more information, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.

## Creating Automation with Events

You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Security

This topic describes security for WAF.

For information about how to secure WAF, including security information and recommendations, see[Securing Web Application Firewall](https://docs.oracle.com/iaas/Content/Security/Reference/waf_security.htm)
