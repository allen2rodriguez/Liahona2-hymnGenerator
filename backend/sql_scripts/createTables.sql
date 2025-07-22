DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS hymns;

CREATE TABLE IF NOT EXISTS hymns (
    h_id SMALLINT PRIMARY KEY,
    h_title VARCHAR(100) NOT NULL,
    special_topic VARCHAR(100),
    position TINYINT,
    CHECK (position <= 4 AND position >= 1)
);

CREATE TABLE IF NOT EXISTS history (
    date DATE PRIMARY KEY,
    opening SMALLINT NOT NULL,
    sacraments SMALLINT NOT NULL,
    intermediate SMALLINT,
    closing SMALLINT,
    FOREIGN KEY (opening)
        REFERENCES hymns (h_id),
    FOREIGN KEY (sacraments)
        REFERENCES hymns (h_id),
    FOREIGN KEY (intermediate)
        REFERENCES hymns (h_id),
    FOREIGN KEY (closing)
        REFERENCES hymns (h_id)
);

