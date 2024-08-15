import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth
from enum import Enum
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM

class AlertType(Enum):
    GREEN = "green"
    ORANGE = "orange"
    RED = "red"

class Alert(AuthMixin, Base):
    __tablename__ = "alerts"

    id = sqla.Column(sqla.Integer, primary_key=True)
    device_id = sqla.Column(sqla.ForeignKey("devices.id"), nullable=False)
    user_id = sqla.Column(sqla.ForeignKey("users.id"), nullable=False)
    threshold = sqla.Column(sqla.Float, nullable=False)
    consumption = sqla.Column(sqla.Float, nullable=False)
    status = sqla.Column(sqla.String(50), nullable=False)  # green, orange, red
    description = sqla.Column(sqla.String(200), nullable=True)
    alert_type = sqla.Column(sqla.Enum(AlertType), nullable=False)
    action_required = sqla.Column(sqla.String(200), nullable=True)
    location = sqla.Column(sqla.String(100), nullable=False)
    created_at = sqla.Column(sqla.DateTime, default=datetime.utcnow)
    resolved_at = sqla.Column(sqla.DateTime, nullable=True)
    resolved_by = sqla.Column(sqla.String(80))
    resolution_description = sqla.Column(sqla.String(200), nullable=True)
    action_taken = sqla.Column(sqla.String(200), nullable=True)
    actual_consumption = sqla.Column(sqla.Float, nullable=True)
    timestamp = sqla.Column(sqla.DateTime, default=datetime.utcnow)

    device = sqla.orm.relationship(
        "Device",
        backref=sqla.orm.backref("alerts", cascade="all, delete-orphan"),
    )

    user = sqla.orm.relationship(
        "User",
        backref=sqla.orm.backref("alerts", cascade="all, delete-orphan"),
    )

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
