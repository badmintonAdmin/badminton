"""create users table

Revision ID: b951cd30f60c
Revises: 
Create Date: 2025-02-07 23:56:08.462144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b951cd30f60c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )


def downgrade():
    op.drop_table('users')
