"""create entries table

Revision ID: fb81ff3dab03
Revises:
Create Date: 2023-11-10 18:49:33.257091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'fb81ff3dab03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('entries',
                    sa.Column('id', UUID(as_uuid=True), primary_key=True, index=True, unique=True),
                    sa.Column('start_time', sa.TIMESTAMP(timezone=True)),
                    sa.Column('stop_time', sa.TIMESTAMP(timezone=True)),
                    sa.Column('type', sa.String(10)),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              default=sa.func.now()),
                    sa.Column('modified_at', sa.TIMESTAMP(timezone=True),
                              default=sa.func.now(), onupdate=sa.func.now()))


def downgrade() -> None:
    op.drop_table('entries')
