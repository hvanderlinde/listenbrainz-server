import os

# Location new parquet dump listen files
LISTENBRAINZ_NEW_DATA_DIRECTORY = os.path.join('/', 'data', 'listenbrainz-new')

# path to save incremental dumps
INCREMENTAL_DUMPS_SAVE_PATH = os.path.join(LISTENBRAINZ_NEW_DATA_DIRECTORY, "incremental.parquet")

# Directory containing similar artist relation.
# (This is a temporary path till incremental dumps for similar artists are prepared)
SIMILAR_ARTIST_DIR = '/similar_artists'
# Absolute path to similar artist relation.
SIMILAR_ARTIST_DATAFRAME_PATH = SIMILAR_ARTIST_DIR + \
    '/' + 'artist_credit_artist_credit_relations.parquet'
# Directory containing RDD checkpoints to break lineage while using iterative algorithms.
CHECKPOINT_DIR = os.path.join('/', 'checkpoint')

################################################
# Recommendation `recording` absolute path/dir #
################################################

# Parent directory containing data used in and generated by `recording` recommendation engine.
RECOMMENDATION_RECORDING_PARENT_DIR = os.path.join('/', 'recommendation')
# Directory containing dataframes to be used in generating `recording` recommendations (not necessarily).
RECOMMENDATION_RECORDING_DATAFRAME_DIR = os.path.join(
    RECOMMENDATION_RECORDING_PARENT_DIR, 'dataframe')
# Directory containing model metadata and the real models to be used for generating `recording` recommendations.
RECOMMENDATION_RECORDING_MODEL_DIR = os.path.join(
    RECOMMENDATION_RECORDING_PARENT_DIR, 'model')
# Directory containing candidate sets to be used for generating recommendations.
RECOMMENDATION_RECORDING_CANDIDATE_SET_DIR = os.path.join(
    RECOMMENDATION_RECORDING_PARENT_DIR, 'candidate_set')
# Directory to save best models for `recording` recommendations.
RECOMMENDATION_RECORDING_DATA_DIR = os.path.join(
    RECOMMENDATION_RECORDING_MODEL_DIR, 'data')

# Absolute path to dataframes used in processing raw data/listens for `recording` recommendations.
RECOMMENDATION_RECORDING_USERS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'users_df.parquet'
RECOMMENDATION_RECORDINGS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'recordings_df.parquet'
# Absolute path to processed data/listens ready to be trained for `recording` recommendations.
RECOMMENDATION_RECORDING_PLAYCOUNTS_DATAFRAME = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'playcounts_df.parquet'
# Absolute path to candidate sets used in `recording` recommendations.
RECOMMENDATION_RECORDING_TOP_ARTIST_CANDIDATE_SET = os.path.join(RECOMMENDATION_RECORDING_CANDIDATE_SET_DIR,
                                                                 'top_artist',
                                                                 'top_artist.parquet')
RECOMMENDATION_RECORDING_SIMILAR_ARTIST_CANDIDATE_SET = os.path.join(RECOMMENDATION_RECORDING_CANDIDATE_SET_DIR,
                                                                     'similar_artist',
                                                                     'similar_artist.parquet')
# Absolute path to model metadata.
RECOMMENDATION_RECORDING_MODEL_METADATA = RECOMMENDATION_RECORDING_MODEL_DIR + \
    '/' + 'model_metadata_new.parquet'
# Absolute path to mapped listens.
RECOMMENDATION_RECORDING_MAPPED_LISTENS = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'mapped_listens_df.parquet'
# Absolute path to save dataframe metadata
RECOMMENDATION_RECORDING_DATAFRAME_METADATA = RECOMMENDATION_RECORDING_DATAFRAME_DIR + \
    '/' + 'dataframe_metadata.parquet'

#######################################################
# All the paths/dirs for `recording` recommendations  #
# should be contained within this block               #
#######################################################

# Absolute path to save import metadata
IMPORT_METADATA = "/import_metadata.parquet"

# Path to files downloaded from FTP.
FTP_FILES_PATH = '/rec/listenbrainz_spark'

###########################################
# paths/dirs used by user similarity jobs #
###########################################
USER_SIMILARITY_PARENT_DIR = os.path.join('/', 'user_similarity')
USER_SIMILARITY_DATAFRAME_DIR = os.path.join(
    USER_SIMILARITY_PARENT_DIR, 'dataframe')
USER_SIMILARITY_PLAYCOUNTS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'playcounts_df.parquet')
USER_SIMILARITY_USERS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'users_df.parquet')
USER_SIMILARITY_RECORDINGS_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'recordings_df.parquet')
USER_SIMILARITY_METADATA_DATAFRAME = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'dataframe_metadata.parquet')
USER_SIMILARITY_MAPPED_LISTENS = os.path.join(
    USER_SIMILARITY_DATAFRAME_DIR, 'mapped_listens_df.parquet')

# MusicBrainz Release JSON dump
MUSICBRAINZ_RELEASE_DUMP = "/musicbrainz/release"
MUSICBRAINZ_RELEASE_DUMP_JSON_FILE = "/musicbrainz/release/mbdump/release"

# Release colors
RELEASE_COLOR_DUMP = "/release_color.json"
