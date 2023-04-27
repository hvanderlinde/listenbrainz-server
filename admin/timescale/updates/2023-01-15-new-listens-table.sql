BEGIN;

CREATE TABLE listen_new (
    listened_at     TIMESTAMP WITH TIME ZONE NOT NULL,
    tz_offset       INTERVAL, -- offset to apply to listened_at to get listen's local timestamp
    created         TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
    user_id         INTEGER                  NOT NULL,
    recording_msid  UUID                     NOT NULL,
    data            JSONB                    NOT NULL
);

SELECT create_hypertable('listen_new', 'listened_at', chunk_time_interval => INTERVAL '30 days');

CREATE UNIQUE INDEX listened_at_user_id_recording_msid_ndx_listen ON listen_new (listened_at DESC, user_id, recording_msid);

COMMIT;
