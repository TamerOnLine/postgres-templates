import sys
import os

# ✅ أضف مجلد المشروع الجذري للمسار ليسمح بالاستيراد من db/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from fastapi import APIRouter
from pydantic import BaseModel
from serve_manager.db_utils import get_pg_session

from db.models.user_section_settings import UserSectionSettings

router = APIRouter()

class SectionUpdate(BaseModel):
    user_id: int
    print_visible: bool | None = None
    order_index: int | None = None

@router.post("/section-settings/{section_id}")
def update_section_settings(section_id: int, payload: SectionUpdate):
    db = get_pg_session()

    setting = db.query(UserSectionSettings).filter_by(
        user_id=payload.user_id,
        section_id=section_id
    ).first()

    if not setting:
        setting = UserSectionSettings(user_id=payload.user_id, section_id=section_id)

    if payload.print_visible is not None:
        setting.print_visible = payload.print_visible
    if payload.order_index is not None:
        setting.order_index = payload.order_index

    db.add(setting)
    db.commit()
    return {"status": "success"}
