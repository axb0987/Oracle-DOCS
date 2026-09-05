# Data Rules Reference to Customize and Transform Identity and Account Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/transformation-for-inbound-and-outbound-rules.htm
- Fetched: 2026-09-05 03:16 CDT

# Data Rules Reference to Customize and Transform Identity and Account Attributes

You can add rules to customize or transform identity and account attributes. These rules are written in JavaScript.

## Objects
Attribute values for an outbound data transformation can be derived from the following objects:

Objects (Outbound)

Object Name

Purpose

Example

requestAttributes

Provisioning request Attribute Object. These attributes are available when provisioning is via policy based, access bundle request, role based, or direct methods.

`requestAttributes.get('name')`

user

User Object. Use required getter on this to access any member.

`user.getName().getGivenName(), user.getUserName()`

application

Resource Object. Use required getter on this to access any member.

`application.getDisplayName()`
Attribute value for an inbound data transformation can be derived from the following objects:

Objects (Inbound)

Object Name

Purpose

Example

user

User Object. Use required getter on this to access any member for Source of Identity.`user.getName().getGivenName(), user.getUserName()`

account

Account Object. Use required getter on this to access any member for Manage Permissions.`account.getDisplayName()`

## Best Practices to Transform or Customize Identity and Account Attributes

Here are a few best practices and recommendations to consider:
- You can transform or customize identity and account attributes for Inbound data ingested from Authoritative Sources or Managed Systems. However, you can only transform identity (user) attributes for Outbound Data.
- Always perform a NULL check in rules for extracted values before using them otherwise it can lead to ingestion cycle failures on NULL references. This has to be done for both, user attributes object in Authoritative Sources and account attributes object in Managed Systems for inbound transformations.
- You cannot directly transform or assign value to attributes having array object data type, i.e. attributes returning a list of values, such as emails, photos, and addresses, but you can use them to modify/manipulate other user or account attributes. For example, to set the country value as the default value for the attribute location if a location is null, use:
```

```

## Authoritative Source Identity Object Attributes for Outbound Transformation

You can modify or alter the outbound data by applying data transformation rules to the data available or provisioned into the Orchestrated system. Here's a list of identity (user) attributes available for use in outbound data transformations.

### Syntax to Fetch Identity Attributes for Outbound Data

These details can be fetched using the syntax:
```

```

### Retrieve the user's given name
```

```

Identity (User) Object Attributes for Outbound Data
Attribute Sub Attribute Data Type Syntax

name

Reference`user.getName()`

formatted

String`user.getName().getFormatted()`

familyName

String`user.getName().getFamilyName()`

givenName

String`user.getName().getGivenName()`

middleName

String`user.getName().getMiddleName()`

honorificPrefix

String`user.getName().getHonorificPrefix()`

honorificSuffix

String`user.getName().getHonorificSuffix()`

userName

String`user.getUserName()`

displayName

String`user.getDisplayName()`

description

String`user.getDescription()`

primaryEmail

String`user.getPrimaryEmail()`

userType

String`user.getUserType()`

title

String`user.getTitle()`

employeeNumber

String`user.getEmployeeNumber()`

organization

Reference`user.getOrganization()`

value

String`user.getOrganization().getValue()`

ref

String`user.getOrganization().getRef()`

displayName

String`user.getOrganization().getDisplayName()`

resourceType

String`user.getOrganization().getResourceType()`

department

String`user.getDepartment()`

manager

Reference`user.getManager()`

value

String`user.getManager().getValue()`

ref

String`user.getManager().getRef()`

displayName

String`user.getManager().getDisplayName()`

resourceType

String`user.getManager().getResourceType()`

status

String`user.getStatus()`

jobCode

String`user.getJobCode()`

state

String`user.getState()`

risk

String`user.getRisk()`

location

String`user.getLocation()`

emails

List of Email
```

```

pendingVerificationData

String`email.getPendingVerificationData()`

primary

Boolean`email.getPrimary()`

secondary

Boolean`email.getSecondary()`

type

String`email.getType()`

value

String`email.getValue()`

verified

Boolean`email.getVerified()`

addresses

List of Address
```

```

country

String`address.getCountry()`

formatted

String`address.getFormatted()`

locality

String`address.getLocality()`

postalCode

String`address.getPostalCode()`

primary

Boolean`address.getPrimary()`

region

String`address.getRegion()`

streetAddress

String`address.getStreetAddress()`

type

String`address.getType()`

phoneNumbers

List of PhoneNumber
```

```

display

String`phoneNumber.getDisplay()`

primary

Boolean`phoneNumber.getPrimary()`

type

String`phoneNumber.getType()`

value

String`phoneNumber.getValue()`

Boolean`phoneNumber.isVerified()`

## Authoritative Source Identity Object Attributes for Inbound Transformation and Identity Attributes Customization

You can modify or alter the incoming data by applying data transformation rules during the data ingestion phase into the Orchestrated system. You can use the same set of attributes to customize composite identity profile constructed in Oracle Access Governance by transforming identity attributes.

### Syntax to Fetch Identity Attributes for Inbound Data

The attribute details can be fetched using the syntax:
```

```

### Retrieve the user's given name
```

```

Authoritative Source Identity Attributes for Inbound Data
Attribute Sub Attribute Data Type Syntax

fullName (for OIG/ICF)

Reference`user.getFullName()`

formatted

String`user.getFullName().getFormatted()`

familyName

String`user.getFullName().getFamilyName()`

givenName

String`user.getFullName().getGivenName()`

middleName

String`user.getFullName().getMiddleName()`

honorificPrefix

String`user.getFullName().getHonorificPrefix()`

honorificSuffix

String`user.getFullName().getHonorificSuffix()`

name (for OCI)

Reference`user.getName()`

formatted

String`user.getName().getFormatted()`

familyName

String`user.getName().getFamilyName()`

givenName

String`user.getName().getGivenName()`

middleName

String`user.getName().getMiddleName()`

honorificPrefix

String`user.getName().getHonorificPrefix()`

honorificSuffix

String`user.getName().getHonorificSuffix()`

userName

String`user.getUserName()`

displayName

String`user.getDisplayName()`

description

String`user.getDescription()`

primaryEmail

Boolean`user.getPrimaryEmail()`

userType

String`user.getUserType()`

title

String`user.getTitle()`

employeeNumber

String`user.getEmployeeNumber()`

organization

Reference`user.getOrganization()`

value

String`user.getOrganization().getValue()`

ref

String`user.getOrganization().getRef()`

displayName

String`user.getOrganization().getDisplayName()`

resourceType

String`user.getOrganization().getResourceType()`

department

String`user.getDepartment()`

manager

Reference`user.getManager()`

value

String`user.getManager().getValue()`

ref

String`user.getManager().getRef()`

displayName

String`user.getManager().getDisplayName()`

resourceType

String`user.getManager().getResourceType()`

status

String`user.getStatus()`

jobCode

String`user.getJobCode()`

state

String`user.getState()`

risk

String`user.getRisk()`

location

String`user.getLocation()`

compartmentId

String`user.getCompartmentId()`

domainId

String`user.getDomainId()`

domainOCID

String`user.getDomainOCID()`

region

String`user.getRegion()`

emails

List of Email`emails = user.getEmails()`

pendingVerificationData

String`user.getEmails()[0].getPendingVerificationData()`

primary

Boolean`user.getEmails()[0].getPrimary()`

secondary

Boolean`user.getEmails()[0].getSecondary()`

type

String`user.getEmails()[0].getType()`

value

String`user.getEmails()[0].getValue()`

verified

Boolean`user.getEmails()[0].getVerified()`

addresses

List of Address
```

```

country

String`user.getAddresses()[0].getCountry()`

formatted

String`user.getAddresses()[0].getFormatted()`

locality

String`user.getAddresses()[0].getLocality()`

postalCode

String`user.getAddresses()[0].getPostalCode()`

primary

String`user.getAddresses()[0].getPrimary()`

region

String`user.getAddresses()[0].getRegion()`

streetAddress

String`user.getAddresses()[0].getStreetAddress()`

type

String`user.getAddresses()[0].getType()`

phoneNumbers

List of PhoneNumber
```

```

display

String`user.getPhoneNumbers()[0].getDisplay()`

primary

Boolean`user.getPhoneNumbers()[0].getPrimary()`

type

String`user.getPhoneNumbers()[0].getType()`

value

String`user.getPhoneNumbers()[0].getValue()`

Boolean`user.getPhoneNumbers()[0].isVerified()`

photos

List of photos
```

```

display

String`user.getPhotos()[0].getDisplay()`

primary

Boolean`user.getPhotos()[0].getPrimary()`

type

String`user.getPhotos()[0].getType()`

value

String`user.getPhotos()[0].getValue()`

ims

List of ims
```

```

display

String`user.getIms()[0].getDisplay()`

primary

Boolean`user.getIms()[0].getPrimary()`

type

String`user.getIms()[0].getType()`

value

String`user.getIms()[0].getValue()`

## Managed Systems Account Object Attributes for Inbound Transformation

You can modify or alter the incoming account attribute data by applying data transformation rules during the data ingestion phase into the Orchestrated system.

### Syntax to Fetch Account Attributes for Inbound Data Transformation

The attribute details can be fetched using the syntax:
```

```

### Retrieve the user's given name
```

```

Managed Systems Account Attributes for the Inbound Data Transformation
Attribute Sub Attribute Data Type Syntax

fullName

Reference`account.getFullName()`

formatted

String`account.getFullName().getFormatted()`

familyName

String`account.getFullName().getFamilyName()`

givenName

String`account.getFullName().getGivenName()`

middleName

String`account.getFullName().getMiddleName()`

honorificPrefix

String`account.getFullName().getHonorificPrefix()`

honorificSuffix

String`account.getFullName().getHonorificSuffix()`

userName

String`account.getUserName()`

displayName

String`account.getDisplayName()`

description

String`account.getDescription()`

primaryEmail

Boolean`account.getPrimaryEmail()`

userType

String`account.getUserType()`

title

String`account.getTitle()`

status

String`account.getStatus()`

accountType

String`account.getAccountType()`

provisionedByMechanism

String`account.getProvisionedByMechanism()`

provisionedOnDate

String`account.getProvisionedOnDate()`

resourceName

String`account.getResourceName()`

startDate

Long`account.getStartDate()`

name

String`account.getName()`

userLogin

String`account.getUserLogin()`

resourcesId

String`account.getResourcesId()`

compartmentId

String`account.getCompartmentId()`

domainId

String`account.getDomainId()`

domainOCID

String`account.getDomainOCID()`

region

String`account.getRegion()`

emails

List of Email`emails = account.getEmails()`

pendingVerificationData

String`account.getEmails()[0].getPendingVerificationData()`

primary

Boolean`account.getEmails()[0].getPrimary()`

secondary

Boolean`account.getEmails()[0].getSecondary()`

type

String`account.getEmails()[0].getType()`

value

String`account.getEmails()[0].getValue()`

verified

Boolean`account.getEmails()[0].getVerified()`

addresses

List of Address`addresses = account.getAddresses();`

country

String`account.getAddresses()[0].getCountry()`

formatted

String`account.getAddresses()[0].getFormatted()`

locality

String`account.getAddresses()[0].getLocality()`

postalCode

String`account.getAddresses()[0].getPostalCode()`

primary

Boolean`account.getAddresses()[0].getPrimary()`

region

String`account.getAddresses()[0].getRegion()`

streetAddress

String`account.getAddresses()[0].getStreetAddress()`

type

String`account.getAddresses()[0].getType()`

phoneNumbers

List of PhoneNumber`phoneNumbers = account.getPhoneNumbers()`

display

String`account.getPhoneNumbers()[0].getDisplay()`

primary

Boolean`account.getPhoneNumbers()[0].getPrimary()`

type

String`account.getPhoneNumbers()[0].getType()`

value

String`account.getPhoneNumbers()[0].getValue()`

Boolean`account.getPhoneNumbers()[0].isVerified()`

photos

List of photos`photos = account.getPhotos()`

display

String`account.getPhotos()[0].getDisplay()`

primary

Boolean`account.getPhotos()[0].getPrimary()`

type

String`account.getPhotos()[0].getType()`

value

String`account.getPhotos()[0].getValue()`

ims

List of ims`ims = account.getIms()`

display

String`account.getIms()[0].getDisplay()`

primary

Boolean`account.getIms()[0].getPrimary()`

type

String`account.getIms()[0].getType()`

value

String`account.getIms()[0].getValue()`

## Multiple Attribute Rule in Inbound Transformation

Using transformation rules, you can generate unique value and map that generated value to multiple attributes at once in the inbound transformation.

This rule sets description and Building attributes to the`tempName`value. You must remove prior single-attribute rules set for the attributes before using them in multi-attribute rule.
```

```

Using this rule, you can set value for`description`and`building`in a single rule. Select Yes for the Does this rule set multiple attributes? and select the relevant attributes.

Output:
```

```

```

```

## Custom User and Account Attributes

You can fetch and use custom user or account attributes while applying data transformation rules for inbound data transformations. Outbound data transformations allow for fetching custom user attributes only.

### User Custom Attribute

Oracle Access Governance provides a utility method to fetch the custom attribute of a user for inbound or outbound transformations. To fetch the CUSTOM_ATTRIBUTE_NAME of a user, you would use the following syntax, for example:

```

```

For example, for a custom attribute called Tags :

```

```

For a custom attribute of date type:

```

```

### Account Custom Attribute

Oracle Access Governance provides a utility method to fetch the custom attribute of an account for inbound transformations only. To fetch the CUSTOM_ATTRIBUTE_NAME of an account, you would use the following syntax, for example:

```

```

For example, for a custom attribute called Tags :

```

```

## Transformation Utilities for Inbound Data Transformation

Apply utility methods to perform transformation tasks such as validating values, retrieving users, checking attribute availability, and working with lookup mappings. Available only for Authoritative Sources.

Transformation utilities for Inbound Data Transformation
Usecase Utility Method

Get a target lookup code value

`lookupTarget.getLookup('jobCode', user.getJobCode())`

Get a target lookup code object.

Used when`user.getJobCode()`returns a code such as IC0002.`lookupTarget.getLookupObject('jobCode', user.getJobCode())`

Get a target lookup decode object.

Used when`user.getJobCode()`returns a descriptive value such as 'Software Developer'.

`lookupTarget.getLookupObjectByName('jobCode', user.getJobCode());`
Get a global lookup code value`lookupGlobal.getLookup('country', 'US');`
Get a global lookup code object.`lookupGlobal.getLookupObject('country', 'US');`
Check whether a specific value is available for an attribute name. Returns true if the value isn't associated with the specified attribute.`checkValue.IsAvailable('attributeName', 'value')`

For example, check whether the value 'alex@example.com' is already associated with the attribute`primaryEmail`. Returns true if the value isn't currently associated with the specified attribute.

`checkValue.isAvailable('primaryEmail','alex@example.com')`
Checks whether the user's primary email is available for the`primaryEmail`attribute and returns the primary email if available, otherwise returns the display name.
```

```

Check whether a value is null or empty. Returns true if user.getDisplayName() is null or contains an empty value.
```

```

Fetch a user object based on a specific attribute name and value. Returns a User Object.
```

```
For example:
```

```
The returned object attributes can be accessed using Get methods, such as`tempUser.getDisplayName()`,`tempUser.getEmail()`.

## Transformation Utilities for Outbound Data Transformation

A number of utilities are available to assist you in transformation tasks such as checking account existence, getting a user, using lookups, and others.

Transformation utilities
Usecase Utility Method

Fetch a custom attribute for a user.

`transformationUtil.getUserIdentityCustomAttributeValue(agcs_tenant_id, user.getId(), 'CUSTOM_ATTRIBUTE_NAME')`

Get a target lookup code and decode value.

`transformationUtil.getLookupCode(agcs_tenant_id, agcs_target_id, 'countries', user.getAddresses().get(0).getCountry())`

`transformationUtil.getLookupDecode(agcs_tenant_id, agcs_target_id, 'countries', user.getAddresses().get(0).getCountry())`

Get a global lookup code and decode value.

`transformationUtil.getGlobalLookupCode(agcs_tenant_id, 'countries', user.getAddresses().get(0).getCountry())`

`transformationUtil.getGlobalLookupDecode(agcs_tenant_id, 'countries', user.getAddresses().get(0).getCountry())`

Get Value of an attribute from Managed Object filtered on another attribute value.

In this utility, you can get the value of a desired attribute by providing an attribute's Oracle Access Governance name and value to be matched, along with the Oracle Access Governance name of the attribute for which you want to return a value. If there is more than one matching object, or no matches then you will get null.

`transformationUtil.getAttributeValueFromManagedObject(agcs_tenant_id, agcs_target_id, matchAttributeName, matchAttributeValue, returnAttributeName)`

For example: In the following example, by providing fullName as the matching attribute name and Alice Smith as its value, you can get the value of the organizationName from the matched managed object.

`transformationUtil.getAttributeValueFromManagedObject(agcs_tenant_id, agcs_target_id, 'fullName', 'Alice Smith', 'organizationName')`

Check whether an account exists for a given attribute name and value.

`transformationUtil.isAccountExists(agcs_tenant_id, agcs_target_id, matchAttributeName, matchAttributeValue, operator)`

For example: Check to see if an account exists where the attribute name is fullName , the attribute value is Alice Smith , and the operator for the match is eq .

`transformationUtil.isAccountExists(agcs_tenant_id, agcs_target_id, 'fullName', 'Alice Smith', 'eq')`

Get a user from the global identity ID. This will return the user object from which you can then get other attributes.

`transformationUtil.getUser(agcs_tenant_id, 'global_identity_id')`

For example:

```

```

Check if a User has direct reportee(s).

Returns true if the user has one or more reportees, otherwise it returns false .

`transformationUtil.hasDirectReportees(agcs_tenant_id,'global_identity_id')`

## Examples for Outbound Data Transformation

Here are a few sample mapping rules and uses cases while applying outbound data transformations in Oracle Access Governance.

Sample Mapping Rules
Usecase Sample Rule

Fixed string value`'SampleValue'`

User attribute`user.getName().getGivenName()`
Note  
  
You must perform a null check before using such operations as the value can be null.
Date attribute`new Number(new Date().getTime());`

For example, to set the date to 31st Jan 2024:

`new Number(new Date(2024,00,31).getTime());`

Application attribute`application.getDisplayName()`
Note  
  
You must perform a null check before using such operations as the value can be null.

Request attribute`requestAttributes.get('organizationName').get(0)`
Note  
  

- You must perform a null check before using such operations as the value can be null.
- The 'requestAttributes.get(attrName)' always returns an array, so we need to do a get(i) to fetch the specific value
Set value to the combination of 2 user attributes
```

```
or:
```

```

Set the value to another attribute if the input value is null (if organization is null then set to a fixed value)`user.getOrganization() != null && user.getOrganization().getDisplayName() != null ? user.getOrganization().getDisplayName() : 'DefaultOrganization'`

## Examples for Inbound Data Transformation and Identity Attributes

Here are a few sample mapping rules and uses cases while applying inbound data transformations or applying transformations on the composite identity profile in Oracle Access Governance.

Note  
  
As a best practice, we recommend to always perform a NULL check in rules for extracted values before using them otherwise it can lead to ingestion cycle failures on NULL references. This has to be done for both, user attributes object in Authoritative Sources and account attributes object in Managed Systems for inbound transformations.

### Sample Mapping Rules for Authoritative Sources

Here are a few mapping rule expressions along with input value or output value for the identity (user) object attributes.

Target attribute

Type of attribute

Target attribute data type

Aim of mapping rule

Mapping rule expression

Value input

Value output

userName

DEFAULTS

String

Concatenate userName &amp; displayName and set this value in userName attribute`user.getUserName().concat('-',user.getDisplayName())`

userName=mark.hill

displayName=Mark Hill

mark.hill-Mark Hill

userName

DEFAULTS

String

If userName is not null, then convert userName to upperCase and set in userName attribute`if(user.getUserName()!=null) {user.getUserName().toUpperCase() }`

userName=mark.hill

MARK.HILL

jobDescription

CUSTOM

String

LowerCase the value of description and set it in custom attribute, jobDescription`user.getDescription().toLowerCase()`

description = SoftwareDeveloper1

jobDescription = softwaredeveloper1

status

DEFAULTS

Boolean

If status is null set it to true else alternate the value.`user.getStatus()==null ? true : !user.getStatus()`status = true false

risk

DEFAULTS

Integer If risk is null set 20, else increase risk by 15`user.getRisk() == null ? 20 : user.getRisk() + 15`

risk = 30

risk = null

45

20

description

DEFAULTS

String

Get startDate of type long, convert it into Date and then set it as a String to the description attribute.`new Date(user.getStartDate()).toISOString()`startDate = 1703442600000

2023-12-25T07:55:46.061Z

provisionedOnDate

DEFAULTS

Date

Get validFromDate (long), convert to date, then set provisionedOnDate rounded to 1st of next month.`const currentDate = new Date(user.getValidFromDate()); new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1).getTime();`

validFromDate = 1703442600000

provisionedOnDate = 1704047400000

provisionedFromDate

DEFAULTS

Date

Input type string. Output type date. new Date(user.getValidFromDate()).toISOString()

validFromDate = 1703442600000

input = 2023-12-24T18:30:00.000Z provisionedFromDate = 1703422800000

### Sample Mapping Rules for Managed Systems

Here are a few mapping rule expressions along with input value or output value for the account object attributes.

Sample Mapping Rules for Managing Permissions

Target attribute

Type of attribute

Target attribute data type

Aim of mapping rule

Mapping rule expression

Value input

Value output

displayName

DEFAULTS

String

If displayName is not null then set upper case value to displayName.`if(account.getDisplayName()!=null) {account.getDisplayName().toUpperCase() }`

displayName = Mark Hill

MARK HILL

primaryEmail

DEFAULTS

String

Concatenate userLogin &amp; "@myexample.com" and set in primaryEmail.`account.getUserLogin().concat('@myexample.com')`userLogin = mark.hill mark.hill@myexample.com

jobDescription

CUSTOM

String

LowerCase the value of description and set it in custom attributes jobDescription.`if(account.getDescription()!=null) { account.getDescription().toLowerCase() }`description = SoftwareDeveloper1 jobDescription = softwaredeveloper1

status

DEFAULTS

Boolean

Example 1: If status is null then set it to true else alternate the value.`account.getStatus()==null ? true : !account.getStatus()`

status = true

false

Example 2: Set status to false.`false`status = null/true/false false

risk

DEFAULTS

Integer

If risk is null then set to 20, else increase risk by 15.`account.getRisk() == null ? 20 : account.getRisk() + 15`

risk = 30

risk = null

45

20

riskSummary

DEFAULTS

Long

If riskSummary is null set to 1234, else increase risk by 70.`account.getRiskSummary() == null ? 1234 : account.getRiskSummary() + 70`

riskSummary = 30

riskSummary = null

100
