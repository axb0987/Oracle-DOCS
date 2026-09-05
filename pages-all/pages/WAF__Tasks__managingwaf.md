# Managing Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm
- Fetched: 2026-09-05 03:11 CDT

# Managing Edge Policies

Manage Edge policies in the Web Application Firewall.

Use the Oracle Cloud Infrastructure WAF service to create an edge policy and origin.

## Order of Processing

The order in which rules and handlers are processed is:
- IP Whitelists/Blacklists/Good Bot Whitelists
- Threat Intelligence
- Access Rules
- Rate Limiting (available in the API)
- JavaScript Challenge
- Device Fingerprinting Challenge
- Human Interaction Challenge
- Captcha Challenge
- Protection Rules
- Caching Rules

## Using the Console

### Create and Manage WAF Policies

[To create an edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select Create edge policy .

The Create edge policy panel opens.
- Complete the following:
- Name: A unique name for the policy.
- Domains:
- Primary Domain : The fully qualified domain name (FQDN) of the application where the policy will be applied.
- Additional Domains : (Optional) Subdomains where the policy will be applied. There isn't a limit on the number of domains that can be added.
Note  
  

Wildcard domains are accepted, however, only as additional domains and only through the API and CLI.
- WAF Origin: The host or IP address of the public internet facing application that is being protected by the application.
- Origin Name : A unique name for the origin.
- URI : Enter the public facing endpoint (IPv4 or FQDN) of the application.
- HTTPS Port : The port used for secure HTTP connection. The default port is 443.
- HTTP Port : The HTTP port the origin listens on. The default port is 80.
- Headers: (Optional)
- Header Name : The name displayed in the HTTP request header and the header value that can be added and passed to the origin server with all requests.
- Header Value : Specifies the data requested by the header.
- Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create WAF Policy . The WAF Policy overview appears. Expect the policy to become active within 15 minutes of creation.

See[Managing Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#Managing_WAF_Policies)for more information.

[To update an edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Apply one or more of the following Filters to limit the edge policies displayed:
- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- 

Select the name of the edge policy you want to update. The Details page for the edge policy you selected appears.
Tip  
  
You can use the Date Created sort filter to sort policies by the date they were created in ascending or descending order.
- Select Edit .
- 

In the Edit Edge Policy dialog box, make the needed changes and then select Save Changes .

[To delete an edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Apply one or more of the following Filters to limit the edge policies displayed:
- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- 

Select the check box for the policy you want to delete.
Tip  
  
You can use the Date Created sort filter to sort policies by the date they were created in ascending or descending order.
- Select Delete .
- 

In the confirmation dialog box, select Delete .

The status of the policy changes from Active to Deleting . Deleted policies are maintained for a short time before they are unavailable in the Console.

[To publish changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

Updates to your WAF policy appear in the list to be published in Unpublished Changes. Pending changes do not persist across browser sessions. Once you publish changes, it cannot be edited until changes propagate to the edge nodes.
- In the WAF Policy overview, select Unpublished Changes .
- In the Unpublished Changes list, select the drop-down arrow beside an unpublished change to review the change.
- Select Publish All .
- In the Publish Changes dialog box, select Publish All .

[To manage tags for a edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the edge policy you want to view. The Details page for the edge policy you selected appears.
- Select the Tags tab to view or edit existing tags. Or select Apply tag(s) to add new ones.

For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

[To move a edge policy to a different compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/managingwaf.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Apply one or more of the following Filters to limit the edge policies displayed:
- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- Find the WAF policy in the list, select the Actions menu (three dots) , and then select Move Resource to a Different Compartment .
- Choose the destination compartment from the list.
- Select Move Resource .

## Using the CLI

Open a command prompt and run the following command to get the details of a WAAS policy:
```

```

This can be useful in retrieving the necessary information when opening a ticket with Oracle Cloud Infrastructure support. For more information about how to access and use the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
- [CreateWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/CreateWaasPolicy)
- [GetWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/GetWaasPolicy)
- [UpdateWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/UpdateWaasPolicy)
- [DeleteWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/DeleteWaasPolicy)
- [ChangeWaasPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/ChangeWaasPolicyCompartment)
