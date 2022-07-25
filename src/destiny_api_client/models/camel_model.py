from pydantic import BaseModel


def snake_to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


class CamelModel(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
