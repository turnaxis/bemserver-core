"""remove repeating columns

Revision ID: 799e288b6b1e
Revises: 6a099622c512
Create Date: 2024-08-15 19:02:31.429278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '799e288b6b1e'
down_revision = '6a099622c512'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('alerts', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               nullable=False)
    op.drop_column('alerts', 'consumption')
    op.drop_column('alerts', 'resolved_at')
    op.drop_column('alerts', 'status')
    op.drop_column('alerts', 'resolution_description')
    op.drop_column('alerts', 'action_taken')
    op.drop_column('alerts', 'action_required')
    op.drop_column('alerts', 'created_at')
    op.drop_column('alerts', 'resolved_by')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alerts', sa.Column('resolved_by', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('action_required', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('action_taken', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('resolution_description', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('alerts', sa.Column('resolved_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('alerts', sa.Column('consumption', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.alter_column('alerts', 'timestamp',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###
