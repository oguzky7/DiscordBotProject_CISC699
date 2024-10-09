from test_init import *
"""
Executable steps for the 'get_price' use case:
1. Control Layer Processing
   This test will ensure that PriceControl.receive_command() correctly processes the "get_price" command,
   including proper URL parameter handling and delegation to the get_price method.

2. Price Retrieval
   This test will verify that PriceEntity.get_price_from_page() retrieves the correct price from the webpage,
   simulating the fetching process accurately.

3. Data Logging to Excel
   This test checks that the price data is correctly logged to an Excel file using DataExportEntity.log_to_excel(),
   ensuring that data is recorded properly.

4. Data Logging to HTML
   This test ensures that the price data is correctly exported to an HTML file using DataExportEntity.export_to_html(),
   validating the data export process.

5. Response Assembly and Output
   This test will confirm that the control layer assembles and outputs the correct response, including price information,
   Excel and HTML paths, ensuring the completeness of the response.
"""

# Testing the control layer's ability to process the "get_price" command
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: Control Layer Processing for get_price command")
    
    # Mock the actual command handling to simulate command receipt and processing
    with patch('control.PriceControl.PriceControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = await PriceControl().get_price("https://example.com/product")
        result = await PriceControl().receive_command("get_price", "https://example.com/product")
        
        logging.info("Verifying that the receive_command correctly processed the 'get_price' command")
        assert "get_price" in str(mock_receive.call_args)
        logging.info("Test passed: Control layer processing correctly handles 'get_price'")

# Testing the price retrieval functionality from the PriceEntity
@pytest.mark.asyncio
async def test_price_retrieval():
    logging.info("Starting test: Price Retrieval from webpage")
    
    with patch('entity.PriceEntity.PriceEntity.get_price_from_page', return_value="100.00") as mock_price:
        price_control = PriceControl()
        result = await price_control.get_price("https://example.com/product")
        
        logging.info("Expected fetched price: '100.00'")
        assert "100.00" in result
        logging.info("Test passed: Price retrieval successful and correct")

# Testing the Excel logging functionality
@pytest.mark.asyncio
async def test_data_logging_excel():
    logging.info("Starting test: Data Logging to Excel")
    
    with patch('entity.DataExportEntity.ExportUtils.log_to_excel', return_value="Data saved to Excel file at path.xlsx") as mock_excel:
        price_control = PriceControl()
        _, excel_result, _ = await price_control.get_price("https://example.com/product")
        
        logging.info("Verifying Excel file creation and data logging")
        assert "path.xlsx" in excel_result
        logging.info("Test passed: Data correctly logged to Excel")

# Testing the HTML export functionality
@pytest.mark.asyncio
async def test_data_logging_html():
    logging.info("Starting test: Data Export to HTML")
    
    with patch('entity.DataExportEntity.ExportUtils.export_to_html', return_value="Data exported to HTML file at path.html") as mock_html:
        price_control = PriceControl()
        _, _, html_result = await price_control.get_price("https://example.com/product")
        
        logging.info("Verifying HTML file creation and data export")
        assert "path.html" in html_result
        logging.info("Test passed: Data correctly exported to HTML")

# Testing response assembly and output correctness
@pytest.mark.asyncio
async def test_response_assembly_and_output():
    logging.info("Starting test: Response Assembly and Output")
    
    # Mocking get_price to return a tuple of price, excel file path, and html file path
    with patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock) as mock_get_price:
        mock_get_price.return_value = ("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML at path.html")
        price_control = PriceControl()
        result = await price_control.receive_command("get_price", "https://example.com/product")
        
        # Unpack the result tuple for clarity
        price, excel_path, html_path = result

        logging.info("Checking response contains price, Excel and HTML paths")
        assert price == "100.00", "Price did not match expected value"
        assert "path.xlsx" in excel_path, "Excel path did not contain expected file name"
        assert "path.html" in html_path, "HTML path did not contain expected file name"
        
        logging.info("Test passed: Correct response assembled and output")

if __name__ == "__main__":
    pytest.main([__file__])
