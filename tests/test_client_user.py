import pytest


@pytest.mark.asyncio
async def test_search_returns_results(client):
    sample_search_prefix = "TheGodfatherCC"  # Known to exist
    results = await client.search_for_user_by_global_name_prefix(
        prefix=sample_search_prefix
    )
    assert len(results) > 0
    assert sample_search_prefix in [x.bungie_global_display_name for x in results]
