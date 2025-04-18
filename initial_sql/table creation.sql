DROP SCHEMA IF EXISTS `resleriana`;
CREATE SCHEMA `resleriana` DEFAULT CHARACTER SET utf8mb4 ;
USE `resleriana`;

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- GENERIC TABLE CREATION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

create table TRANSLATION (
    TL_ID varchar(50) not null,
    `LANGUAGE` varchar(2) not null,
	`TEXT` varchar(2000) not null,
    PRIMARY KEY (TL_ID, `LANGUAGE`),
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP
);

create table TAG (
    EXT_ID int not null unique,
    `NAME` varchar(50) not null,
    PRIORITY int not null ,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID),
    FOREIGN KEY (`NAME`) REFERENCES TRANSLATION(TL_ID)
);

create table EFFECT (
    EXT_ID int not null unique,
    `DESCRIPTION` varchar(50) not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID),
    FOREIGN KEY (`DESCRIPTION`) REFERENCES TRANSLATION(TL_ID)
);

create table ABILITY (
    EXT_ID int not null unique,
    `DESCRIPTION` varchar(50) not null,
    `NAME` varchar(50) not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID),
    FOREIGN KEY (`NAME`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`DESCRIPTION`) REFERENCES TRANSLATION(TL_ID)
);

create table ABILITY_EFFECT (
    ABILITY_ID int not null,
    EFFECT_ID int not null,
    `VALUE` int not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (ABILITY_ID) REFERENCES `ABILITY`(EXT_ID),
    FOREIGN KEY (EFFECT_ID) REFERENCES `EFFECT`(EXT_ID),
    PRIMARY KEY (ABILITY_ID, EFFECT_ID)
);

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- CHARACTER RELATED TABLE CREATION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
create table `CHARACTER` (
    EXT_ID int not null UNIQUE,
    `NAME` varchar(50),
    ANOTHER_NAME varchar(50),
    FULL_NAME varchar(50),
    `DESCRIPTION` varchar(50),
    ACQUISITION_TEXT varchar(50),
    INITIAL_RARITY smallint not null,
    MAX_RARITY smallint not null,
    `ROLE` varchar(50),
    ATTACK_ATTRIBUTE varchar(50),
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
    FOREIGN KEY (EXT_ID) REFERENCES `CHARACTER`(EXT_ID),
    INDEX (EXT_ID)
);

create table CHARACTER_RESIST (
    EXT_ID int not null unique,
    FIRE smallint not null,
    ICE smallint not null,
    AIR smallint not null,
    BOLT smallint not null,
    STRIKE smallint not null,
    STAB smallint not null,
    SLASH smallint not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (EXT_ID) REFERENCES `CHARACTER`(EXT_ID),
    INDEX (EXT_ID)
);


create table CHARACTER_TAG (
    CHARACTER_ID int not null,
    TAG_ID int not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (CHARACTER_ID) REFERENCES `CHARACTER`(EXT_ID),
    FOREIGN KEY (TAG_ID) REFERENCES `TAG`(EXT_ID),
    PRIMARY KEY (CHARACTER_ID, TAG_ID)
);

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- MEMORIA RELATED TABLE CREATION ------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

create table MEMORIA_GROWTH (
    EXT_ID int not null,
    `LEVEL` smallint not null ,
    `STAT_VALUE` smallint not null ,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID, `LEVEL`)
);

create table MEMORIA (
    EXT_ID int not null UNIQUE,
    `NAME` varchar(50),
    `DESCRIPTION` varchar(50),
    RARITY smallint not null,
    RELEASE_DATE TIMESTAMP,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    PRIMARY KEY (EXT_ID),
    FOREIGN KEY (`NAME`) REFERENCES TRANSLATION(TL_ID),
    FOREIGN KEY (`DESCRIPTION`) REFERENCES TRANSLATION(TL_ID)
);

create table MEMORIA_ABILITY (
    MEMORIA_ID int not null,
    ABILITY_ID int not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (MEMORIA_ID) REFERENCES `MEMORIA`(EXT_ID),
    FOREIGN KEY (ABILITY_ID) REFERENCES `ABILITY`(EXT_ID),
    PRIMARY KEY (MEMORIA_ID, ABILITY_ID)
);

create table MEMORIA_ATTRIBUTE (
    MEMORIA_ID int not null,
    ATTRIBUTE varchar(50) not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (MEMORIA_ID) REFERENCES `MEMORIA`(EXT_ID),
    PRIMARY KEY (MEMORIA_ID, ATTRIBUTE)
);

create table MEMORIA_ROLE (
    MEMORIA_ID int not null,
    `ROLE` varchar(50) not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (MEMORIA_ID) REFERENCES `MEMORIA`(EXT_ID),
    PRIMARY KEY (MEMORIA_ID, `ROLE`)
);

create table MEMORIA_STATUS (
    MEMORIA_ID int not null unique,
    ATTACK int not null,
    DEFENSE int not null,
    HP int not null,
    MAGIC int not null,
    MENTAL int not null,
    SPEED int not null,
    CREATE_DATE TIMESTAMP not null,
    UPDATE_DATE TIMESTAMP,
    DELETE_DATE TIMESTAMP,
    FOREIGN KEY (MEMORIA_ID) REFERENCES `MEMORIA`(EXT_ID),
    FOREIGN KEY (ATTACK) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    FOREIGN KEY (DEFENSE) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    FOREIGN KEY (HP) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    FOREIGN KEY (MAGIC) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    FOREIGN KEY (MENTAL) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    FOREIGN KEY (SPEED) REFERENCES `MEMORIA_GROWTH`(EXT_ID),
    INDEX (MEMORIA_ID)
);
