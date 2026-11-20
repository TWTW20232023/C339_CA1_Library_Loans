
import pytest

from library_fine import calculate_fine


# FINE-001 to FINE-006:
# Test valid overdue days and expected fine amounts.

@pytest.mark.parametrize(
    "days_overdue, expected_fine",
    [
        (0, 0),        # FINE-001: Zero overdue days
        (1, 50),       # FINE-002: One overdue day
        (2, 100),      # FINE-003: Multiple overdue days
        (10, 500),     # FINE-004: Ten overdue days
        (11, 550),     # FINE-005: No maximum fine
        (100, 5000),   # FINE-006: Large overdue value
    ],
    ids=[
        "FINE-001",
        "FINE-002",
        "FINE-003",
        "FINE-004",
        "FINE-005",
        "FINE-006",
    ],
)
def test_calculate_fine_valid_days(days_overdue, expected_fine):
    assert calculate_fine(days_overdue) == expected_fine


# FINE-007:
# Test negative overdue days.

def test_calculate_fine_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-1)


# FINE-008 to FINE-011:
# Test invalid data types.

@pytest.mark.parametrize(
    "days_overdue",
    [
        "5",    # FINE-008: String
        5.0,    # FINE-009: Float
        True,   # FINE-010: Boolean
        None,   # FINE-011: None
    ],
    ids=[
        "FINE-008",
        "FINE-009",
        "FINE-010",
        "FINE-011",
    ],
)
def test_calculate_fine_invalid_type(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
