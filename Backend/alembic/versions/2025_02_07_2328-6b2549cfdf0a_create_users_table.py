"""create users table

Revision ID: 6b2549cfdf0a
Revises: 
Create Date: 2025-02-07 23:28:06.525621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b2549cfdf0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('users')


def downgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('category_id', sa.INTEGER(),
                  autoincrement=False, nullable=False),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('invate', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('rang', sa.DOUBLE_PRECISION(precision=53),
                  autoincrement=False, nullable=False),
        sa.Column('level', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
