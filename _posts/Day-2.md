# Architecting for performance

## Design Patterns
Matrix multiplication for performance.
Cpu caching is important.
### Row traversal vs Column traversal
Row traversal has greater throughput as it traverses the way cpu cache expects.

### Recommendation
Reduce code footprint as possible. (Smaller methods are better.) Remember JVM already performs some optimizations.

## Tactics

### Cashing
Data Patterns  for cachign and eviction algo affect performance. 

### Batching
Minimmizing round trips in server communications. Remember bandwidth and receiver handling rate.

### Design Asynchronous
Prefer async by default, synchronous only when needed. Use also stateless. In Java use CompletableFuture.

### Mem Access Patters
Access in most linear manner possible. Any jumps reduce access speed. Typ

#### HashMap: 
- chaining: same bucket values are still completely distributed across allocated mem.
- open addressing: better locality.

#### Read Ulrich Drepper

### Lock Free Algos
Avoiding blocking by locks generally lead to beter performance.
- Compare And Swap: In Java Atomic classes.

### Cache Oblivious Algos
- cpu cache optimizatoins
Load array of fields instead of array of objects accessing the field.

### Thread Affomotu
Thread binding to single cpu thus can leverage cpu cache.

### Non Uniform Memory Access
### Large Pages
Can represent larger memory range hence reduces TLB misses
Java has switch to turn on large pages if supported in the OS.
Suitable for mem intensive apps. Large contiguous mem access. Not recomm for shoft lived apps with small working set or apps with large sparsely used heap.

### RamFS or TmpFS
Simulate FS by accessing RAM instead of FS.

## Hardware Recomms
### False sharing
- independent vals sits on the same cache line
- different cores concurrently access that line
- there is at least one writer thread
- high frequency of writing/reading

Java annotian: @sun.misc.Contended

### ZeroBit Recording
hdd stores more sectors per track in the outer parts of hdd than in the inside.
### SSD
Enable Trim: delete immediately istead of delaying to write causing delays
I/O Scheduler: noop vs deadline vs cfg: noop seems little bit better.
Enable write caching

### C-States
- saving energy by sleeping. this causes cpu warm up delays. This is problematic when latency is more important.

### Ky Latency Hierachical Model
cleancode, cyclomatic complexity, cohesion, abstrations.
affordable latency: data strcutures, algos complexities, btaching, caching.
low latency: memory access pattern, lock free, asynchronous processing, stateless, RamFS/TmpFS, GC andobject lifecycle tning.
ultra low latency: Trhead affinity, numa, large pages, false sharing, data oriented design.


