import webview
import os

from utils.get_resources import resource_path
from api.api import Api


def is_dev():
    env = os.environ.get("APP_DEV", default=None)

    if env:
        return "http://localhost:5173"

    if not env:
        return resource_path("frontend/index.html")


renderer = is_dev()
api = Api()

if __name__ == "__main__":
    webview.create_window("Nyanga Read", renderer, js_api=api)
    webview.start(private_mode=False, debug=True)
