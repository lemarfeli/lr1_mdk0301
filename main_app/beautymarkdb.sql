
CREATE TABLE services ( 
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL, 
    description VARCHAR NULL, 
    cost MONEY NOT NULL,
    image TEXT NULL,
    service_id INT NOT NULL 
);

CREATE TABLE stylists (
    stylist_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL, 
    master BOOLEAN NOT NULL
);

CREATE TABLE stylist_services (

)


INSERT INTO stylists (stylist_id, name, master) VALUES
(1, 'Rachel', 'TRUE'),
(2, 'Annabelle', 'TRUE'),
(3, 'Giang', 'FALSE'),
(4, 'Corey', 'FALSE');

INSERT INTO services (type, description, cost, image, service_id) VALUES
('Blowout','',40,'images/blowout.png',1),
('Womens Cut & Style','',60,'images/womenscutstyle.png',2),
('Womens Master Cut & Style','',65,'images/mastercutstyle.png',3),
('Mens Wash & Scissor Cut','',40,'images/menswashcut.png',4),
('Lengthy Master Color','',200,'images/lengthmastercolor.png',5),
('Buzz Master Color','',100,'images/buzzmastercolor.png',6),
('Fix Your Face','Standardmakeup',60,'images/fixyourface.png',7),
('Face First','Mastermakeup',90,'images/facefirst.png',8);
