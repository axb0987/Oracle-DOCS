# Creating an Events Rule for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Events/create_rule.htm
- Fetched: 2026-09-05 02:59 CDT

# Creating an Events Rule for a Roving Edge Infrastructure Device

Describes how to create an events rule on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/create_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/create_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/create_rule.htm#)
- 

- Open the navigation menu and select Events &gt; Rules . The Rules page appears. All events rules are listed in tabular form.
- Select Create Rule . The Create Rule dialog box appears.
- Enter the following:

- Display Name : Specify a friendly name for the rule. You can change this name later. Avoid entering confidential information.
- Description : Specify a description of what the rule does. You can change this description later.
- Under Rule Conditions , complete the following:

To add an event type:
- 

Select Event Type from Condition .
- 

Select a Service Name .
- 

In Event Type , select one or more event types for this service.

To add an attribute:

You must first have already created an event type rule condition before you can add an attribute.
- 

Select Attribute from Condition .
- 

Select an Attribute Name .
- 

Select or enter attribute values from Attribute Values . Attribute values are optional.

Select + Another Condition to add another rule condition.
- Under Actions , specify the trigger for the specified event conditions:

- 

Select the Action Type from the list. Options are HTTP and HTTPS.
- 

Select the URL of the action.
- 

Select + Another Action and select Event Type to add another action for the rule condition.
- Select Create Rule .

The Create Rule dialog box closes and you are returned to the Rule page. The events rule you created is listed with the other ones.
- 

Use the[oci events rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/create.html)command and required parameters to create an events rule on your Roving Edge Infrastructure devices:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/../Access/cli_install.htm#CLI)
- 

Run the[CreateRule](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Rule/CreateRule)
