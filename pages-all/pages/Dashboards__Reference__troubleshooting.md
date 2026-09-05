# Troubleshooting Console Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Reference/troubleshooting.htm
- Fetched: 2026-09-05 01:59 CDT

# Troubleshooting Console Dashboards

Use troubleshooting information to identify and address common issues that can occur while working with Oracle Cloud Infrastructure Console Dashboards.

## "Show URL" Link Missing for Firefox Users

Summary: When a Firefox user selects Copy URL from the Dashboard actions menu, the dashboard's URL is copied, but the "Show URL" text is missing from the notification.

Firefox requires that you modify an advanced preference to allow the Console to read from the clipboard.

Solution: Explicitly enable the`Clipboard.readText()`functionality for Firefox:
- Open Firefox.
- Enter`about:config`in the navigation bar.
- Select "Accept the Risk and Continue."
- Search for`dom.events.testing.asyncClipboard`and toggle the setting to`true`
