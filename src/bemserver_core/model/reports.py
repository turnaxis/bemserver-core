import sqlalchemy as sqla
from bemserver_core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


# from timeseries_data import TimeseriesData


class Report(Base):
    __tablename__ = "reports"

    id = sqla.Column(sqla.Integer, primary_key=True)
    location = sqla.Column(sqla.String(100), nullable=True)
    period_start = sqla.Column(sqla.DateTime, nullable=False, default=datetime.utcnow)
    period_end = sqla.Column(sqla.DateTime, nullable=False, default=datetime.utcnow)
    consumption = sqla.Column(sqla.Float, nullable=False)
    cost = sqla.Column(sqla.Float, nullable=False)
    co2_emissions = sqla.Column(sqla.Float, nullable=False)
    renewable_energy_utilization = sqla.Column(sqla.Float, nullable=False)
    peak_usage_time = sqla.Column(sqla.String(50), nullable=False)
    cost_savings = sqla.Column(sqla.Float, nullable=True)

    # Foreign key to device if required, but not necessary for now.
    device_id = sqla.Column(sqla.Integer, sqla.ForeignKey("devices.id"), nullable=True)

    device = relationship("Device", back_populates="reports")


# Function to generate report by location
def get_report_by_location(session, location, period_start, period_end):
    query = (
        session.query(Report)
        .filter(Report.location == location)
        .filter(Report.period_start >= period_start, Report.period_end <= period_end)
    )
    return query.all()


# Function to generate general report for last x days, months or custom period
def get_general_report(session, period_start, period_end):
    query = (
        session.query(Report)
        .filter(Report.period_start >= period_start, Report.period_end <= period_end)
    )
    return query.all()

