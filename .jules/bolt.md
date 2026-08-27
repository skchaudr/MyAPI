## 2024-05-18 - Async Endpoint File I/O Optimization
**Learning:** Performing synchronous file I/O operations directly within `async def` endpoints blocks the entire asyncio event loop. In high-throughput APIs handling large datasets (e.g. exporting documents), a blocked loop prevents concurrent requests from being processed, causing major responsiveness degradation.
**Action:** Always offload synchronous file I/O and CPU-bound operations in async FastAPI endpoints using `await asyncio.get_running_loop().run_in_executor(None, sync_function, *args)`.
