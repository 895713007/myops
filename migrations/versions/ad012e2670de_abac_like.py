"""abac like

Revision ID: ad012e2670de
Revises: d164fdb4ed73
Create Date: 2018-04-30 17:26:48.306168

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ad012e2670de'
down_revision = 'd164fdb4ed73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('policy_versions')
    op.add_column('policies', sa.Column('document', sa.JSON(), nullable=False))
    op.drop_column('policies', 'default_version')
    op.add_column('salt', sa.Column('state', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('salt', 'state')
    op.add_column('policies', sa.Column('default_version', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('policies', 'document')
    op.create_table('policy_versions',
    sa.Column('version_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('policy_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('document', mysql.JSON(), nullable=True),
    sa.Column('create_date', mysql.DATETIME(), nullable=True),
    sa.Column('delete_date', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['policy_id'], [u'policies.policy_id'], name=u'policy_versions_ibfk_1'),
    sa.PrimaryKeyConstraint('version_id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###