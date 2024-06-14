--  creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT;
	DECLARE num_projects INT;

	SELECT SUM(score), COUNT(*)
       	INTO total_score,num_projects
	FROM corrections
	WHERE corrections.user_id = user_id;

	IF num_projects > 0 THEN
		UPDATE users
		SET average_score = total_score / num_projects
		WHERE id = user_id;
	ELSE
		UPDATE users
		SET average_score = 0
		WHERE users.id = user_id;
	END IF;
END//

DELIMITER ;
