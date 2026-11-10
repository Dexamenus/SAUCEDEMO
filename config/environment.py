import os


BASE_URL = os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com/")
WAIT_TIMEOUT = int(os.getenv("SAUCEDEMO_WAIT_TIMEOUT", "10"))
HEADLESS = os.getenv("SAUCEDEMO_HEADLESS", "false").strip().lower() in {
    "1",
    "true",
    "yes",
}
