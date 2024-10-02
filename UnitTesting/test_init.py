import sys, os, logging, pytest, asyncio
import subprocess
from unittest.mock import patch, MagicMock
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.email_utils import send_email_with_attachments
from control.BrowserControl import BrowserControl
from control.AccountControl import AccountControl
from control.AvailabilityControl import AvailabilityControl
from control.PriceControl import PriceControl
from control.BotControl import BotControl
from DataObjects.AccountDAO import AccountDAO
from entity.AvailabilityEntity import AvailabilityEntity
from entity.BrowserEntity import BrowserEntity
from entity.PriceEntity import PriceEntity
#pytest -v > test_results.txt
#Run this command in the terminal to save the test results to a file

async def run_monitoring_loop(control_object, check_function, url, date_str, frequency, iterations=1):
    """Run the monitoring loop for a control object and execute a check function."""
    control_object.is_monitoring = True
    results = []

    while control_object.is_monitoring and iterations > 0:
        try:
            result = await check_function(url, date_str)
        except Exception as e:
            result = f"Failed to monitor: {str(e)}"
        logging.info(f"Monitoring Iteration: {result}")
        results.append(result)
        iterations -= 1
        await asyncio.sleep(frequency)

    control_object.is_monitoring = False
    results.append("Monitoring stopped successfully!")
    
    return results

def setup_logging():
    """Set up logging without timestamp and other unnecessary information."""
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logging.basicConfig(level=logging.INFO, format='%(message)s')


def save_test_results_to_file(output_file="test_results.txt"):
    """Helper function to run pytest and save results to a file."""
    print("Running tests and saving results to file...")
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file)
    with open(output_path, 'w') as f:
        # Use subprocess to call pytest and redirect output to file
        subprocess.run(['pytest', '-v'], stdout=f, stderr=subprocess.STDOUT)
        
# Custom fixture for logging test start and end
@pytest.fixture(autouse=True)
def log_test_start_end(request):
    test_name = request.node.name
    logging.info(f"------------------------------------------------------\nStarting test: {test_name}\n")
    
    # Yield control to the test function
    yield
    
    # Log after the test finishes
    logging.info(f"\nFinished test: {test_name}\n------------------------------------------------------")


@pytest.fixture
def base_test_case():
    """Base test setup that can be used by all test functions."""
    test_case = MagicMock()
    test_case.browser_control = BrowserControl()
    test_case.account_control = AccountControl()
    test_case.availability_control = AvailabilityControl()
    test_case.price_control = PriceControl()
    test_case.bot_control = BotControl()
    test_case.account_dao = AccountDAO()
    test_case.availability_entity = AvailabilityEntity()
    test_case.browser_entity = BrowserEntity()
    test_case.price_entity = PriceEntity()
    test_case.email_dao = send_email_with_attachments
    return test_case

if __name__ == "__main__":
    # Save the pytest output to a file in the same folder
    save_test_results_to_file(output_file="test_results.txt")