CREATE TABLE IF NOT EXISTS food (
                        food_id         INTEGER NOT NULL AUTO_INCREMENT,
                        food            VARCHAR(30) NOT NULL,
                        PRIMARY KEY (food_id)
            );

CREATE TABLE IF NOT EXISTS cats (
                        cat_id          INTEGER NOT NULL AUTO_INCREMENT,
                        cat_name        VARCHAR(20) NOT NULL,
                        fur_type        VARCHAR(20),
                        temprament      VARCHAR(20),
                        approx_age      INTEGER,
                        fav_food        INTEGER,
                        PRIMARY KEY (cat_id),
                        FOREIGN KEY (fav_food) REFERENCES food(food_id)
            );

CREATE TABLE IF NOT EXISTS food_likes (
                        likes_id        INTEGER NOT NULL AUTO_INCREMENT,
                        cat_id          INTEGER,
                        food_id         INTEGER,
                        PRIMARY KEY (likes_id),
                        FOREIGN KEY (cat_id) REFERENCES cats(cat_id),
                        FOREIGN KEY (food_id) REFERENCES food(food_id)
            );

INSERT INTO food VALUES (1, 'A Raw Cauliflower'),(2,'A Freshly Baked Pie'),(3,'A Live, Wriggling Spider'),(4,"An Entire Roast Chicken"),(5,"Bacon, Cooked or Raw"),(6,"Frozen Peas"),(7,"A Victoria Sponge"),(8,"Fresh Cream")
