from pydantic import BaseModel, ConfigDict, Field

#BaseModel class helps define the structure of data
#Blueprint of what data does our API expects

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)  #from attributes helps the Pydantic to access data through attributes as well
    
    id: int
    date_posted: str