Project Overview
This project is a Discord Bot System designed using the Boundary-Control-Entity (BCE) architecture pattern. The bot performs various tasks like managing accounts, launching a browser, fetching prices, checking availability, and monitoring both prices and availability. It automates interactions with websites, tracks data, and logs results into Excel and HTML formats.

Command Mapping and BCE Structure
!stop_bot

Boundary: StopBoundary
Control: StopControl
Entity: No entity interaction required for stopping the bot.
Functionality: Stops the bot gracefully when invoked.
!project_help

Boundary: HelpBoundary
Control: HelpControl
Entity: No entity interaction is required for help commands.
Functionality: Displays all available commands of the bot.
!fetch_all_accounts

Boundary: AccountBoundary
Control: AccountControl
Entity: AccountDAO (Data Access Object interacts with the database)
Functionality: Fetches and displays all user accounts from the database.
!add_account

Boundary: AccountBoundary
Control: AccountControl
Entity: AccountDAO
Functionality: Adds a new account to the database. This command passes credentials from the boundary to the control layer and finally to the DAO for database insertion.
!fetch_account_by_website

Boundary: AccountBoundary
Control: AccountControl
Entity: AccountDAO
Functionality: Fetches a specific account by the website from the database and displays the result.
!delete_account

Boundary: AccountBoundary
Control: AccountControl
Entity: AccountDAO
Functionality: Deletes an account from the database by ID.
!launch_browser

Boundary: LaunchBrowserBoundary
Control: LaunchBrowserControl
Entity: BrowserEntity
Functionality: Launches a browser using BrowserEntity and handles browser state through the control layer.
!close_browser

Boundary: CloseBrowserBoundary
Control: CloseBrowserControl
Entity: BrowserEntity
Functionality: Closes the currently running browser.
!navigate_to_website

Boundary: NavigationBoundary
Control: NavigationControl
Entity: BrowserEntity
Functionality: Navigates to a specified URL.
!login

Boundary: LoginBoundary
Control: LoginControl
Entity: BrowserEntity, AccountControl (fetches credentials)
Functionality: Logs into a website using stored credentials fetched from AccountControl and executes the login through BrowserEntity.
!get_price

Boundary: GetPriceBoundary
Control: GetPriceControl
Entity: PriceEntity
Functionality: Fetches the current price of a product from a specified URL using PriceEntity.
!start_monitoring_price

Boundary: MonitorPriceBoundary
Control: MonitorPriceControl
Entity: PriceEntity
Functionality: Monitors the price of a product at a given frequency and stores the results. Results are logged into Excel and HTML using ExportUtils.
!stop_monitoring_price

Boundary: StopMonitoringPriceBoundary
Control: MonitorPriceControl
Entity: PriceEntity
Functionality: Stops monitoring the price and sends the collected results.
!check_availability

Boundary: CheckAvailabilityBoundary
Control: CheckAvailabilityControl
Entity: AvailabilityEntity
Functionality: Checks availability on a website like OpenTable and returns the result. Data can be logged into Excel and HTML.
!monitor_availability

Boundary: MonitorAvailabilityBoundary
Control: MonitorAvailabilityControl
Entity: AvailabilityEntity
Functionality: Monitors availability at a given frequency. Collected data is stored and exported to Excel and HTML.
!stop_monitoring_availability

Boundary: MonitorAvailabilityBoundary
Control: MonitorAvailabilityControl
Entity: AvailabilityEntity
Functionality: Stops monitoring availability and returns the collected results.
Data and Output Overview
Account Management
The AccountDAO is responsible for interacting with the database (PostgreSQL) to manage user accounts (add, delete, fetch). It uses SQL queries to perform operations and ensures data persistence.
Browser and Web Interaction
BrowserEntity is central to all browser-related operations. It manages launching, closing, navigating, and interacting with elements on a webpage. Selenium is used to interact with web elements like buttons, input fields, and retrieving data.
Price and Availability Monitoring
PriceEntity and AvailabilityEntity handle the core business logic of interacting with the webpage to fetch prices and check availability. They also manage exporting the results using ExportUtils.
Data Export
ExportUtils provides utility functions to export data to Excel and HTML. Results from price checks or availability checks are passed as a Data Transfer Object (DTO) and saved to corresponding files. The DTO pattern ensures that structured data is passed efficiently between layers.
BCE Pattern Validation
Boundary objects act as the communication layer between the user (via Discord) and the control objects.
Control objects handle the business logic, deciding what entity objects to use.
Entity objects encapsulate business rules and interactions with external systems like the browser or the database.
Excel and HTML Outputs
The results of commands like price monitoring and availability checks are exported into Excel and HTML. Files are organized in ExportedFiles/excelFiles and ExportedFiles/htmlFiles, ensuring that all command results are logged and can be reviewed later.
Databases and Logs
Accounts are stored in a PostgreSQL database, and actions like login or availability checks interact with this data. Results are also stored in Excel and HTML files, which act as logs for the actions taken by the bot.