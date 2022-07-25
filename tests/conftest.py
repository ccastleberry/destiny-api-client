import os

from destiny_api_client.client import DestinyClient
from dotenv import load_dotenv
from pytest import fixture

load_dotenv()


@fixture(scope="session")
def client() -> DestinyClient:
    return DestinyClient(api_key=os.environ.get("BUNGIE_API_KEY"))


@fixture()
def sample_search_prefix() -> str:
    return "TheGodfatherCC"
