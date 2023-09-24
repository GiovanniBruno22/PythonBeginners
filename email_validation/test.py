import pytest
from email_validation import validate_email

def test_valid_email():
    valid_emails = [
        "test@example.com",
        "john.doe@example.com",
        "info123@example.co.uk",
        "user-name@example.domain"
    ]
    for email in valid_emails:
        assert validate_email(email) == True

def test_invalid_email():
    invalid_emails = [
        "invalid",
        "invalid@",
        "@example.com",
        "user@example",
        "user@.com",
        "user@example..com",
        "user@example_com"
    ]
    for email in invalid_emails:
        assert validate_email(email) == False