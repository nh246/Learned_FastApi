
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import List, Optional,Literal,Annotated
from config.city_tier import tier_1_cities, tier_2_cities




# Pydantic model to validate incoming data 
class UserInput(BaseModel):
    age:Annotated[int, Field(..., gt=0, lt=120, description="Age must be between 0 and 120")]
    weight:Annotated[float, Field(..., gt=0, description="Weight must be greater than 0")]
    height:Annotated[float, Field(..., gt=0, lt=2.5, description="Height must be in meters and less than 2.5 meters")]
    income_lpa:Annotated[float, Field(..., gt=0, description="Income LPA must be greater than 0")]  
    smoker:Annotated[bool, Field(..., description="Smoker must be a boolean value")]
    city:Annotated[str, Field(..., description="City of residence")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]

# field validator
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        return v.strip().title()


# bmi is a computed field
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
# lifestyle_risk is a computed field
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

# age_group is a computed field

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

# city_tier is a computed field    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3   
