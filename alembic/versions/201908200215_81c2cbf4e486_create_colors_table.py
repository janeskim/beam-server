"""Create colors table

Revision ID: 81c2cbf4e486
Revises: a39dac0130ae
Create Date: 2019-08-20 02:16:15.872693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81c2cbf4e486'
down_revision = 'a39dac0130ae'
branch_labels = None
depends_on = None


def upgrade():
    """ Upgrade migration to create colors table """
    op.create_table(
        'colors',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('hex_code', sa.String(length=50), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
    )


def downgrade():
    """ Downgrade migration to drop colors table """
    op.drop_table('colors')
