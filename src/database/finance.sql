CREATE TABLE IF NOT EXISTS Category
(
    id_category VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    aliases TEXT
);


CREATE TABLE IF NOT EXISTS Expense
(
    id_expense INTEGER PRIMARY KEY,
    expense_text TEXT,
    price INTEGER,
    date_created DATETIME,
    id_category INTEGER,

    FOREIGN KEY(id_category) REFERENCES Category(id_category)
);


INSERT INTO Category(id_category, name, aliases)
VALUES
    ("products", "products", "food"),
    ("transport", "transport", "metro, taxi, fuel"),
    ("self needs", "self needs", "self, needs"),
    ("debts", "debts", "debt"),
    ("anya", "anya", "Anya"),
    ("subscriptions", "subscriptions", "sub, subs"),
    ("others", "others", "other")