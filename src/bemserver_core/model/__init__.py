"""Model"""

from pathlib import Path

from bemserver_core.model.alerts import Alert
from bemserver_core.model.team import Member, Team

from .campaigns import (
    Campaign,
    CampaignScope,
    UserGroupByCampaign,
    UserGroupByCampaignScope,
)
from .energy import (
    Energy,
    EnergyConsumptionTimeseriesByBuilding,
    EnergyConsumptionTimeseriesBySite,
    EnergyEndUse,
    EnergyProductionTechnology,
    EnergyProductionTimeseriesByBuilding,
    EnergyProductionTimeseriesBySite,
)
from .events import (  # noqa
    Event,
    EventByBuilding,
    EventBySite,
    EventBySpace,
    EventByStorey,
    EventByZone,
    EventCategory,
    EventCategoryByUser,
    EventLevelEnum,
    TimeseriesByEvent,
)
from .notifications import Notification
from .sites import (
    Building,
    BuildingProperty,
    BuildingPropertyData,
    Site,
    SiteProperty,
    SitePropertyData,
    Space,
    SpaceProperty,
    SpacePropertyData,
    Storey,
    StoreyProperty,
    StoreyPropertyData,
    StructuralElementProperty,
    Zone,
    ZoneProperty,
    ZonePropertyData,
)
from .timeseries import (
    Timeseries,
    TimeseriesByBuilding,
    TimeseriesByDataState,
    TimeseriesBySite,
    TimeseriesBySpace,
    TimeseriesByStorey,
    TimeseriesByZone,
    TimeseriesDataState,
    TimeseriesProperty,
    TimeseriesPropertyData,
)
from .timeseries_data import TimeseriesData  # noqa
from .users import User, UserByUserGroup, UserGroup
from .weather import (
    WeatherParameterEnum,
    WeatherTimeseriesBySite,
)
from .authtoken import Token
from .device import Device, DeviceByTimeseries, DeviceCategory

__all__ = [
    "User",
    "UserGroup",
    "UserByUserGroup",
    "Campaign",
    "CampaignScope",
    "UserGroupByCampaign",
    "UserGroupByCampaignScope",
    "StructuralElementProperty",
    "SiteProperty",
    "BuildingProperty",
    "StoreyProperty",
    "SpaceProperty",
    "ZoneProperty",
    "Site",
    "Building",
    "Storey",
    "Space",
    "Zone",
    "SitePropertyData",
    "BuildingPropertyData",
    "StoreyPropertyData",
    "SpacePropertyData",
    "ZonePropertyData",
    "TimeseriesDataState",
    "TimeseriesProperty",
    "Timeseries",
    "TimeseriesPropertyData",
    "TimeseriesByDataState",
    "TimeseriesData",
    "TimeseriesBySite",
    "TimeseriesByBuilding",
    "TimeseriesByStorey",
    "TimeseriesBySpace",
    "TimeseriesByZone",
    "EventLevelEnum",
    "EventCategory",
    "Event",
    "EventCategoryByUser",
    "TimeseriesByEvent",
    "EventBySite",
    "EventByBuilding",
    "EventByStorey",
    "EventBySpace",
    "EventByZone",
    "Notification",
    "Energy",
    "EnergyEndUse",
    "EnergyProductionTechnology",
    "EnergyConsumptionTimeseriesBySite",
    "EnergyConsumptionTimeseriesByBuilding",
    "EnergyProductionTimeseriesBySite",
    "EnergyProductionTimeseriesByBuilding",
    "WeatherParameterEnum",
    "WeatherTimeseriesBySite",
    "Token",
    "Team",
    "Member",
    "Alert",
]


AUTH_MODEL_CLASSES = [
    User,
    UserGroup,
    UserByUserGroup,
    Campaign,
    CampaignScope,
    UserGroupByCampaign,
    UserGroupByCampaignScope,
    StructuralElementProperty,
    SiteProperty,
    BuildingProperty,
    StoreyProperty,
    SpaceProperty,
    ZoneProperty,
    Site,
    Building,
    Storey,
    Space,
    Zone,
    SitePropertyData,
    BuildingPropertyData,
    StoreyPropertyData,
    SpacePropertyData,
    ZonePropertyData,
    TimeseriesDataState,
    TimeseriesProperty,
    Timeseries,
    TimeseriesPropertyData,
    TimeseriesByDataState,
    TimeseriesBySite,
    TimeseriesByBuilding,
    TimeseriesByStorey,
    TimeseriesBySpace,
    TimeseriesByZone,
    EventCategory,
    Event,
    EventCategoryByUser,
    TimeseriesByEvent,
    EventBySite,
    EventByBuilding,
    EventByStorey,
    EventBySpace,
    EventByZone,
    Notification,
    Energy,
    EnergyEndUse,
    EnergyProductionTechnology,
    EnergyConsumptionTimeseriesBySite,
    EnergyConsumptionTimeseriesByBuilding,
    EnergyProductionTimeseriesBySite,
    EnergyProductionTimeseriesByBuilding,
    WeatherTimeseriesBySite,
    Token,
    Team,
    Member,
    Alert,
]


AUTH_POLAR_FILE = Path(__file__).parent / "authorization.polar"
