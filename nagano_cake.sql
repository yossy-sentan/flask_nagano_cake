\encoding UTF8;
\c nagano_cake


INSERT INTO genres(name, created_at, updated_at) VALUES('ケーキ', current_date, current_date);
INSERT INTO genres(name, created_at, updated_at) VALUES('焼き菓子', current_date, current_date);
INSERT INTO genres(name, created_at, updated_at) VALUES('プリン', current_date, current_date);
INSERT INTO genres(name, created_at, updated_at) VALUES('和菓子', current_date, current_date);
INSERT INTO genres(name, created_at, updated_at) VALUES('アイス', current_date, current_date);

INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(1, 'ケーキ1', 1000, '1番目のケーキです', '/static/images/cake1.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(1, 'ケーキ2', 1000, '2番目のケーキです', '/static/images/cake2.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(1, 'ケーキ3', 1000, '3番目のケーキです', '/static/images/cake3.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(1, 'ケーキ4', 1000, '4番目のケーキです', '/static/images/cake4.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(1, 'ケーキ5', 1000, '5番目のケーキです', '/static/images/cake5.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(2, 'クッキー1', 500, '1番目のクッキーです', '/static/images/cookies1.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(2, 'クッキー2', 500, '2番目のクッキーです', '/static/images/cookies2.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(2, 'クッキー3', 500, '3番目のクッキーです', '/static/images/cookies3.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(2, 'クッキー4', 500, '4番目のクッキーです', '/static/images/cookies4.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(2, 'クッキー5', 500, '5番目のクッキーです', '/static/images/cookies5.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(3, 'プリン1', 500, '1番目のプリンです', '/static/images/pudding1.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(3, 'プリン2', 500, '2番目のプリンです', '/static/images/pudding2.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(3, 'プリン3', 500, '3番目のプリンです', '/static/images/pudding3.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(3, 'プリン4', 500, '4番目のプリンです', '/static/images/pudding4.jpg', True, current_date, current_date);
INSERT INTO items(genre_id, name, price, introduction, image_path, is_active, created_at, updated_at) VALUES(3, 'プリン5', 500, '5番目のプリンです', '/static/images/pudding5.jpg', True, current_date, current_date);