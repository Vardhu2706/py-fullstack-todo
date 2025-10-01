"""Create Phone Number for Users Table

Revision ID: 9bf64a1d5e1d
Revises: 
Create Date: 2025-09-26 11:34:40.361038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9bf64a1d5e1d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column(
            'phone_number',
            sa.String(15),
            nullable=True
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column(
        'users',
        'phone_number'
    )
