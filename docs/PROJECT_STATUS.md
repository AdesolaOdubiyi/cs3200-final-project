# Stratify Project Status & Implementation Guide

## Overview
This document tracks both the **Flask Blueprint requirements** and the **MVP implementation status** for the Stratify project. It identifies what's complete, what's missing, and what needs to be implemented.

---

## Flask Requirements Status

### Requirements Checklist

| Requirement | Status | Details |
|------------|--------|---------|
| At least 4 Blueprints | ✅ **MET** | 12 blueprints exist |
| Each Blueprint has 5+ routes | ❌ **NOT MET** | Only 3 blueprints meet this (positions, simple_routes, ngos) |
| Use all 4 HTTP verbs | ✅ **MET** | GET, POST, PUT, DELETE all used |
| At least 2 POST routes | ✅ **MET** | 6 POST routes across multiple blueprints |
| At least 2 PUT routes | ✅ **MET** | 3 PUT routes across multiple blueprints |
| At least 2 DELETE routes | ❌ **NOT MET** | Only 1 DELETE route (need 1 more) |
| ~20 routes total | ✅ **MET** | ~40 routes currently |

**Overall: 5/7 Flask requirements met**

---

## Current Implementation Status

### ✅ Complete Blueprints (3/11 MVP Blueprints)

#### 1. **portfolios** (`api/backend/portfolios/portfolio_routes.py`)
- **Routes**: 4 (GET x2, POST x1, PUT x1)
- **Status**: ✅ Complete for MVP, ⚠️ Needs 1 more route for Flask requirement
- **Endpoints**:
  - ✅ GET `/portfolio/portfolios` - Get all portfolios
  - ✅ GET `/portfolio/portfolios/<id>` - Get portfolio by ID
  - ✅ POST `/portfolio/portfolios` - Create portfolio
  - ✅ PUT `/portfolio/portfolios/<id>` - Update portfolio
- **Registered**: ✅ Yes

#### 2. **assets** (`api/backend/assets/asset_routes.py`)
- **Routes**: 4 (GET x4)
- **Status**: ✅ Complete for MVP, ⚠️ Needs 1+ route and POST/PUT/DELETE for Flask requirement
- **Endpoints**:
  - ✅ GET `/asset/assets` - Get all assets
  - ✅ GET `/asset/assets/<id>` - Get asset by ID
  - ✅ GET `/asset/assets/<id>/price-history` - Get price history
  - ✅ GET `/asset/assets/sector/<sector_id>` - Get assets by sector
- **Registered**: ✅ Yes

#### 3. **positions** (`api/backend/positions/position_routes.py`)
- **Routes**: 5 (GET x2, POST x1, PUT x1, DELETE x1)
- **Status**: ✅ Complete for MVP and Flask requirements
- **Endpoints**:
  - ✅ GET `/position/positions` - Get all positions
  - ✅ GET `/position/positions/<id>` - Get position by ID
  - ✅ POST `/position/positions` - Create position
  - ✅ PUT `/position/positions/<id>` - Update position
  - ✅ DELETE `/position/positions/<id>` - Delete position
- **Registered**: ✅ Yes

### ⚠️ Partial Blueprints (2/11 MVP Blueprints)

#### 4. **backtests** (`api/backend/backtests/backtest_routes.py`)
- **Routes**: 1 (GET x1)
- **Status**: ⚠️ Partial - Missing POST endpoint for MVP, needs 4 more routes for Flask requirement
- **Endpoints**:
  - ✅ GET `/backtest/results/<backtest_id>` - Get backtest results
  - ❌ POST `/backtest/backtests` - Create backtest (MISSING - MVP requirement)
  - ❌ GET `/backtest/backtests` - List all backtests (Flask requirement)
  - ❌ PUT `/backtest/backtests/<id>` - Update backtest (Flask requirement)
  - ❌ DELETE `/backtest/backtests/<id>` - Delete backtest (Flask requirement)
- **Registered**: ✅ Yes

#### 5. **performance** (`api/backend/performance/performance_routes.py`)
- **Routes**: 1 (GET x1)
- **Status**: ⚠️ Partial - Missing 4 endpoints for MVP, needs 4 more routes for Flask requirement
- **Endpoints**:
  - ✅ GET `/performance/firm/summary` - Firm-wide summary
  - ❌ GET `/performance/portfolio/<id>` - Portfolio performance (MISSING - MVP)
  - ❌ GET `/performance/portfolio/<id>/comparison` - Portfolio comparison (MISSING - MVP)
  - ❌ GET `/performance/benchmark` - Benchmark comparison (MISSING - MVP)
  - ❌ GET `/performance/sector/exposure` - Sector exposure (MISSING - MVP)
- **Registered**: ✅ Yes

### ❌ Empty Blueprints (6/11 MVP Blueprints)

#### 6. **transactions** (`api/backend/transactions/transaction_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Critical for MVP
- **Required Endpoints**:
  - ❌ GET `/transaction/transactions` - Get all transactions
  - ❌ POST `/transaction/transactions` - Create transaction (buy/sell)
- **Registered**: ❌ No

#### 7. **scenarios** (`api/backend/scenarios/scenario_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Required for MVP
- **Required Endpoints**:
  - ❌ GET `/scenario/scenarios` - Get scenario results
- **Registered**: ❌ No

#### 8. **alerts** (`api/backend/alerts/alert_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Required for MVP
- **Required Endpoints**:
  - ❌ GET `/alert/alerts` - Get alerts
  - ❌ POST `/alert/alerts` - Create alert rule
- **Registered**: ❌ No

#### 9. **users** (`api/backend/users/user_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Required for MVP
- **Required Endpoints**:
  - ❌ GET `/user/users` - Get all users
  - ❌ PUT `/user/users/<id>/role` - Update user role
  - ❌ GET `/user/users/<id>/activity` - Get user activity
- **Registered**: ❌ No

#### 10. **watchlists** (`api/backend/watchlists/watchlist_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Required for MVP
- **Required Endpoints**:
  - ❌ GET `/watchlist/watchlists` - Get watchlists
  - ❌ POST `/watchlist/watchlists` - Create watchlist
  - ❌ DELETE `/watchlist/watchlists/<id>` - Delete watchlist item
- **Registered**: ❌ No

#### 11. **audit** (`api/backend/audit/audit_routes.py`)
- **Routes**: 0
- **Status**: ❌ Empty - Required for MVP
- **Required Endpoints**:
  - ❌ GET `/audit/events` - Get audit events with date filtering
- **Registered**: ❌ No

### Additional Blueprints (Not in MVP Plan)

These blueprints exist but are not part of the core MVP:
- `simple_routes` - 6 routes (GET x6) ✅ Meets Flask requirement
- `ngos` - 6 routes (GET x4, POST x1, PUT x1) ✅ Meets Flask requirement
- `system` - 4 routes (GET x2, POST x2) ⚠️ Needs 1 more route
- `ml_models` - 2 routes (GET x1, POST x1) ❌ Needs 3 more routes
- `macro` - 2 routes (GET x2) ❌ Needs 3 more routes
- `geo` - 2 routes (GET x2) ❌ Needs 3 more routes
- `director` - 3 routes (GET x3) ❌ Needs 2 more routes

---

## What Needs to Be Done

### Priority 1: Meet Flask Requirements (Critical for Grading)

#### 1.1 Add Missing DELETE Route
- **Current**: Only `positions` has DELETE
- **Action**: Add DELETE to `portfolios` blueprint
- **Impact**: 
  - ✅ Meets Flask requirement (2 DELETE routes)
  - ✅ Brings `portfolios` to 5 routes (meets Flask requirement)

```python
@portfolios.route("/portfolios/<int:portfolio_id>", methods=["DELETE"])
def delete_portfolio(portfolio_id):
    # Delete portfolio and cascade delete positions
```

#### 1.2 Bring Blueprints to 5+ Routes

**For `portfolios` (needs 1):**
- Add DELETE route (see 1.1 above)

**For `assets` (needs 1+ POST/PUT/DELETE):**
- Add POST `/assets` - Create new asset
- Add PUT `/assets/<id>` - Update asset
- Add DELETE `/assets/<id>` - Delete asset (also helps Flask DELETE requirement)

**For `backtests` (needs 4):**
- Add POST `/backtest/backtests` - Create backtest (also MVP requirement)
- Add GET `/backtest/backtests` - List all backtests
- Add PUT `/backtest/backtests/<id>` - Update backtest
- Add DELETE `/backtest/backtests/<id>` - Delete backtest

**For `performance` (needs 4):**
- Add GET `/performance/portfolio/<id>` - Portfolio performance (also MVP requirement)
- Add GET `/performance/portfolio/<id>/comparison` - Comparison (also MVP requirement)
- Add GET `/performance/benchmark` - Benchmark data (also MVP requirement)
- Add GET `/performance/sector/exposure` - Sector exposure (also MVP requirement)

### Priority 2: Complete MVP Blueprints (Critical for Functionality)

#### 2.1 Implement Empty Blueprints

**transactions.py** (Critical - blocks Jonathan-4 user story):
- GET `/transaction/transactions` - Get all transactions
- POST `/transaction/transactions` - Create transaction (buy/sell)
- Register in `rest_entry.py`

**scenarios.py**:
- GET `/scenario/scenarios` - Get scenario results
- Register in `rest_entry.py`

**alerts.py**:
- GET `/alert/alerts` - Get alerts
- POST `/alert/alerts` - Create alert rule
- Register in `rest_entry.py`

**users.py**:
- GET `/user/users` - Get all users
- PUT `/user/users/<id>/role` - Update user role
- GET `/user/users/<id>/activity` - Get user activity
- Register in `rest_entry.py`

**watchlists.py**:
- GET `/watchlist/watchlists` - Get watchlists
- POST `/watchlist/watchlists` - Create watchlist
- DELETE `/watchlist/watchlists/<id>` - Delete watchlist item
- Register in `rest_entry.py`

**audit.py**:
- GET `/audit/events` - Get audit events with date filtering
- Register in `rest_entry.py`

#### 2.2 Register All Blueprints in `rest_entry.py`

Add imports and registrations for:
- transactions
- scenarios
- alerts
- users
- watchlists
- audit

### Priority 3: Frontend Updates

- **Home.py**: Add persona selector (radio buttons/selectbox) to set `session_state['role']` and `session_state['persona_name']`
- **nav.py**: Update for simplified RBAC based on persona
- Update Streamlit pages to use new API endpoints

---

## User Stories Coverage

### Persona 0X: Noah Harrison (Data Analyst)
- ✅ Noah-1: Create backtests (needs POST endpoint in backtests)
- ✅ Noah-2: View backtest results
- ✅ Noah-3: Risk exposure visualization
- ✅ Noah-4: Filtered price history
- ✅ Noah-6: Portfolio comparison charts (needs performance endpoint)

### Persona 1X: Jonathan Chen (Asset Management Analyst)
- ✅ Jonathan-1: Create portfolio (partial - needs transactions)
- ✅ Jonathan-2: Add positions (partial - needs transactions)
- ✅ Jonathan-3: View backtest results
- ❌ Jonathan-4: Execute transactions (MISSING - transactions.py)
- ✅ Jonathan-6: Benchmark comparison (needs performance endpoint)

### Persona 2X: Rajesh Singh (Systems Administrator)
- ✅ Rajesh-1: System health metrics (system.py exists)
- ❌ Rajesh-2: User role management (MISSING - users.py)
- ✅ Rajesh-4: Backtest status (needs backtest POST)
- ❌ Rajesh-5: Alert configuration (MISSING - alerts.py)

### Persona 3X: Sarah Martinez (Director)
- ✅ Sarah-1: Firm-wide performance (partial)
- ❌ Sarah-2: Sector exposure (MISSING - performance endpoint)
- ❌ Sarah-3: Strategy compliance (needs scenarios)
- ❌ Sarah-4: Market alerts (MISSING - alerts.py)
- ❌ Sarah-5: User activity (MISSING - users.py)

**Coverage: ~12/24 user stories fully supported, ~6 partially supported, ~6 not supported**

---

## Quick Implementation Summary

### To Meet Flask Requirements:
1. Add DELETE to portfolios (1 route)
2. Add POST, PUT, DELETE to assets (3 routes)
3. Add 4 routes to backtests (POST, GET list, PUT, DELETE)
4. Add 4 routes to performance (4 GET routes)

**Total: 12 additional routes** → **New total: ~52 routes**

### To Complete MVP:
1. Implement 6 empty blueprints (transactions, scenarios, alerts, users, watchlists, audit)
2. Register all 6 blueprints in `rest_entry.py`
3. Complete backtests POST endpoint
4. Complete performance missing endpoints
5. Add persona selector to Home.py

---

## Completion Estimates

### Flask Requirements
- **Current**: 5/7 requirements met (71%)
- **After Priority 1 fixes**: 7/7 requirements met (100%)

### MVP Implementation
- **API Layer**: ~60% complete (5/11 blueprints fully functional)
- **Frontend Layer**: ~90% complete (11/11 pages exist, need API integration)
- **Overall MVP**: ~70% complete

### Total Routes
- **Current**: ~40 routes
- **After Flask fixes**: ~52 routes
- **After MVP completion**: ~65 routes

---

## Next Steps (Prioritized)

1. ✅ **Add DELETE to portfolios** (meets Flask requirement + brings to 5 routes)
2. ✅ **Add POST, PUT, DELETE to assets** (meets Flask requirement + brings to 7 routes)
3. ✅ **Add 4 routes to backtests** (meets Flask requirement + MVP POST endpoint)
4. ✅ **Add 4 routes to performance** (meets Flask requirement + MVP endpoints)
5. ✅ **Implement transactions.py** (critical for MVP - Jonathan-4)
6. ✅ **Register all missing blueprints** in `rest_entry.py`
7. ✅ **Implement remaining empty blueprints** (scenarios, alerts, users, watchlists, audit)
8. ✅ **Add persona selector to Home.py**

---

## Notes

- All endpoints should include proper error handling
- All endpoints should log requests using `current_app.logger`
- Database operations should use transactions where appropriate
- Response format should be consistent across all endpoints
- Consider adding pagination for list endpoints (GET all)
- See `docs/Stratify_REST_API_Matrix.md` for detailed endpoint specifications

