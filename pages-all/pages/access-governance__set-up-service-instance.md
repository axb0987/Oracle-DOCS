# Set up Service Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-service-instance.htm
- Fetched: 2026-09-05 03:16 CDT

# Set up Service Instance

You can create an Oracle Access Governance instance in the Oracle Cloud Infrastructure Console. The steps below show you how to create an instance and verify its operation.

Note  
  
Oracle Access Governance is available in all the regions of the commercial realm. Full details about the regions can be referred to at[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

## Prerequisites

Create and set up an Oracle Access Governance service instance and manage the agcs-instance resource.

The Oracle Cloud Infrastructure Identity and Access Management administrator or domain administrator must perform the following operations:

- To create Oracle Access Governance service instance, create a group and allow group permissions:
```

```

```

```

- To update or delete an Oracle Access Governance service instance, create a group and allow that group permissions:
```

```

Note  
  
The Oracle Access Governance service instance must be created in your Home Region. If you try to create the instance outside your Home Region, the setup will fail. For more details, see[Tenancy Home Region](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How).

### Setup Policies for Tenancies using Identity Domains

Lists the required policies to create Oracle Access Governance an service instance.

#### Tenancy Admin
```

```

#### Compartment Admin
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance.
```

```

#### Manage agcs-instance in tenancy
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance
```

```

#### With ‘manage agcs-instance’ in a compartment
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance
```

```

### Setup Policies for Tenancies NOT using Identity Domains

Lists the required policies to create an Oracle Access Governance service instance with tenancies not using Identity Domains.

#### Tenancy Admin
```

```

#### Compartment Admin
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance
```

```

#### Manage agcs-instance in tenancy
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance.
```

```

#### With ‘manage agcs-instance’ in a compartment
- Add the following policy statement in the root compartment of your tenancy. This will fetch the tenancy namespace to create a service instance.
```

```

- Add the following policy statement in the compartment where you want create the service instance
```

```

## Create Service Instance

Create an Oracle Access Governance instance in the Oracle Cloud Infrastructure console.
You can create an Oracle Access Governance service instance using the following steps:

- Open your web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of your Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Click Sign In .
- When you have successfully logged in, click the icon in the top left corner to display the navigation menu.
- Click Identity and Security in the navigation menu.
- Select Access Governance from the list of products.
- On the Service Instances page, click the Create service instance button.
- Enter values for the service instance as detailed in the following table .

Parameter Value Description
Name Name of the service instance.
Description Description of the service instance.
Create in compartment Compartment Name into which the service instance will be created. Name of the OCI compartment into which the service instance will be created.
License type

Select from the following license types:

- Access Governance Premium : Governance of access privileges for Oracle and Non-Oracle Workloads running anywhere
- Access Governance for Oracle Workloads : Governance of access privileges for Oracle Workloads running anywhere
- Access Governance for Oracle Cloud Infrastructure : Governance of access privileges for OCI resources and services.

Access Governance for OCI is the entry level license option, covering OCI in cloud environments. Access Governance for Oracle Workloads is a broader option, covering Oracle Workloads running anywhere, and includes OCI. Access Governance Premium is the widest option, including non-Oracle as well as Oracle workloads.

When you select a license option, be aware that it may take approximately 10 minutes before the licence is enabled on your service instance.
Tagging Tags allow you to organize and track resources within your tenancy. If you want to tag resources within the service instance, add them here. Add value as described in the following rows. If you want to add additional tags, select Another Tag to create more.
TAG NAMESPACE Namespace to which the tag applies.
TAG KEY Key for the tag.
TAG VALUE Value of the tag.
- To create the service instance with the value you have input, select Create service instance . If you don't want to proceed with the service creation, select Cancel .

## Verify Service Instance

You can verify an Oracle Access Governance service instance using the following steps:

- Open the web browser and navigate to[https://cloud.oracle.com](https://cloud.oracle.com).
- Enter the name of your Cloud Account Administrator in the Cloud Account Name field and click Next .
- On the Cloud Infrastructure sign-in page, enter your sign-in credentials under Oracle Cloud Infrastructure Direct Sign-In . Click Sign In .
- Click the icon in the top left corner to display the navigation menu.
- Click Identity and Security in the navigation menu
- Select Access Governance from the list of products.
- On the Service Instances page, select the newly created service instance.
- Click Service Home Page to access the Oracle Access Governance Console in a browser.

The Oracle Access Governance Home page should look similar to below. Depending on the application roles assigned to your user, you will see the following tabs:  

  

- My Stuff
- Access Controls
- Access Reviews
- Who Has Access to What
- Service Administration
