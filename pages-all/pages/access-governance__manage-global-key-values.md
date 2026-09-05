# Manage Global Key-Values
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-global-key-values.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Global Key-Values

## Normalise Key-Values Across Orchestrated Systems

Global Key-Values allow you to normalise attribute values across orchestrated systems by providing key-value pairs that can be utilized by in-bound and out-bound transformations, and in account attributes. This allows you to standardize attribute values across your enterprise for items such as country code.
Global Key-Values is a feature which allows you to load a CSV file containing key/value pairs and make them available to:
- In-bound transformations
- Out-bound transformations
- Account attributes

For example, you might have a requirement to standardize country codes according to the ISO alpha-2 and ISO alpha-3 standards. Global Key-Values allow you to set a lookup for each of these 2 and 3 digit codes together with the corresponding country name (e.g. US , USA , United States of America ). When populating an account attribute or setting values via an in-bound or out-bound transformation, you can utilize these Global Key-Values to maintain consistency across your enterprise.

## Create a Global Key-Value

Create a Global Key-Value by uploading a CSV file with key/value pairs into Oracle Access Governance

To create a Global Key-Value, perform the following steps:

- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Global Key-Values page by clicking on the icon, then select Service Administration → Global Key-Values . The page will display any existing Global Key-Values that have been setup previously.
- Select Create global key-values to add a new global key-value definition.
- In the Create global key-values pop-up enter the following values for the Global Key-Value required.
- Name : The name of the Global Key-Value you are creating, for example CountryCodeISO2 .
- Description : A description for the Global Key-Value you are creating, for example ISO alpha-2 country codes
- Select a file : Select a CSV file containing the key/value pairs you want to create for this Global Key-Value. An example for the ISO2 example might include:
```

```

The CSV file you upload should comply with the following requirements:
- Files should be UTF-8 encoded
- Keys must be unique
- The string length of keys and values must both be less than 256 characters
- Key/value pairs cannot exceed 10k
- Click Create to save the Global Key-Value.

## View Details of a Global Key-Value

You can view the details of your Global Key-Value using the Oracle Access Governance Console.

To view details of a Global Key-Value, perform the following steps:

- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Global Key-Values page by clicking on the icon, then select Service Administration → Global Key-Values . The page will display any existing Global Key-Values.
- Select the Global Key-Value that you want to manage and select View Details .
- Details of the status and values assigned to the Global Key-Value are displayed.
- You have the option to export the key/value pairs by selecting the button.

## Edit Details of a Global Key-Value

Edit details of your Global Key-Value using the Oracle Access Governance Console.

To edit a Global Key-Value, perform the following steps:

- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Global Key-Values page by clicking on the icon, then select Service Administration → Global Key-Values . The page will display any existing Global Key-Values.
- Select the Global Key-Value that you want to manage and select Edit .
- In the Edit global key-values pop-up amend the following values for the Global Key-Value as required.
- Name : The name of the Global Key-Value you are creating, for example CountryCodeISO2 .
- Description : A description for the Global Key-Value you are creating, for example ISO alpha-2 country codes
- Select a file : Select a CSV file containing the key/value pairs you want to create for this Global Key-Value. You might want to amend the CSV file to add updates to the key/value pairs, or you may need to reload a CSV file when you have had a failure during creation of the Global Key-Value and the status is set to Failed .
- Make your changes and click Update to save the Global Key-Value.

## Delete a Global Key-Value

Delete a Global Key-Value using the Oracle Access Governance Console.

To delete a Global Key-Value, perform the following steps:

- In your browser, navigate to the Oracle Access Governance service home page, and login as a user with the Administrator application role.
- Navigate to the Global Key-Values page by clicking on the icon, then select Service Administration → Global Key-Values . The page will display any existing Global Key-Values.
- Select the Global Key-Value that you want to delete and click on the actions menu. Select Delete .
- Confirm your deletion in the pop-up by selecting Delete
Note
