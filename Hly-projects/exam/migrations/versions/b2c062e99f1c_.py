"""empty message

Revision ID: b2c062e99f1c
Revises: 
Create Date: 2018-10-16 23:37:08.583667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c062e99f1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wheel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wheel')
    # ### end Alembic commands ###