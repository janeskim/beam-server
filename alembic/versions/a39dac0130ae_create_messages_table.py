"""Create messages table

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
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('messages')
