DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO pg_database_owner;
GRANT ALL ON SCHEMA public TO public;
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
--------------------------------------------- GENERIC TABLE CREATION ------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

CREATE TYPE attack_attribute
AS
ENUM('SLASH', 'STRIKE', 'STAB', 'FIRE', 'ICE', 'BOLT', 'AIR');

CREATE TYPE role_type
AS
ENUM('ATTACKER', 'BREAKER', 'DEFENDER', 'SUPPORTER');

CREATE TYPE skill_type
AS
ENUM('SKILL_1', 'SKILL_2', 'BURST_SKILL');

CREATE TYPE skill_target_type
AS
ENUM('SINGLE_ALLY', 'SINGLE_ENEMY', 'ALL_ALLY', 'ALL_ENEMY');

CREATE TYPE skill_effect_type
AS
ENUM('DAMAGE', 'RECOVERY', 'BUFF', 'DEBUFF');

CREATE TABLE translation_keys (
    id VARCHAR(50) PRIMARY KEY
);

CREATE TABLE translations (
    id VARCHAR(50) NOT NULL,
    lang_code VARCHAR(2) NOT NULL,
    translated_text VARCHAR(2000) NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    PRIMARY KEY (id, lang_code),
    FOREIGN KEY (id) REFERENCES translation_keys(id)
);

CREATE TABLE tag (
    tag_name VARCHAR(50) NOT NULL,
    priority INT NOT NULL ,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (tag_name) REFERENCES translation_keys(id)
);

CREATE TABLE effect (
    effect_description VARCHAR(50) NOT NULL,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (effect_description) REFERENCES translation_keys(id)
);

CREATE TABLE ability (
    ability_description VARCHAR(50) NOT NULL,
    ability_name VARCHAR(50) NOT NULL,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (ability_name) REFERENCES translation_keys(id),
    FOREIGN KEY (ability_description) REFERENCES translation_keys(id)
);

CREATE TABLE ability_effect (
    ability_id INT NOT NULL,
    effect_id INT NOT NULL,
    number_value INT NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (ability_id) REFERENCES ability(id),
    FOREIGN KEY (effect_id) REFERENCES effect(id),
    PRIMARY KEY (ability_id, effect_id)
);

CREATE TABLE skill (
    skill_description VARCHAR(50) NOT NULL,
    skill_name VARCHAR(50) NOT NULL,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    skill_power INT NOT NULL,
    skill_break_power INT NOT NULL,
    skill_wait INT NOT NULL,
	skill_attribute ATTACK_ATTRIBUTE,
	skill_target_type SKILL_TARGET_TYPE,
	linked_skill INT,
	skill_effect_type SKILL_EFFECT_TYPE,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
	FOREIGN KEY (linked_skill) REFERENCES skill(id),
    FOREIGN KEY (skill_name) REFERENCES translation_keys(id),
    FOREIGN KEY (skill_description) REFERENCES translation_keys(id)
);

CREATE TABLE skill_effect (
    skill_id INT NOT NULL,
    effect_id INT NOT NULL,
    number_value INT NOT NULL,
	skill_effect_index SMALLINT,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (skill_id) REFERENCES skill(id),
    FOREIGN KEY (effect_id) REFERENCES effect(id),
    PRIMARY KEY (skill_id, effect_id)
);

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
--------------------------------------------- CHARACTER TABLE CREATION ----------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
CREATE TABLE character (
    character_name VARCHAR(50),
    another_name VARCHAR(50),
    full_name VARCHAR(50),
    character_description VARCHAR(50),
    acquisition_text VARCHAR(50),
    initial_rarity SMALLINT NOT NULL,
    max_rarity SMALLINT NOT NULL,
    character_role ROLE_TYPE,
    attack_attribute ATTACK_ATTRIBUTE,
    is_alchemist boolean NOT NULL,
    release_date TIMESTAMP,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (character_name) REFERENCES translation_keys(id),
    FOREIGN KEY (another_name) REFERENCES translation_keys(id),
    FOREIGN KEY (full_name) REFERENCES translation_keys(id),
    FOREIGN KEY (character_description) REFERENCES translation_keys(id),
    FOREIGN KEY (acquisition_text) REFERENCES translation_keys(id)
);

CREATE TABLE character_status (
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    hp SMALLINT NOT NULL,
    magic SMALLINT NOT NULL,
    mental SMALLINT NOT NULL,
    speed SMALLINT NOT NULL,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (id) REFERENCES character(id)
);

CREATE TABLE character_resist (
    fire SMALLINT NOT NULL,
    ice SMALLINT NOT NULL,
    air SMALLINT NOT NULL,
    bolt SMALLINT NOT NULL,
    strike SMALLINT NOT NULL,
    stab SMALLINT NOT NULL,
    slash SMALLINT NOT NULL,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (id) REFERENCES character(id)
);

CREATE TABLE character_tag (
    tag_id INT NOT NULL,
    character_id INT NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (character_id) REFERENCES character(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id),
    PRIMARY KEY (character_id, tag_id)
);

CREATE TABLE character_skill (
    skill_id INT NOT NULL,
    character_id INT NOT NULL,
	skill_type SKILL_TYPE NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (character_id) REFERENCES character(id),
    FOREIGN KEY (skill_id) REFERENCES skill(id),
    PRIMARY KEY (character_id, skill_id)
);

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------- MEMORIA TABLE CREATION -----------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

CREATE TABLE memoria_growth_key (
    id INT NOT NULL PRIMARY KEY
);

CREATE TABLE memoria_growth (
    id INT NOT NULL,
    memoria_level SMALLINT NOT NULL,
    stat_value SMALLINT NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    PRIMARY KEY (id, memoria_level),
	FOREIGN KEY (id) REFERENCES memoria_growth_key(id)
);

CREATE TABLE memoria (
    memoria_name VARCHAR(50),
    memoria_description VARCHAR(50),
    rarity SMALLINT NOT NULL,
    release_date TIMESTAMP,
    id INT NOT NULL UNIQUE PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (memoria_name) REFERENCES translation_keys(id),
    FOREIGN KEY (memoria_description) REFERENCES translation_keys(id)
);

CREATE TABLE memoria_ability (
    memoria_id INT NOT NULL,
    ability_id INT NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (memoria_id) REFERENCES memoria(id),
    FOREIGN KEY (ability_id) REFERENCES ability(id),
    PRIMARY KEY (memoria_id, ability_id)
);

CREATE TABLE memoria_attribute (
    memoria_id INT NOT NULL,
    memoria_attribute ATTACK_ATTRIBUTE NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (memoria_id) REFERENCES memoria(id),
    PRIMARY KEY (memoria_id, memoria_attribute)
);

CREATE TABLE memoria_role (
    memoria_id INT NOT NULL,
    memoria_role ROLE_TYPE NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (memoria_id) REFERENCES memoria(id),
    PRIMARY KEY (memoria_id, memoria_role)
);

CREATE TABLE memoria_status (
    memoria_id INT NOT NULL UNIQUE,
    attack INT NOT NULL,
    defense INT NOT NULL,
    hp INT NOT NULL,
    magic INT NOT NULL,
    mental INT NOT NULL,
    speed INT NOT NULL,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP,
    delete_date TIMESTAMP,
    FOREIGN KEY (memoria_id) REFERENCES memoria(id),
    FOREIGN KEY (attack) REFERENCES memoria_growth_key(id),
    FOREIGN KEY (defense) REFERENCES memoria_growth_key(id),
    FOREIGN KEY (hp) REFERENCES memoria_growth_key(id),
    FOREIGN KEY (magic) REFERENCES memoria_growth_key(id),
    FOREIGN KEY (mental) REFERENCES memoria_growth_key(id),
    FOREIGN KEY (speed) REFERENCES memoria_growth_key(id),
    PRIMARY KEY (memoria_id)
);


-- GRANTS --
GRANT ALL ON TABLE public.ability TO resleriana_admin;

GRANT ALL ON TABLE public.ability_effect TO resleriana_admin;

GRANT ALL ON TABLE public."character" TO resleriana_admin;

GRANT ALL ON TABLE public.character_resist TO resleriana_admin;

GRANT ALL ON TABLE public.character_skill TO resleriana_admin;

GRANT ALL ON TABLE public.character_status TO resleriana_admin;

GRANT ALL ON TABLE public.character_tag TO resleriana_admin;

GRANT ALL ON TABLE public.effect TO resleriana_admin;

GRANT ALL ON TABLE public.memoria TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_ability TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_attribute TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_growth TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_growth_key TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_role TO resleriana_admin;

GRANT ALL ON TABLE public.memoria_status TO resleriana_admin;

GRANT ALL ON TABLE public.skill TO resleriana_admin;

GRANT ALL ON TABLE public.skill_effect TO resleriana_admin;

GRANT ALL ON TABLE public.tag TO resleriana_admin;

GRANT ALL ON TABLE public.translation_keys TO resleriana_admin;

GRANT ALL ON TABLE public.translations TO resleriana_admin;


