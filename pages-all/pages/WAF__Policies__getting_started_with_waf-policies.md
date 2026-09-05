# Getting Started with Web Application Firewall Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm
- Fetched: 2026-09-05 03:11 CDT

# Getting Started with Web Application Firewall Policies

Get started with creating and managing a web application firewall policy.

## Before You Begin

For important concepts about the web application firewall, see[Required IAM Service Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#iam).

To begin using the WAF service, you must have the following available:
- 

Ensure that you have the[Required IAM Service Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#iam)permissions.
- 

We recommended that you use a separate compartment for your web application firewall policy so that management is easier and more secure. See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for more information.
- 

A load balancer with an HTTP listener.

You can change your web application firewall policy only when the policy status is ACTIVE.

## Tasks

You can perform the following tasks with WAF policies:

[List the policies in a compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#top).

[Creat a policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/create_waf-policy.htm#top).

[View a policy's details](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/get_waf-policy.htm#top).

[Update a policy's settings](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/update_waf-policy.htm#top).

[Move a policy to another compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm#top).

[Delete a policy from the compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/delete_waf-policy.htm#top).

## Ways to Access the Web Application Firewall Service

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Web Application Firewall Service Capabilities and Limits

The Web Application Firewall (WAF) service has the following capabilities and limits:
- 

Web Application Firewall policies: 100 per tenant.
- 

Network address lists: 100 per tenant.
For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
Note  
  
The WAF service allows a total run time of 10 minutes for upload and download processes through the web application firewall.

- WAF policy doesn't support Network Load Balancer. WAF policy supports only Load Balancer.
- TCP Listener is not compatible with WAF policy. WAF policy supports only[HTTP listeners](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../Concepts/overview.htm#Overview_of_the_Web_Application_Firewall_Service).
- 

WAF policy supports IPv6. WAF policy is attached directly to the[load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)where you can select[IPv6 Support](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).

After you create a load balancer and choose the type, select Enable IPv6 Address Assignment .
When you create a load balancer, you can choose to use an IPv4/IPv6 dual-stack configuration. When you choose the IPv6 option, the Load Balancer service assigns both an IPv4 and an IPv6 address to the load balancer. The load balancer receives client traffic sent to the assigned IPv6 address. The load balancer uses only IPv4 addresses to communicate with backend servers. No IPv6 communication exists between the load balancer and the backend servers.
Note  
  
IPv6 address assignment occurs only during load balancer creation. You can't assign an IPv6 address to an existing load balancer.
- WAF policies are regional only. One WAF policy can't be used in multiple regions simultaneously.
- A single policy can be used with multiple load balancers. You can use a policy with multiple load balancers as long as all load balancers are in the same region as the policy.
- WAF policy rules are run in the following order:
- WAF requestAccessControl
- WAF requestRateLimiting
- WAF requestProtection
- requestProtection rule 1
- header inspection CHECK mode protectionCapabilities
- header inspection BLOCK mode protectionCapabilities
- body inspection CHECK mode protectionCapabilities
- body inspection BLOCK mode protectionCapabilities
- requestProtection rule 2
- requestProtection rule N
- &lt;request forwarded to backend and response is received&gt;
- WAF responseAccessControl
- WAF responseProtection
- responseProtection rule 1
- header inspection CHECK mode protectionCapabilities
- header inspection BLOCK mode protectionCapabilities
- body inspection CHECK mode protectionCapabilities
- body inspection BLOCK mode protectionCapabilities
- responseProtection rule 2
- responseProtection rule N

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, you must be given access in a policy for waas-policy. If you try to perform an action and get a message that you do not have permission or are unauthorized, confirm with your administrator the type of access you have been granted and which compartment you should work in.

Mandatory permissions list :
```

```

Policy examples :
- To allow a specific user group to manage web application firewalls in your tenancy:
```

```

- To allow a specific user group to inspect web application firewall policies in a specific compartment:
```

```

- To allow a specific user group to use web application firewall network address lists in your tenancy:
```

```

If you are new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for WAF, see[Details for the WAF service](https://docs.oracle.com/iaas/Content/Identity/Reference/wafpolicyreference.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
