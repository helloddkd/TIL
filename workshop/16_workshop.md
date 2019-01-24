```sqlite
CREATE TABLE bands (
	id INTEGER PRIMARY KEY,
	name TEXT,
	debut INTEGER
	);
	
	
INSERT INTO bands (id, name, debut)
VALUES
(1, 'Queen', 1973),
(2, 'Coldplay', 1998),
(3, 'MCR', 2001);


--  bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.
SELECT id, name from bands;

-- bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.
SELECT name from bands WHERE debut < 2000;


ALTER TABLE bands ADD COLUMN members INTEGER;

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;

UPDATE bands SET members=5 WHERE id=3;

DELETE FROM bands WHERE id=2;
```

