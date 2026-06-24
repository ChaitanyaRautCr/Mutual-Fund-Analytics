-- Average NAV
SELECT AVG(nav) FROM fund_125497;

-- Maximum NAV
SELECT MAX(nav) FROM fund_125497;

-- Minimum NAV
SELECT MIN(nav) FROM fund_125497;

-- Latest NAV
SELECT * FROM fund_125497
ORDER BY date DESC
LIMIT 1;

-- Count Records
SELECT COUNT(*) FROM fund_125497;

-- Average NAV for each fund
SELECT AVG(nav) FROM fund_118632;
SELECT AVG(nav) FROM fund_119092;
SELECT AVG(nav) FROM fund_119551;
SELECT AVG(nav) FROM fund_120503;
SELECT AVG(nav) FROM fund_120841;