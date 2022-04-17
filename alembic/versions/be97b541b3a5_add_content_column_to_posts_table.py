"""add content column to posts table

Revision ID: be97b541b3a5
Revises: 76e3e67a96e4
Create Date: 2022-04-17 12:51:23.488294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be97b541b3a5'
down_revision = '76e3e67a96e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
