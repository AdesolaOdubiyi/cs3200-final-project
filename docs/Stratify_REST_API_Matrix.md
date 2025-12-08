# Stratify REST API Matrix

## Overview
This document provides a comprehensive matrix of all REST API endpoints in the Stratify platform, organized by resource category (Blueprint).

**Base URL**: `http://web-api:4000` (or `http://localhost:4000` in development)

**Response Format**: All endpoints return JSON with the following structure:
```json
{
  "success": true|false,
  "data": {...},
  "error": "error message" (if success is false),
  "status_code": 200|400|404|500
}
```

---

## 1. Portfolios Blueprint (`/portfolio`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/portfolio/portfolios` | Get all portfolios (optional: `?userID=<id>`) | ✅ Implemented | Jonathan-1 |
| GET | `/portfolio/portfolios/<id>` | Get portfolio by ID with positions | ✅ Implemented | Jonathan-1, Jonathan-2 |
| POST | `/portfolio/portfolios` | Create new portfolio | ✅ Implemented | Jonathan-1 |
| PUT | `/portfolio/portfolios/<id>` | Update portfolio (Name, Description) | ✅ Implemented | Jonathan-1 |

### Request/Response Examples

**POST `/portfolio/portfolios`**
```json
Request Body:
{
  "Name": "Growth Portfolio",
  "userID": 1,
  "Description": "Tech-focused growth strategy"
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Portfolio created successfully",
    "portfolioID": 5
  }
}
```

---

## 2. Assets Blueprint (`/asset`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/asset/assets` | Get all assets (optional: `?sectorID=<id>&ticker=<symbol>`) | ✅ Implemented | Noah-4 |
| GET | `/asset/assets/<id>` | Get asset by ID | ✅ Implemented | Noah-4 |
| GET | `/asset/assets/<id>/price-history` | Get price history for asset | ✅ Implemented | Noah-4 |
| GET | `/asset/assets/sector/<sector_id>` | Get all assets in a sector | ✅ Implemented | Sarah-2 |

### Request/Response Examples

**GET `/asset/assets/1/price-history`**
```json
Response (200):
{
  "success": true,
  "data": [
    {
      "date": "2024-01-01",
      "price": 150.25,
      "volume": 1000000
    },
    ...
  ]
}
```

---

## 3. Positions Blueprint (`/position`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/position/positions` | Get all positions (optional: `?portfolioID=<id>`) | ✅ Implemented | Jonathan-2 |
| GET | `/position/positions/<id>` | Get position by ID | ✅ Implemented | Jonathan-2 |
| POST | `/position/positions` | Create new position | ✅ Implemented | Jonathan-2 |
| PUT | `/position/positions/<id>` | Update position (Quantity, AvgCostBasis) | ✅ Implemented | Jonathan-2 |
| DELETE | `/position/positions/<id>` | Delete position | ✅ Implemented | Jonathan-2 |

### Request/Response Examples

**POST `/position/positions`**
```json
Request Body:
{
  "portfolioID": 1,
  "assetID": 5,
  "Quantity": 100,
  "AvgCostBasis": 150.50
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Position created successfully",
    "positionID": 12
  }
}
```

---

## 4. Transactions Blueprint (`/transaction`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/transaction/transactions` | Get all transactions (optional: `?portfolioID=<id>`) | ❌ **MISSING** | Jonathan-4 |
| POST | `/transaction/transactions` | Create transaction (buy/sell) | ❌ **MISSING** | Jonathan-4 |

### Required Implementation

**POST `/transaction/transactions`**
```json
Request Body:
{
  "portfolioID": 1,
  "assetID": 5,
  "transactionType": "BUY" | "SELL",
  "quantity": 100,
  "price": 150.50,
  "transactionDate": "2024-01-15",
  "notes": "Optional transaction notes"
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Transaction recorded successfully",
    "transactionID": 25,
    "positionUpdated": true
  }
}
```

**Note**: This endpoint should:
- Create a Transaction record
- Update or create the corresponding Position
- Recalculate average cost basis for BUY transactions
- Validate sufficient quantity for SELL transactions

---

## 5. Backtests Blueprint (`/backtest`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/backtest/results/<backtest_id>` | Get backtest results | ✅ Implemented | Noah-1, Noah-2, Jonathan-3 |
| POST | `/backtest/backtests` | Create new backtest | ❌ **MISSING** | Noah-1 |

### Required Implementation

**POST `/backtest/backtests`**
```json
Request Body:
{
  "name": "Momentum Strategy v2",
  "description": "30-day momentum with rebalancing",
  "startDate": "2024-01-01",
  "endDate": "2024-12-31",
  "initialCapital": 100000,
  "strategyConfig": {
    "lookbackPeriod": 30,
    "rebalanceFrequency": "weekly",
    "assets": [1, 2, 3, 5]
  },
  "userID": 1
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Backtest created successfully",
    "backtestID": 10,
    "status": "PENDING" | "RUNNING" | "COMPLETED"
  }
}
```

---

## 6. Performance Blueprint (`/performance`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/performance/firm/summary` | Get firm-wide performance summary | ✅ Implemented | Sarah-1 |
| GET | `/performance/portfolio/<id>` | Get portfolio performance metrics | ❌ **MISSING** | Noah-6, Jonathan-6 |
| GET | `/performance/portfolio/<id>/comparison` | Compare portfolio vs benchmark | ❌ **MISSING** | Noah-6, Jonathan-6 |
| GET | `/performance/benchmark` | Get benchmark data (S&P 500) | ❌ **MISSING** | Jonathan-6 |
| GET | `/performance/sector/exposure` | Get sector exposure analysis | ❌ **MISSING** | Sarah-2 |

### Required Implementations

**GET `/performance/portfolio/<id>`**
```json
Response (200):
{
  "success": true,
  "data": {
    "portfolioID": 1,
    "totalValue": 125000.50,
    "totalReturn": 25.0,
    "ytdReturn": 12.5,
    "sharpeRatio": 1.85,
    "maxDrawdown": -12.4,
    "volatility": 15.2,
    "startDate": "2024-01-01",
    "endDate": "2024-12-31"
  }
}
```

**GET `/performance/portfolio/<id>/comparison`**
```json
Query Parameters: ?benchmark=SP500&startDate=2024-01-01&endDate=2024-12-31

Response (200):
{
  "success": true,
  "data": {
    "portfolio": {
      "totalReturn": 25.0,
      "sharpeRatio": 1.85
    },
    "benchmark": {
      "totalReturn": 18.5,
      "sharpeRatio": 1.45
    },
    "outperformance": 6.5
  }
}
```

**GET `/performance/sector/exposure`**
```json
Response (200):
{
  "success": true,
  "data": {
    "sectors": [
      {
        "sectorID": 1,
        "sectorName": "Technology",
        "exposure": 35.5,
        "value": 45000000
      },
      ...
    ],
    "totalValue": 125000000
  }
}
```

---

## 7. Scenarios Blueprint (`/scenario`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/scenario/scenarios` | Get scenario analysis results | ❌ **MISSING** | Sarah-3, Sarah-6 |

### Required Implementation

**GET `/scenario/scenarios`**
```json
Query Parameters: ?portfolioID=<id>&scenarioType=stress_test

Response (200):
{
  "success": true,
  "data": {
    "scenarios": [
      {
        "scenarioID": 1,
        "name": "Market Crash -20%",
        "portfolioImpact": -18.5,
        "sectorBreakdown": {...}
      },
      ...
    ]
  }
}
```

---

## 8. Alerts Blueprint (`/alert`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/alert/alerts` | Get all active alerts | ❌ **MISSING** | Sarah-4, Rajesh-5 |
| POST | `/alert/alerts` | Create alert rule | ❌ **MISSING** | Rajesh-5 |

### Required Implementations

**GET `/alert/alerts`**
```json
Query Parameters: ?portfolioID=<id>&severity=HIGH

Response (200):
{
  "success": true,
  "data": [
    {
      "alertID": 1,
      "type": "PRICE_THRESHOLD",
      "severity": "HIGH",
      "message": "AAPL dropped below $150",
      "timestamp": "2024-01-15T10:30:00Z",
      "portfolioID": 1
    },
    ...
  ]
}
```

**POST `/alert/alerts`**
```json
Request Body:
{
  "name": "Price Drop Alert",
  "type": "PRICE_THRESHOLD",
  "condition": {
    "assetID": 5,
    "threshold": 150.00,
    "direction": "BELOW"
  },
  "severity": "HIGH",
  "portfolioID": 1
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Alert rule created successfully",
    "alertID": 10
  }
}
```

---

## 9. Users Blueprint (`/user`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/user/users` | Get all users | ❌ **MISSING** | Rajesh-2 |
| PUT | `/user/users/<id>/role` | Update user role | ❌ **MISSING** | Rajesh-2 |
| GET | `/user/users/<id>/activity` | Get user activity log | ❌ **MISSING** | Sarah-5 |

### Required Implementations

**GET `/user/users`**
```json
Response (200):
{
  "success": true,
  "data": [
    {
      "userID": 1,
      "name": "Noah Harrison",
      "email": "noah@stratify.com",
      "role": "data_analyst",
      "lastLogin": "2024-01-15T08:30:00Z"
    },
    ...
  ]
}
```

**PUT `/user/users/<id>/role`**
```json
Request Body:
{
  "role": "analyst" | "data_analyst" | "administrator" | "director"
}

Response (200):
{
  "success": true,
  "data": {
    "message": "User role updated successfully"
  }
}
```

**GET `/user/users/<id>/activity`**
```json
Query Parameters: ?startDate=2024-01-01&endDate=2024-01-31

Response (200):
{
  "success": true,
  "data": {
    "userID": 1,
    "activities": [
      {
        "activityID": 1,
        "type": "PORTFOLIO_CREATED",
        "timestamp": "2024-01-15T10:00:00Z",
        "details": "Created portfolio 'Growth Strategy'"
      },
      ...
    ]
  }
}
```

---

## 10. Watchlists Blueprint (`/watchlist`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/watchlist/watchlists` | Get watchlists (optional: `?userID=<id>`) | ❌ **MISSING** | Jonathan-5 |
| POST | `/watchlist/watchlists` | Add asset to watchlist | ❌ **MISSING** | Jonathan-5 |
| DELETE | `/watchlist/watchlists/<id>` | Remove asset from watchlist | ❌ **MISSING** | Jonathan-5 |

### Required Implementations

**GET `/watchlist/watchlists`**
```json
Query Parameters: ?userID=1

Response (200):
{
  "success": true,
  "data": [
    {
      "watchlistID": 1,
      "userID": 1,
      "assetID": 5,
      "assetName": "Apple Inc.",
      "tickerSymbol": "AAPL",
      "addedDate": "2024-01-10"
    },
    ...
  ]
}
```

**POST `/watchlist/watchlists`**
```json
Request Body:
{
  "userID": 1,
  "assetID": 5
}

Response (201):
{
  "success": true,
  "data": {
    "message": "Asset added to watchlist",
    "watchlistID": 10
  }
}
```

---

## 11. Audit Blueprint (`/audit`)

| Method | Endpoint | Description | Status | User Stories |
|--------|----------|-------------|--------|--------------|
| GET | `/audit/events` | Get audit events with filtering | ❌ **MISSING** | Rajesh-3 |

### Required Implementation

**GET `/audit/events`**
```json
Query Parameters: ?startDate=2024-01-01&endDate=2024-01-31&eventType=PORTFOLIO_CREATED&userID=1

Response (200):
{
  "success": true,
  "data": [
    {
      "auditID": 1,
      "eventType": "PORTFOLIO_CREATED",
      "userID": 1,
      "timestamp": "2024-01-15T10:00:00Z",
      "details": {
        "portfolioID": 5,
        "portfolioName": "Growth Strategy"
      }
    },
    ...
  ]
}
```

---

## Summary Statistics

### Implementation Status
- **Fully Implemented**: 3 blueprints (portfolios, assets, positions)
- **Partially Implemented**: 2 blueprints (backtests, performance)
- **Not Implemented**: 6 blueprints (transactions, scenarios, alerts, users, watchlists, audit)

### Endpoint Count
- **Total Required Endpoints**: ~35
- **Implemented**: 15
- **Missing**: 20

### User Story Coverage
- **Total User Stories**: 24
- **Fully Supported**: ~12
- **Partially Supported**: ~6
- **Not Supported**: ~6

---

## Registration Status in `rest_entry.py`

Currently registered:
- ✅ portfolios
- ✅ assets
- ✅ positions
- ✅ backtests
- ✅ performance
- ❌ transactions (MISSING)
- ❌ scenarios (MISSING)
- ❌ alerts (MISSING)
- ❌ users (MISSING)
- ❌ watchlists (MISSING)
- ❌ audit (MISSING)

---

## Next Steps for Completion

1. **Implement missing blueprints** (transactions, scenarios, alerts, users, watchlists, audit)
2. **Complete partial blueprints** (backtests POST, performance endpoints)
3. **Register all blueprints** in `rest_entry.py`
4. **Update frontend pages** to use new API endpoints
5. **Add persona selector** to `Home.py`
6. **Test all endpoints** and update this matrix

---

## Notes

- All endpoints should include proper error handling
- All endpoints should log requests using `current_app.logger`
- Database operations should use transactions where appropriate
- Response format should be consistent across all endpoints
- Consider adding pagination for list endpoints (GET all)

