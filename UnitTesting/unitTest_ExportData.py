import pandas as pd
import pytest
from unittest.mock import MagicMock, patch
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging

# Initialize logging
setup_logging()

@pytest.mark.usefixtures("base_test_case")
class TestExportUtils:

    @pytest.fixture
    def setup_mocked_paths(self, mocker):
        mocker.patch('os.path.exists', return_value=False)
        mocker.patch('os.makedirs')  # Mock directory creation
        mocker.patch('pandas.DataFrame.to_excel')  # Mock the Excel export method
        mocker.patch('builtins.open', mocker.mock_open())  # Mock open for HTML writing
        logging.info("Mocks for os.path, os.makedirs, pandas.to_excel, and open set up successfully.")

    def test_positive_html_export(self, base_test_case, setup_mocked_paths):
        # Test positive case for HTML export
        result = base_test_case.export_utils.export_to_html("test_command", "http://example.com", "Success")
        
        # Assert and log the result
        assert "HTML file saved and updated" in result
        logging.info(f"Result: {result}")
        logging.info("Test positive HTML export passed successfully.")

    def test_positive_excel_export(self, base_test_case, setup_mocked_paths):
        # Mock reading from Excel and test positive case for Excel export
        with patch('pandas.read_excel', return_value=pd.DataFrame(columns=["Timestamp", "Command", "URL", "Result", "Entered Date", "Entered Time"])):
            result = base_test_case.export_utils.log_to_excel("test_command", "http://example.com", "Success")
            
            # Assert and log the result
            assert "Data saved to Excel file" in result
            logging.info(f"Result: {result}")
            logging.info("Test positive Excel export passed successfully.")

    def test_negative_html_export(self, base_test_case, setup_mocked_paths):
        # Simulate an error during HTML export by raising an exception
        with patch('builtins.open', side_effect=Exception("Failed to write HTML")):
            try:
                result = base_test_case.export_utils.export_to_html("test_command", "http://example.com", "Success")
            except Exception as e:
                # Assert that the correct exception was raised and log the result
                assert str(e) == "Failed to write HTML"
                logging.info(f"Expected exception caught: {str(e)}")
                logging.info("Test negative HTML export passed with expected exception.")

    def test_negative_excel_export(self, base_test_case, setup_mocked_paths):
        # Simulate an error during Excel export by raising an exception
        with patch('pandas.DataFrame.to_excel', side_effect=Exception("Failed to write Excel")):
            try:
                result = base_test_case.export_utils.log_to_excel("test_command", "http://example.com", "Success")
            except Exception as e:
                # Assert that the correct exception was raised and log the result
                assert str(e) == "Failed to write Excel"
                logging.info(f"Expected exception caught: {str(e)}")
                logging.info("Test negative Excel export passed with expected exception.")



if __name__ == '__main__':
    logging.info("Starting pytest for TestExportUtils...")
    pytest.main([__file__])
