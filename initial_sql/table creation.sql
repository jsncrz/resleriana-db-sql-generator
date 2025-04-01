DROP TABLE IF EXISTS TRANSLATION;
DROP TABLE IF EXISTS `CHARACTER`;
DROP TABLE IF EXISTS CHARACTER_STAT;
DROP TABLE IF EXISTS CHARACTER_RESIST;

create table TRANSLATION (
    TL_ID varchar(30) not null,
    `LANGUAGE` varchar(2) not null,
	`TEXT` varchar(1000) not null,
    PRIMARY KEY (TL_ID, `LANGUAGE`),
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP
);
create table `CHARACTER` (
    EXT_ID int not null UNIQUE,
    `NAME` varchar(30),
    ANOTHER_NAME varchar(30),
    FULL_NAME varchar(30),
    `DESCRIPTION` varchar(30),
    ACQUISITION_TEXT varchar(30),
    INITIAL_RARITY tinyint not null,
    ATTACK_ATTRIBUTE varchar(30),
    IS_ALCHEMIST boolean not null,
    RELEASE_DATE TIMESTAMP,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID),
    FOREIGN KEY (`NAME`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`ANOTHER_NAME`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`FULL_NAME`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`DESCRIPTION`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`ACQUISITION_TEXT`) REFERENCES TRANSLATION(TL_ID)
);

create table CHARACTER_STATS (
    EXT_ID int not null unique,
    ATTACK smallint not null,
    DEFENSE smallint not null,
    HP smallint not null,
    MAGIC smallint not null,
    MENTAL smallint not null,
    SPEED smallint not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (EXT_ID) REFERENCES `CHARACTER`(EXT_ID)
);

create table CHARACTER_RESIST (
    EXT_ID int not null unique,
    FIRE tinyint not null,
    ICE tinyint not null,
    WIND tinyint not null,
    LIGHTNING tinyint not null,
    IMPACT tinyint not null,
    PIERCING tinyint not null,
    SLASHING tinyint not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (EXT_ID) REFERENCES `CHARACTER`(EXT_ID)
);