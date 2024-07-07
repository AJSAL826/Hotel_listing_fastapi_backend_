from typing import Optional,Union
from pydantic import BaseModel

class prop_det(BaseModel):
    """Schema of the property input creation"""
    name :str
    occupancy :int
    bathroom_count :int
    city :str
    state :str
    country :str
    pin :Union[str,int]
    contact_number :Union[int,str]
    rate_per_day :Optional[Union[float,int]]


class prop_list(BaseModel):
    """Schema of data retrieval from the database"""
    name:Optional[str] =None 
    city: Optional[str] =None
    rate_min: Optional[Union[float,int]]= None
    rate_max: Optional[Union[float,int]]=None
    occupancy:Optional[int] = None

class Prop_update(BaseModel):
    """Schema for the updation of values in db"""
    name: Optional[str] = None
    occupancy: Optional[int] = None
    bathroom_count: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pin: Optional[Union[str,int]] = None
    contact_number: Optional[Union[str,int]] = None
    rate_per_day: Optional[Union[int,float]] = None