from pydantic import BaseModel,Field,EmailStr
from typing import Optional
class Student(BaseModel):
    name: str = "unknown_user"
    age: int = Field(gt=18,lt=23,default=18,description="an field for storing student age in int formate")
    email: Optional[EmailStr]=None
    # email: EmailStr

std1 = {'name':'sahil','email':'sahil@vit.com'}
std2 = {}
student1 = Student(**std1)
student2 = Student(**std2)
print(student1)
print(student2)