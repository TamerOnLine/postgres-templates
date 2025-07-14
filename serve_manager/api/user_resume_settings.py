import sys
import os

# أضف مجلد postgres-templates للجذر
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PARENT_DIR = os.path.abspath(os.path.join(ROOT_DIR, ".."))

if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config import get_db
from db.models.user_resume_settings import UserResumeSettings


router = APIRouter()

@router.post("/user-resume-settings/")
def create_user_resume_settings(settings: dict, db: Session = Depends(get_db)):
    obj = UserResumeSettings(**settings)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/user-resume-settings/")
def get_user_resume_settings(user_id: int, template_id: int, db: Session = Depends(get_db)):
    result = db.query(UserResumeSettings).filter_by(user_id=user_id, template_id=template_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Settings not found")
    return result
