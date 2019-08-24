"""add adminboolean column

Revision ID: 4457c67a0c79
Revises: 0f20dd38d0ff
Create Date: 2019-08-24 10:25:56.176609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4457c67a0c79'
down_revision = '0f20dd38d0ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
