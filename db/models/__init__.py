from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ✅ اجعل جميع الموديلات تستورد Base من هنا
from .user import User
# يمكنك إضافة جميع الموديلات الأخرى هنا بنفس الشكل
