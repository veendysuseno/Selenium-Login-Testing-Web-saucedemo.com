# Selenium Login Testing

## Description:

This project includes Selenium-based tests for the login functionality of a web application. The script performs various tests to ensure that login functionality is working correctly under different scenarios.

## Overview

### Dependencies:

- **unittest**: For structuring the test cases.
- **selenium**: For automating web browser interaction.
- **webdriver_manager**: To automatically manage the ChromeDriver binary.

### Test Cases:

- **test_failed_login**: Tests logging in with an incorrect username and checks if the error message "Epic sadface: Password is required" is displayed.
- **test_success_login**: Tests logging in with valid credentials.
- **test_empty_login**: Tests clicking the login button without entering any credentials.

## Directory Structure:

. <br/>
├── login_test.py <br/>
├── README.md <br/>
└── requirements.txt <br/>

- test_login.py: Contains the Selenium test cases for login functionality.
- requirements.txt: Lists the necessary Python packages.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (automatically managed by webdriver_manager)

## Installation

1. Install Python packages using pip:

```bash
pip install -r requirements.txt
```

2. Ensure you have Google Chrome installed.

## Usage

To run the tests, execute the following command:

```bash
python login_test.py
```

## Test Cases

1. Failed Login Test (test_failed_login):

   - Attempts to log in with an incorrect username and verifies that an error message is displayed.

2. Successful Login Test (test_success_login):

   - Logs in with valid credentials and checks if the login is successful.

3. Empty Login Test (test_empty_login):
   - Attempts to log in without providing any credentials and verifies that no errors are triggered.

## Requirements

The requirements.txt file includes the necessary packages:

```requirements.txt
unittest
selenium
webdriver-manager
```
