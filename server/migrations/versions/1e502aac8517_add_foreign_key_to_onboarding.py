"""add foreign key to onboarding

Revision ID: 1e502aac8517
Revises: aa2e92be97de
Create Date: 2024-10-03 19:11:37.015333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e502aac8517'
down_revision = 'aa2e92be97de'
branch_labels = None
depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('onboardings', sa.Column('employee_id', sa.Integer(), nullable=True))
#     op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'onboardings', 'employees', ['employee_id'], ['id'])
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')
#     op.drop_column('onboardings', 'employee_id')
#     # ### end Alembic commands ###

def upgrade():
    # Use batch mode to safely add the employee_id column and the foreign key
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_onboardings_employee_id_employees'),
            'employees', ['employee_id'], ['id']
        )

def downgrade():
    # Use batch mode to safely remove the foreign key and the column
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
