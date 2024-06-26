-- Database + tables to test
DROP DATABASE IF EXISTS test_101;
CREATE DATABASE IF NOT EXISTS test_101;
USE test_101;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("A"), ("B"), ("C"), ("D"), ("E"), ("F"), ("G"), ("H"), ("I"), ("J"), ("K"), ("L");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "MPY3PTF3QC"), (1, "M1CTOO3N0P"), (1, "QXL9X5N27Y"), (1, "UF3EOSQE5Z"), (1, "XT1DG1SMVS"), (1, "6P9BIU3V9W"), (1, "5KTXG6C8X4"), (1, "LB3QVD2OS3"), (1, "XAA8FT68D7"), (1, "L97GHFU7V3"), (1, "LFV4LZ8KDB"), (1, "EG4TUIXDQ2"), (1, "AIG2UUITUU"), (1, "1R3PBSWLA9"), (1, "X3XFP0T0KU"), (1, "SHINGSQ8EU");
INSERT INTO cities (state_id, name) VALUES (2, "F9F9VM0UH2"), (2, "Z5ZVJW1ET6"), (2, "9YC3M04MGH"), (2, "67O6MVJODU"), (2, "MKA6NWTJIA"), (2, "E85KZQKOCE"), (2, "BOZSTRSJ26"), (2, "4ASCU0NLF2"), (2, "4RYF8B24LF"), (2, "FVL2LYYWHJ"), (2, "150GGKLOZD"), (2, "VKRFCCV543"), (2, "02DD6QVP7O"), (2, "CBZALYUGX0"), (2, "7EWR7SDWC9"), (2, "XLRMXADH4T"), (2, "FSVFW5TEIM"), (2, "15XMXA7IJ7"), (2, "DDC1A4VVG5"), (2, "4RTH6HBFBP");
INSERT INTO cities (state_id, name) VALUES (3, "6JQJ4XPFKK"), (3, "WDOYABI6RV"), (3, "N1VSD9HLLX"), (3, "TBEEKKR7GW"), (3, "5CHJGRCBFH"), (3, "4DRR14KEOR"), (3, "TXS0LBHOIZ"), (3, "IGGXJEDS9R"), (3, "BS7D1Z0V2T"), (3, "V68UZ394QG"), (3, "WBMLHV1LGE"), (3, "95H7ME2LDF"), (3, "XPB2NJ5QEW"), (3, "Q43EO6HD2O");
INSERT INTO cities (state_id, name) VALUES (4, "CZV0T6KA1G"), (4, "M8EB8FSRJ2"), (4, "CP5XTDL7P2"), (4, "08RX5VSDSJ"), (4, "Y8LWRBW41V"), (4, "712RUQJGZO"), (4, "D6A0U2C0YL"), (4, "LFE8LRIIH0"), (4, "HO6I8K1NBB"), (4, "Y2ME7C0Z4Q"), (4, "LJCJRKQK6S");
INSERT INTO cities (state_id, name) VALUES (5, "EYYMH9ZGGX"), (5, "PGH2P2RJMU"), (5, "1YCSU22GUP"), (5, "47R1Y8AEAJ"), (5, "TKUJJYBYQA"), (5, "DMCYXOKZEE"), (5, "0F5OFZSOHN"), (5, "Z7CFJN2IJQ"), (5, "3MJ10CD388"), (5, "9KI0E4F1EJ"), (5, "O8Q7HXZ2SV"), (5, "OQ31LG4JNH");
INSERT INTO cities (state_id, name) VALUES (6, "DOET6TZP1G"), (6, "TW6Y1HDOKJ"), (6, "29X62ODI2H"), (6, "FYRPFHWJNN"), (6, "SFZTJVDVM2"), (6, "L017YPWOJ8"), (6, "E6NLUR9WPP"), (6, "1CHQY2K86B"), (6, "L7J3HUIOA3"), (6, "VL96RQCHE7"), (6, "01T26D3CNV"), (6, "P1SE0TO8CL"), (6, "SMW7BR7SOE"), (6, "WDXMQJT32Y"), (6, "1MQXGV7RH2"), (6, "UZ5NNI27TZ"), (6, "IQ4Z45K9RI"), (6, "MGQ9V5EJE4");
INSERT INTO cities (state_id, name) VALUES (7, "XSXCO8OQH1"), (7, "W8HVAFS4C1"), (7, "B9UT6KZ0K7"), (7, "1KZLQXOOOU"), (7, "TDWHD0FPI6"), (7, "SFNIQ718WZ"), (7, "SOJRGF1MDV"), (7, "IZB0Q1LAC2"), (7, "6YHRFAY9MA"), (7, "6PMZGTFWDS"), (7, "KIW9LS6NNX"), (7, "W2JV4TYBVO"), (7, "GINWPOTJAU"), (7, "0GXUR3UASG"), (7, "ZSE5Z9ZTKQ"), (7, "OMRQ680HVH"), (7, "U3P31CQ0FU"), (7, "FZO95B358G");
INSERT INTO cities (state_id, name) VALUES (8, "T1DP5JAKC4"), (8, "REY8R0CKVR"), (8, "2N4Q0FWZ1N"), (8, "N9QE8JF5FD"), (8, "WF5Z6U7ZTF");
INSERT INTO cities (state_id, name) VALUES (9, "HL7BJLLTAD"), (9, "7S6DGLUCTL"), (9, "7HW9QJ3XWO"), (9, "5PDDUX98HY"), (9, "6QYPOL148F");
INSERT INTO cities (state_id, name) VALUES (10, "L13FMNS6EK"), (10, "B4YJK8YK5C"), (10, "M5SOB0TRDY"), (10, "GWNLHFNN6Q"), (10, "UR8WJQF5HZ"), (10, "AA8IN0TZ52"), (10, "RBD4ROIAA0"), (10, "JGAQX42NYX"), (10, "611953MY20"), (10, "N8MZ3H7IVZ");
