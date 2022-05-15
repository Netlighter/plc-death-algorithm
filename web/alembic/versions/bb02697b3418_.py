"""empty message

Revision ID: bb02697b3418
Revises: 
Create Date: 2022-05-15 11:04:51.464570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, DropSequence
from database.tables import sensor_table_sequence, accident_type_table_sequence, tool_table_sequence


# revision identifiers, used by Alembic.
revision = 'bb02697b3418'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(CreateSequence(sensor_table_sequence))
    op.execute(CreateSequence(accident_type_table_sequence))
    op.execute(CreateSequence(tool_table_sequence))
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TOOL',
    sa.Column('tool_id', sa.Integer(), server_default=sa.text("nextval('tool_id_seq')"), nullable=False),
    sa.Column('tool_name', sa.String(), nullable=False),
    sa.Column('tool_state', sa.String(), nullable=False),
    sa.Column('tool_accident', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('tool_id')
    )
    op.create_table('ACCIDENT_TYPE',
    sa.Column('accident_type_id', sa.Integer(), server_default=sa.text("nextval('accident_type_id_seq')"), nullable=False),
    sa.Column('accident_type', sa.String(), nullable=False),
    sa.Column('tool_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tool_id'], ['TOOL.tool_id'], ),
    sa.PrimaryKeyConstraint('accident_type_id')
    )
    op.create_table('SENSOR',
    sa.Column('sensor_id', sa.Integer(), server_default=sa.text("nextval('sensor_id_seq')"), nullable=False),
    sa.Column('sensor_name', sa.String(), nullable=False),
    sa.Column('sensor_type', sa.String(), nullable=False),
    sa.Column('tool_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tool_id'], ['TOOL.tool_id'], ),
    sa.PrimaryKeyConstraint('sensor_id')
    )
    op.create_table('ACCIDENT',
    sa.Column('accident_type_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.Column('accident_name', sa.String(), nullable=False),
    sa.Column('accident_status', sa.String(), nullable=False),
    sa.Column('accident_logs', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['accident_type_id'], ['ACCIDENT_TYPE.accident_type_id'], ),
    sa.PrimaryKeyConstraint('accident_type_id', 'data')
    )
    op.create_table('SENSOR_VALUE',
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('sensor_value_date', sa.DateTime(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['sensor_id'], ['SENSOR.sensor_id'], ),
    sa.PrimaryKeyConstraint('sensor_id', 'sensor_value_date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('SENSOR_VALUE')
    op.drop_table('ACCIDENT')
    op.drop_table('SENSOR')
    op.drop_table('ACCIDENT_TYPE')
    op.drop_table('TOOL')
    # ### end Alembic commands ###