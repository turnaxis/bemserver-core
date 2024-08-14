import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth
from enum import Enum
from datetime import datetime
from sqlalchemy.orm import relationship
from bemserver_core.model.device import Device
from bemserver_core.model.users import User

class PriorityLevel(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

class Alert(AuthMixin, Base):
    __tablename__ = "alerts"

    id = sqla.Column(sqla.Integer, primary_key=True)
    device_id = sqla.Column(sqla.ForeignKey("devices.id"), nullable=False)
    threshold = sqla.Column(sqla.Float, nullable=False)
    consumption = sqla.Column(sqla.Float, nullable=False)
    status = sqla.Column(sqla.String(50), nullable=False)  # green, orange, red
    description = sqla.Column(sqla.String(200), nullable=True)
    priority = sqla.Column(sqla.Enum(PriorityLevel), nullable=False)
    action_required = sqla.Column(sqla.String(200), nullable=True)
    location = sqla.Column(sqla.String(100), nullable=False)
    created_at = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    resolved_at = sqla.Column(sqla.DateTime, nullable=True)
    resolved_by_user_id = sqla.Column(sqla.ForeignKey("users.id"), nullable=True)
    resolution_description = sqla.Column(sqla.String(200), nullable=True)
    action_taken = sqla.Column(sqla.String(200), nullable=True)

    device = relationship("Device", back_populates="alerts")
    resolved_by_user = relationship("User", back_populates="resolved_alerts")

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls,
            fields={
                "device": Relation(
                    kind="one",
                    other_type="Device",
                    my_field="device_id",
                    other_field="id",
                ),
                "resolved_by_user": Relation(
                    kind="one",
                    other_type="User",
                    my_field="resolved_by_user_id",
                    other_field="id",
                ),
            },
        )


Device.alerts = relationship("Alert", back_populates="device", cascade="all, delete-orphan")
User.resolved_alerts = relationship("Alert", back_populates="resolved_by_user", cascade="all, delete-orphan")