from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class PolarSearchConfig(BaseSettings):
    """
    PolarSearch configs
    """

    POLARSEARCH_URL: Optional[str] = Field(
        description="PolarSearch url",
        default=None,
    )
    POLARSEARCH_USERNAME: Optional[str] = Field(
        description="PolarSearch user",
        default=None,
    )
    POLARSEARCH_PASSWORD: Optional[str] = Field(
        description="PolarSearch password",
        default=None,
    )
    DEFAULT_INDEX_TYPE: Optional[str] = Field(
        description="PolarSearch Vector Index Type, hnsw or flat is available in dify",
        default="hnsw",
    )
    DEFAULT_DISTANCE_TYPE: Optional[str] = Field(
        description="Vector Distance Type, support l2, cosinesimil, innerproduct", default="l2"
    )
    USING_UGC_INDEX: Optional[bool] = Field(
        description="Using UGC index will store the same type of Index in a single index but can retrieve separately.",
        default=False,
    )