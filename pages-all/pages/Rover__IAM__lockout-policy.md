# Applying Lockout Policies to Roving Edge Infrastructure Device Users
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/lockout-policy.htm
- Fetched: 2026-09-05 03:00 CDT

# Applying Lockout Policies to Roving Edge Infrastructure Device Users

Describes how to apply lockout policies to Roving Edge Infrastructuredevice users.

As an administrator, you can establish a lockout policy for Roving Edge Infrastructure users based on the number of failed login attempts, the amount of time since the previous login, or both. If these factors apply, the user is unable to log in without their account being reactivated by an administrator.

## Using the Device Console

- Open the navigation menu and select Identity Management &gt; Authentication Settings . The Authentication Settings page appears.
- Select Edit Authentication Settings . The Edit Authentication Settings dialog box appears.
- Select either or both of the following options:

- 

Deactivate a user after 3 consecutive failed login attempts within a 15 minute window.
- 

Deactivate a user if they have not logged in after 90 days.
-
