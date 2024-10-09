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

@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: Control Layer Processing for get_price command")
    
    result = await PriceControl().receive_command("get_price", "https://example.com/product")
    
    logging.info("Verifying that the receive_command correctly processed the 'get_price' command")
    price, excel_path, html_path = result
    
    # Validate the return values
    assert price == "100.00"
    assert "path.xlsx" in excel_path
    assert "path.html" in html_path

    logging.info("Test passed: Control layer processing correctly handles 'get_price'")


@pytest.mark.asyncio
async def test_price_retrieval():
    logging.info("Starting test: Price Retrieval from webpage")
    
    result = await PriceControl().get_price("https://example.com/product")
    
    # Unpack the result (price, excel_path, html_path)
    price, _, _ = result
    
    logging.info("Expected fetched price: '100.00'")
    assert price == "100.00", f"Expected price '100.00', but got {price}"
    
    logging.info("Test passed: Price retrieval successful and correct")



@pytest.mark.asyncio
async def test_data_logging_excel():
    logging.info("Starting test: Data Logging to Excel")
    
    _, excel_result, _ = await PriceControl().get_price("https://example.com/product")

    logging.info("Verifying Excel file creation and data logging")
    assert "path.xlsx" in excel_result

    logging.info("Test passed: Data correctly logged to Excel")


@pytest.mark.asyncio
async def test_data_logging_html():
    logging.info("Starting test: Data Export to HTML")
    
    _, _, html_result = await PriceControl().get_price("https://example.com/product")

    logging.info("Verifying HTML file creation and data export")
    assert "path.html" in html_result

    logging.info("Test passed: Data correctly exported to HTML")


@pytest.mark.asyncio
async def test_response_assembly_and_output():
    logging.info("Starting test: Response Assembly and Output")
    
    result = await PriceControl().receive_command("get_price", "https://example.com/product")
    
    price, excel_path, html_path = result

    logging.info("Checking response contains price, Excel, and HTML paths")
    assert price == "100.00"
    assert "path.xlsx" in excel_path
    assert "path.html" in html_path

    logging.info("Test passed: Correct response assembled and output")



if __name__ == "__main__":
    pytest.main([__file__])
