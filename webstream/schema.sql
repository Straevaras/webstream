DROP TABLE IF EXISTS layout_boxes;
DROP TABLE IF EXISTS layouts;
DROP TABLE IF EXISTS layout_contains;
DROP TABLE IF EXISTS timers;

CREATE TABLE layout_boxes (
	id INTEGER PRIMARY KEY autoincrement,
	width INT NOT NULL,
	height INT NOT NULL,
	posx INT DEFAULT 0,
	posy INT DEFAULT 1
);

CREATE TABLE layouts (
	id INTEGER PRIMARY KEY autoincrement,
	name text NOT NULL
);

CREATE TABLE layout_contains (
	id INTEGER PRIMARY KEY autoincrement,
	layoutid INT NOT NULL,
	boxid INT NOT NULL
);

CREATE TABLE timers (
	id INTEGER PRIMARY KEY autoincrement,
	tstart DATETIME NOT NULL,
	tstop DATETIME NOT NULL
);

