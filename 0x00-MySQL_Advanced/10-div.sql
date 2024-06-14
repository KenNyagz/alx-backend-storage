-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
	RETURN CASE WHEN b = 0 THEN 0 ELSE a / b END;
END//

DELIMITER ;
