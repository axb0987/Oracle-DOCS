# Getting an Auth Token
- Source: https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrygettingauthtoken.htm
- Fetched: 2026-09-05 02:54 CDT

# Getting an Auth Token

Find out how to create a new auth token for use with Container Registry.

Before you can push and pull Docker images to and from Oracle Cloud Infrastructure Registry (also known as Container Registry), you must already have an Oracle Cloud Infrastructure username and an auth token. If you haven't got an auth token, or you've forgotten it, or you're not sure, you can create a new auth token. You only see the auth token string when you create it, so be sure to copy the auth token to a secure location immediately.
Tip  
  
Each user can have up to two auth tokens at a time. So if you do lose or forget the auth token, you can always create a second auth token.

To create a new auth token:
- 

In the top-right corner of the Console, open the Profile menu , and then select User Settings (or My Profile or your account name) to view the details.
- 

On the Tokens and keys tab, go to the Auth Tokens section and select Generate token .
- 

Enter a friendly description for the auth token. Avoid entering confidential information.
- 

Select Generate token . The new auth token is displayed.
- 

Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
-
