# Manage Service Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-service-instance.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Service Instance

You can manage an Oracle Access Governance instance in the Oracle Cloud Infrastructure Console. The steps below show you how to perform management tasks on your service instance using the Oracle Cloud Infrastructure Console.

## Review Service Instance

As Cloud Account Administrator , you can review Oracle Access Governance instances in the Oracle Cloud Infrastructure Console.
To review the details of a service instance, use the tasks detailed in this section:

- Open the web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of the Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter the sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Select Sign In .
- Select the icon in the top left corner to display the navigation menu .
- Select Identity and Security in the navigation menu
- Select Access Governance from the list of products.
- On the Access Governance page, select Service Instances .
- Select the Actions menu for the service instance that you want to review.
- Select View details .
- Review the information for the service instance in the Service Instance Details page.

## Launch Service Home Page

As a Cloud Account Administrator , you can launch the service home page for Oracle Access Governance from the Oracle Cloud Infrastructure Console.
To launch the service home page:

- Open the web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of the Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Select Sign In .
- Select the icon in the upper left corner to display the navigation menu .
- Select Identity and Security in the navigation menu
- Select Access Governance from the list of products.
- On the Access Governance page, select Service Instances .
- Select the Actions menu for the service instance that you want to review.
- Select Service home page .
- Perform activities in the Oracle Access Governance Console.

## Edit Service Instance

As a Cloud Account Administrator , you can edit an Oracle Access Governance service instance from the Oracle Cloud Infrastructure Console.
To edit a service instance:

- Open your web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of your Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Click Sign In .
- Click the icon in the top left corner to display the navigation menu.
- Click Identity and Security in the navigation menu
- Select Access Governance from the list of products.
- On the Access Governance page, select Service Instances .
- Select the Actions menu for the service instance that you want to review.
- Select Edit .
- The Cloud Account Administrator can update the name and description of the service selected, or upgrade the Licence Type as required.
Licence type becomes more inclusive in the following order:
- Access Governance for Oracle Cloud Infrastructure
- Access Governance for Oracle Workloads
- Access Governance Premium

You can only upgrade to a more inclusive licence type:
- Access Governance for Oracle Cloud Infrastructure to Access Governance for Oracle Workloads is a valid upgrade.
- Access Governance for Oracle Cloud Infrastructure to Access Governance Premium is a valid upgrade.
- Access Governance for Oracle Workloads to Access Governance Premium is a valid upgrade

You cannot downgrade to a less inclusive licence type:
- Access Governance Premium to Access Governance for Oracle Workloads is not valid.
- Access Governance Premium to Access Governance for Oracle Cloud Infrastructure is not valid.
- Access Governance for Oracle Workloads to Access Governance for Oracle Cloud Infrastructure is not valid.

When you select a license option, be aware that it may take approximately 10 minutes before the licence is enabled on your service instance.

## Delete Service Instance

As a Cloud Account Administrator , you can delete an Oracle Access Governance service instance from the Oracle Cloud Infrastructure Console.
To delete a service instance:

- Open your web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of your Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Click Sign In .
- Click the icon in the top left corner to display the navigation menu .
- Click Identity and Security in the navigation menu
- Select Access Governance from the list of products.
- On the Access Governance page, select Service Instances .
- Click the Actions menu for the service instance that you want to review.
- Select Delete .
- The service instance is marked for deletion. The service URL to the Oracle Access Governance Console is inaccessible to all users.

Note  
  
The service instance is displayed in the OCI Console for 60 days following deletion, with a status of Deleted . After 60 days the deleted service instance is removed from the OCI Console.

## Session Idle Timeout

Oracle Access Governance administrators can configure automatic sign-out after a period of inactivity. To configure session timeout for the service instance, see[Session Idle Timeout](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#inactivity-timeout)
