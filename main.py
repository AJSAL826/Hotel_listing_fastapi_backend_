from fastapi import Depends, FastAPI, HTTPException,status
from sqlalchemy import text
from db_controller import create_datas, get_alldata, get_data, update_prop
from input_schema import Prop_update, prop_det, prop_list
import models
from sqlalchemy.orm import Session


app = FastAPI()

models.base.metadata.create_all(models.engine)

@app.get("/create_data")
def create_data(request:prop_det,db:Session = Depends(models.get_db)):
    """To create property data """
    result=create_datas(request,db)
    return result

@app.post("/get_data")

def data(request:prop_list,db:Session= Depends(models.get_db)):
    """Display the data based on user search"""
    result=get_data(request,db)
    return result


@app.get("/get_alldata")
def data(db:Session= Depends(models.get_db)):
    """Display all the data in database"""
    result=get_alldata(db)
    return result


@app.put("/property_id/{property_id}")
def update_property(property_id: int, request: Prop_update, db: Session = Depends(models.get_db)):
    """To update the data based on users choice """
    if not property_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    details = db.query(models.Registration).filter(models.Registration.id == property_id).first()
    if not details:
        raise HTTPException(status_code=404, detail="Task not found")
    s = update_prop(details, request, db)
    return s
    
@app.delete("/delete_property/{id}")
def delete_property(id:int, db: Session = Depends(models.get_db)):
    """To delete the data based on the user choice"""
    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    db.query(models.Registration).filter(models.Registration.id == id).delete(synchronize_session=False)
    db.commit()
    return {
        "status": "success",
        "message": "successfully deleted these rows",
        "data": "deleted",
        "error": False,
    }

@app.delete("/clear")
def clear_db(db:Session = Depends(models.get_db)):
    """To clear all the data inside the database"""
    db.query(models.Registration).delete()
    db.commit()
    # db.execute(text("ALTER SEQUENCE property_id RESTART WITH 1"))
    # db.commit()