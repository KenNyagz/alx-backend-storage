-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

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

DELIMITER ;
