"""Add ai_insights and ai_similar_destinations

Revision ID: 1c9a71bc2ed6
Revises: 
Create Date: 2026-06-02 17:45:53.023154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9a71bc2ed6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('blog_posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ai_insights', sa.VARCHAR(length=250), nullable=True))
        batch_op.add_column(sa.Column('ai_similar_destinations', sa.VARCHAR(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('blog_posts', schema=None) as batch_op:
        batch_op.drop_column('ai_similar_destinations')
        batch_op.drop_column('ai_insights')

    # ### end Alembic commands ###
