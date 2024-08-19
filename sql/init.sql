CREATE TABLE tblUsers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(100)
);

INSERT INTO tblUsers (name, phone) VALUES
  ('John', 123456789),
  ('Jane', 987654321),
  ('Bob', 123456789),
  ('Alice', 987654321);
 
