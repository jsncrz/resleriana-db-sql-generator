DROP PROCEDURE IF EXISTS GET_CHARACTER_BY_LANGUAGE_AND_ID;
DELIMITER //
CREATE PROCEDURE GET_CHARACTER_BY_LANGUAGE_AND_ID(IN language_code VARCHAR(2), IN character_id INT)
BEGIN 
	SELECT c.id, c.ext_id, t.`text` as `Name`, t2.`text` AS `Another_Name`, t3.`text` AS `Full_name`,t4.`text` AS `Description`, t5.`text` AS `Acquisition_Text`,
    cr.FIRE AS Fire_Resist, cr.ICE AS Ice_Resist, cr.WIND as Wind_Resist, cr.LIGHTNING AS Lightning_Resist, cr.SLASHING AS Slashing_Resist, cr.IMPACT AS Impact_Resist, cr.PIERCING AS Piercing_Resist,
    cs.ATTACK AS Attack, cs.DEFENSE AS Defense, cs.HP as HP, cs.MAGIC AS Magic, cs.MENTAL AS Mental, cs.SPEED as Speed,
    c.ATTACK_ATTRIBUTE as Attack_Attribute
	FROM `character` c 
	JOIN translation t ON c.name = t.id
	JOIN translation t2 ON c.ANOTHER_NAME = t2.id
	JOIN translation t3 ON c.FULL_NAME = t3.id 
	JOIN translation t4 ON c.`DESCRIPTION` = t4.id 
	JOIN translation t5 ON c.ACQUISITION_TEXT = t5.id
	JOIN character_resist cr ON cr.EXT_ID = c.EXT_ID 
	JOIN character_stats cs ON cs.EXT_ID = c.EXT_ID
	WHERE t.`language` = language_code AND t2.`language` = language_code AND t3.`language` = language_code AND t4.`language` = language_code AND t5.`language` = language_code
    AND c.EXT_ID = character_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS GET_CHARACTERS_BY_LANGUAGE;
DELIMITER //
CREATE PROCEDURE GET_CHARACTERS_BY_LANGUAGE(IN language_code VARCHAR(2))
BEGIN 
	SELECT c.id, c.ext_id, t.`text` as `Name`, t2.`text` AS `Another_Name`,
    c.ATTACK_ATTRIBUTE as Attack_Attribute, c.INITIAL_RARITY AS Initial_Rarity
	FROM `character` c 
	JOIN translation t ON c.name = t.id
	JOIN translation t2 ON c.ANOTHER_NAME = t2.id
	WHERE t.`language` = language_code AND t2.`language` = language_code;
END //
DELIMITER ;
