"""empty message

Revision ID: d5a20530cccf
Revises: 4a1daf6630f0
Create Date: 2024-11-22 14:09:49.922234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5a20530cccf'
down_revision = '4a1daf6630f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('Approved2')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Approved2', mysql.VARCHAR(length=255), nullable=False))

    # ### end Alembic commands ###