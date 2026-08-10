
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

---

## 2. Async vs Sync Benchmark

Compares sequential (blocking) vs concurrent (async) execution using real
API calls, to demonstrate the real-world speed benefit of `asyncio`.

### What it does
Fetches currency exchange rates (BTC, ETH, USD) from the Coinbase API two ways:
1. **Sequentially** — using `requests`, one call after another
2. **Concurrently** — using `aiohttp` + `asyncio.gather()`, all calls at once

Both runs are timed with `time.perf_counter()`, and the results are printed
side by side along with the speed-up factor.

### Why this matters
`requests` is a blocking library — even inside an `async def` function, a
`requests.get()` call freezes the entire event loop, so nothing else can run
during that wait. `aiohttp` is async-native: it yields control back to the
event loop while waiting on a network response, letting `asyncio.gather()`
run multiple requests concurrently instead of one after another.

### Results(may vary each time)
| Method      | Time taken |
|-------------|------------|
| Sequential  | 3.20 sec   |
| Concurrent  | 0.41 sec   |

Concurrent was 7.81x faster.

### Tech
- Python
- `asyncio`
- `aiohttp`
- `requests` (sequential baseline only)
- Coinbase Exchange Rates API

---

## 3. Async Countdown Timers

Runs multiple independent countdown timers concurrently, using
`asyncio.create_task()`, to make the event loop's interleaving behavior
visible tick by tick.

### What it does
- Prompts the user for how many timers to set, then a name and duration
  (in seconds) for each
- Counts each timer down to zero, printing a line every second
- Runs all timers concurrently, so their countdowns interleave in the
  terminal instead of running one after another

### Why this matters
Watching shorter timers finish before longer ones, even though they all
start together, is direct proof that `asyncio` overlaps wait time instead
of stacking it. This project also introduces `asyncio.create_task()`,
which starts a coroutine running immediately rather than waiting for
`await` — closer to how real agent code manages multiple in-flight tasks.

### Tech
- Python
- `asyncio`

---
