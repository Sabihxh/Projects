import random

with open('a_file.sql', 'w') as file:
    file.write("DROP TABLE IF EXISTS `Laptops`;")
    file.write('\nCREATE TABLE `Laptops` (name VARCHAR(20), speed VARCHAR(20), id INT(11));')

    for x in range(1, 6):
        speed = random.randrange(60, 120)
        file.write("\nINSERT INTO `Laptops` (name, speed, id) VALUES (\'Honda\', %d, %d);" % (speed, x))