"""add actual consumption column

Revision ID: 8ae0fa2d843b
Revises: d21c59a52cbd
Create Date: 2024-08-15 05:38:44.166164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae0fa2d843b'
down_revision = 'd21c59a52cbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alerts', sa.Column('actual_consumption', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alerts', 'actual_consumption')
    # ### end Alembic commands ###
