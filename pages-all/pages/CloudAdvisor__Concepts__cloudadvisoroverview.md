# About Cloud Advisor
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/cloudadvisoroverview.htm
- Fetched: 2026-09-05 01:47 CDT

# About Cloud Advisor

Cloud Advisor finds potential inefficiencies in the tenancy and offers guided solutions to help you address them.
Note  
  
Cloud Advisor operates on the tenancy you're signed in to. If you have more than one tenancy, you must sign in to each one separately to see the recommendations for each tenancy. Depending on which type of tenancy you're signed in to (parent, child, or standalone), you might need to switch to a different tenancy before you can implement a recommendation.

## Introduction

Oracle Cloud Advisor is an Oracle Cloud Infrastructure (OCI) service that analyzes the OCI cloud resources of every tenancy, and provides recommendations to maximize cost savings and optimize performance, security, and availability. It complements and cross-sells Cloud Guard and Data Safe, displays summary Cloud Guard data, and redirects customers directly to Cloud Guard for all security issues. The Cloud Advisor service is integrated with Oracle Cloud Infrastructure Identity and Access Management (IAM) service, which provides easy authentication with native Oracle Cloud Infrastructure identity functionality. For more information about Cloud Advisor and its concepts and terms, see[Cloud Advisor Concepts](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/cloudadvisoroverview.htm#cloudadvisoroverview-concepts).

## Benefits

Cloud Advisor helps you:
- Save money: Cost management identifies underutilized resources and makes recommendations so that you can save money without degrading performance.
- Improve performance: Performance recommendations identify overutilized resources, recommend changes, and identify block volumes and boot volumes that aren't using[the performance auto-tuning feature](https://docs.oracle.com/iaas/Content/Block/Tasks/create-autotunepolicies-bv-volume.htm).
- Strengthen system resilience: High availability recommendations provide best practices to manage hardware failure and ensure the resilience and business continuity of your environment.
- Improve security: The built-in[Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/home.htm)recommendations help you see and address security vulnerabilities.

## Operation

Once a day, Oracle Cloud Advisor analyzes all the resources in your tenancy. It identifies cost optimization opportunities, performance bottlenecks, and availability issues in each tenancy. It provides recommendations to help you configure your cloud resources to improve their efficiency in cost management, performance, high availability, and security. It provides a high-level dashboard summary of the recommendations it made and suggests actions that you can take to optimize your cloud resources. Note: Cloud Advisor makes cross-region calls to consolidate usage data and resource metadata from all regions subscribed to the tenancy. Cloud Advisor stores this data in the tenancy's home region to aggregate the data and generate recommendations.

Using Cloud Advisor, you can view, implement, postpone, or dismiss recommendations using the Console,[REST API](https://docs.oracle.com/iaas/api/#/en/advisor/latest), and[CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer.html). Using these tools, you can customize Cloud Advisor to use the recommendation profiles that best match your needs, display only the types of recommendations that you want to see, and postpone, or dismiss recommendations that aren't applicable to you.

For more information about Cloud Advisor operations, see[How Cloud Advisor Works](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/cloudadvisoroverview.htm#cloudadvisoroverview-how_cloud_advisor_works). For more information about how to access Cloud Advisor, see[Using Cloud Advisor](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/cloudadvisoroverview.htm#cloudadvisoroverview-more_information-Copy).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

Although the permissions described above let you view the recommendations and some information about them, beginning in December 2023, Cloud Advisor supports a new dedicated IAM policy that improves data security and safeguards resource metadata using granular permissions to support compartment and resource based security policies. These permissions are granted at the compartment level rather than the tenancy level as was previously done. If you don't have the correct permissions, you might not be able to view all the recommendation details, or the resource details for the recommendation you're viewing. To view all the recommendation and resource metadata, contact your account administrator to get the permissions for your compartment. For more information, see[Additional Required Permissions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/additional_required_permissions.htm).

## Recommendation Categories

Cloud Advisor provides three categories of recommendations:
- Cost management recommendations identify underutilized resources and help you reduce costs by right-sizing them to the optimum size.

Example: Cost management recommendations find underutilized Compute instances, overprovisioned Autonomous AI Lakehouse instances, unattached block volumes, unattached boot volumes, and Object Storage buckets without lifecycle policy rules. They show you the current use and cost, the number of recommendations made for improvement, the recommended usage, and the cost savings per month.
- Performance recommendations find overutilized resources and recommend changes.

Example: Performance recommendations show you how improve performance by rightsizing overutilized Compute instances and load balancers, and how to optimize performance settings by finding block volumes and boot volumes that aren't using the autotune feature.
- High availability recommendations provide hardware failure best practices to ensure the resilience of your solution and show you how to improve system resilience.

Example: High availability recommendations might suggest increasing the availability of applications running on Oracle Cloud Infrastructure by using redundant Compute nodes in different availability domains to support failover capability and correctly leverage fault domains.

More information about categories and a complete list of Cloud Advisor recommendations are on this page:[Categories and Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations.htm).

## Viewing Recommendations across an Organization

Cloud Advisor customers in a parent tenancy can view recommendations at both the parent and child tenancy levels. Cloud Advisor creates a consolidated report of Cloud Advisor's recommendations across the region as well as the tenancies it contains. For organization users, a parent tenancy can view the recommendations that are generated for any child tenancy in their organization. Note: The Cloud Advisor Organization feature automatically lets resource metadata in a child tenancy become available to your parent tenancy. If you don't want the resource material in the child tenancy to be visible in the parent tenancy, disable Cloud Advisor in the child tenancy.

For more information about organization management see[Organization Management Overview](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm).

## More Information

This section provides details about how Cloud Advisor works, the concepts used in Cloud Advisor, ways to access Cloud Advisore, Cloud Advisor authentication and authorization and using the CLI and API.

### How Cloud Advisor Works

Cloud Advisor scans your tenancy once a day to identify problems and generates recommendations to solve them. Depending on the[recommendation type](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations.htm), Cloud Advisor either provides recommendations immediately after scanning the tenancy, or after seven days, when Cloud Advisor has accumulated enough data to recommend actions. (For Cloud Advisor to see CPU utilization and provide Compute recommendations, you must enable Compute Agent to monitor Compute instances. When monitoring isn't enabled, Cloud Advisor generates a recommendation that you enable it. For more information, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).)

Cloud Advisor makes cross-region calls to consolidate usage data and resource metadata from all regions subscribed to the tenancy. Cloud Advisor stores this data in the tenancy's home region to aggregate the data and generate recommendations.

When Cloud Advisor has enough data to provide recommendations, it displays a list of recommendations in the Recommendations dashboard. When applicable, the recommendations include cost savings estimates. In the Recommendations dashboard, you can implement, postpone, or dismiss the recommendations. For more information, see[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm).

When possible, Cloud Advisor allows you to[implement recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm)directly from the Recommendations dashboard. Often, you can implement the recommendation either for specific resources or for all resources in the tenancy. When you implement a recommendation within Cloud Advisor, a work request for the change is created. When the work request completes, the new status appears in the History table.

You can also implement recommendations with the API or manually with the Console. In those cases, the new status is reflected in the History table the next time Cloud Advisor scans your tenancy. To view the History table, see[Viewing Recommendation History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm).

### Cloud Advisor Concepts

This section provides a list of basic concepts for Cloud Advisor. Recommendation Cloud Advisor scans your tenancy to find potential inefficiencies and then uses this information to provide recommendations that suggest ways to reduce costs and increase efficiency. For information about the specific types of recommendations, see[Categories and Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations.htm). Estimated cost savings Cloud Advisor provides estimated cost savings for applicable recommendations. This value is a dollar amount that estimates how much lower your costs could be if you implement the recommendation. These values are estimates and are not guaranteed. For more information, see[How Cost Savings Estimates Are Calculated](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm#cost-calc). Status Each recommendation has a status that reflects its current state.
- Pending . When Cloud Advisor identifies a recommendation but no user action has been taken, the status of the recommendation is Pending. Cloud Advisor evaluates each resource once every 24 hours and sets the status accordingly.
- Implemented . When a recommendation is implemented, the suggested change has been made in the tenancy. The recommendation status is also implemented when a recommendation is no longer applicable because of a change in usage in your tenancy.
- Postponed . When a recommendation is postponed, it does not appear in your dashboard until a future date that you select.
- Dismissed . When a recommendation is dismissed, it does not appear in your dashboard until you reactivate it. Implement You can implement (activate) a recommendation to make the suggested change to your resources.
- When you use Cloud Advisor to implement a recommendation, the system creates a work request. When the work request completes, a row appears in the[History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm)table with the recommendation status Implemented.
- When you implement a recommendation using a work flow outside of Cloud Advisor, an entry appears in the History table after Cloud Advisor scans the tenancy. Postpone You can postpone a recommendation so that it does not appear in your dashboard until a future date of your choice.
- When you postpone a recommendation for a single resource or for a select list of resources, a row for each resource appears in the History table. The recommendation status is Postponed.
- When you postpone a recommendation for all resources, no entry appears in the[History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm)table, and no existing recommendations become postponed. Postponing a recommendation for all resources prevents Cloud Advisor from making new recommendations of this type until the postponement expires. Dismiss You can dismiss a recommendation so that it no longer appears in your dashboard.
- When you dismiss a recommendation for a single resource or for a select list of resources, a row for each resource appears in the History table. The recommendation status is Dismissed.
- When you dismiss a recommendation for all resources, no entry appears in the[History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm)table, and no existing recommendations become dismissed. Dismissing a recommendation for all resources prevents Cloud Advisor from making new recommendations of this type unless the recommendation is reactivated. Reactivate You can reactivate a recommendation that has been postponed or dismissed, and Cloud Advisor once again includes this recommendation when it scans your tenancy. The status temporarily changes to Pending, and the next time Cloud Advisor scans the tenancy, Cloud Advisor updates the recommendation status and the associated cost savings estimate.
- When you reactivate a recommendation for a single resource or for a select list of resources, a row for each resource appears in the[History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm)table. The recommendation status is Pending.
- When you reactivate a recommendation for all resources, no entry appears in the[History](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/history.htm)table.

### Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure using the Oracle Cloud Infrastructure Console (a browser-based interface), the Command Line Interpreter (CLI), the[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs), or the[OCI Terraform Provider.](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/optimizer_enrollment_status)Instructions to use the Console, CLI, and API are included in topics throughout this guide. The list of available SDKs is at[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface). See the[OCI Terraform Provider documentation](https://docs.oracle.com/iaas/Content/API/SDKDocs/terraform.htm)for information about using Cloud Advisor with Terraform.

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#Supporte). To go to the Console sign-in page, open the navigation menu at the top of this screen and select Infrastructure Console . When prompted, enter a cloud tenant, username, and password.

For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

### OCI Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### Cloud Advisor CLI and API

- For the full list of Cloud Advisor CLI commands, see[Cloud Advisor CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/optimizer.html).
- For the complete Cloud Advisor API documentation, see[Cloud Advisor API](https://docs.oracle.com/iaas/api/index.html#/en/advisor/20200606/).

## Using Cloud Advisor

The following topics explain how to use Cloud Advisor.

[Getting Started with Cloud Advisor](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-getting_started.htm)

[Viewing Categories and Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/view-recommendations.htm)

[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/implementing_cloud_advisor_recommendations.htm)

[Cloud Advisor settings](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/cloudadvisor-cloud_advisor_settings.htm)

[Creating Cloud Advisor queries](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Reference/query-syntax.htm)

[Creating Cloud Advisor policies](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Reference/cloudadvisorpolicyreference.htm)
