from .camel_model import CamelModel


class UserSearchPrefixRequest(CamelModel):
    display_name_prefix: str


class UserInfoCard(CamelModel):
    supplemental_display_name: str | None
    icon_path: str
    cross_save_override: int
    applicable_membership_types: list[int]
    is_public: bool
    membership_type: int
    membership_id: int
    display_name: str
    bungie_global_display_name: str
    bungie_global_display_name_code: int | None


class UserSearchResponseDetail(CamelModel):
    bungie_global_display_name: str
    bungie_global_display_name_code: int | None
    bungie_net_membership_id: int | None
    destiny_memberships: list[UserInfoCard]


class UserSearchResponse(CamelModel):
    page: int
    has_more: bool
    search_results: list[UserSearchResponseDetail]
