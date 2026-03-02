# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from app.models.roles import Role
from app.models.user_roles import UserRole

def assign_role(db: Session, user_id: int, role_name: str):
    role = db.query(Role).filter(Role.name == role_name).first()

    if not role:
        raise ValueError("Role not found")

    link = UserRole(user_id=user_id, role_id=role.id)

    db.add(link)
    db.commit()