"""empty message

Revision ID: c008184e2145
Revises: 199ccb8de166
Create Date: 2020-11-05 15:56:50.556164

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c008184e2145'
down_revision = '199ccb8de166'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('doenca', 'nome',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('doenca', 'sintomas',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('epidemiologico', 'data_coleta',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('epidemiologico', 'doenca_associada',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('epidemiologico', 'doenca_associada',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('epidemiologico', 'data_coleta',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('doenca', 'sintomas',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('doenca', 'nome',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    # ### end Alembic commands ###
