"""add reports table

Revision ID: d5a0ee98c472
Revises: 31c4cccc507d
Create Date: 2024-10-17 18:50:51.603685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5a0ee98c472'
down_revision = '31c4cccc507d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('period_start', sa.DateTime(), nullable=False),
    sa.Column('period_end', sa.DateTime(), nullable=False),
    sa.Column('consumption', sa.Float(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('co2_emissions', sa.Float(), nullable=False),
    sa.Column('renewable_energy_utilization', sa.Float(), nullable=False),
    sa.Column('peak_usage_time', sa.Time(), nullable=False),
    sa.Column('cost_savings', sa.Float(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], name=op.f('fk_reports_device_id_devices')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reports'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    # ### end Alembic commands ###