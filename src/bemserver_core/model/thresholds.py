from datetime import datetime
import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth

class Threshold(AuthMixin, Base):
    __tablename__ = "thresholds"

    id = sqla.Column(sqla.Integer, primary_key=True)
    device_id = sqla.Column(sqla.ForeignKey("devices.id"), nullable=False)
    user_id = sqla.Column(sqla.ForeignKey("users.id"), nullable=False)
    value = sqla.Column(sqla.Float, nullable=False)
    created_at = sqla.Column(sqla.Date, nullable=False, default=datetime.utcnow)

    device = sqla.orm.relationship("Device", backref="thresholds")
    user = sqla.orm.relationship("User", backref="thresholds")

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls, 
            fields={
                "device": Relation(
                    kind="one", 
                    other_type="Device", 
                    my_field="device_id", 
                    other_field="id"
                    ),
                "user": Relation(
                    kind="one", 
                    other_type="User", 
                    my_field="user_id", 
                    other_field="id"
                    ),
            }
        )