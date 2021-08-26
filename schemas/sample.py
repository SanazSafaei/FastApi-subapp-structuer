from typing import Optional, List
from pydantic import Field, EmailStr, validator
from core import BaseModel, Pagination


class TestSchema(BaseModel):
    x: int
    y: int


class SampleBaseSchema(BaseModel):
    test1: str = Field(max_length=10)
    test2: Optional[int] = Field(default=None)
    test3: TestSchema
    test5: Optional[float] = None
    test5: Optional[str] = None


class SampleCreateSchema(BaseModel):
    test1: str = Field(max_length=10)
    test3: TestSchema


class SampleUpdateSchema(SampleCreateSchema):
    pass


class SampleOutDBSchema(SampleCreateSchema):
    pass


class SampleListSchema(Pagination):
    results: List[SampleOutDBSchema] = []
