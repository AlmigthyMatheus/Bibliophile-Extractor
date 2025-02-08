import os

# List of proxies in the format "IP:PORT:USERNAME:PASSWORD".
# Replace these placeholder values with your own proxies or set them via environment variables.
DEFAULT_RAW_PROXIES = [
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD",
    "IP_ADDRESS:PORT:USERNAME:PASSWORD"
]

# List of User Agents for rotation.
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
]

# 2Captcha API Key.
# Replace the default with your actual API key, or better yet, set it via an environment variable.
CAPTCHA_API_KEY = os.environ.get("CAPTCHA_API_KEY", "YOUR_2CAPTCHA_API_KEY")

CAPTCHA_REQUEST_URL = "http://2captcha.com/in.php"
CAPTCHA_RESPONSE_URL = "http://2captcha.com/res.php"
CAPTCHA_POLL_INTERVAL = 5  # in seconds
