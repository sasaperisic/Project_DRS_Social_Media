"""empty message

Revision ID: 55a7135ced0c
Revises: d97ed1eb396f
Create Date: 2024-11-19 15:32:18.194345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '55a7135ced0c'
down_revision = 'd97ed1eb396f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('ID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Username', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('Txt', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('ImagePath', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('Approved', mysql.VARCHAR(length=255), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###