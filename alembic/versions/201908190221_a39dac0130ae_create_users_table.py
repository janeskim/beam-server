"""Create users table

Revision ID: a39dac0130ae
Revises:
Create Date: 2019-08-18 02:02:19.473094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a39dac0130ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """ Upgrade migration to create users table """
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('_password', sa.String(length=255), nullable=False),
    )

def downgrade():
    """ Downgrade migration to drop users table """
    op.drop_table('users')
