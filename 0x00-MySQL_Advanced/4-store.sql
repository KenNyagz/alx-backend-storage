-- creates a trigger that decreases the quantity of an item after adding a new order

DELIMITER //
CREATE TRIGGER DecreaseItemQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE name = NEW.item_name;
END //

DELIMITER ;
