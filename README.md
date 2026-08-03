
# API Projects

A collection of small Python projects exploring API!!

---

## 1. Weather Checker

Fetches real-time weather data for Indian cities using the Open-Meteo API.

### What it does
- Gets live temperature and wind speed for Bangalore, Mumbai, and Delhi
- Labels each city as Cold, Moderate, or Hot based on temperature

### Why this matters
A hands-on exercise in consuming a real public API — handling requests,
parsing JSON responses, and turning raw data into something meaningful
(the Cold/Moderate/Hot classification).

### Tech
- Python
- `requests`
- Open-Meteo API

---

## 2. Async vs Sync Benchmark

Compares sequential (blocking) vs concurrent (async) execution using
simulated delays, to demonstrate the real-world speed benefit of `asyncio`.

### What it does
Simulates fetching data for 5 people two ways:
1. **Sequentially** — using `time.sleep()`, one call after another
2. **Concurrently** — using `asyncio.sleep()` + `asyncio.gather()`, all calls at once

Both runs are timed with `time.perf_counter()`, and the results are printed
side by side along with the speed-up factor.

### Why this matters
`time.sleep()` blocks the entire program — nothing else can happen while
one call is "waiting." `asyncio.sleep()` inside a coroutine yields control
back to the event loop instead, letting `asyncio.gather()` run multiple
"waits" concurrently rather than stacking them up one after another. This
is the same mechanism that lets a real program make several API calls at
once instead of waiting for each one to finish before starting the next.

### Results(varies each time)
| Method      | Time taken |
|-------------|------------|
| Sequential  | 7.89 sec   |
| Concurrent  | 3.23 sec   |



### Tech
- Python
- `asyncio`

### Next step
A future version will replace simulated delays with real API calls using
`aiohttp`, once async-native HTTP libraries are covered.

---

## Setup
Each project is self-contained. Install dependencies as needed per project
(see individual files for imports used) and run directly with `python <filename>.py`.
## 2. Async vs Sync Benchmark

Compares
