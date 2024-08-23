import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth
from enum import Enum
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM
from bemserver_core.model.thresholds import Threshold
from bemserver_core.database import db

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

    resolved = sqla.Column(sqla.Boolean, nullable=False, default=False)
    resolved_at = sqla.Column(sqla.DateTime, nullable=True)
    resolved_by = sqla.Column(sqla.ForeignKey("users.id"), nullable=True)

    threshold = sqla.orm.relationship("Threshold", backref="alerts")
    device = sqla.orm.relationship("Device", backref="alerts")
    
    user = sqla.orm.relationship("User", foreign_keys=[user_id], backref="alerts")
    resolved_user = sqla.orm.relationship("User", foreign_keys=[resolved_by], backref="resolved_alerts")


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
                "resolved_user": Relation(
                    kind="one",
                    other_type="User",
                    my_field="resolved_by",
                    other_field="id",
                ),
                "threshold": Relation(
                    kind="one",
                    other_type="Threshold",
                    my_field="threshold_id",
                    other_field="id",
                ),
            },
        )

    @classmethod
    def get_active_alerts(cls, **kwargs):
        return db.session.query(cls).filter_by(resolved=False, **kwargs).all()

    @classmethod
    def get_resolved_alerts(cls, **kwargs):
        return db.session.query(cls).filter_by(resolved=True, **kwargs).all()

    def mark_resolved(self, user_id):
        self.resolved = True
        self.resolved_by = user_id
        self.resolved_at = datetime.utcnow()
