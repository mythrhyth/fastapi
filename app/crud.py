from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_health_record(db: Session, record: schemas.HealthRecordCreate):
    db_record = models.HealthRecord(
        user_id=record.user_id,
        weight=record.weight,
        height=record.height,
        blood_pressure=record.blood_pressure
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_health_records_by_user(db: Session, user_id: int):
    return db.query(models.HealthRecord).filter(models.HealthRecord.user_id == user_id).all()

def get_all_users(db: Session):
    return db.query(models.User).all()
