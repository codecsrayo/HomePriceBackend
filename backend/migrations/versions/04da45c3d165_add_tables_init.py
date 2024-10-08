"""add tables init

Revision ID: 04da45c3d165
Revises: 
Create Date: 2024-09-22 22:34:29.367591

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = '04da45c3d165'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ml_models',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('ml_model_tag', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ml_model_version', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ml_models_id'), 'ml_models', ['id'], unique=False)
    op.create_table('properties',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('city', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('state', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('zip_code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('bedrooms', sa.Integer(), nullable=False),
    sa.Column('bathrooms', sa.Integer(), nullable=False),
    sa.Column('square_feet', sa.Integer(), nullable=False),
    sa.Column('lot_size', sa.Integer(), nullable=True),
    sa.Column('year_built', sa.Integer(), nullable=True),
    sa.Column('property_type', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('price', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_properties_id'), 'properties', ['id'], unique=False)
    op.create_table('features',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('property_id', sa.Uuid(), nullable=False),
    sa.Column('feature_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('feature_value', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_features_id'), 'features', ['id'], unique=False)
    op.create_table('predictions',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('property_id', sa.Uuid(), nullable=False),
    sa.Column('predicted_price', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('prediction_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predictions_id'), 'predictions', ['id'], unique=False)
    op.create_table('ml_model_predictions',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('ml_model_id', sa.Uuid(), nullable=False),
    sa.Column('prediction_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['ml_model_id'], ['ml_models.id'], ),
    sa.ForeignKeyConstraint(['prediction_id'], ['predictions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ml_model_predictions_id'), 'ml_model_predictions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ml_model_predictions_id'), table_name='ml_model_predictions')
    op.drop_table('ml_model_predictions')
    op.drop_index(op.f('ix_predictions_id'), table_name='predictions')
    op.drop_table('predictions')
    op.drop_index(op.f('ix_features_id'), table_name='features')
    op.drop_table('features')
    op.drop_index(op.f('ix_properties_id'), table_name='properties')
    op.drop_table('properties')
    op.drop_index(op.f('ix_ml_models_id'), table_name='ml_models')
    op.drop_table('ml_models')
    # ### end Alembic commands ###