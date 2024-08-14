"""add alerts models

Revision ID: 909e41a1cdd5
Revises: 75d0c05b5f3b
Create Date: 2024-08-14 12:25:16.796303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '909e41a1cdd5'
down_revision = '75d0c05b5f3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('alert_type', sa.Enum('GREEN', 'ORANGE', 'RED', name='alerttype'), nullable=False),
    sa.Column('threshold', sa.Float(), nullable=False),
    sa.Column('actual_consumption', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], name=op.f('fk_alerts_device_id_devices')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_alerts_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_alerts'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alerts')
    # ### end Alembic commands ###
