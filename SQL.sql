-- Question 1
SELECT 
	date, SUM (prod_price * prod_qty) AS ventes
FROM "TRANSACTIONS"
WHERE date >= '01/01/19' 
AND date <= '31/12/19'
GROUP BY date
ORDER BY date ASC;


-- Question 2


SELECT 
	clients.client_id,
	COALESCE (meuble.ventes, 0) AS ventes_meuble,
	COALESCE (deco.ventes, 0) AS ventes_deco
FROM (
	SELECT DISTINCT client_id FROM "TRANSACTIONS" WHERE date >= '01/01/19' AND date <= '31/12/19'
) AS clients

LEFT JOIN (
	SELECT 
		trans.client_id,
		SUM (trans.prod_price * trans.prod_qty) AS ventes
	FROM "TRANSACTIONS" AS trans
	LEFT JOIN "PRODUCT_NOMENCLATURE" AS prods
	ON trans.prod_id = prods.product_id
	WHERE date >= '01/01/19' 
	AND date <= '31/12/19'
	AND prods.product_type = 'MEUBLE'
	GROUP BY trans.client_id
) AS meuble
ON clients.client_id = meuble.client_id

LEFT JOIN (
	SELECT 
		trans.client_id,
		SUM (trans.prod_price * trans.prod_qty) AS ventes
	FROM "TRANSACTIONS" AS trans
	LEFT JOIN "PRODUCT_NOMENCLATURE" AS prods
	ON trans.prod_id = prods.product_id
	WHERE date >= '01/01/19' 
	AND date <= '31/12/19'
	AND prods.product_type = 'DECO'
	GROUP BY trans.client_id
) AS deco
ON clients.client_id = deco.client_id

ORDER BY clients.client_id::INT ASC