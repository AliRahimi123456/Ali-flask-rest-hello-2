"""empty message

Revision ID: 242817618f99
Revises: 7e2e60c21a30
Create Date: 2024-06-07 22:31:58.488963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '242817618f99'
down_revision = '7e2e60c21a30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('home_planet', sa.Integer(), nullable=True))
        batch_op.drop_constraint('person_resident_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['home_planet'], ['id'])
        batch_op.drop_column('homeworld')
        batch_op.drop_column('resident_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('resident_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('homeworld', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('person_resident_id_fkey', 'planet', ['resident_id'], ['id'])
        batch_op.drop_column('home_planet')

    # ### end Alembic commands ###
