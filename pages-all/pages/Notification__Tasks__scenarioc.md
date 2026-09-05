# Scenario C: Filing Jira Tickets for Reminders
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm
- Fetched: 2026-09-05 02:49 CDT

# Scenario C: Filing Jira Tickets for Reminders

Automatically file a Jira ticket whenever a maintenance reminder event occurs. In this scenario, whenever a reminder for upcoming database maintenance comes from Oracle Cloud Infrastructure, a Jira ticket is created for the on-call engineer.

This scenario involves writing a[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)to file[Jira](https://www.atlassian.com/software/jira)tickets (and creating a[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)to store Jira credentials), adding that function and optional email as subscriptions to a topic , and creating a[rule](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm)that sends messages to that topic when maintenance reminder events occur (see[Autonomous Container Database Event Types](https://docs.oracle.com/en/cloud/paas/autonomous-database/arfad/index.html#ARFAD-GUID-99243E04-1089-4801-95DE-4D68C15E726A)). The message fans out to the topic's subscriptions, which includes a group email address in addition to the function. The function is invoked on receipt of the message.

Everything but the function can be set up in the Console. Alternatively, you can use the Oracle Cloud Infrastructure CLI or API, which lets you run the individual operations yourself.
Note  
  

The Notifications service has no information about a function after it's invoked. For details, see the troubleshooting information in[Function Not Invoked or Run](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/troubleshootingnotifications.htm#fxno).

[

For more information about this scenario, see[Automated Jira Ticketing using OCI Events, Notifications, and Functions](https://blogs.oracle.com/cloud-infrastructure/automated-jira-ticketing-using-oci-events,-notifications,-and-functions)and[the associated GitHub repository](https://github.com/mayur-oci/oci_fn_jira_integration).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're a member of the Administrators group, you already have the required access to execute this scenario. Otherwise, you need access to[Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm#authenticate),[Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Authenti), and[Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm#requiredpolicy). You must have`FN_INVOCATION`permission against the function to be able to add the function as a subscription to a topic. To access your Jira credentials, the function must be authorized to read secrets. This scenario walks through[steps to provide this authorization](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#createfunction).

## Task 1: Store Credentials in a Secret

For more information about creating secrets using the Vault service, see[Creating a Secret in a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Vault .
- Under List Scope , in the Compartment list, select the name of the compartment where you want to create a secret.
- 

From the list of vaults in the compartment, do one of the following:
- 

Select the name of the vault where you want to create a secret.
- 

Create a new vault for the secret by following the instructions in[To create a new vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm), and then select the name of the vault.
- Select Secrets , and then select Create Secret .
- In the Create Secret panel, choose a compartment from the Create in Compartment list. (Secrets can exist outside the compartment the vault is in.)
- 

Enter a Name to identify the secret. Avoid entering confidential information.

Example name:`jira_auth_plain_text`
- Enter a brief Description of the secret to help identify it. Avoid entering confidential information.

Example description:`jira_auth_plain_text`
- Choose the master encryption key that you want to use to encrypt the secret contents while they're imported to the vault. (The key must belong to the same vault.)
- For Secret Type Template , select Plain-Text .
- For Secret Contents , enter your Jira credentials in the following format, with a colon separating your login email from your auth token:

&lt;your-jira-cloud-login-email&gt; : &lt;your-jira-cloud-auth-token&gt;
- Select Create Secret .
- Note the secret OCID for use in your function code to securely fetch the secret.
- 

Note  
  
You must specify a symmetric key to encrypt the secret during import to the vault. You cannot encrypt secrets with asymmetric keys. Furthermore, the key must exist in the vault that you specify.

Use the`oci vault secret create-base64`command and required parameters to create a secret storing your Jira credentials:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSecret](https://docs.oracle.com/iaas/api/#/en/secretmgmt/latest/Secret/CreateSecret)operation to create a secret.

Example:
```

```

Note  
  
Each region has a unique endpoint for create, update, and list operations for secrets. This endpoint is referred to as the control plane URL or secret management endpoint. Each region also has a unique endpoint for operations related to retrieving secret contents. This endpoint is known as the data plane URL or the secret retrieval endpoint. For regional endpoints, see the[API Documentation](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Task 2: Create the Function

This section provides the code sample for[creating your function](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm)and covers steps to authorize the function to access your Jira credentials in the secret created using the Vault service.

[Function code sample](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)

The following code sample is for a function to file Jira tickets.

Add your secret OCID in the line that includes`getSecretForOcid`.

For instructions on creating and deploying functions, see[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm).

```

```

[Authorize your function to access secrets](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)

Use a dynamic group to grant your function the ability to read secrets. Your function must have this authorization to access your Jira credentials, which are stored in[the secret you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#store-credentials).

[To authorize your function to access secrets (Console)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)

- Find and note your function OCID (format is`ocid1.fnfunc.oc1.iad.exampleuniqueID`).
- Include your function in a dynamic group: In the relevant dynamic group , specify the following rule:

```

```

Alternatively, you can create a dynamic group that includes all functions:
```

```

- Grant the dynamic group access to secrets: Add the following policy :

```

```

To authorize your function for access to other Oracle Cloud Infrastructure resources, such as compute instances, include the function in a dynamic group and create a policy to grant the dynamic group access to those resources. For more information, see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm).

For more information about dynamic groups, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).

## Task 3: Create the Topic

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- 

- Open the Create Topic panel: On the Topics list page, select Create topic . If you need help finding the list page, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- For Name , type the following: Maintenance Topic
- Select Create .
- 

Use the[oci ons topic create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/create.html)command and required parameters to create a topic:

```

```

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateTopic](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/CreateTopic)operation to create a topic.

Example:
```

```

## Task 4: Create the Subscriptions

Your function must be deployed before creating the function subscription.

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- 

- Select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#create-topic)(example name was Maintenance Topic ): On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- Create the function subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Function .
- Fill in the remaining fields.

Field Description
Function Compartment Select the compartment containing the function.
Function Application Select the application containing the function.
Function Select the function.
- Select Create .
No confirmation is needed for new function subscriptions.
- Create the email subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Email .
- Fill in the remaining fields.

Field Description
Email Type an email address.
- Select Create .
- [Confirm the new email subscription:](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)Open the email and navigate to the confirmation URL.
- 

Note  
  
After creating the email subscription,[confirm it](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create each subscription:

```

```

Function subscription example:

```

```

Email subscription example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Note  
  
After creating the email subscription,[confirm it](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create each subscription.

Function subscription example:
```

```

Email subscription example:
```

```

## Task 5: Create the Event Rule

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioc.htm#)
- 

This section walks through creating the rule that sends a message to the topic whenever the Database service emits an event for a database maintenance reminder.
- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- Choose a Compartment you have permission to work in, and then select Create Rule .

Events compares the rules you create in this compartment to event messages emitted from resources in this compartment and any child compartments.
- Enter the following.
- 

Display Name: Specify a friendly name for the rule. You can change this name later. Avoid entering confidential information.

Example: Maintenance Reminder
- Description: Specify a description of what the rule does. You can change this description later. Avoid entering confidential information.

Example: Sends messages to Maintenance Topic
- In Rule Conditions , create a filter for database reminder events:

- For Service Name , select Database .
- In Event type , select Autonomous Container Database – Maintenance Reminder .
- In Actions , select the topic you previously created:
- Select Notifications .
- Select the Notifications Compartment .
- Select the Topic that you previously created.
- Select Create Rule .
- 

Create a rule that's triggered by maintenance reminders and references this topic as the destination.
- 

Create a file,`action.json`, that contains the following, referencing your topic created previously.

Example:

```

```

- 

Open a command prompt and run the`oci events rule create`command.

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

For more information about creating rules using the CLI, see[Creating an Events Rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm).
- 

Run the[CreateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/CreateRule)operation to create an event rule.

Example:
```

```
