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
    threshold_id = sqla.Column(sqla.ForeignKey("thresholds.id"), nullable=True)
    description = sqla.Column(sqla.String(200), nullable=True)
    alert_type = sqla.Column(sqla.Enum(AlertType), nullable=False)
    location = sqla.Column(sqla.String(100), nullable=False)
    actual_consumption = sqla.Column(sqla.Float, nullable=True)
    timestamp = sqla.Column(sqla.Date, nullable=False)

    threshold = sqla.orm.relationship("Threshold", backref="alerts")
    device = sqla.orm.relationship("Device", backref="alerts")
    user = sqla.orm.relationship("User", backref="alerts")

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
                "user": Relation(
                    kind="one",
                    other_type="User",
                    my_field="user_id",
                    other_field="id",
                ),
            },
        )
