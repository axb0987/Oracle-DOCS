# Granting Birthright Access
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm
- Fetched: 2026-09-05 03:13 CDT

# Granting Birthright Access

Birthright access refers to a set of default permissions automatically granted to users using Oracle Access Governance automated policies to ensure new joiners have essential access before or at the start of employment.
Oracle Access Governance grants birthright access to
- Prehire : Start date is in the future.
- Hire : Start date is now or in the past; not terminated.

Employee State AG Status Status (from Authoritative Source) Join Date (from Authoritative Source) Termination Started Termination Date (from Authoritative Source)
Prehire AG Active Disabled Greater than today FALSE Greater than today
Hire AG Active Active Less than or equal to today FALSE Greater than today

## Prerequisites

Ensure the following prerequisites to grant birthright access from Oracle Access Governance:
- 
- The Authoritative source must include employee attributes, including the official Joining date or Start date
- [Create system attribute and global identity attribute to fetch source value](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm#birthright-prereqs__system-global-attribute).
- The Authoritative source must include termination date or last working date orchestrated system attribute.
- [Create a global AG identity attribute`terminated`](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm#birthright-prereqs__global-terminated-attribute)
- [Set Workforce/Consumer conditions for activation](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm#birthright-prereqs__worforce-consumer-active-rules)

### Step 1: Create System Attribute and Global Identity Attribute for JoinDate
- Create a simple system attribute`joinDate`and map it to the joining date source, such as`startDate`. See[Create System Attribute](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#system-attribute).
- Now, go to the Identity Attributes page and search`joinDate`core identity attribute. Edit the core identity attribute to select the relevant orchestrated system and update the Value source with a single attribute rule, such as:
```

```
See[Manage Attributes Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).

### Step 2: Create a Global Identity Attribute to Exclude Terminated Users

Create an AG Attribute,`terminated`, for policies that grant birthright access before the`joinDate`to exclude terminated users from being assigned permissions through these policies. Here`terminationDate`is the last working date source from the Authoritative source.
- 
- Go to the Identity Attributes page and create an internal AG Attribute, terminated , of type Boolean . For details, see Create an Oracle Access Governance Attribute.
- Use the single attribute rule to compare`terminationDate`with today. If`terminationDate`is less than or equal to today, it returns true; otherwise, it returns false, such as:
```

```

- Select appropriate identity flags to include this attributes in the Oracle Access Governance features

### Step 3: Configure Workforce/Consumer Activation Rules
Go to the Manage Identities page and set the following activation rules:
- For Active users:
```

```

- For Consumer users:
```

```

## Birthright Access Workflow

You can configure birthright access from Oracle Access Governance by creating identity collections, packaging permissions in an access bundle, and then configuring policies to ensure new hires have essential access before or at the start of employment.
- Create an Identity Collection based on membership rules. See[Create an Identity Collection](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm).
- For users to grant access on or after start date.
```

```

- For pre-hires to grant access before the start date
```

```

Note  
  

- To grant access on or after the start date, you must add a condition`Status Equals Active`.
- If you configured the policy using`today()`, then each day, an in-house scheduler adds new member who meet the membership criteria. Based on the configuration, the policy is triggered every day at midnight.
- Create an Access Bundle and package access to necessary permissions. For example, access to default collaboration tools. See[Create an Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- Create a policy and associate the permissions part of the access bundle with identity collection. See[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm).

## Pre-hire Example

Let's understand complete birthright access workflow for pre-hires, where access should be granted before the start date.

Alice is expected to join Acme Corporation on March 20 . As an`AG_Administrator`and`AG_AccessControl_Admin`, grant the following:
- 
- Ensure you configure the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/access-governance/birthright-access.htm#birthright-prereqs)to activate workforce rules and ingest start date in the joinDate core attribute.
- Create an identity collection with the membership rule:
```

```

- Package permissions in an access bundle for the default collaboration or enterprise tools. You can further configure to ensure No one can request this access bundle and should be granted only using policy.
- Create a policy and associate the permissions part of the access bundle with identity collection.

For Alice, if join date is March 20 , the policy is triggered on March 10 to grant birthright access.

## Validating the Configuration

Verify if the set up is correct.
- From System Administration , select Identity Attributes , and then enable Include in identity details and Include in manage identities flag for the following identity attributes:`status`,`startDate`,`joinDate`,`terminated`,`terminationDate`, and`terminationStarted`.
- From Who has access to what , select Enterprise wide browser , select identities, select Edit list settings , and then add the following attributes to the list settings:`status`,`startDate`,`joinDate`,`terminated`,`terminationDate`, and`terminationStarted`.
- Validate the following for identities loaded from the Authoritative Source system:
- The`startDate`and`joinDate`attributes must be set to the same value.
- Identities with a`startDate`in the future and a`terminationDate`that's not set or is in the future must have the following values:
- `status`=`Disabled`
- `AG status`=`Active`
- `AG subtype`=`Consumer`
- `terminated`=`false`
- Identities with a`startDate`in the past and a`terminationDate`that's not set or is in the future must have the following values:
- `status`=`Active`
- `AG status`=`Active`
- `AG subtype`=`Workforce`
- `terminated`=`false`
- Identities with a`terminationDate`in the past must have the following values:
- `status`=`Disabled`
- `AG status`=`Active`or`Inactive`(depends on how the group is configured; if these are Oracle Access Governance Active identity collections for pre-hire policies, then it must have the`terminated`=`false`condition)
- `AG subtype`=`Consumer`(if these identities are loaded to Oracle Access Governance, then it must be f type Consumers )
- `terminated`=`true`
