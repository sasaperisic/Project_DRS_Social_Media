"""empty message

Revision ID: a1b4c9123939
Revises: 
Create Date: 2024-11-22 14:06:54.176921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b4c9123939'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('ID', sa.String(length=255), nullable=False),
    sa.Column('Username', sa.String(length=255), nullable=False),
    sa.Column('Txt', sa.String(length=255), nullable=False),
    sa.Column('ImagePath', sa.String(length=255), nullable=False),
    sa.Column('Approved', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###

