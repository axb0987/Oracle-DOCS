# Using the Open in Code Editor Button
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/code_editor_using_using_git_from_code_editor_one_click_clone.htm
- Fetched: 2026-09-05 01:35 CDT

# Using the Open in Code Editor Button

Learn how to use the Open in Code Editor button.

Some Git repositories or websites feature an Open in Code Editor button. Clicking this button will automatically clone a repository in a Cloud Shell session and open it in Code Editor.
To use the Open in Code Editor button:
- Click the Open in Code Editor button.
- If prompted, log in to the OCI Console.
- A Code Editor session starts, and a Verify Cloning dialog appears, allowing you to verify that you want to clone the repository:

- The destination directory defaults to the repository name. You can change this by entering a new value in the Enter directory name text box.
- Select the checkbox indicating that you have reviewed and accept the Oracle Terms of Use.
- Click the Clone button.

Code Editor will clone the repository into the destination directory and open the project's README file in the editor.

For example:

## Embedding an Open in Code Editor Button
You can add an Open in Code Editor button to your own README files.
Note  
  
The recommended location for this link is the root README.md file of your Git repository.

To add an Open in Code Editor button in your own content, you need to specify the following parameters in your URL:
Parameters

URL Parameter Description
cs_repo_url [Mandatory] Any accessible Git Repo URL.
cs_branch [Optional] Branch to checkout. If not specified, the default branch is used.
cs_open_ce [Optional] Open Code Editor after cloning and executing any required scripts. Code Editor automatically opens the cloned folder in the workspace.
cs_initscript_path [Optional] Path to an executable script. The file path is relative to the current directory.
cs_readme_path [Optional] Path to a readme file in a git repo. The contents of this file will display in Cloud Shell or Code Editor after cloning the repo. This could contain a welcome message and further instructions to the user. The file path is relative to the current directory.
This example shows a URL to embed an Open In Code Editor button in a Git repository README.md file. With the click of the button, you will be redirected to the Oracle Cloud domain and all the required query parameters will be passed, as shown below:

```

```

Note  
  
We recommend the use of HTTP URLs rather than SSH URLs. For security, automatic script execution from non-trusted GitHub repositories is disabled, even when the redirected URL query parameters have a`cs_initscript_path`
