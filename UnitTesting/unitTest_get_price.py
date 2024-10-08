import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.PriceControl import PriceControl
from entity.PriceEntity import PriceEntity
from test_init import logging

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
    
    with patch('control.PriceControl.PriceControl.get_price', return_value=("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML at path.html")):
        price_control = PriceControl()
        result = await price_control.receive_command("get_price", "https://example.com/product")
        
        logging.info("Checking response contains price, Excel and HTML paths")
        assert all(x in result for x in ["100.00", "path.xlsx", "path.html"])
        logging.info("Test passed: Correct response assembled and output")

if __name__ == "__main__":
    pytest.main([__file__])
