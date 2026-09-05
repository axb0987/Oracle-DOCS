# Enabling Premium Jobs
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/premium-jobs.htm
- Fetched: 2026-09-05 02:54 CDT

# Enabling Premium Jobs

Enable premium jobs to support more concurrent Resource Manager jobs.

Resource Manager has a service limit named[Concurrent Job Count (concurrent-job-count) to limit how many jobs can run at the same time for a tenancy.

If you need to run more concurrent jobs beyond the existing Concurrent Job Count limit, you can request an OCI service limit increase for that limit. However, large increase requests aren't guaranteed to be approved, especially when the requested value might affect service capacity or other customers.

Premium jobs are introduced specifically to support high-volume job creation scenarios by letting you create a larger number of concurrent jobs. Jobs that exceed the Concurrent Job Count limit are run as premium jobs using dedicated resources.

## Using Premium Jobs

Premium jobs are designed to keep the job creation experience consistent across Resource Manager jobs. You don't need to select a separate job type or distinguish premium jobs from other jobs when creating a job. After premium jobs are enabled, jobs created beyond the existing Concurrent Job Count limit are automatically treated as premium jobs.

Note that if a very large number of premium jobs are submitted at the same time, these jobs might experience execution delays.

## Billing and Total Concurrent Job Calculations

Your tenancy is charged for the resources used to run premium jobs. Jobs that run within the existing Concurrent Job Count limit remain free. Billing applies only to the premium portion. For more information, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html).

Total concurrent jobs are calculated using the following formula:

`Total concurrent jobs = Concurrent Job Count (concurrent-job-count) + Premium Job Submission Count (premium-job-submission-count)`

Here's what happens:
- The free Concurrent Job Count is consumed first.
- After that limit is reached, additional concurrent jobs count against Premium Job Submission Count and can incur charges.

For example, if your Concurrent Job Count limit is 20 but you sometimes might need to run 50 jobs at the same time, request a Premium Job Submission Count limit increase to 30.

If you submit 50 concurrent jobs, the jobs count against the limits as follows:
- The first 20 jobs count against Concurrent Job Count and are free.
- The remaining 30 jobs count against Premium Job Submission Count and can incur charges.

## Requesting Premium Jobs

By default, premium jobs are disabled for OCI tenancies and the[Premium Job Submission Count (premium-job-submission-count) service limit is initialized to 0.

To enable premium jobs, submit an OCI[service limit increase request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)
