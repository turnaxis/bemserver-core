"""remove user id column

Revision ID: 539e3808a99b
Revises: e179e65c2ed7
Create Date: 2024-09-11 22:01:05.637489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '539e3808a99b'
down_revision = 'e179e65c2ed7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_members_user_id_users', 'members', type_='foreignkey')
    op.drop_column('members', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_members_user_id_users', 'members', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###