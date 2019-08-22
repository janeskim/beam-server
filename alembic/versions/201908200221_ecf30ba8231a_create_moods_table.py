"""Create moods table

Revision ID: ecf30ba8231a
Revises: 81c2cbf4e486
Create Date: 2019-08-20 02:20:32.748119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecf30ba8231a'
down_revision = '81c2cbf4e486'
branch_labels = None
depends_on = None


def upgrade():
    """ Upgrade migration to create moods table """
    op.create_table(
        'moods',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('mood_at', sa.DateTime()),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('color_hex', sa.String(length=6)),
        sa.Column('color_id', sa.Integer(), sa.ForeignKey('colors.id'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    )


def downgrade():
    """ Downgrade migration to drop modds table """
    op.drop_table('moods')
