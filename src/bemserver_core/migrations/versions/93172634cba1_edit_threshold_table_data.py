"""edit threshold table data

Revision ID: 93172634cba1
Revises: b0c23e71cece
Create Date: 2024-08-20 09:04:12.858791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93172634cba1'
down_revision = 'b0c23e71cece'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_thresholds_user_id_users', 'thresholds', type_='foreignkey')
    op.drop_column('thresholds', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thresholds', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_thresholds_user_id_users', 'thresholds', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###