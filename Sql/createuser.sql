DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(45),
    IN p_email VARCHAR(45),
    IN p_password VARCHAR(45),
    In p_teamname VARCHAR(45)
)
BEGIN
    if ( select exists (select 1 from users where user_email = p_email) ) THEN

        select 'Username Exists !!';

    ELSE

        insert into users
        (
            user_name,
			user_teamname,
            user_email,
            user_password
        )
        values
        (
            p_name,
            p_email,
            p_password,
            p_teamname
        );

    END IF;
END$$
DELIMITER ;