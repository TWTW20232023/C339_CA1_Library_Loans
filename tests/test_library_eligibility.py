
import pytest

from library_eligibility import can_borrow


# ELIG-001 to ELIG-008:
# Test valid borrowing eligibility conditions.

@pytest.mark.parametrize(
    "active_loans, overdue_books, expected_result",
    [
        (0, 0, True),    # ELIG-001: No active loans
        (1, 0, True),    # ELIG-002: One active loan
        (4, 0, True),    # ELIG-003: Below borrowing limit
        (5, 0, False),   # ELIG-004: Exactly five active loans
        (6, 0, False),   # ELIG-005: Above borrowing limit
        (0, 1, False),   # ELIG-006: Overdue books
        (4, 1, False),   # ELIG-007: Active loans and overdue books
        (5, 2, False),   # ELIG-008: Five loans and overdue books
    ],
    ids=[
        "ELIG-001",
        "ELIG-002",
        "ELIG-003",
        "ELIG-004",
        "ELIG-005",
        "ELIG-006",
        "ELIG-007",
        "ELIG-008",
    ],
)
def test_can_borrow_valid_inputs(
    active_loans, overdue_books, expected_result
):
    result = can_borrow(active_loans, overdue_books)

    assert result == expected_result
    assert type(result) is bool


# ELIG-009 and ELIG-010:
# Test negative values.

@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        (-1, 0),    # ELIG-009: Negative active loans
        (0, -1),    # ELIG-010: Negative overdue books
    ],
    ids=[
        "ELIG-009",
        "ELIG-010",
    ],
)
def test_can_borrow_negative_values(active_loans, overdue_books):
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


# ELIG-011 to ELIG-018:
# Test invalid data types.

@pytest.mark.parametrize(
    "active_loans, overdue_books",
    [
        ("5", 0),   # ELIG-011: String active loans
        (5.0, 0),   # ELIG-012: Float active loans
        (True, 0),  # ELIG-013: Boolean active loans
        (0, "1"),   # ELIG-014: String overdue books
        (0, 1.0),   # ELIG-015: Float overdue books
        (0, True),  # ELIG-016: Boolean overdue books
        (None, 0),  # ELIG-017: None active loans
        (0, None),  # ELIG-018: None overdue books
    ],
    ids=[
        "ELIG-011",
        "ELIG-012",
        "ELIG-013",
        "ELIG-014",
        "ELIG-015",
        "ELIG-016",
        "ELIG-017",
        "ELIG-018",
    ],
)
def test_can_borrow_invalid_types(active_loans, overdue_books):
    with pytest.raises(TypeError):
        can_borrow(active_loans, overdue_books)
