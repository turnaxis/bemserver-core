"""v0.6

Revision ID: 0.6
Revises: 0.4
Create Date: 2023-01-06 16:53:58.160326

"""

from textwrap import dedent
import enum

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "0.6"
down_revision = "0.4"
branch_labels = None
depends_on = None


def gen_ddl_trigger_ro(table_name, col_name):
    return sa.DDL(
        dedent(
            f"""
            CREATE TRIGGER
                {table_name}_trigger_update_readonly_{col_name}
            BEFORE UPDATE
                OF {col_name} ON {table_name}
            FOR EACH ROW
                WHEN (
                    NEW.{col_name} IS DISTINCT FROM OLD.{col_name}
                )
                EXECUTE FUNCTION column_update_not_allowed({col_name});
            """
        )
    )


class EventLevelEnum(enum.IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


def upgrade():
    event_level = postgresql.ENUM(
        EventLevelEnum, name="eventlevelenum", create_type=False
    )

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_categs_by_users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("notification_level", event_level, nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["event_categs.id"],
            name=op.f("fk_event_categs_by_users_category_id_event_categs"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_event_categs_by_users_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_event_categs_by_users")),
        sa.UniqueConstraint(
            "user_id", "category_id", name=op.f("uq_event_categs_by_users_user_id")
        ),
    )
    op.create_table(
        "notifs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("read", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"], ["events.id"], name=op.f("fk_notifs_event_id_events")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_notifs_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_notifs")),
    )
    # ### end Alembic commands ###

    op.execute(gen_ddl_trigger_ro("event_categs_by_users", "user_id"))
    op.execute(gen_ddl_trigger_ro("notifs", "user_id"))
    op.execute(gen_ddl_trigger_ro("notifs", "event_id"))
    op.execute(gen_ddl_trigger_ro("notifs", "timestamp"))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("notifs")
    op.drop_table("event_categs_by_users")
    # ### end Alembic commands ###
