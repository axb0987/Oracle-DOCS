# Scheduling a Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsscheduling.htm
- Fetched: 2026-09-05 02:09 CDT

# Scheduling a Function

Find out how to schedule a function with OCI Functions.

For prerequisites and more information, see[Scheduling Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsschedulingfunctions-about.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsscheduling.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsscheduling.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsscheduling.htm#)
- 

When using the Console to schedule functions, you can create a new resource schedule in Resource Scheduler and add a function to the resource schedule using:
- OCI Functions Console pages
- Resource Scheduler Console pages

Note that if you want to edit or delete an existing resource schedule, or to remove a function from a resource schedule, you have to use Resource Scheduler Console pages (for more information, see[Managing Schedules](https://docs.oracle.com/iaas/Content/resource-scheduler/tasks/managing-schedules.htm)in the Resource Scheduler documentation).

To schedule a function by using OCI Functions Console pages to create a schedule in Resource Scheduler:
- On the Applications list page, select the application that contains the function that you want to work with. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/list-applications.htm).
- 

Select the Functions tab.

The Functions list page opens. All functions in the selected application are displayed in a table.
- Select the name of the function that you want to schedule, and then select Schedules to display the Schedules page for the function.

Any existing schedules in the current compartment to which the function has already been added are shown.
- On the Schedules page in the OCI Functions Console, select Add Schedule to add the function to a schedule.

You can add the function to a new schedule that you create (as described in this section), or add the function to an existing schedule that you (or somebody else) has already created.
- Select Create new schedule , and specify the following details:
- Name: A name of your choice for the new resource schedule. Avoid entering confidential information.
- Description: (Optional) A meaningful description of the new resource schedule.
- Compartment: The compartment in which to create the new resource schedule.
- 

Specify how you want to enter details for the schedule by selecting one of the following options:
- Form interface: Select this option to define the schedule using fields in the UI.
- Cron expression: Select this option to define the schedule by entering a Cron expression.
- If you selected Form interface as the way to define the schedule, use the Interval field to select the time interval for the schedule, and specify other details appropriate for the time interval as follows:
- One-time: Enter the UTC time and date on which the schedule is to start.
- Hourly: Enter how often the schedule is to repeat (1 = every hour, 2 = every two hours, 3 = every three hours), the UTC time and date on which the schedule is to start, and (optionally) the date on which the schedule is to end.
- Daily: Enter how often the schedule is to repeat (1 = every day, 2 = every two days, 3 = every three days), the UTC time and date on which the schedule is to start, and (optionally) the date on which the schedule is to end.
- Weekly: Enter how often the schedule is to repeat (1 = every week, 2 = every two weeks, 3 = every three weeks), the days of the week on which the schedule is to run the function, the UTC time and date on which the schedule is to start, and (optionally) the date on which the schedule is to end.
- Monthly: Enter how often the schedule is to repeat (1 = every month, 2 = every two months, 3 = every three months), the days of the month on which the schedule is to run the function, the UTC time and date on which the schedule is to start, and (optionally) the date on which the schedule is to end.

The Summary field shows a text version of the schedule you enter.
- If you selected Cron expression as the way to define the schedule, enter the following details:
- Cron expression: Enter a valid Cron expression to set the schedule interval. For example:
- To set the schedule to run the function every week at 13:30 UTC on Monday, Tuesday, Wednesday, Thursday, and Friday, enter:
```

```

- To set the schedule to run the function every 2 hours on the 15th day of every month, enter:
```

```

- Time: Enter the UTC time on which the schedule is to start.
- Start date: Enter the date on which the schedule is to start.
- End date: (Optional) Enter the date on which the schedule is to end.

For more information about Cron expressions, see[Using a Cron expression](https://docs.oracle.com/iaas/Content/resource-scheduler/tasks/schedule-info.htm#untitled4)in the Resource Scheduler documentation.
- (Optional) To pass arguments and values to the function, select the Add invocation payload option and enter the arguments and values in a format expected by the function. If the function is expecting arguments and values as JSON, use a valid JSON format.
- (Optional) To apply tags to the resource, select Add tag . If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Create to create the schedule and add the function to it.

The new resource schedule is shown on the Schedules page for the function in the OCI Functions Console.

Having created the resource schedule and added a function to it, you have to create both a dynamic group with a rule that includes the resource schedule's OCID, and a policy statement that grants the dynamic group access to the function:
- Select the resource schedule to display its details in the Resource Scheduler Console, and copy the schedule's OCID. For example,`ocid1.resourceschedule.oc1.phx.amaaaaaa3______owq`.
- Create a dynamic group by following the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), give the dynamic group a name (for example,`resource-scheduler-prod-dynamic-group`), and specify a rule for the dynamic group as follows:

```

```

where`<resource-schedule-OCID>`is the OCID of the resource schedule that you copied earlier. For example:

```

```

- Create a policy to grant the new dynamic group access to functions in OCI Functions by following the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), give the policy a name (for example,`resource-scheduler-prod-dyn-grp-policy`), and specify a policy statement similar to the following:

```

```

where`<dynamic-group-name>`is the name of the dynamic group that you created in the previous step. For example:

```

```

The function is now invoked according to the resource schedule that you have defined.

To schedule a function by using Resource Scheduler Console pages to create a schedule in Resource Scheduler:
- Sign in to the Console as a functions developer.
- Open the navigation menu and select Governance &amp; Administration . Under Resource Scheduler , select Schedules .
- Select the region you're using with OCI Functions.

We recommend that you use the same region as the Docker registry that's specified in the Fn Project CLI context. See[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm).
- On the Schedules page in the Resource Scheduler Console, select Create a schedule to create a new resource schedule.
- On the Basic information page, specify the following values for the resource schedule:
- Schedule name: A name of your choice for the resource schedule. Avoid entering confidential information.
- Schedule description: (Optional) A meaningful description of the resource schedule.
- Action to be executed: Select Start .
- Compartment: The compartment in which to create the resource schedule.
- Show advanced options: Select this option to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .
- On the Resources page, select the function you want to schedule as follows:
- From the Resource selection method options, select the Static - apply schedule to specific resources option.
- In the Search and filter box, use the default filter ( Compartment All ) to search for resources in all compartments, or select Compartment to select a specific compartment in which to search for resources..
- In the Search and filter box, select Resource type .
- Select FunctionsFunction from the list of resource types (de-select any other resource types that are selected), and select Apply .

The functions in the compartment you selected are shown.
- Select the function you want to schedule.
- Select Next .
- On the Schedule page, specify when and how often you want the function to run, and when the resource schedule should start and end.

For more information about setting up a resource schedule, see[Adding Schedule Information](https://docs.oracle.com/iaas/Content/resource-scheduler/tasks/schedule-info.htm).
- Select Next .
- On the Review page, confirm the information you have entered, and select Create schedule to schedule the function.

The new resource schedule is shown on the Schedules page of the Resource Scheduler Console.

Having created the resource schedule and added a function to it, you have to create both a dynamic group with a rule that includes the resource schedule's OCID, and a policy statement that grants the dynamic group access to the function:
- Select the resource schedule to display its details, and copy the schedule's OCID. For example,`ocid1.resourceschedule.oc1.phx.amaaaaaa3______owq`.
- Create a dynamic group by following the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), give the dynamic group a name (for example,`resource-scheduler-prod-dynamic-group`), and specify a rule for the dynamic group as follows:

```

```

where`<resource-schedule-OCID>`is the OCID of the resource schedule that you copied earlier. For example:

```

```

- Create a policy to grant the new dynamic group access to functions in OCI Functions by following the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), give the policy a name (for example,`resource-scheduler-prod-dyn-grp-policy`), and specify a policy statement similar to the following:

```

```

where`<dynamic-group-name>`is the name of the dynamic group that you created in the previous step. For example:

```

```

The function is now invoked according to the resource schedule that you have defined.
- 

Use the Resource Scheduler[resource-scheduler schedule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-scheduler/schedule/create.html)command and required parameters to schedule a function.

For more information, see[Creating Schedules](https://docs.oracle.com/iaas/Content/resource-scheduler/tasks/creating-schedules.htm)

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the Resource Scheduler[CreateSchedule](https://docs.oracle.com/iaas/api/#/en/resource-scheduler/latest/Schedule/CreateSchedule)
