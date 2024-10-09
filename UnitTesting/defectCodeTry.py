import pytest
from unittest.mock import patch, AsyncMock
import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.AvailabilityControl import AvailabilityControl

# Corrected tests based on provided structure and data

@pytest.mark.asyncio
async def test_availability_checking():
    with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability', new_callable=AsyncMock) as mock_check:
        mock_check.return_value = "Availability confirmed"  # Return a realistic string
        result = await AvailabilityControl().check_availability("https://example.com/reservation", "2023-10-10")
        assert "Availability confirmed" in result

if __name__ == "__main__":
    pytest.main([__file__])
