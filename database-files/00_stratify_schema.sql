DROP DATABASE IF EXISTS Stratify;
CREATE DATABASE Stratify;
USE Stratify;

CREATE TABLE IF NOT EXISTS User (
                                    UserID INT AUTO_INCREMENT,
                                    Name VARCHAR(50) NOT NULL,
                                    Email VARCHAR(50) NOT NULL,
                                    Role VARCHAR(30) NOT NULL,
                                    PRIMARY KEY (UserID)
);

CREATE TABLE IF NOT EXISTS Sector (
                                      sectorID INT AUTO_INCREMENT,
                                      sectorName VARCHAR(50) NOT NULL,
                                      sectorDescription TEXT,
                                      PRIMARY KEY (sectorID)
);

CREATE TABLE IF NOT EXISTS AlertRule (
                                         alertRuleID INT AUTO_INCREMENT,
                                         Name VARCHAR(50) NOT NULL,
                                         `Condition` TEXT NOT NULL,
                                         Severity VARCHAR(20) NOT NULL,
                                         scopeType VARCHAR(30) NOT NULL,
                                         PRIMARY KEY (alertRuleID)
);

CREATE TABLE IF NOT EXISTS Scenario (
                                        scenarioID INT AUTO_INCREMENT,
                                        Name VARCHAR(50) NOT NULL,
                                        Description TEXT,
                                        scenarioType VARCHAR(30) NOT NULL,
                                        PRIMARY KEY (scenarioID)
);

CREATE TABLE IF NOT EXISTS InvestmentStrategy (
                                                  strategyID INT AUTO_INCREMENT,
                                                  strategyName VARCHAR(50) NOT NULL,
                                                  investmentTerm VARCHAR(30) NOT NULL,
                                                  Description TEXT,
                                                  PRIMARY KEY (strategyID)
);

INSERT INTO User (Name, Email, Role) VALUES
                                         ('Noah Harrison', 'noah.harrison@stratify.com', 'Data Analyst'),
                                         ('Jonathan Chen', 'jonathan.chen@stratify.com', 'Asset Management Analyst'),
                                         ('Rajesh Singh', 'rajesh.singh@stratify.com', 'Systems Administrator'),
                                         ('Sarah Martinez', 'sarah.martinez@stratify.com', 'Director of Portfolio Strategy');

INSERT INTO Sector (sectorName, sectorDescription) VALUES
                                                       ('Technology', 'Companies in software, hardware, semiconductors, and IT services'),
                                                       ('Healthcare', 'Pharmaceutical, biotech, medical devices, and healthcare services'),
                                                       ('Finance', 'Banks, investment firms, insurance companies, and financial services'),
                                                       ('Energy', 'Oil, gas, renewable energy, and utilities companies'),
                                                       ('Consumer', 'Retail, consumer goods, restaurants, and consumer services');

INSERT INTO AlertRule (Name, `Condition`, Severity, scopeType) VALUES
                                                                   ('Portfolio Concentration', 'Single position exceeds 25% of portfolio value', 'High', 'Portfolio'),
                                                                   ('Tech Sector Overweight', 'Technology sector allocation exceeds 35%', 'Medium', 'Sector'),
                                                                   ('Market Drop Alert', 'Portfolio value drops more than 5% in single day', 'Critical', 'Portfolio');

INSERT INTO Scenario (Name, Description, scenarioType) VALUES
                                                           ('2008 Financial Crisis', 'Simulates market conditions during the 2008-2009 financial crisis', 'Historical'),
                                                           ('COVID-19 Market Crash', 'March 2020 market crash scenario with rapid recovery', 'Historical'),
                                                           ('Bull Market 2020-2021', 'Extended bull market with tech sector outperformance', 'Historical');

INSERT INTO InvestmentStrategy (strategyName, investmentTerm, Description) VALUES
                                                                               ('Growth Strategy', 'Long-term', 'Focuses on high-growth technology and healthcare stocks with 5+ year horizon'),
                                                                               ('Value Strategy', 'Medium-term', 'Targets undervalued stocks with strong fundamentals and dividend yield'),
                                                                               ('Dividend Strategy', 'Long-term', 'Emphasizes stable dividend-paying stocks for income generation');

CREATE TABLE IF NOT EXISTS Asset (
                                     assetID INT AUTO_INCREMENT,
                                     TickerSymbol VARCHAR(10) NOT NULL,
                                     AssetName VARCHAR(50) NOT NULL,
                                     AssetType VARCHAR(30) NOT NULL,
                                     CurrentPrice DECIMAL(10,2) NOT NULL,
                                     sectorID INT NOT NULL,
                                     PRIMARY KEY (assetID),
                                     CONSTRAINT fk_asset_sector FOREIGN KEY (sectorID)
                                         REFERENCES Sector(sectorID)
                                         ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Portfolio (
                                         portfolioID INT AUTO_INCREMENT,
                                         Name VARCHAR(50) NOT NULL,
                                         Description TEXT,
                                         dateCreated DATETIME NOT NULL,
                                         userID INT NOT NULL,
                                         PRIMARY KEY (portfolioID),
                                         CONSTRAINT fk_portfolio_user FOREIGN KEY (userID)
                                             REFERENCES User(UserID)
                                             ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS WatchList (
                                         UserID INT,
                                         WatchListID INT,
                                         Name VARCHAR(50) NOT NULL,
                                         createdDate DATETIME NOT NULL,
                                         PRIMARY KEY (UserID, WatchListID),
                                         CONSTRAINT fk_watchlist_user FOREIGN KEY (UserID)
                                             REFERENCES User(UserID)
                                             ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS AuditEvent (
                                          AuditEventID INT AUTO_INCREMENT,
                                          eventType VARCHAR(50) NOT NULL,
                                          eventTime DATETIME NOT NULL,
                                          resourceType VARCHAR(50) NOT NULL,
                                          resourceID INT NOT NULL,
                                          UserID INT NOT NULL,
                                          PRIMARY KEY (AuditEventID),
                                          CONSTRAINT fk_auditevent_user FOREIGN KEY (UserID)
                                              REFERENCES User(UserID)
                                              ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO Asset (TickerSymbol, AssetName, AssetType, CurrentPrice, sectorID) VALUES
                                                                                   ('AAPL', 'Apple Inc.', 'Stock', 178.50, 1),
                                                                                   ('TSLA', 'Tesla Inc.', 'Stock', 242.80, 1),
                                                                                   ('NVDA', 'NVIDIA Corporation', 'Stock', 495.20, 1),
                                                                                   ('MSFT', 'Microsoft Corporation', 'Stock', 378.90, 1),
                                                                                   ('GOOGL', 'Alphabet Inc.', 'Stock', 141.80, 1),
                                                                                   ('JNJ', 'Johnson & Johnson', 'Stock', 156.30, 2),
                                                                                   ('XOM', 'Exxon Mobil Corporation', 'Stock', 102.45, 4),
                                                                                   ('JPM', 'JPMorgan Chase & Co.', 'Stock', 158.70, 3),
                                                                                   ('PG', 'Procter & Gamble Co.', 'Stock', 152.80, 5),
                                                                                   ('SPY', 'SPDR S&P 500 ETF Trust', 'ETF', 452.30, 1);

INSERT INTO Portfolio (Name, Description, dateCreated, userID) VALUES
                                                                   ('Tech Growth 2024', 'Aggressive growth portfolio focused on large-cap technology stocks', '2024-01-15 09:30:00', 2),
                                                                   ('Balanced Fund', 'Diversified portfolio balancing growth and income across sectors', '2024-02-01 10:00:00', 4),
                                                                   ('Dividend Portfolio', 'Income-focused portfolio with stable dividend-paying stocks', '2024-03-10 14:20:00', 1),
                                                                   ('Test Strategy Portfolio', 'Experimental portfolio for system testing and validation', '2024-04-05 11:45:00', 3);

INSERT INTO WatchList (UserID, WatchListID, Name, createdDate) VALUES
                                                                   (1, 1, 'High Dividend Stocks', '2024-01-20 08:00:00'),
                                                                   (2, 1, 'Growth Tech Opportunities', '2024-02-15 09:15:00'),
                                                                   (4, 1, 'Strategic Monitoring List', '2024-03-01 10:30:00');

INSERT INTO AuditEvent (eventType, eventTime, resourceType, resourceID, UserID) VALUES
                                                                                    ('CREATE', '2024-01-15 09:30:00', 'Portfolio', 1, 2),
                                                                                    ('UPDATE', '2024-02-20 14:45:00', 'Position', 5, 1),
                                                                                    ('CREATE', '2024-03-10 14:20:00', 'Portfolio', 3, 1);

CREATE TABLE IF NOT EXISTS Position (
                                        positionID INT AUTO_INCREMENT,
                                        portfolioID INT NOT NULL,
                                        assetID INT NOT NULL,
                                        Quantity INT NOT NULL,
                                        AvgCostBasis DECIMAL(10,2) NOT NULL,
                                        PRIMARY KEY (positionID),
                                        UNIQUE KEY unique_portfolio_asset (portfolioID, assetID),
                                        CONSTRAINT fk_position_portfolio FOREIGN KEY (portfolioID)
                                            REFERENCES Portfolio(portfolioID)
                                            ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk_position_asset FOREIGN KEY (assetID)
                                            REFERENCES Asset(assetID)
                                            ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Transaction (
                                           transactionID INT AUTO_INCREMENT,
                                           transactionDate DATETIME NOT NULL,
                                           transactionType VARCHAR(10) NOT NULL,
                                           Quantity INT NOT NULL,
                                           pricePerShare DECIMAL(10,2) NOT NULL,
                                           portfolioID INT NOT NULL,
                                           assetID INT NOT NULL,
                                           PRIMARY KEY (transactionID),
                                           CONSTRAINT fk_transaction_portfolio FOREIGN KEY (portfolioID)
                                               REFERENCES Portfolio(portfolioID)
                                               ON UPDATE CASCADE ON DELETE RESTRICT,
                                           CONSTRAINT fk_transaction_asset FOREIGN KEY (assetID)
                                               REFERENCES Asset(assetID)
                                               ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS PriceHistory (
                                            priceID INT AUTO_INCREMENT,
                                            Date DATETIME NOT NULL,
                                            openPrice DECIMAL(10,2) NOT NULL,
                                            closePrice DECIMAL(10,2) NOT NULL,
                                            Volume BIGINT NOT NULL,
                                            assetID INT NOT NULL,
                                            PRIMARY KEY (priceID),
                                            CONSTRAINT fk_pricehistory_asset FOREIGN KEY (assetID)
                                                REFERENCES Asset(assetID)
                                                ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Alert (
                                     AlertID INT AUTO_INCREMENT,
                                     triggerTime DATETIME NOT NULL,
                                     Message TEXT NOT NULL,
                                     Status VARCHAR(20) NOT NULL,
                                     alertRuleID INT NOT NULL,
                                     portfolioID INT,
                                     PRIMARY KEY (AlertID),
                                     CONSTRAINT fk_alert_alertrule FOREIGN KEY (alertRuleID)
                                         REFERENCES AlertRule(alertRuleID)
                                         ON UPDATE CASCADE ON DELETE RESTRICT,
                                     CONSTRAINT fk_alert_portfolio FOREIGN KEY (portfolioID)
                                         REFERENCES Portfolio(portfolioID)
                                         ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS PortfolioPerformance (
                                                    portfolioID INT,
                                                    performanceID INT,
                                                    portfolioValue DECIMAL(15,2) NOT NULL,
                                                    calculationDate DATETIME NOT NULL,
                                                    totalReturn DECIMAL(10,2) NOT NULL,
                                                    PRIMARY KEY (portfolioID, performanceID),
                                                    CONSTRAINT fk_portfolioperformance_portfolio FOREIGN KEY (portfolioID)
                                                        REFERENCES Portfolio(portfolioID)
                                                        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS StrategyGuideline (
                                                 strategyID INT,
                                                 guidelineID INT,
                                                 metricType VARCHAR(50) NOT NULL,
                                                 targetValue DECIMAL(10,2) NOT NULL,
                                                 PRIMARY KEY (strategyID, guidelineID),
                                                 CONSTRAINT fk_strategyguideline_strategy FOREIGN KEY (strategyID)
                                                     REFERENCES InvestmentStrategy(strategyID)
                                                     ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS scenarioResult (
                                              scenarioID INT,
                                              scenarioResultID INT,
                                              projectedReturn DECIMAL(10,2) NOT NULL,
                                              portfolioID INT NOT NULL,
                                              PRIMARY KEY (scenarioID, scenarioResultID),
                                              CONSTRAINT fk_scenarioresult_scenario FOREIGN KEY (scenarioID)
                                                  REFERENCES Scenario(scenarioID)
                                                  ON UPDATE CASCADE ON DELETE CASCADE,
                                              CONSTRAINT fk_scenarioresult_portfolio FOREIGN KEY (portfolioID)
                                                  REFERENCES Portfolio(portfolioID)
                                                  ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO Position (portfolioID, assetID, Quantity, AvgCostBasis) VALUES
                                                                        (1, 1, 50, 165.20),
                                                                        (1, 2, 30, 238.50),
                                                                        (1, 3, 25, 480.00),
                                                                        (2, 1, 40, 170.00),
                                                                        (2, 6, 60, 155.00),
                                                                        (2, 8, 35, 152.30),
                                                                        (3, 6, 80, 154.50),
                                                                        (3, 9, 100, 150.00);

INSERT INTO Transaction (transactionDate, transactionType, Quantity, pricePerShare, portfolioID, assetID) VALUES
                                                                                                              ('2024-01-15 10:00:00', 'BUY', 50, 165.20, 1, 1),
                                                                                                              ('2024-01-20 11:30:00', 'BUY', 30, 238.50, 1, 2),
                                                                                                              ('2024-02-01 09:15:00', 'BUY', 25, 480.00, 1, 3),
                                                                                                              ('2024-02-05 14:20:00', 'BUY', 40, 170.00, 2, 1),
                                                                                                              ('2024-02-10 10:45:00', 'BUY', 60, 155.00, 2, 6),
                                                                                                              ('2024-02-15 13:00:00', 'BUY', 35, 152.30, 2, 8),
                                                                                                              ('2024-03-10 15:30:00', 'BUY', 80, 154.50, 3, 6),
                                                                                                              ('2024-03-12 09:00:00', 'BUY', 100, 150.00, 3, 9),
                                                                                                              ('2024-03-20 11:15:00', 'SELL', 10, 175.00, 1, 1),
                                                                                                              ('2024-04-01 10:30:00', 'BUY', 15, 490.00, 1, 3),
                                                                                                              ('2024-04-10 14:00:00', 'SELL', 20, 158.00, 2, 6),
                                                                                                              ('2024-04-15 16:00:00', 'BUY', 50, 153.50, 3, 9);

INSERT INTO PriceHistory (Date, openPrice, closePrice, Volume, assetID) VALUES
                                                                            ('2024-01-15 09:30:00', 164.50, 165.80, 52000000, 1),
                                                                            ('2024-02-15 09:30:00', 168.20, 170.50, 48000000, 1),
                                                                            ('2024-03-15 09:30:00', 172.00, 174.30, 55000000, 1),
                                                                            ('2024-04-15 09:30:00', 175.50, 178.50, 51000000, 1),
                                                                            ('2024-05-15 09:30:00', 176.00, 177.90, 49000000, 1),
                                                                            ('2024-01-15 09:30:00', 235.00, 240.00, 120000000, 2),
                                                                            ('2024-02-15 09:30:00', 238.00, 242.80, 115000000, 2),
                                                                            ('2024-03-15 09:30:00', 230.00, 235.50, 130000000, 2),
                                                                            ('2024-04-15 09:30:00', 240.00, 245.00, 125000000, 2),
                                                                            ('2024-05-15 09:30:00', 241.00, 242.80, 118000000, 2),
                                                                            ('2024-01-15 09:30:00', 475.00, 482.00, 35000000, 3),
                                                                            ('2024-02-15 09:30:00', 480.00, 488.50, 38000000, 3),
                                                                            ('2024-03-15 09:30:00', 485.00, 492.00, 40000000, 3),
                                                                            ('2024-04-15 09:30:00', 490.00, 495.20, 42000000, 3),
                                                                            ('2024-05-15 09:30:00', 493.00, 497.00, 39000000, 3),
                                                                            ('2024-01-15 09:30:00', 153.00, 155.50, 28000000, 6),
                                                                            ('2024-02-15 09:30:00', 154.00, 156.00, 26000000, 6),
                                                                            ('2024-03-15 09:30:00', 155.50, 157.20, 27000000, 6),
                                                                            ('2024-04-15 09:30:00', 156.00, 156.30, 25000000, 6),
                                                                            ('2024-05-15 09:30:00', 155.80, 156.50, 24000000, 6),
                                                                            ('2024-01-15 09:30:00', 149.00, 151.00, 18000000, 9),
                                                                            ('2024-02-15 09:30:00', 150.50, 152.30, 17000000, 9),
                                                                            ('2024-03-15 09:30:00', 151.00, 152.80, 19000000, 9),
                                                                            ('2024-04-15 09:30:00', 152.00, 153.50, 20000000, 9),
                                                                            ('2024-05-15 09:30:00', 152.50, 152.80, 18500000, 9);

INSERT INTO Alert (triggerTime, Message, Status, alertRuleID, portfolioID) VALUES
                                                                               ('2024-03-20 12:00:00', 'NVDA position exceeds 25% of portfolio value in Tech Growth 2024', 'Active', 1, 1),
                                                                               ('2024-04-01 10:00:00', 'Technology sector allocation at 38% in Tech Growth 2024', 'Active', 2, 1),
                                                                               ('2024-04-15 15:30:00', 'Balanced Fund dropped 5.2% today due to market correction', 'Resolved', 3, 2);

INSERT INTO PortfolioPerformance (portfolioID, performanceID, portfolioValue, calculationDate, totalReturn) VALUES
                                                                                                                (1, 1, 32500.00, '2024-03-01 00:00:00', 8.50),
                                                                                                                (1, 2, 35200.00, '2024-05-01 00:00:00', 14.20),
                                                                                                                (2, 1, 28000.00, '2024-03-01 00:00:00', 5.20),
                                                                                                                (2, 2, 29500.00, '2024-05-01 00:00:00', 8.90),
                                                                                                                (3, 1, 27400.00, '2024-04-01 00:00:00', 3.80),
                                                                                                                (3, 2, 28100.00, '2024-05-15 00:00:00', 5.20);

INSERT INTO StrategyGuideline (strategyID, guidelineID, metricType, targetValue) VALUES
                                                                                     (1, 1, 'Max Sector Allocation', 35.00),
                                                                                     (1, 2, 'Target Annual Return', 15.00),
                                                                                     (2, 1, 'Max Single Position', 10.00),
                                                                                     (3, 1, 'Min Dividend Yield', 3.50);

INSERT INTO scenarioResult (scenarioID, scenarioResultID, projectedReturn, portfolioID) VALUES
                                                                                            (1, 1, -35.20, 1),
                                                                                            (1, 2, -28.50, 2),
                                                                                            (2, 1, -22.40, 1),
                                                                                            (2, 2, -18.30, 2),
                                                                                            (3, 1, 45.80, 1),
                                                                                            (3, 2, 28.90, 2);

CREATE TABLE IF NOT EXISTS Backtest (
                                        backtestID INT AUTO_INCREMENT,
                                        startDate DATETIME NOT NULL,
                                        endDate DATETIME NOT NULL,
                                        finalValue DECIMAL(15,2) NOT NULL,
                                        portfolioID INT NOT NULL,
                                        strategyID INT NOT NULL,
                                        PRIMARY KEY (backtestID),
                                        CONSTRAINT fk_backtest_portfolio FOREIGN KEY (portfolioID)
                                            REFERENCES Portfolio(portfolioID)
                                            ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk_backtest_strategy FOREIGN KEY (strategyID)
                                            REFERENCES InvestmentStrategy(strategyID)
                                            ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS User_Alert (
                                          UserID INT,
                                          AlertID INT,
                                          PRIMARY KEY (UserID, AlertID),
                                          CONSTRAINT fk_useralert_user FOREIGN KEY (UserID)
                                              REFERENCES User(UserID)
                                              ON UPDATE CASCADE ON DELETE CASCADE,
                                          CONSTRAINT fk_useralert_alert FOREIGN KEY (AlertID)
                                              REFERENCES Alert(AlertID)
                                              ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS WatchList_Asset (
                                               UserID INT,
                                               WatchListID INT,
                                               assetID INT,
                                               PRIMARY KEY (UserID, WatchListID, assetID),
                                               CONSTRAINT fk_watchlistasset_watchlist FOREIGN KEY (UserID, WatchListID)
                                                   REFERENCES WatchList(UserID, WatchListID)
                                                   ON UPDATE CASCADE ON DELETE CASCADE,
                                               CONSTRAINT fk_watchlistasset_asset FOREIGN KEY (assetID)
                                                   REFERENCES Asset(assetID)
                                                   ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Backtest (startDate, endDate, finalValue, portfolioID, strategyID) VALUES
                                                                                   ('2024-01-01 00:00:00', '2024-03-31 23:59:59', 35200.00, 1, 1),
                                                                                   ('2024-02-01 00:00:00', '2024-04-30 23:59:59', 29800.00, 2, 2),
                                                                                   ('2024-03-01 00:00:00', '2024-05-31 23:59:59', 28500.00, 3, 3),
                                                                                   ('2024-01-15 00:00:00', '2024-05-15 23:59:59', 32000.00, 1, 2);

INSERT INTO User_Alert (UserID, AlertID) VALUES
                                             (2, 1),
                                             (2, 2),
                                             (4, 3),
                                             (1, 2);

INSERT INTO WatchList_Asset (UserID, WatchListID, assetID) VALUES
                                                               (1, 1, 6),
                                                               (1, 1, 9),
                                                               (1, 1, 8),
                                                               (2, 1, 1),
                                                               (2, 1, 2),
                                                               (2, 1, 3),
                                                               (2, 1, 4),
                                                               (4, 1, 1),
                                                               (4, 1, 10);

SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'Stratify';

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'Stratify'
ORDER BY table_name;

SELECT COUNT(DISTINCT CONSTRAINT_NAME) AS Total_FK_Constraints
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'Stratify'
  AND REFERENCED_TABLE_NAME IS NOT NULL;

SELECT
    u.Name AS UserName,
    p.Name AS PortfolioName,
    a.TickerSymbol,
    pos.Quantity,
    t.transactionType,
    t.transactionDate
FROM User u
         JOIN Portfolio p ON u.UserID = p.userID
         JOIN Position pos ON p.portfolioID = pos.portfolioID
         JOIN Asset a ON pos.assetID = a.assetID
         JOIN Transaction t ON p.portfolioID = t.portfolioID AND a.assetID = t.assetID
ORDER BY u.Name, p.Name, t.transactionDate
LIMIT 10;
