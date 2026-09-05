# Getting Started with Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventsgetstarted.htm
- Fetched: 2026-09-05 02:01 CDT

# Getting Started with Events

Learn about how to create automation with the Events service.

You can create a simple rule that sends a notification whenever someone creates a bucket in a particular compartment in your tenancy.

## Setting Up for Events

To try out the Events service for this tutorial, you must have these things set up first:
- Create IAM policy for Events
- [Create a topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-topic.htm)and[subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription.htm)to use as an action
Important  
  
A tenancy administrator must configure your tenancy for Events. These configurations give you access to an Oracle Cloud Infrastructure tenancy with the necessary IAM policy and a resource to use as an action.

### Create Users, Groups, and Compartments

You can use existing users, groups, and compartments or make new ones.

#### To create groups and users

If suitable users and groups for assigning users permissions to work with rules don't already exist, log in to the Console as a tenancy administrator and create them.
- Log in to the Console as a tenancy administrator.
- If you need a group for Events, perform these steps:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . A list of the groups in your tenancy is displayed.
- Select &lt;your-tenancy-name&gt; . The tenancy details are displayed.
- Select the User Management tab.
- Scroll down to Groups .
- Select Create Group and create a new group (see[Creating a Group](https://docs.oracle.com/iaas/Content/Identity/groups/create-groups.htm)). Give the group a meaningful name and description. Avoid entering confidential information.
- If you need user accounts for Events, perform these steps:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . A list of the groups in your tenancy is displayed.
- Select &lt;your-tenancy-name&gt; . The tenancy details are displayed.
- Select the User Management tab.
- Select Create User and create one or more new users (see[Creating a User](https://docs.oracle.com/iaas/Content/Identity/users/create-user-accounts.htm)).
- If users haven't been added to groups already, perform these steps:
- Select the group you want to use for Events.
- Select the Users tab.
- Select Assign User to Group .
- Select the users from the drop-down list, and then select Add .

#### To create a compartment

If suitable compartment for rules and the resources that emit events doesn't already exist, log in to the Console as a tenancy administrator and create it.
- Log in to the Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Compartments . A list of the compartments in your tenancy is displayed.
- Select Create Compartment and create a new compartment (see[Creating a Compartment](https://docs.oracle.com/iaas/Content/Identity/compartments/To_create_a_compartment.htm)). Give the compartment a meaningful name and description. Avoid entering confidential information.

### Create IAM Policy for Events

Before users can start using Events to create automation, as a tenancy administrator you must create IAM policy:

#### To create a policy that allows users to create and manage rules
- Log in to the Console as a tenancy administrator.
- In the Console, Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies .A list of the policies in the compartment you're viewing is displayed.
- Select the root compartment.
- Select Create Policy .
- Enter the following:
- Name: A meaningful name for the policy. The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A meaningful description. You can change this later if you want to.
- Compartment: Select a compartment.
- Select Show manual editor .
- 

Enter the following policy statements to give users in the group the ability to manage and create rules:

This line gives the user inspect access to resources in compartments to select actions.

```

```

This line gives the user access to defined tags to apply filter tags to rules.

```

```

These lines give the user access to Streaming resources for actions

```

```

These lines give the user access to Functions resources for actions.

```

```

This line give the user access to Notifications topics for actions.

```

```

This line gives the user manage access to rules for Events.

```

```

- Select Create .

### Create Notifications Topic and Subscription

If a suitable Notifications topic doesn't already exist, then you must log in to the Console as a tenancy administrator and create it. Whether you use an existing topic or create a new one, add an email address as a subscription so that you can monitor that email account for notifications.

#### To create a topic
- Open the navigation menu and select Developer Services . Under Application Integration , select Notifications .
- Select Create Topic at the top of the topic list.
- In the Create Topic panel, configure your topic.
- Name: Required. Specify a friendly name for the topic. It must be unique; validation is case-sensitive. Avoid entering confidential information.
- Description: Optional. Enter a description for the topic.
- Compartment: Select a compartment.
- Select Create .

#### To create a subscription
- Open the navigation menu and select Developer Services . Under Application Integration , select Notifications .
- Select Subscriptions .
- Select Create Subscription .
- Select the name of the topic that you created in the previous step or the topic you intend to use for this tutorial.
- In the Create Subscription panel, select Email , and then type an email address.
- Select Create .

The subscription has been created and a subscription confirmation URL will be sent. The subscription remains in "Pending" status until it has been confirmed.

#### To confirm a subscription
- In the confirmation email sent to the address you specified in the previous procedure, click the confirmation URL.

## Using the Console to Create a Rule

Use the Console to create a rule with a pattern that matches bucket creation events emitted by Object Storage. Specify the Notifications topic you created as an action to deliver matching events. To test your rule, create a bucket. Object Storage emits an event which triggers the action. Check the email specified in the subscription to receive your notification.

### Creating a Rule

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- Select a Compartment you have permission to work in, and then select Create Rule .

Events compares the rules you create in this compartment to event messages emitted from resources in this compartment and any child compartments.
- Enter the following.
- Display Name: Specify a friendly name for the rule. You can change this name later. Avoid entering confidential information.
- Description: Specify a description of what the rule does. You can change this description later.
- In Condition , select Event Type .
- In Service Name , select Object Storage .
- In Event Type , select Bucket - Create .
- In Actions , specify the actions to trigger when the filter finds a match:
- In Action Type , select Notifications .
- In Notifications Compartment , select the compartment that contains the topic.
- In Topic , select the topic.
- Select Create Rule .

### Create a bucket

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Select the compartment where you created your rule (or any of its subordinate compartments).
- Select Create Bucket .
- In the Create Bucket dialog, specify the attributes of the bucket:
- Name : Required. A user-friendly name or description. Avoid entering confidential information.
- 

Storage Tier : Select the tier in which you want to store your data. Available tiers include:
- Standard is the primary default Object Storage tier for storing data that is accessed frequently and requires fast and immediate access.
- Archive is a special tier for storing data that is accessed infrequently and requires long retention periods. Access to data in the Archive tier is not immediate. You must restore archived data before it's accessible. For more information, see[Overview of Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm).
- Select any other special setting avaialble for the bucket.
- Select Create .

### Retrieving Your Notification

- 

Log in to the email account you specified in the previous procedure to receive the notification about the bucket being created.

[
Tip  
  
You will receive notifications each time a bucket is created in the compartment (or any of its sub compartments) until you disable the rule.

## Using the CLI to Create a Rule

When you use the CLI to create a rule, you work a little differently than using the Console.
- To specify the actions for your rule, use a JSON formatted file. You create this file before you create the rule, and the file simplifies the amount of information you must type at the command line.
- To specify an event to match, use a JSON formatted string. You type this right into the console as you create the rule.

### Creating an Action File

- Create a file and add the following content.

```

```

Tip: You can specify functions, streams, or topics as an action.

Example action file template

```

```

- Fill in &lt;topic_OCID&gt; with actual topic OCID value from your tenancy.
- Add a description.
- Save the file with`action.json`as the file name.

### Creating a Rule

Open a command prompt and run`oci events rule create`to create a rule.

Use the following options:
- `display-name`indicates the name of the rule in the Console
- `is-enabled`indicates whether the rule is evaluated.
- 

`condition`a JSON formatted string used to indicate a pattern for event matching (see the example command below for usage).
- `compartment-id`indicates the compartment where the rule applies. Events evaluates messages from resources in this compartment and any child compartments.
- `actions`indicates the location in the local file system of the JSON formatted file you created to specify the actions for a rule.
- `wait-for-state=`when used with ACTIVE indicates that the CLI should wait for the service to create the rule, do another GET operation, and then display the rule in the active state. Without the option, the CLI displays the rule immediately in the creating state.

For example:

```

```

Note  
  
Replace the values in &lt;compartment_OCID&gt; and &lt;path_to_json_formatted_actions_file&gt; with the actual values from your tenancy and local file system.

When you run the preceding command, the CLI prompts you about the rule and its display:
```

```

### Create another Bucket

Create another bucket as outlined in a preceding section.

### Receiving Your Notification

Log in to the email account you specified in the previous procedure to receive the notification about the bucket being created.
Tip
