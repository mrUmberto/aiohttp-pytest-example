"""Initial migration

Revision ID: 76b925fc6e3d
Revises: 
Create Date: 2020-06-25 15:03:27.897213

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '76b925fc6e3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""CREATE EXTENSION IF NOT EXISTS "uuid-ossp";""")
    op.create_table(
        'bread',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True,
        ),
        sa.Column('name', sa.String()),
    )


def downgrade():
    op.drop_table('bread')
