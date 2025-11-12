from pydantic import BaseModel, Field
from typing import Annotated


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class TeacherInfo(BaseModel):
    name: str
    password: str


class UserInfo(BaseModel):
    name: str
    password: str
    role: str


class InfoStudentResponse(UserInfo):
    group: str


class GradePutRequest(BaseModel):
    student_full_name: str
    discipline: str
    session: str
    grade: int = Field(..., gt=0,le=2)

Grade = Annotated[int, Field(..., ge=2, le=5)]

class MassPutGrades(BaseModel):
    group_name : str
    students: list[str] | None = None
    grades: list[Grade] | None = None