"""v0.13

Revision ID: 0.13
Revises: 0.12
Create Date: 2023-04-11 14:42:53.133506

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0.13"
down_revision = "0.12"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "st_dl_weather_data_by_site",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("site_id", sa.Integer(), nullable=False),
        sa.Column("is_enabled", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["site_id"],
            ["sites.id"],
            name=op.f("fk_st_dl_weather_data_by_site_site_id_sites"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_st_dl_weather_data_by_site")),
        sa.UniqueConstraint(
            "site_id", name=op.f("uq_st_dl_weather_data_by_site_site_id")
        ),
    )
    op.add_column("sites", sa.Column("latitude", sa.Float(), nullable=True))
    op.add_column("sites", sa.Column("longitude", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("sites", "longitude")
    op.drop_column("sites", "latitude")
    op.drop_table("st_dl_weather_data_by_site")
    # ### end Alembic commands ###
