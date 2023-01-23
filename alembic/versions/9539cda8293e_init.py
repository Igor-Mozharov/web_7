"""Init

Revision ID: 9539cda8293e
Revises: 
Create Date: 2023-01-22 20:31:36.785360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9539cda8293e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discipline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('teachers_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teachers_id'], ['teacher.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=100), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('date_of', sa.DateTime(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('discipline_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['discipline_id'], ['discipline.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grade')
    op.drop_table('student')
    op.drop_table('discipline')
    op.drop_table('teacher')
    op.drop_table('group')
    # ### end Alembic commands ###