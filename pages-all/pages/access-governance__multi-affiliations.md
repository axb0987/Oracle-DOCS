# Handling Identity Personas with Affiliations
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/multi-affiliations.htm
- Fetched: 2026-09-05 03:15 CDT

# Handling Identity Personas with Affiliations

Affiliations in Oracle Access Governance allow a single identity to have multiple persona within the organization, each tied to their own data, accounts, and access. It's made of one or more simple or complex attributes recognized by the Authoritative source system.

## Affiliations Overview

Affiliations allow administrators to define new affiliation attributes by mapping specific identity attributes and then using scripts to create derived values from the source system.

In many large organizations (for example, universities, government), a single identity (person) may have multiple roles or affiliations, such as being a student and a faculty member, or holding two distinct jobs (for example, nurse and home health worker). Each affiliation may require different accounts/access and must be managed separately.

Affiliations help to flatten and segregate complex, array-based attribute data, such as`jobData`, so each affiliation and its related attributes become easy to handle for provisioning and reporting to connected Managed Systems.

Affiliations also provide a mechanism to expose individual child attributes from complex attributes by defining corresponding affiliation attributes. Through affiliation rules, you can map values from the complex attribute to specific affiliation attributes. Furthermore, usage flags can only be updated and managed on these affiliation attributes.

Applies to :[Peoplesoft](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-peoplesoft.htm),[Flat File](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-identity-schemaextension),[DBAT](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbataffiliations), and all Authoritative Sources.

## Multiple Affiliation Process Flow

Here's how you can configure and use affiliations at a high-level:

For step-wise workflow to configure affiliations, see[Configure and Manage Affiliations](https://docs.oracle.com/en-us/iaas/Content/access-governance/affiliations-configure-affiliations.htm)

- Choose the orchestrated system for which you want to define affiliation.
- (Optional) Create complex identity attributes that you want to support.
- Add affiliation details by providing meaningful name.
- Include the child identity attributes in the affiliations.
- Add Rules using functions, such as`user.get`to provide the source value.
- Validate and submit affiliations.
- Perform full data load.
- Enable Identity Flags for Affiliations from the Identity Attributes page.
- Verify identity attributes in the Enterprise-wide Browser.

## Affiliations Example

Let's see an end-to-end example of how affiliations work, using a scenario to understand how the system processes affiliations from creation to the final attribute mapping.
Perform full data load for the orchestrated system.
Scenario

At a large university, a person named Alex is both:
- A graduate student at the engineering campus
- A part-time instructor in the business school

Alex needs different types of access and accounts for each of these roles. For example:
- Student : Library access, Student email, Course registration
- Instructor : Faculty email, Grading system access, departmental resources In the source system, here's how Alex's jobData looks:
```

```

Step 1: Affiliation Builder Setup As an administrator, create two affiliations for this scenario:
- PrimaryJobAffiliation: filters where`employeeRecord == '0'`(Graduate Student)
- SecondaryJobAffiliation: filters where`employeeRecord == '1'`(Instructor)

Step 2: Add Attributes in the Affiliations
Include the following attributes both the affiliations:
- jobType
- department
- company
- fullPartTime
- emplStatus
- supervisorUid
- lastUpdateTimestamp

Step 2: Define Script for Extracting Jobs

The below script retrieves job-related data from a identity's custom attributes and maps it into variable PrimaryJobAffiliation or SecondaryJob1Affiliation based on employee record number.
```

```
Viewing Affiliations Identity Attributes
In the Enterprise-wide Browser, Alex’s identity profile after mapping, looks like:
- PrimaryJobAffiliation.jobType: Graduate Student
- PrimaryJobAffiliation.company: University
- PrimaryJobAffiliation.supervisorUid: dr_brown
- SecondaryJobAffiliation.department: Business School
- SecondaryJobAffiliation.jobType: Instructor
- SecondaryJobAffiliation.company: University
- SecondaryJobAffiliation.supervisorUid: prof_wilson
