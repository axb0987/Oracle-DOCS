# Activate the Oracle Fusion Data Intelligence Subscription
- Source: https://docs.oracle.com/iaas/analytics-for-applications/doc/activate-oracle-fusion-data-intelligence-subscription.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-for-applications/doc/activate-oracle-fusion-data-intelligence-subscription.html#dcoc-content-body)

# Activate the Oracle Fusion Data Intelligence Subscription

Activate your Oracle Fusion Data Intelligence subscription into the Oracle Cloud account where you've Oracle Fusion Cloud Applications.

After Oracle processes your subscription order, you receive an email asking you to activate the subscription. As part of the activation process, you sign into the Cloud account that has your Oracle Fusion Cloud Applications already in it. Upon signing in, you're taken to the Add Subscription page in the Oracle Cloud Infrastructure Console where you'll add the Oracle Fusion Data Intelligence subscription to the Cloud account.
Note  
  
Your subscriptions are linked and activated into the home region of your tenancy. After activating a subscription, you can create the Oracle Fusion Data Intelligence instance in the regions where Oracle Fusion Data Intelligence is available and you have subscribed for such regions. Use the Manage Regions option in the Oracle Cloud Infrastructure Console to subscribe for a region. See[Region Availability](https://docs.oracle.com/iaas/analytics-for-applications/doc/region-availability.html#GUID-E51125AE-D726-43B6-853A-BDEE3DBC224B)and[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#Managing_Regions).

After you add the Oracle Fusion Data Intelligence subscription, it can take up to an hour for the activation process to complete. You’ll receive another email confirming that your subscription is ready. Don't proceed to the next step until you’ve received this email.
- Locate your Oracle Fusion Data Intelligence Welcome email that you received from Oracle Cloud.

Note  
  
The name of the service in the body of this Welcome email is "Oracle Fusion XXX Analytics…" where XXX represents the pillars you subscribed to, such as Fusion HCM Analytics and Fusion ERP Analytics.  

  

- In the email, click Add to existing cloud account .
  

  

- On the Oracle Cloud page, click Sign In using a Cloud Account Name .
  

  
[Description of the illustration fawag-sign-into-existing-cloud-account.png](https://docs.oracle.com/iaas/analytics-for-applications/doc/img_text/fawag-sign-into-existing-cloud-account.html)  

- In Cloud Account Name , enter the tenancy name of the existing Oracle Cloud account that has Oracle Fusion Cloud Applications and then click Next .
  

  
[Description of the illustration fawag-oracle-cloud-account.png](https://docs.oracle.com/iaas/analytics-for-applications/doc/img_text/fawag-oracle-cloud-account.html)  

If you don't see your existing Oracle Cloud account that has Oracle Fusion Cloud Applications in it, stop and submit a service request against Oracle Fusion Data Intelligence in My Oracle Support so that it gets routed to the correct team. For this service request, select Significant Impairment as Issue Type and in Problem Type , click Activate, Create, Delete, Manage FDI Instance and then select FDI Activation . Ensure that you include the account name you're trying to activate into along with a screen shot showing that you’ve been assigned this role in that Cloud account.
- On the Oracle Cloud Account Sign In page, sign in as follows:
- 

If the tenancy is set up with single sign-on, then in the Single Sign-On (SSO) section, select the applicable identity provider and click Continue to display the sign-in details.  
  

In the Oracle Cloud Account sign-in details, verify that the tenancy name is your Oracle Fusion Cloud Applications account, enter your credentials, and then click Sign In that takes you to the Add Subscription page in Oracle Cloud Infrastructure.  
  

- If the tenancy isn’t set up with single sign-on, then in the Oracle Cloud Account sign-in details, verify that the tenancy name is your Oracle Fusion Cloud Applications account, enter your credentials, and then click Sign In which takes you to the Add Subscription page in Oracle Cloud Infrastructure.
- On the Add subscription page, click the applicable row to select the subscription that matches the subscription listed in the activation email, and then click Add subscription .
  

  
[Description of the illustration fawag-add-subscription.png](https://docs.oracle.com/iaas/analytics-for-applications/doc/img_text/fawag-add-subscription.html)  

Note  
  
Stop here if you don’t see the subscription that you wish to activate.
- It likely means that you don’t have the OCI_Administrator role or Administrators group (whichever is available) assigned to you. You must contact your cloud account administrator.
- If you’ve been assigned the OCI_Administrator role or are part of the Administrators group, then enter a service request against “Fusion Data Intelligence” in My Oracle Support so that it gets routed to the correct team. For this service request, select Significant Impairment as Issue Type and in Problem Type , click Activate, Create, Delete, Manage FDI Instance and then select FDI Activation . Ensure that you include the account name you're trying to activate into along with a screen shot showing that you’ve been assigned this role in that Cloud account.
- In the Thanks for adding your subscriptions message, click Close .
  

  

It can take upto an hour to receive an email with the subject "Your services are ready!”.
- Open the email that you received from Oracle Cloud stating that your services are ready and click Sign in . Use your Cloud account credentials.
  

  

- In Oracle Cloud Infrastructure Console, click the Navigator menu icon, click Analytics &amp; AI , and then under Analytics &amp; AI, click Data Intelligence .
  

  

- On the Fusion Data Intelligence Instances page, verify that the subscriptions listed in the Compartment banner match your Oracle Fusion Data Intelligence order and the Create Instance button is enabled.

Before you click the Create Instance button, ensure the following:
- You have the User Administrator permission in the domains that you plan to create the Oracle Fusion Data Intelligence instance.
- You set up user access using single sign-on. See[Set Up User Access to Oracle Fusion Data Intelligence Using Single Sign-On](https://docs.oracle.com/iaas/analytics-for-applications/doc/user-access-oracle-fusion-data-intelligence-using-single-sign.html#GUID-8E6311FF-C26F-4BA2-B48F-AFDC150051CE).

Oracle highly recommends that you create an Oracle Fusion Data Intelligence instance integrated with your Oracle Fusion Cloud Applications instance. To create an integrated, see[Create an Integrated Oracle Fusion Data Intelligence Instance](https://docs.oracle.com/iaas/analytics-for-applications/doc/create-integrated-oracle-fusion-data-intelligence-instance.html#GUID-140A5B60-0D6C-4458-9B4F-305647A47327).
- If you run into issues, then enter a service request against “Fusion Data Intelligence” in My Oracle Support so that it gets routed to the correct team. For this service request, select Significant Impairment as Issue Type and in Problem Type , click Activate, Create, Delete, Manage FDI Instance and then select FDI Activation . Prior to creating the service request, ensure that you have noted down the Cloud account, order number, subscription details, and the failed step information.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
