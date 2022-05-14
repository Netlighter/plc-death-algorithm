"""fix

Revision ID: 644d0d8aca72
Revises: 0c1e736167ba
Create Date: 2022-05-15 00:11:55.550419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '644d0d8aca72'
down_revision = '0c1e736167ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SENSOR_VALUE', sa.Column('sensor_value_date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('SENSOR_VALUE', 'sensor_value_date')
    # ### end Alembic commands ###