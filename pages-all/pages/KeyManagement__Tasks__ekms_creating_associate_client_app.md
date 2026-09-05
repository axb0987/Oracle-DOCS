# Associating Confidential Client Application
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_associate_client_app.htm
- Fetched: 2026-09-05 02:34 CDT

# Associating Confidential Client Application

Learn how to associate a confidential client application with a resource application.

To configure authorization, you must associate the confidential client application with confidential resource application.

Complete the following steps to configure the association:

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the Default domain.
- Select Integrated Applications .
- Select Add application .
- In the Add application panel, select Confidential Application .
- Select Launch Workflow .
- In the Add Confidential Application page, provide the following details:

- Name: Enter the name of the confidential client application.
- Description: Enter a short description about the client application.
- Select Next .
- In the Configure Auth page, provide the following details.

- Client Configuration. Select the Configure the client as an application now option.
- Client Credentials. Under Authorization section, select the Client Credentials checkbox.
- Add resources. Under Token issuance policy , select Add resource checkbox.
- Add Scope. Under Resources , select Add Scope to select and add an existing scope.
- After adding, the scopes are now associated with the client application.
- Select Next and then Finish .
