# Configuring a Confidential Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/configure-confidential-application.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring a Confidential Application

To register the IAM Linux PAM as a client application in IAM, you create a confidential application with the POSIX Viewer role.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Integrated applications .
- Select Add application.
- In the Add application window, select Confidential Application , and then select Launch workflow .
- In the Add Confidential Application page, enter a Name for the application. Select Next .
- On the Add Confidential Application page, select Configure this application as a client now .
- In the Authorization section, select these two Allowed grant types :

- Client Credentials
- JWT Assertion
- Select Add app roles .
- In the Add app roles dialog box, select these roles:

- Me
- POSIX Viewer
- Signin
- Identity Domain Administrator or User Administrator
- Select Add .
- Select Next .
- Select Finish .
- Record the Client ID and Client Secret in the General Information section.
To integrate with your confidential application, use this ID and secret as part of your connection settings. The Client ID and Client Secret are equivalent to a credential (for example, an ID and password) that your application uses to communicate with IAM.
- Return to the Add app roles dialog box, and remove the following administrator role: Identity Domain Administrator or User Administrator . If you don't remove roles, the application will fail during testing.
- At the top of the page, to the right of the application name, select Activate .
-
