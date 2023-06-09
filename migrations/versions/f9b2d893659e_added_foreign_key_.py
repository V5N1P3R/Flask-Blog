"""Added Foreign Key_

Revision ID: f9b2d893659e
Revises: cae8d2b4800c
Create Date: 2023-05-14 07:57:54.843232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f9b2d893659e'
down_revision = 'cae8d2b4800c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('posts_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['poster_id'], ['id'])
        batch_op.drop_column('proster_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('proster_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('posts_ibfk_1', 'users', ['proster_id'], ['id'])
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###
