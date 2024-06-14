-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
        DECLARE tot_weighted_score FLOAT;
        DECLARE tot_weight FLOAT;

        SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO tot_weighted_score, tot_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        IF tot_weight > 0 THEN
                UPDATE users
                SET average_score = tot_weighted_score / tot_weight
                WHERE users.id = user_id;
        END IF;

END$$


CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE user_id INT;
	DECLARE cur CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN cur;
	read_loop: LOOP
		FETCH cur INTO user_id;
		IF done THEN
			LEAVE read_loop;
		END IF;
		CALL ComputeAverageWeightedScoreForUser(user_id);
	END LOOP;
	CLOSE cur;
END$$

DELIMITER ;
