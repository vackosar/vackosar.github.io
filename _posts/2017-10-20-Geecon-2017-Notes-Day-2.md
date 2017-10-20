---
layout: post
title: "Geecon 2017 Notes Day 2"
date: 2017-10-20
---

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


# Adam Bien: No Migrations: Use Webstandard

I lost most of my notes as idea crashed and nothing was autosave to disk. The point that webstandards are suffient.
Uber-Jar doesnot make sense as u dont need to deploy such a huge file.

## Tools
bsyncn tool to push file changes to the browser
Visual Studio Code for js, html, css

## Reactivity
Possible easily with standard CSS webstandard.

## Query
document.querySelector("#save")

## Value binding
saveButton.onclick = (e) => this.header.innerText = e.target.value

## importing
import KrtekSerivce from "./KrtekService.js";

## Sockets
```
new WebSocket("ws://localhost:8080/heroes/heroes")
  .onmessage = e => console.log(e.data)
```

## JaxRS Backend
```
@Stateless
@Path
@GET
```

## TypeScript Problems

Very good, but architects encourage strange patterns. Refactoring is made easier. Use tsc compiler. Disadvantage is the build step. 


# Java 9 Security

## JSSE blocking mode

SSLSocket class. Usedin the smae manner as regular socket.

## JSSE non blocking mode

SSLEngine. Methods wrap() n unwrap() used to transfer data. Handshake triggered by wrap, unwrap, beginHandshake.

## Java 9 new feature: DTLS

DTLS is TLS over UDP. 

## Skipped rest and left for another.

# Hibernate Tips n Tricks

## Primary Keys

### UUID
Advantage in distribution of ability to create id. Hibernate can generate UUID for you.

#### Generation Strategies:
- Random generation
- Timestamp and IP strategy

## Optionals
Entities support getters returning optinals.

## Java 8 Date and Time
JPA 2.2+. 
Hibernate 5+.

## Conversion

### Attirubte convertor
```
@Convertor LocalDateConvertor implements AttributeConvereter<LocalDate, Date>
  java.sql.Date convertToDatanaseColumn(LocalDate date)
  LocalDate convertToEntityAtrribute(sql.Date date)
```


### Auto apply
Allows no need to specify the convertor on all columns.
```@Convertor(autoApply = true)```

## Multi-Tenancy
One db serves multiple consumers sharing same app.

Tenant *-> App ->* Db

- Each tenant can have their own db
- Each tenant can have their own schema

```
TenantIdResolver implements CurrentTenantIdentifierResolver
  resolveCjrrentTenantIdentifier
  validateExistingCurrentSeesions
  setTenantIdentifier

MultiTenantConnectionProvide
  getAnyConnectionProvider
  selectConnectionProvider(tenantIdentifier)
```


# Infinispan

jgroups, lucene, jbossmarshalling. proto buffers, push events, 

## 4 Modes of data distrib

### Local
Not distrib. 
### Invalidation mode
Sending invalidation to other nodes. Infinispan does not hold any data.
### Replicated
Holds data in replicated manner.
### Distributed
Is AP system. ...missed.

## Raft
Client writes. Leader is already elected. Leader maintains partially-orderedreplicated log. Raft cluster accepts write when n/2+1 nodes are up. It is thus CP system. Recovery is complicated sometimes not possible.

Raft is great when you have much more reads than writes.

## Split

Split will happen i.e. cluster will split into two at some point. Rebalance has to happen. Data will be accumulated on both sides of the split.

### Merging
Merge happens when we have two different values for same key. There are auto policies, but they are not enough.

Modes:
- preferred always
- preferrendnon null
- remove all
- custom

Merging has to happen using our business logic.

### Time

Clocks are never the same cross the cluster. It is very hard to sync clock. Do not use time for coordination.

### Append only approach
Event:
- Order can be determined by logic order of event types.
- Some events trigger idempotent actions thus it does not matter.
- ?

#### Op requiing coord
Seq num generator.

#### Transactions
For order and rollback. Order not needed as mentioned. Rollback is not supported. Readers need to able to recover from inconsistent states.

## Ids

UUIDs.

## Demo

Client ->* JobServices