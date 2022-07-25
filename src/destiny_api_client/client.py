import aiohttp

from .models.user_models import (
    UserSearchPrefixRequest,
    UserSearchResponse,
    UserSearchResponseDetail,
)

BASE_API_URL = "https://www.bungie.net/Platform"


class DestinyClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def say_hello(self):
        print("hello")

    async def search_for_user_by_global_name_prefix(
        self, prefix: str
    ) -> list[UserSearchResponseDetail]:
        post_payload = UserSearchPrefixRequest(display_name_prefix=prefix).dict(
            by_alias=True
        )
        async with aiohttp.ClientSession() as session:
            next_page = 0
            has_more = True
            resp_detail_list: list[UserSearchResponseDetail] = []
            while has_more:
                response = await session.post(
                    url=BASE_API_URL + f"/User/Search/GlobalName/{next_page}/",
                    headers={
                        "X-API-Key": self.api_key,
                        "Content-Type": "application/json",
                    },
                    json=post_payload,
                )
                last_resp = UserSearchResponse.parse_obj(
                    (await response.json())["Response"]
                )
                for detail in last_resp.search_results:
                    resp_detail_list.append(detail)
                has_more = last_resp.has_more
                next_page = last_resp.page + 1
            return resp_detail_list


async def main():
    load_dotenv()
    client = DestinyClient(os.environ.get("BUNGIE_API_KEY"))
    search_name = "TheGodfatherCC"
    search_results = await client.search_for_user_by_global_name_prefix(
        prefix=search_name
    )
    for result in search_results:
        print("-" * 30)
        pprint(result.dict(by_alias=False))


if __name__ == "__main__":
    import asyncio
    import os
    from pprint import pprint

    from dotenv import load_dotenv

    asyncio.run(main())
