# Scheduling Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsschedulingfunctions-about.htm
- Fetched: 2026-09-05 02:09 CDT

# Scheduling Functions

Find out about scheduling functions that you have created with OCI Functions.

You can run the functions that you create with OCI Functions on a recurring schedule using resource schedules. Scheduling functions to run at the same time each week, day, or hour enables you to automate some of the tasks associated with managing cloud infrastructure, such as:
- Maintenance and Housekeeping: Schedule functions to perform regular maintenance tasks. For example, database cleanup, log rotation, data archiving, cleanup of expired sessions in an application's cache, and monthly archiving of audit logs to long-term storage.
- Periodic Data Processing and Analytics: Run data processing or analytics jobs at set intervals. For example, to generate daily reports, to update dashboards, to aggregate sensor data every hour for trend analysis, and to process batched data on a schedule that meets business requirements.
- Machine Learning and AI: Schedule model retraining with new data to improve accuracy and performance. For example, by running periodic inference tasks at scheduled times to generate predictions or recommendations, by evaluating model performance daily and monitoring key metrics to detect drift, and by triggering alerts if performance drops below thresholds.

You schedule a function by creating a new resource schedule, and adding the function to that resource schedule. You can add additional functions to the same resource schedule later. The resource schedules you create are stored in OCI Resource Scheduler (for more information, see[About Resource Scheduler](https://docs.oracle.com/iaas/Content/resource-scheduler/concepts/resourcescheduleroverview-about.htm)).

When you schedule a function, the function is invoked with Detached as the invocation type. Detached invocation can be better than synchronous invocation for functions that take a long time to run, because detached invocation supports a longer execution timeout, and also supports additional configuration options for post-execution delivery destinations. For more information, see[Synchronous and Detached Invocation Types](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#Invoking_Functions__section_synchronous_detached_invocation_types).

You can create resource schedules and add functions to them using:
- OCI Functions Console pages
- Resource Scheduler Console pages
- Resource Scheduler CLI
- Resource Scheduler API

See[Scheduling a Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsscheduling.htm).

## Prerequisites

To create and use resource schedules in Resource Scheduler, you must have been granted permission to manage resource schedules in the tenancy. For example, by a policy statement similar to the following:
```

```

Before a function can be invoked according to a resource schedule:
- You have to create a dynamic group with a rule that includes the resource schedule's OCID. For example:

```

```

- You have to create a policy statement that grants the dynamic group access to the function. For example:

```

```

For more information, see[Creating Schedules](https://docs.oracle.com/iaas/Content/resource-scheduler/tasks/creating-schedules.htm)
