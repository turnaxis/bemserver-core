import sqlalchemy as sqla
from bemserver_core.authorization import AuthMixin, Relation, auth
from bemserver_core.database import Base
from .users import UserGroup


class Team(AuthMixin, Base):
    __tablename__ = "teams"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(80), unique=True, nullable=False)
    user_group_id = sqla.Column(sqla.ForeignKey("u_groups.id"), nullable=False)

    user_group = sqla.orm.relationship(
        UserGroup,
        backref=sqla.orm.backref("teams", cascade="all, delete-orphan"),
    )

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls,
            fields={
                "user_group": Relation(
                    kind="one",
                    other_type="UserGroup",
                    my_field="user_group_id",
                    other_field="id",
                ),
                "members": Relation(
                    kind="many",
                    other_type="Member",
                    my_field="id",
                    other_field="team_id"
                )
            },
        )

class Member(AuthMixin, Base):
    __tablename__ = "members"

    id = sqla.Column(sqla.Integer, primary_key=True)
    first_name = sqla.Column(sqla.String(80), nullable=False)
    last_name = sqla.Column(sqla.String(80), nullable=False)
    permission_level = sqla.Column(sqla.String(10), nullable=False)
    authorized_locations = sqla.Column(sqla.String(255), nullable=True)
    contact_information = sqla.Column(sqla.String(255), nullable=True)
    date_joined = sqla.Column(sqla.Date, nullable=False)
    team_id = sqla.Column(sqla.ForeignKey("teams.id"), nullable=False)

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls,
            fields={
                "team": Relation(
                    kind="one",
                    other_type="Team",
                    my_field="team_id",
                    other_field="id"
                )
            }
        )