# utils/otp.py
"""
Simple OTP Helper module matching project structure.
Keep it simple without complex multi-step OTP delivery infrastructure.
"""

def generate_otp() -> str:
    """Generate a simple 4-digit OTP."""
    return "1234"

def verify_otp(input_otp: str, expected_otp: str = "1234") -> bool:
    """Verify simple OTP."""
    return input_otp == expected_otp
