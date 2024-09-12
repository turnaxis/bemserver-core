import argon2
import sqlalchemy as sqla
from bemserver_core.authorization import AuthMixin, Relation, auth, get_current_user
from bemserver_core.database import Base
from .users import UserGroup
from bemserver_core.database import db

ph = argon2.PasswordHasher()


class Team(AuthMixin, Base):
    __tablename__ = "teams"

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(80), unique=True, nullable=False)

    # optional
    user_group_id = sqla.Column(sqla.ForeignKey("u_groups.id"), nullable=True)

    user_group = sqla.orm.relationship(
        UserGroup,
        backref=sqla.orm.backref("teams", cascade="all, delete-orphan"),
    )

    def is_admin(self, user):
        """Check if the given user is an admin of the team"""
        member = db.session.query(Member).filter_by(team_id=self.id, user_id=user.id).first()
        return member and member.permission_level == "ADMIN"

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
    name = sqla.Column(sqla.String(80), nullable=False)
    permission_level = sqla.Column(sqla.String(10), nullable=False, default="VIEWER")
    authorized_locations = sqla.Column(sqla.String(255), nullable=True)
    email = sqla.Column(sqla.String(255), nullable=True)
    password = sqla.Column(sqla.String(200), nullable=False)
    date_joined = sqla.Column(sqla.Date, nullable=False)
    team_id = sqla.Column(sqla.ForeignKey("teams.id"), nullable=False)

    team = sqla.orm.relationship(
        "Team",
        backref=sqla.orm.backref("members", cascade="all, delete-orphan"),
    )

    def set_password(self, password: str) -> None:
        auth.authorize(get_current_user(), "update", self)
        self.password = ph.hash(password)

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