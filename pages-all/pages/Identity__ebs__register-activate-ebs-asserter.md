# Registering and Activate the E-Business Suite Asserter in IAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/register-activate-ebs-asserter.htm
- Fetched: 2026-09-05 02:22 CDT

# Registering and Activate the E-Business Suite Asserter in IAM

To establish communication with IAM, the E-Business Suite Asserter uses the client ID and the client secret of an IAM registered application.

- In the IAM Console, expand the Navigation Drawer , and then select Applications .
- On the Applications page, select Add .
- In the Add Application dialog box, select Trusted Application .
- In the Details pane, enter the following information, and then select Next .
- Name: EBS Asserter
- Description: E-Business Suite Asserter Application
- Application URL: https://ebsasserter.example.com:7002/ebs
- Display in My Apps: Select this check box
- In the Client pane, select Configure this application as a client now , and then enter or select the following values:
- Allowed Grant Types : Client Credentials and Authorization Code
- Redirect URL : https://ebsasserter.example.com:7002/ebs/response
- Logout URL : https://ebsasserter.example.com:7002/ebs/logout
- Post Logout Redirect URL : https://ebs.example.com:8001/OA_HTML/OA.jsp?OAFunc=OANEWHOMEPAGE
- In the Client pane, scroll down, and select Add underneath Grant the client access to IAM Admin APIs.
- In the Add App Role dialog box, select Authenticator Client and Me from the list, and then select Add .
- In the Client pane, select Next .
- Select Next until you reach the last pane, and then select Finish .
- In the Application Added dialog box, make a note of the Client ID and Client Secret values, and then select Close .
E-Business Suite Asserter needs these values to integrate with IAM.
- Select Activate .
-
