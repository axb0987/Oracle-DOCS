# Configuring Mobile OTP and Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-mobile-otp-and-notifications.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring Mobile OTP and Notifications

Configure a policy an identity domain in IAM for the time-based one-time passcode (OTP), and protection and compliance policies for the Oracle Mobile Authenticator (OMA) app.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Authentication .
- On the Authentication page, in the Mobile app passcode row select Edit .
- Under Passcode policy , make any necessary changes. The default values are the industry-recommended settings.

- The value in the Passcode generation interval (seconds) box indicates the number of seconds before a new passcode must be generated. To avoid clock skew, which is the time difference between the server and the device, the user must ensure that their device clock is synchronized. The maximum allowed time difference between the server and the device is 90 seconds.
- The value in the Secret key refresh interval (days) box indicates the number of days before you want to refresh the shared secret. Each time that a user enrolls a mobile device, a secret key is pushed and securely stored on the device by using the scanned Quick Response (QR) code or when the user enters the key manually. This key is the input to the OTP algorithm that's used to generate the OTP. The key is refreshed silently, so no user action is required.
- Under Notification policy , select Enable pull notifications to allow the OMA App to pull pending notification requests from the server.
Pull notifications are updates that are delivered to a mobile device or computer in response to a user who is manually checking (pulling) for login request notifications.

Pull notifications are useful in scenarios where the GCM service (Android), APNS Service (iPhone), or WNS service (Windows) doesn't work. For example, China blocks the GCM service, so users don't receive notifications that are pushed to their device. However, if pull notifications are available, the user can manually pull notifications from a server using the OMA app. Also, offering pull notifications is useful in situations where push notifications aren't 100% reliable.
- Configure the App protection policy for the OMA app.

- None: The app is unprotected.
- App PIN: A PIN is needed to access the app.
- Fingerprint: A fingerprint is used to access the app.
- Configure the Compliance policy for the OMA app. Compliance policy checks are performed each time that the OMA app opens
- Mobile authenticator app version check: To block users from using an outdated app, select Require latest updates .
- Minimum OS version check: To block users from using the app on a device that has an outdated operating system, select Restrict access from devices with outdated OS versions .
Users won't receive push notification requests and won't be able to generate passcodes.
- Rooted devices check (iOS and Android only): To block users from using the app on a device that is rooted or where rooted status is unknown, select Restrict access from rooted devices , Restrict access from devices where rooted status is unknown , or both.
Users won't receive push notification requests and won't be able to generate passcodes.
- Device screen lock check: To block users from using the app on a device that doesn't have a screen lock or where the screen lock status is unknown, select Restrict access from devices without a screen lock , Restrict access from devices where screen lock status is unknown , or both.
Users won't receive push notification requests and won't be able to generate passcodes.
- Select Save changes .
-
