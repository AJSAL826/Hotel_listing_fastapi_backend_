
from fastapi import HTTPException,status
from input_schema import prop_list
from models import Registration

def create_datas(request,db):
    """Create the property by adding details"""
    try:
        det=Registration(name=request.name,city=request.city,occupancy=request.occupancy,
                    bathroom_count=request.bathroom_count,state=request.state,
                    country=request.country,pin=request.pin,contact_number=request.contact_number,
                    rate_per_day=request.rate_per_day)
        print(db)
        db.add(det)
        db.commit()
        return {
            "status": "success",
            "message": "successfully created a new user",
            "data": [],
            "error": False,
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Not Created",
        )
    
def get_data(request, db):
    """"Get filtered data based on your search keyword"""
    query = db.query(Registration)
    
    if not (request.name or request.city):
        return {"error": "Either name or city must be provided"}

    if request.name:
        query = query.filter(Registration.name == request.name)
    if request.city:
        query = query.filter(Registration.city == request.city)
    
    if request.rate_min is not None:
        query = query.filter(Registration.rate_per_day >= request.rate_min)
    if request.rate_max is not None:
        query = query.filter(Registration.rate_per_day <= request.rate_max)
    if request.occupancy is not None:
        query = query.filter(Registration.occupancy <= request.occupancy)
    
    properties = query.all()
    if not properties:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Searched element not present"
        )
    return properties


def get_alldata(db):
    """Get all data from the database"""
    properties=db.query(Registration.name,Registration.city, Registration.rate_per_day).all()
    if not properties:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No data found",)
    return properties

def update_prop(det,request,db):
    """Update the data based on the users choice"""
    try:
        update_data = request.dict(exclude_unset=True)
        # print(update_data)
        for field, value in update_data.items():
            if hasattr(det, field):
                setattr(det, field, value)
        db.commit()
        return "updated succesfully"
    except Exception as e:
        db.rollback()
        return f"not updated due to {str(e)}"
