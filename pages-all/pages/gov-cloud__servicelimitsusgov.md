# Requesting a Service Limit Increase for Oracle US Government Cloud and Oracle US Defense Cloud
- Source: https://docs.oracle.com/en-us/iaas/Content/gov-cloud/servicelimitsusgov.htm
- Fetched: 2026-09-05 03:32 CDT

# Requesting a Service Limit Increase for Oracle US Government Cloud and Oracle US Defense Cloud

Learn how to request a service limit increase for Oracle US Government Cloud and Oracle US Defense Cloud tenancies.

The US Government Cloud and the US Defense Cloud provide a highly secure, enterprise-scale cloud, isolated from the commercial cloud. The US Government Cloud and the US Defense Cloud both support regulatory compliant, mission-critical public sector workloads, and includes FedRAMP High Joint Authorization Board authorization and DISA Impact Level 5 authorization. This authorization provides compliant, highly secure, and resilient infrastructure and solutions for United States federal, state, and local government, and government-affiliated entities.

OCI services in the commercial cloud, the US Government Cloud, and the US Defense Cloud have the same functionality, however with some notable differences between both the clouds, including how to request a service limit increase.

## Service Limits

Your tenancy has a set of service limits configured for the tenancy. A service limit is the quota or allowance set on a resource. For example, your tenancy has a maximum number of compute instances per availability domain. For more information, see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). You can view your tenancy's limits, quotas, and usage in the Console.

To view your tenancy's service limits, follow these steps:
- In the Console, open the navigation menu, and select Governance and Administration .
- Under Tenancy Management , select Limits, Quotas and Usage .

This page displays resource limits, quotas, and usage for the specific region, by service. You can use the filter lists at the top of the list to filter by service, scope, resource, and compartment.

To request a service limit increase, open a support request. The following sections describe the prerequisites and steps to open the support request. To help you in the process, download the[Limit Increase Request template](https://docs.oracle.com/iaas/Content/Resources/Assets/limit_increase_request.xlsx), an excel file that identifies the information required when requesting a service limit increase. You can fill out this template and then upload it when you create the service request.

## Request a MOS Account

You need to have a MOS account to open a support request. If you don't have an existing MOS account, use the following steps to create a MOS account.
- Navigate to[http://support.oracle.com](http://support.oracle.com).
- Select Register as a new user .
- Complete the form, ensuring that you use your government or company email address.
- Select Create Account .
Note  
  

Oracle support manually reviews account requests, so it can take a few days for your account to be created.

## Create a Service Request

Use the following steps to create a service request for a limit increase. Step 7 includes instructions to upload a file with the request details. You can use the[Limit Increase Request template](https://docs.oracle.com/iaas/Content/Resources/Assets/limit_increase_request.xlsx)to create this file.
- Navigate to[http://support.oracle.com](http://support.oracle.com), select Login to My Oracle Support , and sign in with your Oracle ID.
- On the landing page to create a SR, select Create Service Request located in the top right corner.
- On the Create a new Service Request page, enter the details for the limit increase request, as shown in the following screenshot

[
- Select Technical Issue as the issue type.
- For business impact, specify System Fully Available .
- For who should be able to view this service request, select the tenancy name with the correct CSI.
- Select the primary contact.
- For the service which is experiencing this issue, specify Oracle Cloud Infrastructure .
- For the Cloud Console URL, OCID, Service URL, or Instance URL, specify the cloud Console URL or the OCID.
- For the system lifecycle, select the applicable option, for example production live .
- For title your service request with a brief summary, provide a brief summary of the limit increase request.
- To describe the issue in detail, describe which service limit you would like to increase.
- For how would you categorize this issue, select OCI limits , and then Limit Increase Request .
- For what is your request about, select Have an issue .
- For what is your issue about, select None of the above .
- Specify the report email.
- Specify the tenancy OCID.
- Specify the resource that you want to increase the limit of.
- Specify the current limit that you want to increase.
- Specify the current usage, for example 100 OCPU .
- Specify the requested limit, for example 200 OCPU .
- Select Submit Service Request .
- In the following page, attach the[Limit Increase Request template](https://docs.oracle.com/iaas/Content/Resources/Assets/limit_increase_request.xlsx)
