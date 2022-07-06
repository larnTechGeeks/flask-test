INSERT INTO wallets (balance, user_id) VALUES(1000000, 1);
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'debit', 1000000, '2022-03-02 06:51:59.717872', '121211001810', 'bank', 1, 1);


UPDATE wallets 
	SET balance= 999000 WHERE id =1;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'credit', 1000, '2022-04-02 06:51:59.717872', '+254718686211', 'phone', 1, 1);


UPDATE wallets 
	SET balance= 499000 WHERE id =1;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'credit', 300000, '2022-07-02 06:51:59.717872', '+254718686201', 'phone', 1, 1);


UPDATE wallets 
	SET balance= 899000 WHERE id =1;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'debit', 400000, '2022-07-03 06:51:59.717872', '201819181918191', 'bank', 1, 1);




INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'debit', 1000000, '2022-03-02 06:51:59.717872', '121211001810', 'bank', 1, 3);


UPDATE wallets 
	SET balance= 999000 WHERE id =3;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'credit', 1000, '2022-04-02 06:51:59.717872', '+254718686211', 'phone', 1, 3);


UPDATE wallets 
	SET balance= 499000 WHERE id =3;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'credit', 300000, '2022-07-02 06:51:59.717872', '+254718686201', 'phone', 1, 3);


UPDATE wallets 
	SET balance= 899000 WHERE id =3;
INSERT INTO transactions (id, type, amount, transaction_date, account_number, account_type, user_id, wallet_id) 
VALUES(1, 'debit', 400000, '2022-07-03 06:51:59.717872', '201819181918191', 'bank', 1, 3);