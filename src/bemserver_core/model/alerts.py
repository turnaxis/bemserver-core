import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth
from enum import Enum

class AlertType(Enum):
    GREEN = "green"
    ORANGE = "orange"
    RED = "red"

class Alert(AuthMixin, Base):
    __tablename__ = "alerts"

    id = sqla.Column(sqla.Integer, primary_key=True)
    device_id = sqla.Column(sqla.ForeignKey("devices.id"), nullable=False)
    user_id = sqla.Column(sqla.ForeignKey("users.id"), nullable=False)
    alert_type = sqla.Column(sqla.Enum(AlertType), nullable=False)
    threshold = sqla.Column(sqla.Float, nullable=False)
    actual_consumption = sqla.Column(sqla.Float, nullable=False)
    timestamp = sqla.Column(sqla.DateTime, nullable=False, default=sqla.func.now())

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
                "user": Relation(
                    kind="one",
                    other_type="User",
                    my_field="user_id",
                    other_field="id",
                ),
            },
        )
