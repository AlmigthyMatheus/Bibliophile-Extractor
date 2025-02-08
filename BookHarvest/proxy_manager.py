import random
from config import DEFAULT_RAW_PROXIES, USER_AGENTS

def format_proxy(proxy_str):
    """
    Converts a proxy string in the format "IP:PORT:USERNAME:PASSWORD" to the format
    "http://USERNAME:PASSWORD@IP:PORT".
    """
    parts = proxy_str.split(":")
    if len(parts) != 4:
        return None
    ip, port, username, password = parts
    return f"http://{username}:{password}@{ip}:{port}"

# Format all proxies from the raw list
PROXIES = [format_proxy(proxy) for proxy in DEFAULT_RAW_PROXIES if format_proxy(proxy) is not None]

def get_random_proxy():
    """
    Returns a dictionary with a random proxy for HTTP and HTTPS.
    Example: {'http': 'http://USERNAME:PASSWORD@IP:PORT', 'https': 'http://USERNAME:PASSWORD@IP:PORT'}
    """
    if PROXIES:
        proxy = random.choice(PROXIES)
        return {"http": proxy, "https": proxy}
    else:
        return {}

def get_random_user_agent():
    """
    Returns a random User-Agent string from the list.
    """
    return random.choice(USER_AGENTS)
