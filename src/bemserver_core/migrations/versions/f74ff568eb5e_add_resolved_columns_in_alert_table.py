"""add resolved columns in alert table

Revision ID: f74ff568eb5e
Revises: 7d81247e0d4b
Create Date: 2024-08-22 22:03:33.506181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f74ff568eb5e'
down_revision = '7d81247e0d4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alerts', sa.Column('resolved', sa.Boolean(), nullable=False))
    op.add_column('alerts', sa.Column('resolved_at', sa.DateTime(), nullable=True))
    op.add_column('alerts', sa.Column('resolved_by', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_alerts_resolved_by_users'), 'alerts', 'users', ['resolved_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_alerts_resolved_by_users'), 'alerts', type_='foreignkey')
    op.drop_column('alerts', 'resolved_by')
    op.drop_column('alerts', 'resolved_at')
    op.drop_column('alerts', 'resolved')
    # ### end Alembic commands ###
