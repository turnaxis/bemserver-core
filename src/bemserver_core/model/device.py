import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth
from enum import Enum


class DeviceStatus(Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    DISABLED = "disabled"


class DeviceCategory(AuthMixin, Base):
    __tablename__ = "devicecategory"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(100))


class Device(AuthMixin, Base):
    __tablename__ = "devices"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(100))
    unique_identifier = sqla.Column(sqla.String(50), unique=True)
    status = sqla.Column(sqla.Enum(DeviceStatus), nullable=False)
    energy_rating = sqla.Column(sqla.String(20), nullable=True)
    device_category_id = sqla.Column(
        sqla.ForeignKey("devicecategory.id"), nullable=False
    )
    installation_date = sqla.Column(sqla.Date())
    manufacturer = sqla.Column(sqla.String(50))
    model = sqla.Column(sqla.String(50))
    building_id = sqla.Column(sqla.ForeignKey("buildings.id"), nullable=False)

    device_category = sqla.orm.relationship(
        DeviceCategory,
        backref=sqla.orm.backref("devices", cascade="all, delete-orphan"),
    )

    building = sqla.orm.relationship(
        "Building",
        backref=sqla.orm.backref("devices", cascade="all, delete-orphan"),
    )

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls,
            fields={
                "device_category": Relation(
                    kind="one",
                    other_type="DeviceCategory",
                    my_field="device_category_id",
                    other_field="id",
                ),
                "building": Relation(
                    kind="one",
                    other_type="Building",
                    my_field="building_id",
                    other_field="id",
                ),
            },
        )


class DeviceByTimeseries(AuthMixin, Base):
    __tablename__ = "devices_by_timeseries"
    __table_args__ = (sqla.UniqueConstraint("device_id", "timeseries_id"),)

    id = sqla.Column(sqla.Integer, primary_key=True)
    device_id = sqla.Column(sqla.ForeignKey("devices.id"), nullable=False)
    timeseries_id = sqla.Column(sqla.ForeignKey("timeseries.id"), nullable=False)

    device = sqla.orm.relationship(
        Device,
        backref=sqla.orm.backref("devices_by_timeseries", cascade="all, delete-orphan"),
    )

    timeseries = sqla.orm.relationship(
        "Timeseries",
        backref=sqla.orm.backref("devices_by_timeseries", cascade="all, delete-orphan"),
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
                "timeseries": Relation(
                    kind="one",
                    other_type="Timeseries",
                    my_field="timeseries_id",
                    other_field="id",
                ),
                "building": Relation(
                    kind="one",
                    other_type="Building",
                    my_field="building_id",
                    other_field="id",
                ),
            },
        )
