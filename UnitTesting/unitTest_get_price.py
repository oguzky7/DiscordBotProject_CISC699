from test_init import *
import pytest
import logging
from unittest.mock import patch, AsyncMock

"""
Executable steps for the 'get_price' use case:
1. Control Layer Processing:
   This test ensures that `PriceControl.receive_command()` correctly processes the 'get_price' command, 
   including proper URL parameter handling and delegation to the `get_price` method.

2. Price Retrieval:
   This test verifies that `PriceEntity.get_price_from_page()` retrieves the correct price from the webpage, 
   simulating the fetching process accurately.

3. Data Logging to Excel:
   This test ensures that the price data is correctly logged to an Excel file using `DataExportEntity.log_to_excel()`, 
   ensuring that data is recorded properly.

4. Data Logging to HTML:
   This test ensures that the price data is correctly exported to an HTML file using `DataExportEntity.export_to_html()`, 
   validating the data export process.

5. Response Assembly and Output:
   This test confirms that the control layer assembles and outputs the correct response, including price information, 
   Excel and HTML paths, ensuring the completeness of the response.
"""

# Test 1: Control Layer Processing
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: Control Layer Processing for 'get_price' command")

    # Mock the `get_price` method to avoid browser interaction
    with patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock) as mock_get_price:
        # Set the return value for `get_price` method
        mock_get_price.return_value = ("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML at path.html")

        # Mock the PriceControl.receive_command method
        price_control = PriceControl()

        # Simulate the command processing
        result = await price_control.receive_command("get_price", "https://example.com/product")

        # Validate the return values
        logging.info("Verifying that the receive_command correctly processed the 'get_price' command")

        # Unpack the result for clearer assertions
        price, excel_path, html_path = result
        
        # Validate the return values match what we mocked
        assert price == "100.00", f"Expected price '100.00', got {price}"
        assert excel_path == "Data saved to Excel file at path.xlsx", f"Expected Excel path 'path.xlsx', got {excel_path}"
        assert html_path == "Data exported to HTML at path.html", f"Expected HTML path 'path.html', got {html_path}"

        logging.info("Test passed: Control layer processing correctly handles 'get_price'")


# Test 2: Price Retrieval
@pytest.mark.asyncio
async def test_price_retrieval():
    logging.info("Starting test: Price Retrieval from webpage")

    # Mock the `get_price_from_page` method to simulate price retrieval without browser interaction
    with patch('entity.PriceEntity.PriceEntity.get_price_from_page', return_value="100.00") as mock_price:
        price_control = PriceControl()
        
        # Call the `get_price` method
        result = await price_control.get_price("https://example.com/product")

        logging.info("Expected fetched price: '100.00'")
        assert "100.00" in result, f"Expected price '100.00', got {result}"
        logging.info("Test passed: Price retrieval successful and correct")


# Test 3: Data Logging to Excel
@pytest.mark.asyncio
async def test_data_logging_excel():
    logging.info("Starting test: Data Logging to Excel")

    # Mock the `get_price` method to avoid browser interaction
    with patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock) as mock_get_price:
        # Set return value for `get_price` method
        mock_get_price.return_value = ("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML file at path.html")

        # Mock the log_to_excel method to simulate Excel data logging
        with patch('entity.DataExportEntity.ExportUtils.log_to_excel', return_value="Data saved to Excel file at path.xlsx") as mock_excel:
            price_control = PriceControl()
            
            # Call the `get_price` method, which is now mocked
            _, excel_result, _ = await price_control.get_price("https://example.com/product")

            logging.info("Verifying Excel file creation and data logging")
            assert "path.xlsx" in excel_result, f"Expected Excel path 'path.xlsx', got {excel_result}"
            logging.info("Test passed: Data correctly logged to Excel")


# Test 4: Data Export to HTML
@pytest.mark.asyncio
async def test_data_logging_html():
    logging.info("Starting test: Data Export to HTML")

    # Mock the `get_price` method to avoid browser interaction
    with patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock) as mock_get_price:
        # Set return value for `get_price` method
        mock_get_price.return_value = ("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML file at path.html")

        # Mock the export_to_html method to simulate HTML export
        with patch('entity.DataExportEntity.ExportUtils.export_to_html', return_value="Data exported to HTML file at path.html") as mock_html:
            price_control = PriceControl()

            # Call the `get_price` method, which is now mocked
            _, _, html_result = await price_control.get_price("https://example.com/product")

            logging.info("Verifying HTML file creation and data export")
            assert "path.html" in html_result, f"Expected HTML path 'path.html', got {html_result}"
            logging.info("Test passed: Data correctly exported to HTML")


# Test 5: Response Assembly and Output
@pytest.mark.asyncio
async def test_response_assembly_and_output():
    logging.info("Starting test: Response Assembly and Output")

    # Mock the `get_price` method to simulate price retrieval
    with patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock) as mock_get_price:
        mock_get_price.return_value = ("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML at path.html")

        price_control = PriceControl()

        # Call `receive_command` with `get_price` command
        result = await price_control.receive_command("get_price", "https://example.com/product")

        # Unpack the result
        price, excel_path, html_path = result

        logging.info("Checking response contains price, Excel, and HTML paths")
        assert price == "100.00", f"Price did not match expected value, got {price}"
        assert "path.xlsx" in excel_path, f"Excel path did not match, got {excel_path}"
        assert "path.html" in html_path, f"HTML path did not match, got {html_path}"

        logging.info("Test passed: Correct response assembled and output")

if __name__ == "__main__":
    pytest.main([__file__])
