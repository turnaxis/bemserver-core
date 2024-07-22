from bemserver_core.model import User
import sqlalchemy as sqla
from bemserver_core.database import Base
from bemserver_core.authorization import AuthMixin, Relation, auth


class Token(AuthMixin, Base):
    __tablename__ = "authenticationtoken"

    id = sqla.Column(sqla.Integer, primary_key=True)
    token = sqla.Column(sqla.String(6), nullable=True)
    token_expiry = sqla.Column(sqla.DateTime())
    token_type = sqla.Column(sqla.String(20))
    user_id = sqla.Column(sqla.Integer, sqla.ForeignKey(User.id), nullable=True)
  
    user = sqla.orm.relationship(User, backref="auth_tokens")

    @classmethod
    def register_class(cls):
        auth.register_class(
            cls,
            fields={
                "site": Relation(
                    kind="one",
                    other_type="User",
                    my_field="user_id",
                    other_field="id",
                ),
            },
        )
