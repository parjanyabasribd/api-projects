
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

## 4. Multi-Tool Assistant (Gemini Function Calling)

Gives Gemini two custom tools — a GitHub user lookup and a random advice
generator — and lets the model decide which one (or several) to call based
on the user's question, showing exactly which tools were used.

### What it does
- Fetches public GitHub profile stats (repos, followers, bio) for a given username
- Fetches a random piece of advice
- Correctly answers unrelated questions directly, without forcing a tool call
- Displays which tool(s), if any, were actually called for transparency

### Why this matters
This demonstrates real compositional/multi-step tool use, not just a single
lookup. For example, asking the assistant to "compare GitHub followers for
two users, then give advice based on the result" triggers three sequential
tool calls in one turn — two GitHub lookups plus an advice call — with the
model reasoning over all three results to form one coherent answer. This is
the same Reason → Act → Observe mechanism (the ReAct pattern) that powers
real AI agents, handled automatically here by Gemini's function calling.

Uses `client.chats.create()` instead of a single `generate_content()` call,
since a chat session automatically tracks the growing conversation and tool
call history needed for multi-step reasoning — a single stateless call
can't do this on its own.

### Tech
- Python
- Gemini API (`google-genai`) — automatic function calling, chat sessions
- GitHub public API
- Advice Slip API

### Setup
1. Clone the repo
2. Create a `.env` file in the root (see `.env.example` for the required variable)
3. Add your own Gemini API key: `GEMINI_API_KEY=your_key_here`
4. Install dependencies: `pip install google-genai requests python-dotenv`
5. Run: `python multi_tool_assistant.py`

---

## 5. Multi-Turn Agent (Chat with Memory + Tool Use)

An interactive command-line agent that remembers the full conversation
and can call tools — country lookups, book search, and number facts —
reasoning across multiple turns, and automatically trimming its own
history to stay within the model's context window.

### What it does
- Answers questions about countries (population, capital, languages) via
  the REST Countries API
- Looks up books (author, publish year, page count) via the Open Library API
- Fetches trivia facts about numbers via the Numbers API
- Remembers prior turns — correctly resolves follow-up questions like "what's
  its capital?" or "who wrote it?" without repeating the subject
- Automatically trims conversation history once it exceeds a set length,
  keeping the most recent context and discarding the oldest
- Displays a running log of every tool called during the conversation
- Detects when the user wants to end the chat using an LLM-based check for
  natural phrasing, not just exact "quit"/"exit" matches

### Why this matters
A conversation can't grow forever — every model has a maximum context
window, and an unbounded chat session will eventually fail or lose control
over what gets remembered. This agent uses a persistent `chat` session
(`client.chats.create()`) for multi-turn memory, then periodically checks
the raw history length and, once it passes a threshold, rebuilds the
session from just the most recent items — keeping the conversation
functional indefinitely without silently overflowing the context window.

### Tech
- Python
- Gemini API (`google-genai`) — chat sessions, automatic function calling,
  history management
- REST Countries API
- Open Library API
- Numbers API

### Setup
1. Clone the repo
2. Create a `.env` file in the root (see `.env.example` for the required variable)
3. Add your own Gemini API key: `GEMINI_API_KEY=your_key_here`
4. Install dependencies: `pip install google-genai requests python-dotenv`
5. Run: `python multi_turn_agent.py`

---