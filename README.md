# DuckDB Changelog

A single-file changelog of all [DuckDB's releases](https://github.com/duckdb/duckdb/releases).

> [!WARNING]
> Open the README file manually [here](README.md) to see all versions; GitHub
> truncates large README files on a repository's homepage by default.

# Table of Contents

- [v1.4.0 - DuckDB 1.4.0 "Andium"](#v140)
- [v1.3.2 - v1.3.2 Bugfix Release](#v132)
- [v1.3.1 - v1.3.1 Bugfix Release](#v131)
- [v1.3.0 - DuckDB 1.3.0 "Ossivalis" ](#v130)
- [v1.2.2 - v1.2.2 Bugfix Release](#v122)
- [v1.2.1 - v1.2.1 Bugfix Release](#v121)
- [v1.2.0 - DuckDB 1.2.0 "Histrionicus"](#v120)
- [v1.1.3 - v1.1.3 Bugfix Release](#v113)
- [v1.1.2 - v1.1.2 Bugfix Release](#v112)
- [v1.1.1 - v1.1.1 Bugfix Release](#v111)
- [v1.1.0 - DuckDB 1.1.0 "Eatoni"](#v110)
- [v1.0.0 - DuckDB 1.0.0 "Nivis"](#v100)
- [v0.10.3 - v0.10.3 Bugfix Release](#v0103)
- [v0.10.2 - v0.10.2 Bugfix Release](#v0102)
- [v0.10.1 - v0.10.1 Bugfix Release](#v0101)
- [v0.10.0 - DuckDB 0.10.0 "Fusca"](#v0100)
- [v0.9.2 - 0.9.2 Bugfix Release ](#v092)
- [v0.9.1 - 0.9.1 Bugfix Release](#v091)
- [v0.9.0 - 0.9.0 Preview Release "Undulata"](#v090)
- [v0.8.1 - 0.8.1 Bugfix Release](#v081)
- [v0.8.0 - 0.8.0 Preview Release "Fulvigula"](#v080)
- [v0.7.1 - 0.7.1 Bugfix Release](#v071)
- [v0.7.0 - 0.7.0 Preview Release "Labradorius"](#v070)
- [v0.6.1 - 0.6.1 Bugfix Release](#v061)
- [v0.6.0 - 0.6.0 Preview Release "Oxyura"](#v060)
- [v0.5.1 - 0.5.1 Bugfix Release](#v051)
- [v0.5.0 - 0.5.0 Preview Release "Pulchellus"](#v050)
- [v0.4.0 - 0.4.0 Preview Release "Ferruginea"](#v040)
- [v0.3.4 - 0.3.4 Bugfix Release](#v034)
- [v0.3.3 - 0.3.3 Preview Release "Sansaniensis"](#v033)
- [v0.3.2 - 0.3.2 Preview Release "Gibberifrons"](#v032)
- [v0.3.1 - 0.3.1 Preview Release "Spectabilis"](#v031)
- [v0.3.0 - 0.3.0 Preview Release "Gracilis"](#v030)
- [v0.2.9 - 0.2.9 Preview Release "Platyrhynchos"](#v029)
- [v0.2.8 - 0.2.8 Preview Release "Ceruttii"](#v028)
- [v0.2.7 - 0.2.7 Preview Release "Mollissima"](#v027)
- [v0.2.6 - 0.2.6 Preview Release "Jamaicensis"](#v026)
- [v0.2.5 - 0.2.5 Preview Release "Falcata"](#v025)
- [v0.2.4 - 0.2.4 Preview Release "Jubata"](#v024)
- [v0.2.3 - 0.2.3 Preview Release "Serrator"](#v023)
- [v0.2.2 - 0.2.2 Preview Release "Clypeata"](#v022)
- [v0.2.1 - 0.2.1 Preview Release](#v021)
- [v0.2.0 - 0.2.0 Preview Release](#v020)
- [v0.1.9 - 0.1.9 Preview Release](#v019)
- [v0.1.8 - 0.1.8 Preview Release](#v018)
- [v0.1.7 - 0.1.7 Preview Release](#v017)
- [v0.1.6 - 0.1.6 Preview Release](#v016)
- [v0.1.5 - 0.1.5 Preview Release](#v015)
- [v0.1.3 - 0.1.3 Preview Release](#v013)
- [v0.1.2 - 0.1.2 Preview Release](#v012)
- [v0.1.1 - 0.1.1 Preview Release](#v011)
- [v0.1.0 - 0.1.0 Preview Release](#v010)

---

# v1.4.0 - DuckDB 1.4.0 "Andium" <a id="v140"></a>

*Released on 2025-09-16*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.4.0)

This release of DuckDB is named "Andium" after Anas Andium, a species of duck that lives in the Andes mountains in South America.

Please also refer to the announcement blog post: https://duckdb.org/2025/09/16/announcing-duckdb-140.html


## What's Changed
* Python package devexp improvements by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/17483
* change exception type to not be an internal exception by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17551
* Remove redundant code path in the ConflictManager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17562
* Add support for ToSqlString for union types by [@wmTJc9IK0Q](https://github.com/wmTJc9IK0Q) in https://github.com/duckdb/duckdb/pull/17513
* Update function descriptions and examples by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17132
* Move query profiler's EndQuery after commit/rollback by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17595
* fix extension troubleshooting link by [@simon0191](https://github.com/simon0191) in https://github.com/duckdb/duckdb/pull/17616
* C API tidying by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17623
* bump DuckDB_jll to v1.3.0 by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17677
* Add rowsort in generate_series test #43 by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/17675
* [C API] Expose duckdb_scalar_function_bind_get_extra_info by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17666
* Enable profiling output for all operator types by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17665
* Output hashes in unittest and fix order by [@niykko](https://github.com/niykko) in https://github.com/duckdb/duckdb/pull/17664
* New Sorting Implementation by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17584
* Merge v1.3-ossivalis into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17690
* Issue #17040: FILL Window Function  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17686
* ClientBufferManager wrapper to access the client context in the buffer manager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17699
* Revert "set default for MAIN_BRANCH_VERSIONING to false" by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17708
* Sorting followup by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17717
* Correctly setting the delim offset by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/17716
* fix linux extension ci by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17720
* Aggregation performance by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17718
* Fix windows-2025 build errors by [@adsharma](https://github.com/adsharma) in https://github.com/duckdb/duckdb/pull/17726
* [SQLLogicTester] Introduce `reset label <query label>` in the tester by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17729
* Adding additional authenticated data for encryption by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17508
* csv_scanner: correct code comment by [@Djfe](https://github.com/Djfe) in https://github.com/duckdb/duckdb/pull/17735
* Deprecate windows-2019 runners  by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/17745
* re-add httpfs apply_patches by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17755
* Rename decorator from test_nulls to null_test_parameters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17760
* [CAPI] Expose ErrorData by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17722
* Expose file_size_bytes and footer_size in parquet_file_metadata by [@gijshendriksen](https://github.com/gijshendriksen) in https://github.com/duckdb/duckdb/pull/17750
* Pass `ExtensionLoader` when loading extensions, change extension entry function by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17772
* Support glibc 2.28 environments by [@James-Gilbert-](https://github.com/James-Gilbert-) in https://github.com/duckdb/duckdb/pull/17776
* Mark Upper/LowerComparisonType as const by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/17773
* [Indexes] Buffer-managed indexes part 1: segment handles by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17758
* [Julia] api docs improvements  by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15645
* Ensure we use the same layout in `RadixPartitionedHashTable` and `GroupedAggregateHashTable` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17790
* [Profiling] Propagate the ClientContext into file handle writes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17754
* Fix propagatesNullValues for case expr by [@suibianwanwank](https://github.com/suibianwanwank) in https://github.com/duckdb/duckdb/pull/17796
* Add qualified parameter to Python GetTableNames API by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/17797
* Merge v1.3 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17806
* Pushdown pivot filter by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/17801
* Replace string for const data ptr in encryption api by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17825
* Merge130 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17833
* fix: escape using_columns on JoinRef::ToString by [@akoshchiy](https://github.com/akoshchiy) in https://github.com/duckdb/duckdb/pull/17839
* Fix ICE with Windows ARM64 by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17844
* Merge v1.3 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17851
* Add `duckdb_type` column to parquet_schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17852
* Internal #4991: Remove Epoch_MS(MS) by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17816
* #17853 Enable flexible page sizes and update Android NDK to r27 in workflow. by [@aprock](https://github.com/aprock) in https://github.com/duckdb/duckdb/pull/17854
* [Indexes] Buffer-managed indexes part 2: segment handle for base nodes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17828
* Function Serialization: adapt to removal of overloads by explicitly casting if argument types have changed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17864
* julia: add missing methods from C-API by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/17733
* Issue #17153: Window Order Columns by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17835
* Issue #17040: FILL Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17821
* Add STRUCT to MAP cast function by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/17799
* Issue #17849: Test FILL Duplicates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17869
* Add GenAI policy by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17882
* Update function descriptions and examples for list, array, lambda functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17886
* Issue #17861: FILL Argument Types by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17888
* Reword GenAI policy by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17895
* Use an arena linked list for the physical operator children by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17748
* Make CTE Materialization the Default Instead of Inlining by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/17459
* Merge v1.3 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17897
* Leverage `VectorType` in `ColumnDataCollection` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17881
* Fix empty BP block when writing parquet by [@platypii](https://github.com/platypii) in https://github.com/duckdb/duckdb/pull/17929
* fix use after free in adbc on invalid stmt by [@ruslandoga](https://github.com/ruslandoga) in https://github.com/duckdb/duckdb/pull/17927
* Do not dispatch JDBC/ODBC jobs in release CI runs by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17937
* Block based encryption by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17275
* Unittester failures summary by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16833
* Add v1.3-ossivalis to Cross version workflow by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17906
* [CI Nightly Fix] Skip logging test if not standard block size by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17957
* Visual Studio 17 (2022) fixes by [@edouarda](https://github.com/edouarda) in https://github.com/duckdb/duckdb/pull/17948
* [Nested] Add `struct_position` and `struct_contains` functions by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17819
* Enable building spatial and encodings extensions by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17960
* [Nested] Optimize structs in `LIST_VALUE` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17169
* Unit Tester Configuration by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17972
* [nested] Allow fixed-size arrays to be unnested by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17968
* Merge v1.3-ossivalis into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17973
* [CI] Skip some workflows when updating out of tree extensions SHA by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17949
* Issue #5144: AsOf Join Threshold by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17979
* [Fix] Reset profiling info before preparing a query by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17940
* Flag to disable database invalidation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17938
* Issue #5123: make_timestamp_ms by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17908
* Rework extension loading to go through thread-safe ExtensionManager by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17994
* Implement consumption and production of Arrow Binary View by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17975
* Add support to produce Polars Lazy Dataframes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17947
* c-api to copy vector with selection by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/17870
* Fix #18007: correctly execute expressions with pivot operator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18020
* [Chore] Minor conflict manager refactoring by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18015
* Remove Linux (32 Bit) job by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18012
* [Explain] Add the YAML format for EXPLAIN statements by [@qsliu2017](https://github.com/qsliu2017) in https://github.com/duckdb/duckdb/pull/17572
* Unittest: Add skip_compiled option that can be used to skip built-in C++ tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18034
* Add ppc64le spin-wait instruction by [@mgiessing](https://github.com/mgiessing) in https://github.com/duckdb/duckdb/pull/17837
* Merge ossivalis into main by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18036
* Remove match-case statements from polars_io.py by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18052
* Avoid adding commands read from a file to the shell history by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18057
* Adding WAL encryption by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17955
* Encryption: adding -key for the command line by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17950
* fix star expr exclude error by [@jayhan94](https://github.com/jayhan94) in https://github.com/duckdb/duckdb/pull/18063
* Add support for class-based expression iteration by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18070
* Use `timestamp_t` instead of `time_t` for file last modified time by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18037
* Unittester: add `on_new_connection` + `on_load` + `skip_tests` options by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18042
* Fix some scaling issues by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17985
* Issue #18071: Temporal inf -inf by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18083
* Switch to Optional for type hints in polars lazy dataframe function by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18078
* Unittest: Configure skip error messages by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18087
* Avoid running DraftPR.yml until timeout if token is missing by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18090
* Add start/end offset percentage options to Python test runner by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/18091
* [CSV Reader] Prohibit options delim and sep in same read_csv call by [@ackxolotl](https://github.com/ackxolotl) in https://github.com/duckdb/duckdb/pull/18096
* Fix  correlated subquery unnest fail by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/18092
* [CI] don't run jobs on draft PRs by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18016
* TPC-DS: Use BIGINT fields by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18098
* Don't throw `InternalException` in `Sort::Sink` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18105
* ci: build duckdb against the latest emscripten by [@cpcloud](https://github.com/cpcloud) in https://github.com/duckdb/duckdb/pull/18110
* [chore] Merge v1.3-ossivalis on main by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18109
* Update description of 'arrow_lossless_conversion' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18046
* Internal #3273: Window Task Generation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18113
* set ::error:: annotations for test runners by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18072
* Improve sort key comparison performance by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18131
* Add support for `MERGE INTO` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18135
* Detect when updates have no effect, and skip performing the actual updates if we encounter these nop updates by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18144
* Add support for AdbcConnectionGetObjects(table_type) by [@kou](https://github.com/kou) in https://github.com/duckdb/duckdb/pull/18066
* Issue #17683: TIME_NS Compilation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18053
* Implement `replace_type` function by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18077
* Bump spatial again: include re-linking for handling global objects in Wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18170
* Resolve some small build issues by [@madscientist](https://github.com/madscientist) in https://github.com/duckdb/duckdb/pull/18162
* fix typo by [@felixhummel](https://github.com/felixhummel) in https://github.com/duckdb/duckdb/pull/18165
* Avoid `realloc` in CSV writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18174
* fix bug with allowed_paths by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18176
* Reduce lock contention for the instance cache by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/18079
* Check if `GetLastSegment` is not `nullptr` in `ColumnData::RevertAppend` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18171
* [Profiling] Move the client context into more write functions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17875
* Bump Julia to v1.3.2 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18185
* Merge `v1.3-ossivalis` into `main` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18188
* Parquet reader logging by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18172
* Add VS2019 compat flag to Python wheel build by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/18198
* [Parquet][Dev] Update the vendored `parquet.thrift` to `3ce0760` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18195
* Two-rowID-leaf support in the conflict manager and general refactoring by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18194
* More internal-linkage by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18177
* Temporary file encryption by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18208
* Adding temporary file encryption by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/18013
* Skip logging test for smaller block sizes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18201
* ci(pyodide): enable WASM exceptions on the latest pyodide build by [@cpcloud](https://github.com/cpcloud) in https://github.com/duckdb/duckdb/pull/18173
* Allow explicit compression for user types by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18219
* Get type of encoded `SortKey` from `TupleDataLayout` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18218
* Improve Parquet reader `NULL` statistics and compress all-`NULL` columns using `CompressedMaterialization` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18217
* Internal #5264: NLJ Not Distinct by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18216
* Bug#18163 Fix STDDEV_SAMP undeterminism by [@minaracic](https://github.com/minaracic) in https://github.com/duckdb/duckdb/pull/18210
* [Parquet] Add read support for the `VARIANT` LogicalType by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18187
* Track `DataChunk` memory usage in various places by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18191
* Better `NULL` handling in `TupleDataLayout` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18069
* Dictionary functions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18127
* Add support for geoarrow encoded geometries in geoparquet files. by [@cfis](https://github.com/cfis) in https://github.com/duckdb/duckdb/pull/17942
* Improve descriptions of thresholds vars affecting join algorithm selection by [@TheHillBright](https://github.com/TheHillBright) in https://github.com/duckdb/duckdb/pull/17377
* Connect relations that are not in a subgraph, but are still part of the new relation set by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18182
* [Fix] Don't write empty (partial) blocks for FSST dictionary compression by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18203
* Slightly higher memory limit for test by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18235
* Re-add string -> hugeint compressed materialization function by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18234
* [Fix] Database path conflict resolution by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18247
* Remove require block size from a batch of tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18242
* Add nightly builds for out-of-tree python extension by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18239
* Backport DB invalidation flag to ossivalis by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18244
* Bump vcpkg-duckdb-ports and test extensions on Windows 10 default stdlib by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18205
* Add type safety to `FlatVector::GetData<T>`, `ConstantVector::GetData<T>` and `UnifiedVectorFormat::GetData<T>` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18256
* [Fix] Adjust test for smaller block sizes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18255
* Fix integer overflow in sequence vector by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/18245
* fixes for some minor llvm 20 complaints by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18257
* update run_extension_medata_tests.sh by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17976
* Bunch of loosely connected test/CI fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18254
* disable WebAssembly duckdb-wasm builds job in NightlyTests triggered by 'workflow_dispatch' event by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18129
* Allow for static libs from extension dependencies to be bundled by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/18226
* Fix dictionary-related assertions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18260
* Fixes for gcc 15 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18261
* Reduce copy in Vector::Reinterpret by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/18264
* [Parquet] Add read support for the `VARIANT` LogicalType (with shredded encoding) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18224
* Expanded autocomplete suggestions by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18243
* Support HUGEINT in printf and format by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/13277
* Move aarch64 / arm64 to native github runner by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18269
* Bump vcpkg-duckdb-ports to solve OSX linking by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18268
* Add support for RETURNING to MERGE INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18271
* Use set for row ID scanning during index scans by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18274
* Use DuckDB cast infrastructure in fmt for new uhugeint/hugeint code by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18275
* [Fix] Adjust test to run with different block sizes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18277
* Use `FromEpochSeconds` instead of `FromTimeT` in `FileSystem::GetLastModifiedTime` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18281
* Add target for installing Python deps. by [@xevix](https://github.com/xevix) in https://github.com/duckdb/duckdb/pull/18285
* backport 'Unit Tester Configuration' pt2 by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18282
* backport 'Unit Tester Configuration' by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18263
* Fixup Main.yml for v1.3-ossivalis post https://github.com/duckdb/duckdb/pull/18282 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18289
* SHOW TABLES FROM <qualified_name> by [@xevix](https://github.com/xevix) in https://github.com/duckdb/duckdb/pull/18179
* [Unittester] Add autoloading option by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18290
* Merge ossivalis into main by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18272
* resolve hidden merge conflict with duplicate db name in json configs by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18292
* Bump vcpkg-duckdb-ports, now fixing also mingw by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18300
* [Fix] Missing block when renaming fields by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18293
* [Arrow] Fix unused static function warning by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18278
* feat: Parquet extension add row_group_compressed_size by [@mapleFU](https://github.com/mapleFU) in https://github.com/duckdb/duckdb/pull/18294
* [Parquet][Write] Fix timestamp sec writes to parquet by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18273
* bump httpfs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18258
* [Clang Tidy] Fix missing includes in `patas_scan.hpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18276
* New Arrow C-API by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18246
* Skip test/sql/copy/s3/url_encode.test due to httpfs update by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18317
* Make storage-version a test parameter by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18324
* Backport #18254 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18306
* feat: making Parquet write RowGroup.total_compressed_size by [@mapleFU](https://github.com/mapleFU) in https://github.com/duckdb/duckdb/pull/18307
* add the from-table-function as parameter to copy-from-bind by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/18004
* Python external dispatch param fixes by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18343
* Aarch64 backport by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18345
* Fix debug error in join order optimizer by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18344
* [Fix] Block verification for add and drop field info by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18302
* download Real Nest data in quiet mode by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18346
* Fix condition indexes in join filter pushdown by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/18341
* [unittest] - fix doubled error headers on `Unexpected failure` by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18314
* Extend PEG parser grammar by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18221
* [C API] Expose expressions and use them in scalar function binding by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18142
* Restore OSX tests, moving them to single `--autoloading available` step by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18335
* Add support for checkpointing in-memory tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18348
* Revert "[unittest] - fix doubled error headers on `Unexpected failure`" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18355
* Python external dispatch param fixes by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18359
* Re-enable url-encode test by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18360
* Enable stack traces on linux for bundled libraries by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18363
* Split up out-of-tree extensions into separate files, and allow out-of-tree extensions to be built using BUILD_EXTENSIONS={ext_name} by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18357
* Pass `AttachOptions` to `attach` method, and turn `StorageExtensionInfo` into an `optional_ptr` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18368
* Merge `v1.3-ossivalis` into `main` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18364
* More robustness around deprecated extension settings by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18353
* Add missing ninja to workflow file by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18373
* bump httpfs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18380
* Re-enable but deprecate CORE_EXTENSIONS in CMakeLists.txt by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18377
* Uncomment skipped decimal REE tests by [@amoeba](https://github.com/amoeba) in https://github.com/duckdb/duckdb/pull/18372
* add option 'block_size' to test configs by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18347
* [chore] Fixup side-effects from 8cf9ed43b60 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18385
* Bump httpfs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18388
* Re-use table metadata when table is not altered during checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18390
* Approx database count system function by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18392
* Re-use metadata of unaltered row groups when checkpointing a table by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18395
* Correct and consistent integer arithmetic error messages by [@soerenwolfers](https://github.com/soerenwolfers) in https://github.com/duckdb/duckdb/pull/18393
* Record whether or not cross products are implicit or not, and use this for converting queries back to SQL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18394
* CI: Fix Discussion mirroring by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18397
* Store extra metadata blocks in RowGroupPointer, and only flush dirty Metadata blocks by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18398
* Internal #3273: Window Hashed Sort by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18337
* Wrap runner.ExecuteFile, otherwise cleanup is not properly performed by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18400
* [BUGFIX] Update delim offset for RHS of DELIM JOIN when correlated column is in RHS of Cross product by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18375
* CI: Add separate job for discussion mirroring by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18407
* [ Python SQLLogic Tester ] Add `MERGE_INTO` statement to duckdb python by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18402
* Remove incorrect assertion by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18404
* Internal #5294: TIME_NS C API by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18215
* Add DuckLake back in by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18405
* Add support for table_constraints of AdbcConnectionGetObjects() by [@kou](https://github.com/kou) in https://github.com/duckdb/duckdb/pull/18181
* Merge `v1.3-ossivalis` in `main` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18401
* feat: remove anything following `?` in database name by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18417
* Correctly fetch only base column data in ColumnData::FetchUpdateData by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18423
* Refactor extension CI to use extension-ci-tools by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18361
* Internal #5367: SortedAggregateFunction Sort Update  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18408
* Internal #5368: WindowNaiveAggregator Sort Update  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18409
* [Fix] Block size nightly by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18425
* [Chore] Tidy test configs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18426
* Include pyodide build configuration by [@rgbkrk](https://github.com/rgbkrk) in https://github.com/duckdb/duckdb/pull/18183
* Parquet: add row-group ordinal during writing encryption by [@mapleFU](https://github.com/mapleFU) in https://github.com/duckdb/duckdb/pull/18433
* [Fix] Reset segment memory when initialising new Prefix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18441
* Update pyodide build to 0.28.0 by [@rgbkrk](https://github.com/rgbkrk) in https://github.com/duckdb/duckdb/pull/18446
* Add support for "template" types by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18410
* Internal #5384: WindowDistinctAggregator Sort Update  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18442
* [Chore] Improve skipped tests in test config and add verify_fetch_row config by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18436
* Buffer index appends during WAL replay by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18313
* Add support for generic settings, and move many settings over to generic settings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18447
* Internal #5385: WindowMergeSortTree Sort Update by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18461
* Bump postgres to latest main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18464
* Merge ossivalis by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18456
* Internal #5366: WindowDeltaScanner  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18468
* SUM and + Operator for Varints by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18424
* [Fix] Rework transaction logic in commit, rollback and checkpoint paths by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18474
* re-nable extensions in invokeci by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18476
* Internal #5384: Window Sorting Polish by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18484
* Unify `ON CONFLICT` and `MERGE INTO` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18480
* More insights around dict_fsst compression failure by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18475
* Change ctrl-a/ctrl-e to move to start/end of line, not buffer by [@tpot](https://github.com/tpot) in https://github.com/duckdb/duckdb/pull/18490
* add delta linux back to ci by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18491
* Fix accidental internal exception in type transformation by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18492
* [Profiling] Add client context into read functions by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/18438
* julia: config improvements by [@aplavin](https://github.com/aplavin) in https://github.com/duckdb/duckdb/pull/17585
* fix: add missing space in AttachInfo::ToString() by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18500
* Merge ossivalis by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18502
* Change UNICODE to UTF8 by [@sheldonrobinson](https://github.com/sheldonrobinson) in https://github.com/duckdb/duckdb/pull/17586
* Fix: Remove overly strict assertion on empty string value by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18504
* Fix several bugs/fuzzer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18503
* Allow expressions to be used in ATTACH / COPY options by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18515
* Remove `immediate_transaction_mode` from DB config options by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/18516
* Temporarily excluding `Build Pyodide wheel` for Python 3.11 because it fails to build `WASM` wheels  by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18508
* ParserException for Pragma with named parameters by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18506
* Add verify fetch row config to Main.yml by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18478
* Adding WITH ORDINALITY to DuckDB by [@niykko](https://github.com/niykko) in https://github.com/duckdb/duckdb/pull/16581
* When tracking evicted_data_per_tag, track actual size on disk after temp file compression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18521
* Fix: Write the salt together with the HT offset when determining the value for key comparison by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/18374
* Fix incorrect character encoding in GetLastErrorAsString on Windows by [@soutong](https://github.com/soutong) in https://github.com/duckdb/duckdb/pull/18431
* Dynamically determine dictionary size limit in Parquet writer (if unset) by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18356
* Internal #16560: Numeric TRUNC Precision by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18511
* Consistently detect JSON schema indepent of number of threads by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18522
* ALP test: skip TPC-DS 67 - it is not consistent with floating point numbers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18528
* [Varint] Negation, Subtraction and Over/under-flow checking by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18477
* fix: support both field orders for variant struct by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18532
* Add CAPI to retrieve client context for table functions by [@VGSML](https://github.com/VGSML) in https://github.com/duckdb/duckdb/pull/18520
* Add `StatementVerifier` for `EXPLAIN` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18529
* Use global index, not local id when creating filters in `MultiFileColumnMapper` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18537
* Add support for explicit clean-up routine in test config, and exit multi-statement execution when an error is encountered by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18539
* fix: improve handling variant nulls and nested types by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18538
* Allow overriding openssl version for FIPS compliance by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/18499
* Unittester: Add the `--sort-style` parameter that allows a fallback comparison where results are sorted according to a given sort-style by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18542
* Restore missing `test/configs/small_block_size.json` file by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18507
* [Fix] Follow-up PR to only delete unique row IDs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18545
* [ART] Node::Free refactoring by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18544
* Implement special-case `VARCHAR` to `JSON[]` casts and vice versa by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18541
* Check if `heap_block_ids` is empty before getting start/end when destroying chunks in `TupleDataCollection` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18556
* optimize/parquet: generate movable types for parquet by [@mapleFU](https://github.com/mapleFU) in https://github.com/duckdb/duckdb/pull/18510
* [easy] [no-op] Minor optimization on iterator lookup by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/15349
* Fixing compilation with -std=cpp23 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18557
* Add compile option standalone-debug for clang by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/17433
* Rename the Varint type to Bignum by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18547
* [Indexes] Buffer-managed indexes part 3: segment handle for Node48 and Node256 by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18567
* fix: add formatting to explain row counts by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18566
* [CSV Sniffer] Fixing bug of not properly setting skipped rows from sniffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18555
* [Fix] Tidy check ossivalis by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18583
* [Fix] Adjust shrink threshold back to original count > SHRINK_THRESHOLD by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18582
* Flip left/right delim join based on cardinalities by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18552
* fix: use thousands separator and decimal for row counts in`duckbox` output format by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18564
* Force `LIST`/`ARRAY` child vectors on a Parquet single page by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18578
* String dictionary hash cache by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18580
* fix: libduckdb.so missing soversion by [@strophy](https://github.com/strophy) in https://github.com/duckdb/duckdb/pull/18305
* Pushdown filters on coalesced outer join keys compared for equality under the join condition by [@matteobilardi](https://github.com/matteobilardi) in https://github.com/duckdb/duckdb/pull/18169
* Adds a function for updating and adding values in a struct by [@teaguesterling](https://github.com/teaguesterling) in https://github.com/duckdb/duckdb/pull/15533
* fix hidden merge conflict by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18589
* Increment storage version to enable `DICT_FSST` in benchmark file by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18588
* [Fix] Hidden test failure in test_struct_update.test by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18598
* correctly setting log transaction id in ThreadContext by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/18536
* Backport renaming a config name `small_block_size.json` to `block_size_16kB` in NightlyTests by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18581
* Update README.md by [@matthew-wright07](https://github.com/matthew-wright07) in https://github.com/duckdb/duckdb/pull/18614
* [Test] Fix test case and a benchmark by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18610
* [CI] Don't zip and upload Code Coverage tests results when Code Coverage got cancelled by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18607
* [Profiling] Add client context into more read functions by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/18514
* bump httpfs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18591
* Fix serialization backwards compatability for varargs functions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18596
* Issue #18631: Streaming Windowed Quantile by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18636
* parquet/parquet_multi_file_info.cpp: fix move from stack by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18634
* Adjust filter pushdown to latest polars release by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18624
* Re-add `hugeint` to `__internal_compress_string` by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/18622
* Add Field IDS to multi file reader for positional deletes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18617
* [CSV Sniffer] Fix type detection issue with union and empty columns by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18606
* [ART] ART::Erase refactoring by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18595
* wrap httplib ::max() call in `WIN_32` check by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18590
* Add enable verification config run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18467
* feat: add ETA to progress bar in DuckDB CLI by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18575
* Add "Hash Zero" verification CI run by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18623
* Make more configs into generic settings by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/18592
* bump avro to v1.4 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18434
* bump spatial (on main) by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18197
* Change arrow() to export record batch reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18642
* [Fix] Prevent logger deadlock by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18637
* Remove `PRAGMA enable_verification` by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18645
* Add 1.4 release codename by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18652
* Python test runner: Fix result check for `COPY ... RETURN_STATS` queries by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/18625
* Merge ossivalis into main by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18644
* CLI: Make ETA more of an estimate, and support large_row_rendering for footers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18656
* Remove more `PRAGMA enable_verification` by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18664
* [CI] skip building encodings extension in InvokeCI by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18655
* Python test runner: Fix hash comparison error output by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/18626
* [Dev] Add script to create patch from changes in an extension repository by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18620
* Correctly set weights in reservoir sample when switch to slow sampling by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/18563
* Internal #5366: Window Interrupt Arguments by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18651
* Remove `PRAGMA enable_verification` in more tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18670
* [ Python SQLLogic Tester ] Add `MERGE_INTO` to `statement.type` enum in `result.py` by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18675
* Load pandas in import cache before binding by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18658
* Internal #5662: IEJoin Test Plans by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18680
* Correctly allocate uncompressed string data in ZSTD for many giant strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18678
* Grab lock and double-check that column is not loaded in MoveToCollection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18677
* fix error message related to wrong memory unit by [@LiranBri](https://github.com/LiranBri) in https://github.com/duckdb/duckdb/pull/18671
* [CI] Temporarily skip triggering `R Package Windows (Extensions)` job by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18628
* Fix the issue where delta_for isn't used in bitpacking when for is unavailable by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/18616
* Add `date_trunc()` simplification rules by [@rcurtin](https://github.com/rcurtin) in https://github.com/duckdb/duckdb/pull/18457
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/14213
* Internal #5366: Window State Arguments  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18676
* Add WAL test config run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18683
* Using a different workflow to release the python package by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18685
* Make sure parse errors are wrapped in ErrorData by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18682
* [Python SQLLogicTest] Add `test/sql/pragma/profiling/test_profiling_all.test` to the SKIPPED_TESTS set by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18689
* Issue #18457: DateTrunc Simplification Warnings by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18687
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18695
* Hold row group lock for entire call of MoveToCollection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18694
* Unplug python (in ossivalis) by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18699
* Correctly handle collations for IN (subquery) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18698
* Move attached databases from a CatalogSet to a dedicated map of shared pointers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18693
* Make ART construction iterative via ARTBuilder by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18702
* [Fix] Correctly handle table and index chunks in WAL replay buffering by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18700
* Python-style positional/named arguments for macro's by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18684
* Internal #3273: Hashed Sort States by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18690
* Add Option to Allocate Using an Arena in `string_t` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17992
* Fix issue with materialized CTE optimization in flatten_dependent_join by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/18714
* [Profiling] Add Profiling to Read Function by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/18661
* Correctly throw an error when too few columns are supplied in MERGE INTO INSERT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18715
* Improved grammar generation script by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/18716
* #Fix 18558: add row_group scan fast path by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/18686
* Added support for blob<->uuid conversions by [@dioptre](https://github.com/dioptre) in https://github.com/duckdb/duckdb/pull/18027
* Minor fixes for other catalogs - mostly checking `IsDuckTable()` for unsupported operations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18720
* Fix PIVOT in multiple statements by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18729
* Internal #5669: Loop Join Thresholds by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18733
* feat: enhance .tables command with schema disambiguation and filtering by [@shivampr](https://github.com/shivampr) in https://github.com/duckdb/duckdb/pull/18641
* Add (CSV) file logger by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17692
* Use 1-based indexing for SQL-based JSON array extraction by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18735
* [unittest] SkipLoggingSameError() to make unittester report one failure per case by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18270
* fix timetravel for default tables by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18240
* [C API] Function to set a copy callback for bind data by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18739
* Secrets: if serialization_type is not specified, assume it's a key value secret by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18743
* Merge ossivalis into main by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18719
* Use correct type for pushing collations in subqueries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18744
* Add OS X notarization for DuckDB CLI and libduckdb.dylib by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18747
* Add missing expected errors to the test cases by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18746
* removed placeholder client directories for node and jdbc, its been > 1 yr by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18757
* Append using a SQL query, instead of directly appending to a base table, and support user-provided queries through the QueryAppender by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18738
* Backport #18374 to `v1.3-ossivalis` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18752
* Add leak suppressions to nightly runs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18748
* Remove separate WAL encryption flag by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18750
* Fixing lazy polars execution on query result by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18749
* [Profiling] Add Profiling to Write Function by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/18724
* Extensions.yml should also check converted_to_draft by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18754
* Minor logging fixes and more benchmarking by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18755
* Add missing expected errors to the test cases (next chunk) by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18753
* Refactor read_blob and read_text to use MultiFileFunction. by [@xevix](https://github.com/xevix) in https://github.com/duckdb/duckdb/pull/18706
* Add support for auto-globbing within a directory: if no matches are found for a specific path, we retry with `/**/*.[ext]` appended by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18760
* Fix radix partitioning with more than 10 bits by [@ctsk](https://github.com/ctsk) in https://github.com/duckdb/duckdb/pull/18761
* Fix index resolution when querying table with index via view by [@mach-kernel](https://github.com/mach-kernel) in https://github.com/duckdb/duckdb/pull/18319
* Fix Path Typo in Extension's CMake Warning Message by [@beryllw](https://github.com/beryllw) in https://github.com/duckdb/duckdb/pull/18766
* Make `duckdb_log` return a TIMESTAMP_TZ by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18768
* Revert "Use 1-based indexing for SQL-based JSON array extraction" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18758
* [CI] Adjust test configs post logger PR by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18771
* [Test Fix] Forward output to file by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18772
* Propagate `DUCKDB_*_VERSION` in extensions and tests by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/18774
* Add `file_size_bytes` (de-)serialization by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18775
* Use microsecond resolution for printing the current timestamp by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18776
* Improve error messages for merge / vector reference by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18777
* Move row id logic to separate RowIdColumnData class instead of inlining it into the RowGroup by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18780
* Treat ENABLE_EXTENSION_AUTOINSTALL as the BOOL that it is by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18778
* Add `memory_limit` parameter to `benchmark_runner`/`test_runner.py` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18790
* fix: improve speed of GetValue() for STRUCT type by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18785
* Internal #3273: Parallel Window Masks by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18731
* Task Scheduler: track exact task count, and re-signal on dequeue failure if there are tasks left by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18792
* fix: coalesce query progress updates to reduce terminal writes by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18672
* Support expressions as COPY file target by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18795
* Remove everything python-package related by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18789
* Improve autocomplete suggestions by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/18773
* bump httpfs so it includes curl option by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18691
* Issue #18767: Ignore Timestamp Offsets by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18794
* Fixup progress_bar: avoid converting doubles into int32_t unchecked by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18800
* [chore] Fixup tidy-check on src/logging/log_manager.cpp by passing const & by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18801
* Internal #3273: Hashed Sort Callbacks by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18796
* Typed macro parameters by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18786
* Fix some unindented interactions between `EMPTY_RESULT_PULLUP` and `MATERIALIZED` CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/18805
* Add support for non-aggregate window functions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18788
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18810
* Test runner: Expand '{UUID}' into a random UUID by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18809
* Provide failing file name in Parquet reader error messages by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18814
* [CI] install  libcurl4-openssl-dev with apt-get by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18811
* fix: Add COLLATE NOCASE support to strpos function by [@shivampr](https://github.com/shivampr) in https://github.com/duckdb/duckdb/pull/18819
* Add callback to get a list of copy options, use this to provide suggestions and to erase options from import that are only used during exporting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18812
* For BC reasons - keep VARINT as alias for BIGNUM by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18821
* [Fix] Bug in fixed-size buffer when throwing out-of-memory by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18769
* Re-add accidentally removed check if copy_from is supported by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18824
* Fix format-fix runs on Linux by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/18827
* Extensions.yml: Pass down save_cache to inner workflows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18828
* Fix: Preserve database configuration flags for tab completion in DuckDB shell by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18482
* Ensure a WAL file matches the DB file and checkpoint iteration by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18823
* fix: sanitize input for enable_logging by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18830
* fix: silence warnings about signed/unsigned conversions. by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18835
* Avoid expensive checkpoints and write amplification by appending row groups, and limiting vacuum operations for the last number of row groups by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18829
* Fix/run function in transaction by [@Evannnnnnnn](https://github.com/Evannnnnnnn) in https://github.com/duckdb/duckdb/pull/18741
* add appender to concurrent test by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18721
* Add support for reading/writing native parquet geometry types by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18832
* Don't notify Py pkg when override git describe is set by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18843
* Avoid printing '99 hours', given in most cases that means estimate is… by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18839
* Add the `VARIANT` LogicalType by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18609
* Document storage version flag in CLI + minor rendering fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18841
* Ignore null verification for statistics on structs by [@d-justen](https://github.com/d-justen) in https://github.com/duckdb/duckdb/pull/18813
* Add OnBeginExtensionLoad callback by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18842
* Bump MySQL/Postgres/SQLite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18848
* Merge ossivalis into main by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18844
* Add test_env to unit tester by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18847
* WAL <> DB File Match Fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18849
* Make ATTACH OR REPLACE atomic, keep list of used databases in MetaTransaction by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18850
* Fix `NULL` path for `json_each`/`json_tree` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18852
* No more `wal_encryption` flag by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/18851
* Bump Ducklake by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18825
* Add more encryption modes CTR and CBC by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18619
* Centralize attached database paths in a DatabaseFilePathManager which is shared across databases created through the same DBInstanceCache by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18857
* Hold segment lock during GetColumnSegmentInfo by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18859
* update duckdb azure extension ref for 1.4.0 by [@benfleis](https://github.com/benfleis) in https://github.com/duckdb/duckdb/pull/18868
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18864
* Add a FORCE_DEBUG flag to force `-DDEBUG`, similar to FORCE_ASSERT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18872
* Bump & remove patches for delta, avro, excel, encodings, fts  by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18869
* [minor] Incompatible DB error message: add newline by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18861
* Bump mbedtls to v3.6.4 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18871
* Storage fuzzing + several fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18876
* Update ducdkb iceberg hash by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18873
* [Test] Small fixes to concurrent attach/detach test by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18862
* Internal #5796: Window Progress by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18860
* Add `COPY (...) TO ... (FORMAT BLOB)` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18840
* Update spatial+vss+sqlsmith in preparation for v1.4 by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18882
* Avoid automatically checkpointing if the database instance has been invalidated by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18881
* Add `COPY (FORMAT BLOB)` to Andium too :^) by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18884
* [C API] Result schema of prepared statements by [@hrl20](https://github.com/hrl20) in https://github.com/duckdb/duckdb/pull/18779
* Json: no reinterpret<size_t*> by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18886
* [Dev] Fix footgun in `string_t::SetSizeAndFinalize` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18885
* [chore] Bump config test/configs/compressed_in_memory.json to new format by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18888
* bump aws and iceberg by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18889
* Add rowsort to upsert_default.test by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/18890
* fixing auto-specifying ciphers and remove double storage by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18891
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18892
* Keep base data scan state alive in ColumnData::Update call by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18893
* Add callback for when an extension fails to load, and also log this by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18894
* Encryption now encoded as a bit, centralizing in set/getter by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18897
* Bump httpfs to v1.4-andium branch by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18898
* fix: refine query ETA display and Kalman filter stability by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18880
* Bump inet & aws by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18899
* [chore] Fix amalgamation build in progress_bar by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18910
* Cannot create table from variant yet by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18912
* In VerifyZeroReaders, get the header size from the buffer we are replacing instead of from the block manager by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18909
* Fix #18152: avoid auto-detecting hive partitioning with COPY .. FROM by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18911
* CLI: Correctly move to start of line by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18920
* Strip question mark parameters from default temporary directory by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18915
* Move Hash Zero CI run to nightly by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18925
* Bump Iceberg by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18917
* Issue template: Add the Python repository by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18928
* fix extension size increase by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18923
* [Dev] Fix reference of uninitialized memory in Variant conversion first pass by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18921
* Bump DuckLake to Latest Main by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18926
* Make row-group metadata re-use experimental for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18922
* Fix exception propagation in C API  by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/18924
* Bump httpfs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18930
* Bump ducklake and don't write empty bbox in geoparquet stats by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18936
* [PROFILING] Fix EXPLAIN ANALYZE returning empty results when PRAGMA enabled_profiling = 'no_output' by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/18935
* Http_util can return success for all [200, 300) responses, as well as redirects by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18940
* Fix TransformStringToLogicalType for enums arrays by [@tdoehmen](https://github.com/tdoehmen) in https://github.com/duckdb/duckdb/pull/18941
* [unittester] Allow overriding data/ folder to custom location by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18929
* Unpin fixed-size sorting keys by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18945
* Add missing parameters to `COPY ... (FORMAT JSON)` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18946
* Fixes for encrypted database, make cross-engine encryption work, and expand testing by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/18951
* fix windows linking issue ducklake by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18953
* bump iceberg by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18957
* [SQLLogicTest] Detect errors thrown in `LoadExtension` of the `require` statement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/18950
* Don't use `VectorOperations::Copy` for string dictionary hashes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18949
* Fix error reporting in SSLClient by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/18958
* bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18961
* Allow extensions to customize ATTACH OR REPLACE conflict behavior by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/18962
* Unify test runner keyword replacement, and don't run `LOAD [ext]` by default by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18963
* [chore] Bump httpfs and remove patches by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18965
* Correctly update row group data pointers and root table pointer after checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18966
* Attach: Cleanup duplicate data path handling, and make IF NOT EXISTS no longer abort if we are adding a path with the same name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18974
* Bump DuckLake and HTTPFS by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18975
* Issue #18971: Empty Unsorted Windows by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18976
* Check context.interrupted flag in table scan by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18981
* Only return cgroup memory limit if it's a sane value by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/18668
* Macro fixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18992
* ATTACH IF NOT EXISTS - wait until database is fully attached before returning by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18993
* WALReplay Fix: In UpdateColumn, no longer assume all updates are part of the same vector, but instead verify this and batch updates per vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18999
* Bump iceberg by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/19001

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.3.2...v1.4.0

---

# v1.3.2 - v1.3.2 Bugfix Release <a id="v132"></a>

*Released on 2025-07-08*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.3.2)

This is a bug fix release for various issues discovered after we released 1.3.1. There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9 can be read by this version.

## What's Changed
* bump julia to v1.3.1 by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17966
* [CI] adding DONT_LINK parameter to the test extension configuration for `inet` extension by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17967
* Eviction queue: Sort purged nodes and bulk re-add by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17913
* Grab lock before finalizing dynamic filters by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17964
* Issue #5144: AsOf Join Threshold by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17978
* Fix for IsDenseRange check in filter_combiner by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17988
* Use SharedLockTable in DataTable::Fetch by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17983
* On Windows CI use zip from msys2 instead of choco by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17993
* [FIX] Arrow ArrowBool8 Extension Type Add Validity Type Check by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/18005
* Make test more lenient by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18022
* Print internal exception stack traces on failed transaction rollback  by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18023
* More fixes around GetDatabases by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18024
* [Fix] Binding error when resolving lambdas with a struct alias by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18014
* Disable constexpr std::mutex on Windows by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17991
* Use correct expression function after filter pushdown by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17860
* Implement bulk enqueue for non-concurrent queue by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18032
* Bring back libduckdb-src.zip as release artifact by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/18019
* Issue #18035: Zero Fill TIMESTAMP_NS by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18045
* Fix handling dynamic table filters in RemoveUnusedColumns by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/18033
* Fix incorrect results in index scan by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18058
* bump spatial (v1.3) by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18059
* constant or null can be replaced when argument is a bound column reg by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18018
* Issue #18047: TIMESTAMP_TZ Upcast Costs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18064
* Properly handle empty RHS in IE Join by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18067
* Avoid going too in-depth while computing join order by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17904
* Main.yml: Move very long job from debug to release with `-DDEBUG` and `FORCE_ASSERT` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18081
* Run Python workflow against both Python 3.9 and 3.13 on PR to ensure … by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/18080
* fix statistics propagation for anti-joins on empty tables by [@bradynwalsh](https://github.com/bradynwalsh) in https://github.com/duckdb/duckdb/pull/17439
* OSX.yml: Move from using debug builds to release + DDEBUG + FORCE_ASSERT by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18102
* Fix copy constructor in SetVariableStatement by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/18101
* [Parquet] Add write_bloom_filter flag to allow disabling of bloom filters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/18093
* Add Stack Trace marker to stack trace by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/18089
* Add missing `INT128` to decimal Parquet reader switch by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18104
* shared_ptr<HTTPUtil>& must be reached from FileOpener by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18107
* Cleanup on correct branch (1.3-ossivalis) instead of v1.2-histrionicus by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18111
* Refactor extracting expressions for dynamic index scans by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18095
* Add v1.3.2 to version_map.json and generate storage_info.cpp by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/18112
* CI: Actually correctly skip building unnecessary extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18119
* Absorb patch from https://github.com/duckdb/duckdb/pull/18107 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18114
* Use _unsigned_ hugeint for compressed materialization strings by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/18128
* Throw internal exception on corrupted roaring bitmap offsets by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18130
* Allow .tsv as an accepted db file by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18133
* Fixing CSV Fuzzer issues by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18134
* Bump iceberg for 1.3.2, from [@Tishj](https://github.com/Tishj), and bumping also httpfs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18148
* Internal #5245: AsOf NLJ Comparisons by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/18159
* Add internal exceptions to compression paths to prevent segmentation violations by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/18151
* Fix for arrow.json production extension type by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/18132
* partially restore deprecated http logging settings by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/18150
* Bump for wasm fixes (excel and httpfs) and test fixes (iceberg) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18167
* bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/18161
* Bump sqlsmith and aws by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/18155
* bump ducklake for v1.3.2. by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/18156
* Bump spatial again: include re-linking for handling global objects in Wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/18170

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.3.1...v1.3.2

---

# v1.3.1 - v1.3.1 Bugfix Release <a id="v131"></a>

*Released on 2025-06-16*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.3.1)

This is a bug fix release for various issues discovered after we released 1.3.0 "Ossivalis". There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9 can be read by this version.

## What's Changed
* MultiFileReader: Fix for handling nested list/map default values by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17589
* Signed to Unsigned is not reversible by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17571
* [Dev][CLI] Use an unused bit for `DUCKDB_LATEST_STORAGE_VERSION` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17598
* minor restructure MAIN_BRANCH_VERSIONING by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17601
* Main branch versioning set to false by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17602
* Generate correct UUID v7 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17612
* Issue #17606: Disable TIMESTAMPTZ Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17614
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17543
* Improve Windows lock conflict error by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17622
* Actually initialize in batch copy to file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17627
* Issue #17621: Streaming Window Reset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17649
* CLI: Print codename for '-version' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17637
* [Python][Dev] Ignore `DYNAMIC_FILTER` TableFilters in filter pushdown by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17657
* [Dev] Throw if `db` is not available yet in setting certain configuration options by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17659
* chore: Fix initialization by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/17643
* chore: Fix initialization by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/17644
* DefaultSecretGenerator: require lock for modifying persistent_secrets by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17650
* initialize the read with the OpenFile info and not just the path by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17652
* Don't bail on TopN optimization if we don't have a cardinality by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17654
* Fixes for CSV fuzzer tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17678
* chore: Fix strict aliasing warning on GCC by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/17641
* Partitioned copy: don't check if file exists for remote files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17689
* Fix version detection for sdist builds without git info by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/17605
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17695
* Do not get file handle unnecessarily.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17698
* Allow table functions to disable statement caching by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17702
* [SQLLogicTester] Replace keywords in `<FILE>:pattern` result for the `query` statement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17710
* Parquet Reader: only read strings as fixed length strings if the type is FIXED_LEN_BYTE_ARRAY by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17723
* Internal #5022: IN Pushdown Equalities by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17731
* Internal #4995: Commutative INTERVAL Multiply by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17730
* Issue #17725: Quantile NaN Compare by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17761
* Backport CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17763
* Have the skip_rows option consider empty csv lines by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17756
* Fix wrong assertion in Parquet DBP encoder by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17746
* CLI: make -f always bail on error by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17768
* Don't Flatten() then Reference() by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/17769
* [Dev] Fix `TRY` expression crash on literals by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17753
* Pop up ICU errors to the csv sniffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17719
* [Nested] Fix incorrect type casting in list_reduce lambda expressions by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17581
* [chore] Avoid caching msys artifacts on PRs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17777
* Skip encodings and spatial extensions on PRs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17775
* Add `FileBufferType::EXTERNAL_FILE` and add to same queue as `FileBufferType::BLOCK` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17771
* Storge the argument and value of arg_min_max in the state as a unique_ptr by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17749
* Physical operator logging by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17752
* Take string size into account in `GetRowSize` in `ParquetWriter` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17793
* [CSV Sniffer] Consider if null_padding is set to true when detecting midcomment line during sniffing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17751
* Revert "Avoid early-out when catalog lookup fails - instead finish all look-ups" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17805
* Support file rotation with WRITE_EMPTY_FILE false by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17804
* Check page filtered out flag before reading it by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/17786
* Avoid saving ccache on pull_requests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17810
* Support glibc 2.28 environments in 1.3.x by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17814
* arrow_output_version option to produce arrow depending on a format version. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17791
* Internal #5069: Win32 Cast Simplification by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17820
* local_agnostic::isspace to avoid spaces be depending on locale by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17808
* MultiFileReader: Make column mapping mode configurable per-file, instead of requiring it to be set globally by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17817
* Fixup confict by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17831
* [Fix] Throw serialisation error when encountering invalid row IDs in WAL delete by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17832
* `remap_struct`: Correctly reserve list vectors to deal with remapping larger-than-vector-size lists/maps by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17836
* Fixup `unique_ptr<T[], deleter>`, now with working custom deleters by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17840
* Fix ICE with Windows ARM64 (1.3) by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17846
* [Fix] WAL replay catalog error in AddForeignKeyConstraint by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17830
* Add ducklake sha by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17818
* add ducklake to internal_extensions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17811
* Use boolean operators instead of bitwise operators for (`u`)`hugeint` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17862
* Bump httpfs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17863
* Function Serialization: adapt to removal of overloads by explicitly casting if argument types have changed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17867
* Add FinalizeLoad callback to catalogs, which can be called after the database is fully instantiated by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17868
* Set query location for interval constants in all cases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17876
* Add support for `option.scheduler_process_partial` to the Executor  by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/17877
* Add array indices to nested paths in `json_each`/`json_tree` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17878
* Add urllib3 dependency and improve fixture download reliability by [@evertlammerts](https://github.com/evertlammerts) in https://github.com/duckdb/duckdb/pull/17880
* Add option to control parquet NaN pruning by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17883
* Issue #17781: ASOF Predicate Binding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17889
* `duckdb_base_std::` plus compile time test on discontinued functions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17866
* Early-out on catalog errors to prevent GetDatabases by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17865
* Fix mismatch between idx_t (64 bits) and size_t (implementation dependent) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17898
* Skipping failing on OSX Release part by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17899
* [Fix] Serialisation error for invalid block ID in index deserialization by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17900
* Update `MemoryTag` when converting block to persistent by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17893
* Add support for deserializing multiple json-serialized statements by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17902
* Deprecated std::stringstream by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17894
* Bump extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17905
* http_log.test: solve non-determinism at the test level by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17914
* Fixup https://github.com/duckdb/duckdb/pull/17775, correct boolean logic by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17912
* Make sure distance is always an int when doing version bumps in setup.py by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17918
* bump azure, aws and httpfs by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17919
* bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17920
* Add v1.3.1 to version_map.json by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/17922
* Bump Avro and Iceberg + fix by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17930
* Bump `Avro` and `Iceberg` in `out_of_tree_extensions.cmake` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17923
* Enable Test extension (inside docker) step in build_extensions_dockerized by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17916
* [chore] Skip 2 tests in autoloading mode (parquet + ZSTD) plus improve error message by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17935
* [tpcds] dsdgen currently assumes DuckTable, throw if that's not the case by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17934

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.3.0...v1.3.1

---

# v1.3.0 - DuckDB 1.3.0 "Ossivalis"  <a id="v130"></a>

*Released on 2025-05-21*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.3.0)

This release of DuckDB is named "Ossivalis" after Bucephala Ossivalis, an ancestor of the [Goldeneye duck](https://en.wikipedia.org/wiki/Common_goldeneye) that lived Millions of years ago.

Please also refer to the announcement blog post: https://duckdb.org/2025/05/21/announcing-duckdb-130

## What's Changed
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16070
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16072
* unittests: clear test directory after every test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16053
* Benchmark runner: catch and log errors + add support for `retry load N` syntax by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16054
* Throw an error when unsupported commands are used in concurrentloop by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16009
* Remove extension definitions to prevent re-compilation of the entire system on commit by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15955
* Display schema information of currently selected database only by [@ashwaniYDV](https://github.com/ashwaniYDV) in https://github.com/duckdb/duckdb/pull/15815
* Issue #14366: Average Intervals  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15864
* Internal #2176: Temporal AVG by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15661
* discussions #15981: remove confusing comment in "duckdb/tools/shell/shell.cpp" by [@komainu8](https://github.com/komainu8) in https://github.com/duckdb/duckdb/pull/15984
* Fix #15466 Transform LIMIT or OFFSET first based on order specified in prepared statement by [@ashwaniYDV](https://github.com/ashwaniYDV) in https://github.com/duckdb/duckdb/pull/15484
* Bitpacking mode info by [@arjenpdevries](https://github.com/arjenpdevries) in https://github.com/duckdb/duckdb/pull/15623
* Sniff Timestamp_TZ from CSV FIles by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15730
* [no-op] Add documentation for filesystem read behavior by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/15937
* Accept "Auto" as date/timestamp format by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15808
* Parquet Reader Cleanup: Move ColumnReaders to separate files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16092
* Parquet Reader: Move decoding logic into separate Decoder classes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16100
* BundleStaticLibs to be also triggered by InvokeCI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16107
* Parquet Reader: Split DeltaLengthByteArray decoder from DeltaByteArray, and read the strings in a streaming manner by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16105
* Parquet Dictionary reader: set NULL values as the last value in the dictionary by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16106
* Parquet Reader: Share ResizeableBuffers across decoders, and unify Plain/PlainReference by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16113
* Using GitHub ARM runners for Linux CLI builds by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16119
* Parquet Reader: Implement dedicated Skip method by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16117
* Use ColumnSegment::FilterSelection and SelectionVector for filtering in Parquet scans by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16126
* [Dev] Fix output (long lines > 333 characters) getting truncated in shell by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16128
* Adaptive table filter: initialize filter order based on heuristics by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16127
* Feature #16044: TimeZone Offset Seconds by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16048
* ATTACH OR REPLACE database to allow swapping of new data. by [@xevix](https://github.com/xevix) in https://github.com/duckdb/duckdb/pull/15355
* [Dev] Remove `upsert_conflict_in_different_chunk.test` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15980
* [Dev] Fix issue related to unpacked columns and the NOT operator by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15534
* [Julia] Add support for named params in prepared statements by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15621
* Use Adaptive Filters in the Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16133
* Parquet reader: push table filters directly into dictionaries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16136
* Parquet reader: Plain templates - make CHECKED a template parameter, and use memcpy/bulk skip when reading/skipping without defines by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16141
* Parquet reader: only set invalid entry in the dictionary when the column has defines by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16144
* Add uniq_ptr_cast for interpreted benchmark. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16151
* Hopefully fixing ci runs by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16150
* Removed the last CI job that used the Ubuntu 18 setup by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16155
* Parquet Reader: Split `CreateReader` into two separate stages - `ParseSchema` and `CreateReader` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16161
* Have CSV Parellel tests on CI again by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16164
* [Python][Dev] Bump the minimum pybind11 version from `2.6` to `2.9` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16159
* Add StackTraces to FatalExceptions by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16158
* Rework invoke by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16108
* Adds pre-optimization hooks for DuckDB by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16115
* Unify behavior of `range`/`generate_series` with PostgreSQL by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/15935
* [CI] Avoid Linux CLI jobs to fail-fast by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16173
* Parquet: Add dedicated Select method that can be used to push selection vectors into the read by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16174
* Unvendor ICU by [@m-kuhn](https://github.com/m-kuhn) in https://github.com/duckdb/duckdb/pull/16176
* Parquet reader: batch check if buffer is available in RLEBpDecoder by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16185
* Parquet Reader: for DeltaLengthByteArray encoding, directly refer to strings from the block without copying by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16186
* unified names for duckdb-extensions by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16179
* Only delete test directory when `--test-temp-dir` is not specified by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16192
* Fix #16163: COLUMNS should not treat identifiers as strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16193
* Parquet reader: Avoid applying bloom filters if we are casting columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16194
* Pretty print sniffer values by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16182
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16191
* Bump Julia by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16199
* Ensure that dependent targets are present after find_package. by [@BillyONeal](https://github.com/BillyONeal) in https://github.com/duckdb/duckdb/pull/16197
* Concurrency groups for R and Wasm by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16201
* Parquet Writer Cleanup: Move ColumnWriters to separate files  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16202
* [fix] Use bigobj when building with MSVC by [@m-kuhn](https://github.com/m-kuhn) in https://github.com/duckdb/duckdb/pull/16200
* Improve performance of `UNNEST/UNPIVOT` by using selection vectors to unnest multiple lists at once by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16210
* Add the `TRY` expression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15939
* [Python][Dev] Replace the default connection when it's closed by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16160
* Use steady clock for profiler by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/16198
* Add parallel memset when building hash join table by [@hehezhou](https://github.com/hehezhou) in https://github.com/duckdb/duckdb/pull/16172
* Avoid unnecessarily projecting the input columns of the UNPIVOT operator in the UNNEST by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16221
* Left join push down optimization by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/15881
* Do In-Filter pushdown in PyArrow by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16224
* Use _win32 with MSVC by [@cfis](https://github.com/cfis) in https://github.com/duckdb/duckdb/pull/16235
* Fix Python 3 executable name on Windows by [@cfis](https://github.com/cfis) in https://github.com/duckdb/duckdb/pull/16236
* Fix -std=c++11 by [@cfis](https://github.com/cfis) in https://github.com/duckdb/duckdb/pull/16237
* Issue #8265: AsOf Nested Loop by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16218
* Include extension_util.hpp in libduckdb by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/16255
* Generalize `rowid` into the concept of virtual columns, and make `filename` a virtual column in the Parquet/CSV/JSON readers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16248
* Modify histogram test to more fuzzily check boundaries since the test can be inconsistent on different platforms by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16261
* [Dev] Fix issue in `TRY` expression with `dictionary_expression` Vector verification by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16262
* [Python Dev] Add the correct variant of the `-std=c++11` flag based on the compiler (MSVC or not) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16267
* Fix extension install mode null by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16268
* A little cleanup. by [@JasonPunyon](https://github.com/JasonPunyon) in https://github.com/duckdb/duckdb/pull/16028
* Improve Parquet writer performance by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16243
* Merge v1.2-histrionicus into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16284
* Many reclaim storage fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15825
* Arena allocator for `MinMaxN` and skip `NULL`s when creating enum by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16246
* Add pragma to truncate duckdb log storage by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16274
* Some more Parquet writer performance improvements by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16287
* Do duckdb_extract_statements to be able to execute pivot in ADBC by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16162
* [Dev] Improve/Add handling of escapes in VARCHAR -> list/struct/map and align behavior by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15944
* make ValidityMask::RowIsValidUnsafe really unsafe by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/16302
* Multi File Reader Rework: Add `MultiFileReaderFunction` that is used to wrap a single-file reader, and use it for the Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16299
* [Python Dev] Add support for fully qualified references in `.table(...)` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16291
* [Dev] MultiFileReader - Add to the `column_indexes` for `file_row_number` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16311
* Parquet reader performance by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16315
* Bump Julia FixedPointDecimals dependency version by [@mbarbar](https://github.com/mbarbar) in https://github.com/duckdb/duckdb/pull/16323
* Merge V1.2 histrionicus into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16324
* Add new recursive semantics (`USING KEY`) by [@cryoEncryp](https://github.com/cryoEncryp) in https://github.com/duckdb/duckdb/pull/12430
* fix: add StringStats::SetMaxStringLength by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/16326
* Fix decorrelation of WITH USING KEY by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/16330
* Issue #16250: Window Range Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16320
* Verify UTF-8 in `DeltaLengthByteArrayDecoder` and speed it up by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16328
* Add missing include by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16342
* [chore] No ccache for OSX Python by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16348
* Linux CLI: override platform for ARM manylinux by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16347
* docs: tweak explanation of median for even cardinality inputs by [@NickCrews](https://github.com/NickCrews) in https://github.com/duckdb/duckdb/pull/13726
* [parquet] Fix implicit idx_t to int64_t conversion flagged by clang-tidy by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16368
* Improve error message on failure to install local extension by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16371
* MAIN_BRANCH_VERSIONING: main branch to get descriptors like v1.3.0-dev1234 instead of v1.2.1-dev1234 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16366
* Parallel HT Zeroing: Set entries_per_task so that there are 4x more tasks than threads by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/16301
* Internal #2176: SUMMARIZE Temporal Types by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16095
* [SwiftRelease CI] fetch tags before checking there is already a tag with the same name by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16376
* Push Select into ArrayColumnData to avoid scanning arrays that are not required for the query by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16356
* Revert "Linux CLI: override platform for ARM manylinux" by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16374
* Rework CSV Reader: use the new MultiFileReaderFunction interface by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16349
* Add connection and transaction identifiers by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16296
* Add parquet 'unknown' logical type by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16378
* Internal #4287: INTERVAL Times DOUBLE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16386
* pb/compressed vector serialization by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/16066
* Fix issue #16377 by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/16391
* Read support for Parquet Float16 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16395
* MAIN_BRANCH_VERSIONING: Adopt also for Python build and amalgamation by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16400
* Fuzzer Fix: Fix Avg for NULL cast to TIMESTAMP by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16394
* [FriendlySQL] Expand functionality of the Unpacked COLUMNS expression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16290
* Python Client: Faster Python Object Conversion by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16431
* Fixup #16400 by correctly passing down SETUPTOOLS_SCM_PRETEND_VERSION by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16435
* Issue #16250: Window Range Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16438
* Merge v1.2-histrionicus into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16439
* MAIN_BRANCH_VERSIONING: Add also prefix_version by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16441
* [no-op] Remove unused function `GetValueRefUnsafe` by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/16440
* Filter Combiner Clean-up: move filter pushdown to separate functions, remove old commented out code by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16443
* [Python] Add the SQLExpression method to the Expression API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16424
* [Dev] Mention the problematic type in UNNEST BinderException by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16429
* Merge v1.2 into main again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16447
* Filter Combiner: Allow rowid pushdown for IN/OR filters and pushdown for temporal types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16450
* Parquet: always launch max threads if we are scanning multiple files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16457
* fix documents of C functions by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/16357
* Add a TableFilterState for execution of table filters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16461
* Mirror discussions to the internal repository by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16464
* Rework JSON Reader: use the new MultiFileReaderFunction interface by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16477
* Speed-up contains by using `memchr` on every iteration by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16484
* Fix error cases by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/16494
* Prevent external joins (if possible) by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16430
* Merge v1.2 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16517
* Optimize FSST decoding by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16508
* Extract subsystem by name by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/16226
* Avoid throwing an exception (that is then swallowed) when computing compressed materialization over stats that are not set by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16532
* Checksum backward compatibility by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16505
* Prefetch Parquet page header by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16507
* Let GitHub render *.test files as SQL by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/16534
* Fix ADBC to properly quote table and schema names by [@CurtHagenlocher](https://github.com/CurtHagenlocher) in https://github.com/duckdb/duckdb/pull/16526
* Pass `ClientContext` to catalog initialize, and postpone index binding when replaying the WAL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16536
* Allow UNITTEST_ROOT_DIRECTORY to be configured through CMake by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16540
* Internal #4347: ISO Year Week by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16567
* throw() -> noexcept in skiplist by [@r-barnes](https://github.com/r-barnes) in https://github.com/duckdb/duckdb/pull/16548
* Fix `test/sql/aggregate/aggregates/histogram_table_function.test` to pass the Linux CLI (arm64) CI by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16538
* feat: move GRANT from reserved to unreserved keyword by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/16546
* Python test runner: Avoid enabling profiling when executing restart command by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/16547
* Add `duckdb_prepared_statements` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16541
* [minor] Keep bit type sanity check consistent by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/16575
* Support CREATE TABLE AS ... WITH NO DATA by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16586
* Parquet FLOAT16 - fix cast by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16580
* remove invalid tokens from nanosecond example by [@hamilton](https://github.com/hamilton) in https://github.com/duckdb/duckdb/pull/16577
* CrossVersion.yml: Add v1.2.1, v1.2-histrionicus and main by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16576
* Fix #16524: DEPENDENT_JOIN may not flatten by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/16537
* [Julia] Add support for appending duckdb List types by [@era127](https://github.com/era127) in https://github.com/duckdb/duckdb/pull/16512
* [PySpark] - Add  `expr` function by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/16468
* regex_replace no longer swallows regex errors by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16380
* Parquet Writer Clean-up: Split `CreateWriterRecursive` into two methods, and use `ParquetColumnData` for writer as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16592
* Bump Julia to 1.2.1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16593
* Improved appender error message by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16599
* Change static variables to be on the stack instead by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/16597
* Add support for `RETURN_STATS` to `COPY` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16595
* Better error messages for the CSV Scanner by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16585
* Support Enum types in read_csv - Python by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15710
* Fix CI Tidy by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16610
* Add some minor helper functions (`QueryResultIterator::IsNull` and casts to MultiFileList/Reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16611
* Add support for `ALTER TABLE tbl SET PARTITIONED BY (key1, key2, ...)` in the grammar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16612
* Issue template: direct UI issues to the UI repository by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16619
* [Dev] Make the various mappings in `MultiFileReaderData` typesafe by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16596
* Bump mbedtls to 3.6.2 and re-apply patches by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16485
* Read and Write Complex Json from Arrow Types by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16385
* Add Docker support for RISC-V CI with appropriate build commands by [@mocusez](https://github.com/mocusez) in https://github.com/duckdb/duckdb/pull/16549
* Fix missing **kwargs in adbc_driver_duckdb.dbapi.connect() by [@davlee1972](https://github.com/davlee1972) in https://github.com/duckdb/duckdb/pull/16637
* [Dev] Clean up and fix the CGroup memory/cpu limit discovery logic by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16608
* Expose `Value::ToSQLString()` in C API  by [@mt-caret](https://github.com/mt-caret) in https://github.com/duckdb/duckdb/pull/16471
* Add the missing binding for json_serialize_sql by [@liznear](https://github.com/liznear) in https://github.com/duckdb/duckdb/pull/16666
* Do not create validity mask for non-null const vector by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/16669
* Fix #16665: fix parquet multi_reader bloom_probe logic error by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/16677
* Add alias to catalog by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/16600
* Decouple physical operator ownership from operators by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16545
* cmake: fix external icu by [@autoantwort](https://github.com/autoantwort) in https://github.com/duckdb/duckdb/pull/16676
* Character length and date functions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16653
* [Dev] Don't try to include `third_party/mbedtls/VERSION` with `package_build.py` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16683
* Add `-ui` to CLI help text by [@akx](https://github.com/akx) in https://github.com/duckdb/duckdb/pull/16626
* Fix alias of column reference lost in ReplaceProjectionBindings by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/16686
* Merge v1.2-histrionicus into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16687
* Fix for GCC-4.8 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16690
* JSON Reader: make read_position atomic so this can be read by the progress bar while processing the JSON file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16692
* [Julia] support binding for vectors by [@slwu89](https://github.com/slwu89) in https://github.com/duckdb/duckdb/pull/16701
* Make CSV Parser strict_mode=True fail on a mix of new line delimiters. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15959
* [pypi] Fix cleanup logic for multiple branches by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16634
* Add support for `ALTER TABLE tbl SET SORTED BY (key1 DESC, key2, ...)` in the grammar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16714
* RETURN_STATS: remove footer_offset, and emit written partition keys by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16715
* In case all rows of a CSV batch are errors, we continue processing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16713
* add workaround for patching httpfs ext by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16722
* Implement UUID v7 by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/15819
* Fix roundtripping of stringified nested types by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16304
* Add Notify External Repositories Workflow by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/16730
* Expose a selection vector and the Slice method to the C API by [@joseph-isaacs](https://github.com/joseph-isaacs) in https://github.com/duckdb/duckdb/pull/16696
* Add support for tracking `column_size_bytes` and `contains_nan` in RETURN_STATS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16731
* Add support for `WRITE_EMPTY_FILE` option to `COPY` - which allows skipping of writing empty files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16737
* Parquet Writer: Truncate string stats for large strings, instead of bailing on writing stats by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16736
* RLE compression - memset alignment bytes to zero when aligning the counts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16735
* Write UUID stats to Parquet files and support reading uuid stats by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16744
* Add an initial value to `list_reduce` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/16602
* shell: make -bail work for more errors by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/16594
* Call Notify External Repositories from Invoke CI by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/16747
* JSON bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16729
* Add support for dynamically providing extra info post-execution in table functions, and use this to emit the total number of files read by the MultiFileReader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16749
* [Python Dev] Fix the versioning of the nightly python builds by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16739
* shell: fix sometimes-uninitialized error by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/16761
* Issue #16250: Window Range Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16765
* Avoid building Python 3.7 wheels also for Linux by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16769
* Pyodide 0.27.2: conditionally skip tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16772
* Push catalog lookups through an extensible EntryLookupInfo struct by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16764
* Fix two minor problems with NotifyExternalRepositories / odbc by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16776
* update expected results reflecting the changes brought ups with `Fix roundtripping of stringified nested types` PR by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16775
* Merge V1.2 -> Main by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16751
* Add support for time travel syntax in the `FROM` clause by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16774
* Python docs: List all join types by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16789
* [chore] NotifyExternalRepositories.yml: Fix endpoint to be pinged by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16793
* Remove delta from extensions built on a nightly basis (vs main branch) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16795
* OSX.yml & Windows.yml: remove repository_dispatch, already handled by InvokeCI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16796
* Make extensions be linked privitally into duckdb by [@JAicewizard](https://github.com/JAicewizard) in https://github.com/duckdb/duckdb/pull/16726
* Add additional iterations to avoid assertion failure in `TemporaryMemoryManager` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16801
* Change the STANDARD_MASK_SIZE calculation to use size of template type. by [@sebastiaan-dev](https://github.com/sebastiaan-dev) in https://github.com/duckdb/duckdb/pull/16807
* Fix nightly table sample error by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16811
* Fix tidy by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16805
* support 'categories' label in function catalog by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/15654
* regenerate function headers by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/16822
* Internal #4490: Window Jump Reset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16816
* Regression.yml: Actually checkout proper base.sha commit by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16824
* fix: drop useless python import by [@yihong0618](https://github.com/yihong0618) in https://github.com/duckdb/duckdb/pull/16808
* NightlyTests.yml: Inline env variables into build command by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16817
* Benchmark runner summary by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16759
* Add storage_version 66 for version 1.3.0 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16800
* Revert "fix: drop useless python import" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16834
* [MultiFileReader] Rework `MultiFileReader::FinalizeChunk` to use Expressions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16630
* Merge v1.2 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16832
* Fix NULL key handling in mark join by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/16825
* compressed vector serialization fixes by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/16648
* really sorry about this by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/16840
* Fix Python docstrings for unique by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16845
* [MultiFileReader] Create "local" filters to hand to underlying readers by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16838
* Revert "Regression.yml: Actually checkout proper base.sha commit" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16860
* [ART] Immediately erase empty fixed-size buffers by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16727
* Resolve defaults and column index map by pushing a Projection (instead of executing in the insert itself) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16867
* Fix issue with sorting dev versions in pypi_cleanup.py script to keep on PyPi the most recent dev versions by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16873
* Allow filters to be pushed through joins if there are projection maps by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16871
* Expressions in create secret by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15801
* Python -  Arrow IPC support in from_arrow by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16821
* [ART] Introduce a new ARTScanner and make InitMerge and Vacuum iterative by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16861
* Do not pushdown filters which bindings only match the right side of the left join by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/16880
* MultiFileReader Rework (part 17) - remove `MultiFileReaderData` - and move as much as possible out of the file readers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16882
* ICU: Unify TimeZone accessing code by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16887
* Rework ICU age computation to convert to a timestamp and use the regular interval age computation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16889
* Reduce allocations during aggregations by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16849
* CI: Prevent marking issues as 'stale' if they have the 'no stale' label by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16903
* Add field name to log line which fails Parquet spec by [@jsbali](https://github.com/jsbali) in https://github.com/duckdb/duckdb/pull/16862
* Internal #4490: Window Threading Cleanup by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16879
* Adding gzip version of shell for linux/osx install script by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16116
* Fix USING KEY reference error by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/16906
* [Nested] Enable Varargs in `LIST_CONCAT` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/16870
* Fix several issues with vsize=2, and move vsize=2 tests to `Main.yml` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16918
* C API comments: Fix a/an typos by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16925
* Reduce locking with `FILE_SIZE_BYTES`/`ROW_GROUPS_PER_FILE` in Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16928
* [Python] Fix annotation of `condition` argument in `join` so it accepts `Expression` by [@MarcoGorelli](https://github.com/MarcoGorelli) in https://github.com/duckdb/duckdb/pull/16933
* Fix GCC 4.8 and add it back to `Main` workflow by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16937
* Merge v1.2 into main again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16939
* MultiFileReader - Perform nested remapping of field indexes instead of relying on casts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16941
* Internal #4552: Short Circuit CSE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16931
* Add back manylinux extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16944
* Run CI on merge group by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16945
* Internal #4516: Interval BIGINT Variants by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16904
* Split query string for multi-statement queries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16955
* Vector Verification: Rework to run based on env variable `DUCKDB_DEBUG_VERIFY_VECTOR` and move to `Main.yml` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16957
* Move the no string inline/alternative verify workflow to Main.yml by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16958
* [Python] Tighten type annotations on ``shape`` and ``columns`` by [@MarcoGorelli](https://github.com/MarcoGorelli) in https://github.com/duckdb/duckdb/pull/16948
* Pass down CMAKE_POLICY_VERSION_MINIMUM and fix for local development by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16953
* [ART] Use the ARTScanner for VerifyAllocations (make it iterative) by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16946
* Move ThreadSanitizer test from nightly test to Main, and fix locking issue by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16960
* Re-enable workflows to run on PRs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16961
* Fix for selecting NaN values from Parquet files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16962
* Move LatestStorage tests to NightlyRelease - and fix issue with overflow string blocks not being cleaned up correctly by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16972
* Arena-allocate physical operators by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16911
* Make `file_row_number` a virtual column, and support per-file virtual columns in the MultiFileReader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16979
* Add a setting `scheduler_process_partial` that allows partial scheduling of tasks in the background threads by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16973
* Clean up format script, gather all files then run concurrently instead of running concurrently per directory by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16988
* Add support for altering struct columns (adding fields, dropping fields, renaming fields) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17003
* Fix CSV fuzzer tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16994
* [Fix] Keep original expression for macro + lambda's with subqueries by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17020
* Detect when tables have been dropped or altered, and prevent deletes in this scenario by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17018
* Update links pointing to duckdb.org by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/16999
* Fix for joining on floating columns #16901 by [@nickzoic](https://github.com/nickzoic) in https://github.com/duckdb/duckdb/pull/16965
* fix: remove ununsed stream struct member from ArrowScanLocalState by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/17023
* [Dev] Use `UnifiedVectorFormat` instead of a flattened `Vector` in `UpdateSegment::Update` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16974
* Remove Arrow Extenson from core extensions by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17027
* Correctly propagate ClientContext to TaskExecutor by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/17026
* Issue #17001: AsOf memory Management by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17028
* [MultiFileReader] Make it possible for the multi file reader to add a `DeleteFilter` to the `BaseFileReader` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17032
* Add optional `OVERRIDE_NEW_DELETE` build parameter by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17035
* Clean-up virtual columns and make MultiFileReader::InitializeReader virtual by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17038
* Allow a table to define their own row-id columns for delete/update, instead of assuming it is always COLUMN_IDENTIFIER_ROW_ID by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17039
* Handle Parquet with compressed empty DataPage v2 by [@EnricoMi](https://github.com/EnricoMi) in https://github.com/duckdb/duckdb/pull/17031
* Combine small row groups in Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17036
* Merge v1.2.2 into main by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17037
* implement function so I can send a patch to httpfs by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17048
* FORCE_ASYNC_SINK_SOURCE: pass also to unittester by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17053
* If a Max Line Size Error happens on all CSV dialect candidates, throw a max line size error. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16935
* Expose BindExtraColumns as a public function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17060
* trigger .github/workflows/NightlyBuildsCheck.yml from external repo by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/16949
* Minor parquet crypto clean-up: allow footer key to be passed in directly, and avoid constantly re-reading the key from the config by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17070
* update julia to v1.2.2 by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17074
* MultiFileReader Rework (part 18): Replace file path with `OpenFileInfo` struct by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17071
* Fix httpfs patches: avoid `git log` since might contain unsanitised `error` word by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17075
* Re-enable Avro on core by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17072
* [Nested] Optimize List Type in `list_value` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17063
* Grow string dictionary dynamically in Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17061
* Add extended file info to OpenFileInfo, and use this to pass encryption keys and footer size to Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17085
* [Dev] Automatically re-execute when calling `__arrow_c_stream__` on an already-consumed-result by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17087
* fsst: Avoid to propagate alignment information in FSST_UNALIGNED_STORE by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17094
* Fix sqlite3 api wrapper link + remove R-CMD-check + add more nightly tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17095
* support large dictionary value and constant vector creation in the C API by [@joseph-isaacs](https://github.com/joseph-isaacs) in https://github.com/duckdb/duckdb/pull/17064
* Add missing lock to UpdateSegment::FetchRow, and cleanup API to require the lock by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17100
* Valgrind requires tpch by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17101
* Switch to manylinux_2_28 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16956
* Changing mbedtls encryption API by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/16196
* Pull OpenFileExtended through the opener and virtual file system layers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17102
* Fix an issue in upserts where the local append state was not correctly flushed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17109
* Always parallelize `read_json` schema detection by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17106
* Move transaction cleanup outside of the transaction lock by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17034
* Remove R_CMD_CHECK.yml, now handled by duckdb/duckdb-r repo by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17127
* JSON Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17119
* Refactor relassert runs, adding some variations in compiler / statically linked extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17104
* extension-upload-from-nightly.sh: Add --region by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17120
* MultiFileReader: several fixes for virtual column handling and make virtual column handling extensible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17123
* Remove misleading lock comment in data table by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17125
* [Dev] Add "registries" to `vcpkg.json`, add script to list the packages of the registry. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17124
* External File Cache by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16463
* Notify nightly build status by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17108
* Strict UUID cast by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17138
* Copy To File: avoid calling Combine for threads that have not written any rows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17142
* Add file_index virtual column to the multi file reader that returns the file index of the read file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17144
* MultiFileReader: simplify constant handling, and allow virtual columns returned by the multi file reader to be constant by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17149
* Changes to encodings to make them more flexible to replacement maps. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17146
* Optimize large Top N queries by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17141
* Only trigger TopN rewrite relatively small limits compared to the table size.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17140
* platform.hpp: Propagate DUCKDB_EXPLICIT_PLATFORM, avoid early return by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17137
* Keeping the filters which do not remove NULL values by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/17045
* Improve `FileSync` call on unix platform by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/16893
* README: Fix to building link by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17161
* [InvokeCI] Add missing pipe to run instruction by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17163
* Internal #4667: 2025b TimeZone Data by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17160
* Unify function list by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/17168
* [Dev] Generate the `EXTENSION_SECRET_TYPES` instead of hardcoding them by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17183
* Fix grouping feature with interval type by [@handstuyennn](https://github.com/handstuyennn) in https://github.com/duckdb/duckdb/pull/17181
* Add filename to GZIP stream error by [@marcoslot](https://github.com/marcoslot) in https://github.com/duckdb/duckdb/pull/17166
* Issue #17115: TimeTZ Approximate Quantile by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17162
* Issue #17046: AsOf Left Predicates  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17159
* [Fix] Pass delete indexes when committing updates by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17176
* Python.yml: Add back logic to perform fast-fail on Python 3.10 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17107
* Notify JDBC repo to run Vendor.yml workflow by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17099
* Issue #17049: ICU Date Cast by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17067
* Add bind_operator callback to TableFunction - allowing table functions to directly emit a LogicalOperator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17196
* [ENCRYPTION] Make block header size adaptive by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17118
* Issue #16839: Disable TIMESTAMP Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16899
* Add support for an explicit PRESERVE_ORDER flag for copy to file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17199
* Add `SYSTEM_PEAK_BUFFER_MANAGER_MEMORY` and `SYSTEM_PEAK_TEMP_DIRECTORY_SIZE` to profiler by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17164
* Fix [InvokeCI / NotifyExternalRepository] Unexpected value 'true' by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17212
* Add support for the cast_to_type function, that allows generating a cast from an expression to the type of another column by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17209
* Better cardinality estimates for inequality joins/grouped aggregations by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17139
* Add `ExternalFileCache` validation as option for `ExtendedOpenFileInfo` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17205
* Explicitly flush the thread-local optimistic writer in `PhysicalBatchInsert` when finalizing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17214
* Pushdown arbitrary expressions into scans by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17213
* Fix #17170: sort selection result in OR expression by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/17180
* [Dev] Re-enable Iceberg, Bump Avro, fix `generate_extension_functions.py` for dependencies between extensions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17204
* Change Invalid Unicode Error to Invalid Encoding by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17208
* Direct IO for temp files by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17219
* Fix [InvokeCI / NotifyExternalRepository] GitHub Actions has encountered an internal error when running your job. by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17218
* Add "thousands" option to CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17220
* add capi functions to create map and union values by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/17227
* Only notify JDBC when all runs are successful by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17233
* Update Friendlier SQL link.md by [@hfrifkin](https://github.com/hfrifkin) in https://github.com/duckdb/duckdb/pull/17248
* Implement reading concatenated GZIP members by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17255
* Return invalid `BufferHandle` upon loading a destroyed `BlockHandle` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17249
* Internal #4772: Timestamp Error Parameter by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17283
* BUGFIX: do not perform unused columns optimization in presence of multiple grouping sets by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17259
* Internal #4532: 13 Month Intervals  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17303
* Dont try to load extension if storage type is already registered by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17241
* Adapt size of hash table during aggregation using HyperLogLog by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17236
* Switch to always using list identifier instead of array by [@J-Meyers](https://github.com/J-Meyers) in https://github.com/duckdb/duckdb/pull/17242
* Add root's query_location also to TransformInterval by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17271
* Histogram table function test by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17276
* Guess Parquet footer size by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17300
* Issue #16563: FLOAT to DECIMAL by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17302
* Feature #15873: Windowed ORDER BYs  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17304
* Switch from Bottom-Up to Top-Down Decorrelation Strategy by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/17294
* Generating random data for mbedtls without key by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17309
* Fix CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17319
* [Arrow] Implement support to consuming and producing Decimal 32 and 64. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17314
* take the column ids from the logical get, don't require a LogicalGet … by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17315
* Allow installing extensions with external access allowlist by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/17316
* Implement ARTMerger replacing the recursive ART merge algorithm by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17243
* Share null mask with constant null arg vector by [@iceTTTT](https://github.com/iceTTTT) in https://github.com/duckdb/duckdb/pull/17234
* Fix #17311: correctly check for presence of recursive keys in transformer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17320
* [CSV Reader] Simplify Quote/Escape detection code, make it more robust and decouple comment and skip_rows option. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17284
* Fix `try_cast` from NaN `double` to `decimal` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17322
* Add serialization for new TableColumn type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17321
* Extract expressions from nested conjunction AND for index scan by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17297
* Support late materialization in the Parquet reader, and handle `COUNT(*)` directly in the multi file reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17325
* Implement ARTOperator replacing Lookup and the recursive Insert by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17327
* Internal #4723: Inequality Condition Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17317
* Properly format strings when throw JSON errors by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17331
* Fix potential vulnerable cloned function by [@npt-1707](https://github.com/npt-1707) in https://github.com/duckdb/duckdb/pull/17340
* Fix potential vulnerable cloned function by [@npt-1707](https://github.com/npt-1707) in https://github.com/duckdb/duckdb/pull/17339
* Revert "Skip MinGW, currently failing on main" by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17342
* Unify Parquet Metadata cache invalidation logic with Cached File System cache invalidation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17334
* Fix issue with empty ranges by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/17332
* Internal #4797: Timestamp Range Cardinality by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17330
* Some nitpicking fixes by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17337
* Issue #17299: Integer Rounding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17328
* Parquet Reader: emit partition stats for any files that have cached metadata, and implement `ListFilesExtended` that adds extra info to files globbed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17344
* Add support for UUID v7 to Filename Pattern - and clean it up so that it correctly supports composite patterns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17345
* Add support for the HIVE_FILE_PATTERN option - that allows partitioned files to be written without writing them to a hive-style directory structure by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17346
* Add an OnDetach callback to the catalog that is triggered when the user detaches a catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17347
* Pass commit ID to NotifyExternalRepositories.yml by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17333
* Add support for BENCHMARK_ROOT_DIRECTORY cmake option to change benchmark runner root directory, and add support for cache_file and reload options to enable better caching for non-DuckDB databases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17355
* Support --directories option in format.py by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17354
* Handle both ENCRYPTION_KEY and STORAGE_VERSION passed as options by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17357
* Fix internal exception from assigning invalid index to `optional_idx query_id;` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17359
* Fixup amalgamation: reqlen is only used with assert enabled by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17361
* md5_number: return UHUGEINT by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17336
* Skip emitting partition stats if "has_deletes" is set in the file info by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17365
* Benchmark runner: add `argument`, `include` and `load_only` options - and make ClickBench run the original benchmark instead of a subset by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17367
* Fix two off-by-one errors in row estimate of range and generate_series by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/17373
* [Nested] Fix: 16489 - Find `NULL`s in lists using `list_position` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17080
* fix #17258: Allow to open database in readonly mode within cli by [@jjballano](https://github.com/jjballano) in https://github.com/duckdb/duckdb/pull/17375
* Join Hash Table Probing Optimization: Optional Probing Selection Vector by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/17062
* Remove bundled TPCH & TPCDS in Python wheels by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15923
* [Compression] Introduce `DICT_FSST` compression method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15637
* Deprecate lambda arrow (->) and replace it with LAMBDA x : x + 1 by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17235
* fix not setting nested validity when map_extract returns null by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17379
* Function chaining: report missing column instead of missing function if function exists by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17383
* Improve error messages in UPDATE ... SET by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17384
* Add candidates suggestion when COLUMNS regex does not match any columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17385
* add step to clean up the disc space to fix `No space left on device` by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17390
* Fix issue in string -> hugeint conversion with decimals and exponents by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17388
* Improve error message reporting for cast failures by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17382
* Fix Python CI: pin virtualenv to previous version by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17386
* Improve error reporting for missing qualified columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17397
* Issue #17266: Lead Lag Nulls  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17391
* Fix #17266：the result of lad/lead when the offset is null by [@ditdb](https://github.com/ditdb) in https://github.com/duckdb/duckdb/pull/17268
* VirtualFileSystem to take an input, allowing to customize behaviour by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17393
* [Dev] Add `QualifiedName::ParseComponents`, add input to the error messages by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17403
* Provide suggestions and a link to the documentation for OOM errors by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17402
* [Dev] Flatten any deeper children vectors, when the top level is a FLAT vector by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17387
* Minor fixes for the CLI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17405
* Add support for CREATE OR REPLACE TYPE, CREATE TYPE IF NOT EXISTS and CREATE TEMPORARY TYPE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17404
* Use an insertion order preserving map in Value::MAP by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17389
* Implement `json_each`/`json_tree` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17406
* Fix #16552: adjust join condition sequence by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/16943
* WAL replay index fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17409
* ZSTD: use a high penalty when min size is exceeded instead of disabling compression to allow force compression to work by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17412
* Internal #4723: PWMJ Inequality Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17400
* Move all httplib code to HTTPUtil class by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17420
* Avoid generating default views and macros in the temporary catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17408
* unittest: improve detection of whether or not we can run `--force-restart` tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17419
* Give tasks a `TaskType` with a name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17421
* Use argparse in scripts/format.py by [@adsharma](https://github.com/adsharma) in https://github.com/duckdb/duckdb/pull/17360
* Add missing commas by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17424
* Internal #4830: IEJoin Inequality Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17422
* Add conn.query_progress() method by [@nickzoic](https://github.com/nickzoic) in https://github.com/duckdb/duckdb/pull/16927
* Fixes filter pruning use the statistics updated by the same filter by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/17425
* Fix JSON extension compilation on Ubuntu 22.04 by [@staticlibs](https://github.com/staticlibs) in https://github.com/duckdb/duckdb/pull/17434
* Use pytest in SQLLogic Python test runner by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/16685
* On COPY TO/FROM check the format during binding. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17381
* BUGFIX: DELIM_JOINS should reflect functionality of NULL filtering conditions in joins with DELIM_GETS by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16910
* Allow directly attaching of Parquet/CSV/JSON files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17415
* Force errors when trying lines as early as possible by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17427
* Enable `SYSTEM_PEAK_BUFFER_MEMORY` and `SYSTEM_PEAK_TEMP_DIR_SIZE` profiling by default by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17407
* [C API] Expose the client context, connection id and scalar function bind data by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17449
* [CSV Sniffer] Proper type replacement in header only files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17447
* Recurse into `MAP` and `LIST` with the `remap_struct` and the MFR ColumnMapper by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17448
* Fix: pyproject.toml does not contain a tool.setuptools_scm section by [@YUKI2eN3e](https://github.com/YUKI2eN3e) in https://github.com/duckdb/duckdb/pull/17443
* [Fix] Macro binding with unknown parameters in list_has_all and some other code tidying by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17450
* Generalize HTTP interface and use the new HTTP interface in `httpfs` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17464
* [Fix] Switch between constant and flat vector in C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17465
* Fix TIMETZ cast in example by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17468
* Remove duplicated arrow fetch test by [@emmanuel-ferdman](https://github.com/emmanuel-ferdman) in https://github.com/duckdb/duckdb/pull/17476
* Multi File Reader Rework (Part 19): Make `MultiFileReaderInterface` virtual, and move reading methods to the `BaseFileReader` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17475
* [Serializer] Lambda Compatibilty Fix by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/17428
* fix parsing bool values in JSON by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/17460
* Emit dictionary vectors with unaligned start index by [@OmidAfroozeh](https://github.com/OmidAfroozeh) in https://github.com/duckdb/duckdb/pull/17471
* Add release version by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/17479
* Expose qualified table names in GetTableNames and add duckdb_get_table_names to C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17472
* Bump avro, httpfs, mysql, postgres and sqlite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17482
* Fix GeoParquet ExpressionColumnReader schema by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17481
* add regression_threshold_seconds argument to `regression/test_runner.py` by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/17485
* DROP of missing entry should fail in binding by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/17474
* HTTPFS Parameters fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17486
* HTTPUtil Fix: correctly pass in on_retry by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17494
* Bump spatial & vss by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17492
* Add support for altering structs (drop, add, rename field) inside `LIST` and `MAP` columns. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17462
* [Python Dev] Guard against python exceptions when interacting with the `currentframe` object by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17490
* If distinct count from stats is 0, do not use it in Join Order Optimizer by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17466
* Make the encodings extension a core extension, and make it auto-loadable. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17206
* Allow passing down rc-style version also via OVERRIDE_GIT_DESCRIBE by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17501
* Allow DUCKDB_EXPLICIT_VERSION to be propagated by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17498
* Minor nightly fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17500
* Add FileSystem::TryRemoveFile - that only removes a file if it exists by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17502
* Add OperatorFinalize callback to operators - which is called after a pipeline is finished by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17503
* Apply dynamic filter pushdown of TopN optimizer also to existing TopN nodes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17504
* Fix: Optional Probe Selection by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/17505
* FileHandle Logging by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16758
* Fix typos by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/17478
* Remove spatial from OSX Relassert by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17509
* Update more extensions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/17510
* Bump HTTPFS again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17511
* feat: include catalog and schema names in function serialization by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/17512
* Fix encodings by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17514
* Fix python nightly build by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17515
* Use Catalog::TryAutoLoad for encodings extension by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17520
* [Python Dev] Using `reinterpret_steal` breaks the refcount of the passed-in object by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17525
* Fix update extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17527
* Minor fixes to exception error messages by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17528
* [Python Dev] Fix failing tests for the Python SQLLogicTester by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17529
* Resolve GitHub workflow `set-output` deprecation warnings by [@kurtmckee](https://github.com/kurtmckee) in https://github.com/duckdb/duckdb/pull/17516
* [CSV Reader] Detect SQLNULL types for schema merging, use schema merging in csv relations, add files_to_sniff option.  by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/17467
* Fix extension test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17536
* [Dev] Fix crash when describing a table with a virtual column by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17544
* [HTTPUtil] Let requests made through the `HTTPUtil` interface accept URI's without a scheme. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17545
* Attach after setting database type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17546
* Pass MultiFileGlobalState to InitializeReader, and pass file list to CreateMapping instead of eagerly getting the first file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17553
* [Dev] Fix `allowed_directories` crash by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17548
* [Fix] duplicate filters during index scans by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/17547
* Generate data for tpch sf100 in steps by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/17539
* Issue #17537: Fractional Second Padding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/17556
* Make MultiFileList::Copy a virtual method by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17566
* [Dev] Can't use `USING COMPRESSION` with a deprecated compression type by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17542
* Add (de)serialization for ExtraOperatorInfo by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/17563
* Fix issue with `ExternalFileCache` when data is evicted by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/17567
* Remote Reads: allocate correct buffer size for prefetch by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/17557
* Remove patch and bump httpfs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17558
* [Dev] Fix Arrow fixed size binary reading by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/17573
* Fix setup.py to correctly handle OVERRIDE_GIT_DESCRIBE by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17580

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.2.2...v1.3.0

---

# v1.2.2 - v1.2.2 Bugfix Release <a id="v122"></a>

*Released on 2025-04-08*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.2.2)

This is a bug fix release for various issues discovered after we released 1.2.1. There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9.* can be read by this version.

## What's Changed
* [Python] Fix deadlock in `from_parquet` with `file_globs` caused by not releasing the GIL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16522
* [Python] Fix some stubs issues by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16523
* [Dev] Fix issues in the benchmark runner related to the serialized `storage_version` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16533
* Set estimated cardinality to newly created logical operators by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/16528
* custom_extension_repository to also be the default autoinstall_extension_repository by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16459
* [Python Dev] No longer trigger a DeprecationWarning when using a UDF by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16433
* Fixup problems connected to prep to 1.2.1 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16578
* Give preference to quote=escape if we can't do better by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16584
* Max ART key length by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16588
* Issue #16617: Window Constant Finalize by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16628
* [Fix] Index scan - Move the table scan state into the local state by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16650
* [Fix] Perform eager constraint checking during physical batch insert by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16651
* [Python] Don't push down `OPTIONAL_FILTER` into `pyarrow` for the arrow scan. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16657
* move OrderPreservationRecursive to physical_plan_generator.hpp by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/16656
* Add libs folder to bundled static libs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16655
* Avoid UMA by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/16641
* Avoid UMA by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/16643
* Avoid UMA by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/16642
* Several fixes for CSV fuzzer tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16636
* FSST Fix: Correctly detect the situation where we have 3 bytes remaining by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16688
* Fix #16627: handle DISTINCT FROM and NOT DISTINCT FROM in zone-map pushdown by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16691
* Fix #16554: emit blobs as part of .dump by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16693
* add avro by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/16708
* Issue #16652: Implicit Ordered Aggregation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16718
* Issue #16649: SelectNth Remainders by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16705
* [Dev] Fix `EXPORT DATABASE` missing semicolons in produced `schema.sql` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16723
* Always throw the error that happens the earliest in the CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16728
* Fix #16662 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16732
* [Test] Add missing test for eager-constraint checking fix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16745
* Clamp reported memory in duckdb_memory by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16753
* CLI `-help`: Fix default value for -nullvalue by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16755
* Apply RLE fix to v1.2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16756
* [Arrow] Setting schema of the keys to not null for maps and properly write Null columns to arrow by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16711
* Fix min/max values in numeric cast exception message by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/16777
* [ADBC] Add wrapper to connection new, set options at connection init, if any. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16748
* Remove delta from extensions built on a nightly basis (vs 1.2-histrionicus) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16794
* `PhysicalTopN`: Buffer-allocated `StringHeap` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16770
* [chore] Add v1.2.2 to storage versions, preparation for upcoming patch release by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16799
* Fix issue when line is empty by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16823
* Add extra check in normalize for commit, rollback and abort by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16802
* Fix #16783: Fix DistributivityRule by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/16804
* Internal #4492: Ignore Nulls Orrification by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16837
* Fix #16836: rewrite main column data in case of an update that only modifies the validity by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16851
* Initialize type by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16848
* [CSV Reader] Add check on ever quoted for candidate selection by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16868
* Clean up partial deletes when encountering a transaction conflict in a vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16905
* Fix clang-tidy: add missing include by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16920
* Backport "Adding gzip version of shell for linux/osx install script" by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16917
* Backport "Adding gzip version of shell for linux/osx install script"/2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16924
* Skip tests for Python 3.8, already end-of-life by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16923
* Bump to avro version that now support wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16916
* Unwrap DUCKDB_EXTENSION__LINKED_LIBS via CMake by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16914
* Skip manylinux-extensions-x64 job by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16932
* [Fix] Disable recursion for invalidated database error by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16907
* bump excel (on v1.2) by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16915
* [Fix] Flush local storage before any deletes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16951
* [Python] Fix PyArrow filter pushdown for NaN by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16952
* Allow overriding the Printer::Print output destination by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/16909
* bump out-of-tree extensions to v1.2.2 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16913
* Allow SQL prepared statements to be rebound by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16820
* Fix #16959: binding constraints should not modify the original constraints by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16971
* Add back manylinux extensions [on v1.2-histrionicus] AND bump extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16976
* Skip TPC-DS Q67 on DOUBLE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16987
* Re-enable iceberg by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16992
* Try enabling and bump delta by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16990
* Backport [@szarnyasg](https://github.com/szarnyasg)'s PR 16999 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/17013

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.2.1...v1.2.2

---

# v1.2.1 - v1.2.1 Bugfix Release <a id="v121"></a>

*Released on 2025-03-05*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.2.1)

This is a bug fix release for various issues discovered after we released 1.2.0. There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9.* can be read by this version.

## What's Changed
* [Dev] MultiFileReader fix InternalError in CreateFilterMap by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16114
* [bug-fix] Avoid throwing in catch block for failed commits by [@Vegetable26](https://github.com/Vegetable26) in https://github.com/duckdb/duckdb/pull/15903
* Issue #16098: ValidEnd Parallel Vectorisation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16140
* Adding an extension option shouldn't delete a set value and promote unrecognized options by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/15919
* Parquet writer: Re-implement GetRowSize for Strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16178
* Fix #16157: correctly get the first row when reading hive partitions from a dictionary vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16180
* Fix #16122: bind default values in a sub-binder to avoid modifying the catalog search path of the current binder by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16181
* Fix #16134: when a catalog/schema/table has the same name, we prefer to suggest the table name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16189
* Ensure MergeCollectionTask has a writer by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/16207
* Backport #16115 by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16227
* Deleted copy constructor of pending query by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16242
* Correctly report errors caused by get_database in C extensions by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/16253
* use random seeds for bernoulli sample when parallel is enabled by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16223
* Parquet Reader: avoid caching the compressed buffer in the ColumnReader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16263
* Fix #16260: correctly handle parameters in getvariable by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16264
* Avoid calling SetFilterAlwaysTrue multiple times in RowGroup::CheckZonemap by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16269
* [Fix] Scanning from normal leaf to nested leaf by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16270
* Fix #16231: refer to order by condition in ARRAY(SUBQUERY) by alias instead of by index by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16272
* Fix #16257 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16275
* AFL Tests for the CSV reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16280
* Issue #16250: Window Range Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16276
* Fix #16278: late materialization should not trigger on very large limits, and it should never trigger on limits without offsets when preserve_insertion_order = false by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16282
* Overflow strings allocations: avoid rounding up memory allocated per overflow string - when reading "small" overflow strings place them directly into the vector instead by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16283
* Use ordered map to preserve expressions order by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/16111
* [Dev] `register_filesystem` stubs, use `fsspec.AbstractFileSystem`, not `str` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16266
* [Python Dev] Fix crash with empty args for `isin` | Fix transformation for `isnotin` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16271
* Fix issue related to hang when all candidates are eliminated in refinement by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16288
* [Fix] Early-out on CREATE INDEX (IF NOT EXISTS) by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16093
* [Python] Fix the reverse binary expressions in the Expression API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16300
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16244
* [Fix] MinGW bundle static libs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16292
* Fix heap buffer oveflow sampling by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16279
* Expose STRING_LITERAL in C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16293
* Allow accessing profiler query tree under lock by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/16314
* bump extensions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16313
* Inline virtual list lambda bind functions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16327
* Update shell.cpp to fix #16333 by [@teaguesterling](https://github.com/teaguesterling) in https://github.com/duckdb/duckdb/pull/16335
* Add the suggestion to verify the nullstring as part of the cast error message by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16336
* Take `NULL`s into account for `DELTA_BINARY_PACKED` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16317
* PhysicalTableScan: Adapt to allow async behaviour by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16310
* Allow querying attached catalog from detached catalog by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/16289
* Reduce minimum expected memory usage in `RadixPartitionedHashTable` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16332
* Backport ebb4dccf to v1.2-, adding missing include by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16369
* Excecption load on mismatched ABI: Use '%d' to print ABI type by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16367
* Aggregation: For dictionaries without an id - use the correct threshold to bail-out on using the dictionary by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16364
* Bump excel to the same version distributed on `core` repository by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16375
* Accept valid dialects with escape set into the refinement phase by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16387
* Push the correct casts for values of different types in (X, Y) IN (SELECT X, Y) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16392
* Add support for autoload and autoinstall for `ui` extension by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16393
* Add twine_upload option to Python.yml to trigger upload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16410
* Only select options that generate more columns with null_padding, if they at least hold 50% of consistency by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16404
* Use checkpoint bind in DuckTableEntry::Copy to avoid re-validating default values (and potentially causing issues during WAL replay) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16398
* Rename `DUCKDB_API` to `DUCKDB_C_API` for `duckdb.h` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16397
* Issue #16407: Try_Strptime Invalid TimeZone by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16416
* Internal #4303: Windowed DISTINCT Leaks by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16417
* Internal #4258: MODE Spooling Stability by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/16415
* Fix PyPi upload also for branches, when twine_upload is provided by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16421
* [Fix] Throw constraint violation for FK constraint checking by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/16399
* Add storage and serialization version for v1.2.1 by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/16403
* Update flaky return_files.test by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/16432
* Add python version to duckdb_api by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/15599
* Do not accept null values in lists for column parameters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16425
* Use seed for system sample when it is provided.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16408
* Bump delta to working commit by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16442
* Adding windows code signing using azure by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/16444
* CSV small code Improvements + initialising boolean variable. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/16454
* [Python Dev] Make `pandas` not required in a couple places, check if it's installed in others by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16414
* fix passing a null path to the C API instance cache by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/16474
* Add methods to retrieve current task scheduler busyness by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/16465
* Fixed reading piped JSON by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16480
* [Python Dev] `pyproject.toml` should not use `oldest-supported-numpy` anymore by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/16486
* [tests] Multiple FORMAT in copy, only last one matters by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16493
* Bump `postgres_scanner` and `fts` extensions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/16492
* bump sqlsmith extension tag by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16488
* [BugFix]: Swap join children, not left and right set by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/16487
* [tests] Add allow_unsigned_extensions require by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16499
* Provide callback when tasks are starting / stopping by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/16451
* CodeQuality: ubuntu-20 to ubuntu-22, lock black to version 24 and trick clang_format detection by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16513
* Move from ubuntu-20:04 to ubuntu-22:04, part I by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16510
* [chore] Build Linux releases also on PRs AND ubuntu-20 to 22 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16506
* Move from ubuntu-20:04 to ubuntu-22:04, part II by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16514
* bump spatial and excel for v1.2 by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16504
* CI Fixes after upgrade to ubuntu 22 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/16516
* LinuxRelease.yml: Pass down override git describe by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/16521
* bump spatial again by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/16518

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.2.0...v1.2.1

---

# v1.2.0 - DuckDB 1.2.0 "Histrionicus" <a id="v120"></a>

*Released on 2025-02-05*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.2.0)

This release of DuckDB is named "Histrionicus" after the good-looking Harlequin duck (Histrionicus Histrionicus) that inhabits "cold fast moving streams in North America, Greenland, Iceland and eastern Russia".

Please also refer to the announcement blog post: https://duckdb.org/2025/02/05/announcing-duckdb-120

## What's Changed
* Optimise division by a constant at runtime for integer division by [@JAicewizard](https://github.com/JAicewizard) in https://github.com/duckdb/duckdb/pull/10348
* Add cross join to Python Relational and PySpark API by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/13519
* Fix #13805: throw a more descriptive error message when an on-disk file is referenced using a replacement scan for an unsupported file format by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13871
* Make sampling accept parameters at the parser/transformer layer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13903
* Fix #13867: use 64-bit random numbers to generate random numbers for `random()` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13920
* Fix #13769: when binding views, always first search in the schema that the view is defined in by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13921
* Rework table bindings to be components (`catalog`, `schema`, `table`) instead of flat strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14017
* Add auto-loadable extension settings to duckdb_config_count and duckdb_get_config_flag by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14021
* Fix #10961 - in the HAVING clause - in case of column name conflicts, bind to aliases instead of to ungrouped columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14023
* Enable filter pushdown through Logical Unnest by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14008
* Allow duplicate table aliases in the table binder by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14035
* Unify DESCRIBE [query] and DESCRIBE [table] by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14039
* Support qualified identifiers in the `EXCLUDE` clause by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14043
* Add `SMALLER_BINARY` flag to reduce binary size  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14057
* Smaller Binary: remove more templates from arg_min_max by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14071
* Unify entropy and mode aggregates - and skip specialized implementations for entropy with smaller binary by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14080
* [Python] Add `set_default_connection` to the `duckdb` module by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13442
* Provide workaround for prefetching parquet files with incorrect page offsets by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13697
* Move `core_functions` to a separate extension by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14149
* PySpark df.drop() to support expressions by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/14059
* add some RealNest benchmarks by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13345
* feed table function into multifilereader initialization by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14112
* [Dev] Fix an issue causing ExecuteTask to do much more work than intended by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14034
* Overhaul Parquet dictionary handling  by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14194
* [Feature] Allow passing the catalog (database name) to appender by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13692
* Add Taxi Dataset Benchmark by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14197
* Feature #3036: Window Spooling by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14181
* Small C Extension API changes by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13987
* Add HTML and Graphviz support for explain analyze by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/13942
* Fix #13064: offer more suggestions with same score by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14048
* New Algorithm to find a new line on parallel execution by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14260
* Making client context lock optional for relation binding by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14093
* [Feature] Allow passing the catalog during C API appender creation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14256
* Make test random output ordered by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14267
* Skip test_window_distinct by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14309
* Taxi Benchmark by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14301
* Switch to shared pointer for multfilelists by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14291
* Push  #14298 to feature branch by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14311
* Implement PullUp Empty Results optimizer by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13524
* [Export/Import] Use the DependencyManager to (stable) sort the entries before export by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14196
* Partitioning-Aware Aggregation and Partitioning-Aware Infrastructure by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14329
* Add df.unionByName to PySpark API by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/14063
* Or filter pushdown into zone maps by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14313
* Get the current setting in the database file opener by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14361
* [Feature + Fix] Support ALTER TABLE tbl ALTER col TYPE USING and fix null handling in struct_insert by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14359
* [C API] Add table_description_create_ext and table_description_get_column_name by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14285
* Move _rtools platform to be equivalent to _mingw by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14368
* Fix for accidental like skip in the CSV Buffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14380
* Table locks - always grab table locks through the transaction interface  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14379
* Implementing array_slice and [] for BLOB by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14358
* Rework settings handling and implement auto-generation for new ones by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14383
* Rework settings handling and implement auto-generation for new ones by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/14018
* Arrow list buffer - suggest setting `arrow_large_buffer_size` to true when regular list buffer size is exceeded by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14384
* Fix incorrect merge conflict resolution in workflow file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14390
* Update Parquet Thrift to latest version by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14258
* Reformat list functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14372
* Tidy Check to do complete run also on feature by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14394
* [Python] Use an `ArrowQueryResult` in `FetchArrowTable` when possible. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14319
* Make mysql_scanner auto-loadable, and add mysql/postgres secrets by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14392
* Improvement the speed of table sample systems by [@continue-revolution](https://github.com/continue-revolution) in https://github.com/duckdb/duckdb/pull/12631
* Support defining column names in CTAS by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/14327
* Fix pointer indirection in pyrelation.cpp by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14403
* Fix idx_t to int64_t implicit conversion flagged by clang-tidy by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14402
* Storage: make `ROW_GROUP_SIZE` configurable by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14406
* [Dev] Update vendored ZSTD to v1.5.6 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14360
* Top-N: Rework to use heap of sort keys by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14424
* reformat string functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14400
* Prefix Aliases in SQL by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14436
* [Dev] Optimize `ValidityMask` when reading from a `ColumnDataCollection` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14416
* [Dev] Further optimize the CDC ValidityMask deserialization by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14448
* Reformat date and map functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14425
* Reformat generic functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14423
* Push dynamically generated join filters through `UNION`, `UNNEST` and `AGGREGATE` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14453
* Try auto-casting for mismatching data chunks in the Appender API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14433
* Implement `DELTA_BINARY_PACKED` compression in Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14257
* Eviction Queue Partitioning by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14375
* Implement `map_extract_first` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14175
* RowGroup no longer lives in format namespace by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14469
* Convert the shell from C to C++ by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14473
* Fixing an issue with parquet dictionary reading by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14438
* Strip down unused/unsupported options from the CLI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14478
* [PySpark] Add withColumns, withColumnsRenamed, cos, acos, any_value, approx_count_distinct and various array functions by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14347
* CLI Code Cleanup: move all shell functions into the ShellState by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14483
* CLI Code Cleanup: Move rendering logic into separate Renderer classes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14485
* Reformat compressed materialization functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14470
* Internal #3273: Shared Window Expressions  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14450
* CLI Code Cleanup: rework metadata commands in the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14503
* CSV Parallel Reading Validation by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14439
* Avoid recompilations of duckdb when there are no actual changes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14176
* Add `-safe` mode to shell which disables external access, and remove SQLite UDFs from the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14509
* [PySpark] Add functions covar_pop, covar_samp, call_functions, endswith, startswith, exp, factorial, log2, ln, degrees, radians, atan, atan2, tan, round, bround by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14454
* Reformat arithmetic operators by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14489
* add attach with default tables by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14118
* Add duckdb_param_logical_type by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/14515
* Remove most BUILD_ options for extensions, using CORE_EXTENSIONS by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14531
* CLI: more code clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14551
* Reformat nested and sequence functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14495
* Parquet: Fixing selection vector calculation by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14558
* CLI: Fix for .mode markdown rendering after refactor by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14569
* Out-Of-Core Updates & Deletes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14559
* Manage `enable_external_access` at the FileSystem level, and add `allowed_paths` and `allowed_directories` option by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14568
* feat(iejoin): use sort to replace binary search in iejoin by [@my-vegetable-has-exploded](https://github.com/my-vegetable-has-exploded) in https://github.com/duckdb/duckdb/pull/14507
* Clean-up distinct statistics - add hashes cache add the Append and Vacuum layers, and remove unnecessary lock by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14578
* [PySpark] Test Spark API with actual PySpark as backend by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14526
* Internal #3273: Shared Window Frames by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14544
* Reformat aggregate functions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14530
* Expose threshold argument of Jaro-Winkler similarity by [@zmbc](https://github.com/zmbc) in https://github.com/duckdb/duckdb/pull/12079
* No pushing filters below projections that cast to a lower logical type id by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13617
* Implement `left_projection_map` for joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13729
* remove superfluous comment by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14586
* [Dev] Make the `regression_test_runner` easier to replicate by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14557
* [PySpark] Add dataframe methods drop_duplicates, intersectAll, exceptAll, toArrow by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14458
* Internal #3381: Window Race Condition by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14599
* Rework generated EnumUtil code by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14391
* Force aggregate state to be `trivially_destructible`, unless `AggregateDestructorType::LEGACY` is used by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14615
* AWS - remove expected error message by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14633
* Temp directory compression by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14465
* Add support for SELECT * RENAME by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14650
* [PySpark] Add autocompletion for column names to dataframes by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14577
* Force aggregate state to be `is_trivially_move_constructible` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14640
* Correctly render EXPLAIN EXECUTE - use op.GetChildren() instead of hard-coding special cases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14651
* Buffer Manager - Make DestroyBufferUpon atomic by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14656
* proposed enhancements to the query graphs by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/14637
* Sampling respects seed from random number generator if no seed is given. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14374
* Blockwise NL Join: Return control on every iteration in `ExecuteInternal` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14658
* feature(spark): add hex and unhex functions by [@spenrose](https://github.com/spenrose) in https://github.com/duckdb/duckdb/pull/14573
* Support `SELECT * LIKE '%col%'` syntax by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14662
* feature(spark): add base64 and unbase64 function by [@spenrose](https://github.com/spenrose) in https://github.com/duckdb/duckdb/pull/14561
* Fix #14663: correctly propagate null values in list concat operator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14675
* `ALTER TABLE ADD PRIMARY KEY` by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14419
* Merge feature into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14690
* Support for CSV Encoding (UTF-16 and Latin-1) by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14560
* Fix #14699 - Correctly handle SHOW TABLES in views by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14705
* Fix #14701 - avoid flattening in-place in ColumnData Append method by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14708
* Use TryCastAs instead of DefaultTryCastAs in comparison_simplification by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14711
* Value interface & serialization clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14710
* Fix various nightly CI issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14720
* CLI: Add support for `.thousand_sep` and `.decimal_sep`  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14721
* Propagate collations through functions in a generic manner by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14717
* Add functions for handling null duckdb_values by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/14687
* adaptive filters should not reorder filters that can throw by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14672
* [Python] Add `LambdaExpression` to the Python Expression API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14713
* Add fallback for thread count if jemalloc cannot identify by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14688
* csv: parse escape character in unquoted fields by [@fanyang01](https://github.com/fanyang01) in https://github.com/duckdb/duckdb/pull/14464
* [Python][Expression API] Add the `between` method on the `Expression` class by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14726
* [Attach][Macro] Fix issues identified with an attached macro by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14715
* Dont quote strings on csv files if quote='' by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14731
* sqlite3_api_wrapper: avoid nullptr dereference by [@ProjectMutilation](https://github.com/ProjectMutilation) in https://github.com/duckdb/duckdb/pull/14748
* Rework `BlockHandle` to no longer have friend classes, and rework `ConvertToPersistent` so it fails if there are active outstanding pins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14746
* Revert "CMake: Avoid dependency-inducing codegeneration of extension headers" by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14723
* [PySpark] Add more functions such as ascii, asin, btrim, char, corr, ... and fix differences in ordering of null values between PySpark and DuckDB by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14738
* Added list value getters duckdb_get_list_child and duckdb_get_list_size by [@prashanthellina](https://github.com/prashanthellina) in https://github.com/duckdb/duckdb/pull/14714
* [Python][Expression API] Add `collate` to create a `CollateExpression` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14749
* copy to operator still write schema for empty rows by [@wenjun93](https://github.com/wenjun93) in https://github.com/duckdb/duckdb/pull/14524
* [Python] Use nullable dtypes in Pandas `DataFrame` creation when possible by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14377
* Update metrics generation script and include it in CI run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14756
* Add support for projection pushdown into struct fields by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14750
* Optimistic writes: flush the last row group in all scenarios by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14759
* Improve SqlStatement::ToString for UPDATE and DELETE statement to include alias of RETURNING clause by [@HarshLunagariya](https://github.com/HarshLunagariya) in https://github.com/duckdb/duckdb/pull/14765
* Add JSON Logical Type metadata to parquet writer by [@niger-prequel](https://github.com/niger-prequel) in https://github.com/duckdb/duckdb/pull/14747
* [Python] Add support for `Expression` to `values` to create a ValueRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14757
* Add missing global options to Python's `write_parquet` by [@fr3fou](https://github.com/fr3fou) in https://github.com/duckdb/duckdb/pull/14766
* Add operator name to profiling output by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14744
* Detect catalog changes on DROP IF EXISTS by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14742
* Correctly deal with continued operation after reading a truncated WAL, and clean up WAL handling logic in storage manager by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14785
* [Fix] Error message in transaction manager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14788
* Initialize the grouping sets when there is a group by all to enable filter pushdown by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14660
* Merge feature into main again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14793
* [Python][Expression API] Add `update` to `DuckDBPyRelation`, accepting `Expression` objects | Add `DefaultExpression` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14780
* Fix #14540: fix unnest rewriter by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14784
* [PySpark] Add approxCountDistinct, add_months, and various array functions by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14620
* Add syntax highlighting support for errors in the CLI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14799
* Implement #14787: allow expressions in the aggregate clause of a PIVOT statement, as long as the aggregate clause only modifies the aggregate result and does not contain other columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14800
* When repeatable is set, set ParallelSink to false by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14797
* [Catalog] Fix issue related to uncaught problems during a COMMIT by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14150
* [Upsert] Support non-distinct values in the inserted data by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14293
* Fix issue copying a TABLE that references a SEQUENCE by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14693
* fix duckdb_extension.h macros for C by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14808
* LTO CMake setting was not working anymore on MacOS, fixing that by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14811
* Add syntax highlighting support to the DuckBox query result by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14820
* Avoiding unnecessary rebinding by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14616
* Support struct projection pushdown in Parquet files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14839
* Internal #3263: Window Distinct Deadlock by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14775
* Issue #14737: DISTINCT ORDER Dependency by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14840
* [Python][Dev] Skip `test_pandas_selection` on Python3.8 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14851
* [Python][Dev] Fix issues with new/updated tests in the python sqllogictest implementation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14850
* add function ends_with back by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14859
* Require `capacity` in ValidityMask by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14846
* Issue #11557: DECIMAL Downcast Rounding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14860
* Increase map inference threshold by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14848
* Output exception message on parse exception by [@ackxolotl](https://github.com/ackxolotl) in https://github.com/duckdb/duckdb/pull/14852
* Use `LogicalTypeId::Unknown` instead of `LogicalTypeId::SQLNULL` for macro binding by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14809
* return InsertionOrderPreservingMap from TableFunction to_string by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14835
* Support default values when appending data chunks by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14733
* [PySpark] Add a lot more functions incl. some regexp ones by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14761
* Added getters for enum and struct type values by [@prashanthellina](https://github.com/prashanthellina) in https://github.com/duckdb/duckdb/pull/14831
* Fix write partition columns false by [@ykskb](https://github.com/ykskb) in https://github.com/duckdb/duckdb/pull/14871
* Generate In-Clause filters from hash joins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14864
* Move FTS extension out-of-tree by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14872
* [C API] More tests and nits by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14758
* Issue #14885: DATEPART Cache Bounds by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14891
* Fix arrow table filters by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14893
* [Python] Fix various issues uncovered by #12959 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13149
* Remove some Snappy definitions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14897
* [Fix] Binder exception when creating a foreign key on a view by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14882
* [C API] Implement AddColumn and ClearColumns for the Appender by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14880
* python: use PyUnicode_FromStringAndSize() by [@methane](https://github.com/methane) in https://github.com/duckdb/duckdb/pull/14895
* Top-N: Improve performance with large heaps, and correctly call Reduce by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14900
* Append to child column first in list column append by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14902
* Update cardinality during limit pushdown by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/14901
* Add `struct_concat` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14853
* [Compression] Add ZSTD compression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14514
* Improve timestamp functionality by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14818
* Fix #14833: split_part follow pg by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14875
* C API: Add Value Relation constructor with RelationContextWrapper and ParsedExpression as argument by [@anshuldata](https://github.com/anshuldata) in https://github.com/duckdb/duckdb/pull/14892
* Issue #14734: Wrap Parquet TIMETZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14908
* [Fix] release shared connection pointer before it goes out of scope by [@roj516](https://github.com/roj516) in https://github.com/duckdb/duckdb/pull/14926
* [Fix] Nightly async build by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14913
* [Tests] Re-enable test for vector verification run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14911
* Return timestamp with timezone in `read_text`/`read_blob` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14925
* Fix several CLI issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14929
* improve ReadAheadBuffer::AddReadHead error message by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/14940
* Skip Dynamic Join Ordering Algorithm if there are many relations by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14943
* remove failing benchmark  by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/14945
* Typo in csv UnterminatedQuotesError how_to_fix_it by [@bradleybuda](https://github.com/bradleybuda) in https://github.com/duckdb/duckdb/pull/14951
* Pullup empty results through delim joins as well by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14920
* Fix getting named parameter type information. by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/14952
* Fix casting long to int via explicit cast in parquet by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14959
* Fix script/regression/benchmark.py rework by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14958
* Explicit install of pkg-config broke, removing it by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14965
* Improve code generation of storage and serialization version infos by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14947
* C API support for non-standard timestamp values by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/14954
* Implement Logical Compaction in Hash Join Operator by [@YimingQiao](https://github.com/YimingQiao) in https://github.com/duckdb/duckdb/pull/14956
* Disable row group size bytes default initialization by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14974
* [Swift.yml] Bump to macos-14, and switch simulation targets by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14984
* Use IOException for failed fstat calls by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14975
* Logical Sample requires child to have separate join order optimization by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14969
* Properly register successful dialect runs by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14977
* Run containerized builds requiring deprecatd ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION only on main/feature by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14998
* Fuzzer #3297: Nth Value Indexing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14997
* [Arrow] Filter pushdown decimal fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14995
* Support multiple function descriptions by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14838
* Join Filter Pushdown does not push down in filters when nulls are present by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14970
* [Fix] Throw on invalid MAP input in Value::MAP by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14916
* Rely on extension-ci-tools workflow to build linux_amd64_gcc4 extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14987
* Rework Auto-Complete To Work Based On PEG grammar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15003
* for-loop-erase bugfix in filter pushdown by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/15008
* Internal #861: Window Code Refactoring by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15007
* Internal #3574: INTERVAL Normlisation Carries by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15009
* [Arrow] Fix scan of an object providing the PyCapsuleInterface when projection pushdown is possible. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14993
* [PySpark] - Add extra str functions to pyspark api by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/14921
* [PySpark] - Add .isNull and .isNotNull methods to Column class by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/14960
* DuckDB Arrow Non Canonical Extensions to use arrow.opaque by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15002
* Autocomplete test fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15019
* Add check_peg_parser to extension_entries by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15021
* Re-enable jemalloc on ARM by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14810
* Dynamically decide whether to do a Perfect Hash Join by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14971
* No salt for Android by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14923
* Fixup linux_arm64 extension builds by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15016
* Issue #14834: INTERVAL Collations by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15022
* SUM(x + C) rewrite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15017
* Spell NULL with uppercase in configuration description and comments by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15006
* Force download doesn't require to do a head request by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14979
* CSV Reader - 4 byte delimiters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14670
* More regression tests by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14973
* [PySpark] Add more functions such as slice, split, standard deviations, etc. by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/14863
* Fix extension entries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15027
* Speed up scans of RLE compressed data by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15023
* Speed up scans of Uncompressed strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15024
* Internal #3583: INGNORE NULLS Race by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15032
* [Regression.yml] Add icu, needed for external regression tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15044
* Fix internal error of list_zip with only truncate argument provided by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/15039
* Avoid sum rewrite for hugeint/uhugeint since it could introduce overflow errors by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15040
* BarScalarFunction needs to keep track of width != string.size() by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15041
* Add SUM(BOOL) overload by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15042
* Add virtual callback to get dependency manager to the catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15043
* Flip OR filter comparison if constant is on the other side by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15045
* Fix #15010: in map cast only access validity when child elements were not fully converted by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15046
* Various fixes for vector size = 2 CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15047
* Add `require ram` to test runner, and use to limit distinct_grouping_tpch.test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15048
* [pystubs] Fix type of `proto` parameter in `from_substrait` methods. by [@ingomueller-net](https://github.com/ingomueller-net) in https://github.com/duckdb/duckdb/pull/15004
* CLI: Add -f [FILE] argument that allows execution of a file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15050
* max_temp_directory_size - print "90% of available disk space" as value if temp directory is not initialized by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15057
* Interrupt query on error in `ClientContext::Query` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15058
* Turn count_if into an actual aggregate function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15061
* CLI: Add .safe_mode as a dot command as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15064
* Pushdown inequality filters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15059
* Restore support for DEBUG_STACKTRACE by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15053
* Shell: Provide a summary of numbers if we are rendering only a single row by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15031
* Issue #15067: Postgres Age Compatibility by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15070
* add duckdb_append_value to C API by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/15065
* Speed up Main CI workflow by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15071
* [CSV Reader] Being more flexible with unescaped quotes in quoted values. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15018
* IEJoin GetProgress: Normalize to 0-100 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15081
* Avoid building for Python 3.7 on Windows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15085
* Allow inputting a base hash in Regression workflow by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15082
* Top-N: Perform global boundary checking before doing sort-key conversion by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15087
* Fix aggregate regression by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15025
* Sum Rewriter: correctly match only Sum aggregations in sum rewriter by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15088
* new answers for some JOIN benchmarks by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/15090
* Ensure checkpoint tasks complete on IO exceptions by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/15089
* Internal #3615: Quantile Cursor Allocation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15102
* Issue #15056: DISTINCT Insensitive Aggregation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15066
* Bloom Filter Support in Parquet Reader/Writer by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14597
* Dynamically push table filters from Top-N operator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15099
* Fix for #15080 cgroup v2 memory limit not being read correctly by [@nickzoic](https://github.com/nickzoic) in https://github.com/duckdb/duckdb/pull/15103
* Provide support for continuous profiling by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14972
* fix bundle-library step by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15093
* Internal #861: Value Function SubFrames by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15100
* Parquet reader: correctly reset vector in between calls to read when skipping by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15107
* Do not swap `RIGHT` joins to `LEFT` when `BuildProbeSideOptimizer` is disabled by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15105
* Fix CheckMarkToSemi conversion in FilterPushdown optimizer by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/15104
* Setting `temp_directory` to `NULL` should be same as setting it to `''` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15113
* Add make_date(INT) function, similar to make_timestamp(BIGINT) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15109
* Support unlimited precision in JSON by using yyjson "raw" values by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15112
* Avoid repartitioning out-of-core hash joins if very, very skewed  by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15114
* Linux dockerized extensions: invoke script in right folder by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15122
* Operator's GetProgress to return ProgressData instead of double by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15084
* Skip building azure extension due to problems installing libxml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15126
* Test now passes due to flexible quote on CSVs by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15133
* Avoid cleaning up past releases if we have not just uploaded a new one by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15134
* Implement struct projection pushdown for JSON reads by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15116
* Update the `.clang-format` file to disable sorting includes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15131
* `rowid` filter pushdown by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15020
* Parquet Reader: use aligned unpack in RleBpDecoder when possible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15106
* Fixup deployment of extensions for build_extensions_dockerized by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15136
* Parquet reader: rename metadata cache setting to `parquet_metadata_cache`, and avoid using it for stats by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15129
* Fix `BLOB` conversion in `parquet_metadata` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15132
* Add explicit_cardinality to ParquetOptions [de]serialized fields by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15135
* Issue #15138: Friendlier ICU Settings by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15139
* Execute test/sql/aggregate/aggregates/first_memory_usage.test_slow single threaded by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15146
* Store transactions that have deletes on a table with indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15144
* Only generate physical plan for LogicalPrepare when it is going to be used by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/15145
* [CSV Sniffer] Selecting file to sniff from Glob and List by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13703
* Refactor signing linux extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15159
* FileHandle should retain the FileOpenFlags it was opened with by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/15153
* transform modifiers in pivot with no columns by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/15155
* Fix wrong type append of base vector by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15157
* Add cross-version testing CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15161
* Fix wrongly used github.ref to sha by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15167
* Fix Regression workflow running against itself by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15165
* Add dictionary size, and use dictionary/constant vectors in the aggregate hash table to speed up finding groups  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15152
* Fix ci issues by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15169
* Do not assume constant comparison is compare equal by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15164
* Read file in 100mb chunks in read_file/read_blob by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15160
* [Compression] Add RoaringBitmap Compression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14878
* bump spatial + VCPKG Commit by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15158
* Fix various ci nightly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15178
* Keep track of compression function in ColumnData, and add dedicated `select` call to compression function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15186
* Push dynamic Top-N filters for VARCHAR columns as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15188
* Issue #15069: Postgres CURRENT_XXX Compatibility by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15125
* Add DictionaryId that can be used to uniquely identify dictionaries, and use this in the aggregate HT to cache look-ups by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15196
* NULL check for invalid result by [@MonkeybreadSoftware](https://github.com/MonkeybreadSoftware) in https://github.com/duckdb/duckdb/pull/15194
* Rework `TableFilterType::CONSTANT_COMPARISON` to work identically to constant comparisons in SQL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15197
* Fix spelling mistakes in some comments by [@tomhanks2024](https://github.com/tomhanks2024) in https://github.com/duckdb/duckdb/pull/14982
* Move httpfs to external repository by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14727
* Review no_extension_autoloading requires in tests: either remove, add FIXME or add EXPECTED by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15191
* Fix for row-id pushdown, and remove unnecessarily complicated method by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15216
* Fix deserialization of approx decimal quantile aggregate by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15215
* LoadInfo::Copy needs to copy the version by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15214
* RE2: reduce unnecessary allocations in BitState by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15210
* Increase stale bot's timeout by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15224
* [Python][Dev] Remove noisy / faulty test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15220
* Add dedicated `filter` method to compression algorithms by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15209
* [Python][Dev] Fix `test_filter_pushdown.py` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15225
* Rework Wasm extensions CI, and use out_of_tree_extensions.cmake by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15223
* Fix #15221: use TryCast when converting Parquet stats - and fallback to not having stats by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15233
* Fix #15177 - detect corruption in dictionary compressed strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15227
* Fix #15175 - use case-insensitive comparison when de-duplicating hive columns from files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15228
* CLI: only render large numbers if ALL values are large numbers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15229
* Fix several fuzzer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15226
* In Clause Rewriter: add mark column to the filter projection map to avoid projecting it upwards which can cause issues with set operations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15213
* Skip spatial on MinGW, given otherwise mingw extensions CI will fail by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15237
* Add filter on repository_dispatch to Regression nightly run by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15241
* Rework upload ci via reusable workflow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15243
* Bump excel extension by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15222
* `OR`/`IN` filter pushdown for `VARCHAR` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15219
* Issue #15054: Windowed Aggregate Macros by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15181
* feat: Add CHECK expression to error message on constraint failure by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/15148
* Linenoise: make Ctrl+G execute the query by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15244
* Fix #15072 and #15073: propagate aliases correctly in * SIMILAR TO, and forbid `RENAME` as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15247
* Fix #15051: support ORDER BY rowid in ARRAY by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15248
* CLI: improve quote handling in syntax highlighting of errors and don't throw in shell renderer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15249
* Histogram: convert decimals to doubles for histogram binning function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15250
* Revert "RE2: reduce unnecessary allocations in BitState" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15252
* Grouped aggregation performance improvements by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15251
* Add run_benchmark.py script by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15253
* Fix #15012: transform large literals in the range of > HUGEINT_MAX < UHUGEINT_MAX to uhugeint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15255
* Clang-tidy fixes in Parquet writer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15256
* Fix for VERIFY_VECTOR=Dictionary in Window Bounds by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15257
* Fix #15239: detect subqueries in lateral join conditions and throw an explicit error when encountered by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15260
* Implement #14513: implement support for (a, b) IN (SELECT ...) for uncorrelated subqueries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15259
* Various nightly CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15258
* Fix #15261: turn AuxInfo into a safe optional_ptr instead of a raw pointer, and check whether or not enum is complete in pivot by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15263
* Fix for JSONSerializer of BLOB by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15274
* Do not exclude nulls when multiple mark join conditions by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15275
* [Python] Fix an issue with double quotes in `getattr` of DuckDBPyRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15277
* Fixup extension selection by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15272
* [Fix] Bind the ALTER TABLE ADD PK code into the duck catalog by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15231
* Realnest HEP benchmarks by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/14468
* Feature #12699: XXX_VALUE Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15270
* Join order bugs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15230
* Various nightly CI test fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15273
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15276
* Ungrouped aggregate gets cardinality of 1 by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/15279
* More nightly tidy fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15280
* bump vss by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15283
* Fix #15183: correctly handle NULL values in generic GREATEST implementation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15287
* Issue #15246: Negative Nanosecond Timestamps by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15289
* Don't decode special characters on redirect by [@lcostantino](https://github.com/lcostantino) in https://github.com/duckdb/duckdb/pull/15101
* remove O_SYNC from O_DIRECT by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/15294
* Fix #14938: when combining ENUM with SQLNULL/UNKNOWN types, preserve the ENUM type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15297
* allow positional access in named structs by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/15151
* Fix 2 unconnected small problems in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15304
* Add value creation and accessor functions to the C API for VARINT, DECIMAL, BIT, and UUID by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/15212
* Only create information_schema/pg_catalog catalogs in the system catalog  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15286
* Add `get_partition_stats` callback to TableFunction to get a list of all row group metadata, and use this to speed up `COUNT(*)` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15301
* Fix for bitstring_agg on empty result - only complain about missing stats when we actually process rows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15305
* Correctly propagate child-types in MAP to the internal struct values, and test httpfs in LATEST_STORAGE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15303
* remove conditional around fsync in single_file_block_manager by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/15306
* Move away from upload-artifacts[@v3](https://github.com/v3) / download-artifacts[@v3](https://github.com/v3) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15309
* Fix update_extensions_ci test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15310
* Addressing over-eager constraint checking with delete indexes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15092
* Fix internal issue #3740 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/15320
* EXPLAIN/EXPLAIN ANALYZE - limit max lines of each extra info element, instead of truncating the entire node by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15317
* Minor nightly test fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15318
* Bump Extension C API to stable by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14992
* Pass down DUCKDB_EXTENSION_SIGNING_PK as env by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15324
* Bump to latest sqlsmith and re-enable wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15323
* Skipping lookups in `GroupedAggregateHashTable` if (almost) everything is unique by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15321
* Add automatic sampling regression fix 2 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14914
* [Dev] Fix Roaring compression bug on appending small vectors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15326
* Fix JSON reader hang by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15328
* [Dev] Clean up `Dictionary` compression code by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15300
* Adjustments on test to bypass sniffing limitation on vector_size by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15330
* Enable stack traces by default, split into getting the frame pointers and resolve symbols only when the error is finalized, and add support for demangling by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15337
* Use correct element rename_list_el in grammar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15339
* Unified use of constant MainHeader: FLAG_COUNT by [@guoxiangCN](https://github.com/guoxiangCN) in https://github.com/duckdb/duckdb/pull/15338
* Append default to appender by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/15121
* add core functions make_timestamp_ns(nanos) and epoch_ns(timestamp_ts) by [@andreimatei](https://github.com/andreimatei) in https://github.com/duckdb/duckdb/pull/14930
* feat: support create_on_conflict in create_table_relation by [@scgkiran](https://github.com/scgkiran) in https://github.com/duckdb/duckdb/pull/15245
* Fix error message checking in test concurrent index by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15340
* CI: Use mirror for Spark binaries by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15372
* Fix skip CSV Rejects test by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15359
* Vectorize lookups in `GroupedAggregateHashTable` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15368
* Bump azure and remove patches by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15382
* Fix conditional jump or move depends on uninitialised value(s) by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15367
* Start encapsulating `BaseExpression` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15360
* [Python] Allow use of `DuckDBPyType` as child objects in implicit conversions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15346
* [Dev] Made `reference<CompressionFunction> function` private in `ColumnSegment` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15347
* [Dev] Fix erroneous assert in `ZSTD` scan for `LogicalTypeId::VARCHAR` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15357
* [Dev] Reset to the vector cache so the vectors are clean for the scan by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15383
* Fix tests not to use compatibility version latest by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15361
* Fix Test introduced by new sampling by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15378
* Feature #12699: RANK Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15331
* [Fix] Uninitialised values in list_reverse by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15387
* [Dev] Check in `insert` if the InsertionOrderPreservingMap contains the key, do nothing in that case by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15385
* AFL++ Fuzzer Tests and Fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15329
* Fix RelationStatisticsHelper to estimate table filters correctly by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15308
* [PySpark] - Add broadcast function by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/15037
* feat: refactor getting tie_break_offset in SelectBestMatch by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/15235
* Added dashes to test case csv_buffer_size_rejects.test_slow by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/15398
* [Dev] Split last part of `ColumnDataCheckpointer::Checkpoint` into `FinalizeCheckpoint` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15388
* Fix JSON reader hang found by fuzzer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15397
* Better partition selection for external hash joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15389
* fix arm extensions ci by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15400
* Feature #12699: ROW_NUMBER Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15403
* Improve hash combining by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15408
* allow multifilereaders to delete entire chunks in FinalizeChunk by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15401
* Fix issue #14659 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15411
* Fix for issue #14648 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15409
* Re-enable some tests, removing `mode skip` or moving it later by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15488
* [Fix] Adjust reclaim space test to smaller block size nightly by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15414
* Feature #12699: CUME_DIST Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15413
* Fix issue with cleanup of buffers when reading same file multiple times by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15358
* [Fix] Track correct allocation size of evicted memory by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15433
* Fix internal issue 3813 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15427
* Exploit RFC_4180 to be more strict with newline settings by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15426
* Adds comment to Python Object + small adjustment do sniffer with comment detection. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15425
* Fix more nightly test errors due to sampling by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15423
* Type mismatch set operation  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15422
* Making the names option of CSV Files more restrictive when reading one file. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15431
* [Python][Dev] Lock `mypy` at 1.13 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15448
* Fix InFilter::ToString, visible via EXPLAIN ANALYZE for example by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15487
* Mention configuration option that avoids total string size error in error message by [@soerenwolfers](https://github.com/soerenwolfers) in https://github.com/duckdb/duckdb/pull/15489
* Fix the seed of RandomLocalState to be 64bit instead of 32bits by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15482
* Fix ADBC Leak when reusing statements by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15475
* chore: Add physical type translations for new timestamp types by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/15472
* [Dev] Slight cleanup of `assert.hpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15453
* Retain join partition order by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15460
* Use system threads for parallelism on read_csv if reading from pipe by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15461
* C API header generation for Go bindings by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14944
* Move InitSegment into roaring namespace (nit) by [@arjenpdevries](https://github.com/arjenpdevries) in https://github.com/duckdb/duckdb/pull/15495
* chore: Add header for g++15 compatibility by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/15509
* Functions can throw errors by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15166
* Improve candidate error message and relax constraint of rfc_4180 = false on quotes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15371
* Implement Union By Name on read csv relation by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15452
* Add behaviour to remove unescaped quotes of unquoted values by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15454
* [CSV Sniffer] If a column with Time/Date/Timestamp values encounter any other value, immediately go to VARCHAR by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15494
* Introduce 2 new platforms: `musllinux_arm64` and `musllinux_amd64` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15429
* 15128: failed to bind column reference for function under unnest. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15421
* Setting descriptions grammar by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15500
* Feature #12699: LEAD/LAG Secondary Sorts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15497
* Replace funcs copies with moves in sorted_aggregate_function.cpp by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/15442
* Re-enable iceberg extension by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15456
* Fix a binder issue with type aliases and foreign key constraints by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15517
* Properly ignore empty spaces after end of quotes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15522
* Fix window/test_window_wide_frame.test_slow after random() changes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15524
* Add atomic ptr class, use in ColumnData to protect Compression function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15518
* fix broken link by [@alexravenna](https://github.com/alexravenna) in https://github.com/duckdb/duckdb/pull/15532
* Various fuzzer fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15531
* remove duplicate FastMem copies in binary by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/15470
* [Julia] Improves Julia support for scalar UDFs by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15430
* Update year in license file to 2025 by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15545
* [Python] Align the behavior between `sql` and `execute` for `.pl()` call by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15537
* Don't create config folder on extension listing by [@lcostantino](https://github.com/lcostantino) in https://github.com/duckdb/duckdb/pull/15530
* Add `ExtensionTypeInfo` to `ExtraTypeInfo` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15373
* Fix some external join benchmark specifications by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15561
* Update progress_bar.cpp / drop DUCKDB_DISABLE_PRINT macro by [@meztez](https://github.com/meztez) in https://github.com/duckdb/duckdb/pull/15560
* Fix answers for benchmarks containing `random()` function by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/15562
* Make `max_temp_directory_size` round-trip by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15549
* Allow databases with table_macros to be copyable via COPY FROM DATABASE by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15548
* Allow a variable type `rowid` pseudocolumn in tables by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/14674
* Internal #3860: Deserialise Secondary Orderings by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15541
* Throw IO exception on 1.1.3 database file with incorrect dependency order by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15568
* Use ISNULL in conjunction or filters by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15529
* Avoid fast fail: change defaults to run all tests in more cases by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15558
* Asof join adds rows in specific case by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15567
* [Julia]: Auto-generate api.jl  (requires duckdb v1.2?) by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15474
* Implicit STRUCT to STRUCT cast for mismatching member names by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15477
* make test always fail in case of internal exception by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/15569
* CI: Bump container for Android build by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15577
* Fix #15526: CTE use operator type modified by intersect_all by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/15575
* [Julia]: Auto-generate api.jl with new order by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15580
* [Dev] `ColumnDataCheckpointer` can now checkpoint column data and validity data together by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15566
* Feature #12699: Secondary Sort Framing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15523
* [Test] More STRUCT cast tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15578
* Making RFC4180=True more reestrisctive when it comes to newline delimiters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15581
* In PhysicalInsert call FinalFlush before merging row groups into local storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15583
* HTTPFS test - no longer check for IS NOT NULL filter as this is no longer necessary by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15585
* Clean-up stack traces on MacOS, fix demangling on Linux, and add `EXPORT_DYNAMIC_SYMBOLS` flag which enables stack traces on Linux by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15587
* InternalException should only invalidate database when encountered during execution by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15588
* DuckFuzz Fix on Null parameters for both read_csv and sniff_csv by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15565
* Annotate errors in table macros with the call position of the table macro by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15590
* Line dependent buffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14512
* More bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15605
* csv_scanner: fix order of evaluation of arguments to a function by [@ProjectMutilation](https://github.com/ProjectMutilation) in https://github.com/duckdb/duckdb/pull/15609
* [Dev] Fix an unnecessary copy in Dictionary compression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15594
* [Julia] Fix incorrect types by [@tqml](https://github.com/tqml) in https://github.com/duckdb/duckdb/pull/15612
* Update URLs by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15617
* [Compression] `Dictionary` compression data now also includes the validity data by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15591
* Issue #14996: Aggregate Secondary Orderings by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15592
* Backport ENTRY_VISIBILITY from duckdb/extension-template-c by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15611
* Adjust list_reduce to use a 1-based indexing by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15614
* window: fix nullptr dereference by [@ProjectMutilation](https://github.com/ProjectMutilation) in https://github.com/duckdb/duckdb/pull/15610
* Improve reading duplicate column names in JSON by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15615
* Build/test/distribute linux_amd64_musl core extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15607
* Implement `simple_update` for `first` aggregate function by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15619
* Issue #15596: Infinite Value Checks by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15620
* Issue #15610: Wide Secondary Ordering by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15625
* Issue template updates by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15618
* [C API] Expose the DB instance cache in the C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15579
* File url scheme by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15563
* Fix an if statement that is always True by [@cclauss](https://github.com/cclauss) in https://github.com/duckdb/duckdb/pull/15630
* Issue #15597: Temporal Error Messages by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15635
* Parallel `union_by_name` for `read_json` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15593
* [Tidy]  create index info in static function for reusability by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15633
* [Arrow] Fix a bug related to ArrowArray lifetimes in the arrow scan code by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15632
* Not using Random Device in DuckDB Core by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15540
* Initialize random_seed to silence warning on uninitialized variable by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15649
* Cleanup the GitHub Action for Python by [@cclauss](https://github.com/cclauss) in https://github.com/duckdb/duckdb/pull/15643
* Added `weighted_avg` function using macro by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/15616
* Skip tests, cleaning up known failures in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15651
* Extension type modifier followup by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15638
* Index scan on (dynamic) table filters by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15410
* Feature #12699: Windowed Aggregate Ordering by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15634
* Make MemoryStream non-copyable by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15656
* Implement `DELTA_LENGTH_BYTE_ARRAY` and `BYTE_STREAM_SPLIT` encodings for Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15653
* Arrow Extension Type to be registered in DuckDB Extensions by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15285
* fix creating VARINT logical type in C API by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/15670
* Allow switching to a different catalog from a detached catalog by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/15624
* Logging by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15119
* TableCatalogEntry instead of DuckTableEntry in TableScanBindData by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15668
* Throw on unknown logging_storage set by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15681
* Remove mention to not existing logging_disabled_thread_local.benchmark by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15680
* [Dev] Remove the `CompressionValidity::NO_VALIDITY_REQUIRED` from `Dictionary` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15636
* [Dev] Fix wrong result reported by Roaring Compression `FinalAnalyze` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15677
* Fix Python dictionary key is repeated by [@cclauss](https://github.com/cclauss) in https://github.com/duckdb/duckdb/pull/15663
* Fix sign-compare compilation warning by [@dentiny](https://github.com/dentiny) in https://github.com/duckdb/duckdb/pull/15672
* Deploy bundled static libraries for OSX arm64 and amd64 by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15682
* Varint to varchar optimization by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/15521
* Nightly Fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15690
* Reduce test size so CI is less likely to fail by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15689
* Clean up temporary test directory in `run_tests_one_by_one.py` even if test segfaults by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15688
* Late Materialization Optimizer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15692
* [Fix] Make next_batch_index atomic by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15699
* Add late_materialization_max_rows setting that allows you to configure the threshold at which late materialization is triggered by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15697
* Default to BOOL on csv sniffer for files with only a header by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15701
* DatabaseInstance's destructor: avoid throwing (and not cleaning up) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15707
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15704
* Remove iceberg, again by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15716
* Allow shift-tab to be used to revert auto-complete suggestion, and implement SHOW [table] auto-completion by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15708
* [Dev] Fix alignment issue in Roaring compression method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15711
* Minor fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15715
* Move the DatabaseCacheEntry into the DBConfig, and set it before the constructor is called by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15714
* Patching comparison operators in ICU to actually return bool by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/15700
* Preserve stack trace information when re-throwing by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/15709
* [MultiFileReader] Extend support for column mapping from local -> global column by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/15446
* Fix Arrow extension type Locks by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15705
* Dont encode + on URL by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15693
* Print an error when using "duckdb -f [file]" on a file that does not exist by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15718
* Implement `parquet_version` parameter for Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15684
* [Testing] Temporarily skip tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15727
* Add NATIVE_ARCH option to compile using -march=native, and in the CLI time queries that are send through "-c" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15726
* Remove httpfs patch by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15729
* Fix #15659: VARCHAR parameters now count as STRING_LITERAL again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15724
* Parquet reader: fix for filter on file_row_number column by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15736
* Scan validity from dictionary vectors directly, and skip scanning validity when we encounter a dictionary vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15737
* Make entries field non-nullable for Arrow map type by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15733
* Properly set `external` flag again in `RadixPartitionedHashTable` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15728
* Storage version 65 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15702
* Enable index scan for dynamic IN filter by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15665
* Ignore pushes to version branches by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15743
* Move changes in v1.2 to main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15744
* Initialize create_index_info.catalog by [@philippmd](https://github.com/philippmd) in https://github.com/duckdb/duckdb/pull/15738
* Feature #15717: Window GROUPS by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15739
* Fetch only required columns in physical delete by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15746
* Add duckdb secret types function by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15564
* First round of extension bumps by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15655
* Move core_functions to use unity builds by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15753
* Add `disabled_compression_methods` setting that can be used to disable certain compression methods by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15754
* Add support for deserializing a list of SetOperations in the SetOperationNode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15755
* Feature #15717: Window GROUPS by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15761
* Check for mark join indexes in aggregate and group by by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15691
* Default end of binding to varchar and not bool in CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15747
* If arrow extension is not registered, use format information instead of failing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15749
* Merge 1.2 into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15769
* Fix CI for Linux Release Building by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/15748
* Merge changes in main into v1.2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15770
* When loading LogicalDependency from a database file or WAL file, modify the catalog to the catalog that we are loading into by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15767
* Fix minor DuckDB-Wasm problem with stacktraces, that would be shown twice by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15765
* Move the instance cache entry when configuring by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15768
* nitpick: Sequence Scan -> Sequential Scan by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15772
* Bundle MingW static library with the default extension configuration by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15774
* [Fix] Fix truncate + FK internal exception and another index bug by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15771
* Switch logging to macros by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15751
* Add back Iceberg extension by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15780
* Internal #4002: SQLite EXCLUDE Tests by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15785
* Skip 3 tests, to be reviewed on a side by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15790
* Add MD to autoload list by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15797
* Connection manager: make count available without a lock by keeping track of it with an atomic by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15798
* Add `STORAGE_VERSION` option that allows you to specify the target storage version when serializing a database by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15794
* Fix some memory/storage issues in CI by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15795
* Fix map_extract backwards compatability by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15799
* Fixes for vsize=2 tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15809
* Fix tests for storage 65 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15807
* Enable tests using no_alternative_verify by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/15806
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15812
* Fix dependency conflict in PK FK benchmark by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/15800
* Remove shuffle from sampling by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15703
* bump inet by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15804
* Fix `map_inference_threshold` issue in JSON reader by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15802
* [CI] Invert operations for Linux CLI: first deploy, then test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15820
* Fixup shell & autocomplete versioning information by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15823
* Skip end of test/sql/storage/parallel/insert_many_compressible_batches.test_slow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15814
* Attempted parquet warning fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15827
* Issue #15758: Streaming LEAD Buffering by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15834
* Removing all core code and CI related to the substrait extension by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15810
* CSV AFL Tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15805
* improve error messages for mismatching versions of extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15829
* dbgen: correctly join threads in case an error is thrown while generating data in parallel by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15840
* Do not change type of empty files, if the types were manually set by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15841
* Fix #15760 - when a SQL value function conflicts with an alias in the WHERE clause, prefer the alias by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15842
* Fix #15570: preserve alias when using bind_replace in table functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15843
* Fix CAPI chunk tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15846
* fix: Fix compiler warning for uninitialized access by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/15849
* Relax RFC_4180=False a bit more flexible by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15832
* More lenient test limits by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15845
* bump delta, remove patches by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15824
* enable autoloading for iceberg and delta for storage by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15822
* Fix get_current_time, today, current_date backwards compatibility by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15803
* Reset buffer before allocating a new one in `ResizableBuffer` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/15838
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15851
* [tpch] dbgen: Avoid throwing interrupt that can't be caught by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15856
* Add CI run testing also slow tests on PRs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15854
* More memory for external aggregate test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15861
* Fixes for nightly tests related to the CSV Parser by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15855
* Fix latest storage tests CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15863
* Fix duckdb_extensions() listing by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15858
* Use const T& and T instead of const T&& and T&& in (de)serializer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15866
* Make tests more lenient for smaller block sizes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15872
* Remove default in MultiFileReaderColumnDefinition constructor by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15871
* Fix spurious test/sql/copy/partitioned/partitioned_write_tpch.test_slow:53 error by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15869
* BindLogicalType should return a new type, instead of modifying an existing type in-place by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15868
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15875
* Issue #15877: CUME_DIST Moving Frame by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/15878
* Nightly CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15885
* Disable the RealNest benchmark nightly by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/15839
* disable iceberg tests by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/15883
* [Linux CI] Remove examples, already tested as part of OSX Release by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15879
* Fix fuzzer issue found by the DuckFuzzer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15886
* Avoid unnecessarily reading the string dictionary size when scanning uncompressed strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15887
* GCC-4.8 fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15884
* Several nightly CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15889
* Merge main into v1.2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15895
* When Deserializing, Sample Selection Vectors should be initialized to `FIXED_SAMPLE_SIZE` by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/15890
* Faster re-builds by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/15891
* Add missing ExpressionType::COMPARE_NOTEQUAL no arrow pushdown by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15892
* Fix race/deadlock in `FixedSizebuffer::Get()` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/15893
* Call ProcessError also for PendingQueries by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15899
* Removed unused variable in LoggingContext by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/15898
* CI: Handle 'fixed on nightly' label by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/15900
* CheckMagicBytes: zero initialise buffer by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/15902
* Rename RFC_4180 to STRICT_MODE. Change default to true. Use the same option in the sniffer as the parser. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15896
* Fix Arrow Type Registration on Extensions by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/15901
* V1.2 histrionicus by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/15909
* Use Arrow extension GetType() implementation when converting Arrow arrays by [@paleolimbot](https://github.com/paleolimbot) in https://github.com/duckdb/duckdb/pull/15813

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.1.3...v1.2.0

---

# v1.1.3 - v1.1.3 Bugfix Release <a id="v113"></a>

*Released on 2024-11-04*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.1.3)

This is a bug fix release for various issues discovered after we released 1.1.2. There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9.* can be read by this version.


## What's Changed
* [Adaptive Sniffer] In case files have only one row, be more permissive to detect headers and types. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14174
* Increase bounds for `test/sql/copy/file_size_bytes.test` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14367
* Use table-level locking when acquiring shared locks by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14370
* [Arrow] Fix scanning of BOOL columns when offsets are involved by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14395
* avoid unnecessary file list materialization when pruning readers by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14397
* Fixing type pushdown on the CSV Scanner by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14399
* Issue #14398: Lead Shift Defaults by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14409
* Escape should default to quoted by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14418
* Sniff CSV rejects options and small sniffer fix for ignore_errors by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14417
* Fix #14430 - throw an error when reading corrupt statistics in the perfect hash aggregate by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14442
* Use corrent container to produce BinderErrors by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14437
* Rework list_concat to accept a variable number of arguments similar to string concat by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14443
* SingleFileBlockManager::MarkBlockAsUsed - also erase from newly_freed_list to ensure trim does not prune blocks that are in-use by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14467
* acosh: Change example to avoid returning NaN by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14477
* Don't move lvalue when inserting in order preserving map by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14492
* bump vss by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14493
* Bug in percentage calculation in query_graph by [@bjornasm](https://github.com/bjornasm) in https://github.com/duckdb/duckdb/pull/14494
* fix: standardize usage of LogicalType::ROW_TYPE for COLUMN_IDENTIFIER_ROW_ID by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/14480
* [Python][Dev] Fix up test to work with older version by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14505
* Avoid throwing on failure to open extensions's .info file (when force installing) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14272
* Python 3.7 tests are particularly brittle, we will keep building wheels but avoid testing them by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14510
* Being more restrictive with the names option in the csv reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14466
* [Arrow] Fix issue where uninitialized memory was being read when scanning empty lists by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14538
* Fix #14545 - pivot header must be defined in the grammar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14556
* [Python][Arrow] Cast to `py::bytes` when dealing with BLOB in filter pushdown by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14553
* [Dev] Include aliases for RETURNING list expressions in `ToString` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14533
* CI: Mirror 'reproduced' / 'under review' to the internal repository by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14527
* Approx-Top K: Make aggregate state trivially destructible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14571
* Don't pre-initialize hash vector in DistinctStatistics construction by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/14570
* Fix query_graph tool for #14290 by [@JasonPunyon](https://github.com/JasonPunyon) in https://github.com/duckdb/duckdb/pull/14521
* Fix typos by [@deining](https://github.com/deining) in https://github.com/duckdb/duckdb/pull/14579
* [Dev] Traverse the `replace_list` of StarExpression in `ParsedExpressionIterator::EnumerateChildren` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14535
* chore: Add EOL to source files by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/14583
* Issue template: Add Swift redirect by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14588
* Fix for underflow issue on number of rows in the CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14587
* Cas strong by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14592
* HTTPFS: HTTPException no longer inherits from IOException by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14585
* [bufferpool] Fix PurgeAgedBlocksInternal() evictions by [@Vegetable26](https://github.com/Vegetable26) in https://github.com/duckdb/duckdb/pull/14446
* CI: Add bot for 'minimal reproducible example' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14598
* CI: Fix and simplify 'needs reproducible example' labelling by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14608
* CI: Fix and simplify 'needs reproducible example' labelling by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14609
* Enable serialization of LogicalExport by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14594
* Test fixes for new arrow release by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14593
* CI: Fix labelling bot by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14611
* CI: Add repo name to labelling script by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14612
* Unexpected result comparing blob by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14604
* Storage info update by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14371
* Fix #14600: use UUID to generate unique pivot enum names by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14622
* Fix #14601: avoid exporting entries in the temp or system schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14623
* Issue #14618: Year Day Year by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14624
* Fix #14542 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14610
* add index plan callback to IndexType by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14511
* FIX: Discrepancy Between Count and Sum Queries in SQL by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14634
* Fix Windows Extensions CI  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14643
* chore: Add qualification for brotli code by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/14628
* fix: Initialize atomic class member by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/14627
* Fix secret serialization issues by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14652
* Add serialization for bitstring_agg function by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14654
* Force error on CSV Sniffer Failure by [@lcostantino](https://github.com/lcostantino) in https://github.com/duckdb/duckdb/pull/14661
* bump vss + spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14667
* Bump extensions: AWS, Delta, Iceberg, INET by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14669
* fix scoping problem with function argument by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14666

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.1.2...v1.1.3

---

# v1.1.2 - v1.1.2 Bugfix Release <a id="v112"></a>

*Released on 2024-10-14*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.1.2)

This is a bug fix release for various issues discovered after we released 1.1.1. There are no new major features, just bug fixes. Database files created by DuckDB versions all the way back to v0.9.* *can* be read by DuckDB v1.1.2.

## What's Changed
* [CI] Re-enable ART zero initialisation verification by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14031
* Push filters instead of overwriting filters by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14078
* Fix test by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14079
* fix maximum_threads test inside containers by [@wenjun93](https://github.com/wenjun93) in https://github.com/duckdb/duckdb/pull/14083
* Fix: remove is_probe_in_domain by [@Light-City](https://github.com/Light-City) in https://github.com/duckdb/duckdb/pull/14084
* Add duckdb_extension.h to amalgamation release by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14086
* Bump minimum required cmake version by [@abramk](https://github.com/abramk) in https://github.com/duckdb/duckdb/pull/14089
* Fix parser error by removing alias by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14090
* [Dev] Move `EnumTypeInfoTemplated` definition into a `hpp` file by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14038
* Fix #14077: correctly reset next pointer when reconstructing new row group segment tree after vacuum by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14092
* Format CSV error messages by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/14097
* Fix the answer file for tpcds q67 at sf100 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14096
* Add v1.1.1 to version_map.json by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/14110
* CREATE TABLE now supports columns with `ENUM[]` types. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14102
* fix parquet cardinality when first file is empty by [@wenjun93](https://github.com/wenjun93) in https://github.com/duckdb/duckdb/pull/14058
* [Python Dev] Make sure the GIL is released when the connection+db are being shut down by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14113
* Less salt by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14173
* remove redundant code by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14172
* comparison of nested types returns true or false always (even with nulls) by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14094
* subtype DBInterface.Connection in julia client by [@piever](https://github.com/piever) in https://github.com/duckdb/duckdb/pull/14193
* [Python] Fix a bug with `python_scan_all_frames` reaching the bottom of the frame stack by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14183
* [Dev] Fix issue where the InsertStatement::ToString call destroyed the `alias` of the ValuesList by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14171
* [Python] Fix issue related to scanning float64 dtype columns that contain a mask by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14170
* Fix some warnings found while compiling duckdb-node by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13994
* fix minmax type info miss by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14159
* fix: ArrowSchemaMetadata::GetOption to return empty string instead of raising exception if key is not found. by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/14157
* Issue 14151: Fix conflicting defines on Windows hidden by cmake unity builds by [@zmajeed](https://github.com/zmajeed) in https://github.com/duckdb/duckdb/pull/14154
* Issue 14189: Fix build when threads are disabled by [@zmajeed](https://github.com/zmajeed) in https://github.com/duckdb/duckdb/pull/14190
* Fix an uncaught error with a generated column containing a subquery by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14198
* Add missing word in TableFunction comment by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/14210
* add method to check whether julia connection is open by [@piever](https://github.com/piever) in https://github.com/duckdb/duckdb/pull/14195
* Avoid schema changes with IF NOT EXISTS by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/14143
* Fix typos in code by [@c8ef](https://github.com/c8ef) in https://github.com/duckdb/duckdb/pull/14243
* [Dev] Add the ExecutorException class, making use of the EXECUTOR ExceptionType by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14231
* [Python] Don't allow construction of DuckDBPyType from empty Dict type by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14221
* Fix #14232: fix deliminator optimizer by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14238
* [CSV Reader] Also use figure-out-line code when ignoring errors. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14184
* remove redundant Bit::SetBit by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14226
* Fix #14212: mention correct query component when using literal in DISTINCT ON by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14255
* Removing overzealous check in Parquet by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/14268
* Update sqlsmith extension and patches by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/14270
* Support for duckdb.varint extension in Arrow. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14273
* Disable CSV ignore_errors benchmark by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14277
* Only slice initialized vectors in `PhysicalHashAggregate::SinkDistinctGrouping` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14289
* Fix #14249: return NAN when dividened is 0 by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14298
* Revert "Fix #14249: return NAN when dividened is 0" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14308
* fix macro name with the same function name in it which causing repeat… by [@Damon07](https://github.com/Damon07) in https://github.com/duckdb/duckdb/pull/14296
* Fixing issue with the sniffer on copy statetements by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14295
* Json bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14288
* [Bitstring] Add overload for `bitstring` to accept BIT as the type of the first argument by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14247
* [Fix] Don't initialize reference, constant, and parameter children in intermediate chunk by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14254
* Profiling - correct settings per node type and minor renaming for clarity by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14290
* Fix extension size increase by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14185
* Add option to ignore GeoParquet, disable spatial autoloading when reading GeoParquet by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14297
* More defensive programming in RowVersionManager::CleanupAppend by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14317
* Change Makefile to correctly handle DISABLE_SANITIZER and DISABLE_UBSAN by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/14316
* [CSV Reader] Making escape not limited to only quotes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14314
* allow external cardinality information (e.g. from iceberg) by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/14292
* [SecretManager] Fix deserialization of Value types in KeyValueSecret::Deserialize by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14332
* Avoid throwing InternalException on reading secret by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14336
* delay the rewrite of a large IN-clause into a MarkJoin on remote Filter-Scans by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/14266
* JSON reader - never generate maps if map_inference_threshold is -1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14348
* [Appender] Support appending to table with generated columns by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/14346
* Internal #3251: DateDiff Across Epoch by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14338
* Bump azure and delta extensions commits by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14350
* Bump spatial to 3f94d52aa9f7d67b1a30e6cea642bbb790c04aa2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14351
* Bump more extensions: iceberg, vss and sqlite_scanner by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14352
* Emit profiling info for extension operators by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14355

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.1.1...v1.1.2

---

# v1.1.1 - v1.1.1 Bugfix Release <a id="v111"></a>

*Released on 2024-09-24*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.1.1)

This is a bug fix release for various issues discovered after we released 1.1.0. There are no new major features, just bug fixes. Database files created by DuckDB since v0.9.* can be read by DuckDB v1.1.1.

## What's Changed
* [Python] Fix a crash related to handling of the `f_locals` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13821
* [Dev] Remove unnecessary parameter from BufferHandle constructor by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13823
* When vacuuming, immediately checkpoint the vacuumed row groups instead of scheduling a checkpoint task by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13825
* Check for unquoted errors after finishing up a buffer. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13826
* Issue #13813: TIMETZ Uninvertible Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13820
* add cardinality for cross product and propositional join by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/13818
* Add requested_schema argument to PyCapsule interface by [@WillAyd](https://github.com/WillAyd) in https://github.com/duckdb/duckdb/pull/13802
* Throw at double/float cast to decimal if it does not fit by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13745
* [Fix] C API - Correct type comparison in MAP value functions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13844
* [C-API Dev] Fix up `"Test DataChunk populate ListVector in C API"` test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13839
* [Dev] Minor cleanup to BufferManager and BlockHandle API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13838
* Small fixes for prompt of sniff_csv by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13843
* [BufferManager] Fix `duckdb_memory()` reporting wrong size for `temporary_storage_bytes` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13837
* Fix for internal error when using rejects tables and adding implicit cast for boolean values. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13849
* [Fix ART] Correct prefix transformation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13858
* [Python] Fix issue causing an exception when creating a `duckdb.StarExpression` without an `exclude_list` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13881
* Fix issue with cgroups/slurm variables: skip if memory limit cannot be parsed, and only run this on Linux by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13879
* Explicit windows-2019 instead of windows-latest by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13883
* CI/Windows: Drop redundant package by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13874
* Preserve operator in `BindWithCTE` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13873
* Update description of 'max_temp_directory_size' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13724
* 13810 unnest cross join error by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13878
* Tweak allocation purging by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13877
* Copy From Database - create a balanced UNION ALL tree instead of a depth-first union all tree to avoid stack overflows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13889
* [Python] Fix issue related to the GIL when using `execute` with multiple statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13893
* Fix #13880: correctly name http_proxy_password setting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13890
* Fix #13872: duckdb_result_return_type is not deprecated, and group together deprecated functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13891
* [Python] Add `python_scan_all_frames` to opt-in to scanning all frames (< 1.1 behavior) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13896
* Improve error on enums by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13885
* Handle extension ABI mismatches in a forward & backward compatible way by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13894
* Fix #13824: min() max() varchar column use default collation by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/13909
* Fix issue in casting 2 byte BIT -> BLOB by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13908
* add missing azure secret providers for autoloading by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13902
* Remove buffer_manager_allocate.patch and bump spatial by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13895
* [Python] Improve `install_extension` to support `repository`/`repository_url` and `version` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13876
* fix REGEX not supported anymore for valid queries (only statement error) #2889 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13633
* [CI] Invert operations on OSX.yml, deploying nightly artifacts before test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13927
* [Python][Jupyter] Don't use `ExplainFormat::HTML` for `explain('analyze')` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13928
* Only bind to SQL value functions if there is no alias with this name present we can bind to instead by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13925
* Improve logic for remote extension install on Windows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13929
* CI: Trigger actions for labeled discussions by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13937
* [Swift] Update README.md in Swift repo by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/13955
* [Dev] Add exclusion for `pybind11` internal `_pybind11_conduit_v1_` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13961
* Create a balanced union tree, also for export by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13956
* Increment julia version by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13966
* Fix #13585 - transform from or select first based on order specified by the user by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13959
* Fix Cross Product Cardinality by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/13954
* Do not run the date/timestamp format sniffer if they are set by the user by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13960
* Modify create_art_varchar.benchmark so it passes weekly regressions by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13968
* Fix data race when writing GeoParquet by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13962
* Check vector type in GetVectorScanType to avoid concurrent race when updating validity by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13965
* Parser Keyword Category Search by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13875
* Escape quotes in FTS by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13917
* Fix #13941: fix error message in appender by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13957
* fix: remove http prefix from proxy value when present by [@dylanspag-lmco](https://github.com/dylanspag-lmco) in https://github.com/duckdb/duckdb/pull/13973
* Use defaults when serializing copy to file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13978
* Fix #13933: disable join filter pushdown when a join is performed over collated columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13958
* Fix partitions on wide tables by [@piever](https://github.com/piever) in https://github.com/duckdb/duckdb/pull/13988
* [Fix] Throw exception for UNNEST in lambdas by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13969
* Fixing some parquet issues found by fuzzing by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13964
* fix julia partitions for streaming result by [@piever](https://github.com/piever) in https://github.com/duckdb/duckdb/pull/14000
* More descriptive Parquet created_by with version and source hash by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13992
* Decimal downcast limit check by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13922
* [C API] Add SQLNULL to the duckdb types by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13999
* Fix crash in the shell caused by printing blobs that failed to cast by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13983
* [Binding] Always try binding with the schema of the `UserType` first if it's set by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13995
* [Arrow] Only produce 'arrow.json' Extension types when `arrow_lossless_conversion` is enabled. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13989
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13982
* Disable swift linux tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14019
* fix minor typos in comments of aggregate function tests by [@era127](https://github.com/era127) in https://github.com/duckdb/duckdb/pull/14007
* [CSV Sniffer] Slight change of rules for dialect detection by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14013
* [Test Fix] Add noforcestorage to in-memory tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/14016
* Fix #14020: fix off-by-one in RLE compression: avoid flushing when last_seen_count == 0 which can happen if a column has exactly 2^16 (65535) repeated values by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14030
* Adds Julia support for scalar UDFs by [@drizk1](https://github.com/drizk1) in https://github.com/duckdb/duckdb/pull/14024
* Proper NULL handling in special json extraction functions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/14032
* Fix #13993 - avoid disabling optimizers for SET VARIABLE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14028
* [Arrow] Make unknown Arrow extensions throw at scan instead of bind by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14015
* Improve assertion macros by [@c-herrewijn](https://github.com/c-herrewijn) in https://github.com/duckdb/duckdb/pull/14033
* [Arrow] Move `ArrowUtil` to its own file by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13990
* [CSV Sniffer] Verify validity of header before value access by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14040
* Fix #14026: all TIMESTAMP_xx cannot cast to TIME directly by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/14045
* Only merge distinct stats if both sides have distinct stats available by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14046
* Avoid http-redirect in README by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14029
* fix: make ArrowArrayWrapper::GetNextChunk() virtual  by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/14003
* Issue #13655: MEDIAN Even Tests by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13722
* Fix #13934: use CreateSortKeyWithValidity to correctly handle NULL in all calls to arg_max by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14053
* Upgrade MySQL/Postgres extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/14054
* [Union Reader] Early-out on readers of files that do not have data by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14050
* Issue #13899: AsOf Unrelated Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13975
* Feature #3128: 2024b Time Zones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/14061
* bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/14062
* Fixup StagedUpload invocation via workflow_call by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14065
* Skip polars test in 3.7 due to missing PanicException by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14066
* Add building, testing and distributing for Python 3.13 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14067
* bump sqlsmith and azure versions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/14069
* bump substrait by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/14055
* CIBW_SKIP also musllinux on Python 3.7 or Python 3.8 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/14074

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.1.0...v1.1.1

---

# v1.1.0 - DuckDB 1.1.0 "Eatoni" <a id="v110"></a>

*Released on 2024-09-09*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.1.0)

This release of DuckDB is named "Eatoni" after Eaton's pintail (Anas Eatoni) from the southern Indian Ocean.

Please also refer to the announcement blog post: https://duckdb.org/2024/09/09/announcing-duckdb-110

## What's Changed
* Add feature changes back in by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11146
* Make `MultiFileReader` filename configurable by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11178
* [Dev] Fix compilation issues on `feature` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11082
* add query() and query_table() functions by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/10586
* [Block Size] Move the block allocation size into the block manager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11176
* LIMIT pushdown below PROJECT by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/11112
* BUGFIX: IN () filter with one argument should translate to = filter.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11473
* Regression Script should calculate micro benchmark differences with the correct base branch by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11762
* Pushdown filters on window partitions by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10932
* Arrow ListView Type by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10766
* Add scalar function support to the C API by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11786
* Add TopN optimization in physical plan mapping by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/11290
* Join-dependent filter derivation by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11272
* Implement `ROW_GROUPS_PER_FILE` for Parquet by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11249
* Prefer Final projected columns on probe side if cardinalities are similar by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11109
* Propagate unused columns to distinct on by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11006
* Separate eviction queues by `FileBufferType` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11417
* Disable false positive for vector size nightly in test by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11953
* Rework jemalloc extension by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11891
* Tweak jemalloc config by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12034
* Httpfs test to nightly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12196
* Removed three reinterpret casts and some rewriting by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12200
* Begin Profiling Rework to move towards Modularity by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11101
* [CLI] Add highlighting + limited auto-complete for shell dot commands by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12201
* Skip test to fix block size nightly and add more explicit error checking by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12211
* Remove BLOCK_ALLOC_SIZE from the column segment files by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11474
* [Julia] - Added optional `schema` input argument to `DuckDB.Appender` constructor by [@curtd](https://github.com/curtd) in https://github.com/duckdb/duckdb/pull/12174
* Fix Mark Index in the Bound Join Ref by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12263
* Fix for CI Regression Failure by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/12273
* 🦆 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12303
* Disable `JEMALLOC_RETAIN` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12185
* Enforce compression extensions for CSV Files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11903
* Make spuriously failing test more robust by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12306
* Add new extensions to issue template by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12313
* [Fix] Block size nightly run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12283
* Spell Check | Nothing Major | Corrected base_scanner.cpp by [@nj7](https://github.com/nj7) in https://github.com/duckdb/duckdb/pull/12282
* add duckdb_bind_timestamp_tz function to C API by [@karlseguin](https://github.com/karlseguin) in https://github.com/duckdb/duckdb/pull/12151
* [Python] Add some date/datetime functions to pyspark api by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/12075
* Fixes to Windows workflow and ubuntu_18 action by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12308
* [Extension Dev] Forward declare re2 in `hive_partitioning.hpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12302
* add expected errors to test/sql/copy/per_thread_output.test by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12280
* Issue #12287: ICU Strptime Lists by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12295
* Issue #12171: Streaming Window FILTER by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12250
* [Python] Update the Connection wrapper generation, now generates c++ code by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12216
* Use iterator buffer position when storing buffer handles by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12315
* Bump Julia client to v0.10.3 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12323
* Fix #12286 - in the MetadataManager, prefer to allocate new blocks if the next free block id is smaller than the currently used metadata block by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12318
* [Fix] Only read file size if file handle still exists by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12319
* Add support for APPEND argument to hive partitioned write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12262
* Remove all reinterpret casts from the transformer by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12320
* Additional check for overlapping CTE names by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12305
* [Dev] `STANDARD_VECTOR_SIZE` and `BLOCK_ALLOC_SIZE` can now be set through the Makefile by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12164
* [Upsert] Fix issue with lambdas in `DO UPDATE SET` expressions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11866
* [Python] Fix scoping issue for `pandas_analyze_sample` setting by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11706
* Support REGEX matches expected error message by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12327
* Allow run_fuzzer to reduce multi statements.   by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12278
* Fix #12328 - when flattening STRUCT vectors with NULL values, we need to flatten the children recursively as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12332
* Make `dbgen` generate data in parallel by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12337
* dbgen: skip parallel generation if DUCKDB_NO_THREADS is set by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12341
* Add prefix prefix_front_back. to get prefix_front_ and prefix_back_ by [@liujiayi771](https://github.com/liujiayi771) in https://github.com/duckdb/duckdb/pull/12344
* Issue #12171: Streaming Windowed DISTINCT   by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12311
* Update README by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12357
* [CSV Reader] [Skip Option] Tests and fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12213
* Adjust BM25 score in FTS extension to prevent negative scores by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12356
* Fix typos by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12360
* Fix #12293 - accept NULL values in generate_series with timestamp by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12367
* Fix #12335: avoid calling fsync when writing Parquet files, instead just close the file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12371
* Fix parameters passed down to other workflows in OnTag.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12369
* [Python] Fixes for the SQLLogicTest runner implementation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12372
* Bump julia to v1.0.0 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12379
* Fix #11921 - varchar -> timestamp casts are not invertible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12376
* Upgrade utf8proc - and move our custom extensions out of utf8proc itself by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12373
* change max_queries number back to 2000 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12375
* Remove sqlsmith extension by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12300
* Reorder semi and anti joins. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11815
* Issue #12351: implicit cast to `TIMESTAMP_MS`, `TIMESTAMP_S`, `TIMESTAMP_NS` from `DATE` values by [@akoshchiy](https://github.com/akoshchiy) in https://github.com/duckdb/duckdb/pull/12352
* Issue #10023: Approx_Count_Distinct Memory Usage by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12355
* Fix a small typo in dev instructions for swift setup by [@gjmwoods](https://github.com/gjmwoods) in https://github.com/duckdb/duckdb/pull/12383
* Release lock before returning `BufferHandle` in `StandardBufferManager::Pin` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12391
* Remote attach autoload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12393
* Add JSON type to Parquet reader/writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12222
* Add `RETURN_FILES` parameter to `COPY TO` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12220
* Updated JoinHashTable to use linear probing to resolve hash collisions by [@gropaul](https://github.com/gropaul) in https://github.com/duckdb/duckdb/pull/11472
* [Benchmark Runner] Add `--disable-timeout` flag by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12387
* Don't replace unicode spaces within `$$` quotes in query strings by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12405
* [Python] Fix fatal exception caused by empty Pandas Categorical objects. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12370
* Release CSV Blocks when acquiring new blocks if single threaded by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12409
* Add support for prefetching multiple adjacent blocks in a single batched read when attaching to remote databases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12413
* MatchRegex() fixed to do not return false positive result by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12396
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12392
* [C-API] Catch exception in `duckdb_execute_prepared` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12414
* Combining LIST_CONCAT and CONCAT binding  by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/12317
* [Appender] Add `AppendDefault` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11905
* [Python Dev] Push CTE internally for every (python) replacement scan that occurred. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12161
* Improve compiler compatibility by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/12401
* Write zero-length list offsets for NULL values when serializing vectors by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12423
* Get column statistics if Logical Get has a statistics function by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/12424
* jemalloc: Identify GNU source code properly by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12420
* Avoid parallelizing LIMIT clauses when the query plan is simple by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12433
* Prefetch metadata blocks for remote files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12437
* [Jupyter] Remove width limit on the BoxRenderer config by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12443
* Revert duckdb/duckdb#10865 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12426
* inline delta by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12435
* Account for _tagged_ dollar-quoted strings when stripping unicode spaces by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12421
* Work-around for broken github windows runner by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12447
* Prevents clearing of the types of the LogicalExecute operator by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/12436
* Add support for BEGIN TRANSACTION READ ONLY by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12202
* Make `range` and `generate_series` table in-out functions, and fix several issues with table in-out functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12431
* Issue #12412: AsOf Filter Push by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12448
* [Fix] Block Size Nightly by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12427
* [ART] Remove Flatten and template key generation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12428
* [Python] Clean up internals of `execute` / `executemany` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12434
* By default attach remote databases as READ_ONLY by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12461
* Fix #11837: use internal physical type for FIRST/LAST/ANY_VALUE instead of logical type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12462
* Issue #12464: Windowed Order By All by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12470
* Specialize `list_value` for primitive types for significantly improved performance by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12468
* [Dev] Remove dead code from `PhysicalBatchCopyToFile` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12459
* Disable Windows extensions CI until Github actions runners are fixed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12479
* [Fix] access_mode now lives in AttachOptions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12482
* Internal #2186: Nanosecond Functionality  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12440
* [C-API] Fix leak in `duckdb_create_config` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12465
* [Python] No longer scan the entire frame lineage in a replacement scan, added option to disable (python) replacements entirely by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12425
* throw binder error for comment on system catalog by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12486
* Parquet reader performance by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12478
* Operators the Optimizer can skip by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12489
* Fixes clang conversion warnings by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/12467
* Avoid creating internal schemas as non-internal when reading old database files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12456
* Allow parquet encryption/decryption keys to be passed in as base64 encoded strings by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/12445
* [Block Size] Introducing CompressionInfo by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12481
* add the number of filtered files to explain by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12488
* Implement Map Type Detection for JSON Reader by [@ZiyaZa](https://github.com/ZiyaZa) in https://github.com/duckdb/duckdb/pull/11285
* [Dev] Remove busy-spin from `ClientContext::ExecuteTaskInternal` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12483
* Pluggable collations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12492
* [Dev] Don't fail `make generate-files` if the python code generation fails by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12500
* Optimize `EXTRACT(year/month/day FROM date/timestamp)` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12499
* [Fix] Remove BLOCK_ALLOC_SIZE in the single file block manager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12502
* Revert Windows CI fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12510
* Fix duckdb/duckdb#12467 changes to covariance calculation by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12515
* [Python] Fix reading strided `datetime` and `timedelta` columns by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12519
* Add method for decoding sort keys, and use this in min/max for arbitrary types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12520
* Reduce allocations & use predication in ColumnSegment::FilterSelection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12521
* Skip only built-in optimizers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12522
* Improve min/max performance for strings and fallback types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12524
* Move arg_min/arg_max to use sort keys  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12525
* Move FIRST/LAST/ANY_VALUE to use sort keys  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12526
* CMake: use GNUInstallDirs as defaults for INSTALL_{BIN,LIB,INCLUDE}_DIR by [@paparodeo](https://github.com/paparodeo) in https://github.com/duckdb/duckdb/pull/12509
* More formatting and fix to stddev by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12516
* Linux Extensions CI: Attempt at fix missing dependencies by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12429
* Fix checkouts by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12366
* Etag if none match for extension install by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12333
* [Block Size] FixedSizeAllocator, MetadataManager, PartialBlockManager by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12514
* [Python] Skip the PandasAnalyzer if dtype is `'string'` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12511
* [StreamQueryResult] Batched variant of the StreamQueryResult collector by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11494
* Move many tests to slow by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12534
* Add support for `arg_min(ANY, ANY)` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12532
* Avoid overriding types in PrepareTypeForCast when not required by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12539
* Support all types in `histogram` function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12538
* [Python] Remove busy-spin during execution by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12512
* [Block Size] String space constant by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12537
* Use string_t instead of std::string in histogram by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12545
* Add support for binned histograms by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12548
* [Upsert] Fix RETURNING for `DO NOTHING` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12554
* Build Android Binaries by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12550
* [CI] Remove pyarrow version lock by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12566
* [Dev] Change tests: np.NaN -> np.nan by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12565
* Internal #2017: DECIMAL Downcast Rounding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12036
* Issue #12204: Summarize Temporal Quantiles by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12297
* Internal #2186: Nanosecond StrTimeFormat by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12551
* Add support for `equi_width_bins` function to compute histogram boundaries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12574
* add support for casting 'yes'/'no' strings to boolean values by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/12501
* Julia: Add chunked results with Tables.partitions() by [@frankier](https://github.com/frankier) in https://github.com/duckdb/duckdb/pull/12395
* [PySpark] - Allow spark session range by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/12346
* [PySpark] Implement subset drop duplicates by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/12348
* ICU noaccent collation by [@tiagokepe](https://github.com/tiagokepe) in https://github.com/duckdb/duckdb/pull/12170
* Implement Brotli compression for Parquet reading & writing by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12103
* [FriendlySQL] Unpacked COLUMNS() Expression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11872
* [PySpark] Implement UDFRegistration.register method on PySpark api by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/12179
* [Python] Don't use `np.nan`, deprecated alias starting with NumPy 2.0 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12583
* Add `bind_expression` callback to scalar function, and use it to turn `typeof` into a `BoundConstantExpression`  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12580
* Add `can_cast_implicitly` scalar function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12581
* Add support for `histogram` and `histogram_values` table macro, and add support for default table macros (similar to how we support default macros) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12590
* build: swap libclang for cxxheaderparser by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/12567
* [C-API] Add `table_description` struct to query various information about the table. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12460
* Change new micro benchmark script to only look for `.benchmark` files by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/12598
* Add HTTP error code to extension install failures by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12608
* Separate WAL write from commit, and allow writing to the WAL without holding the transaction lock by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12261
* Add `OwningStringMap` - and rework `histogram` and `mode` functions to use this by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12601
* Feature #1272: Window Executor State  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12573
* Add support for any type to `mode` aggregate by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12619
* WAL - when dropping a table, also delete any transaction local storage associated with that table by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12603
* [Python] Allow Generators to be passed where List is expected by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12602
* VectorOperations::Copy - fast path when copying an aligned flat validity mask into a flat vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12618
* Move android CI to only run during nightly CI triggers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12622
* Add initial support for GeoParquet + Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12503
* Issue #12600: Streaming Positive LAG by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12609
* Feature #1272: Window Group Preparation   by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12628
* Minor window improvements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12617
* Merge feature into main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12633
* Refactor `quantile` aggregate - clean up code & support `quantile_disc`/`median` for all types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12630
* Feature 1272: Window Payload Preallocation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12629
* [ART] Configurable index scan threshold by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12635
* Subtract start offset for when fetching array child segment by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12639
* Remove custom logic to detect main vs feature by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12643
* Do not quote fields with space in the CSV output mode by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12644
* Use lowercase in 'html' output mode by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12612
* Internal #2361: Window ROWS Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12652
* Quantile: Fix variable used only in D_ASSERT by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12642
* Skip pytorch test, it fails spuriously in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12645
* Add `histogram_exact` function that adds values to bins only if they match exactly, and add `other` column that contains values that do not fit in any bin by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12650
* Add operator hook for sink progress by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12637
* Regression workflow on newly introduced benchmarks: remove for now by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12659
* Fix #12646 - allow SQL value functions in HAVING by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12654
* Add != operators on string_t and interval_t by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12658
* fix: improve C scalar functions API by [@rustyconover](https://github.com/rustyconover) in https://github.com/duckdb/duckdb/pull/12663
* Add `approx_top_k` aggregate based on the (Filtered) Space-Saving algorithm, and use it in histogram by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12653
* Fix std::sort requirements, from greater_equal to greater by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12669
* fix(parquet): two-complement zeroes check on FIXED_BYTE_ARRAY encoded DECIMAL (#12621) by [@fedefrancescon](https://github.com/fedefrancescon) in https://github.com/duckdb/duckdb/pull/12655
* [CSV Reader] Reorder of Columns for CSV Scans on multiple files. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12288
* [CSV] [Bug-Fix] Fix for issue related with single-threaded execution and null padding. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12679
* [Block Size] String block limit and a few other places by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12671
* Rework arena allocator allocation policy - and increase pivot threshold by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12690
* Julia - Fix Base.isopen(db::DB) in https://github.com/duckdb/duckdb/pull/12700
* [CLI] Limit history size to 100MB, and avoid writing invalid UTF8 to the CLI history by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12677
* Add configurable thresholds for using nested loop join and merge join by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12689
* Prevent unnecessary usage of `std::string` in `list` aggregate - and use more efficient `memcpy` for batched copy by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12694
* Dont load spatial unless geoparquet metata is present by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12692
* Serialization: add CustomData and better support for integrating with extensions by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/12681
* Removing ODBC driver by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12706
* Support thousand separator for floating point numbers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12717
* [Python] Use non-owning references to hold created cursors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12711
* LIST(VARCHAR) - reduce memory usage by avoiding allocation of nullmask for string data, and allocate larger initial batches by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12705
* [CSV] Bug fix for race condition in single-threaded multifile reader + properly print paths on union_by_name errors. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12697
* Issue template: Add ODBC and Node (neo) clients by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12714
* Shell: add .sql suffix to temporary file created with \e by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12723
* Partitioned write - keep only up until 100 files open, when this limit is exceeded close the file and create a new file if more data for this partition appears by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12708
* Change setting types to fix warnings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12724
* Avoid unnecessarily copying child expression when binding COLLATE statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12725
* Support for variadic arguments in scalar UDFs in the C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12678
* [Relation API] Dont push DISTINCT modifier for EXCEPT/INTERSECT ALL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12599
* Builds for Windows on ARM64 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12586
* Rework `union_by_name` so that files are no longer kept open by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12730
* Fix #12729: early-out when checking for perfect hash joins when running on empty tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12731
* CLI: Replace \n with \r\n again in history again by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12735
* Fix #11228 - add support for unsigned integers in printf/format by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12736
* Various CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12737
* Add repeat(LIST[], INT) that allows repetition of lists similar to how this is allowed in Python by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12738
* [Python] Add missing options to `read_json` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12732
* Add support for fetching cardinality estimation and stats through a multifilelist by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12740
* Fixes warnings detected by cppcheck by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12745
* [Arrow] Add `ArrowQueryResult` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12496
* [Dev] StreamQueryResult internals cleanup by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12636
* ALP/ALPRD: correctly skip when we are skipping fewer values than in a vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12753
* Maintain prepared statement parameter types explicitly instead of converting into literals by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12759
* CLI .changes: use sqlite3_changes64 and sqlite3_totalchanges64 to prevent overflows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12761
* Fix #12569: avoid truncating zeros that matter in format function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12762
* Fix #12418: Remove .lint command in SQLite shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12763
* Fewer system calls in LocalFileSystem::ListFiles by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12769
* Support indexes in `COPY DATABASE` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12768
* Issue #12600: Batched LEAD/LAG by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12770
* Issue #12600: Streaming Positive LEAD by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12685
* Add dl functionality for Windows by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/12765
* Fix stale bot permissions, with [@szarnyasg](https://github.com/szarnyasg) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12782
* [CI] Stale bot: actually add permissions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12786
* Fix `FILE_SIZE_BYTES` test (again) by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12779
* Fix extended tests in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12781
* Patch CentOS 7 EOL causing CI failure by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12788
* Allow extensions to optionally add own description (on load) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12754
* Internal #2429: Shifted LEAD NULLs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12791
* Issue #12784: Months Before Days by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12794
* bump vss by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12797
* Remove centos workaround by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12801
* For compressed deletes in the undo buffer - count the actual size that will be written to the WAL when determining the auto-checkpoint threshold by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12803
* feat: new inet functions by [@panga](https://github.com/panga) in https://github.com/duckdb/duckdb/pull/12575
* [Dev] Make`Executor::ResultCollectorIsBlocked` less trigger-happy by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12780
* Fix #12798: Add head file to fix debug build incomplete type error by [@zzachimed](https://github.com/zzachimed) in https://github.com/duckdb/duckdb/pull/12810
* [Block Size] Switching to configurable block sizes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12691
* [Dev] Clean up the `generate_serialization.py` script a bit by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12823
* Remove micro extended from duckdb/duckdb by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12792
* [Python] Allow `pathlib.Path` to be provided to `duckdb.connect` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12809
* remove .py scripts migrating to the sqlsmith by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12827
* Some expected error messages added by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12825
* [Fix] list_resize by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12832
* [Python] Python SQLLogicTester maintenance by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12833
* [Python] Accept a list of `Expression` objects in `DuckDBPyRelation.aggregate` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12812
* [Copy Database] Don't include generated columns in the copied data by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12835
* [Julia] Added Appender support for `Int128`, `UInt128`, and `Base.UUID` values by [@curtd](https://github.com/curtd) in https://github.com/duckdb/duckdb/pull/12836
* [Python] Fix extraction of days/seconds/microseconds from `timedelta` object by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12760
* [Python] Output a regular key -> value dict for hashable keys by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12734
* [Dev] Change internals of `StringUtil::GenerateRandomName` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12806
* [CSV] Adaptive Sniffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12698
* Fix LinuxRelease.yml after bump to Node 20 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12850
* Fix: Reduce repeated judgment in ties[i]. by [@Light-City](https://github.com/Light-City) in https://github.com/duckdb/duckdb/pull/12840
* add html_escape and html_unescape functions in inet extension by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/11191
* Fix union struct implict cast by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12847
* Update httplib from v0.10.2 to v0.14.3 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12849
* Fix an issue where parameters would be promoted to `NULL`, incorrectly causing `PREPARE` to fail by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12844
* More expected error messages added by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12846
* Overload `MIN/MAX/MAX_BY/MIN_BY` to return the "top" `N` values by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12834
* Fix #12789: list_zip support array  by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/12859
* [Python] Fix missing ConnectionException errors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12864
* Make equi_width_binning buckets even nicer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12878
* Add a JSON pretty print function by [@PhictionalOne](https://github.com/PhictionalOne) in https://github.com/duckdb/duckdb/pull/12398
* Add Metrics Support in the CAPI by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/12498
* Update issue template by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/12880
* Fix regression in Parquet reader `TryOpenNextFile` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12848
* Improve performance of memory usage counters by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/12751
* [Fix] No String Inline / Destroy Unpinned Blocks nightly run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12884
* Fix LinuxRelease.yml CI by avoiding upload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12891
* Do not depend on manylinux extension in Python's CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12895
* [Dev] Fix failing test in `test_relation_api.cpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12894
* [Dev] Skip `test_run_pandas_with_tz` on pandas <2.0.0 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12896
* Fix #12688: Julia SubString handling by [@dhanak](https://github.com/dhanak) in https://github.com/duckdb/duckdb/pull/12899
* [Python-Dev] Add `DependencyException`, throw earlier if `PendingQuery` fails by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12888
* [Fix] Mixing block sizes and compression functions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12858
* Fix issue with list radix serialization by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12887
* Respect limit during join order by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12851
* [CHORE]: Fix minor SQL test case by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12909
* Fixes for duckdb_constraints and information_schema constraint tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12914
* [Postgres Compatiblity] Support `=>` to supply named parameters to functions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12913
* Pushdown table filters into probe based on min/max data found during hash build of hash joins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12908
* Count nulls when detecting JSON structure by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12883
* Fix #12870 - improve error message when encountering schema mismatches in COPY tbl FROM file.parquet by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12918
* Use different versions of snappy depending on the compiler by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12889
* Fix Issues with type detection for Doubles/Floats/Decimals by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12866
* Pass 'Unsecure_node_version' to allow node16 for a bit longer by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12922
* Minor refactor for window_executor by [@ZhangHuiGui](https://github.com/ZhangHuiGui) in https://github.com/duckdb/duckdb/pull/12924
* ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION:false for Android and Nightly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12930
* [Fix] Vector verification for dictionary expressions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12890
* Return smaller cardinality for Top N operator by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/12932
* Make GCC Happy Again by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12937
* [Fix] More robust parquet metadata test by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12935
* Rework table filters, and for each row group only execute table filters if they can actually filter out any rows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12938
* Issue #12941: Window Constant Results by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12943
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12927
* Make `ErrorData::Message()` and `ErrorData::RawMessage()` const by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/12885
* Feature #1272: Window Parallel Sink by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12907
* [Arrow] Add `PhysicalArrowBatchCollector`, a batched result collector for the `ArrowQueryResult` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12787
* [Python] Rework internals of object registration by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12625
* [StreamQueryResult] Add `ExecuteTask` method to StreamQueryResult by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12824
* Fix several CTE related issues by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/12948
* Label mark joins with convert to semi by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12916
* [Julia]: Added `FixedDecimal` support to Appender API by [@curtd](https://github.com/curtd) in https://github.com/duckdb/duckdb/pull/12923
* Pushdown dynamically generated filters into `MultiFileList`, allowing partitions to be pruned by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12955
* Automatically materialize CTEs by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12290
* Move checkpointing parallelism into `TaskExecutor` class, use that class for parallel `union_by_name` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12957
* [Dev] Uncouple `HTTPState` from core by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12912
* [Dev] Clean up TreeRenderer code by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12716
* Swap build side and probe side base on cardinality AND width of build side. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12755
* [Python] Use `Set` instead of `List` for the `get_table_names` stubs by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12963
* Feature #1272: Window Validity Array by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12954
* [CSV Reader] Make glob reading more permissive to errors if ignore_errors is set by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12966
* [Python] Convert ENUM to `np.array` instead of `pd.Categorical` for `fetchnumpy` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12964
* Several hive partitioning fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12970
* fix incorrect int32 appender by [@piever](https://github.com/piever) in https://github.com/duckdb/duckdb/pull/12956
* Add missing TransformCTE extraction to TransformRecursiveCTE by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/12968
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12969
* Add Pyodide 0.26.1 (corresponding to Python 3.12) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12965
* Avoid adding a suffix to Parquet files when doing a partitioned write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12972
* URL Encode/Decode Hive Partitioning Columns/Filters + add url_encode/url_decode scalar functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12974
* Fix JSON extension Cmake by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12975
* Clarify when it's necessary to refresh data and validity pointers by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/12973
* Added new information_schema views - closes #4343 by [@prmoore77](https://github.com/prmoore77) in https://github.com/duckdb/duckdb/pull/12942
* Use jaro winkler similarity for finding similar entries in catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12980
* Internal #2503: Streaming Window Reset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12984
* Fix #12933: maintain insertion order in window when the window clause is empty (i.e. over ()) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12982
* Feature #1272: Window Constant Sink by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12979
* Remove special case for '+' in URLs in httplib by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12929
* Rebind prepared statements based on catalog versions by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/12829
* Allow string stats larger than our default for parquet row group pruning by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12928
* Add work-around for R client table function initialization back in under a config setting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12990
* [Dev] Add getters/setters for the 'column_ids' of a `LogicalGet` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12971
* Accelerate Parquet en/decryption with HTTPFS extension by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/11720
* remove deprecated CDN invalidations by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12997
* add large ingestions by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/12949
* Fix shared_ptr issues in RowGroup and add locks to WAL initialization by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13000
* Add the ANY type and special null handling to the C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12785
* Improve error messages in the presence of subqueries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13001
* Case-insensitive `NULL` casting in `VARCHAR` -> `STRUCT` casts by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13003
* `TemporaryMemoryManager` improvements by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12931
* Make sure that empty and only white space headers have same treatment by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12994
* Push timestamp_tz to do direct casting if ICU is not loaded by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12993
* [Dev] Add `query` to QueryRelation for logging by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13004
* [Spark API] Fix group by compatibility issues by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13005
* [CSV] Progress Bar for compressed files. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12728
* Disable fixed size map in `PartitionedTupleData` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13013
* Fix parallel creation and destruction of instances through the `DBInstanceCache` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13010
* Avoid generating join filters for interval columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13014
* Extend least/greatest to support all types, and always return the same type as its input types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13019
* Add sha1(varchar) -> varchar scalar function by [@bradlarsen](https://github.com/bradlarsen) in https://github.com/duckdb/duckdb/pull/13020
* Decimal to FloatingPoint: Avoid losing precision by splitting operation in two, more fixes and tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12627
* Feature #1272: Segment Tree Finalize by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13002
* Create Delimiter Join and Delimiter Get via Relations by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12953
* Fix CTE/noalternativeverify issues by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13024
* Fix bug in reworked `fixed_size_map_t` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13023
* Fix abs for floating point negative zero by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13025
* [Nightly-Bug] [CSV Reader] Use strings on header detection by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13028
* Release GIL during DB instantiation by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/13029
* GCC 4.8: add noexpr to 2 constructors by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13030
* Fixes for LogicalType::ANY and fixed_size_map by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13035
* [Nightly] Fix for arrow appending fixed size lists by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13039
* fix storing persistent secrets in home dir by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13033
* Internal #2534: IGNORE NULLS Threading by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13050
* [Julia] Only commit transaction on non-error (compat) by [@genericallyterrible](https://github.com/genericallyterrible) in https://github.com/duckdb/duckdb/pull/13049
* Improve EXPLAIN output of Delim Joins and Delim Gets by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/12995
* Make client reuse threadsafe by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13052
* Only remove the first occurrence of extension prefix by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/13057
* Fix incorrect overflow in left shift of unsigned number by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13056
* Add tests for sha1 function by [@bradlarsen](https://github.com/bradlarsen) in https://github.com/duckdb/duckdb/pull/13064
* [Relation] ViewRelation could be created without an alias by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13054
* Support IN operator for LIST by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12920
* [Python] Read from file-like objects with `read_json` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13040
* [Python] Fix lifetime issue with MaterializedRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12998
* PySpark sort by columns and DataFrame.getitem by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/12981
* Fix trouble to compile with MSVC by [@annnei](https://github.com/annnei) in https://github.com/duckdb/duckdb/pull/12579
* Create a dedicated `RegisteredStateManager` that manages client context states in a thread-safe manner by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13027
* DEBUG_STACKTRACE should not be enabled for release builds by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13070
* Add blob overloads to crypto functions, and turn md5_number_lower and md5_number_upper into macros by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13068
* Internal #2534: IGNORE NULLS Threading by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13065
* Variable Integer Size Type by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13015
* Simplify binding of CALL statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13074
* Fix #13045: flatten in list_inner_product by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13076
* Fix for unpivot on zero columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13073
* Add support for overloading to macros by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13062
* Internal #2534: Windowed FILTER Threading by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13086
* Fixup #12579, remove pessimizing std::move by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13089
* [CSV Reader] Fix when reading overbuffer values of csv files with extra delimiter by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13081
* Making error messages more clear for new line delimiter errors by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13082
* [CSV Sniffer] Sniffer can now sniff files with extra delimiters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13083
* Remove test in Pyodide due to weird pandas interactions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13091
* Add support for SQL-level variables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13084
* Fix wasm CI and add missing template argument by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13094
* Some clang tidy fixes around narrowing casts by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13105
* chore: PushdownAggregate fast path by [@lichuang](https://github.com/lichuang) in https://github.com/duckdb/duckdb/pull/13098
* - fix list_distance & list_cosine_similarity execute fail when list i… by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/13090
* [Explain] Add `EXPLAIN (FORMAT JSON)` syntax by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12967
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13107
* [Bug] Enum types not being found if created in a schema by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13106
* Parquet reader can now read files with duplicate column names by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13111
* Prefer aliases over column-value functions in `GROUP BY`, and prefer error message when alias is used in an expression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13118
* Disallowing DISTINCT, FILTER and ORDER BY for UNNEST by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13110
* Feature #1272: Windowed DISTINCT Sink  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13093
* adjust list value logic execute seq by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/13114
* add CORE_EXTENSIONS build flag by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13116
* [Python] Add missing options for `read_csv` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12872
* Fix merge conflict by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13126
* Retry on HTTP failure in extension install by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13122
* Clean up ChunkInfo when cleaning up a transaction by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13125
* typo: conjuction -> conjunction by [@qsliu2017](https://github.com/qsliu2017) in https://github.com/duckdb/duckdb/pull/13127
* Add duckdb_result_error_type that returns the exception type of the error by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13131
* Keep track of user-provided configuration options, and compare them as well for database instance caching purposes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13129
* Disable sniff_csv when enable_external_access is not set by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13133
* Internal #2577: Window Atomic Finalize by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13117
* Internal #2577: Window Tree Allocation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13119
* Fix optimizer error when dealing with IN with a single NULL parameter by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13139
* Internal #2597: Ragged Validity Array by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13137
* Create file with O_EXCL flag set. by [@mkaruza](https://github.com/mkaruza) in https://github.com/duckdb/duckdb/pull/13123
* better CE for comparisons that use `=`, `!=`, `<`, `<=`, `>`, `>=`.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13130
* Use Slurm env vars to manage cpu and memory allocation if run inside Slurm HPC job  by [@dirkpetersen](https://github.com/dirkpetersen) in https://github.com/duckdb/duckdb/pull/12978
* Fix CTEFilterPusher optimization by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/13142
* Test with recent threadsanitizer by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13124
* Fixes for RegexFindAll function errors and multibyte character support by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/13108
* clang-tidy: rework Makefile and CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13101
* Extension updates to also be logged via enable_http_logging by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13087
* Hooks now get an error to indicate transaction/query success. by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/13136
* Use alias bind path in ORDER BY when running <alias> COLLATE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13140
* Implementation of recursive JSONPath expressions by [@robert-s01](https://github.com/robert-s01) in https://github.com/duckdb/duckdb/pull/12991
* Adding option to disable materialized cte optimization by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13146
* [Python] Fix issue with `native` UDFs returning STRUCT items by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13147
* CGroups: fix compilation due to UB cast by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13151
* test_expression.py: Skip throw related test on Windows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13157
* Replaced while loop with if statement by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/13161
* ThreadSanitizer: Avoid spurious data race in InsertMatchesAndIncrementMisses by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13179
* Add 'bugprone-narrowing-conversions' clang-tidy check by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13180
* [C API] Return duckdb_value in duckdb_profiling_info_get_value by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13160
* Fix #13120: implement StructFilter::ToExpression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13182
* Feature #1272: Windowed DISTINCT Sort by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13150
* Add native `list_has_any` implementation by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13163
* Add pragma extension versions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13063
* [C API] Add duckdb_scalar_function_set_volatile that allows changing FunctionStability of a scalar function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13186
* [CSV Sniffer] Give preference to configurations that ignore the least amount of lines by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13188
* Fix #13017 - if grabbing the lock fails due to it not being supported, allow this in read-only mode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13189
* Add test_collate_pivot: used to fail in 1.0.0, add to avoid regressions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13190
* Add catalog_error_max_schemas setting that toggles how many schemas we look at for "did you mean..." style error messages by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13191
* Fix build error when compiling with -DDISABLE_EXTENSION_LOAD=1 by [@whatsthecraic](https://github.com/whatsthecraic) in https://github.com/duckdb/duckdb/pull/13194
* Add clang-tidy-diff script, and invoke it on PRs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13158
* [Explain (mostly internal only)] Change the way key-value pairs of information are stored for RenderTreeNodes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13109
* Fixup invocation of clang-tidy by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13216
* [Julia] fix Vector and DataChunk all_valid() checks by [@aplavin](https://github.com/aplavin) in https://github.com/duckdb/duckdb/pull/13210
* Fix broken explain (format json) test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13218
* Linux 32: avoid packaging Jemalloc, due to regression by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13156
* feat(c): create value support by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13203
* feat(c): create value support  by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/12140
* fix: 13077: use tmp file for secret writes by [@devanbenz](https://github.com/devanbenz) in https://github.com/duckdb/duckdb/pull/13170
* Filter paths before scripts/clang-tidy-diff.py by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13220
* [CSV Reader/Progress Bar] Fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13207
* Use poll in httplib by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13223
* Fix several fuzzer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13240
* Fix #13238 - cannot return constant vector for volatile functions with more than one row as input by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13241
* Rename FORCE_CHECKPOINT to ALWAYS_CHECKPOINT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13242
* C API test fix - correctly use length also in non-inlined case by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13243
* Rollback optimistic writers when all rows we have inserted are deleted by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13236
* Add serialization support and fix ToString of ChangeOwnershipInfo by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13233
* Fix #13200: Transactions that update tables need to keep the underlying row group collection alive to ensure we can safely clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13230
* [CSV Reader] Comment Option by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13162
* Fix foreign key lookups from different search path by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/13256
* Add aggregate function support to the C API by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13229
* Feature #1272: Window Task Blocking by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13249
* Implement #4318: add overload for pg_get_constraintdef by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13258
* Several fuzzer fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13261
* Correctly add profiling information from finalize events to operator timings in EXPLAIN ANALYZE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13260
* Issue #13250: Zero Time Buckets by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13271
* Add delta to CI by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13219
* Remove outadated test that fails somehow randomly and doesn't add much by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13276
* Fix casts logic by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13275
* Executor profiler fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13282
* Avoid clang-tidy-diff to check Python sources or extension folder by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13279
* Enable yacc stack growing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13280
* Fix #13272: correctly read signed integer stats for TIMETZ by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13283
* [Upsert] Fix crash caused by scanning an empty LocalTableStorage by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13281
* Internal #2681: IEJoin Progress by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13284
* Move to latest duckdb-wasm (fixing COI compilation) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13257
* [DEV] CSV Tests Refactor and Sniffer decoupled of the vector size by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13231
* [TemporaryFileManager] Fix bug causing sizes of `.block` files to not be counted towards `max_temp_directory_size` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13278
* [CSV Reader] Properly cleanup invalid rows by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13262
* Disable website docs CI run by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13288
* Window Task Scheduling: avoid blocking tasks during GETDATA by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13290
* Fix #12582: correctly deal with empty grouping sets mixed with non-empty ones in lateral joins/correlated subqueries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13291
* Reduce memory usage of test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13292
* Move back from handrolled checkout to GH action + skip some verification in memory-intensive tests in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13296
* C API extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12682
* Secret settings cascade by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13167
* Fix CMake for when folders are not git folders via `git rev-parse --is-inside-work-tree` by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13315
* [Dev] Fix breakage caused by adjusting `duckdb.h` directly by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13321
* CAPI extensions: Fixup list of exported functions for wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13320
* [Python Dev] Make `cursor` creation threadsafe, perform compaction on the internal vector by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13319
* [Dev] Make (previously implicit) assertion explicit for DuckTransactionManager by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13307
* [PySpark] Fix filter type checking and isin column expression return type by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/13294
* Fix clang-format version in CONTRIBUTING.md by [@JelteF](https://github.com/JelteF) in https://github.com/duckdb/duckdb/pull/13324
* Expected errors 2053 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13322
* Fix #13237: fix .mode insert float column output by [@flashmouse](https://github.com/flashmouse) in https://github.com/duckdb/duckdb/pull/13308
* Add `CUMULATIVE_CARDINALITY` metric by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/13234
* Fuzzer #3113: Lead Lag Shift by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13330
* Implemented `list_extract` with `VectorOperations::Copy` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13313
* Issue template: Fix Arrow extension link by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13333
* NO_PARTITION_COLUMNS option to skip partition writes for Parquet copy by [@ykskb](https://github.com/ykskb) in https://github.com/duckdb/duckdb/pull/12886
* Format Python README by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13340
* Bug/Regression fixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13317
* Enable unnesting lists of arrays by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13342
* Limit relation has wrong relation type by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13343
* [Dev] Remove redundant variable from SQLStatement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13341
* Internal #2722: Partition State Threading by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13350
* Adding hyperbolic trigonometric functions by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/13346
* CSV Sniffer - Error Messages by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13355
* Fix a typo by [@SYaoJun](https://github.com/SYaoJun) in https://github.com/duckdb/duckdb/pull/13360
* Add PySpark head, take and first functions by [@khalidmammadov](https://github.com/khalidmammadov) in https://github.com/duckdb/duckdb/pull/13349
* [Explain] Add the `GRAPHVIZ` format for `EXPLAIN` statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13201
* Time cast: Have same behavior as Postgres by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13267
* Fix reordering semi joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13335
* Fix appian join tests by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13356
* remove sqlsmith patch by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13334
* Support Json Types in CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13359
* [CSV Sniffer] Date/Timestamp Sniffing adjustment by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13168
* WAL: Write pointers to optimistically written row groups directly, instead of copying over the data by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13372
* [Metrics] Add `CUMULATIVE_ROWS_SCANNED` and `OPERATOR_ROWS_SCANNED` by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/13354
* [Transformer] Fix loss of named parameter data in recursive TransformStatement calls by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13344
* Feature #1272: Window Distinct Merging by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13329
* Refine heuristic for flipping join sides by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13399
* Update jemalloc and re-enable opt.retain by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13370
* Add native `list_has_all` implementation by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13401
* Feature #1272: Window Distinct Indices by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13394
* [Arrow] Support consuming an "arrow_array_stream" PyCapsule by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13386
* Sample at least one value for the hyperloglog by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13383
* Fix issues with JSON map inference by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13387
* Compressed materialization for joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13402
* Python installation: Recommend using pip by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13357
* [Python UDF] Filter `NULL` values before calling the user defined function by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13358
* Add support for scalar function overloads to the C API by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13409
* Fix unused variable, resolve warning turned error in the amalgamation CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13408
* Add support for aggregate function overloads to the C API by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13410
* Fix lossy double cast issue by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13411
* Buffer manager: set handle readers after I/O so that any I/O exceptions don't leave the readers with an invalid value by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13417
* fix undefined symbol in httpfs for python by [@cyberjunk](https://github.com/cyberjunk) in https://github.com/duckdb/duckdb/pull/13420
* Fix dsdgen args by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13421
* [Arrow] Support producing an "arrow_array_stream" PyCapsule by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13418
* Disable jemalloc on 32bit through cmake, not through a CI script by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13433
* allow changing the default persistent secret storage after initialization by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13434
* Fixing hugeint cast to varint by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13268
* [Explain] Add the `HTML` format for `EXPLAIN` statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13202
* fix for the issue 2698 by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13440
* Avoid rounding errors and simplify memory assignments in `TemporaryMemoryManager` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13439
* Pull up filters from and through explicit joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13431
* [Metadata] Populate the `expressions` column of `duckdb_indexes` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13415
* Use LossyNumericCast while reading memory limits by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13450
* Label timestampTZ to timestamp cast as not revertible by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13206
* Prevent the query thread from picking up query unrelated tasks if compiled with DUCKDB_NO_THREADS by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/13326
* [Dev] Skip test on lower pyarrow versions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13463
* Add TPCDS sf-100 benchmarks by [@hmeriann](https://github.com/hmeriann) in https://github.com/duckdb/duckdb/pull/13205
* [Python] Let `create_function` cancel an open transaction instead of failing by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13462
* [Dev] Mention non-unique indexes in UPSERT `DO UPDATE SET` error by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13465
* Issue #13380: IN Invertible Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13441
* Compilation Fixes for GCC 4.8 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/13474
* [Dev] Make `Binder::Binder` a private constructor by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13475
* [Arrow] Accept objects that provide the `__arrow_c_stream__` producer method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13425
* [Lambdas] Support N-ary lambdas in the list comprehension syntax by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/13389
* [METRICS] Add `blocked_thread_time` Metric by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/13430
* Add ifdef to allow generating code with newer versions of Bison by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13477
* Clean up rendered text trees by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13476
* Make CMake target exports relocatable by [@cryos](https://github.com/cryos) in https://github.com/duckdb/duckdb/pull/13312
* Disable delta extension on windows for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13485
* Regression runner - don't fail on HTTP error by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13486
* ExecutorTask: flush before finalizing task by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13482
* [Metrics] Rework Optimizer Metrics   by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/13480
* Support collations in ordered aggregates by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13491
* ci: minor optional cleanup for cibuildwheel config by [@henryiii](https://github.com/henryiii) in https://github.com/duckdb/duckdb/pull/13496
* chore: remove wheel dependency by [@henryiii](https://github.com/henryiii) in https://github.com/duckdb/duckdb/pull/13495
* Prefer depth-first plan evaluation for unions and joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13447
* Fix #13472: get correct WAL location for windows long paths by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13487
* Make error message more explicit for when trying to parse SQL types. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13376
* [Arrow] Add UUID and JSON extension types by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13446
* Apply extension patches via 'patch' instead of 'git apply' by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13488
* Feature #1272: Window Distinct Tree by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13503
* Scalar macro default params by [@Alex-Monahan](https://github.com/Alex-Monahan) in https://github.com/duckdb/duckdb/pull/13494
* Add Varint to AllTypes() by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13388
* [ADBC] Support creation and ingestion into temporary tables. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13426
* Add support for registering custom casts (and types) through c api by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13499
* Bump sqlite & mysql by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13515
* Switch floating point division and modulo to use IEEE semantics for division by zero by default, and add ieee_floating_point_ops setting that can be used to revert back to old behavior by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13493
* [C API] Get all metrics by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13497
* Tuning ART indexes for duplicate values by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13373
* Feature #1272: Windowed Quantile Tree by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13516
* [Auto Loading] Autoload extension settings by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12790
* JSON bugfixes and new functions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13481
* Make changes to relation.hpp backward compatible with older API via default parameters by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13522
* Preserve cardinality information by [@jeewonhh](https://github.com/jeewonhh) in https://github.com/duckdb/duckdb/pull/13517
* Return an error when multiple rows are returned from a scalar subquery by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13514
* When referencing optimistically-written blocks in the WAL, we need to fsync the main database file before writing the WAL to ensure all changes have made it to disk by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13526
* Remove assertion in compressed file system by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13531
* Skip empty files in single-threaded CSV reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13528
* Disallow ordering by non-integer literal by default - and add the setting order_by_non_integer_literal to revert to the previous behavior by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13532
* Produce an empty list result for enum_range(NULL::enum_type) by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13530
* [CSV Reader] Fix for invalid unicode in header by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13518
* Issue #13525: Window Local States by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13538
* Linux32 also to regular ci by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13547
* Feature #1272: Windowed Distinct Tree by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13527
* Bump GitHub workflows to their latest versions by [@deining](https://github.com/deining) in https://github.com/duckdb/duckdb/pull/13393
* Add `map_contains`, `map_contains_entry` and `map_contains_value` functions, `list_position` now returns null. by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13406
* Numeric casts: forbid NumericCasts for float/double, add Lossy and Exact equivalent to make syntax explicit by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13546
* Fix clang-tidy on insertion_order_preserving_map.hpp: Alter order of statements by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13556
* Add http proxy by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13368
* move the inet extension out-of-tree by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/13085
* Fix compilation: install extension needs an instance now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13565
* Initialize (potentially) empty buffer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13564
* HTTP glob test fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13563
* Remove patches (vss and substrait), bump other repositories by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13551
* Disable dynamic filter pushdown for right semi joins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13562
* postgres_scanner: bump & remove patches by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13567
* Optimistic write to WAL: cannot write block pointers if we have in-memory updates to transaction local storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13577
* Add all CAPI functions to extension api for now by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13568
* Minor fixes for DuckDB-Wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13566
* Fix for vector size 2 tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13569
* [CSV Sniffer] Date Adjustment by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13573
* Fix issues found by alternative verify by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13578
* Set version info for duckdb.dll by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/13557
* Update storage info by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/13483
* Constrain size of estimated cardinality returned when operator is not initialized by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13574
* Unify task (un)blocking in physical operators by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13559
* [CSV Reader] Fix lock issue on Global CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13560
* TIMETZ group by: collations now no longer always return VARCHAR by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13571
* Internal #2850: Window Local States by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/13581
* Two steps upload action by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/13582
* Use new HLL implementation in `DistinctStatistics` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13489
* Remove inet from extension update test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13589
* [METRICS] Small fixes by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/13575
* Fix #13537: correctly maintain parameter count when rebinding a prepared statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13583
* Various nightly test fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13584
* IE Join: turn these into atomics to prevent tsan from tripping up in GetProgress by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13586
* Fix HTTPFS tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13588
* [PyArrow] Fix issue with passing timestamp types to filters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13593
* Fuzzer fixes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13596
* Automatically call `malloc_trim` to reduce unused outstanding allocations by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13590
* Fix for joins and FSST on 32-bit configurations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13594
* Casting to Bit is no longer Invertible by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/13595
* Switch in-tree DuckDB extension to use DuckDB's semver tag by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/13591
* List has bind fix by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/13600
* Do not include version.rc file on MINGW by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/13601
* [Python RelAPI] Throw an error if trying to use a invalid argument in read_csv by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/13597
* More nightly test fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13605
* Optimistic write to WAL: we cannot optimistically write block pointers if there are indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13610
* Block verification run and FixedSizeBuffer fix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13607
* [Test] Tighter ART storage regression boundaries by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13612
* Disable `JEMALLOC_HAVE_MADVISE_HUGE` in jemalloc by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13608
* Avoid adding buffers that will be destroyed to the eviction queue by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/13606
* Track overflow strings in PartialBlockManager during optimistic write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/13618
* [Fix] Avoid index deletion after catalog exception by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/13627

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.0.0...v1.1.0

---

# v1.0.0 - DuckDB 1.0.0 "Nivis" <a id="v100"></a>

*Released on 2024-06-03*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v1.0.0)

This release of DuckDB is named "Nivis" after the sadly non-existent Snow Duck (Anas Nivis) that is known for its stability.

Please also refer to the announcement blog post: https://duckdb.org/2024/06/03/announcing-duckdb-100

## What's Changed
* Fix move constants optimization by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/12189
* FALLOC_FL_PUNCH_HOLE requires GLIBC 2.18 or above - check for this using an #ifdef by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12193
* Fix cmake install for shared_ptr headers by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12194
* Fix minor warnings by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12195
* Install .ipp files in addition to the usual .hpp files by [@smonkewitz](https://github.com/smonkewitz) in https://github.com/duckdb/duckdb/pull/12198
* Set a default value to the `connection` param in stubs by [@tm-drtina](https://github.com/tm-drtina) in https://github.com/duckdb/duckdb/pull/12207
* Fix #12190: add SYSTEM to set of reserved database names by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12206
* Add `enable_view_dependencies` which defaults to `false` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12209
* [Python] Fix replacement scans incorrectly finding duckdb connection method objects by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12208
* [CI] Diff against the right remote + branch in `Regressions.yml` - `Regression Test new micro benchmark` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12106
* [Python] Fix bug where `enable_external_access` was not being respected by the replacement scan by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12224
* Remove outdated CI for extensions, check duckdb/extension-ci-tools by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12229
* Python: Avoid packaging for both 3.7 on OSX and MacOS 11 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12236
* Issue #12215: AsOf Predicate Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12238
* [DependencyManager] Don't block `ADD COLUMN` statements if there are dependencies. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12226
* [Python] Add check for 'params' to `table_function` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12233
* Extension installing/updateing fixes by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12221
* Move excel extension out of tree by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12123
* Fix #12225: revert OVERWRITE_OR_IGNORE to previous behavior, move new behavior to OVERWRITE flag by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12240
* Fix warning on unannotated fallthrough by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12244
* Fixup staged uploads /3 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12245
* [Python] fix build when BUILD_HTTPFS set by [@paparodeo](https://github.com/paparodeo) in https://github.com/duckdb/duckdb/pull/12223
* Use --always option of git describe for extension tags. by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12253
* [Docs] Fix up examples/python/duckdb-python.py by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12255
* [Fix] Skip lazy WAL creation test for alternative verification by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12258
* add missing virtual destructor by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12266
* Add storage callbacks for checkpoint start and end by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/12260
* Do not prefix error messages with an unknown type by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/12265
* Fix minor duckdb_extensions table function bug by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12269
* C API: Adding deprecation and move notices to duckdb.h and a test case by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12259
* Issue #12252: APPROX_QUANTILE Array Argument by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12271
* Turn InternalException into NotImplementedException in COPY FROM DATABASE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12264
* Add descriptions for vss and delta extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12267
* [C-API] Properly handle exceptions caused by name collisions in `duckdb_register_table_function` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12257
* Fix for multifilereader extra_columns feature by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12281
* Add `enable_macro_dependencies` which defaults to false by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12291

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.10.3...v1.0.0

---

# v0.10.3 - v0.10.3 Bugfix Release <a id="v0103"></a>

*Released on 2024-05-22*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.10.3)

This is a bug fix release for various issues discovered after we released 0.10.2. There are no new major features, just bug fixes. Database files created by DuckDB v0.10.* or v0.9.* can be read by DuckDB v0.10.3.

## Highlights

Even though this is "only" a bug fix release, there have been some major areas of work that warrant a separate mention:
- We have added a feature to update extensions using the `UPDATE EXTENSIONS` syntax #11677
- There have been some serious internal improvements around **checkpointing**, most notably, checkpoints can run while other connections are reading, and no longer block new connections while checkpointing #11918. Also, `FORCE CHECKPOINT`  no longer actively cancels transactions, it now waits until it can checkpoint #12061
- DuckDB now has native support to load data from HuggingFace using the `hf://` prefix #11831
- We have slightly changed `NULL` casting behaviour with the `MAP` type #11745
- The Java JDBC driver has been moved to its own repo: https://github.com/duckdb/duckdb-java #11873
- DuckDB now cleanly compiles with `-Wconversion` and all conversions are actually being checked #11716, #11673

## What's Changed
* Add setting to control the maximum swap space by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10978
* [Python][Dev] Dynamically generate the Connection wrapper methods by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11202
* Fixes duckdb wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11688
* Checked conversions between signed and unsigned integers by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11673
* Bump Julia to v0.10.2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11700
* Minor improvements to sql_reduce script by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11701
* Properly avoid build-time dependency on Python by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11713
* Test dockerized compilation in Alpine:latest and Ubuntu:20.04 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11708
* [COPY CSV] Enable TIMESTAMP_TZ formats by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11711
* Full conversion warnings / checks by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11716
* [Safety] Add safety checks to `shared_ptr` access by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11696
* Remove bound_defaults from BoundCreateTableInfo by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11721
* Improve mkdir error reporting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11723
* [Dev] Fix failing CI in Python SQLLogicTest Runner by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11724
* More docker tests, fix compilation up to C++23 standard by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11725
* Upload staging: from 'git describe --tags' to 'git log -1' by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11715
* Internal #1848: Window Progress by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11702
* Remove BoundConstraint from the TableCatalogEntry by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11735
* Implicit Cast for any Date/Timestamp by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11733
* feat: rewrite which_secret() into a table function by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/11726
* [Map] Rework `MAP` creation method behavior when input is NULL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11730
* [Dev] Always use `SQLStatement->Copy()` when ALTERNATIVE_VERIFY is defined by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11732
* Reconstruct Error Messages for Flush Cast by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11736
* Getting Rid of Value.TryCast in the CSV Sniffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11717
* Fix Join order optimizer so that plan generation is always via the most current entry in the DP table. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11719
* fix(py): support DuckDBPyType#children for array and enum by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/11754
* Consider not null values when doing export database by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11679
* Add missing space in error message by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11759
* Allow to build python packages without c++ sources by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11758
* No Mark to Semi join conversion in statistics propagation by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11596
* Hive partitioned write: lazy partitioning initialization by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11765
* Hive partitioning: avoid calling CreateDirectories for every flush, instead create the directory for a partition only when that partition is instantiated by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11777
* [Parquet] Support reading the non-standard NULL ConvertedType by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11774
* Only store CSV Errors if we are doing rejects table, otherwise just ignore it. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11763
* CI: Add job for 'expected behavior' label by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11784
* Move recursive_query_csv.test to slow test by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11770
* [StatementVerifier] Fix up issues in ToString implementations of classes derived from SQLStatement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11625
* Hive partitioning: make OVERWRITE_OR_IGNORE remove files on local file systems by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11787
* [ODBC] Add ODBC Test for Database Reconnection and Data Persistence by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11783
* Correctly parse dollar-quoted strings in sqlite3_complete and linenoise by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11789
* Add a configurable compression_level parameter to the parquet writer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11791
* Close file after file lock failure by [@awitten1](https://github.com/awitten1) in https://github.com/duckdb/duckdb/pull/11795
* Python: Add missing options to write_parquet by [@jzavala-gonzalez](https://github.com/jzavala-gonzalez) in https://github.com/duckdb/duckdb/pull/11790
* [PythonDev] Fix up failing tests in CI by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11801
* Fix `static bitpacking_width_t FindMinimumBitWidth(T *values, idx_t count)` in `class BitpackingPrimitives` by [@Lloyd-Pottiger](https://github.com/Lloyd-Pottiger) in https://github.com/duckdb/duckdb/pull/11757
* Add note on CMAKE_BUILD_PARALLEL_LEVEL by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/11808
* Elaborate on internal errors by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11816
* Fix #11756: Don't throw exception on CREATE UNIQUE INDEX IF NOT EXISTS if index already exists by [@ewencp](https://github.com/ewencp) in https://github.com/duckdb/duckdb/pull/11821
* Python CI fixes: skip two tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11818
* Fix #11798 - lateral join parameters should not be visible in views by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11825
* Fix #11804: make sure json_type can check null by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11807
* Fixing performance regression in [u]hugeint cast by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11829
* [Dev] ClientContextWrapper yak shaving by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11830
* [Python] Add `checkpoint` method, improve shutdown experience by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11810
* [Benchmark] Enable benchmarking result collection by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11529
* [DependencyManager] Create dependencies between foreign key tables and primary key tables. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11524
* [Python] Synchronize defaults of DuckDBPyRelation method `fetch_df_chunk` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11834
* Internal #1888 TIMETZ Collation Keys by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11861
* Removing old code that used to check if a buffer was the last buffer from the file handler by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11846
* Use `ToSQLString()` in `ConstantFilter` for escaped filter output by [@rcurtin](https://github.com/rcurtin) in https://github.com/duckdb/duckdb/pull/11797
* [StatementVerifier] Add `ToString` for every remaining SQLStatement, is pure virtual now by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11788
* Pushdown Tables Types to CSV Scanner  by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11792
* [Python Dev] Fix shift between `requirements-dev.txt` and `pyproject.toml` `before-test` section by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11863
* Join order optimizer asan bug Follow up by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11794
* BugFix: Introducing Introducing Delim Joins and Delim_Get(s) should respect positionally by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11812
* Provide the native OID of PG type in pg_type by [@goldmedal](https://github.com/goldmedal) in https://github.com/duckdb/duckdb/pull/11746
* Move JDBC (Java) Driver to Separate Repo by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11873
* Link Java client in issue template by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11877
* Change specificity of sniffed types to check time related types earlier by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11878
* fix complex top n test case for constant vector verification by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11882
* [Dev] Merge overloads for HUGEINT cast functions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11879
* Make " default for quote and " default for escape by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11880
* Set secret directory to a test directory when running sqllogictest by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11885
* Bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11785
* [Map] Rework interaction (entries, keys, values, extract) of NULL MAPs by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11745
* Add case when expression for grouping sets when collations are used. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11884
* Internal #11892: Interval Quarter Keyword by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11898
* HTTP Logging by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11771
* [Dev] Use strings in the SQLLogicTest `REQUIRE` calls so they are visible with `-s` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11714
* [Dev] Fix a SerializationException on CopyInfo by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11902
* MultiFileReader refactor by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11806
* Allow checkpoints to run while other connections are reading, and no longer block new connections while checkpointing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11918
* Allow converting `TIMETZ` to Arrow by [@LoganDark](https://github.com/LoganDark) in https://github.com/duckdb/duckdb/pull/11906
* Issue #11894: MIN/MAX_BY DECIMAL Casting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11912
* Issue #1917: WinNode 22 Compilation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11913
* [Relation] Add MaterializedRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11835
* Enable purging of BufferPool pages based on time-since-last-unpinned by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/11441
* Correctly render duckbox for empty results by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11920
* Always store transactions that had errors during the commit phase by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11929
* More anonymous struct zapping in RE2 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11956
* Add the corrupt block location to the exception by [@Vegetable26](https://github.com/Vegetable26) in https://github.com/duckdb/duckdb/pull/11966
* Fix assertion in bitpacking by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/11955
* [Python] Add `CoalesceOperator` to Python Expression API. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11941
* CMake: Handle git failures on invalid inputs better by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11951
* Internal #2005: DISTINCT ORDER BY by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11967
* Fix overlooked function argument rename that leads to seg faults. by [@smonkewitz](https://github.com/smonkewitz) in https://github.com/duckdb/duckdb/pull/11969
* [Nightly] Block size test fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11972
* Optimizing InsertionSort by reducing the size of the comparison by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/11964
* [Python] Keep referenced Python objects alive by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11761
* Move mysql_scanner into main duckdb CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11999
* Fix CURRENT_SETTING with a NULL string arg by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/12015
* Issue #12009: APPROX_QUANTILE NULL List by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12014
* Issue #12003: TIMESTAMP Stack Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12012
* fix extension load error message grammar by [@softprops](https://github.com/softprops) in https://github.com/duckdb/duckdb/pull/11994
* [Python] Fix InternalException from scanning Polars DF with no columns by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11982
* Issue #11959: TIMESTAMPTZ >= DATE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11987
* More fixes for RE2 to pass CRAN tests by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11978
* chore: update exception message by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/11965
* Issue #12005: RESERVOIR_QUANTILE DECIMAL Binding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12013
* [Python] Grab the GIL in the destructor of PyFilesystem by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11980
* [Python] Make the NumPy module optional, not throwing if it's not installed by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11981
* Add support for HuggingFace to httpfs by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11831
* [Fix] lambda binding in ALTER TABLE statements by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11976
* Distinguish between exact and case insensitive matching JSON keys in `json_structure` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11948
* Rework index binding by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11867
* Issue #11995: TIMESTAMP Rounding by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12011
* Fix sample serialization by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12025
* Correctly skipping errors when ignore_errors is set and we have columns with escaped values by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12027
* Update comment to reflect correct data state post-compression by [@wangxuqi](https://github.com/wangxuqi) in https://github.com/duckdb/duckdb/pull/12022
* Fix ordering issue with nested list type by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/11937
* Adding Fix to properly  pass timestamp/date formats in the relational API for CSV Files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12029
* Add more MultiFilereader features/hooks by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11984
* Rethrow serialization errors by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12030
* Move yyjson into core by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11998
* Bugfixes + large allocation hardening by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12028
* Ensure HT capacity is greater than lower bound by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12039
* Fix materialized CTE plan issue by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/11874
* Fix some fuzzer issues by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12043
* [Fix] Return NULL for deprecated getter calls in the C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12035
* Grab checkpoint lock during storage metadata reads by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12053
* Issue #12041: TIMETZ Parquet Nanoseconds by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12052
* Parquet: Correctly return min/max string stats if empty by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12054
* Even more fuzzer fixes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12050
* [Fix] Silent constraint violation error when destroying the appender in the C API by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12051
* Add "Tags" support to catalog entries by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12044
* Rework FORCE CHECKPOINT - instead of actively cancelling transactions it now blocks until it can checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12061
* Aggregation bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12055
* [Fix] Disable test for block size nightly run by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12062
* Bind art index in local storage by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12064
* Cast keys to VARCHAR before creating JSON from MAP by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12065
* [Python] Add pyspark hash and organize unit tests by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/11935
* Check context.interrupted during force checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12068
* [Fix] Lazy WAL creation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12049
* Test docker images: improvement and connected fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12026
* More fuzzer fixes by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12045
* [Python] Add pyspark null functions by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/11940
* CI fixes: unused variable & toolchain version by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12083
* Add autoloading for delta extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12063
* S3FileHandle Destructor should call `Close()` conditionally by [@onderkalaci](https://github.com/onderkalaci) in https://github.com/duckdb/duckdb/pull/12031
* [Fix] Internal segment tree exception in on conflict clause by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12084
* Remove ClientContext usage in Checkpoint Reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12076
* Fixed Parquet crash on missing dictionary by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12085
* [Fix] Add lambda binding to the HAVING binder by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12070
* Decimal/Time implicit casting + Multi-Error store in Flush by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11848
* [Testing Infra Fix] Make input data chunks immutable in the vector verification tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12088
* Correctly rewrite correlated columns inside window functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12087
* Fix #11780 - handle qualifications in ORDER BY of ARRAY clause by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12090
* Nightly CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12093
* Change ExtensionOptimizer input by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12094
* Fix for issue related to the execution of union by all from .sql in Python by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12098
* yyjson bump version to 2020 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12072
* [Dev] Collect CatalogEntry Dependencies during Binding by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11493
* Internal #2040: ICU Collation Serialisation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12077
* Run python tests in Pyodide build by [@cpcloud](https://github.com/cpcloud) in https://github.com/duckdb/duckdb/pull/11914
* Add support for type modifiers on extension types by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12081
* Bump extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12107
* fix huggingface credential_chain autoload issue by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12112
* Fix fuzzer issue 2690 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12108
* Throw exception in case of WAL failure instead of only printing a message by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12091
* Change type of columns from sniff_csv to list of structs by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12099
* [Python][Dev] Skip statements with decorators (only if, skip if) in the Python SQLLogicTester by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12102
* Mark unspecialized C++ `Append` template as delete by [@j1ah0ng](https://github.com/j1ah0ng) in https://github.com/duckdb/duckdb/pull/12116
* SQLLogicTest - skip these tests now that we have dependencies between views by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12118
* Correctly determine if we need to scan flat vectors in all cases - and add an enum to clarify code by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12119
* Avoid signed integer overflow in sequence generation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12120
* Use Binder::BindCreateTableCheckpoint in WAL ReplayCreateTable by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12121
* Avoid checking if wal is set directly and call GetWALSize instead - a WAL might be present even if wal is not set by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12124
* Call StringVector::AddString here for when inlining is disabled by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12125
* Minor fixes for vsize=2 tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12126
* Internal #2078: Nested Nulls First by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12131
* Bump extensions, part 2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12122
* Internal #2081: Window Distinct Reset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12130
* Read scan count once instead of once per vector to avoid issue where scan counts between vectors could become mis-aligned in concurrent scenarios by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12135
* Extension Updating by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11677
* Move pyodide from repository_dispatch to NightlyTests.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12153
* [Storage] Add `storage_compatibility_version` to control for what version the DB has to be serialized. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12110
* Allow quotes to be escaped in JSON path by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12033
* [Python] Fix issue in the SQLLogicTestRunner implementation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12155
* Higher memory limit for test by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/12158
* Fix internal error of list_zip and map_concat by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/12086
* fix row format of arrays larger than vector size with null by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/12143
* Issue #12136: Streaming Window Structs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12150
* Set max vector size to 128GB instead of 4GB by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12144
* Pass prepared statement parameters to OnExecutePrepared callback by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12156
* In string to list try_cast - set the target index to NULL, not the source index by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12160
* More Nightly CI Fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12154
* Fixing unchecked malloc() calls in Parser and elsewhere by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12162
* Modify the pandas analyzer code to always respect the sample size by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12097
* Allow community extensions: add setting and keys by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12152
* Fixing parquet dictionary / data page offset bug by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12109
* small fix to extension origin checks and direct installing over http by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/12165
* [DependencyManager] Provide details in case of a DROP statement that needs CASCADE. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12159
* Remove UnsafeNumericCast in create_sort_key by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12168
* [Dev] `enable_verification` now serializes for compatibility version `'latest'` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12157
* [Relation] Disable creating a VIEW from a MaterializedRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12163
* Move community keys to proper values by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/12175
* Remove release assertions timeout by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12176
* Internal #2095: Streaming Window Structs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/12173
* [CSV Reader] Bug-fix related to skip parameter over vector size in the sniffer by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/12167
* Expression rewrite filter pushdown for dates by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/12056
* [Python] Throw if replacement scan is attempted on cross-connection DuckDBPyRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/12169
* [Fix] Correctly allocate the ARRAY target child vector in a MAP function by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/12111
* Remove java from CI invoker by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/12182
* Mark correct database as modified in CreateIndex by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/12183

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.10.2...v0.10.3

---

# v0.10.2 - v0.10.2 Bugfix Release <a id="v0102"></a>

*Released on 2024-04-17*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.10.2)

This is a bug fix release for various issues discovered after we released 0.10.1. There are no new features, just bug fixes. Database files created by DuckDB v0.10.* or v0.9.* can be read by DuckDB v0.10.2.

## SQL Modifications

This release has a number of bug fixes that change SQL semantics in a few edge cases:

* Nested Boolean Comparisons now have consistent NULL comparison semantics - https://github.com/duckdb/duckdb/pull/11496
* Structs with non-matching keys require explicit casts when compared or combined - https://github.com/duckdb/duckdb/pull/11396

## What's Changed
* Bump julia version & fix release script for sub-versions > 9 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11225
* Flatten Rewrite by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11223
* ORDER BY ColumnNumber with Collations by [@tiagokepe](https://github.com/tiagokepe) in https://github.com/duckdb/duckdb/pull/11139
* Fix differences to implementation for to_parquet, write_parquet, to_csv, write_csv, Expression.alias, DuckDBPyRelation.map by [@binste](https://github.com/binste) in https://github.com/duckdb/duckdb/pull/11135
* Issue template: Ask for MWEs by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11192
* Cleaning up FSST: Remove unused AVX512 code by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11222
* Fix #11211 - correctly fill in string_t padding for bit type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11231
* Fix #3391: Stop creating background threads if the thread constructor throws an exception by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11236
* R_CMD_CHECK: Pin to duckdb/duckdb-r 0ed106a71c by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11245
* Add support for HEX(BLOB) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11243
* Remove no_vector_verification in Map Subscript Test by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11242
* Update logos in README by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11256
* Ignore user defined parameters that change names or types of csv columns in sniffer's prompt. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11257
* [Python] Fix error caused by looking up a TypeCatalogEntry without an active transaction. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11255
* [Fix] Fuzzer issue in list_select by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11248
* [Parquet] Support for LZ4 Compression by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11220
* Fix #11254: Add missing includes to terminal by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11265
* Issue #10867: AsOf Predicate Pushdown by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11233
* Fix plan cost runner regression script by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11129
* Check if we need to throw any remaining errors at end of CSV scanning by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11276
* Allow duplicate names in json objects when ignore_errors is true by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11271
* Do not surround JSON with quotes in sqlite shell output by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11268
* add TRIM support to virtual filesystem, and implementation on linux by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/11258
* Perform direct write operation if input data are larger than buffer size by [@quentingodeau](https://github.com/quentingodeau) in https://github.com/duckdb/duckdb/pull/11203
* Fuzzer fixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11286
* Compile spatial also for rtools by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11291
* allow injecting custom BufferManager implementation by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/11215
* Default to RECORDS in JSON reader if more than one column is specified by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11295
* Add support for materialized CTEs in INSERT/UPDATE/DELETE statements by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/10878
* Only throw exception if `je_mallctl` fails in DEBUG mode by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11303
* Fixing casting issue in generators by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11304
* Rework `FileSystem::OpenFile` call, and add `FILE_FLAGS_NULL_IF_NOT_EXISTS` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11297
* Fix potential UB when `list()` aggregate is used in combination with other arena using aggregate functions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11306
* Fix #11293 - for ARRAY([subquery]) explicitly push the ORDER BY of the underlying subquery into the array aggregate by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11316
* Fix #11281: explicitly select column types of information_schema tables for all columns, even if they are always NULL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11317
* Fixup py upload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11308
* Issue #11279: TIMESTAMP => TIMESTAMPTZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11320
* Fix null pointer exception when rolling back updates if the rollback was caused by an OOM by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11309
* Fix #11283 - report consistent foreign key constraint name in information_schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11318
* Fix #11294 - avoid applying Filter Pushdown optimization for UNION/EXCEPT without ALL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11315
* Fix #10695 - handle ? prepared statement parameters correctly for POSITION(x IN y) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11314
* Windows CLI - emit UTF8 directly using SetConsoleOutputCP(CP_UTF8) if possible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11324
* Fix #11319: use modulo when computing day of the week in excel extension by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11328
* [CI] Fix bash syntax in TwineUpload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11333
* Fix #11284: avoid adding the same column multiple times to a primary key/unique constraint name list by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11325
* In ColumnData, limit scan to the current count in the column by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11329
* Issue #11269: DISTINCT Sorted Aggregates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11321
* [Attach] Fix bug causing sequences to break attaching databases. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11327
* Flatten hash vector before combining list hashes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11340
* Make sniffer more consistent when nullpadding/ignore_errors are on by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11313
* fix(arrow): union buffer count & handle schema errors by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/11326
* fix duckdb-r script by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11345
* Fix regression_test_runner.py by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11346
* Issue #11234: IEJoin Scan Reset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11347
* TPC-H: Use BIGINT for ID fields schema where required by the specification by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11341
* Another round of polishing staged releases by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11342
* CI: Remove issue labeling workflow by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11355
* RE2 upgrade to version 2023-02-01 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11252
* File System: Add `optional_ptr<FileOpener>` to various calls, and add support for attaching DuckDB files over S3 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11343
* README: Display different logo for light/dark mode by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11366
* Fix bug in duckdb_bind_blob by [@pfarndt](https://github.com/pfarndt) in https://github.com/duckdb/duckdb/pull/11368
* Fix OSX CI by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11379
* Enable clang-tidy on headers and fix all headers to conform to our clang-tidy rules by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11376
* Add logical_type to parameters of format_pg_type by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/11369
* Issue #10965: RESPECT IGNORE NULLS by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11372
* Fix building issues in WIN32, remove unnecessary modification. by [@kindred77](https://github.com/kindred77) in https://github.com/duckdb/duckdb/pull/11356
* Zero-initialize aggregate states with destructors immediately after allocating by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11360
* Update README.md by [@jingshi-ant](https://github.com/jingshi-ant) in https://github.com/duckdb/duckdb/pull/11357
* Issue #10885: Negative Window RANGEs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11390
* Issue #11377: Invertible TIMESTAMP_XXX Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11392
* Update __init__.py To export "extract_statements" function by [@oomojola](https://github.com/oomojola) in https://github.com/duckdb/duckdb/pull/11394
* Internal #1657: Stricter STRUCT Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11396
* allow set readonly on attached db by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/11397
* Give preference to FSSPEC defined FS by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11400
* Default serialize `optional_idx`, add `skip_default` option to `json_serialize_sql()` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11405
* CI: Also label PRs as 'stale' and close them when there's no activity by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11420
* fix(jdbc): 1-index getBytes() by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/11421
* Remove redundant default descriptions by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11415
* clang-tidy: enable `cppcoreguidelines-pro-type-const-cast` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11414
* clang-tidy: enable `cppcoreguidelines-avoid-non-const-global-variables` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11424
* Issue #11419: Quantile Order By by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11428
* [CSV Sniffer] Give preference to quoted candidates by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11418
* clang-tidy: enable `cppcoreguidelines-virtual-class-destructor` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11437
* clang-tidy: enable `cppcoreguidelines-[interfaces-global-init|slicing|rvalue-reference-param-not-moved]` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11435
* Fix #11393 - improve error message when trying to use a lateral join column in a table function that does not support it by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11436
* add readonly to duckdb_databases() by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/11429
* Fix missing opener propagation by [@quentingodeau](https://github.com/quentingodeau) in https://github.com/duckdb/duckdb/pull/11454
* Fix #11246: Use SetConsoleCP function to set input to UTF8 when reading by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11452
* CLI: Add support for ".edit" or "\e" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11447
* Fix VS2022 Preview ClangCl build by [@bodand](https://github.com/bodand) in https://github.com/duckdb/duckdb/pull/11456
* Remove an unnecessary line from bind_insert.cpp by [@huachaohuang](https://github.com/huachaohuang) in https://github.com/duckdb/duckdb/pull/11443
* [CI] Skip ccache for R.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11459
* Improve binding of CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/11399
* Move BindCreateIndex from Catalog to Binder by [@philippmd](https://github.com/philippmd) in https://github.com/duckdb/duckdb/pull/11402
* [Substrait-ADBC] Fix for substrait plan execution via ADBC by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11358
* Removing abort() from RE2 again because Google refuses to use exceptions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/11458
* Defer allocation in read_json by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11378
* [ODBC] Add escape character to ParseStringFilter to support Power Query ('table_name' is escaped to 'table\_name') by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/11432
* Bump to post-portfile change for duckdb_azure by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11476
* Reduce memory usage of DELETE operations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11470
* Use `optional_idx` in more places by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11466
* Revert "Move BindCreateIndex from Catalog to Binder" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11478
* [Arrow] Throw on invalid STRUCT type by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11464
* [Dev] Do not use CatalogEntry references inside Dependency objects. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11408
* Fix extension builds by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11486
* [Fix] Throw BinderException for UNNEST expressions in WINDOW expressions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11247
* Check for IUTF8 flag defined before setting it by [@patmaddox](https://github.com/patmaddox) in https://github.com/duckdb/duckdb/pull/11488
* Fix #11445: correctly detect recursive aliases when using struct unnest by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11497
* Fix #11444: avoid using recursion in string -> list parsing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11498
* Add serialization for `LogicalCopyDatabase` operator by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/11401
* add support in Julia appender for missing and nothing values by [@rdavis120](https://github.com/rdavis120) in https://github.com/duckdb/duckdb/pull/11508
* [Python] Produce `datetime.time` values when converting TIME columns to Pandas DataFrame by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11468
* [Fix][ADBC] Implement required ADBCConnectionGetObjects schema by [@joellubi](https://github.com/joellubi) in https://github.com/duckdb/duckdb/pull/11446
* Add support for decimal modulo operation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11506
* Move `CompressedMaterialization` inside of `StatisticsPropagator` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11495
* Bump stale bot version by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11509
* Rework issue workflow by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11522
* [RE2] Add includes and remove potential throw from destructor by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11513
* Issue #11292: Nested Boolean Compares by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11496
* [Dev] Initialize new buffers with garbage data if `DESTROY_UNPINNED_BLOCKS` is set by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11270
* Fix timeout in async workflow by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11525
* Move assertion in `json_scan.cpp` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11530
* Issue #11518: TryParseTime by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11519
* Fuzzer Bugfixes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11544
* [CI] Fix CI failure on `C Enum Integrity Check` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11547
* [ICU] Use the correct lookup precedence for TimeZone settings by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11546
* [CI] Move from default GITHUB_TOKEN to specific one by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11556
* [CI] Fix Deploy step to execute only for duckdb organization by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11553
* Rework `RadixPartitionHashTable` task assignment in source phase by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11528
* Run new micro benchmarks in CI when they are added by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11532
* Rework `vector_hash` for ARRAYs by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11558
* [Dev] Add assertions around Uncompressed String storage by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11267
* python: Add missing global options to write_csv by [@jzavala-gonzalez](https://github.com/jzavala-gonzalez) in https://github.com/duckdb/duckdb/pull/10382
* [Python] Fix issue with lists containing dictionaries of different sizes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11095
* [Dev][Python] Add nightly test to execute all sqllogic tests using the python package by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11137
* Parquet Writer: Early out creating dictionary by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11461
* ODBC driver should ignore "driver" and "trusted_connection" keywords in connection string by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/11382
* [ODBC] Fix: Support loading UTF-8 encoded data with Power BI by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/11423
* Draft permissions - bot does not have permission for drafting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11575
* CI: Remove 'needs reproducible example' when 'reproduced' label is applied by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11576
* Various fixes & clean-up around STRUCT UNNEST by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11580
* Update token by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11592
* Update issue template by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11577
* [CI] Remove GITHUB_PAT variable from R-CMD-check by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11593
* Respect read-only mode in dbgen and dsdgen by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11585
* Bump-back duckdb_azure to pre-lzma custom vcpkg-port by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11595
* Correctly handle database names with quotes in USE statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11587
* Bump postgres version and build arrow also for windows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11604
* Support reading gzipped files in the test runner by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/11600
* initializes unknown indexes on catalog lookup by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11551
* Fix Progress Bar for many large CSV Files + Adjustment to not store buffers from compressed files over single threaded scans by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11273
* CSV Rejects Tables 2.0 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11512
* Fix topn placement by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11601
* Fix various issues found by oss-fuzz by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11613
* [ODBC] Fix: timestamps and times are parsed as dates by Power Query by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/11610
* Fix various fuzzer issues, move fuzzer scripts into this repo, and expand `reduce_sql_statement` to improve test case reduction capabilities of fuzzer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11622
* [Dev] Make the `extension_entries.hpp` generation script more modular by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11623
* [Fix][ADBC] Don't filter system catalogs/schemas in ConnectionGetObjects by [@joellubi](https://github.com/joellubi) in https://github.com/duckdb/duckdb/pull/11618
* Add pyodide wheel building github action by [@cpcloud](https://github.com/cpcloud) in https://github.com/duckdb/duckdb/pull/11531
* Move away from dynamic_cast to Cast<> infrastructure by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11619
* Extension Metadata by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11515
* [Dev] Regenerate query string for `IndexCatalogEntry`. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11462
* Upload pyodide by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11626
* Add docker alpine build to check on builds by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11490
* Add Vector Similarity Search (VSS) Extension by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11614
* Metadata fix by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11629
* Fix extension config for arrow, remove patch from sqlite by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11628
* [CSV Reader] Resets the buffer manager over recursive scans by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11631
* Make path to append_metadata.cmake relative to top-level CMakeLists.txt by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/11635
* [CSV Reader] Fixes an issue with conflicting strategies for buffer cleaning by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11630
* Fix more issues found by the fuzzer, extend SQL reduction further by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11642
* fix(jdbc): support non-string parameter types by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/11646
* Few more fuzzer fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11648
* Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11650
* Avoid performing Apple codesign on extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11652
* Filter out single relation predicates before join ordering by [@wangxiaoying](https://github.com/wangxiaoying) in https://github.com/duckdb/duckdb/pull/11645
* Fix `last_value` in the `duckdb_sequences` metadata function by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11465
* Limit batch insert threads based on available memory, similar to Parquet write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11655
* [Vacuum] Fix serialization and Copy of the VacuumStatement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11656
* More index initialization by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11659
* Skip tests with the unzip keyword in python and disable unzip.test for 32bit systems by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/11658
* Bump extension versions, remove patches by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11662
* Accept a list of multiple nullstring values for CSV Files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11616
* Include falloc to fix build on some Linux systems by [@zmbc](https://github.com/zmbc) in https://github.com/duckdb/duckdb/pull/11663
* Fix #11469 - make unnest parameters case-insensitive by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11667
* Fix #11467: correctly merge unnamed structs and structs in CombineEqualTypes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11668
* Skip ADBC tests if python version is not 3.9 or higher by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11653
* Fix #11621 - correctly zero-initialize padding bits in bitpacking compression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11671
* Fix #11542 - correctly check if a column data segment has updates, and clean up the updates by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11670
* Make UNION BY NAME also use ForceMaxLogicalType, similar to UNION by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11665
* Fix extension_version propagation for external extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11672
* Allow decimal type in CSV auto_type_candidates option by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11675
* Fix #11484: support constant indexes in ARRAY - e.g. `ARRAY(SELECT .. ORDER BY 1)` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11674
* Improve hive type auto-casting so that it looks at all files instead of only the first file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11676
* Fix #11669: deduplicate column names in pivot correctly by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11678
* Disable setting console pages by default, and add .utf8 setting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11682
* bump vss, handle reverting append when index is unknown by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11681

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.10.1...v0.10.2

---

# v0.10.1 - v0.10.1 Bugfix Release <a id="v0101"></a>

*Released on 2024-03-18*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.10.1)

This is a bug fix release for various issues discovered after we released 0.10.0. There are no new features, just bug fixes. Database files created by DuckDB v0.10.0 or v0.9.* can be read by DuckDB v0.10.1.

## What's Changed
* Remove `visualizer` leftovers by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/10642
* Add explicit numbering to C enums + various compilation/CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10649
* Disable print method for CSV scanner for R build by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10650
* Fix #10548 for the DUCKDB_NO_THREADS case by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10654
* Allow StorageExtension to extend DuckCatalog implementation in order to integration with observability system by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/10643
* Update storage info for v0.10.0 by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10660
* Revamp duckdb-wasm extensions CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10672
* [CI] Re-enable skipped test `window-rows-overflow.test` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10679
* Catch: prominently display skipped tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10669
* Update Julia to 0.10.0 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10689
* Ingestion benchmark framework by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10341
* [ICU] Add casts from Timestamp_* to TimestampTZ by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9539
* DISTINCT ON - greatly improve performance by rewriting ordered FIRST aggregate into arg_min_null by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10684
* Fix #10685 - support aliases in join clause by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10691
* Use assertThrows for throwing assertions in JDBC tests by [@peteraisher](https://github.com/peteraisher) in https://github.com/duckdb/duckdb/pull/10448
* Casts: report error location in query for failed casts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10694
* Fix duckdb spelling in _extension_deploy.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10717
* Fuzzer #1374: ARG_XXX By Decimal by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10728
* [Python] Rework the python regression test script by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10715
* Removes static member string by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/10733
* Fuzzer #1372: Order Bind Failure by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10727
* Fuzzer #1380: To Weeks Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10726
* Various fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10708
* Unittest does not satify assertion on MSVC/Debug by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/10738
* Fix OrderPreservationType issue of MATERIALIZED CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/10587
* Map creation fixes and refactoring by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10436
* Fuzzer #1383: NULL Range Arguments by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10723
* Fuzzer #1382: Window Stats Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10725
* Comment on view columns by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10710
* Union exclude by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10688
* move the logic for immediate_transaction_mode to the physical operator by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/10739
* [C API] Small fix and more tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10748
* List_slice bug fix by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10747
* Enable azure autoload by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10746
* Parquet writer - reduce memory usage of order-preserving write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10756
* Refactor csv reader includes because of r path length limitations by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10658
* Arrow String View Type by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10481
* local_file_system.cpp: minor fix for macOS libproc code by [@barracuda156](https://github.com/barracuda156) in https://github.com/duckdb/duckdb/pull/10758
* Make unnamed_subquery naming predictable by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10765
* [Python] Fix overflow issue in PandasAnalyzer by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10768
* Throw when trying to consume over 128 byte decimals by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10601
* CLI: Right-align numerics in markdown tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10767
* Fuzzer #1399: Window NULL RANGE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10776
* [CSV Sniffer] Minor sniffer tweak to give preference to dialects that generate the least errors if ignore_errors = true by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10777
* Add large benchmark directory by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10763
* Improve UNPIVOT error messages, and allow expressions in unpivot  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10773
* Add a method UUID::FromUHugeint to generate a UUID from a uhugeint_t by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10771
* [CSV Reader] Add lock to buffer reset by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10791
* [WINDOWS] Add "/bigobj" that solves compile issue during debug by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10782
* fix: not over-call AllSecrets by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10807
* Update readme by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10814
* [ODBC] Rework Connect to the ODBC driver and add functionality to set all DuckDB configurations in the Connection String by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10692
* Fix arrow conversion, map doesn't support large offset by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/10796
* [CSV Reader] Spinlock over GetLine Error + New Strategy for dialect candidates by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10755
* Trivial fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10816
* Fix unicode handling in underscore of LIKE operator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10821
* JDBC spurious CI failure - an exception being thrown in this test is a race condition by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10825
* Benchmark runner - allow files (e.g. CSV/Parquet) to be cached using the cache command by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10817
* Fix #10803 - correctly reclaim space of list indexes when columns are dropped by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10822
* [Upsert] `INSERT OR REPLACE` fixes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10789
* [Dev] Add an optional time out in seconds to `run_tests_one_by_one.py` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10744
* Maintain names in COLUMNS(*) expression, and allow aliasing multiple columns using {column} by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10774
* Disable AWS/Azure on Windows for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10827
* [Dev] Bump memory limit on batch_memory_usage.test_slow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10845
* Fix coverity apt-get by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10838
* minor: FixedSizeBuffer::Pin move shared_ptr rather than copying by [@mapleFU](https://github.com/mapleFU) in https://github.com/duckdb/duckdb/pull/10837
* ci: Upgrade workflows to actions/setup-python[@v5](https://github.com/v5) by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/10832
* Fuzzer #1389: ARG_XXX Decimal Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10742
* Contributor guide: Fix new issue link by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10836
* Changing source to src in relational_constraints query by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/10848
* Fix: correctly calculate the range of build side for perfect hash join by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/10446
* [Python] Fix issue caused by deadlock between `thread.join()` and acquiring the GIL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10854
* [CSV Parser] 8-Byte Skipping instead of 1-Byte when possible by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10855
* Add components of the version to duckdb.hpp by [@ahuarte47](https://github.com/ahuarte47) in https://github.com/duckdb/duckdb/pull/10840
* [CSV Sniffer] Tweaking header detection by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10714
* Check if directory exists before removing files in regression test runner by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10859
* [Extension] Add CatalogType to the list of functions generated in `extension_entries.hpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10597
* Regression test build side probe side by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10585
* [Arrow] Fix issue surrounding lifetime of dictionary arrays by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10610
* Fix #10745 - correctly deal with empty float columns in floating point compression routines by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10863
* [Extensions] Build fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10860
* Fix MSVC linking issue with workaround by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10865
* Reduce memory usage & avoid spilling to disk unnecessarily for order-preserving table creation/insertion by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10862
* pb/avoid GetSchema opening a transaction by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/10740
* Support dollar-quoted string-constants in the CLI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10879
* Shell: avoid printing "Error: " prefix if the error message already has a prefix (e.g. Binder Error:, Parser Error:, etc) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10880
* Partially fix #10751: correctly catch exceptions in sqlite3_print_duckbox by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10881
* Reset `refresh` in CompressedFile::Close() by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10882
* [CSV Reader] Lock when getting progress by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10884
* [CSV Sniffer] Early out if things go wrong in dialect detection by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10872
* [CSV Reader] Fix for skipping mix of newline delimiters by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10864
* Parallelize format.py script by [@hatvik](https://github.com/hatvik) in https://github.com/duckdb/duckdb/pull/10646
* Remove Old PSQLODBC scripts by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10888
* Add update_odbc_path.py to ODBC bundle by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10895
* Improve Wasm.yml workflow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10899
* [Parquet] Fix #10829, write correct data page offset in the presence of dictionaries by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10890
* Table name binding does not fail for non-existent tables in DROP TABLE statements by [@NiclasHaderer](https://github.com/NiclasHaderer) in https://github.com/duckdb/duckdb/pull/10893
* Fix #10889 - correctly deal with compressed vectors in struct filterpushdown of ColumnSegment::FilterSelection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10896
* CI: Disable julia nightly for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10905
* CLI - add support for rendering errors/matching brackets for square ([]) and curly ({}) brackets as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10904
* Storage: Fix an internal exception that could be triggered when deleting many rows and checkpointing repeatedly by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10897
* LIMIT/OFFSET clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10873
* Add ARRAY to test_all_types + IO and some clients by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10850
* Use M1 (ARM) OSX runners by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10670
* build: restore tarball build support by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10900
* Fix #10902 - allow more expressions to be used with an indirection without brackets (. or [], etc) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10909
* feat(jdbc): fixed size array support by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10911
* Add regexp_split_to_table macro by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10898
* [MetaTransaction] Add lock on modifying `all_transactions` and `transactions` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10799
* Issue #10809: RANGE Hint Corrections by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10828
* Enable the progress bar (without printing) in unittests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10908
* [Python][Dev] Fix issue in `read_csv` related to the s3 extension by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10690
* Add support for the C API duckdb_query function to the Julia api by [@rdavis120](https://github.com/rdavis120) in https://github.com/duckdb/duckdb/pull/10886
* Fix #10501 - in LocalFileSystem::Write split writes into batches of at most 2GB by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10912
* Correctly reset data chunk in RETURNING of DELETE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10915
* bitstring_agg had a trigger-able assertion, [duckdb-fuzzer/#1414] by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10918
* Shell: Remove IEE754 function from CLI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10919
* Use correct index in string to nested cast error handling by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10920
* Batch memory manager - keep track of all used memory correctly and enforce that unflushed memory is correctly set to 0 when we are finished by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10922
* Fix #9975 - correctly open (and keep open) a transaction when checking if prepared statement needs to be rebound by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10923
* CLI - Insert spaces when copy-pasting tabs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10924
* feat: exposing ssl ca cert path to httpfs by [@pvaezi](https://github.com/pvaezi) in https://github.com/duckdb/duckdb/pull/10704
* Centralize dynamic cast check and disable on MacOS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10925
* Checked Numeric Casts by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10870
* Avoid running numeric cast checks when CRASH_ON_ASSERT is enabled by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10942
* Set duckdb_api to 'python jupyter' if in Jupyter notebook by [@guenp](https://github.com/guenp) in https://github.com/duckdb/duckdb/pull/10931
* Array fuzzer issue fixes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10944
* Fix assertion trigger in FilterCombiner::AddTransitiveFilters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10941
* Support recursive describe queries (i.e. DESCRIBE(DESCRIBE ..)) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10945
* Avoid throwing null pointer exception in Window Segment Tree destructor by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10937
* Fix an issue where partitions were not correctly considered in bound window expression equality by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10939
* Fix for limit % with subquery on an empty table by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10946
* Correctly visit all expressions during lateral join decorrelation, particularly with nested lateral joins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10936
* when you add the relation, make sure you call gettableIndexes() on th… by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10949
* Internal #1428: Interval Subtract Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10957
* Fuzzer #1445: Trap MAKE_DATE/TIME Overflows by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10958
* Python.yml: Revert to macos-latest for OSX workflow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10970
* Purge queue refactor by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10594
* Change time from duckdb_time to duckdb_time_struct in duckdb_time_tz_struct by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/10933
* Add require block_sizes 262144 on tests reading db files by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10974
* [duckdb-fuzzer/#1368] - overflow in bitstring_agg on hugeint & uhugei… by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10971
* Fix LIST->ARRAY TRY_CAST when list sizes mismatch by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10973
* Add a micro extended benchmark. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10943
* [Dev] Move `TemporaryFileManager` and friends out of StandardBufferManager by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10938
* [ODBC] Reorganize Directory Structure by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10979
* Internal #1385: Window Partition Collation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10985
* Fuzzer #1471: Trap MAKE_DATE Overflows by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10987
* Range checks for ACOS by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10972
* improve CheckBoundaryValues in TopN by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/10955
* CSV tests - use __TEST_DIR__ to prevent leaking file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10991
* Autoload INET and ICU (and add back sqlite and postgres as autoloadable) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10948
* Fuzzer #1468: Window RANGE Types by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10990
* Fuzzer #1446: Quantile Hugeint Interpolation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10983
* Override git hash / git version by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10977
* [Storage] Only call FinalizeOptimisticWriter after storage merge has succeeded by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10998
* Add MetaTransaction::GetTransaction to threadsan suppressions (false positive) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11001
* Various fixes: CMake + generated extension_entries.hpp checks by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10994
* Nightly Wasm build fix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10993
* Fix return null constant in array_slice and other array issues by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10992
* Add correct table bindings for window relations. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10997
* Clean up ExecutorTask and simplify waiting for all tasks to be cancelled by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11005
* Various JSON thread sanitizer fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11004
* Fix warnings in ALP and logical_insert by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11008
* Check IsLoaded() before importing cached item by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11007
* Issue #10995: ICU VARCHAR TIMETZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11002
* Fix #10982 - only update total rows of row group collection after we finish appending to prevent other readers from attempting to initialize scans on in-progress appends by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11011
* [Nightly] Block size nightly test changes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11010
* ATTACH with reserved names (temp/main) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11020
* Fix various tests for vector_size = 2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11027
* [CI] Create a bigger table in interrupt test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11025
* Issue #10995: TIMETZ DST Fix by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11024
* Fixup LinuxRelease.yml release: unittester was not invoked correctly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11022
* In DatabaseInstance destructor - destroy TaskScheduler first by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11021
* Refactor ATTACH options by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11016
* Fix #11033: don't reset arena allocator in between calls to streaming window expression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11039
* Avoid checking LastModifiedTime for remote files in object cache by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11034
* [Block Size Nightly] Enable more block size nightly tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11036
* Add missing pipeline dependencies in recursive CTE by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/11043
* Use batch limit only when limit + offset are small constants by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11035
* Add New CSV Error for Invalid Unicode by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10984
* [FIX] Lambda bug in subqueries by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11046
* [Swift] performance optimisations by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/11052
* add concat_ws to spark API by [@nicornk](https://github.com/nicornk) in https://github.com/duckdb/duckdb/pull/11051
* feat(jdbc): expose comments via jdbc methods  by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/11031
* [CI / Tests] Disable CSV sniffer test for smaller vector sizes and reduce block-size nightly runtime by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11055
* [CSV Sniffer] Consider date/timestamp formats from the user when sniffing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11057
* Extend the "Contents of view were altered" error with more information by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11064
* [Python]  Add some numeric and string functions to spark API by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/11067
* [ODBC] Allow multiple statements to be executed using SQLExecDirect by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11038
* [CSV Reader] Apply projection on over buffer values. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11056
* Python: use short paths for Windows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11068
* Fix #10752: Add support for Parquet encryption on Windows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11069
* [Python] Code Quality - PEP8 Compliant + only relevant imports by [@mariotaddeucci](https://github.com/mariotaddeucci) in https://github.com/duckdb/duckdb/pull/11070
* [CI] Add patch argument to patch the extension's sources before building by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/10831
* fix(jdbc): support fractional seconds in getTime by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10707
* Fix #11071 - correctly report progress when scanning multiple Parquet files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11072
* Add ipv6 inet + minor fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11073
* Implement IPv6 support in the inet extension. by [@troycurtisjr](https://github.com/troycurtisjr) in https://github.com/duckdb/duckdb/pull/10839
* [CI] Add step to verify C API enum integrity. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10664
* Issue #10995: TIMETZ DST Fix by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11079
* Check Nested Types for UTF-8 Correctness by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11086
* Add `scope` column to `duckdb_settings` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11017
* Partitioned write - flush batches periodically (every 500K rows) instead of only writing when all data has been gathered by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10976
* [Python] Add `extract_statements` and the Statement class by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10891
* [Python] Improve performance of conversion to Numpy/Pandas for nested lists by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10826
* Fix an InternalException caused by DICTIONARY_VECTOR inside `map_from_entries` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11091
* Fix #11084 - fixes an issue with the Parquet writer when writing vectors of lists with repeated list elements (as can be generated through a join) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11094
* Add callbacks for newly added connections, and allow extensions to rebind queries as a result of planning failures by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11096
* Fuzzer #2376: INTERVAL Muliply Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11100
* Make test/sql/copy/csv/test_limit_spinlock.test a slowtest by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11088
* Fix #11063 - avoid throwing exception in InClauseRewriter by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11090
* Add a hint on how to resolve lockups when using ninja. by [@troycurtisjr](https://github.com/troycurtisjr) in https://github.com/duckdb/duckdb/pull/11074
* Fix LocalFileSystem::Read/Write, update location after read/write some data by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/11105
* run_tests_one_by_one - add a default timeout of 1 hour by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11104
* [Fix] Aliases in subqueries by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/11103
* [CSV Scan] Implement ignore_erros for Dates/Timestamps/Decimals by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11083
* Fix TaskScheduler deadlock on NumberOfThreads by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11093
* Fix return null constant in list_resize and list_aggr by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11111
* Add rowsort to more tests for queries that don't have a defined order by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11110
* Do not extract filters that cannot be hyper edges (Join Order Optimizer) by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11108
* Add Dictionary vector verification by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11114
* [Dev][Python] Make `test_httpfs.py` error test more lenient by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11125
* Fix `ConstantVector::Reference` for dictionary arrays by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11136
* Disable jemalloc for ARM distributions and clean up when closing DB by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11130
* Case senstivity issue secret manager by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11128
* Bump az aw vcpkg by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11127
* Fix broken micro benchmarks so they can be run weekly by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/11113
* Refactor OSX.yml, now inputs can be provided by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11133
* Merge main into feature by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11141
* Revert "Merge main into feature" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11145
* Fix upload assets script by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11144
* Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11132
* Fix upload assets OSX/2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11148
* Add more vector type verification tests/settings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11138
* Allow for customization of catalog lookup behavior for different catalog types  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11151
* [Python][Arrow] Don't deduplicate column names when outputting to Arrow by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11160
* More Array and Union fixes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11161
* Refactor upload logic (towards staged releases) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11156
* Fuzzer #2490: Generate NULL TIMESTAMPTZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11143
* Add folder parameter to upload logic and upload also twine artifacts by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11169
* CI: Find mirror issues among all issues, not just open issues by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11170
* Fix `TupleDataCollection` serialization of dictionary vectors containing nested data by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/11174
* Allow overriding of git describe also in scripts (via OVERRIDE_GIT_DESCRIBE environment variable) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11179
* Python staged releases: centralized staged upload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11187
* Fix RevertAppendInternal by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11177
* TwineUpload: Add awscli dependency + minor rework by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11193
* Fix issue in copy constructor of ExtraDropSecretInfo by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11190
* Unify CSV/JSON and Parquet Batch Writing Code - and fix memory management issues in CSV/JSON writing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11188
* More conservative dummy list entry estimation by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/11185
* retry on 500 error by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11184
* Fix warning on unused utf_type by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11198
* Remove outdated duckdb-node related scripts by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11180
* Add StagedUpload.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11189
* Improving CSV Casting error message by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11183
* Improve conversion error message in Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11199
* Fix thread sanitizer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11200
* Internal #1564: Range Join DISTINCT by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/11205
* small fix secret autoloading, bump azure by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11182
* CSV reader - suggest enabling null_padding and ignore_errors in case of missing columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11201
* CI: Create/label mirror issue job should list all internal issues by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/11204
* [Python] Add `IS NULL` / `IS NOT NULL` support to Expression API by [@cmdlineluser](https://github.com/cmdlineluser) in https://github.com/duckdb/duckdb/pull/11175
* Remove old assertions in SegmentTree by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11208
* [lambda] Fix for list_reduce giving the wrong result by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/11171
* [Dev] Fix various issues discovered by #11137 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/11210
* [Dev] Fix py override describe by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11209
* Sanitize CSV Newline identifier for writing CSV files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/11106
* Fix persistent secret file permissions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/11172
* Retry Binding Prior To Execution by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11149
* Avoid copying LogicalType in FlatVector::SetNull. by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/11214
* Review of CI on tags + add R extensions CI to InvokeCI.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11212
* Fix python and apply patches + bump extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/11217
* Disable jemalloc on arm in Python package as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/11218

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.10.0...v0.10.1

---

# v0.10.0 - DuckDB 0.10.0 "Fusca" <a id="v0100"></a>

*Released on 2024-02-13*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.10.0)

This release of DuckDB is named "Fusca" after the [Velvet Scooter](https://en.wikipedia.org/wiki/Velvet_scoter) native to Europe.

Note: The on-disk storage format is **backwards-compatible** with the 0.9 releases of DuckDB. For details, please see the [release announcement blog post](https://duckdb.org/2024/02/13/announcing-duckdb-0100.html).

Also note that we've dropped' the "Preview" designation with this release. DuckDB has matured quite a bit since we started creating releases back in 2019, and it is no longer appropriate.

## What's Changed
* feat(jdbc): support uuid param type by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9164
* Bump ADBC to v0.7 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9185
* Add support for parquet key-value metadata by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9126
* Default to JSON type if objects have an inconsistent structure by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9086
* Add `schema` parameter to `read_parquet` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9123
* [Python] Add the ability to provide a list of files to `read_csv`  by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8977
* Issue #7672: TIMESTAMP_XX to DATE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9279
* N-ary lambdas, and indexes as lambda parameters by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8851
* Feature: Fixed size list nested type (ARRAY) by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8983
* Fix unused warning by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9318
* Internal #215: Window EXCLUDE Functionality by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9220
* Add `json_serialize_plan`, json_serialize_sql tweaks by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9230
* Add create statement support to fuzzer by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9011
* Fix for issue #8108: Random() in lambda by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9353
* Fix Lambda Serialization by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9323
* Allow file_row_number with parquet schema option by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9290
* CSV - Always run sniffer by default by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9250
* [Python Dev] Import items lazily by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8741
* Array fixes + make validity more lazy by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9400
* Lambda performance revamp by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9395
* [Python] Support replacement scan on `connection.table(<name>)` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9427
* [Dev] Fix failure in Format Check CI job by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9516
* Fix parquet serialization by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9485
* Support gcs:// and r2:// URLs to read data from GCS and R2 by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/9388
* Don't reset validity target count by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9565
* Merge into feature by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9583
* Additional list functions by [@cryoEncryp](https://github.com/cryoEncryp) in https://github.com/duckdb/duckdb/pull/8907
* [Python] Support `Optional[...]` in DuckDBPyType by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8658
* C-API: support streaming arrow query by [@Virgiel](https://github.com/Virgiel) in https://github.com/duckdb/duckdb/pull/8642
* Add ToString and Print method for JoinRelationSetManager and Fix JoinNode Print by [@Light-City](https://github.com/Light-City) in https://github.com/duckdb/duckdb/pull/9040
* Removed artificial `HUGEINT` minimum by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/9441
* Parquet Encryption by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9392
* Internal #330: Quantile Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9461
* CAPI: Make it possible to create enum types by [@alnkesq](https://github.com/alnkesq) in https://github.com/duckdb/duckdb/pull/8788
* 5614 database invalidated by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9513
* Add support for proper scoping (catalog + schema) to custom types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9622
* Internal #576: strptime strftime infinities by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9615
* ATTACH IF NOT EXISTS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9627
* Small benchmark changes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9638
* add option for keep_alive setting by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9648
* Add "getenv" function to shell which can be used to read environment variables, and allow functions to be used in SET statements/PRAGMA statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9651
* Julia release by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9670
* In set operations ORDER BY columns refer to the first set operation in SQL - so the reference is not ambiguous by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9658
* Replace old logos by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9674
* Fix  dbgen/dsdgen when using custom catalog and schema by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/9686
* [Arrow] Properly use the parent's `array.offset` in many places in the scan by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9661
* Update issue template with API/extension repositories by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9693
* [Python] Fix lossy `datetime.timedelta` to INTERVAL conversion by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9688
* Issue template: Report vulnerabilities via dedicated channel by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9711
* Fix #9601: Call correct method in duckdb_pending_execution_is_finished by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9728
* Merge Feature Into Main by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9726
* feat(c): add functions for determining statement/return types by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9430
* Issue #9673: ICU DST Truncation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9705
* Deserialize header fields by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9687
* fix: restore support for windows network paths by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9725
* Constant time attach path lookup and locking to ensure unique file handles by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9671
* [ART] WAL serialization, automatic checkpointing, decoupling catalog and storage, index names by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9339
* Fix expanding structs in queries with ORDER BY by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9481
* Only emit batch indices valid within the current pipeline by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/9702
* Fix #9717: Correctly set null statistics of children of structs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9733
* Fixes to warning and rendering of bar() by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9734
* Don't show "blabla" as part of syntax error by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/9746
* Fix #9742: correctly catch empty ROW case in UPDATE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9744
* Explicitly attach duckdb file type by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9747
* For ATTACH - Resolve extension prefix before determining the name so "sqlite:file.db" is again correctly aliased as "file" instead of "sqlite:file" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9753
* Wasm: Add wasm_threads as a class of built extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9735
* Remove index joins by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9751
* Support EXCEPT ALL and INTERSECT ALL by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9636
* Add nightly deploy script by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9761
* update vcpkg by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9759
* Close s3 filehandle on destruction by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9758
* add list of collations that are required to determine equality.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9757
* Apply fix for patching vcpkg in extension workflow by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9767
* Internal #766: SkipList Coin Toss by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9772
* Support reading large decimals into doubles in the Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9770
* ATTACH - Always run ExtractExtensionPrefix also if a name is provided by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9771
* Issue #9762: Interval Fractional Seconds   by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9773
* Internal #716: Summarize approx_unique BIGINT by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9774
* Issue #9755: TIMESTAMP_XX DOUBLE Parts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9769
* Add support for COPY FROM DATABASE statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9765
* chore: move links duckdblabs -> duckdb by [@dpprdan](https://github.com/dpprdan) in https://github.com/duckdb/duckdb/pull/9779
* Detect FreeBSD platform by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9782
* Extention template: Enable DuckDB-Wasm extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9356
* Version: add info on v0.9.2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9788
* [JDBC] Sync all methods from a statement that interact with a query result by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9659
* format_bytes rework, moving from decimal multipliers to binary ones by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9736
* Make FORCE CHECKPOINT abort transactions of concurrently running queries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9790
* Bugfix/9768 by [@nbc](https://github.com/nbc) in https://github.com/duckdb/duckdb/pull/9791
* Cleanup raw pointers from transaction manager by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9237
* Partially fix #4182 - write distinct stats for string dictionary columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9518
* fix(python): minimal changes to support compiling for python 3.12 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9797
* Implement #2534 - add parquet_file_metadata function that supports scanning top-level file metadata by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9793
* Correctly clean up database path when an error is thrown in attach by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9792
* Fix cotangent(0.0): should also throw OutOfRange by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9799
* Call `BindSchemaOrCatalog` when binding functions so that we can qualify functions with only a database as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9810
* Fix #9739 - UNIQUE USING INDEX is not supported by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9809
* Fix #8596 - use ConstructConstantFromExpression for PIVOT IN list by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9813
* Fix #8500 - if we encounter any ambiguity while binding a function with a parameter we rebind during execution by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9814
* Remove watchOS from CI tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9820
* Fix #9262 - avoid checking exclusion/replace list when extracting table names by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9812
* LIST to VARCHAR cast fix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9819
* Fix #9806 - when an overflow is detected during filter pushdown the pushdown should be halted, instead of claiming the result is always false by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9816
* Parquet: Include column key-value metadata in `parquet_metadata` function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9798
* Add duckdb_optimizers function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9815
* Internal #805: Summarize NULL Percentage by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9822
* Add s3a s3n protocols for httpfs by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9817
* S3: Add more details to error on multipart upload by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9826
* CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9827
* [Python] Pandas Analyzer no longer trips up when the `pandas_analyze_sample` would only let it find nulls. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9811
* Create streaming result from a prepared statement. by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/9802
* Clear all updates during checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9829
* Fix #9825 - disable adding transitive filters for <> in filter combiner by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9832
* [Upsert] Do not require ON CONFLICT clause on INSERT OR REPLACE in some situations. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9730
* Issue #9631: Time/Interval Hours by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9643
* feat(c): support creating nested values in C API by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9438
* For EXPORT DATABASE - always write forward slashes in COPY statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9833
* Make checking the database path atomic again by turning db_paths into a bloom filter instead of a source of truth by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9828
* Issue #9785: Missing Interval Parts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9796
* Issue#604 Support collations during IN/NOT IN operations. by [@StarveZhou](https://github.com/StarveZhou) in https://github.com/duckdb/duckdb/pull/9724
* Reset expression before returning binder error by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9821
* Fix: Undefined behaviour in Bitpacking compression by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/9844
* Add ORDER BY to List_Select test by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9847
* CSV Sniffer Function by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9522
* Expand Progress API by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9531
* Fix #8095: Adjust the LG_PAGE parameter in jemalloc to accommodate the 64KB PAGE SIZE in aarch64 Linux systems. by [@vincent-chang](https://github.com/vincent-chang) in https://github.com/duckdb/duckdb/pull/9642
* Improve error message for index limitations by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9862
* Fix empty box in explain analyze statement by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/9860
* [Python] No longer scan `datetime.datetime.max` as infinity by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9848
* Move Wasm logic to inside CMake by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9830
* Fix s3fs close issue by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9846
* Fix TSAN issue related to db_paths_lock by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9868
* Fix #9863 - avoid moving constants for DATE - DATE subtractions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9874
* Disable progress bar test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9875
* add FROM to `InitialKeywords` vector in autocomplete extension by [@hamilton](https://github.com/hamilton) in https://github.com/duckdb/duckdb/pull/9877
* [Optimizer] regexp_matches fix InternalException caused by NULL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9872
* [ADBC Test] Prevent segfault in test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9871
* Fix progress test by properly initialising variables by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9882
* Capitalize URL in httpfs extension flags by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9884
* Mark BufferPool getters const by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/9885
* make BufferPool members protected by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/9886
* Parquet: Support more physical types of time columns with time zone by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9895
* docs(capi): add tests for prepared statement streaming by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9892
* Fix deadlock in LockClients when checkpointing multiple databases, and avoid locking all clients for regular checkpoints by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9898
* Disable copy constructor of connection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9899
* Add TableCatalogEntry to bind info by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9896
* Issue #9869: Strptime Week Start   by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9890
* Fix #9867 - correctly propagate relation name in COLUMNS expression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9904
* Fix progress bar (again) by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9905
* Safeguard uses of ColumnDefinition::DefaultValue by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9842
* Various CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9903
* [ADBC] Add support for windows. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9357
* Fix #8905 - make duckdb_rows_changed work with both new and deprecated results by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9907
* ART duckdb versions test requires 64-bit system by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9906
* Internal #751: Shared Window Partition by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9839
* Issue #9887: ISO Format Directives by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9910
* Fix: string to integer cast by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/9581
* [Test] Make `test_progress_bar.cpp` output more verbose by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9916
* Refactor and fix ART concurrency tests to avoid spurious CI failures by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9919
* Write old (empty) index_pointers to table metadata for forwards compatibility with v0.9.2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9923
* User agent in http header by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/9632
* Add support for vacuuming partial deletes during CHECKPOINT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9931
* JDBC: DuckDBNative - Close Shared Object InputStream Properly by [@brianwyka](https://github.com/brianwyka) in https://github.com/duckdb/duckdb/pull/9933
* Fix ATTACH of foreign key by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9932
* [DependencyManager] Rework internals of the DependencyManager by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9715
* Internal #873: Empty Aggregate Frames by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9936
* Add support for right_semi and right_anti. PR 2 by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9897
* httpfs: fix null pointer dereference in AWSEnvironmentCredentialsProvider by [@mlafeldt](https://github.com/mlafeldt) in https://github.com/duckdb/duckdb/pull/9953
* Limit initial combine capacity in RadixPartitionedHashTable by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9946
* [Python][Dev] Switch to using `pyproject.toml` when building and running CI. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9944
* Issue#9795 min/max doesn't use collation by [@StarveZhou](https://github.com/StarveZhou) in https://github.com/duckdb/duckdb/pull/9855
* [Arrow][UDF] Properly support `side_effects` parameter for Arrow UDFs. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9959
* JDBC - Appender for Decimal by [@Jens-H](https://github.com/Jens-H) in https://github.com/duckdb/duckdb/pull/9568
* [Fix] No duplicates in list_intersect by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9947
* [Python] Fix the ability to provide `pandas_analyze_sample_size` in the config dictionary to `connect` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9961
* [SQLLogicTest] Expected error message is no longer optional for `statement error` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9962
* fix offset type in list_casts and array_casts. by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/9972
* Issue #9978: Approximate Quantile Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9985
* fix regexp_replace bug by [@alitrack](https://github.com/alitrack) in https://github.com/duckdb/duckdb/pull/9938
* chore: Remove dead code by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/9992
* Internal #898: Totally Ordered Intervals by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9994
* Swift Readme.md small fix by [@atacan](https://github.com/atacan) in https://github.com/duckdb/duckdb/pull/9977
* Issue #9956: Alternative TIME Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9984
* Make IEJoin code more clear by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/9973
* Parallel Checkpointing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9999
* [Fix] ambiguous lambda parameters by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9974
* [Python][Dev] Disable test causing issues on Python3.7 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10005
* Shell: Many improvements/fixes to multi-line mode, enable multi-line mode by default by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10015
* Increase CLI history's max length to 1000 by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10006
* [Fix] nullptr dereference when analyzing nested types by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10004
* Improving error message when trying to open a locked database by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9988
* fix(function): fix ceil function by [@sundy-li](https://github.com/sundy-li) in https://github.com/duckdb/duckdb/pull/10014
* fix read parquet progress and read csv progress. by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/10013
* [Python][StreamQueryResult] Fix memory ownership issues in StreamQueryResult::FetchRaw by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9968
* Revert to old method of computing terminal size as new method does not play nice with lldb by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10026
* Issue #9762: Interval Fractional Parts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9954
* Fix #9380 and #9738 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9990
* Fix array subquery by [@chenzl25](https://github.com/chenzl25) in https://github.com/duckdb/duckdb/pull/10025
* Issue #4545: Windowed Distinct Aggregates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9754
* add rowsort to test by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10036
* The `UHUGEINT` type by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/8635
* build(python): fix python pkg version by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10049
* Add support for FixedPointDeclimals v0.5 by [@mcmcgrath13](https://github.com/mcmcgrath13) in https://github.com/duckdb/duckdb/pull/10039
* DuckDB Secrets by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10042
* Improve progress bar for Aggregation and limit threads for large data sizes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9989
* Internal #940: GCC Window Distinct by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10054
* Fix #10058: correctly handle unicode literals in regexp optimizer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10061
* Update database_size.hpp by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/10072
* enable overriding per-query working-memory target. by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/9544
* fix(c): fix duckdb_create_union_type by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10097
* Call InitialCleanup in PendingQuery(SQLStatement) by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/10083
* Removing useless variables by [@ywgrit](https://github.com/ywgrit) in https://github.com/duckdb/duckdb/pull/10082
* [WIP] Support dot notation for JSON by [@ankrgyl](https://github.com/ankrgyl) in https://github.com/duckdb/duckdb/pull/9499
* Refactor deploy script for extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10063
* Add list_reduce lambda function by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9909
* Handle s3_endpoint that includes path by [@tom-s-powell](https://github.com/tom-s-powell) in https://github.com/duckdb/duckdb/pull/9918
* Update year in license file to 2024 by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10103
* Not including stdlib for just size_t, stddef is smaller header by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10104
* Bump iceberg extension version by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10102
* Internal #783: ICU DatePart Serializers by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10055
* CI: Add backlink to original issue when its status changes by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10111
* Streamline handling issues that come with PRs fixing them by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10116
* Fix ParquetScanMaxThreads. by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/10113
* test(python): fix blind catches by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10118
* CI: Create separate job for handling 'PR submitted' label by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10119
* Lazy WAL creation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10086
* [BREAKING] Modify implicit casting rules to differentiate between string literals and VARCHAR columns, and disable implicit casting to VARCHAR for many types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10115
* For parsed expressions and table references - serialize query location, and obtain query location for more properties in transformer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10130
* Checksum WAL entries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10126
* Display unnamed structs as tuples instead of as structs with empty keys by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10134
* Fix #10008 - disallow parameters in DEFAULT clause, and remove unsupported SQLite code for handling parameters in shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10135
* Issue #10140: NULL Constant Lists by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10142
* feat(py): support python 3.12 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10144
* fix create_function python stub by [@yiyuanliu](https://github.com/yiyuanliu) in https://github.com/duckdb/duckdb/pull/10132
* fix(py): don't use jemalloc on windows by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10145
* Build manylinux_2_28 arm python wheels by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10137
* Slightly improve performance of the `first` aggregate function by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9957
* Add csv & parquet write functions and toPandas to experimental PySpark API by [@TomBurdge](https://github.com/TomBurdge) in https://github.com/duckdb/duckdb/pull/9672
* Add handling for duckdb-wasm extensions in extension-upload-from-nightly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9883
* Add some pg session function to pg_catalog by [@goldmedal](https://github.com/goldmedal) in https://github.com/duckdb/duckdb/pull/10156
* Fix CSE elimination for window functions with bind data. Fixes #10124 by [@How-u-doing](https://github.com/How-u-doing) in https://github.com/duckdb/duckdb/pull/10152
* feat(py): Py3.12 support for Windows by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10159
* Py3.12 Windows nightly fixes by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10160
* Serialization for scalar functions nextval and currval by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/10146
* Pushdown filters into semi and anti joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10110
* Issue #9950: Ordered Aggregate Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10045
* `uhugeint_t`/`hugeint_t` operator changes by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/10117
* add regexp_escape function by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/10044
* Infrastructure: truncate not always available in CI, use dd by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10162
* JSON S3 optimization by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10151
* Remove chunk collection from reservoir sampler by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10038
* Fix #10074 - for materialized CTEs the final result names are not influenced by the aliases. Only the names of the CTE itself are influenced by the aliases. by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10163
* [Python] Fix issue in DataFrame construction where non-deduplicated names were being used mistakenly by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10165
* Fix #10141 - Correctly handle recursive and nested types that refer to other types in CREATE TYPE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10164
* Suspend duckdb shell on Ctrl+Z by [@gsauthof](https://github.com/gsauthof) in https://github.com/duckdb/duckdb/pull/10172
* Fix #9456 and improve Deliminator by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9993
* Temporary Memory Manager by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10147
* Issue #10138: Finite Temporal Helpers by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10157
* Internal #425: TIMETZ Functions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10107
* Fix #10057: report correct error message when binding an aliased column fails by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10176
* Allow unquoted keywords to be used in DETACH  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10175
* Implement FILE_SIZE_BYTES by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9920
* [Parquet] Fix 10148, allow reading large byte arrays into small decimals for stats by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10183
* Throw binder error when returning list has no columns by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10184
* Fix missing move by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10186
* [BREAKING] Implicit cast rules for integer literals, and parameterized ANY for binding by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10194
* Handle 0-list maps (erroring out) and add test-case by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10187
* Internal #1001: SEM Test Determinism by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10197
* More work towards Custom Indexes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10032
* Collations are not yet properly serialized, remove enable_verification by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10206
* fix: reject creation of persistent secrets when allow_persistent_secrets=false for storage backends other than local_file by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10199
* prevent physical nested loop join with multiple conditions on semi an… by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10190
* chore: add `const` to BaseSecret and KeyValueSecret copy ctrs, fix compilation error by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10182
* Allow DESCRIBE/SHOW/SUMMARIZE to be used as a subquery by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10210
* Internal #1042: 2023d Time Zones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10215
* fix: fix a bug where free_space was incorrectly calculated when flushing partial blocks by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/10220
* Support more PG information_schema views by [@goldmedal](https://github.com/goldmedal) in https://github.com/duckdb/duckdb/pull/10222
* Fix Issue #10122: wrong result in IEJoin by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/10123
* Internal #861: Aggregation Absorb API by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9971
* Better Cardinality estimates for right and left semi/anti joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9976
* Open JSON files lock-free if there are many by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10188
* Bitpacking compression for the `UHUGEINT` type by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/10195
* fix: drop secret if exists on non-existing secret should not cause ex by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10217
* Replace 'embedded' with 'in-process' in the Python package description by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10232
* In .mode json in the shell use standard float output method by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10229
* Remove duplicate columns in `PhysicalHashJoin` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10203
* Out-of-tree extensions for R Windows by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10204
* [Python] Output unnamed structs as `tuple` in `fetchone/many/all` methods by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10174
* Internal #1022: Window TIME RANGE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10181
* fix(capi): add basic TIME_TZ support by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10207
* Lambda scoping by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10150
* Add batch functionality by [@osidekyle](https://github.com/osidekyle) in https://github.com/duckdb/duckdb/pull/10011
* Make FILE_SIZE_BYTES test more lenient by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10234
* Allow SQLNULL to be bound in VALUES list by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10238
* Sequence clean-up - move all sequence access through a SequenceData entry that is concurrency safe by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10236
* Remove duplicate join conditions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10235
* UNPIVOT - maintain original types and throw a better exception if type matching is not possible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10240
* Correctly account for ORDER BY in ColumnLifetimeAnalyzer optimization pass by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10242
* CSV Parser 2.0 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10209
* COPY - allow copy_file_name to be formatted as identifier by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10246
* remove C-style cast in compression module by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/10256
* Allow dsdgen to be interrupted by user by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/10262
* Upgrade the schema of `pg_proc` to PostgreSQL 16 by [@goldmedal](https://github.com/goldmedal) in https://github.com/duckdb/duckdb/pull/10248
* chore: improvements to duckdb_api / user_agent by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/10226
* Issue #10249: Window Clause Casing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10259
* Fix issue 10254 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10265
* Store unqualified macro parameters, qualify before binding by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10266
* Fix 9384 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10267
* Fixes #10212: Correctly account for non-flat vectors in ListColumnData::Skip by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10268
* Enable intercepting file copy extension after binding by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10255
* [Dev][Util] Have `unittest` respect the `--start-offset` parameter when used alongside `-l` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10277
* Issue #10272: DATE + INTERVAL by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10274
* Fix #10279 - correctly use unsigned integers in delta decoding to wrap overflows as specified by the spec by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10288
* Add parse_path(), parse_dirname() and parse_filename() functions by [@chrisiou](https://github.com/chrisiou) in https://github.com/duckdb/duckdb/pull/10208
* [Compression] ALP Compression (float/double) by [@lkuffo](https://github.com/lkuffo) in https://github.com/duckdb/duckdb/pull/9635
* Add function for non-bias-corrected kurtosis by [@david-cortes](https://github.com/david-cortes) in https://github.com/duckdb/duckdb/pull/9545
* fix the problem of fetching wrong data when using bitpacking compression by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/10291
* [Python] Compatibility with `pandas==2.2.0` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10290
* Avoid re-rendering the progress bar if the percentage has not changed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10284
* Adapt further for z/OS by [@v1gnesh](https://github.com/v1gnesh) in https://github.com/duckdb/duckdb/pull/10297
* CSV Parser Optimizations: Pre-computed skip list. Simpler state machine transition. Flip state machine states and transitions. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10258
* Explicitly cast FTS column to VARCHAR by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10299
* Add table macro_definition to duckdb_functions() by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10301
* [CSV Parser] Fix regression with dialect detection on quoted values. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10307
* Improve bitpacking skip performance + better testing of FetchRow by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10295
* Fix #10308 - allow describe/summarize as prepared statement, and fix issue with describe/summarize with ctes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10311
* CSV Reader making null padding Parallel by default by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10306
* Remove spinlock for closing JSON files by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10300
* Fix NumericLimits<hugeint_t>::Minimum() * 0 case by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/10319
* C API updates by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10317
* Add create_sort_key function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10321
* SQLLogicTestRunner - Make mode command work in loops, and add mode no_output by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10328
* Escape all ASCII control characters in duckbox rendering by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10327
* Fix Failing Nightly Swift test by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10320
* Basic struct filter pushdown by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10314
* Improve the check for glob in sniff_csv function. by [@gabihodoroaga](https://github.com/gabihodoroaga) in https://github.com/duckdb/duckdb/pull/10243
* Add an icon to the duckdb.exe shell executable by [@renevdzee](https://github.com/renevdzee) in https://github.com/duckdb/duckdb/pull/9656
* [Arrow] Support scanning REE (Run End Encoded) Arrow arrays by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9836
* [Compression] Fix Handling of -0.0 in ALP by [@lkuffo](https://github.com/lkuffo) in https://github.com/duckdb/duckdb/pull/10335
* Split jdbc tests by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10338
* Set interrupted flag after pushing an error to prevent race condition where the InterruptException could end up being the top-level error by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10337
* [Python] Fix bug in conversion of INTERVAL to `datetime.timedelta` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10339
* Update Postgres and SQLite extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10310
* Limit the number of threads used to scan distinct aggregates by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10318
* Fail Regression test when difference in cardinalities is detected by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10340
* pin ccache action version by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10344
* test_all_types.py: Formatting according to black 24 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10353
* Allow NULL bytes in ART indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10325
* Ensure version numbers passed to Windows .rc file are numbers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10358
* Feature: Digit separators in numeric literals by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10343
* Autocomplete small improvements by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10370
* Fix: correctly set list size of dictionary vector by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/10369
* Check black version in script/format.py by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10354
* Change extension_directory default by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10359
* feat(jdbc): setBytes by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10365
* [Block Size] CI test for 16KB block size and related code changes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9967
* CI: Add workflow to check new issues for code formatting by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10149
* Add additional STRUCT expansion tests by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/10373
* Fix MATERIALIZED CTE issue #10260 by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/10386
* Add table_sample to TableStatistics (currently saved as nullptr) by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10378
* [Python][Dev] Use `duckdb_cursor` to avoid unintentionally sharing catalogs and registered objects by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10388
* Extension metadata: detecting the platform by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10329
* Add missing checkpoints in test by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10389
* Remove Python function signature (in test) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10399
* Avoid requiring expected error message on original sqlite tests by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10392
* Case insensitive extensions install & load by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10380
* Platform detection: Fix thread sanitizer job passing absolute path by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10398
* [CSV Reader] Implicit Casting and Projection Pushdown by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10390
* CI: Fix workflow to check new issues for code formatting by using heredoc by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10403
* Rework Exception Internals by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10410
* avoid copying in the for loop when there is a const by [@zhouzilong2020](https://github.com/zhouzilong2020) in https://github.com/duckdb/duckdb/pull/10418
* Fix drop secret bug by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10185
* Issue template: Ask about testing with the nightly build (instead of 'main') by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10405
* [CSV Reader] Use array instead of unordered_map in projection pushdown by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10411
* [C-API] Add duckdb_appender_column_type by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/10401
* Fix results for anti joins on empty tables by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10413
* Don't write Chimp/Patas files anymore & deprecate patas and chimp by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10423
* Small secret manager refactor by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10421
* [Python][Dev] Skip pyarrow `test_struct_filter_pushdown` on python3.8 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10419
* Add `read_text` and `read_blob` table functions by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10376
* Rework FunctionSideEffects to FunctionStability - allow NOW() to be pushed down by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10426
* Remove dev logging on local_extension_repo creation by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10424
* GH Workflows: Create CI job for Coverity scan by [@moshekaplan](https://github.com/moshekaplan) in https://github.com/duckdb/duckdb/pull/10433
* Issue #10224: FIRST ORDER BY  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10347
* Coverity Scan: Project name is DuckDB by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10447
* Multiline mode: add continuation prompt rendering by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10425
* Python: fix exception hierarchy, and also catch std::exception by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10420
* Fix bug with full file download by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10429
* Add cloudflare invalidation to nightly deploy script by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10430
* fix(py): fix building python binding from cmake by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10445
* [CSV] Bug Fix related to quoted values starting with empty values by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10438
* Add COMMENT ON statement by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10372
* CLI: Highlighting for continuation tokens by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10453
* Issue #10224: ORDERED FIRST Rewrite  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10457
* add support for date, time, timestamp types to the Julia appender api by [@rdavis120](https://github.com/rdavis120) in https://github.com/duckdb/duckdb/pull/10449
* Bugfix/#10441 correctly validate second colon in jdbc url parameter in Java client. by [@peteraisher](https://github.com/peteraisher) in https://github.com/duckdb/duckdb/pull/10442
* [Execution] Parallel StreamQueryResult by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10245
* [Julia][Dev] Improve README by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10464
* Linenoise Code Cleanup by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10461
* [Bug Fix] [CSV Sniffing] Removing double quotes in header by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10462
* [Add Test] [CSV Parser] Type Detection on columns with null values by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10465
* Unconnected fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10467
* CLI: Only show continuation bytes while editing the query by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10470
* [CSV Reader] [Add Test] Quoted Values impacting the column sniffing. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10472
* GzipFS - use unique_ptr instead of new/delete by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10474
* Group together index instantiation parameters into a struct, pass options map as well. by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10471
* Patch to build on Windows ARM 64 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10479
* [Bug Fix] [CSV Reader] Fix to using null_padding in conjunction to one of the multifile reader options by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10473
* More linenoise/CLI improvements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10480
* Add documentation example for Julia appender api. by [@rdavis120](https://github.com/rdavis120) in https://github.com/duckdb/duckdb/pull/10475
* Linenoise: add support for many more alt command sequences by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10493
* Use `CMAKE_CURRENT_BINARY_DIR` in CMakeLists by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/10484
* Avoid setting `DUCKDB_NORMALIZED_VERSION` to an empty string by [@SChakravorti21](https://github.com/SChakravorti21) in https://github.com/duckdb/duckdb/pull/10492
* Tag memory that is allocated through the buffer manager, and add `duckdb_memory()` function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10496
* Linenoise: Disable automatic auto-complete rendering by default for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10498
* Fix edge case in RANGE for dates/timestamps when start=end by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10499
* Fix for auto-complete on empty words so behavior is consistent with previous DuckDB by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10502
* Nested Array Validity Fixes + `RowOperations` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10483
* Keep file extension for temporary files by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10459
* bundle-library: Add optional Makefile target by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10507
* Fix #10363 - prefer selecting entire rows over SQL value functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10505
* [CSV Reader] Avoid unnecessary writes to temporary file when reading in limited memory cases by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10509
* [Dev] Fix ASAN thread limit exceeded issue in CI by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10510
* [Dev] Cancel tasks in EndQueryInternal by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10512
* Export stack trace as part of extra exception info if DUCKDB_DEBUG_STACKTRACE is defined (DEBUG_STACKTRACE cmake variable) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10514
* feat: make SecretEntry copyable so we don't lose the underlying BaseSecret obj for non-CatalogSet secrets by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/10518
* fix(py): json type in description field by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10521
* Decorrelation and parallelization of recursive and materialized CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/10357
* Keep track of view names and aliases separately so we can distinguish between explicitly provided aliases by the user and names returned by the view, and block usage of view if names changed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10500
* Tweak `TemporaryMemoryManager` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10503
* On *nix, return `errno` in IOException extra_info by [@philippmd](https://github.com/philippmd) in https://github.com/duckdb/duckdb/pull/10529
* Use null cast instead of reinterpret for NULL -> JSON by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10526
* [Python] Fix various small issues by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10533
* [CSV Reader] NullPadding Tests by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10530
* Linenoise: make ENTER behave more similarly to other CLI clients - Ctrl+X can now be used to enter newlines at the cursor position by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10527
* [Python][Dev] Add `PYTHON_EDITABLE_BUILD` to Makefile by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10488
* Reset git status before applying patches in out-of-tree build by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10534
* Fix #10486 - allow out-of-order struct casting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10537
* Make ClientContext available during attach by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/10531
* feat(jdbc): setDate by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10408
* Fix unused variable warning/error by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10542
* [Dev]: ICU 2024a TimeZones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/10544
* Path utility fixes by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10538
* Support struct_extract and unnest for unnamed structs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10541
* [Dev] Fix isses in parallel Checkpoint by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10525
* More `TemporaryMemoryManager` tweaks by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/10549
* Add order to tests by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/10536
* Require at least 1 argument when calling ListZip during bind by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10485
* Benchmark runner: check for errors also if no result is specified by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10554
* [CSV Reader] [Bug Fix] Nightly CI Segfaults by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10551
* Fix for test/sql/copy/file_size_bytes_large.test_slow test by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10552
* Simplify binary-search in FindRunIndex by [@felipecrv](https://github.com/felipecrv) in https://github.com/duckdb/duckdb/pull/10487
* Remove query profiler history and add hooks for certain events in the ClientContext by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10504
* [CSV Reader] Reset state on quoted/escaped when applying projection pushdown by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10557
* CommitState::WriteCatalogEntry refactor by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10555
* [CSV Reader] Fix 9952 and race condition on error handler by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10558
* Fix a few tests failing non-deterministically with ALTERNATIVE_VERIFY=1 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10560
* unittester: if test-dir is provided avoid deleting it by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10564
* Allow DuckDB execution without implicit main thread by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/10548
* Fix #10528 - disallow parsing exponents for integers in strict parsing mode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10559
* [Python] Fix issues related to handling of Python exceptions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10563
* [Python] Fix crash caused by `fetch_record_batch` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10565
* [Dev] Skip some tests on ALTERNATIVE_VERIFY by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10567
* [Python][Dev] Test does not throw HTTPException by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10568
* [Export] Fix export of user-defined types by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10569
* Fix heap buffer overflow in VARCHAR -> TIME trycast by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10571
* [Dev][CI] Add --no-exit to run_tests_one_by_one by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10572
* Handle also branch with no threads enabled by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10573
* Deduplicate code dealing with deduplication of column names by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10532
* Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10580
* extension_distribution.yml: Pass DUCKDB_PLATFORM by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10582
* chore(jdbc): correct datetime delta by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/10584
* Fix Nested Array TupleData Serialization by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/10513
* Do not replace filters that evaluate to always true by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10553
* [Dev] Fix triggered assertion in `SortedAggregateState::FlushChunks` caused by a small STANDARD_VECTOR_SIZE by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10202
* [Tester] Add `--require <name>` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10579
* Add Support Options page by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/10598
* Use all threads to read multiple parquet files. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/10590
* [CSV-Reader] Fix on finalize for projection pushdown + nullpadding by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10596
* [Julia] Remove `DataFrame` from Project.toml by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/10605
* [CSV Reader] [Bug Fix] Make CSV Results hold the buffers they depend on by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/10589
* minor secret manager fix by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10600
* Point error message to stable link by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10592
* Fix issue in aggregate HT where a task could be blocked and never be unblocked if the aggregation was interrupted early due to e.g. a limit by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10604
* Memory tracking - explicitly zero-initialize memory tracking arrays by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10606
* [Dev] Bump extensions & apply patches by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10603
* Secret folder by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/10607
* JDBC: Skip combine test run because #10338 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/10616
* Fix for SQL value functions when there is an alias specified by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/10611
* delay secret storage initialization by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/10612

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.9.2...v0.10.0

---

# v0.9.2 - 0.9.2 Bugfix Release  <a id="v092"></a>

*Released on 2023-11-14*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.9.2)

This is a bug fix release for various issues discovered after we released 0.9.1. There are no new features, just bug fixes. Database files created by DuckDB v0.9.0 or v0.9.1 can be read by DuckDB v0.9.2 (i.e. v0.9.2 is backwards compatible with both v0.9.0 and 0.9.1 and vice versa).

## What's Changed
* [Dev] Fix Wasm.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9303
* [Dev] Fix Wasm.yml, hardcoding extension config to latest duckdb-wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9307
* Fix R CMD check script by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9326
* [Dev] Remove unused tools/wasm folder by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9328
* [ODBC] SQLColAttribute fix by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9316
* Fix typo by [@shreeve](https://github.com/shreeve) in https://github.com/duckdb/duckdb/pull/9313
* [Dev] Trigger R.yml only only if there are changes to R.yml itself by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9304
* Add thread limit to test by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9305
* fix typing_extensions ImportError in experimental spark api by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9346
* HTTPFS: Move from HTTPException to base class IOException by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9351
* fix for System.Data.ODBC GetSchema() by [@bucweat](https://github.com/bucweat) in https://github.com/duckdb/duckdb/pull/9336
* Removes some static global variables by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/9310
* Bump Julia to 0.9.1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9354
* [Optimizer] Fix transitive filter issue by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9337
* Julia - v0.9 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9359
* fix time_bucket_tz(day): don't truncate input to a day boundary in https://github.com/duckdb/duckdb/pull/9320
* Increase the minimum cmake version to 3.5 by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9364
* [PyArrow] Fix bug in timestamp pushdown by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9377
* Satisfy GCC's LTO checks by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/9386
* New generate_query_graph tool. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9212
* Fix LIST aggregate prepare statement exception by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9370
* [Python] Throw explicit error for misuse of `execute` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9394
* update R CMD workflow to apply patches in .github/patches/duckdb-r by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9412
* [UnionVerify] Properly deal with SelectionVectors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9409
* [ART] Improve error message for zero bytes in BLOBs by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9415
* Enable serialization of LogicalCopyToFile by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9418
* Nits for storage and Python API comments by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9414
* Issue #9416: Windowed Peer Functions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9425
* [Python] Adjust `relation.df()` to output microsecond precision for `DATE` types. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9362
* [Python] Support PEP 563 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9385
* Fix #8185 - avoid infinite recursion in AddTransitiveFilters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9440
* Fix 9447: SIGSEGV when executing read_csv() query for struct with empty VARCHAR by [@ryderblue](https://github.com/ryderblue) in https://github.com/duckdb/duckdb/pull/9448
* Fuzzer #1294: Non-Constant NULL Format by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9450
* GitHub Actions bot: Prune search space with '--search' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9445
* Issue #9396: AsOf Inequality Optimisation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9449
* Add bot for the 'Needs Documentation' label by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9444
* Fix field ids in LogicalCopyToFile:Deserialize by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9424
* [Export Database] Produce up-to-date query for ViewCatalogEntry by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9375
* include csv_rejects_table headers for amalgamation by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9454
* feat(jdbc): result streaming by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9437
* [Arrow] Add support for dictionary's in child arrays (i.e list of ENUM) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9331
* Detect AppleClang in cmake, add defines for `DUCKDB_MAJOR/MINOR/PATCH_VERSION` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9457
* [Dev] Fix build for extension-upload-wasm to fix (avoiding manual copy) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9467
* Fix #9459 - remove unused qualified name parsing by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9472
* Add license to Swift client by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9446
* Issue #8937: Window Order Collation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9477
* adding System.Data.ODBC testing to Windows.yml CI. by [@bucweat](https://github.com/bucweat) in https://github.com/duckdb/duckdb/pull/9372
* fix(jdbc): support decimal arrays by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9489
* Needs documentation workflow: Use correct event by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9464
* Needs documentation label: Add PR number in backlink by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9491
* Fix 9399 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9411
* Enable option to skip building duckdb shell in extension distribution CI by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9483
* fix confusing variable name by [@SkyFan2002](https://github.com/SkyFan2002) in https://github.com/duckdb/duckdb/pull/9503
* Add MySQL Scanner Aliases + Enable Autoloading by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9505
* Fix #9498: Amalgamation to properly define DUCKDB_VERSION by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9500
* Issue #582: Greenland TimeZone Change by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9508
* [Union] Fix issue with keyword/quoted UNION member names. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9432
* Dev: Avoid adding name_extension for extensions with DONT_LINK by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9496
* Implement array-based JDBC ResultSet by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/8972
* Fix #9360, fix #9466: grab a lock before creating directories to fix race condition on Windows in partitioned write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9473
* Internal #582: Remove utc_offset Dependency by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9521
* [ART] Don't allow index creation in readonly mode by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9527
* Remove redundant class by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/9511
* Hive partitioning: Fix preprocessing of CreateDirectories by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9535
* fix: check for IsRowId before accessing column name by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/9542
* Commit drop of index memory by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9540
* [Catalog] Fix locking issues + identify problem in MappingValue by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9523
* JDBC - Add append method for LocalDateTime by [@Jens-H](https://github.com/Jens-H) in https://github.com/duckdb/duckdb/pull/9435
* Use run_tests_one_by_one to fix CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9570
* pin run-vcpkg action version by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9579
* Add rowsort to test_window_order_collate.test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9574
* Fix exploding Delim Joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9564
* HivePartition: Add also lock on partition_state by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9576
* Fix typo by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9587
* [C-API] fix duckdb_parameter_name declaration by [@suketa](https://github.com/suketa) in https://github.com/duckdb/duckdb/pull/9566
* Fix incorrect template specialization by [@jhammer](https://github.com/jhammer) in https://github.com/duckdb/duckdb/pull/9529
* fix(jdbc): allow use of nested result values after close by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9592
* Allow pausing pipeline in NextBatch call by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/9562
* Optimize performance of jaccard function by [@ucasfl](https://github.com/ucasfl) in https://github.com/duckdb/duckdb/pull/9560
* [Python] Add missing default values to stubs of aggregate functions. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9595
* Fix symbol leakage check by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9604
* Issue: #8867 Fix: remove unused variables for logical_root. by [@Light-City](https://github.com/Light-City) in https://github.com/duckdb/duckdb/pull/8866
* CI: Add job for 'needs maintainer approval' PR tag by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8853
* Ci: Fix trigger of 'needs maintainer approval' job by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9610
* fix(jdbc): combine jar publish steps by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9484
* Increment postgres_scanner version by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9504
* Improve linear probing performance of `GroupedAggregateHashTable` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9575
* Expose InterruptState in NextBatch by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/9606
* [Arrow] Support LargeString and LargeList by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9471
* Issue #9589: Prefer strict TIMESTAMPs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9600
* Fix issue with streaming query results by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9619
* bump extension versions as prep for 0.9.2 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9621
* feat: duckdb_api and custom_user_agent options by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/9603
* Revert "fix(jdbc): combine jar publish steps" by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9620
* Read JSON bugfix by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9623
* Fix #9548 - Throw a more clear error when using parameters inside of the source of a top-level PIVOT statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9626
* Add SQL:2016 listagg by [@renevdzee](https://github.com/renevdzee) in https://github.com/duckdb/duckdb/pull/9613
* Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9633
* [ODBC] Reorganize the SQLColAttribute Tests by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9580
* Fix #9584: Correctly bail-out on committing appends of 0 rows, which can happen in certain edge cases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9640
* Add log(b,x) function by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9637
* allow dbgen to be interrupted by user by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/9624
* Fix httpfs CI  by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9649
* fix 9232 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9647
* Shell: Set `globalDb` to `NULL` after closing database by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/9655
* Fix #9308 - avoid pruning plan for ANTI join with filter that is always true by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9654
* Serialize decimal quantiles by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9653
* Partial revert of #9624: test seemed to cause some memory leaks in CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9660

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.9.1...v0.9.2

---

# v0.9.1 - 0.9.1 Bugfix Release <a id="v091"></a>

*Released on 2023-10-11*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.9.1)

This is a bug fix release for various issues discovered after we released 0.9.0. There are no new features, just bug fixes. Database files created by DuckDB v0.9.0 can be read by DuckDB v0.9.1 (i.e. v0.9.1 is backwards compatible with v0.9.0 and vice versa).


## What's Changed
* Fix missing header in nightly GCC build by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9109
* Add scripts for cancelling/rerunning workflows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9120
* Update R-CMD-Check workflow by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9128
* CSV error message fix by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9132
* Throw SerializationException instead of InternalException by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/9130
* Radix HT: Get max_threads from config instead of system by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9129
* Wrapping CSV State Machine by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9131
* [CSV] Properly skip new lines mid csv file by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9139
* [PythonDev] Rework `duckdb_cursor` fixture in pytest by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9140
* Update logo in README by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9147
* Bump uncovered lines by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9102
* Python: Uniform DuckDB SQL version to v0.X.Y by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9095
* [PythonDev] Don't dereference None when creating pandas dataframe by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9127
* fix: fix some typo by [@shizuocheng](https://github.com/shizuocheng) in https://github.com/duckdb/duckdb/pull/9156
* [Swift] fix row count and index mapping by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/9149
* Run Single-Threaded CSV Parser when only one thread is available by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9148
* [ODBC] Add missing fields to SQLColAttribute   by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9146
* Merge main into feature by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/9163
* [Python] Pyarrow integer filter pushdown bug fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9155
* [CSV] Be sure to run header detection even if a header is defined by the user by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9168
* Avoid (Try)AutoLoad logic if extension already loaded by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9177
* Fix fuzzer exclusion by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/9103
* [PythonDev] Fix #duckdb-internal/418 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9184
* chore: skip arrow union tests on pyarrow<11 by [@gforsyth](https://github.com/gforsyth) in https://github.com/duckdb/duckdb/pull/9186
* Fix issue related to `map()` and Dictionary Vectors. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9046
* Issue #9183: Arbitrary ASOF Conditions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9188
* Add instructions for jdk installed via brew by [@nicku33](https://github.com/nicku33) in https://github.com/duckdb/duckdb/pull/9192
* Fix nits in API comments by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8768
* Internal #445: Destruct All Aggregates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9202
* Don't initialize data chunk in ExpressionExecutor if it's just a BoundReferenceExpression by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9213
* [ODBC] Add info to fatal error in compiler by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9218
* Rewrite filter remover arrow test by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9217
* [ODBC] Add Unittests to Windows CI Run by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9216
* Add missing parameter defaults for `create_function` in `duckdb-stubs` by [@earwig](https://github.com/earwig) in https://github.com/duckdb/duckdb/pull/9224
* Several fixes related to vector_size=2 nightly build by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9166
* Avoid keeping read-only transactions stored in `old_transactions` by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9236
* Fix reusable workflow for OOTE building by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9229
* [Parquet] Implement reading byte stream split encoded data by [@adamreeve](https://github.com/adamreeve) in https://github.com/duckdb/duckdb/pull/9240
* Bug report template: ask for imports to be included by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/9197
* Remove bundled sqlite, does not seem to be used anywhere by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9245
* update azure extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9243
* Fix #8413: Avoid pushing collations to non-varchar columns, and cleanup around PushCollation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9242
* Fix #8624 - allow changing of schema and search_path parameters even if configuration is locked by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9244
* [ODBC] SQLColAttribte: More tests  by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/9200
* Fix for creating ephemeral schema on readonly by [@nicku33](https://github.com/nicku33) in https://github.com/duckdb/duckdb/pull/9261
* Wasm extensions Makefile changes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9269
* Fix #9241 - avoid pushing filters through DISTINCT ON by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9270
* Fix #7880 part 1 - rebind expression during alias replacement instead of copying the already bound expression by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9274
* ICU: Remove unused variables by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9275
* Fix #9252 - avoid overwriting start value as part of INCREMENT BY in sequence creation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/9272
* [Python] Add back `value_counts` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9278
* [SparkAPI] Add `read.json` and `read.parquet` + some unhappy path testing by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9276
* [Arrow][Dev] Make each produced Array own its own memory. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9254
* Properly register all JSON cast functions so the binder can disambiguate by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9209
* [Dev] Fix `test_map_vector_types.test` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9277
* Issue #9280: Parquet TIME_TZ Reading by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/9283
* Update iceberg extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/9284
* Fix prepare statement issue by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/9288
* [Arrow] Fix issue with scanning of UNION of STRUCTS by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/9291
* Remove nodejs client by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9287
* Clear cached buffers before emitting next chunk by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/9295
* [Dev] Restore _extension_client_tests.yml syntax by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9300
* Fix MacOS exception catching by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9286
* Unify replacement scan filename parsing by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/9273
* Extension install fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/9294
* Re-add windows extension builds for R by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/9302

---

# v0.9.0 - 0.9.0 Preview Release "Undulata" <a id="v090"></a>

*Released on 2023-09-26*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.9.0)

This preview release of DuckDB is named "Undulata" after the aptly named [Yellow-billed duck](https://en.wikipedia.org/wiki/Yellow-billed_duck) native to Africa.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

## What's Changed
* [Dev] Merge master into feature by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7535
* Issue #7563: make_timestamp[tz](microseconds) by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7597
* Add support for nested laterals by [@arhamchopra](https://github.com/arhamchopra) in https://github.com/duckdb/duckdb/pull/7528
* Issue #7563: epoch_us(temporal) by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7629
* Fix lingering clang-tidy issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7670
* Add list_intersect, list_has_any, and list_has_all by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/7518
* Issue #7563: epoch_xs(temporal) by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7648
* Pivot - dynamically switch between using filtered aggregates or the new pivot operator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7688
* Add wildcard to JSON Path by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7624
* [Dev] Add optional build flag to disable assertions in debug mode by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7618
* [DEV]: ICU C Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7715
* List_resize by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/7401
* Issue #7187: AsOf Join Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7607
* Some minor CI changes by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7763
* Binder coverage by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7791
* Vacuum Completely Deleted Row Groups by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7794
* Issue #7187: AsOf Coverage by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7774
* Implement FIELD_IDS for parquet writes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7696
* Optimize Regexp_matches to LIKE statements when possible by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7264
* Jemalloc configuration, more buffer allocator, and remove redundant string copying in parquet dictionary by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7697
* Truncate Database File on Checkpoint by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7824
* LEFT JOIN ON TRUE support by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7821
* Issue #7809: Segment Tree Performance  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7831
* C Data Interface: `duckdb_arrow_scan` and `duckdb_arrow_array_scan` by [@angadn](https://github.com/angadn) in https://github.com/duckdb/duckdb/pull/7570
* Update Julia to 0.8.1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7932
* Add conn.interrupt() to DuckDB python API by [@henrinikku](https://github.com/henrinikku) in https://github.com/duckdb/duckdb/pull/7895
* renaming part of extension build refactor PR by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7926
* fix swapped x/y regression parameters by [@MartinNowak](https://github.com/MartinNowak) in https://github.com/duckdb/duckdb/pull/7855
* [Docs] Aggregate function README.md by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7881
* PhysicalPiecewiseMergeJoin improvement by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/7832
* Initial set of commits to add support for zOS (an IBM mainframe operating system) by [@v1gnesh](https://github.com/v1gnesh) in https://github.com/duckdb/duckdb/pull/7805
* test(nodejs): add test_all_types.test.ts by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7740
* Issue #7879: Missing JDBC TIMESTAMP_TZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7922
* Attempt to fix CI on Windows 32 and Python on Windows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7961
* Fix 7947 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7963
* test: patch test_7652 to skip on pyarrow<11 by [@gforsyth](https://github.com/gforsyth) in https://github.com/duckdb/duckdb/pull/7966
* NodeJS: Add `columns()` method to get type info from prepared statement by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7948
* Fix: Don't free arrow children explicitly by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7917
* CSV Rejects table by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7681
* Issue #7809: Segment Tree Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7891
* Add tpch benchmark run exclusively on parquet files by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7519
* Bidirectional check storage + minor CI fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7955
* [Swift] fix #7985 by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/7993
* Move [@samansmink](https://github.com/samansmink)'s extension_header_rename.patch by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8001
* [Python] Properly use NumPy array `stride` when scanning `object` arrays. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7964
* CI - No longer run on PR synchronize, instead run on ready_for_review  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8007
* Parallel pipeline execution should call NextBatch on first batch by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/7978
* Micro-optimization for generating collation keys by [@Krechals](https://github.com/Krechals) in https://github.com/duckdb/duckdb/pull/7983
* Multiple assignment for `UPDATE SET` by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/7968
* CI job to move synchronized PRs to draft by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8010
* [ADBC] ConnectionGetTableSchema and StatementSetSubstraitPlan Functions by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7914
* Issue #7852: Window Vectorisation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7996
* Moving JDBC Linux x64 builds to CentOS 7 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7991
* CI Draft - token is called GH_TOKEN by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8016
* Add support for materialized CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/7126
* Reduce memory usage of Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7995
* CI auto draft: pass token via environment + avoid wrapping action by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8024
* CI autodraft: use implicit variable [test] by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8027
* remove duplicate pivots declare by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/7992
* Fix typo in fts indexing exception by [@alexanderchiu](https://github.com/alexanderchiu) in https://github.com/duckdb/duckdb/pull/8034
* Fix issue 7988 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8023
* Delete DraftMe.yml by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8048
* Fix 3eb9ab34db1: Remove unneeded move by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8038
* [CI] Skip many more CI jobs for pull requests, and add make coverage-check to run coverage locally by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8046
* Extension build configuration refactor by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7735
* Compressed Materialization by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7644
* [Relation] Add support for creating an empty `ValueRelation` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7967
* Join Order Optimizer has duplicate enumerations and lost some neighbors by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/7358
* Fix CI wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8057
* [CI] More CI reduction and clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8052
* Restore auto-draft functionality by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8058
* Move WebAssembly.yml to NightlyTests.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8060
* Unskip, attach HTTPFS test, and create HTTPState when the opener is not available by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8012
* CI fixes: Don't persist ccache for nightlies by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8075
* Fix regression & fix draft mechanism by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8071
* CI compliance feature branch by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8070
* Fix python flaky test (potentially GET requests gets back 403) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8074
* [Arrow] Fix segfault in appending list data by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8042
* Issue #7852: Window Vectorisation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8050
* CONTRIBUTING.md by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8077
* Add ORDER BY clause to query in test_bool.test by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/8082
* ART test and benchmark refactor by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8055
* Update plan cost runner script to remove 20% threshold for cardinality estimates by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7989
* Fix #8067 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8090
* ART prefix refactor by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7930
* Bump Substrait by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8110
* Merge feature into master by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8136
* Increase memory limit in test to prevent non-deterministic CI failures by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8138
* UNNEST binder fix by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8111
* Out-of-Core Hash Aggregate by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7931
* Add Unittests for ODBC by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/7875
* Hive types by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7674
* CppCheck & CodeQL on master by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8113
* Fix CI for Nodejs and OSX by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8148
* Skip failing test on R on CI by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8161
* Disable failing R tests for now, and disable test_arrow_progress on Windows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8155
* Allow disabling of extension loading (through a CMake flag) and allow selectively disabling specific file systems by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8152
* Fix FTS + ATTACH by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8153
* fix: cli parser issue by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/8107
* integrate with julia tables by [@aplavin](https://github.com/aplavin) in https://github.com/duckdb/duckdb/pull/7984
* Add JoinReftype to Relational Joins (to add asof, positional, dependent joins) by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7987
* Adjust the logic for adding type dependencies to temp tables by [@jwills](https://github.com/jwills) in https://github.com/duckdb/duckdb/pull/8073
* Add File filters to Logical Get / Physical Table Scan. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7986
* Issue #8119: TO_TIMESTAMP Returns TIMESTAMP  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8127
* [Python] Start of DuckDB Spark API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8083
* Create NamingConvention.md, with [@samansmink](https://github.com/samansmink) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8166
* Casts from and to `BIT` type by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/7941
* [Python] Add `Value` class to explicitly set type of prepared parameter by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8114
* Use many linux image in several places by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8097
* Update tests broken after conflicting PRs by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8168
* Auto-generate FormatSerialize/FormatDeserialize code from JSON that defines the schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8156
* Odbc Lambda Removal by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8167
* fix: support case-insensitive lookup in SHOW TABLES by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/8173
* Bump duckdb-wasm, remove patch, fix NightlyTests.yml triggers by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8176
* [Python] Add extra safeguards around `join` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8170
* Bump ubuntu to 18 for linux extensions build by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8179
* user CMAKE_CURRENT_SOURCE_DIR by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/8183
* Auto-generate type serialization + make enum generation deterministic by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8175
* Fix #7863 - use LoadLibraryW to load extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8186
* [Python UDF] Disallow `create_function` as part of a transaction by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8169
* Arrow C API test - initialize result to nullptr by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8184
* Issue #7969: Prefer Range Join  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8092
* add verbose option to generate_grammar.py by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/8181
* Make the Binder respect the `max_expression_depth` setting by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8188
* build: upload libduckdb_static.a too by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8197
* Pragma platform by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8195
* Issue #7595: AsOf Inequalities   by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8196
* CI Job names to explicit platform they build for by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8202
* ODBC Small Issues fix  #7918 #7890 #7653 by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8205
* Enable vcpkg for extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8210
* Remove unnecessary dbplyr fill method by [@mgirlich](https://github.com/mgirlich) in https://github.com/duckdb/duckdb/pull/8211
* Add union to test_all_types, and arrow and json R/W by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7701
* R: Avoid crash when finalizing by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8207
* Fix #8191 - build duckdb shell error with “DISABLE_UNITY=1” for link … by [@zzachimed](https://github.com/zzachimed) in https://github.com/duckdb/duckdb/pull/8192
* Chore: Bump duckdb-wasm AND move to emscripten latest by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8220
* Issue #7808: Partition Using PartitionedTupleData by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8085
* some extensions (like motherduck) take an interest in SET and PRAGMA by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/8226
* Change join ref type to cross if join type is cross and join ref type is regular by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8227
* Issue #8217: Test Lead/Lag Framing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8233
* ODBC: Reformat Diagnosics Function by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8237
* ODBC: Fix for Issue #8190 by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8223
* fix typos and spelling errors in https://github.com/duckdb/duckdb/pull/8244
* (julia) fix show for query result by [@tbeason](https://github.com/tbeason) in https://github.com/duckdb/duckdb/pull/8256
* CI: Fix typo in LinuxRelease.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8267
* Remove Node 15 from supported versions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8251
* Reduce colreaders by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/8248
* Fix init value type in std::accumulate by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/8275
* Allow parser extensions to use PostgresParser by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/8254
* Implement ROW_GROUP_SIZE_BYTES for Parquet writer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8221
* use cmake_current_source_dir  by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8278
* fix(jdbc): result/prepped stmt metadata by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8280
* ART: inline row IDs into node pointers by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8112
* Skip row group size test on vsize=2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8292
* Update duckdb-wasm in CI & fix order of operations by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8288
* Issue #8086: Parallel Window Refactoring by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8269
* [RLE] Emit constant vectors when possible by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8250
* Update R tests to run test_struct.R not on CRAN by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8297
* Always initialize variables used by ParallelCSVGlobalState::MaxThreads() by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/8295
* [ODBC] Add Row-Wise Fetching and Bool-to-Char Tests by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8306
* Print join_ref_type when explaining joins by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8276
* Fix handling of cross joins by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8274
* Remove dangerous overload of cpp11::warning() by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8272
* add `to_base` function by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8122
* Resolve the conflict between the CTE name and the referring table name. by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/8302
* Compression for the `INT128` type by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/8277
* Fix some function json defs by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8313
* Exposing InterruptState in Sink Combine & Finalize by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8296
* Add iceberg extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8317
* Serialization - Add Format(De)Serialize to almost everything by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8323
* [Python] Add a top-level native python module by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8189
* CI WebAssembly: Avoid eagerly '--recurse-submodules' by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8327
* PR2 for zOS support by [@v1gnesh](https://github.com/v1gnesh) in https://github.com/duckdb/duckdb/pull/7973
* fix(python): restore version field by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8338
* Issue 8315: Window Null Order by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8324
* Swap arguments for atan2 function to atan2(y, x) by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8308
* Add Black Python formatter by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8335
* [ADBC] Add support for ingestion mode by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8349
* feat: python scripts formatting by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8354
* [Python] Correctly handle `pandas` DataFrames when `copy_on_write` is set to True by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8348
* [Arrow Appender] Clean up file/folder structure by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8289
* [CI] Fix test failure introduced by #8348 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8361
* Pipeline scheduling issue by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8356
* Workaround for failing vcpkg openssl install by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8362
* Call pwrite/pread in a loop and reduce disk space usage of window_partition_paging.test_slow by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8369
* Add format serialization for BoundFunction/Aggregate/Window and LogicalGet by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8365
* Throw exception for encrypted Parquet files by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/8368
* Small out-of-tree extension fixes/features by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8375
* Path separator fix windows by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8345
* Compare scalar functions by name/args/return instead of function object target by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8364
* [Python] Add support for +/- infinity `datetime` objects by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8294
* Format serialization - add missing serialization logic for DelimJoin, AsOfJoin, CreateIndex and enums by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8378
* [CI Python] More 'copy_on_write' fixes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8376
* fix end of file handling for gzip files by [@igorcalabria](https://github.com/igorcalabria) in https://github.com/duckdb/duckdb/pull/8386
* Issue CI workflows by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8390
* [CI] Fix nightly tests (sqllogictests, asof join out of disk space) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8385
* use labels field instead of workflow for needs triage by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8400
* [Python] Remove `PyObject *` where possible by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8393
* Fix CMake syntax on non defined variable by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8401
* [RLE] Fix problem created by #8250 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8391
* [Arrow] Fix conversion from arrow -> duckdb for nested structs by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8383
* [ADBC] Python Tests and Fix for Arrow Schema call. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8366
* Use bot token for issue workflows and increase stale issue budget by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8404
* Nitpick: change case of "stale" issue label by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8407
* capi: duckdb_interrupt & duckdb_query_progress by [@Virgiel](https://github.com/Virgiel) in https://github.com/duckdb/duckdb/pull/8064
* Bind the children of a STRUCT alias type. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8389
* [NanODBC] Fix `run_nanodbc_tests.sh` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8388
* ODBC: Add remaining tests by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8382
* fix minor ci failure by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8411
* Update bug_report.yml to ask a better master build question by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8427
* Fix capi streaming test - this is not deterministic if there are background threads by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8429
* bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8394
* read_csv_auto tests: Change 'delimiter' to 'delim' by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8409
* [Arrow] Add ChunkScanState interface to preserve chunk-offset when scanning by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8307
* Qualify macros only when called, and throw error on recursive macros by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8224
* Add instructions for installing black and clang-format by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8373
* Get issue title safely in workflow by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8436
* [ADBC] [Python] Adding extra tests and small fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8431
* Set total_byte_size of Parquet row groups by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8405
* Python TIMESTAMPTZ support by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8089
* Add "require noalternativeverify" to all FTS tests by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8448
* Check for duplicate member tag names in serialization generation by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8449
* Issue #5610: Disallow Chained Frames by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8442
* Issue #8416: Pre-Gregorian Timestamps by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8418
* Issue #8399: ICU Epoch Offset by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8415
* Finish specialization of the LIST aggregate function by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8309
* Add Java format config to clang-format by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8355
* List_slice adjusted NULL handling and added steps feature by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8087
* DuckDB PySpark Types by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8165
* Fix issue 8230 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8450
* Move all extensions to new build, remove legacy ci  by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8465
* [Dev] Update uncovered files by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8476
* [Python Dev] Use `pytest.mark.parametrize` to make test logs easier to read in `test_all_types.py` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8479
* [C-API + CLI] Add support for named parameters in prepared statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7113
* Fix issue 8422: date_part('isodow', timestamptz) to return correct iso day numbers. by [@robert-manchester](https://github.com/robert-manchester) in https://github.com/duckdb/duckdb/pull/8432
* remove static loading extensions for node/python/r dev builds by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8473
* Add geomean macro by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8471
* Bump duckdb-wasm to 9f2f87b by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8470
* CI: Change clang-format version to 11 by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8474
* Add list_reverse function by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8477
* R: dbplyr_fill0() no longer exists by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8480
* General ART improvements and memory pressure reduction by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8437
* [Arrow (Dev)] Refactor arrow scan internals by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8430
* Expose lto and llvm folder compilation flags by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8357
* Documenting R release process by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8081
* Remove assertion on empty linked list by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8502
* Fix total_cardinality is zero will result in undefined-behavior by [@zhouliqi](https://github.com/zhouliqi) in https://github.com/duckdb/duckdb/pull/8506
* Issue #8512: Negative Time Intervals by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8515
* Rework Metadata Storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8513
* Issue #8086: Window Work Stealing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8491
* Add android ifdefs by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8526
* Fuzzer #590: MAKE_TIMESTAMPTZ Extreme Paranoia by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8514
* R: Update duckplyr tests by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8482
* R: Add test for disconnect behavior by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8483
* [ADBC] Addings more tests and small fixes. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8478
* Refactoring the Join Order Optimizer by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8468
* [Dev] Fix CI failure caused by #7113 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8533
* fix query hang in Jetbrains programs (IntelliJ, DataGrip, etc) by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8511
* Add PendingExecutionResult::ALL_TASKS_BLOCKED by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8497
* [R] Fix retention of time component of TIMESTAMPS when converting time zones #8547 by [@ateucher](https://github.com/ateucher) in https://github.com/duckdb/duckdb/pull/8548
* Add "field ID's" to new serialization by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8536
* Fix #3170: Get old value when update on rows with big row_id by [@zippond](https://github.com/zippond) in https://github.com/duckdb/duckdb/pull/8520
* Silence warnings on thread sanitizer for CanHave[No]Null by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8552
* Issue #6027: Explicit ROW_GROUP_SIZE no longer breaks IMPORT/EXPORT round-trip by [@jmeulemans](https://github.com/jmeulemans) in https://github.com/duckdb/duckdb/pull/8559
* fix: remove unused ForwardRef import by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8543
* [Python] Enable use of CUBE / ROLLUP in `groups` parameter of DuckDBPyRelation aggregate methods. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8510
* Adding explicit errors for cascade/set null/set default by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8572
* Throw exception on type error in JsonDeserializer by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8291
* Remove packaging for Python 3.6 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8577
* Fix gcc weird behaviour around template deduction (#8533) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8576
* Fix: Remove undefined behaviour in frame-of-reference bitpacking by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/8569
* Issue #8461: Null Hive Typing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8540
* [Python] Don't clog the `tools/pythonpkg/duckdb` folder on build by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8534
* Add Mold Linker Support for Linux by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/8517
* Fuzzer #572: Lead Lag Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8538
* Fuzzer #668: Window List NULLs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8557
* Update R readme to add instructions on how to load the httpfs extension by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8567
* [ADBC] Finish ADBC spec compliance by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8417
* fix(#8412): forbid topn optimization when there are scalar subquery in limit or offset clause by [@Reminiscent](https://github.com/Reminiscent) in https://github.com/duckdb/duckdb/pull/8519
* R: Update duckplyr tests by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8608
* R: Allow microsecond precision for timestamps by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8597
* R: Fix core dump when failing to evaluate ALTREP query by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8600
* Fuzzer #583: Orders Nary Aggregates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8598
* Add register functions for AggregateFunction used by extensions by [@ttanay](https://github.com/ttanay) in https://github.com/duckdb/duckdb/pull/8607
* R: Full support of lists and structs in R by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8503
* R: Avoid leaking format specifiers in `cpp11::stop()` calls by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8614
* [R] Add ADBC integration with the adbcdrivermanager package by [@paleolimbot](https://github.com/paleolimbot) in https://github.com/duckdb/duckdb/pull/8172
* fix(#8441): some filter expressions can not be pushed down by [@Reminiscent](https://github.com/Reminiscent) in https://github.com/duckdb/duckdb/pull/8532
* format.py: add checks (and suggestion) to install needed tools by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8629
* R: Fix warning on mismatched integer comparison by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8626
* Rename branch from master to main by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8639
* Second round of branch renames by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8643
* Fix: Unimplemented type for TryAddOperator by [@nickgerrets](https://github.com/nickgerrets) in https://github.com/duckdb/duckdb/pull/8566
* typo by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8644
* Wrap ALTREP methods with BEGIN_CPP11 and END_CPP11 by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8647
* Fix test_csv_httpfs.test_slow by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8637
* [Python] Add support for `datetime64` columns with a time-unit that is not `ns` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8620
* PR3 for zOS by [@v1gnesh](https://github.com/v1gnesh) in https://github.com/duckdb/duckdb/pull/8625
* [Dev] Add explicit expected error for `test/sql/storage/multiple_clients_checkpoint_pending_updates.test` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8654
* Extension sha256: Avoid full copies by updating sha context by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8636
* Expose window functions in the Python API by [@jarandaf](https://github.com/jarandaf) in https://github.com/duckdb/duckdb/pull/8568
* Issue #2827: Julian Day Parts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8523
* Issue #8659: Non-Invertible Casts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8661
* Fix CI failure with test/sql/copy/s3/glob_s3_paging.test_slow by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8670
* ADBC: Use new(std::nothrow) + check on null by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8676
* Issue #8674: Interrupt Work Stealing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8679
* Add fix for substrait CI failure by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8545
* fix cpp11 issue in r api by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8664
* [Dev] Fix sporadically failing test `window-rows-overflow.test` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8678
* [Dev] Use our parquet writer in `test_filter_pushdown_2145 ` test instead by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8694
* fix: typo in comment by [@SkyFan2002](https://github.com/SkyFan2002) in https://github.com/duckdb/duckdb/pull/8696
* CI: skip test/fuzzer/sqlsmith/window-rows-overflow.test by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8693
* Makefile extension config by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8692
* Remove deprecated experimental_parallel_csv configuration option by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8669
* [Dev] Fix CI failure related to pandas and timezones by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8665
* Fix for #3789, separate updates into storage backends individually by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8618
* [Internals] Fix key/value name in MAP produced by `map_entries` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8460
* C-API: Fix `duckdb_arrow_scan` API  by [@k-anshul](https://github.com/k-anshul) in https://github.com/duckdb/duckdb/pull/8653
* [PythonDev] Fix failing `test_statement_bind.py` test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8711
* Issue #3409: Time TZ Storage by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8650
* [Parquet] Fall back to VARCHAR for unsupported types in EXPORT DATABASE by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8710
* [Parquet reader] support reading small decimals with DBP encoding by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8715
* When projecting to the R client, use `GetName` instead of `ToString()` by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8717
* Custom indexes: Step 0 by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8367
* Add reusable workflows for out-of-tree extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8714
* feat(jdbc): read struct, map, and unions by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8686
* Slight refactor to silence a gcc13 warning by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8727
* Change parquet_write_memory_limit.test_slow to not preserve order by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8746
* [Python] Pandas 2.1.0 update by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8738
* bump codecov by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8751
* Order Describe table with column id by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8729
* CSV Read: move buffer initialisation to thread local by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8672
* Distinct/order modifier column deduplication by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8748
* Autoloading mechanism for extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/8732
* duckspark, implement createOrReplaceTempView by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8759
* Extension load tests: fix-up b014b6919 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8775
* Apply patches and bump extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8765
* Fuzzer #936: Sort Key Exceptions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8773
* CSV Sniffer - State Machine by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8253
* [Dev] Untangle some really obfuscated code in `ReorderTableEntries` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8707
* Use manylinux_2_24 image for Linux aarch64 Python builds by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8770
* Radix Partitioned Hash Table Rework by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8475
* Issue #7809: Parallel Partition Sorting  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8593
* Add the ability to access file_path in FileOpener by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/8484
* CAPI: Make it possible to create struct types by [@alnkesq](https://github.com/alnkesq) in https://github.com/duckdb/duckdb/pull/8455
* Serialization pt 3: mega follow-up by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8752
* Remove patches and bump dependecies (aws & iceberg) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8777
* [Python] DuckDB -> Pandas | NULL -> `str` becomes None instead of 'NaN' by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8745
* [PythonDev] Add timeout to `test_multithread.py` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8747
* Bump uncovered_files.csv by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8790
* Avoid rounding down buffer block sizes to uint32_t by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8785
* Duckdb wasm loadable fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8766
* [Dev] Handle SKIP_EXTENSIONS as early return in duckdb_extension_load by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8781
* Fix R ci by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8783
* Switching to twine token and remove cleanup job by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8792
* Moving R client out of main source tree by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8793
* Re-add pypi-cleanup script and use pypi-cleanup package for deleting dev packages by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8795
* Fix #8797: Fix off-by-one in varchar -> list conversion code causing out-of-bounds access by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8799
* Add "ends_with" as an alias of "suffix" by [@holdenmatt](https://github.com/holdenmatt) in https://github.com/duckdb/duckdb/pull/8807
* [Dev] Pass explicitly USE_MERGED_VCPKG_MANIFEST by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8806
* #7412 add sha256 scalar function by [@jdnvn](https://github.com/jdnvn) in https://github.com/duckdb/duckdb/pull/8723
* Extension docs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8784
* Fix Python Release Clean-up: need to install requests module by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8811
* Very minor fixes of CI problems by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8809
* Fix "Too many open files" issues by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8812
* Add `list_cosine_similarity`, `list_distance`, `list_inner_product` by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8750
* Towards stable storage of indexes and the ART by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8703
* JSON bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8810
* Issue template: Ask contributors to avoid using screenshots in issue reports by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8829
* [PythonDev] Remove version lock on `adbc_driver_manager` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8725
* Internal #215: Serial Unordered Scans by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8824
* [Generated Column] Return stringified generated expression in `duckdb_columns` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8835
* Extension API: Allow autoloading of extensions dependencies & use it for duckdb_aws by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8839
* Remove references to duckdb_query_graph by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8826
* DuckDB-Wasm fixes related to (auto)loadable extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8827
* Revert "Use manylinux_2_24 image for Linux aarch64 Python builds" by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8849
* fix(nodejs): thread safety between node instances in single process by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8862
* fix: remove TODO's in Node docs by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8861
* Switch over to new Serialization Framework by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8863
* Fixes to error messages: An error occurred ... by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8855
* Attempt at fixing OSX Extensions Release nightly build failures by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8847
* Internal #164: Single Partition Sorting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8791
* [Python] Add `Expression` class by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8469
* Partial Blocks for Index Serialization by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8825
* Update create_package.py for new extension defines by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8870
* Wasm extension signing by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8881
* DuckDB-Wasm workflow: Fix syntax by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8883
* Expose SeekPosition in HTTPFS by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/8876
* DuckDB-Wasm workflow: fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8885
* DuckDB-Wasm workflow: Pass on token and secret by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8886
* Use lock when accessing the http metadata cache by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8882
* DuckDB-Wasm workflow: Uncomment line by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8887
* Rework Storage of Deletions - Allow for lazy loading and incremental re-writing of deletions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8869
* Fix for #8440 by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8879
* Issue #8316: Time Cast Statistics by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8888
* Sqlite commands fixes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8848
* Fuzzer #838: Julian DATE Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8677
* Remove support for NodeJS 10 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8872
* DuckDB-Wasm workflow: Add credentials explicitly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8889
* fix some nodejs tests in some envs by [@jraymakers](https://github.com/jraymakers) in https://github.com/duckdb/duckdb/pull/8774
* Fix link in extension/README.md by [@isaacbrodsky](https://github.com/isaacbrodsky) in https://github.com/duckdb/duckdb/pull/8904
* [Fix] Verification that CSV File exceed line sizes. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8892
* Add R CMD Check workflow back for duckdb src PRs by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8845
* DuckDB-Wasm workflow: moving to official repo by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8918
* Fix #8895: Reading .csv.zst files depends on parquet extension (check… by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8906
* ART fixes - no more empty buffers and correctly serializing parsed expressions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8912
* fix(jdbc): uniform exception handling by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8685
* Wrap failing shell-test so it is not tested on windows.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8923
* Fix R CMD BUILD script.  by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8921
* Point to R package repo for new issues by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/8919
* [Dev] Only emit ConstantVectors when `scan_vector` is invoked by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8916
* [Dev] Fix signing scripts so they can be called from arbitrary locations by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8935
* Detect Header columns with nullpadding by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8915
* [Parquet | ExportDatabase] Deal with unsupported parquet types in EXPORT DATABASE. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8798
* Issue: #8932 Fix description in empty_needle_removal.hpp by [@Light-City](https://github.com/Light-City) in https://github.com/duckdb/duckdb/pull/8933
* Fuzzer fixes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/8920
* Add ordering to to underspecified tests by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8819
* Add rowcount property for Python cursor objects by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/8911
* Various fixes for very large (overflow) strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8943
* [PythonDev] Protect `test_replacement_scan.py` from side effects by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8953
* remove redundant code by [@gitccl](https://github.com/gitccl) in https://github.com/duckdb/duckdb/pull/8946
* fix(nodejs): wait to write all data to disk before calling back by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8843
* [Python Arrow] Fix issue related to TIMESTAMP_TZ and filter pushdown into PyArrow by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8856
* Add `PRAGMA metadata_info` that displays info about the storage of metadata, and correctly write free metadata blocks by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8956
* DuckDB-Wasm: Custom repository to be served over https by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8960
* [PythonDev] Merge `pyduckdb` module into `duckdb` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8959
* [Python] Extend `show` with keyword arguments to set BoxRenderer options by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8954
* Bump aws (removing patches) & spatial to latest commits by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8936
* [Python] Fix issue with `dtype` parameter in the `read_csv` method. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8387
* Update logo by [@szarnyasg](https://github.com/szarnyasg) in https://github.com/duckdb/duckdb/pull/8970
* [Python] Add 'names' option to `read_csv` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8967
* Allow JSON reader to sample across multiple files by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8891
* Fix typos and update variable type info in Contributing.md by [@thfmn](https://github.com/thfmn) in https://github.com/duckdb/duckdb/pull/8975
* Fix outdated C API docs by [@ocadaruma](https://github.com/ocadaruma) in https://github.com/duckdb/duckdb/pull/8973
* CSV Parallel Tests CI by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8910
* Truncate the db file before the WAL for differential storage by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/8980
* Fix #8592: correctly deal with torn writes by ignoring SerializationException during initial read by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/8982
* Fixes for CSV And Aggregate Nightly Build Issues by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/8852
* Internal #317: Fix foreach Label by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8987
* httpfs: Avoid corruptions with servers sending more data than asked for by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8940
* Move arrow, postgres_scanner and sqlite_scanner to be autoloadable by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/8966
* Fix some fuzzer issues by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8871
* ART fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/8995
* [ODBC] Error Management Improvement by [@maiadegraaf](https://github.com/maiadegraaf) in https://github.com/duckdb/duckdb/pull/8939
* fix(nodejs): cpp exception handling by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/8994
* [PythonDev][Docs] Add missing docs for Expression methods. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8991
* [Python][DuckSpark] Add `Column` and a bunch of DataFrame methods by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8990
* [JSON] Support escaping quotes in VARCHAR -> LIST cast by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/8655
* Rework row matching by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/8979
* Issue #7581: Epoch Returns Doubles by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/8963

---

# v0.8.1 - 0.8.1 Bugfix Release <a id="v081"></a>

*Released on 2023-06-13*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.8.1)

This is a bug fix release for various issues discovered after we released 0.8.0. There are no new features, just bug fixes. Database files created by DuckDB v0.8.0 can be read by DuckDB v0.8.1 (i.e. v0.8.1 is backwards compatible with v0.8.0). Note that database files created by v0.8.1 cannot be read by DuckDB v0.8.0 (i.e. v0.8.0 is not forwards compatible with v0.8.1).


## Changes
* [Julia] Update DuckDB_jll to v0.8.0 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7568
* CSV reader - allow parallel option to be set in COPY statement as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7579
* shell: Remove .dbinfo command. by [@omo](https://github.com/omo) in https://github.com/duckdb/duckdb/pull/7569
* Catalog::LookupEntry(): Remove unused code. by [@omo](https://github.com/omo) in https://github.com/duckdb/duckdb/pull/7557
* Add the default scheme to the CREATE TYPE's type search path. by [@omo](https://github.com/omo) in https://github.com/duckdb/duckdb/pull/7555
* Use std::all_of instead of raw loop in Disjoint. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7549
* feat: introduce a common grammar/types file for libpgquery parser and update Python scripts to take source/target directory paths as argument by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7574
* Fix #7582 - correctly set "last_offset" in InitializeScanWithOffset and turn assertion into run-time check by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7586
* Partially fix #7551 - throw internal exception in case of type mismatch in ExpressionExecutor by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7587
* Fix #7602 - allow reserved keywords in named parameters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7604
* Fix #7599 - output a clear error message when a subquery is used in a table function that does not support it by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7603
* Rework Code Coverage CI - Remove CodeCov and instead track uncovered lines explicitly + turn lack of coverage into a CI failure by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7611
* Use unordered_set insert range overload. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7615
* Reserve expression_costs storage. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7608
* [ADBC] Testing Unhappy Paths, Fixing Memory Leaks from Error Setting, Removing Macros by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7589
* Windows - path is only absolute if path starts with a single back-slash by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7623
* Fix #7564 - if the auto-complete extension is not enabled, inline it into the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7621
* Remove 2 extra bytes from magic string pattern. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7626
* Avoid unnecessary table lookup. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7630
* Reserve enough storage for unbound_expressions. by [@ttsugriy](https://github.com/ttsugriy) in https://github.com/duckdb/duckdb/pull/7627
* Increment code coverage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7636
* Remove all C-style casts and add clang-tidy rule to forbid them by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7656
* Fix sql auto complete extension CI issue by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7650
* Add missing entries to ParquetDecodeUtils::BITPACK_MASKS by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7658
* Fix: allow distinct and order by in list aggregates by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7638
* Rework the AggregateExecutor interface to no longer have unnecessary pointers and arrays by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7671
* Fix #7660 - avoid exporting the same catalog multiple times in EXPORT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7676
* Move BindUpdateConstraints into a virtual function that is implemented by the DuckTableEntry by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7679
* Fix #7567 - when setting the schema to a different schema within another catalog, keep the correct catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7678
* Fix exception fmt by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7683
* Fix amalgamation build by avoiding overloading multiplication by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7661
* Fix #7659 - use correct catalog when replaying a CREATE TABLE in the WAL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7675
* Implement #7662 - add the "lock_configuration" setting which allows configurations to be locked down by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7682
* Fix #7663 - add in_search_path function, correctly show temporary views in SHOW TABLES, and show views in SHOW ALL TABLES by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7680
* expose the `StripUnicodeSpaces` parser utility method by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7705
* Add FuzzyDuck fuzzer - and move fuzzer CI to separate repo by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7712
* Add missing std::move for old GCCs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7714
* [Dev] Fix failing assertion in python debug by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7722
* Fix crash in `ArrowTableFunction::GetArrowLogicalType` on Linux by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7718
* Allow core duckdb to handle unrecognized JDBC configuration by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/7713
* [ADBC] Transactions and explicitly not-supporting Partition Reading/Execution by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7639
* Verify that Parallel CSV Reader skips lines mid-threads by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7637
* Fix issue with setup.py builds without dependencies by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7695
* [Python] Fix tests for Pandas 2.0.2 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7726
* Code Coverage CI check - allow one uncovered line by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7724
* Generate `default_types` from json files by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7646
* Fix fuzzer issues found by new fuzzer CI runs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7736
* [Python] Fix conversion of deeply nested dictionaries by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7739
* Fix TupleDataCollection List serialization by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7741
* Fuzzer #156: Copy Before Swizzle by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7747
* Minor fixes to failing CI runs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7768
* Fix more fuzzer issues found by new fuzzer CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7759
* Add option to disable serialization by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7745
* fix(httpfs): correct listobjectv2_url for strict s3/http servers by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7761
* Fuzzer #209: Multiple Scalar Blocks by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7764
* Fuzzer #206: Fix Cast Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7770
* More minor CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7779
* Add Exception on dependency verification for Enum Types and Temp Tables by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7641
* Add fuzz_all_functions fuzzer, and add support for varargs to test_vector_types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7754
* JSON fixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7762
* [Julia] Fix issue related to table function callbacks and IO by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7783
* [Dev] Use `sql` in the `python_regression_test.py`. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7787
* Allow core duckdb to handle unrecognized C API configuration by [@elefeint](https://github.com/elefeint) in https://github.com/duckdb/duckdb/pull/7804
* Fuzzer #214: ROWS BETWEEN Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7767
* Add tests to cover issue 5132 and enable force reload by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7800
* Fuzzer #215: Timestamp Arithmetic Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7769
* Remove grammar support for CREATE/DROP DATABASE by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7806
* Serialize: fix some uncovered cases, part 1 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7810
* CodeCov tweaks by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7815
* fix(jdbc): arrow error handling by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7814
* Fix duck fuzzer #218 and #220 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7818
* Add msan and ubsan to cifuzz (+ fix zstd + msan) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7813
* Art bug fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7801
* Check GlobalSortState for external scan in PhysicalWindow by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7827
* remove un-used PGNodeTag by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7833
* refactor(fsspec): remove seekable flag by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6585
* Unnest_rewriter fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7836
* [Julia] Fix comments on #7783 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7843
* Disable attaching on-disk DuckDB databases if external access is disabled by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7850
* Fix #7711 - disallow detaching the currently USEd database by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7851
* [Python] only execute in `DuckDBPyRelation::Close` if it was never executed before by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7844
* Add rel_from_table_function to R relational API by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7823
* [Python] Fix `__exit__` signature by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7849
* Several minor DuckFuzz/OssFuzz fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7848
* Enhance the generation of random floating point by PCG by [@GHamrouni](https://github.com/GHamrouni) in https://github.com/duckdb/duckdb/pull/7842
* Fix #7795 - provide explicit alias for unnamed subquery as unpivot parameter by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7858
* Grab Mark Join lock when using shared correlated_mark_join_info by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7859
* JSON Contains - correctly handle constant NULL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7861
* Serialize: more fixes, part 2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7830
* Regression.yml to check agaist GITHUB_BASE_REF by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7877
* More UNNEST fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7872
* Bump spatial by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7866
* Rework test_plan_serialization_bwc to do roundtrip by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7862
* Serialize: rework signature, part 3 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7867
* [Python] UDFs now produce the correct result when used together with `range` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7876
* CI: Bump up uncovered_files.csv by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7884
* Build Python wheels for aarch64 using QEMU by [@adavis444](https://github.com/adavis444) in https://github.com/duckdb/duckdb/pull/7864
* Spurious CSV reader CI fix by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7889
* Minor CIFixes: flatten.test, rowsort, ctz UBs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7899
* Upgrade to latest substrait version by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7886
* feat: update parser exception handling for extensions by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7868
* fix(nodejs): http state by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7883
* fix pivotref comments by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/7885
* Arrow buffer Size Option by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7784
* Fix for table in function binding by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7857
* Implement DatabaseManager::SetDefaultDatabase by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/7878
* Fix #7902 - add support for blob to approx count distinct by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7907
* Fix Issue 7278 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7916
* Lift update binding logic from DuckTableEntry to TableCatalogEntry by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/7874

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.8.0...v0.8.1

---

# v0.8.0 - 0.8.0 Preview Release "Fulvigula" <a id="v080"></a>

*Released on 2023-05-17*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.8.0)

This preview release of DuckDB is named "Fulvigula" after the [Mottled duck (Anas fulvigula)](https://en.wikipedia.org/wiki/Mottled_duck) which lives in the Gulf of Mexico, where it is apparently highly prized amongst (heartless) hunters.

There are **two SQL-level breaking changes** in this release:

- https://github.com/duckdb/duckdb/pull/7174 The default sort order switched from `NULLS FIRST` to `NULLS LAST` because this is more intuitive, especially in conjunction with `LIMIT`.
- https://github.com/duckdb/duckdb/pull/7082 The division operator `/` will now always lead to a floating point result even with integer parameters. The new operator `//` retains the old semantics. This change is consistent with Python.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

## What's Changed
* Issue 5984 #4 LogicalColumnIndex out of range Error by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6303
* Implementing Integration with PyTorch by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6295
* Implement #4941: Python client: for streaming fetches construct a streaming result (fetch_one, record_batch_reader, etc) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6346
* Implement sharable Buffer Pool across DatabaseInstances by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/6299
* Add table functions range and generate_series for TIMESTAMPTZ by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6285
* Add Initial DuckDB Swift API by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6351
* Integration with TensorFlow Tensors by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6348
* Windows - remove delayload code and enable statically linking extensions by default by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6399
* Add support for Pivot/Unpivot statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6387
* [C-API] Add support for StreamQueryResult by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6318
* [Swift] add remaining non-composite types by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6422
* [Swift] Add Prepared Statements by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6459
* [Python] Exclude jemalloc files while pip install on Android OS by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6450
* CI: Swap cron for repository_dispatch by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6498
* CI improvements + add version badge to README by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6493
* Storage: store lists as uint64 offsets instead of as list_entry_t by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6499
* two changes facilitating  sending table/column stats over the wire (M… by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/6440
* Rework Value class internals to have a similar structure to LogicalType and others by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6503
* Remove unswizzle flag from SortedData::Unswizzle by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6501
* [Swift] Add Appender by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6482
* JDBC: Remove DuckDBDatabase by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6426
* Add nan and inf arithmetic by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6415
* Update `tools/rpkg` README.md by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6530
* Merge feature into master by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6534
* Restrict threads for reliability. by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6540
* Replace replace with format strings by [@domoritz](https://github.com/domoritz) in https://github.com/duckdb/duckdb/pull/6542
* Add missing escape for " by [@domoritz](https://github.com/domoritz) in https://github.com/duckdb/duckdb/pull/6543
* Blob <-> Bitstring casting  by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6488
* Mapfunctions:  map_entries, map_values, map_keys by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6522
* Issue #5920: Ordered Aggregate Buffering by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6539
* Handle SQL-tagged strings correctly with dplyr::tbl, fixes #6506 by [@rsund](https://github.com/rsund) in https://github.com/duckdb/duckdb/pull/6536
* CI: Update Swift.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6553
* Update SwiftRelease.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6554
* Java: Implement JDBC 4.1 by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6376
* Bitstring aggregations by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6417
* Make our default `threads` setting Cgroup-aware on Linux by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6550
* [Swift] Add composite type support by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6557
* Statistics Rework: Switch to single BaseStatistics class, use separate static classes for methods on the stats instead by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6560
* Introduce Syntax for SEMI and ANTI joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6480
* Update storage_info with version 0.7.1 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6572
* [Python] Add the ability to supply a DuckDBPyRelation instance to `register` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6483
* [Python] `map` now defaults to original type when analyzed type at bind is NULL by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6571
* [Dev] Fix broken `test_filesystem.py` test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6582
* CI: Node.js, add common NPM-setup step by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6590
* build: add builds for nodejs linux arm64 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6586
* CI: move to setup-node[@v3](https://github.com/v3) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6596
* Issue #6604: TIMESTAMP <=> TIMESTAMPTZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6605
* [Python] Add support for EXPLAIN ANALYZE to `explain` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6561
* Add ICU list functions generate_series and range by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6445
* feat(nodejs): add errorType attribute to DuckDbError by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6434
* Fix TPC-DS date insertion by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/6591
* Fix #4016: Test amalgamation with --split param by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6587
* feat(python): throw HTTPExceptions instead of IOException for http errors by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6533
* Add httpfs config to support packaging it as an extension by [@ankrgyl](https://github.com/ankrgyl) in https://github.com/duckdb/duckdb/pull/6608
* Issue #6595: N-Ary Positional Joins by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6598
* [Swift] inline documentation plus API tweaks by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6614
* Fix #6602: add inet extension to build/distribute script by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6610
* CI remove amalgama x8 + swift release by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6615
* Fix too many open file handles during JSON schema detection by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6613
* Issue #6580: Parquet Int96 Timestamps by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6601
* Exception_static_build defalt: Partial revert of dabbeada3a by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6620
* Make DISTINCT ON respect the ORDER BY clause similar to Postgres + several ordered aggregate improvements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6616
* fix url encode issue for R2 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6609
* [Swift] Database.Configuration type + documentation enhancements by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6617
* R: Avoid passing SEXP by reference by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6475
* Test and fix preservation of class attribute in external pointers by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6526
* Add support for lambda functions to `COLUMNS`,  and allow COLUMNS to be used in the ORDER BY/WHERE clauses by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6621
* [R] Remove duplicate occurrence of dependency by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6625
* Automatically Fully Download Files through HTTPFS if no length header is provided by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6448
* Remove some function calls that can throw potential false positives in CI by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6623
* [Python] Add `__getattr__` and `__getitem__` implementations for DuckDBPyRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6624
* [Optimizer] Regex Optimization Rule fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6634
* [Bug Fix] Enum Serialization by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6040
* Update interval for arrow by [@handstuyennn](https://github.com/handstuyennn) in https://github.com/duckdb/duckdb/pull/6515
* SQLLogicTest - instead of moving prepared statements over avoid restarting database when there are prepared statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6638
* Bind replace table function by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6639
* Fix #6630: correctly set bind_data->types in the Parquet scan when using union_by_name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6642
* [Python] `read_csv` can now read from a file-like object. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6568
* Fix #6640: correctly throw an error on altering schemas by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6643
* Support multiple aggregates in top-level pivot by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6644
* [DEV]: Fix clangd errors by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6650
* Issue #6635: FIRST LAST NULLS by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6648
* [DEV]: Unreachable window alias by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6649
* Fix IsRegularCharacter() by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/6654
* [Swift] add Xcode playground Example by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6629
* Fix #6651: correctly update UpdateSegment references after transferring from transaction-local to committed data by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6657
* Fix #6656: correctly add casts to NULL values in list_concat, and add more safety around stats mismatches by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6658
* Fixing some tidy warnings by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6661
* Fix c053bc813a75b, unguarded std::thread by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6663
* Fix class name in error message by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6679
* Fix many fuzzer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6681
* Fix #6676 and #6677: correctly instantiate local states for nested casts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6688
* WebAssembly testing against duckdb-wasm latest stable version by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6665
* Support reading from presigned url by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/6467
* Fix #6668: correctly report errors that occur during index appends by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6693
* R: Remove RProtector class by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6637
* Fix #6684: in the aggregate hash table, when we have very wide rows, default to HtEntryType::HT_WIDTH_64 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6689
* ColumnDataCollection -  copy strings if DISALLOW_ZERO_COPY is enabled by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6700
* Fix ossfuzz assertion triggers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6699
* Fix #6690: correctly handle NULL values in CSV auto-detection when decimal separator option is specified by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6701
* Don't try to process validity mask for arrow null type columns by [@cpcloud](https://github.com/cpcloud) in https://github.com/duckdb/duckdb/pull/6702
* Adding Children and Step Options to TPC-H generator for BIG DATA by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6535
* Add `json_serialize_sql` and first step of new Format(De)Serialization infrastructure. by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/6647
* feat(nodejs): Expose HTTPException as HTTPError by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6655
* Add `regexp_extract_all` scalar function by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6685
* Storage: Lazily Load Row Groups from Tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6715
* Add support for function chaining and the dot syntax for function calls by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6725
* Implement JDBC unwrap methods by [@tom-s-powell](https://github.com/tom-s-powell) in https://github.com/duckdb/duckdb/pull/6718
* [Swift] Add sub-repo README.md by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6734
* Fix #6433 - avoid double recursion in pushdown of single/mark join by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6740
* Make more pieces of pivot clause optional, and fix pivot alias issue by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6731
* Add date_add alias to interval arithmetic by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6726
* Add --root-dir option to benchmark runner by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/6739
* Add .col option to duckbox rendering in the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6748
* Add support for CREATE OR REPLACE SEQUENCE and CREATE OR REPLACE SCHEMA by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6730
* Support recursive unnesting and unnesting of structs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6755
* Add support for pivoting on expressions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6758
* arrowIPCStream should return a promise by [@domoritz](https://github.com/domoritz) in https://github.com/duckdb/duckdb/pull/6744
* Bug report: Add duckdb-wasm as potential alternative by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6794
* Anti/Semi Join fixes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6790
* Julia - Add support for streaming query results by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6770
* Adding the option for the user to specify the column types searched in the CSV Auto Detect by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6756
* Add GCD and LCM numeric functions by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/6766
* Release the GIL when getting chunks for arrow results by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6810
* Add to_hex/from_hex functions by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/6579
* Fix duckdb_result_chunk_count return description. by [@Giorgi](https://github.com/Giorgi) in https://github.com/duckdb/duckdb/pull/6813
* Issue #3207: ASOF JOIN Compilation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6719
* Fix #6603/#6799 - Index join fixes + fix verification check by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6807
* Fix #2743 by removing NotImplementedException in CreateUnionPipeline by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/6789
* [Swift] SwiftUI example project and type conversion utils by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/6795
* Fix issue #6822 by instantiating TryMultiplyOperator for hugeint_t by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/6824
* Moving HTTPState initializer to CleanupInternal by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6819
* Map extract now allows composite (nested) types as `key` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6552
* Issue #6728: Constant Windowed Aggregation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6772
* Parquet reader - fixes for reading non-microsecond TIME columns and delta_binary_packed encoded times/timestamps by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6836
* Register function for Polars DFs by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6825
* Storage: Add lazy column meta data loading, and fix issue where RowGroup::InitializeScan was called many times unnecessarily by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6841
* Add support for named parameters in the API by [@dacort](https://github.com/dacort) in https://github.com/duckdb/duckdb/pull/6575
* Issue #5290: Rewrite ordered LIST by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6741
* [Python] Fix crash in Jupyter environment related to progress bars by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6831
* Issue #6764: add "null_padding" option to pad rows in a CSV file with missing columns with NULL values by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6765
* Enable BuildPipelines for nested recursive CTEs by [@kryonix](https://github.com/kryonix) in https://github.com/duckdb/duckdb/pull/6838
* 2023a Time Zones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6844
* Normalize comparisons and improve string_t operations by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6381
* Fix #6856: correctly check cast cost of child element of list during function binding by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6857
* Hash aggregate - switch partitioning threshold to MAX(total_groups) instead of SUM(total_groups), and limit number of partitions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6851
* Fix Parquet writer regression + add Parquet writing to regression test suite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6852
* [Python] `tuple` now gets properly converted to LIST, instead of a VARCHAR by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6868
* Implement predicates in JDBC DB-Meta class by [@pjarra](https://github.com/pjarra) in https://github.com/duckdb/duckdb/pull/6866
* [Dev]: ICU 2023b TimeZones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6855
* [Python/Dev] Add implicit conversion from None -> duckdb.default_connection by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6839
* Add specific version of `clang-format` to the contributing guidelines by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6849
* ** search (crawl) for files in subdirectories by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/6627
* Modify show tables pragma query to respect current catalog scope by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/6816
* Issue #5920: Ordered Aggregate Performance by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6867
* Do not enable jemalloc unconditionally by [@jeroen](https://github.com/jeroen) in https://github.com/duckdb/duckdb/pull/6864
* Parquet reader - millisecond times are stored as int32 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6879
* Aggregate HT: Move intermediate structures to a separate AggregateHTAppendState, and avoid unnecessary resizing when many hash tables are created by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6877
* [Python] Respect strides in 'object' column (string) to DuckDB conversion by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6878
* [Python] Add implicit conversion from `pathlib.Path` to string by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6835
* Ci wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6886
* Include necessary C++ header by [@david-cortes](https://github.com/david-cortes) in https://github.com/duckdb/duckdb/pull/6900
* Wasm loadable extensions wip by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6889
* [Dev]: 2023c TimeZone Data by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6905
* Adding definition for missing extension exception by [@Dtenwolde](https://github.com/Dtenwolde) in https://github.com/duckdb/duckdb/pull/6903
* Export window function as expression in relational api by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6757
* [Catalog] Improve error message on catalog-qualified catalog-entry lookup by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6911
* fix for ODBC driver issues #4887 and #3801  by [@bucweat](https://github.com/bucweat) in https://github.com/duckdb/duckdb/pull/6875
* Add support for transforming boolean tests by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6928
* Support for missing GZIP features (extra field in header and concatenated files) used in BGZF by [@rsund](https://github.com/rsund) in https://github.com/duckdb/duckdb/pull/6817
* MultiFileReader - Provide unified methods for multi-file reader functions (Parquet, CSV, JSON) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6912
* Fixes an issue where CDPATH causes make to fail. by [@marhar](https://github.com/marhar) in https://github.com/duckdb/duckdb/pull/6940
* Add duckdb::make_uniq by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6950
* [Dev] Lock Pandas version in CI by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6958
* Bump duckdb-wasm to support duckdb::make_uniq by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6957
* Support for the ** operator in s3 by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/6930
* Add rel_to_sql method to convert relations to SQL again by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6952
* [Safety] Add safety checks to `unique_ptr` access to guard access by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6891
* [Dev] Add missing header guard for `concurrentqueue.hpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6915
* [Python - Chore] Update name of pybind11 type caster for doc gen by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6963
* Remove unnecessary code from the Python client by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6972
* Faster PIVOT statement by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6961
* CREATE TYPE creates an alias to a type - not an actual new type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6969
* [Safety] Remove C Style Casts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6967
* [Python] Fix issue related to objects that derive from `builtin.str` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6978
* [Dev] Make `copy/csv/test_union_by_name.test` result deterministic by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6987
* Fix #6232 - for SQL value functions, only convert them into functions if there is no column with the same name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6982
* Fix #6990: When type has both num_children and type set, prefer the num_children - plus more defensive code in Parquet reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6992
* Issue #6881: Window Memory Segfault by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6984
* Issue #3207: LogicalAsOfJoin Deserialize by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6983
* Issue #6959: TRY_STRPTIME Implementation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6960
* [Safety] Add safety checks to `vector` indexing by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6927
* Add json->sql deserialisation and execution. by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/6919
* [Python] Enable `rel[name]` and `rel.name` syntax for struct fields by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6988
* LIST aggregate performance improvements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6995
* Treat MinGW as a different platform for extension loading purposes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7007
* Fixes #6775 Error scalar function by [@ozdemircs](https://github.com/ozdemircs) in https://github.com/duckdb/duckdb/pull/6996
* feat(jdbc): stringify nested types by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7000
* feat: standalone autocomplete extension by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7010
* add support for scaning over numpy arrays by [@vlowingkloude](https://github.com/vlowingkloude) in https://github.com/duckdb/duckdb/pull/6523
* Rework Order Dependence Tracking in Pipelines by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7006
* [Python] Fix crash related to file-like objects and `fsspec` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7012
* Partially fixes #6936 - Avoid unnecessarily calling ToString in expression executor state by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7018
* [Python] Fix datetime with tzinfo converting to naive TIMESTAMP by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7024
* Fix crash/error caused by importing an empty database. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7025
* postgres_parser: use std::forward by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7038
* fixed an issue with ** operator by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7040
* CI - Allow codecov uploads to fail by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7043
* [DEV]: test_map_subscript reliability by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7041
* Wasm loadable extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7032
* WebAssembly.yml by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7030
* Issue #6959: ICU TRY_STRPTIME Lists by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7031
* [External Buffer Manager] Step1: Split components from `buffer_manager.cpp` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7028
* Issue #3207: ASOF Join Refactoring by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7001
* [External Buffer Manager] Step2: Abstracting away the `atomic<idx_t>` counter by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7053
* Fix Julia BoundsError with arrays > 2048 by [@frankier](https://github.com/frankier) in https://github.com/duckdb/duckdb/pull/7055
* Issue #7013: Implement TRUNC by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7036
* Add to_binary/from_binary functions by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/6848
* [Python] Extend `project` to accept a list of types + add DuckDBPyType class by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6777
* Ci wasm by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7072
* [Optimizer] Fix `regexp_matches` (again) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7075
* [Safety] Remove many C-style pointers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7080
* [External Buffer Manager] Step3: `BufferManager` interface,`StandardBufferManager` implementation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7078
* Issue #6882: REGEXP_EXTRACT Capture Groups by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6918
* [feature] Add Damerau-Levenshtein string comparison function by [@ADBond](https://github.com/ADBond) in https://github.com/duckdb/duckdb/pull/7035
* Logical Get children should be optimized as well by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7046
* [BREAKING] Use Python-style division operator (/ is always floating point division, // is integer division) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7082
* Issue #6861: Index out of bound for all-NULL case. by [@xuke-hat](https://github.com/xuke-hat) in https://github.com/duckdb/duckdb/pull/7070
* Issue #5920: Ordered Aggregate Sorting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6986
* Decode DuckDB blobs as buffers in Node UDF args by [@matt-allan](https://github.com/matt-allan) in https://github.com/duckdb/duckdb/pull/7059
* Partitioned file naming by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/6791
* fix: accept either AWS_REGION or AWS_DEFAULT_REGION by [@OhmniD](https://github.com/OhmniD) in https://github.com/duckdb/duckdb/pull/7090
* Kitchen sink related to duckdb-wasm WIP by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7074
* Pb/catch stacktrace by [@peterboncz](https://github.com/peterboncz) in https://github.com/duckdb/duckdb/pull/6991
* [Python] Fix nightly build failure by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7104
* Possibly fixing R strict barrier issue by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6974
* Change chunk_size parameter to approx_rows_per_batch by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6840
* Add interrupt() to jdbc by [@zhangyt26](https://github.com/zhangyt26) in https://github.com/duckdb/duckdb/pull/7058
* Bump Julia package to v0.7.1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7109
* R: Add duckplyr tests by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/7097
* [Safety] More C-style pointer removal by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7108
* Disable format_uuid for vsize=2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7115
* Fix #7096 - allow specifying a column list for VACUUM without ANALYZE by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7110
* Fix #7093 - correctly extract table names even when tables are present in the catalog by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7111
* Tuple Data Collection by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6998
* Fix #7083 - correctly reset delta offset when reading a new delta byte array page by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7112
* Bump wasm version by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7121
* Using Parallel CSV Reader as a Default Option by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6977
* Upcast Enum to String in Coalesce Function by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7114
* ADBC - Arrow Database Connectivity - Integration by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7086
* Timestampformat also for timestamps with timezones by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7130
* Remove dependency of arrow import with dataset module by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6809
* [Safety] Even more C-style pointer removal  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7131
* Accidentally pushed timestamp date with current_date instead of fixed… by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7148
* string_t - rename GetDataUnsafe to GetData by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7151
* Coalesce expression operator should propagate null by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/7140
* Issue #7128: Fuzzer DATE_DIFF Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7137
* Issue #7147: TIMESTAMPTZ to DATE by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7150
* Fix floating point error in SKEW by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7146
* feat(jdbc): set{Schema,Catalog} by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7158
* Split ** tests up into two files by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7159
* Arrow Blob Filter Pushdown by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7164
* Fix #7124 - correctly transform order by/limit in pivot/unpivot statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7163
* [Safety] Replacing pointers with references/optional_ptr in the Binder by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7136
* Fix kurtosis on macOS by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7165
* Correctly zero-initialize all unused memory in storage blocks, plus add CI run to ensure all memory is correctly initialized by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7175
* Fix rel to sql by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7172
* Update swift CI run to always push & publish a tag by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7179
* [BREAKING] Switch to NULLS LAST as default null sorting order, instead of NULLS FIRST by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7174
* Issue #3207: ASOF Physical Joins by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7153
* Run ADBC tests on windows by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7185
* feat(jdbc): support TIME_TZ  by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7193
* Fix ASOF join test null ordering by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7195
* [Python] Add support for Pandas 2.0.0 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7005
* [Safety] Remove C-style pointers in Catalog, use references whenever possible by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7203
* Default allow caps to false by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7201
* Fix the `lineitem` table schema definition error of TPC-H by [@r4ntix](https://github.com/r4ntix) in https://github.com/duckdb/duckdb/pull/7099
* Fix #7219 - we cannot use the ungrouped aggregate if there are multiple grouping sets (even if they are all empty) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7234
* Move several tests to slow tests by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7249
* [TPC-DS] Fix issues in data generator (#7222, #7223, #7225) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7247
* Issue #7230: Named Window Overrides by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7243
* Correct license code in nodejs project by [@whscullin](https://github.com/whscullin) in https://github.com/duckdb/duckdb/pull/7241
* Issue #7220 - add support for DEFAULT VALUES clause in INSERT INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7240
* Fix #7235 - correctly detect invalid statistics for decimal type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7238
* Fix #7119/#7120 - correctly do a case insensitive comparison in foreign key REFERENCES by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7236
* [C-API] Add `duckdb_string_t` for use with the data chunk API by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7180
* [CSV Reader] Allow quoted nulls by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7210
* Towards buffer managing the ART - no more tiny allocations by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6951
* Implements #7118 - support REFERENCES syntax for single column references by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7237
* Fix spurious CI failure by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7257
* In the parallel CSV reader, prevent buffering of data unnecessarily when reading from compressed files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7253
* fix(JDBC): push down update count calculation into execute() method by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7242
* Issue #7013: Implement getTimestamp Calendar by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7276
* fix(jdbc): return valid class names from getColumnClassName by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7262
* fix(adbc): crash when setting database option due to malloc by [@zeroshade](https://github.com/zeroshade) in https://github.com/duckdb/duckdb/pull/7268
* build: Node 20 builds  by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7286
* [Dev] Rename `ClientProperties` property `timezone` -> `time_zone` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7258
* Add ExtraTests CI run that can be manually triggered to run *all* benchmarks and compare to last release by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7287
* Reset parsed_chunk when figuring out new line in Parallel CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7284
* fix: add catalog information to the serialization of a few logical operators  by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7270
* [Python] Fix #7269 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7301
* [Python] Add `by_name` option to `connection.append` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7300
* Fix affected row count returned from `INSERT .. ON CONFLICT (..)` statement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7259
* Parquet metadata functions - correctly check for isset on various properties by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7289
* Account for presence of varargs when casting table function arguments by [@MarkRoddy](https://github.com/MarkRoddy) in https://github.com/duckdb/duckdb/pull/7245
* [Python] Add optional `schema` option to `relation.map` method. by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7197
* Force parallelism in R dataframe scans. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7181
* [Python] Add `:default:` option to get the default connection through `duckdb.connect()` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7144
* Rework function registration, and move most scalar/aggregate functions to "core_functions" directory by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7310
* Add ExtensionUtil class and move function registration to ExtensionUtil by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7312
* [swift] Change Int to Int32 in DatabaseType array documentation by [@indragiek](https://github.com/indragiek) in https://github.com/duckdb/duckdb/pull/7318
* [swift] Make LogicalType public by [@indragiek](https://github.com/indragiek) in https://github.com/duckdb/duckdb/pull/7319
* Segmented signing checks on extensions by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7311
* chore: add newer extensions to default extensions array by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7322
* Extend `format` and `printf` to support printing thousand separators similar to SQLite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7323
* Issue #7315: LocalFileSystem Glob FileExists by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7316
* add `dayname`/`monthname` functions for `timestamptz` type by [@dylanscott](https://github.com/dylanscott) in https://github.com/duckdb/duckdb/pull/7332
* [PythonDev] Fix Python regression test CI by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7338
* Simplifying initialization logic by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/7282
* More clear error message on mismatching files by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7205
* Pivot - add support for custom subqueries in the IN clause of pivot entries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7333
* Improve error message when using pivot statement in views or macros by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7328
* [swift] Make ResultSet.rowCount a public member by [@indragiek](https://github.com/indragiek) in https://github.com/duckdb/duckdb/pull/7334
* [swift] Make Foundation extensions public by [@indragiek](https://github.com/indragiek) in https://github.com/duckdb/duckdb/pull/7335
* Blocking Sink/Source operators by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7331
* Restore serialization of BaseStatistics distinct count by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/7329
* Improve error message for unexpected constraint violations by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7343
* Issue #3545: Fix Adar2 Crash by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7346
* Extension signing: Fix #7311 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7347
* TableCatalogEntry should allow customizing serialization but still be opinionated by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/7350
* Add format_bytes function that formats bytes to a human readable size by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7342
* Make `SQLLogicTestRunner::LoadDatabase` virtual by [@Flogex](https://github.com/Flogex) in https://github.com/duckdb/duckdb/pull/7340
* [DEBUG] Add "debug_print_bindings" option to DBConfigOptions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7288
* [Arrow] We always output the large buffers, for blobs, bytes, uuids and strings by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7345
* Julia - Make method `destroy_data_chunk` public - streamed query results must be destroyed before the connection is destroyed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7361
* [Swift] add Int/UInt decoding to VectorElementDecoder by [@tcldr](https://github.com/tcldr) in https://github.com/duckdb/duckdb/pull/7362
* Add Minimum Batch Index + Order Preserving Insertion Rework by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7352
* Initialize HTTPFS state when extracting plans by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7365
* Add support for parallel order-preserving CSV write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7368
* [Safety] Perform `vector` bounds checking on release builds by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7325
* [Dev] Fix some Minio boot problems + extend Makefile for use with extensions by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7363
* Add `BinarySerializer`, `EnumUtil::` and generator script by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7351
* Capture database type in config by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/7359
* Change file exist check to is_pipe and do it in the bind by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7354
* Column function chaining alias by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/7313
* Relational set operations coerce to richer type by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7256
* Autodetect hive_partitioning by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7344
* Add missing rowsort to test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7370
* Fold some DistinctFrom + add bloaty (?) by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7374
* [Python] Add null_padding option to read_csv by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7364
* Add support for parallel order-preserving Parquet write by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7375
* fix: update serialization for logical_delete and logical_update by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/7382
* Issue #7353: Filtered Constant Aggregates by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7381
* Add `map_concat` function by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7360
* Add catalog parameter to dbgen / dsdgen by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/7378
* Fix Ubuntu 16 action: first compile OpenSSL, then Python by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7397
* [Python] Add scalar UDF, using `pyarrow` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7171
* Add github actions to contributing.md by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/7404
* Avoid double rollback caused by a constraint violation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7380
* Addings Tests and Fixes for Multiple CSV Issues by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7379
* feat(jdbc): native array reading support by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7369
* Print Error Lines in the Parallel CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7184
* SQLite - Fix SQLiteScanner#45 by applying correct extension alias and upgrade SQLite extension by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7405
* Correctly concatenate ART prefixes during deletions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7410
* Add support in the parser for `PREPARE COPY ...` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7409
* Fix elusive unrecognized ART node type bug by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7372
* Change exception type for invalid parquet by [@ccfelius](https://github.com/ccfelius) in https://github.com/duckdb/duckdb/pull/7402
* [Optimizer] Fix issue with COMPARE NOT EQUAL and cast overflow by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7413
* CI NodeJS: build and publish nightly for M1 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7429
* Issue #7426: DuckDBVector getTimestamp by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/7428
* [Julia] Fix #7420 - Don't use `unsafe_string` in `appender.jl` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7427
* Correctly reset the ART keys during index joins by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7425
* Remove FileOpener almost everywhere - instead wrap FileSystem in the ClientContext with an "OpenerFileSystem" by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7423
* Make CSV error line numbers 1-indexed by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7422
* Parquet: Check for valid UTF8 also in statistics by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7421
* Fix #7023 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7419
* Fix #7263 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7414
* [swift] Add a CodingUserInfoKey for accessing the LogicalType by [@indragiek](https://github.com/indragiek) in https://github.com/duckdb/duckdb/pull/7371
* Implement JSON <-> Nested types casting by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7366
* CI - comment out failing CSV tests for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7435
* Fix #7274 - correctly do a case insensitive comparison in UndoBuffer::Undo by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7445
* Fix #7348 - In RowGroupCollection::RemoveFromIndexes - correctly account for the case where the row identifiers might not all be present in the same row group by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7442
* Fix #6611 - List lambdas didn't support different vector types by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7424
* Swap Children of Logical ANY joins (or block nl joins) when possible by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7437
* Add initialization of HTTPState to `TryBindRelation` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7443
* Initialize the first two smallest plans when creating a cross product by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7438
* Fix another index join bug and move to generated data by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7441
* 7415 cross-product joins on parquet files by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/7455
* Support binding of ON CONFLICT clauses for extension tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7447
* Add MAP {} syntax for easier map construction by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7459
* Add support for `INTERVAL` type in `BETWEEN` expression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7461
* Lipo macos extensions to reduce their size by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7469
* Fix fuzzer issue 132 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7456
* Fix unnest rewriter bug by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7467
* [Safety] Enable `unique_ptr` safety checks on release builds by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7449
* Add support for array_to_string as an alias to list_aggr with 'string_agg' by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7476
* Fix #7377 - correctly account for memory allocated in reset buffer of CSVFileHandle, and remove unnecessary caching for gzip files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7466
* Fixes 7439 and 7433 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7454
* Signing binaries and extensions for OSX by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7484
* Add support for INSERT INTO tbl BY NAME by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7475
* link Out-of-tree extensions in node/R/python build + fix arrow extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7458
* Fix (de)serialization + enable serialization verification for more operators by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7468
* disable assertions in release node binaries by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/7487
* feat(jdbc): Statement#cancel() by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7489
* Fix #6234 - throw invalid input exception when attempting to create non-temp entry in temp database, and disallow SET SCHEMA to temp/system schemas by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7483
* Simplify COLUMNS with lambda -> operate only on column names, instead of qualified names by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7499
* Fix #6666 - when reading an index in the CheckpointReader directly use the table entry by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7481
* Expand SHOW ALL to include schema/database name, and add SHOW ALL TABLES alias by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7500
* Fix #5777 - always read free-list of database, also in read-only mode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7501
* Run old CSV reader when reading many files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7490
* Build extensions for R on Windows using MinGW by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7440
* JSON reader improvements/fixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/7478
* Windows File System Unicode Fixes and correctly expand home directory in ATTACH/DBInstanceCache by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7503
* JSON: Fix missing std::move by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7507
* [Dev] Add SQLString and SQLIndentifier helpers for `ExceptionFormatValue` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7486
* Unsupported .help options removal by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/7488
* Remove even more unsupported options from the shell's .help by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7511
* Increment julia version to v0.8.0 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7517
* Fixes #7504 and other minor spurious CI issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7509
* Fix amalgamation builds avoiding linking utf8proc by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7512
* Change HTTPState to a shared_ptr so it doesn't get invalidated in prepared statements by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7523
* [Dev] `unique_ptr` helper renames by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7516
* un-exporting sql() in R by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7525
* Alias replacement scans to table name if no explicit alias is provided by the replacement scan by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/7526
* [Python] `read_json` API changes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7505
* Fix minor benchmark errors by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7510
* Fix spurious CI /2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/7515
* [UPSERT] Check for conflict constraint errors within a transaction by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7407
* Fix #7356 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7417
* [Python] Fix GIL issue in `sql` with multiple statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/7534
* Changing platform define for mingw by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/7533
* set the min os x to 11.0 for universal by [@aprock](https://github.com/aprock) in https://github.com/duckdb/duckdb/pull/7497
* Correctly shift row IDs during ART deletions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/7538
* Add internal option to export small buffers to arrow strings by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/7540
* fix: correct format specifier by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/7544
* Add spatial extension to CI by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/7545

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.7.1...v0.8.0

---

# v0.7.1 - 0.7.1 Bugfix Release <a id="v071"></a>

*Released on 2023-02-27*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.7.1)

This is a bug fix release for various issues discovered after we released 0.7.0. There are no new features, just bug fixes. Notably, there is no incompatibility with database files created with v0.7.0

## Changes
* When building extensions we need to add _storage_init to the whitelist on MacOS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6243
* Some more read_json_auto bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6244
* Fix for Thrift.h: std::iterator is deprecated by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6250
* Add missing shell mode descriptions by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6256
* Fix #6255: Shell should be installed in INSTALL_BIN_DIR by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6266
* Bump Julia to v0.7.0 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6280
* Skip headers in read_csv functions as well by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6267
* Correctly compute Windows terminal width, and add a `.maxwidth` option to the shell for duckbox mode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6274
* Fix lateral join bug by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6268
* fix: add storage_version_info entry for v0.7.0 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6279
* Fix to #5461 by [@annnei](https://github.com/annnei) in https://github.com/duckdb/duckdb/pull/6265
* CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6289
* [Fuzzer] Fixes fuzzer issue 11 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6191
* Partially Fix #6253: Improve handling of timezones in the regular VARCHAR -> TIMESTAMP cast by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6283
* Error message on no content-length header by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6293
* fixes #6238 by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6239
* fixes #6236 by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6252
* Missing extension exceptions by [@lverdoes](https://github.com/lverdoes) in https://github.com/duckdb/duckdb/pull/6294
* feat: allow extensions to implement CREATE/DROP DATABASE by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/6115
* fix(python): python object types in stubs by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5732
* Fix UPSERT binding issue related to the source table_index by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6275
* fix: DESCRIBE does not show primary key by [@gkaretka](https://github.com/gkaretka) in https://github.com/duckdb/duckdb/pull/6068
* Fix #6276: avoid transforming the root arg of a case expression multiple times by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6300
* More read_json(_auto) bugfixes by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6281
* JDBC: Expand Blob, add UUID support by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6302
* CMake: Move from GREATER_EQUAL to GREATER, fixing #5528 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6310
* Implement #6003 - add names option to CSV reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6308
* CI: Test for cron based workflows by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6311
* CI Fix + match tests on less specific error messages by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6320
* Fix #6314: select correct block index in IEJoin - and fix issues with left/right IE join resuming in case of multiple matches by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6323
* CI: all workflows moved to nightly by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6334
* Fixes #6315: keep names/types around so description can be used after result is closed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6326
* Fix #5800: add missing Copy() calls, and add ALTERNATE_VERIFY method to verify Copy of INSERT/UPDATE/DELETE/COPY statements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6327
* Apply lower casing to extension aliases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6331
* Fix #6304: correctly handle NULL partitions and constant vectors, plus handle default parameters in COPY by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6336
* [Python] DuckDBPyRelation: Change `explain` method and add `sql` method  by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6287
* Fix Polars CI and properly implement check_ methods in the dataframes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6347
* Fixing a clang16 problem that slipped through by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6345
* Fix #6341: LEFT/RIGHT/OUTER join on condition that is always true is only equal to a cross product if the other side is not empty by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6342
* CI: Skip any CI on branches named 'feature' or 'master' by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6350
* Add correct bail-out to CSV auto-detection on oddly/inconsistently formatted CSV files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6330
* CI: Invert path-ignore for tools folders by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6353
* NULLs sort last in relational by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/5994
* Properly deal with Star (*) expressions in `COPY ... (FORMAT JSON)` by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6319
* fixes #6227 by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6230
* fix typos in dictionary_store_worst_case.benchmark by [@hnjylwb](https://github.com/hnjylwb) in https://github.com/duckdb/duckdb/pull/6371
* Julia: Support change timezone config by [@xcaptain](https://github.com/xcaptain) in https://github.com/duckdb/duckdb/pull/6358
* Paths-ignore on push by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6363
* JDBC - Add separate treatment for timestamptz values by [@Jens-H](https://github.com/Jens-H) in https://github.com/duckdb/duckdb/pull/6364
* bugfix: switch to fsspec's strip protocol impl by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6361
* Disable tidy on ODBC for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6379
* Implements function "sqlite3_column_table_name" for the sqlite3 wrapper by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/6385
* [Python] No jemalloc for successful build on android by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6383
* throw BinderException on empty list in percentile by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6378
* Add optimizer flag to R and Python Substrait api by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6097
* fixes #6269 by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6291
* Java: Use automatic resource management for AutoCloseable types by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6377
* Fix progress bar in (parallel) CSV reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6397
* Fix #6393: for DESCRIBE order by column_index instead of column_name by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6398
* ART (bug) fixes by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6396
* [NodeJS] Support multi-statement prepare by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6278
* Java: Use StringBuilder where appropriate by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6373
* Bitpacking bug by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6402
* bugfix(fsspec): missing fs methods by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6395
* Auto-load HTTPFS extension when http(s)/s3 files are queried and it is not loaded + upgrade SQLite scanner version/other extension fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6401
* Add helpful error message if a setting from an extension is attempted to be set when the extension is not loaded by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6406
* namespace typos in blocking concurrent queue by [@csruiliu](https://github.com/csruiliu) in https://github.com/duckdb/duckdb/pull/6408
* Java: Implement DatabaseMetaData#isReadOnly() by [@MariusVolkhart](https://github.com/MariusVolkhart) in https://github.com/duckdb/duckdb/pull/6375
* CI fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6414
* Parquet: for DELTA_BYTE_ARRAY encoding verify that lengths of subsequent arrays do not exceed length of BYTE_ARRAY by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6412
* Fix #6235: correctly return catalog for views in information_schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6413
* Enable CMAKE_EXPORT_COMPILE_COMMANDS ON default by [@JackDrogon](https://github.com/JackDrogon) in https://github.com/duckdb/duckdb/pull/6394
* Fix #5878: only delete the temp directory if we created it, otherwise delete only our temp files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6425
* Fix under-specified test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6419
* fix: logic fix to allow storage extension to implement DROP DATABASE by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/6430
* Map bug combo of const & non-const lists by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6354
* Issue #6272: Window Scaled Repartitioning by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/6366
* respect column order for partitioned write by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6436
* Properly initialize string vector when reading large JSON arrays of strings by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6437
* Fix #6420 - correctly delete temporary files that are not explicitly read back but just dropped by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6424
* Julia: support Pkg.test() by [@chris-b1](https://github.com/chris-b1) in https://github.com/duckdb/duckdb/pull/6431
* fixes sqlite3_column_bytes nullptr access on some call ordering by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/6409
* Write struct fields as optionally quoted in EXPORT DATABASE by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6416
* Enables sqlite3 wrapper tests for win32 builds by [@TinyTinni](https://github.com/TinyTinni) in https://github.com/duckdb/duckdb/pull/6427
* Adding separate extension_directory configuration setting by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6355
* Preserving replacement_open functionality by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/6449
* [Dev] Add documentation for s3 tests to the extensions/httpfs folder by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6418
* [Python] Fix bug that caused a crash on conversion to arrow by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6441
* Disable operator cache for pull by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6435
* [Python] Add `to_table` and `to_view` alias by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6455
* Improve error message similarity score by using a weighted levenshtein that penalizes non-equal characters more than additions/deletions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6457
* Fix cardinality estimation memoization bug by [@jniewerth](https://github.com/jniewerth) in https://github.com/duckdb/duckdb/pull/6456
* R: Fix protection errors for relational API by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6469
* R: Reenable and stabilize tests by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6474
* Fix multipart upload by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6439
* Fix #6062 (UBSan) by changing order of operations by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6472
* Add split_part function (from Postgres) by [@Alex-Monahan](https://github.com/Alex-Monahan) in https://github.com/duckdb/duckdb/pull/6471
* Auto Install Extensions when opening a database that requires certain extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6479

---

# v0.7.0 - 0.7.0 Preview Release "Labradorius" <a id="v070"></a>

*Released on 2023-02-13*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.7.0)

This preview release of DuckDB is named "Labradorius" after the [Labrador duck (Camptorhynchus labradorius)](https://en.wikipedia.org/wiki/Labrador_duck) which was native to North America and went extinct in 1878 despite its reportedly bad taste.

Again, [@Mytherin](https://github.com/Mytherin) has written a [blog post explaining the exciting list of new features](https://duckdb.org/2023/02/13/announcing-duckdb-070.html) in this release.

Binary builds are listed at the bottom of this post. Please note that it can take a couple of hours until binary builds for all platforms and environments are available.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

## What's Changed
* Use structs to avoid confusing C pointer wrappers by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/4961
* Enum type added to the types metadata table by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5290
* R: code format by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/5185
* Add starts_with function and operator by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5334
* Feature: Allow binary-formatted strings to be cast to integers by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/5337
* For range joins use NL join when the LHS or RHS side is tiny by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5399
* Add support for LATERAL joins by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5393
* [Julia] Add support for consuming a UNION vector into a DataFrame by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5360
* Issue #5314: At Time Zone by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5341
* Decimal values now round when the value given has more decimals than the `scale` of the target by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5362
* Shell: add individual SQL queries to the history, instead of individual lines by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5414
* Shell: add support for history search by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5415
* Parallelise scanning result of ORDER_BY by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5403
* Add translate function by [@zhouliqi](https://github.com/zhouliqi) in https://github.com/duckdb/duckdb/pull/5212
* Enable cmake to recognize AppleClang by [@changhiskhan](https://github.com/changhiskhan) in https://github.com/duckdb/duckdb/pull/5432
* Support enum_code() function by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5408
* Fix binder error and produce more informative error message. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5302
* Parquet Reader: Re-use (de)compression and dictionary buffers and allocate powers of two by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5445
* Support RLE, DELTA_BYTE_ARRAY and DELTA_LENGTH_BYTE_ARRAY Parquet encodings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5457
* print profiling output for deserialized logical query plans by [@ila](https://github.com/ila) in https://github.com/duckdb/duckdb/pull/5448
* Issue #5277: Sorted Aggregate Sorting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5456
* Add internal flag to duckdb_functions, and correctly set internal flag for internal functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5462
* Add experimental R String passthrough support by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5479
* Issue #5258: Quantile Negative Fractions  by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5463
* Arrow stream ingestion for JDBC client by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5449
* PER_THREAD_OUTPUT flag for COPY  by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5412
* Feature: skip broken tests for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5532
* Add Union All support to R extention by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5484
* [Python] Add from_parquet features by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5492
* Add ExtractStatements to C API by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5524
* Improve http retry by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5549
* Issue #5277: Sorted Aggregate Window by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5571
* Issue #5422: QUANTILE_DESC Decimals by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5572
* Issue #5559: 2022g Time Zones by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5570
* [Dev] Clean up of the python pkg folder structure by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5436
* httpfs: check environment vars for AWS Credentials by [@satotake](https://github.com/satotake) in https://github.com/duckdb/duckdb/pull/5419
* Misc union-type improvements by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/5617
* Fix so Left inner join doesn't re-optimize nodes by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5620
* [Substrait] C API + from_substrait_json + bump on substrait version. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5613
* Allow strings in ColumnDataCollection to be written to disk by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5543
* [PythonDEV] Let `clean.sh` be run from anywhere, not just `tools/pythonpkg` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5625
* Reorganize Join order optimizer code by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5621
* [Catalog] Grab missing write_locks in a couple places by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5601
* Parquet info to Substrait by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5627
* HTTP parquet optimizations by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5405
* Adding delta compression to Bitpacking compression by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5491
* [Python] Changed use of DuckDBPyConnection to shared_ptr by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5635
* Merge feature branch into master by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5645
* [Python] Display progress bar by default in an interactive environment by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5596
* Add support for `RESET` statement on configuration options by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5603
* httpfs: Encode url path on request by [@satotake](https://github.com/satotake) in https://github.com/duckdb/duckdb/pull/5587
* Fix broken CI because of RESET statement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5671
* Don't automatically set the bug label on issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5680
* Add support for CREATE VIEW IF NOT EXISTS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5682
* Issue #5622: Validate Timezone Characters by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5658
* Issue 5630 fix. by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5644
* Adding COLUMN_TYPES option for read_csv_auto by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5552
* [Python] Get rid of DuckDBPyResult (merged functionality into DuckDBPyRelation) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5597
* feat: port nodejs tests to typescript by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5632
* Improve nodejs README by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5688
* [Python] Add (partial) support for `numpy.datetime64` objects by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5659
* retry on all httplib errors by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5684
* Return false if file doesn't exist by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/5701
* Adding context option to not run replacement scans and exporting namespace of json substrait function - R by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5689
* Issue #5609: Scope CTE Windows by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5690
* Attempt to fix random NodeJS CI failure by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5710
* [Python] `duckdb.execute()` == `duckdb.default_connection.execute()` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5650
* NodeJS: switch to using package_build, and add support to BUILD_NODE to Makefile by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5691
* JDBC SNAPSHOT Jars by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5687
* Fix NodeJS 19 CI for Windows by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5719
* Fix issue 5664 by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5667
* Issue #5712: CURRENT_TIMESTAMP and CURRENT_TIME by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5713
* [CSVReader] Catch a user error in supplying 'columns' option by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5721
* Improve suggestions when LOAD of an extension fails by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5722
* doc(nodejs): amend arrow stream type docs by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5731
* Fix for TSV throwing during sniffing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5555
* Statically link extensions on Linux with Clang by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/5653
* [Python] Add support for named parameters by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5611
* fix: nodejs source releases should be standalone by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5734
* build: don't install python from chocolatey by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5740
* fix: use non-string-splitting variable interpolation in binding.gyp.in by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5745
* Equalizing DBConfig constructors by [@nicku33](https://github.com/nicku33) in https://github.com/duckdb/duckdb/pull/5747
* We should not treat replacement open paths as disk paths by [@nicku33](https://github.com/nicku33) in https://github.com/duckdb/duckdb/pull/5748
* Allow table in-out functions to be used in correlated subqueries and as LATERAL queries by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5485
* Issue #5750: clangd std::move by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5751
* Always parallelize CSV reader when run over multiple files, and several other fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5757
* Add C++ ODBC tests framework by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5755
* Fix #5730: document older DuckDB versions internally, and state which DuckDB version a specific file came from by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5758
* Add support for non-order preserving parallel writing to the CSV and Parquet writers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5756
* Don't compute SHA if we allow unsigned extensions by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/5760
* Maintain BlockHandle of meta blocks by BlockManager by [@Hzc492](https://github.com/Hzc492) in https://github.com/duckdb/duckdb/pull/5699
* Imdb benchmark validation and benchmark improvements by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5693
* Add support for attaching multiple DuckDB Databases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5764
* Fix #5744: Correctly read "compressed" flag in Parquet V2 header by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5767
* Fix issue 5646 by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5652
* Remove icu from ignored directories when formatted by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5765
* Correctly throw an error when attaching over HTTPFS by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5773
* JDBC add getLong method for timestamp columns by [@Jens-H](https://github.com/Jens-H) in https://github.com/duckdb/duckdb/pull/5783
* Issue #5776: ISO Year Corrections by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5796
* Issue #5669: Advance NULL Pointers by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5793
* Issue #5791: TIMESTAMP/TIMESTAMPTZ Casting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5801
* Issue #4121: INTERVAL List Search by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5805
* Fix incorrect file name in icu-timezone.hpp comment by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5784
* Fully Qualified s3url request with globs by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5774
* Map restructure by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5768
* Issue #5806: Count Star Window by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5810
* S3 uploader fixes by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5769
* fix for FSST segfault by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5824
* Issue: #5717: SetValue TIMESTAMP Case by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5804
* Remove unnecessary code modifying the validity mask of the child vectors of a struct by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5844
* Add date part specifier synonyms by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5845
* Add non ICU time_bucket function by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5835
* Fix list_sort segmentation fault regression by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5823
* Add support for specifying timestamp precision using standard modifiers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5848
* Fix #5836: generate unique oid for attached databases as well by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5851
* Fix #5782 and #5794: in strict mode do not accept leading zeros when parsing numbers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5850
* Fix #5781: add missing flatten call to list_aggregate by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5854
* Fix #5788: improve error message when referencing an alias that contains a subquery (not supported yet) by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5855
* Fix #5853: fully qualify function names inside macros during the binding process by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5856
* CSV Auto Detection: disallow leading + when parsing numbers in strict mode by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5857
* Additional quote handling for string to list cast by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5859
* Parser: add support for unicode space characters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5858
* Adding std:: to every move by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5873
* MinGW Warning Fixes for R by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5881
* Issue #5887: ICU DateAdd Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5888
* NodeJS replacement scans by [@whscullin](https://github.com/whscullin) in https://github.com/duckdb/duckdb/pull/5825
* Further parallelize index creation by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5812
* Added the 'GetExpectedParameterTypes' method to the PreparedStatement… by [@AlexR2D2](https://github.com/AlexR2D2) in https://github.com/duckdb/duckdb/pull/5792
* Extend GenericExecutor by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/5863
* Add signbit function for floating point values by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5862
* Nested/Outer lambda parameters in rhs of inner lambda expressions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5860
* Issue #5826: ICUDateFunc SubtractField Fix by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5869
* Reset `schema` setting when the default schema is dropped by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5874
* Issue #5870: Nested ArgMinMax Results by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5879
* Fix #5779: Parquet writer - when writing lists write only the required subsection of a child entry to the Parquet file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5875
* Change AddString to AddBlob in update_segment.cpp by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/5837
* Support UNION_BY_NAME option in parquet_scan  read_parquet  by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/5716
* Minor fixes for cran by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5904
* [Julia] Use best practices for locking strategies by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5905
* More GCC 13 issues by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5907
* read_csv_auto column_types improvements by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5911
* feat: add parser support for CREATE DATABASE to allow extensions to provide the functionality by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/5898
* Fix #5903: ICU addition overflow by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5908
* Export set operations to relational API by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5872
* Join Order + EXPLAIN Improvements by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5891
* fixed bug in generating grammar script by [@ila](https://github.com/ila) in https://github.com/duckdb/duckdb/pull/5917
* Fix implicit conversion by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5892
* Issue 5660 - do not allow unnest with alias in groupby by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5918
* Parquet: correctly output TIMESTAMP_TZ type when isAdjustedToUTC is set by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5916
* Parquet reader: Fix an issue reading boolean values that cross column pages  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5926
* Allow hive columns to be present in parquet files by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5901
* Fix #5936 - in the Pragma parser, avoid calling ToString() on column references because it might add quotes to keywords by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5939
* Add option to limit parallel compile by [@ashish01](https://github.com/ashish01) in https://github.com/duckdb/duckdb/pull/5935
* Avoid writing .tmp file when redirecting stdout to a file by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5930
* [Macro] Remove limitation for types of expressions accepted as named arguments by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5876
* Benchmarks by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5942
* Fix non-deterministic test failure of parquet_scan by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5954
* [Binder] Throw exception for aggregate function modifiers applied to non-aggregate functions by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5951
* Add logical plan serialization for LOAD, DROP and ALTER by [@ywelsch](https://github.com/ywelsch) in https://github.com/duckdb/duckdb/pull/5934
* Fix trainbenchmark non-determinism adding ordering by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5952
* Add missing include to duckdb.hpp by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5953
* httpfs: remove unneded include by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5945
* [jemalloc] Detect LG_PAGE by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5949
* String to map cast by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5838
* Add time bucket function by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5665
* [Python] Add UNION_BY_NAME to from_parquet arguments by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5913
* Ci partial rework by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5943
* Issue #3423: Positional Join Operator by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5867
* docs: add nodejs connection args to docs by [@tshauck](https://github.com/tshauck) in https://github.com/duckdb/duckdb/pull/5780
* [SQL Logic Test] Add support for environment variables by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5877
* Ci: scope / remove env variables by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5967
* Restore node-pre-gyp credentials by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5970
* Python: Allow replacement scans on pyrelations, move to BoxRenderer and use pending query API for relations by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5962
* Issue #5023: Window Radix Partitions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5909
* Update copyright year by [@sjaenick](https://github.com/sjaenick) in https://github.com/duckdb/duckdb/pull/5974
* Fix #5968: ignore repetition type of root schema by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5969
* Fix #5971: addition and subtraction on infinity of TIMESTAMPTZ by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5978
* Regression ci by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5961
* Add support for UPSERT (INSERT .. ON CONFLICT DO ..) syntax by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5866
* Removing Arrow ABI Testing by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5980
* Remove LogicalTypeId::JSON and implement read_json_objects by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5544
* Make sqlsmith extension compile by [@PedroTadim](https://github.com/PedroTadim) in https://github.com/duckdb/duckdb/pull/5963
* Issue #5023: Radix Partition Cardinality by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5989
* Added UUID case to GetTypeToPython by [@maclockard](https://github.com/maclockard) in https://github.com/duckdb/duckdb/pull/5885
* Export right left and full joins by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5822
* Decimal separator option for CSV reader by [@eeroel](https://github.com/eeroel) in https://github.com/duckdb/duckdb/pull/5958
* feat(python): fsspec filesystems by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5829
* Fix amalgamation build: returning (std::)move will otherwise be flagg… by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/5991
* Fix issue 5675 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6001
* Only copy relevant list children in column data collection by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5982
* Many Parallel CSV Reader Fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5950
* [python] Use duck typing for arrow dataset by [@changhiskhan](https://github.com/changhiskhan) in https://github.com/duckdb/duckdb/pull/5998
* [Import/Export] Exported databases can now be safely moved by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5965
* Add count_if as a macro function by [@ashish01](https://github.com/ashish01) in https://github.com/duckdb/duckdb/pull/6007
* Rcpp17 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6022
* [Dev] Fix #6020: Fix failure of CI with pyarrow by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/6023
* Format script: enforce same varargs formatting by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6014
* fixed fsst issue with size calculation check by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6016
* Fix Node.js Windows CI jobs by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6041
* fix 5923 - convert float16 column in pandas to float32 column by [@wordhardqi](https://github.com/wordhardqi) in https://github.com/duckdb/duckdb/pull/6028
* Add support for JDBC Metadata for the nested typess List, Struct, Map by [@jonathanswenson](https://github.com/jonathanswenson) in https://github.com/duckdb/duckdb/pull/6029
* move block checksum from FileBuffer to BlockManager by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/6033
* Optimize SELECT UNNEST in lateral joins by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6035
* Fix Python CI: numpy added before-build by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6056
* Track exact ART size and many ART improvements by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5893
* Use back-up to download unixODBC by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6063
* Copy into partition by by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5964
* Add support for a pluggable storage and catalog back-end, and add support for a SQLite back-end storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6066
* Various fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6036
* out of tree extension improvements by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6049
* Fix checks on R-devel by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/6025
* Update editor config by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6065
* Implement read_json and improve JSON parse errors by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5992
* [Python] Add `read_csv` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6015
* Add bar function by [@papparapa](https://github.com/papparapa) in https://github.com/duckdb/duckdb/pull/5993
* Remove console.log from UDF catch by [@chrisbrain](https://github.com/chrisbrain) in https://github.com/duckdb/duckdb/pull/6082
* Fix performance regression in read_csv_auto auto detection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6078
* Allowing lambdas in table functions by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6039
* Add relational tests back by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6038
* Force-enabling DEBUG_MOVE for debug builds  by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6099
* [Python] Make `pyarrow.dataset` optional by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6106
* Fuzzer issue #5984 no 25 by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6107
* [ParquetWriter] Prevent creating broken parquet files by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6104
* [Fuzzer] Fix issue related to dropping a generated column by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6113
* Implement md alias for motherduck and add motherduck to list of known extensions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6111
* Map extract bug  by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6109
* [Dev] Fix some unqualified `move`'s that snuck in by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6117
* Ccaching2 by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6101
* Making CSV Parallel tests more robust by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6122
* [Julia] Fix execute deadlock by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6123
* [Python] Check overflow in DATE -> datetime conversion by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6125
* Python box rendering: limit rendering to 10K rows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6121
* Correctly setting the validity of constant struct vector references by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6118
* Fix #6092 - retain casing for keywords by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6112
* Fuzzer issue 9 and 40 from #5984 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6126
* fix(python): fix gil error in fsspec integration  by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6140
* Fuzzer issue #5984 no.43. Substring generating an invalid string by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6139
* Remove sporadically failing Windows CI CSV reader test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6147
* issue 5984  #42 disable nan as random seed by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6128
* [Python] Add `read_parquet`, `to_parquet` and `to_csv` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6129
* Make ATTACH work over HTTP(S), and fix ATTACH for databases with custom types by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6141
* Replace replacement_opens with storage_init by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6132
* Fix to Fuzzer 5 item #30, plus various very marginal fixes by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6137
* Improve read_json transform errors and fix some read_json related bugs by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6145
* [Fuzzer] ArgMax Segfault by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6144
* Fix #6136: fix issue with SINGLE JOIN where NULL values of a struct were not correctly set  by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6148
* Fix fuzzer issue 35: correctly check overflows on casts from float/double to unsigned integers by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6151
* [Fuzzer] Unset 'swizzled' flag in SortedData by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6143
* Introduces Bit type by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5990
* Fix issue related to NodeJS UDF not returning constant vectors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5697
* 6055 column alias in where clause results in binder error by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6162
* Skip concurrent index/grouping sets tests for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6164
* Skip attach over HTTPFS test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6167
* 5982 (8, 12, 15) binder error when group by all & having clause both refer to column from correlated subquery by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/6163
* More minor fixes to warnings by [@carlopi](https://github.com/carlopi) in https://github.com/duckdb/duckdb/pull/6138
* Fix fuzzer issue 14: correctly switch between deleting from transaction local storage and main table based on ids by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6166
* fix(nodejs): error as object instead of string by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6174
* Fixing Parallel CSV Reader over multiple files by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/6131
* Issue 6157 duckdbj database meta data supports like escape clause by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6178
* Fuzzer issue: Grapheme function overflow by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6171
* Fix fuzzer issue 31 (again) by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6172
* Wiring storage_info into attach and create_transaction_manager calls by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/6161
* Try to auto-cast list_filter input and throw exception when failing by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6119
* Pass unrecognized configuration options to storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6177
* Art fuzzer issues by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6168
* Fix Python deadlock - execute all PyRelations through the shared execute loop, and throw exception if Pandas Scan is called while GIL is held by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6186
* No lambdas in CHECK constraint and generated columns by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6190
* fixes #6159 by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6183
* Fix lambda warning on building by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/6195
* Python: Make duckdb.sql return results for non-select queries in the form of a ValueRelation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6196
* Fix #6204: fix buffer management in ColumnDataRowCollection construction used in BoxRenderer by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6205
* Python: make imports lazy, add .sql as an alias for .query, and add integration functions with polars by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6181
* bugfix(python): fsspec file modes by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/6207
* Fix #6182: add DESCRIBE to the set of table name keywords by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6206
* Fix #5983: avoid serializing type as part of numeric statistics (de)serialization by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6197
* Fuzzer 16: Between type mismatch  by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/6194
* [Fuzzer] Fixes fuzzer issue 27 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6193
* Fuzzer fixes 2, 3 and 5 of #5984 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/6187
* DuckDBJ: sanitize values of tableTypes argument in DatabaseMetadata.getTables() by [@rpbouman](https://github.com/rpbouman) in https://github.com/duckdb/duckdb/pull/6180
* Add more tests for fetch* functions, and add support for Pandas-style .describe() by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6212
* More descriptive error message if we are using a table function as a scalar function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6201
* Make NumPy dependency optional by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6215
* Implement FORMAT JSON for COPY/IMPORT/EXPORT by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/6170
* Fix ODBC CI by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6216
* [Python] Add `read_json` method by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6165
* [C-API] Add struct list_entry, ListVector::reserve and ListVector::set_size by [@eddyxu](https://github.com/eddyxu) in https://github.com/duckdb/duckdb/pull/6155
* Disable the Node build cache in the CI for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6220
* [Java] BigDecimal scale > precision bug fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/6110
* Fix #6044: in Value::DECIMAL, switch on the width instead of assuming the width is correctly set with the corresponding integer type by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6219
* Fix #6184: skip unused column removal right after a filter with entries in the projection map by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6221
* Bump postgres scanner by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/6226
* Add support for "show" to py relation objects by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/6224

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.6.1...v0.7.0

---

# v0.6.1 - 0.6.1 Bugfix Release <a id="v061"></a>

*Released on 2022-12-06*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.6.1)

This is a bug fix release for various issues discovered after we released 0.6.0. There are no new features, just bug fixes.
## What's Changed
* Correctly accept BUILD_JEMALLOC_EXTENSION on Linux by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5343
* [julia] fix docstring of `load!` and relax type restriction by [@jfb-h](https://github.com/jfb-h) in https://github.com/duckdb/duckdb/pull/5354
* Bump DuckDB_jll compat to v0.6 by [@jeremiahpslewis](https://github.com/jeremiahpslewis) in https://github.com/duckdb/duckdb/pull/5356
* Issue #5342: DATE_PART Struct Indexing by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5382
* Add reference to cleanup function for duckdb_result_get_chunk by [@ak-coram](https://github.com/ak-coram) in https://github.com/duckdb/duckdb/pull/5389
* Fix #5390: in filter pull-up optimizer avoid adding columns to one side of a set operation by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5400
* Fix #5371: correctly use instance cache in JDBC and ODBC connector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5398
* Add support for reading JSON type columns from Parquet files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5401
* [Dev] Fix compilation issues related to MSVC and Windows.h by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5386
* fix: upgrade npm's internal node-gyp by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5402
* [Appender] Appender can now properly append to DECIMAL columns by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5364
* Fix bug causing loss of order preservation in insert by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5427
* Allocator: throw std::bad_alloc if a malloc allocation fails by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5439
* Fix the use of COLUMNS(...) in ORDER BY clause by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5444
* Adding lazy relation -> data.frame conversion for R client by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5181
* Fix #5450, don't crash on integer dates in R by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5451
* Issue #5366: QUANTILE_DISC Intervals by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5442
* Remove the f off by [@hatvik](https://github.com/hatvik) in https://github.com/duckdb/duckdb/pull/5475
* Fix many fuzzer issues by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5482
* Allow column references in constant table functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5483
* Node register arrow ipc buffer fix by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5433
* Add initializer for queue_insertions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5504
* Disabling per-value materialization of r altrep strings in results by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5454
* Correctly set delim_offset in flatten dependent join and disable linux arrow test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5509
* update arrow extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5506
* [Python] Correct stub for DuckDBPyConnection::df by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5385
* Add deserialization to custom operators by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/5496
* [Python] No longer truncate ByteArray values by nullbytes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5517
* Add in the pg_database, pg_proc, and pg_settings views to pg_catalog by [@jwills](https://github.com/jwills) in https://github.com/duckdb/duckdb/pull/5526
* Fix various BufferManager issues by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5476
* Add feature request link by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5324
* [Python] Fix `relation.query()` not accepting non-select statements by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5531
* fix issue #5488 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5519
* [Python] Adding back Query interrupt support (through Ctrl+C) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5487
* Adding dummy user/username/password settings by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5530
* Add memory leak tests, and fix memory leaks related to repeated table creation/destruction by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5537
* DuckBox renderer fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5539
* Fix #5533: correctly use timestamp logical type unit in Parquet stats reader by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5540
* Disable the extended code coverage tests for now by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5542
* NLJoin is not always terrible by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5538
* naming mismatch for linux arm extension upload by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5556
* Deprecate 'sprintf' usage using MacOSX SDK 13  by [@darrenfu](https://github.com/darrenfu) in https://github.com/duckdb/duckdb/pull/5545
* Fix #5546: allow foldable scalar expressions in standard table functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5550
* Upgrade sqlite scanner hash by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5551
* [Python] Fixed bug where creating a cursor from a closed connection caused a segfault by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5565
* Fsst pull bugfix from upstream by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5567
* Parquet: Not setting num_children for primitive types as per spec by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5579
* [Python] Fix accidental dependency on `pandas` by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5581
* Throw error when sorting or using indexes on big endian architecture by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5588
* fix: separate artifacts for 32bit and 64bit builds by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5592
* Bug fix for 5523 by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5554
* Disabling truncating of temporary buffer manager files on Windows by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5600
* Removed FSST unused global that triggered compiler warning by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5602
* Copy JDBC Properties to not lose readonly setting by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5594

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.6.0...v0.6.1

---

# v0.6.0 - 0.6.0 Preview Release "Oxyura" <a id="v060"></a>

*Released on 2022-11-14*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.6.0)

This preview release of DuckDB is named "Oxyura" after the [White-headed duck (Oxyura leucocephala)](https://en.wikipedia.org/wiki/White-headed_duck) which is an endangered species native to Eurasia.

This time, [@Mytherin](https://github.com/Mytherin) has written a [blog post explaining the quite long and exciting list of new features](https://duckdb.org/2022/11/14/announcing-duckdb-060.html) in this release.

Binary builds are listed at the bottom of this post. Please note that it can take a couple of hours until binary builds for all platforms and environments are available.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

## Featured Changes
* Optimistically write data to disk when batch loading data into the system by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4996
* Parallel non-order preserving CREATE TABLE AS and INSERT INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5033
* Parallel order preserving CREATE TABLE AS and INSERT INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5082
* FSST compression by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4366
* CHIMP128 Compression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4878
* Patas Compression (float/double) (variation on Chimp) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5044
* Parallel CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5194
* Parallelize CREATE INDEX of ART by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/4655
* Improve memory management of ART indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5292
* DISTINCT aggregates *with* GROUP BY are now executed in parallel by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5146
* Nested "UNION"-type by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/4966
* Allow for queries to start with FROM, instead of with SELECT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5076
* Support for the COLUMNS expression, which allows expanding computations on multiple columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5120
* Python-style list-comprehension syntax [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4926
* Improvements to Out-of-Core Hash Join by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4970
* jemalloc "extension" for Linux by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4971
* Improve rendering of result sets for the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5140
* Add auto-complete support to the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4921
* Nicer looking progress bar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5187


## All Changes
* Fix #4747: Handle pandas num categories between 128 and 256 by [@pankajp](https://github.com/pankajp) in https://github.com/duckdb/duckdb/pull/4757
* Julia 0.5.1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4758
* Fix #3595: avoid using system hash for floating point values by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4761
* Fix #4704. Correct the column name for pragma_storage_info with generated column by [@zippond](https://github.com/zippond) in https://github.com/duckdb/duckdb/pull/4750
* Allow to load extensions through compiler variable definitions by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4767
* Fix some typo in code comments by [@buaazhwb](https://github.com/buaazhwb) in https://github.com/duckdb/duckdb/pull/4769
* Enhance duckdb_constraints() by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/4346
* Issue #4764: Window Ignore Nulls by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4773
* [Python (Relational)] Query now returns a DuckDBPyRelation by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4471
* R types expansion by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4778
* Add json_contains by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4686
* Fix #4152: create base table reference in returning clause so generated columns are correctly resolved by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4783
* Fix Exists and ANY correlated subquerys by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4752
* Fix for ORDER BY on large dictionary vectors: correctly pass offset into get_index of selection vector by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4787
* Missing json_contains in extension list by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4788
* Extensible Casts & Cast Function Rework by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4785
* Bump sqlite scanner by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4789
* Improve sorting for strings and push projections into sort operator by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4697
* Parquet: Refactor decompression, including more complete datapage v2 support by [@wisp3rwind](https://github.com/wisp3rwind) in https://github.com/duckdb/duckdb/pull/4628
* Parallelize CREATE INDEX of ART by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/4655
* Unify LocalStorage and DataTable Storage by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4798
* feat: support passing all db config to jdbc driver by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4794
* Fix #4806: correctly use offset index in pragma_table_info on view by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4807
* Map VARCHAR, JSON, ENUM to Julia String by [@nickrobinson251](https://github.com/nickrobinson251) in https://github.com/duckdb/duckdb/pull/4810
* fix: support SHOW query types in jdbc client by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4799
* Replacement Open Hooks by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4721
* Build multiple out of tree extensions in one pass by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4828
* fix(jdbc): release results before releasing statements by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4831
* Fix for #4827 by [@PedroTadim](https://github.com/PedroTadim) in https://github.com/duckdb/duckdb/pull/4829
* Multiblock2 by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/4555
* Disconnect after test by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/4835
* Check prefix length, not string_t::INLINE_LENGTH when comparing strings while sorting by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4816
* Adding a CI workflow to re-build individual out-of-tree extensions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4833
* fix: json getColumnType error by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4847
* Attempt two at rebuilding old extensions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4848
* Updating postgres scanner by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4832
* Extension Rebuild Attempt 3 by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4849
* Adding overwrite flag to R duckdb_register by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4850
* Move LocalStorage row groups directly to DataTable instead of re-appending by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4851
* fix for macos CI by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4854
* Fully qualified s3url by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/4786
* FSST compression by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4366
* Julia: add support for handling errors in replacement scans by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4865
* Extension build: turn IGNORE_WARNINGS into generic OPTIONS field, and add --main-only field by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4866
* Issue #4867: Approximate Quantile Hugeint by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4868
* Install OpenSSH on ubuntu 16 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4877
* Join order regression test: add 20% threshold to cardinalities before we care about regressions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4880
* Move LocalStorage row groups directly to DataTable if there are enough rows being appended by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4876
* Allow referencing of aliases in SELECT clause and TPC-DS extension clean-up by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4879
* Add github to known hosts by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4884
* Adding a serialized version of all TPCH queries and test we can read them by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/4605
* Add support for custom bind functions to RegisterCastFunction, and propagate client context to the bind function by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4885
* CSV reader: quoted NULL values should be kept as non-NULL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4888
* fix: add numpy to setup_requires to fix build from source by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4893
* fix openFlags overwriting in shell fixing #4894 by [@kouta-kun](https://github.com/kouta-kun) in https://github.com/duckdb/duckdb/pull/4895
* Remove filter columns from table scans if they are unused in the remainder of the plan by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4817
* feat: add duckdb_library_version method and fix extension load state by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4881
* uuid.cpp: GenerateRandomUUID: fix indexing by [@nodakai](https://github.com/nodakai) in https://github.com/duckdb/duckdb/pull/4892
* Update serialized plans by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4900
* Add CPython 3.11 to build matrix by [@edgarrmondragon](https://github.com/edgarrmondragon) in https://github.com/duckdb/duckdb/pull/4906
* Support UNION_BY_NAME option in read_csv_auto  by [@douenergy](https://github.com/douenergy) in https://github.com/duckdb/duckdb/pull/4837
* support for virtualizing storage layer by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/4858
* Reduce data set size of IE join test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4905
* Making sure parquet column readers return the expected amount of rows by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4909
* Issue #3187: TIMESTAMPTZ <=> VARCHAR by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4904
* Fix breaking CI on unused variable errors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4916
* Issue #4912: NOW returns TIMESTAMPTZ by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4914
* Add ClickBench to benchmark suite by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4919
* Add auto-complete support to the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4921
* Add support for list parameters to read_csv and read_csv_auto by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4922
* + methods for sink_schema by [@alitrack](https://github.com/alitrack) in https://github.com/duckdb/duckdb/pull/4918
* Add Python-style list-comprehension syntax support to SQL by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4926
* Auto-complete: prioritize files with known extensions, and include position at which completion should be placed by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4930
* Fix ART by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4763
* [Python] Add support for Protocols by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4435
* Work-around for #4935: throw internal error if there is no node by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4940
* Fix #4933: avoid introducing NULL value on first value after empty row by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4934
* Issue #4942: Check DESC Errors by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4945
* Issue #4944: Negative Unpadded Centuries by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4948
* Issue #4943: Date Nanosecond Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4947
* feat: add copy method for logical_operator by [@stephaniewang526](https://github.com/stephaniewang526) in https://github.com/duckdb/duckdb/pull/4915
* Bug fix for segmentation fault in list apply by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/4910
* Fixing hmac for large secrets in S3FS by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4949
* buffered by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/4924
* Caching Database Instances by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4414
* Faster ART key allocations, faster index join by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/4800
* Add CI run with disabled string inlining by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4957
* Split row-group append into Initialize/Append/Finalize and separate append code from version info append by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4953
* Issue #4965: DateDiff Day Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4973
* noswizzle by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/4923
* Issue #4978: DATE_SUB Subtraction Overflows by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4985
* feat: request that people raise scanner issues in the right repos by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4956
* avoid double-writing the index data by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/4946
* [Python] Optional Pandas Date as datetime by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4633
* Optimistically write data to disk when batch loading data into the system by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4996
* Bring substrait-extension build back by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4993
* fix(jdbc): shutdown database after last connection is closed by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4990
* Add support for TRUNCATE [TABLE] syntax by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5001
* Directly merge row groups from local storage into table even if the table has indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5003
* String to list casting by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/4994
* Optimize away DELIM_JOIN even when the child join with the DELIM_GET is an inequality join by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4991
* JDBC: Add public getter for statement return type by [@Jens-H](https://github.com/Jens-H) in https://github.com/duckdb/duckdb/pull/5014
* Remove duplicate code by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5008
* Fix lambda bug for struct extract by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5007
* Support CREATE OR REPLACE / TEMPORARY / IF NOT EXISTS with CREATE MACRO / FUNCTION by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5006
* Fixing #4859, correctly passing struct type to recursive calls by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5017
* [CSV] Added line number to 'maximum_line_size' exceeded error by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5018
* ODBC/JDBC Database Instance Cache by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5004
* String functions: count unicode codepoints instead of grapheme clusters by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5028
* Support file_search_path with globbing by [@whscullin](https://github.com/whscullin) in https://github.com/duckdb/duckdb/pull/5021
* First cut at TypeScript type declarations for DuckDb by [@antonycourtney](https://github.com/antonycourtney) in https://github.com/duckdb/duckdb/pull/5025
* Undefined behavior sanitizer error fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5030
* [Compression] CHIMP128 Compression Algorithm by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4878
* Parallel non-order preserving CREATE TABLE AS and INSERT INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5033
* fsst bugfix by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5042
* Avoid installing git for ODBC Windows CI Run by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5051
* Fix for shell auto-complete by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5047
* Fix a race condition in an assert by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5049
* [Python] Accept 'schema' in table reference by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5059
* Fix levenshtein(s1, s2) for empty strings by [@lmores](https://github.com/lmores) in https://github.com/duckdb/duckdb/pull/5062
* Correctly handle NULL values in compound ART keys by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/5010
* Issue #5023: Fully Parallel Partitioning by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5024
* Enable remote optimizer test by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/5019
* make wal impl more reusable by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/5071
* Optionally allow for queries to start with FROM, instead of with SELECT by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5076
* [Python] Fall back to DOUBLE for unsupported DECIMAL widths by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4749
* Issue #5046: Window Size Restriction by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5079
* Shell: fixes for auto-complete of home directory and absolute paths by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5081
* Varsizeblock by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/5069
* Parallel order preserving CREATE TABLE AS and INSERT INTO by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5082
* Fix #5077: correctly handle carriage return newlines in CSV auto-detection by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5083
* caching table-in-out-functions & chunk cache refactor by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4992
* Fix for #4935: throw internal error if there is no node by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5089
* Add nested "union"-type by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/4966
* Row Group Collection - smaller allocations for tiny tables by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5086
* chore: pin setuptools_scm to py3.6 compatible version by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5099
* Correctly scan unaligned row groups in DataTable::ScanTableSegment by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5101
* feat: implement DatabaseMetadata#getFunctions() by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5090
* Support batch index in arrow scans by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5085
* Arrow support for JDBC ResultSet by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5088
* fix(jdbc): gracefully handle null bytes in strings by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5100
* Add file_row_number flag to parquet reader by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5084
* Fix comment by [@zhouliqi](https://github.com/zhouliqi) in https://github.com/duckdb/duckdb/pull/5110
* Add ErrorManager class, allow SQLLogicTests to verify error messages, and improve CSV reader errors by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5103
* Add support for the COLUMNS expression, which allows expanding computations on multiple columns by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5120
* Issue #5107: ICU Data Scripts by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5109
* Batch Insert: Add support for eagerly merging of small adjacent batch indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5113
* Add temporary 'skip_reload' to problematic test by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5133
* [Python] Add MSVC `/utf-8` flag by [@metab0t](https://github.com/metab0t) in https://github.com/duckdb/duckdb/pull/5129
* Convert values whose data types do not have explicit support in NodeJS into strings by [@jwills](https://github.com/jwills) in https://github.com/duckdb/duckdb/pull/5130
* Download OpenSSL from Github instead by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5141
* Add BoxRenderer class - which improves rendering of result sets for the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5140
* [Dev] Add `extension` to excluded folder in `format.py' (format-fix/master) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5142
* Fix #5124: correctly deal with DICTIONARY vectors inside LIST vectors for various functions by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5151
* [Aggregate] DISTINCT aggregates *with* GROUP BY are now executed in parallel by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5146
* [Python] Exceptions encountered in 'with' body are now properly propagated by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5157
* Create enum type from query by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5126
* Fix #5149: better tracking of query location in column reference, and improve error message by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5158
* Allow builder to set `GIT_COMMIT_HASH` by [@Y--](https://github.com/Y--) in https://github.com/duckdb/duckdb/pull/5164
* Fsst bug by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5168
* [Python] Arrow Dataset type requirement is now less strict by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5170
* Fix progress bar of regular table scan by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5171
* Document highlight features in the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5176
* Support parallel (batch) insertion into tables that have indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5177
* Support casting of hex strings to integer types by [@IanCal](https://github.com/IanCal) in https://github.com/duckdb/duckdb/pull/5160
* [Aggregate] Fix regressions caused by latest distinct HT operator PR by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5169
* R: Remove duckdb:: qualifier by [@krlmlr](https://github.com/krlmlr) in https://github.com/duckdb/duckdb/pull/5135
* [Compression] Patas Compression (float/double) (variation on Chimp) by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5044
* [C-API] Decimal casting to other type fixes by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4526
* Default NULL handing for CARDINALITY function by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/5073
* Update OpenSSL to 1.1.1s by [@sjaenick](https://github.com/sjaenick) in https://github.com/duckdb/duckdb/pull/5184
* Box renderer: Always display "0 rows" if there are no rows by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5188
* chore: request OS version and architecture in bug reports by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5191
* String to struct cast by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5147
* Optimize String Split by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5186
* Nicer looking progress bar by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5187
* Correctly call Reset on cast_chunk in CSV writer to prevent string heap from continuously accumulating data by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5199
* Increase vector size to 2048 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5193
* Issue #5131: Time Zone 2022f  … by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5198
* jemalloc "extension" for Linux by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4971
* Further clarify database invalidation error, unify db/transaction invalidation, and move errors to error manager by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5213
* fix: build NodeJS bindings for M1 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5189
* Arrow extension by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5195
* Fix distinct aggregate race: insert next event before scheduling tasks by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5219
* Avoid exporting SQLite symbols from our sqlite_api_wrapper when building the shell by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5217
* buffermanager accounting by [@jkub](https://github.com/jkub) in https://github.com/duckdb/duckdb/pull/5134
* Allow NULL bytes in strings by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5218
* Use cmake's find_package to trace git executable by [@bleskes](https://github.com/bleskes) in https://github.com/duckdb/duckdb/pull/5220
* Issue #5197: Deterministic TimeZone Abbreviations by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5214
* Issue #5239: DATE_DIFF Microseconds Overflow by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5242
* Various CI Improvements/Speed Ups by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5228
* Issue #5240: DATE_TRUNC Statistics Orientation by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5241
* Improvements to Out-of-Core Hash Join by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4970
* Add support for extension aliases by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5226
* Physical batch insert: correctly optimistically flush batches to disk that are close to our row group size by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5231
* Fix Python stub test by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5245
* DISTINCT grouped aggregate lowered memory consumption optimization by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5227
* fix: bump node-gyp version by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5221
* json_extract bugfixes and memory accounting bugfix by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5204
* [Python] Add support for strided `float32` and `float64` data by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5256
* Issue #4978 - 4. Cardinality estimator assertion errors and filter errors by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5232
* Adding total_uncompressed_size to parquet column chunk metadata by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5216
* Issue #5258: Inverse Percentile NULLs by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5260
* Issue #5205: TIMESTAMPTZ Casting by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5229
* 6. Like empty list assertion error by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5261
* fix: fix python stub test by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5269
* Issue #5254: Validate Collation Expressions by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5270
* Cast overflow varchar to decimal by [@LindsayWray](https://github.com/LindsayWray) in https://github.com/duckdb/duckdb/pull/5262
* Issue #5259: ChunkCollection Sort Values by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5280
* Parallel CSV Reader by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5194
* Add Java constant for default schema name by [@michaeljohnalbers](https://github.com/michaeljohnalbers) in https://github.com/duckdb/duckdb/pull/5271
* Fix/4978 substring overflow by [@Maxxen](https://github.com/Maxxen) in https://github.com/duckdb/duckdb/pull/5273
* token url encoding bug in S3 glob by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5248
* fix: don't build M1 NodeJS binaries on node versions that don't support M1 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5284
* Several CI fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5281
* Fix several fuzzer issues, move client context into ExpressionExecutor, and ColumnList index rework by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5276
* feat: prebuild for NodeJS 19 by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5295
* Calendar overflow Fixes by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/5287
* Add correlated columns to LogicalDistinct::distinct_targets when flattening dependent joins by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5286
* Fuzzer fixes - 4978 (16) Binder assertion error by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5285
* [Fuzzer] Fix triggered assertion in LogicalOperator::Verify by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5283
* Disable url decoding of http header values by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5275
* fix: pg constraint foreign key by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5264
* Improve memory management of ART indexes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5292
* Several parallel CSV reader fixes by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5291
* [Python] support for pandas experimental NA type by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5246
* Add internal verification to unpinning buffer blocks by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5263
* [Python] Fix support for UInt64 and similar by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5299
* Add support for quoted schema/column in DESCRIBE statement by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5230
* Increase SQLite scanner version by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5309
* node / TypesScript bindings: add missing accessMode argument to Database constructor. by [@antonycourtney](https://github.com/antonycourtney) in https://github.com/duckdb/duckdb/pull/5307
* Initial version of extension to allow creating operators outside of duckdb core lib by [@rjatwal](https://github.com/rjatwal) in https://github.com/duckdb/duckdb/pull/5144
* Improve progress bar & box rendering by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5304
* Parallel csv auto fixes by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/5303
* Current fix for Issue #5266 Returning error with rowid by [@Tmonster](https://github.com/Tmonster) in https://github.com/duckdb/duckdb/pull/5267
* [Fuzzer] Add support for use of generated columns in GROUP BY expression by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5249
* [Fuzzer] Generated columns now work properly with query-level aliases by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5308
* fix: use oldest supported numpy to build for a given python version by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/5319
* [UB sanitizer] Prevent doing arithmetic on NaN in 'logical_limit_percent.cpp' by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/5322
* Fix OSX Builds on Master - Revert #5319 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/5329
* Bump Postgres Scanner by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/5325
* disable node client arrow ipc replacement scans by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/5332
* Shared ColumnDataAllocator: hold lock for just a bit longer by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/5333

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.5.1...v0.6.0

---

# v0.5.1 - 0.5.1 Bugfix Release <a id="v051"></a>

*Released on 2022-09-19*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.5.1)

This is a bug fix release for various issues discovered after we released 0.5.0. There are no new features, just bug fixes. The following PRs were included in this release:

* [Fuzzer] Issue #4152 - Lag window function issue by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4603
* Fix zonemap check for VARCHAR by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4613
* Remove the DLLEXPORT from deleted API methods by [@emmenlau](https://github.com/emmenlau) in https://github.com/duckdb/duckdb/pull/4611
* Fix update statement on generated column by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4616
* [Fuzzer] Issue #4152 - Limit 0% on ANY subquery by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4544
* [Fuzzer] Issue #4610 - Vacuum table with generated column by [@lokax](https://github.com/lokax) in https://github.com/duckdb/duckdb/pull/4622
* [Fuzzer] Decimal scale+width overflows too quickly by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4627
* [Fuzzer] issue #4566 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4592
* Issue #4635: DATE_DIFF Week Boundaries by [@hawkfish](https://github.com/hawkfish) in https://github.com/duckdb/duckdb/pull/4648
* Fix issue #4630 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4642
* [Python] Fix unwanted conversion from NaN -> NULL in param list by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4624
* Fix home directory setter by [@attilahorvath](https://github.com/attilahorvath) in https://github.com/duckdb/duckdb/pull/4617
* fix(jdbc): correct mapping for TIMESTAMP_WITH_TIME_ZONE by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4654
* Fix bug changing input order on array_sort column by [@taniabogatsch](https://github.com/taniabogatsch) in https://github.com/duckdb/duckdb/pull/4643
* Fix issue #4625 by [@lnkuiper](https://github.com/lnkuiper) in https://github.com/duckdb/duckdb/pull/4653
* [Extensions] Suggesting which extension to Load/Install by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4634
* Fixes issue #4123 by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4523
* Updating jdbc deploy script by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4663
* Consistent struct definitions by [@hannes](https://github.com/hannes) in https://github.com/duckdb/duckdb/pull/4667
* Fix #4666 by [@taofengliu](https://github.com/taofengliu) in https://github.com/duckdb/duckdb/pull/4670
* Fix for #3417 by [@PedroTadim](https://github.com/PedroTadim) in https://github.com/duckdb/duckdb/pull/4664
* feat: improve python replacement scan error by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4672
* [C-API] Data chunk invalid left-shift by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4660
* fix: correct mislabelling of amd64 libs in jars by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4691
* Fix #4647 by [@taofengliu](https://github.com/taofengliu) in https://github.com/duckdb/duckdb/pull/4698
* Throw error if attempting to delete from table without physical columns by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4693
* Fix #4475: allow ignore_errors in read_csv and read_csv_auto by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4713
* Fix #4442: correctly handle TIMESTAMP logicalType in Parquet files by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4714
* Fix #4699: when no file is found globbing, fallback to using the literal string name as a path by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4716
* Fuzzer fixes batch 1 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4707
* Fix #4677. Correctly set_not_null when table contains generated column by [@zippond](https://github.com/zippond) in https://github.com/duckdb/duckdb/pull/4706
* Fix #4703 by [@taofengliu](https://github.com/taofengliu) in https://github.com/duckdb/duckdb/pull/4715
* Fixing Extension naming CI Checker by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4717
* [Python(pandas)] Scan multiple chunks worth of values from a 'object' dtype DataFrame by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4692
* Fix #4694: Keep shared pointer to pipelines around in additionally scheduled events by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4724
* Fuzzer Batch Fixes 2 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4722
* Fix #4702. Correctly use index when generated column is involved by [@zippond](https://github.com/zippond) in https://github.com/duckdb/duckdb/pull/4727
* Fix for #4583 by [@PedroTadim](https://github.com/PedroTadim) in https://github.com/duckdb/duckdb/pull/4728
* Fuzzer fix batch 3 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4726
* Fix #4562: generate table index for dummy scan generated from VALUES clause by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4731
* [Arrow] Guarantee threads don't call get_next after stream is done. by [@pdet](https://github.com/pdet) in https://github.com/duckdb/duckdb/pull/4712
* Correctly catch and report exceptions thrown during a pipeline's scheduling by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4733
* Fix for issue #4708 by [@PedroTadim](https://github.com/PedroTadim) in https://github.com/duckdb/duckdb/pull/4711
* Fix #4568: correctly handle casts in deliminator by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4734
* No longer disable vptr sanitizer on M1 macs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4735
* Use version tag as dir for extensions for releases by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4729
* Correctly call ::Skip function of child of structs by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4736
* [Map] Map extract now properly uses the selection vectors of the `map` and `key` vectors by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4725
* Fix #4356 by [@taofengliu](https://github.com/taofengliu) in https://github.com/duckdb/duckdb/pull/4740
* Fuzzer Batch 4 by [@Mytherin](https://github.com/Mytherin) in https://github.com/duckdb/duckdb/pull/4737
* feat: bump Julia package version by [@Mause](https://github.com/Mause) in https://github.com/duckdb/duckdb/pull/4742
* Julia API: Add load! to add a DataFrame as a table by [@jfb-h](https://github.com/jfb-h) in https://github.com/duckdb/duckdb/pull/4743
* aarch64 extensions by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4745
* Faster hive part filters by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4746
* [Python] DECIMAL with value 0.00... issue fix by [@Tishj](https://github.com/Tishj) in https://github.com/duckdb/duckdb/pull/4690
* enable out-of-tree extensions for aarch64 by [@samansmink](https://github.com/samansmink) in https://github.com/duckdb/duckdb/pull/4751

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v0.5.0...v0.5.1

---

# v0.5.0 - 0.5.0 Preview Release "Pulchellus" <a id="v050"></a>

*Released on 2022-09-05*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.5.0)

This preview release of DuckDB is named "Pulchellus" after the [Green pygmy goose (Nettapus pulchellus)](https://en.wikipedia.org/wiki/Green_pygmy_goose) which is native to Australia where [VLDB 2022](https://vldb.org/2022/) is starting today. Despite being called a "goose" it is actually a duck.

Binary builds are listed at the bottom of this post. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Below a list of changes in this release

## Major Changes & Features

 - #4189: Implement Out-of-Core Hash Join and Re-Work Query Verification
 - #4022: Art Index Storage
 - #4274: Join Order Optimizer improvements
 - #4420: Logical Plan Serialization
 - #4137, #4347, #4293, #4190, #4178, #4177, #3954 & #4159: Scalability and performance improvements for Window operator
 - #4004: Add support for extensions to the parser, and add an example of this to the loadable extension demo
 - #4089: Signed Extensions
 - #4097 & #4211: Filename column + Hive partitioning support for Parquet Reader
 - #4501, #4511: Aarch64 Linux builds of CLI, shared library, JDBC & ODBC

## Minor Changes & Bug Fixes
 - #4594: [Map] Fix map_extract from multiple rows
 - #4585: Fix for r test instability, #4549
 - #4560: Support all basic integer types in node API
 - #4558: [CPP-API] Comment no longer causes crash
 - #4552: [Fuzzer] Issue #4152 - Remove ToString roundtrip in query verification
 - #4543: Fixing silent assertions
 - #4542: Check if database is still alive when trying to connect for nodejs
 - #4541: fix for issue 4533
 - #4539: Paralelization non-dependent on Arrow rows
 - #4524: Explicitly deleting default connection on js side
 - #4522: Correct architecture name for Linux aarch64
 - #4521: Adding correct substrait release tag to out-of-tree extension deployment
 - #4520: Added test cases for several fixed JDBC issues
 - #4516: Fix #4455, dont set default schema in transform
 - #4513: Issue 4502
 - #4510: [Casting] Varchar -> Decimal cast fix
 - #4507: [CSV] Fixed bug related to invalidated iterators
 - #4505: extension trigger event
 - #4504: fix: short-circuit hash and version discovery
 - #4496: [Fuzzer]  Issue #4152 - Force no cross-product issue
 - #4495: Build ODBC driver binary for OSX
 - #4494: [Fuzzer] Issue #4152 - Analyze inexisting column
 - #4493: Declare all variables for nodejs.
 - #4491: Issue #4419: Range Join Swizzling
 - #4488: Making the parquet extension loadable
 - #4484: fix: ignore status message from output of mypy stubs check
 - #4483: [Development bug] unittest result_helper.cpp triggers assertion
 - #4480: Remove REST server
 - #4479: Remove assertion
 - #4477: Removing Substrait From DuckDB Repo
 - #4474: WIP #4152
 - #4472: [Python] Removed mutable default parameters
 - #4470: Fix hidden merge conflict with fetchmany
 - #4465: [Python] `fetchmany` implemented
 - #4458: Issue #4454: VARCHAR/DATE Reversibility
 - #4448: Issue #3954: Pinned Heap Blocks
 - #4440: Added support for HUGEINT input type to BIT_COUNT scalar function
 - #4434: Python: Add PyRelation.fetchnumpy()
 - #4429: Allow indicating a format version that should be used to write/read from (De)serializer and use it for plans
 - #4427: Python: Improve docstrings for DuckDBPyRelation and DuckDBPyResult
 - #4418: Fix typo
 - #4416: Fix several update issues
 - #4413: Correctly schedule mix of union/child pipelines (again)
 - #4409: Increase timeout for coverage checks
 - #4405: Hybrid ART Leaf Part I
 - #4404: Add support for TS_MS, TS_NS, and TS_S
 - #4400: Issue #4388: DATE_TRUNC Low Precision
 - #4398: fix: correct object return types for arrow functions
 - #4395: Fix name of environment variable
 - #4390: Support UNION BY NAME set operation
 - #4383: Missing LISTs are NULL
 - #4382: Include PID in test directory name
 - #4380: R: Avoid `translate_duckdb()` in tests
 - #4377: R: Full BLOB support
 - #4372: Fix #4370: correctly handle non-flat vectors in list_sort
 - #4371: [Python] Changed all RuntimeErrors thrown in the Python client
 - #4368: Fixes issue #4365 - Not null constraint is no longer duplicated
 - #4364: Allow extra parameters in list_aggr to be passed in, as long as they are constant and only used during the bind
 - #4363: Fix for array_position with NaNs: use Equals::Operation instead of regular equality
 - #4362: Allow table functions to set cardinality stats through the C API - and utilize this in Julia DataFrame scans
 - #4359: Mark slow tests
 - #4355: Fix typo in exception text
 - #4354: R: Use preinstalled symbol
 - #4353: Shell: Add missing newline in help output
 - #4352: Tweak contributing guide [ci skip]
 - #4345: [Substrait] Pushing-down projections and filters to read relation
 - #4340: Correctly schedule pipeline dependencies when scheduling mix of UNION and FULL OUTER JOINs
 - #4336: feat: add basic json support to jdbc client
 - #4334: Bring ibis/substrait tests to a sane state
 - #4332: Fix Julia parallelism interleaving with the garbage collector, and expose Pending Query Result in C interface
 - #4328: Allow specifying a custom home directory using the SET home_directory option
 - #4327: [Aggregate] DISTINCT aggregates without GROUP BY are now executed in parallel
 - #4324: Fix #4309: fix for multiple foreign key constraints on the same table-table pair
 - #4323: Optimizer profiling
 - #4322: Print NOT operator correctly
 - #4319: feat: add missing node versions to CI
 - #4317: refactor: remove dead code in python client
 - #4316: R: Add rlang as suggested dependency
 - #4315: Column Data Collection, Arrow Result conversion rework, Cross Product performance fixes & more
 - #4312: R: Install tidy CLI tool
 - #4310: R: Add test for `test_all_types()`
 - #4304: Improve numeric hash function to a better but slightly slower hash function
 - #4301: Add unit of measurement in timer function
 - #4300: Support root type on expressions #4278
 - #4298: Feature/nodejs client docs
 - #4297: fix: remove nodejs test focus
 - #4296: Avoid infinite loop in range(NULL)
 - #4294: #4276 Serializing data types on table schema in substrait
 - #4289: [Python/Pandas] fix +/- inf wrongly converting to NaN (NULL)
 - #4288: Fix fuzzer issue w.r.t. NULL values in generate_series
 - #4286: [Python - Relation] CreateView on a filtered relation does not cause infinite loop anymore
 - #4285: chore: remove cython constraint now that bug is fixed
 - #4284: Pandas timezone
 - #4283: Return errors from RecordBatchReader
 - #4280: R: Remove nycflights13 dependency
 - #4279: R: Don't export duckdb_explain()
 - #4277: feat: update setup.py links
 - #4272: Allow 0 as a seed parameter
 - #4266: R: Only quote non-syntactic and reserved words
 - #4265: Specialize LIST aggregate function implementation
 - #4263: R: Avoid attaching package during tests
 - #4259: Add ANY_VALUE agg function
 - #4256: Schedule child pipeline correctly
 - #4255: Disable ibis substrait tests for now
 - #4250: C API: Report appender error in case conversion fails
 - #4240: DELIM_JOIN now propagate statistics correctly
 - #4237: fix: pin cython to work around bug
 - #4236: Integer types now correctly increase `width` of DECIMAL type.
 - #4235: Parquet writer: Write dictionary_page_offset, and distinct_count for dictionary encoded strings/enum
 - #4234: Implement json_merge_patch and jsonlines output mode
 - #4233: feat: fix pandas types in docstrings/python types
 - #4230: Handle nulls in structs and lists
 - #4225: Add Jaro Winkler
 - #4215: Use right template for smallint
 - #4213: feat: update instructions for installing master builds in bug report template
 - #4212: Improve error message
 - #4210: PARQUET: Move StringColumnWriter dictionary to use string_t to avoid allocations
 - #4209: Remove unused PhysicalTypes
 - #4207: Disable GC during Julia execution to avoid internal GC deadlock in DataFrame scan
 - #4206: Fix #4202: in the comparison simplification optimizer, we can only shift the cast to the constant if both casts are invertible
 - #4199: feat: Use pip to install and uninstall python client
 - #4198: [capi] impl clear bindings for prepared stmt
 - #4197: feat: port bug_report.md to bug_report.yml
 - #4196: Fix RTTI issue across extension boundaries on OSX
 - #4192: Correctly call SetFilePointerEx on Windows so the truncate works as expected
 - #4191: Fix Expanded CI test case by adding swap space to test
 - #4188: ALTER SEQUENCE IF EXISTS fix
 - #4187: [Storage] FOR compression
 - #4185: ISSUE #3248 Support for ALTER TABLE altering columns NOT NULL
 - #4183: Julia multi-threading fix: avoid using a time-out to cancel threads in case there are no tasks
 - #4179: node: add async-iterator-based streaming
 - #4175: [CI] Python Build with Sanitizer
 - #4172: Update stubs test
 - #4168: Issue #4161: Create WindowExecutor
 - #4167: node: report memory usage to the node GC
 - #4166: Fix #4165: correctly fill in false_sel when performing comparison with constant null value
 - #4160: node: don't crash on syntax errors
 - #4154: Making date_trunc statistics handling consistent with date_part
 - #4153: Support for int64 round trips in R driver using the bit64 package
 - #4151: Fix orrify merge conflict
 - #4143: Correctly handle query parameters in JDBC
 - #4140: CI Fixes
 - #4139: Remove redundant code
 - #4138: Support struct.* to retrieve all struct fields in SELECT list
 - #4134: Fuzzer Fixes
 - #4133: Remove DUCKDB_API for deletes. (For Windows/ZIG)
 - #4132: [Python] `project` now correctly inherits owning references to PyObjects
 - #4131: Missing error messages
 - #4125: Fix Orrify rename merge conflicts
 - #4124: [Substrait] [Python] [R] Upgrade Substrait and introduce function to export query plan as a substrait - JSON
 - #4117: (Hopefully) fix signing extension signing on master
 - #4112: PARQUET: Add data pages encodings to their metadata
 - #4111: Fix off-by-one in plan cost regression test script
 - #4110: Rename Orrify -> ToUnifiedFormat, VectorData -> UnifiedVectorFormat, Normalify -> Flatten
 - #4108: ODBC: fixing multicolumn parameter binding
 - #4107: Refactor: rename simple aggregate to ungrouped aggregate
 - #4104: Support Parquet's `RLE_DICTIONARY` encoding for string columns
 - #4103: Ntile fixes
 - #4101: Some follow up fixes for extension signing
 - #4096: Implement ANALYZE
 - #4093: Support ORDER BY and LIMIT in correlated subqueries, and add support for the ARRAY(subquery) syntax
 - #4090: Fix for non varchar input for sequence functions
 - #4088: Fix Issue #3813 - fixedsize PyArrow List -> DuckDB conversion
 - #4083: JDBC Change getTimestamp to throw an error for wrong data types
 - #4080: Several parser improvements
 - #4076: Unentangle Parquet ColumnWriter and StandardColumnWriterState
 - #4075: feat(breaking): improve python exceptions
 - #4070: [JDBC] CachedRowSet support
 - #4069: Improve error messages of extension install
 - #4068: Fix bug with PhysicalStreamingWindow
 - #4065: Better handling plus encoding in urls
 - #4061: Fix #3991: use case_insensitive_map for headers
 - #4060: Null handling unification
 - #4059: Prepared Statement Verification & many prepared statement fixes
 - #4058: nodejs: use less memory in each
 - #4057: Fixed an error in comment
 - #4053: [R] [CI] Run arrow test single threaded to avoid wrong fp comparison
 - #4050: Bump sqlite scanner version
 - #4049: Remove need for locks in TPC-H dbgen
 - #4048: Test query profiler shouldn't output profiling info to the console
 - #4045: Making delayload flags dependent on whether we are NOT doing a static…
 - #4044: Issue #3593: avoid duplicate eliminating correlated columns in subqueries when they involve LIST columns
 - #4039: Making memory leak sanitizer happy with DuckDB Shell
 - #4035: Fix several memory-allocation related issues - use Allocator in many places, and reduce many allocations all over
 - #4033: Plan cost regression tests
 - #4032: Add missing python test dependencies
 - #4031: Fix issue 3989
 - #4012: Fix amalgamated build with multiple .cpp
 - #4011: Fix amalgamation script when --splits is used
 - #4009: `EXPLAIN ANALYSE` should honor profiler output format
 - #4005: Fix for #3997
 - #4002: fix fts/httpfs include directories
 - #3999: Include guard renaming for amalgamation export
 - #3996: Fix for issue #3951
 - #3990: Substrait Interface in R API
 - #3988: feat: implement DuckDBConnection#getSchema for JDBC
 - #3985: Pandas->DuckDB Series of dtype='O' conversion
 - #3982: Expose dbgen text buffer size as a parameter and Python Replacement Scans Leak fix
 - #3978: Enhance bound parameters error message
 - #3977: Adding alias part 2
 - #3973: Using aggregate input data for aggregate functions
 - #3971: Issue #3079: When installed system RAM cannot be determined, default to no memory limit
 - #3967: Use fmt library for Value::ToString of float/double types
 - #3965: Fix #3942: avoid converting + to space in httplib::decode_url
 - #3964: Add support for DATEFORMAT and TIMESTAMPFORMAT to COPY TO
 - #3963: Atomic extension install: use UUID in temp file
 - #3961: Fix #3960: avoid returning an error when a blob contains a NULL character in duckdb_append_blob
 - #3958: Fix #3955: correctly compute width/scale when combining decimal type of different width/scale
 - #3957: [Java] Implement appender support for all? UTF-8 characters 😜
 - #3953: Fix missing LIST type in duckdb_types
 - #3952: Windows FileExists regression fix: need to use _wstati64 instead of _wstat64i32
 - #3950: Atomic extension installation
 - #3945: Fuzzer #55: Remove Normalify Call
 - #3939: Issue #3937: Casting infinite times
 - #3928: Adding alias type struct and map
 - #3927: Fix failing TPC-E test
 - #3925: New Julia package requires 0.4 of DuckDB_jll
 - #3921: Retire `LogicalTypeId::HASH` and replace it with `LogicalTypeId::UBIGINT`
 - #3919: ODBC: SingleExecuteStmt and error message
 - #3918: Julia compat version
 - #3917: Ignore invalid UTF8 in fuzzer scripts
 - #3916: Julia Guidelines fix
 - #3915: Add duckdb_extensions function
 - #3914: Expanding jdbc deploy script to be able to automatically release, too
 - #3912: Julia UUID and version bump
 - #3911: Making universal builds of OSX Extensions
 - #3910: Fix for export of current_time, current_timestamp, etc functions
 - #3909: More fuzzer fixes
 - #3903: Issue #3881: DATE_TRUNC statistics
 - #3900: Add newlines at EOF
 - #3897: feat: add extension load/install methods to python client
 - #3882: Uncompressed string improvements
 - #3868: Bump yyjson version
 - #3867: Enable exporting macro's
 - #3866: Add default for function NULL handling
 - #3864: [Python] Relation Explain
 - #3853: Feature/struct_insert function
 - #3814: Expose dbgen text buffer size as a parameter
 - #3694: List lambdas
 - #3618: Struct Types for Node.js UDFs
 - #3600: Issue  #1466: added `map_from_entries` function

---

# v0.4.0 - 0.4.0 Preview Release "Ferruginea" <a id="v040"></a>

*Released on 2022-06-20*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.4.0)

This preview release of DuckDB is named "Ferruginea" after the [Andean Duck](https://en.wikipedia.org/wiki/Andean_duck).

Binary builds are listed below. Feedback is very welcome.

Note: This release should be backwards-compatible wrt the on-disk storage format, but the next release may very well be incompatible again. So please don't rely on this just yet.  We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Also note: DuckDB is switching to [semantic versioning](https://semver.org). Version numbers look like this: `MAJOR.MINOR.PATCH` with changes to
 - MAJOR version when you make incompatible API changes,
 - MINOR version when you add functionality in a backwards compatible manner, and
 - PATCH version when you make backwards compatible bug fixes.

However, note that because `MAJOR` is currently 0, "Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable."


Below a list of changes in this release

## Major Changes & Features
 - #3767: Table function rework, parallel Julia DF scans & Python regression tests
 - #3749 & #3747: Query cancellation with CTRL-C for R and Python clients
 - #3700: Support Parallel Order-Preserving Result Set Materialization
 - #3696: Support WINDOW FILTER
 - #3620: HTTP read optimization
 - #3668: Adding alias type
 - #3435: Add support for reading newline-delimited JSON
 - #3783: Extension loading by statically linking DuckDB

## Minor Changes & Bug Fixes
 - #3905: Fix SQLancer CI
 - #3904: Fix #3896: correctly compute GroupRowsAvailable in struct reader in case a child-entry is not just a list, but a struct with only list entries
 - #3902: Fuzzer: fix sanitization of address sanitizer error
 - #3901: R: Extract DetectLogicalType() function
 - #3899: R: Check query return type instead of query type in dbFetch()
 - #3898: Issue #3880: Rebind DATE_TRUNC dates
 - #3894: Purge concurrent queue when enqueueing entries to prevent entries from piling up
 - #3892: Fix for issue #3878
 - #3889: Fix TreeRenderer crash on invalid UTF8
 - #3888: Julia Table Functions: add stack trace to errors reported
 - #3887: Correctly reset interrupted flag so verification does not overwrite original error
 - #3886: Remove the check_tread from python connection
 - #3879: Avoid title is too long error in fuzzer issue submission
 - #3877: Fix use-after-free in create view with prepared statement parameter
 - #3872: Glob with search paths
 - #3871: [Python] Making new connections to cursors and adding lock on queries over sampe connection
 - #3869: Several OSSFuzz fixes
 - #3865: Fix #3860: add support for creating foreign keys on temporary tables, and for now disable support for cross-schema foreign keys
 - #3863: Out-of-tree Extensions for Windows
 - #3862: Rework of Struct <> Dictionary Vectors, and add test_vector_types function
 - #3852: Added support for generated columns to TableCatalogEntry->ToSQL()
 - #3850: Enable EXTENSION_STATIC_BUILD for Mac too
 - #3849: [Python] Unbundle Substrait
 - #3848: Parquet: fix for fixed length byte arrays in dictionary column reader
 - #3847: Expand oss-fuzz tests to run queries and check for internal errors
 - #3846: Pass through read only flag for node connector
 - #3845: Add queries over Arrow to Python regression tests, and time entirety of TPC-H
 - #3843: [JDBC] Pass through scale and precision for decimal types from DuckDBColumnTypeMetaData
 - #3842: Allow to use custom memory allocator through DuckDB API on Windows
 - #3837: Fix overflow in generate_series and overflow in abs operator
 - #3832: Issue #3816: Parquet Time Zones
 - #3831: s3fs decode keys correctly
 - #3828: Update testthat snapshots
 - #3818: Add SQLancer to CI Fuzzing Framework
 - #3815: Out-of-tree Extension Builds
 - #3812: Fix several issues found by Valgrind
 - #3810: DuckDB.jl Julia Package History
 - #3809: Add `shell: bash` everywhere
 - #3802: fix ci breaking from extension PR
 - #3799: Optimisation rule for regexp_matches with literal pattern
 - #3798: Substrait: Adding more compatibility with Substrait and Ibis
 - #3792: Issue #3790: Temporal IsFinite/IsInf
 - #3791: Issue #3721: Rightshift Negative Hugeint
 - #3786: Fix binding of fully qualified view reference
 - #3785: Python: Allowing cursor to set check threads flag
 - #3784: Improve speed of ALTER TABLE ADD COLUMN
 - #3778: More node types
 - #3777: Python: Updating Stubs and Bringing Stubs tests back
 - #3776: Simplify `clangd` target
 - #3775: Expose dbgen speed_seed functions on header file and add missing ones
 - #3771: Increment R package version
 - #3765: Issue #3759: Node Time Zone
 - #3764: Issue #3763: List Min/Max Problems
 - #3761: Fix .import not creating missing table in CLI
 - #3760: Requiring keys provided to `map` to be unique
 - #3757: Fix #3756: fix issue when running blockwise NL join on dictionary vectors of structs
 - #3752: Fixed error handling for node exec()
 - #3751: Decreasing the overallocation for list aggregates
 - #3750: Fix a bug in HyperLogLog
 - #3746: Check if replacement scans don't leak memory
 - #3745: Arrow/Pandas Case Insensitive Columns
 - #3744: Treating ENUM Case in pyresult describe
 - #3739: DuckDBPyRelation: support `offset` argument for `limit()`
 - #3738: Fix #3730: avoid modifying the payload in-place in aggregate hash table, because it might be used multiple times in case of grouping sets
 - #3736: JDBC better error handling
 - #3733: Progress bar clean-up: fix thread sanitizer issue, and move progress bar code to individual operators
 - #3720: Issue #3515: Add statistical rounding
 - #3707: Fix #3702: avoid assertion that we are not storing internal entries in the file
 - #3706: Implement sqlite3_file_control and sqlite3_sleep
 - #3705: Add support for ENUM converted types in the Parquet reader
 - #3699: Zero-copy scans for non-list uncompressed segments
 - #3695: Only rename pandas columns that have duplicates
 - #3692: Compatibility with dev dbplyr
 - #3691: Fix #3690: correctly assign catalog set to default objects to avoid crash when used as dependency
 - #3681: R: Fail CI/CD on NOTEs, check examples on UBSAN, log valgrind output
 - #3677: Fuzzer fix: avoid reporting non-internal errors
 - #3676: More ccache removal from OSX Extension Release
 - #3675: More extensive SQLLogicTest testing, and temporarily disable OR pushdown
 - #3667: Handling dataframes with repeated names in columns outside the bind. Now when registering df for scan.
 - #3665: Delete correct revision in pypi cleanup script
 - #3664: try/except in pypi cleanup
 - #3663: Return PY registered objects from temporary views
 - #3662: Remove CCache from the OSX Extensions Release build
 - #3661: Automatic PyPI cleanup in CI
 - #3653: Fixing enum comparison at where clause to TRY_CAST
 - #3652: to issue#3475 optimize CSG & CMP enumeration of join order optimizer
 - #3650: Issue #3610 mem leak
 - #3648: Julia DataFrame Scan Performance Improvements & TPC-H Tests
 - #3646: ODBC: adjustments because of ADO
 - #3643: Fix for #3639, dont use string copy and value api to fill factor vector
 - #3635: Avoid running approx quantile with vsize=2
 - #3634: Fix some issues with the fuzzer auto-closing issue behavior
 - #3633: Add default type generator, move built-in types to default type class and improve error reporting for types
 - #3632: Check for div by zero in distinct stats
 - #3630: Fix issue 3611
 - #3629: S3 Minio fix
 - #3628: Issue #3625: Adding canonical guards around Arrow CData Interface
 - #3624: Add interval to DBAPI description
 - #3615: Fix #1785: correctly copy constraints in ADD COLUMN of alter table
 - #3614: Correctly propagate what a statement returns from the binder
 - #3613: SQLSmith fuzzer fixes
 - #3612: SQLite UDF fixes for writefile and friends
 - #3609: Fix operator precedence of ** in the parser
 - #3608: Turn the expression depth limit into a configureable parameter
 - #3607: Implements __enter__ and __exit__ functions on pyconnection to allow the use of context managers
 - #3606: Use Python 3 for configuring R
 - #3604: Equal or null optimization
 - #3603: Fixing ascii bug in histogram strings
 - #3602: Support for Arrow Timezone
 - #3598: Add auto-commit off to JDBC Connection
 - #3594: Issue #3588: Half constant BETWEEN
 - #3592: Issue #3444: Approximate quantile lists
 - #3589: Issue #1187: Virtual Generated Columns
 - #3576: More compliant with substrait and upgrading version up to 0.1.2
 - #3575: Issue #3534: Remove TIMESTAMPTZ casts
 - #3574: Issue #3430: Temporal Infinity Values
 - #3571: Fixing JNI, matching function signature exactly
 - #3569: Implicit struct_pack
 - #3564: Fix for #3562
 - #3551:  Issue #2309: Update benchmark info in README.
 - #3550: ICU Extension Rework: clangd for extensions
 - #3547: Issue #3273 support multistatments for JDBC driver
 - #3546: Issue #2910: Support pandas boolean datatype
 - #3533: Exit with the correct exit code in the regression test runner
 - #3531: Correctly increment list offset on histogram aggregation
 - #3528: Julia Client - re-enable parallelism by executing tasks on dedicated Julia threads
 - #3524: Rework table-in-out function API, and move Unnest table function to table-in-out function
 - #3523: Improve HyperLogLog
 - #3519: Support in-place updates for unsigned integers
 - #3516: Issue #3497: Round DECIMAL casts
 - #3514: Issue #3453: Window Partition Collections
 - #3512: Issue #3418: Match Multiple Spaces
 - #3511: Fix #3505: Correctly handle Foreign Key syntax for when primary-key columns are not specified
 - #3507: Fix merge conflicts
 - #3504: ODBC: issue #3398
 - #3503: ODBC: issue #3478
 - #3502: Random-value generation clean-up, and move aux data in client context to separate ClientData class
 - #3500: Bug fixes for ENUMs
 - #3498: Relational API basics for R client
 - #3495: R: support structs
 - #3481: List distinct and list unique functionality
 - #3474: Unified BufferedCSVReaderOptions parsing
 - #3470: Force aggregates to have a Combine method, expose bind data in combine & general bind data clean up
 - #3469: Add duckdb.lib to Windows release package
 - #3467: ODBC: PowerBI showing column headers
 - #3464: CSVReader option 'ignore_errors'
 - #3456: Add C API functions to build list/map types and read map types
 - #3454: CMake install DLL file on Windows platform
 - #3442: ICU Extension Rework: No longer use ICU amalgamation, and update ICU data to 71
 - #3437: Implement JNI class, method and field caching
 - #3420: Expose get table names from conn to python
 - #3416: R extension loading
 - #3410: Turn SQLSmith into an extension, add CI fuzzing framework, and add automatic SQL test case reduce functionality
 - #3405: Issue 3403: Logical Type Append
 - #3389: Issue #3187: Implement strptime_icu
 - #3388: CI: Use ccache and clang-tidy-cache
 - #3386: Issue #3384: DATE_TRUNC for INTERVAL
 - #3382: Fixing python dependency memory leaks
 - #3375: Rebind prepared statements in case of type ambiguities, rather than default to VARCHAR
 - #3346: list_sort function support

---

# v0.3.4 - 0.3.4 Bugfix Release <a id="v034"></a>

*Released on 2022-04-25*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.3.4)

This is a bug fix release that we need to create because uploading artefacts failed for the last one. Contents are the same as https://github.com/duckdb/duckdb/releases/tag/v0.3.3 plus some minor bug fixes.

Note: We are going to switch to a new versioning scheme, so the next proper release will be 0.4.0

---

# v0.3.3 - 0.3.3 Preview Release "Sansaniensis" <a id="v033"></a>

*Released on 2022-04-11*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.3.3)

This preview release of DuckDB is named "Sansaniensis" after the (regrettably extinct) [Chenoanas sansaniensis](https://books.google.nl/books?hl=en&lr=&id=jcEyAQAAMAAJ&oi=fnd&pg=PA1&ots=Yo7uqiwWjB&sig=jeAB2gFbhShF5AWmK1obw8FfYZk&redir_esc=y#v=onepage&q&f=false).

Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Below a list of changes in this release

## Major Changes & Features

 - #2926: DuckDB SQL backend for dbplyr
 - #2970: JSON extension
 - #2998: Support explicit aggregate state export, re-combination and finalisation
 - #3069: S3 writes and #3225: S3 file glob
 - #3092: Basic UDF support for Node API
 - #3109: Storage dictionary compression
 - #3111: Simple filtered aggregates
 - #3165: Add support for a `DESCRIBE` statement that gives a summary of all tables
 - #3178: 1-based indexing for lists and strings
 - #3195: Add support for `FOREIGN KEY`
 - #3253: Julia Client & C API Extensions
 - #3292: Support NaN and Infinity in floating point columns


## Minor Changes & Bug Fixes

 - #2954: JDBC enable usage of LocalDateTime via get/setObject
 - #2985: Issue #2590: Add overwrite flag to CSV copy, overwrite only if query completes
 - #3006: JDBC BigDecimal support
 - #3007: Feature: Add support for Excel text format (Update #2996)
 - #3010: R: Arrow timestamps in seconds, milliseconds and nanoseconds
 - #3027: Allow literal option for regex
 - #3030: Macros for floored division and modulo
 - #3034: Substrait Installable Extension
 - #3038: Issue #3037: DATE + TIME
 - #3045: fix for STRING_AGG(...) failing (vector type mismatch) assertion when used with DISTINCT and ORDER BY inside STRING_AGG.
 - #3050: R-pkg: cpp11-ify
 - #3051: Enable printing of EXPLAIN query trees in the R client
 - #3060: Issue #3056: Null list scatter
 - #3065: Implementation of list_contains
 - #3066: Report dlopen/dlsym errors in extension load
 - #3067: ODBC: Many changes
 - #3071: c-api: support decimal and prevent invalid type throws
 - #3072: Add CMake setting to disable linking of extensions
 - #3077: Issue 2498: Consistent NULL hashing
 - #3084: Hmb1 select macro feature mr
 - #3085: First batch of aggregation functions for python rapi
 - #3087: Fix incorrect link for testing docs
 - #3088: Add LIST_EXTRACT support for several missing types (including booleans)
 - #3090: Fix for Arrow Timezone CI Fail
 - #3093: Test/add parser error on missing newline
 - #3097: Fix remaining winsock error
 - #3098: Round-trippable Expression ToString()
 - #3101: Issue #3100: MAKE_DATE struct variant
 - #3102: Add flatten function for nested list
 - #3107: Allow multiple statements in the R-client
 - #3112: Issue #1423: PiecewiseMergeJoin multiple predicates
 - #3115: ODBC: SQLGetDescRec and SQLSetDescRec
 - #3116: NodeJS Windows CI Fix Attempt
 - #3120: Fix #3119: correctly perform case insensitive comparisons in default function/view/schema creation
 - #3121: Fix #3108: support ILIKE ESCAPE
 - #3123: Issue #3020: Unify column names of DESCRIBE and SUMMARIZE
 - #3124: Add Alias to projected columns
 - #3125: Adds support for the REPLACE keyword in CREATE TABLE AS ... SELECT (CTAS) statements
 - #3126: BLOB support for aggregate state combine
 - #3139: More Python Relational API Functions
 - #3142: Fix type hints for query_df
 - #3147: Python: Relation dependency on Connection
 - #3148: Alter Type of column from varchar to enum
 - #3151: Support trailing commas in many lists in the parser
 - #3154: JDBC - Bugfix - Negative timestamp fix
 - #3156: JDBC - Add timestamp with timezone support
 - #3158: Enable DISABLE_VPTR_SANITIZER by default on M1
 - #3161: Implementation of unnest(null), list_position, rewrites
 - #3162: Add support for list parameters in the Python API
 - #3163: ODBC: Diagnostic Feature
 - #3166: Move test_group_by_parallel out of the coverage tests
 - #3171: Fix #3169: verify that WAL exists in PRAGMA database_size
 - #3173: Adding chunk size parameter to functions that return arrow objects.
 - #3174: Correctly zero-initialize pg_parser allocation heap to prevent potential corruption in clean up of parser state of SQL strings
 - #3179: Change pipe so it doesnt print on terminal
 - #3180: Fix for build error of R package on Windows
 - #3190: Fix Python clean.sh: avoid deleting all locally installed libraries and instead only remove installed DuckDB libraries
 - #3191: Returning feature for INSERT
 - #3192: Tear down connections
 - #3196: linking fixes for extensions
 - #3197: Fix convert uuid to arrow str error
 - #3199: Dbplyr-backend SQL translation of is.na() must use only IS NULL
 - #3201: Enable universal builds for OSX
 - #3208: numeric md5 functions
 - #3209: JDBC - Fix missing metadata
 - #3213: Making the deliminator more flexible and Q 02/17/20 of TPC-H for Substrait
 - #3214: Extension linking fix
 - #3218: Fixed empty list aggregates
 - #3219: Issue #1423: IEJoin Implementation
 - #3220: Fix for #3200
 - #3221: FIX for parquet reader on diff files
 - #3224: feat: expose from_substrait in python package
 - #3226: ODBC: Windows setup
 - #3230: Fix for #3215
 - #3231: CodeCov apparently does not like target anymore, + validate codecov configuration in CI
 - #3232: Fix #3223: Prune trees with LIMIT 0
 - #3233: Fix #3205: implement skip for struct and list column readers
 - #3234: Fix #3222: avoid int overflow in RleBpDecoder
 - #3235: Removing std::binary_function because its deprecated in cpp11
 - #3238: Parquet globbing: Better support for schema evolution
 - #3239: Properly send mapped function on RAPI
 - #3244: Returning feature for update and delete statements
 - #3245: test: prevent master ci from being canceled
 - #3251: Improving CI performance
 - #3255: Adding check_same_thread option to py connector
 - #3256: ci: restructure to run format/tidy/codecov for python
 - #3263: JDBC - Enable useage of ENUM type
 - #3264: Allow the use of native replacement scan of parquet/csv files with the dbplyr-backend
 - #3266: Fix #3260: if a schema name is provided, pass along the schema name and table name to the replacement scan
 - #3268: Add python module constants from PEP249
 - #3270: python extension loading tests
 - #3274: Implementation of the list aggregate function
 - #3276: Properly resizing DuckDB batches that reference arrow batches
 - #3281: ODBC: LibreOffice on Linux
 - #3287: Several Julia API enhancements
 - #3289: ODBC: windows installer has to copy and pass program parameters
 - #3293: Issue #3262: Nested comparison fixes
 - #3295: Allow strftime arguments to be specified in both orders
 - #3299: [Arrow] Read Record Batch Reader and Scanners
 - #3301: Use FieldWriter/FieldReader in Checkpoint Manager
 - #3303: Add benchmark_runner based regression test, and remove random engine from cycle counter
 - #3305: Fix #3304: correctly trigger old result-set materialization prior in duckdb_value_is_null
 - #3307: Fix #3271: correctly check for negative limit and offset
 - #3308: Cleanup some unused include
 - #3311: Fix #3272: avoid incorrectly moving LIMIT to before the ORDER clause in certain cases
 - #3312: Issue #3290: Histogram Temporal Bindings
 - #3313: Issue #3275: Global Operator State
 - #3314: Issue #3262: Dead Code Removal
 - #3318: R bug-fixes: Pipes in tests and silence R NOTE
 - #3323: Fix #3291: delete root entries after a catalog entry is deleted and no more transactions can reference it
 - #3328: Fix #3294: initialize validity mask to correct size in placeholder code
 - #3329: Fix use after free bug in local storage
 - #3331: Add automatic issue labeler
 - #3335: #3324 Throw error instead of crashing when misusing prepared statements
 - #3338: Issue #3298: Nested Unflat MinMax
 - #3339: Add a create_value for strings to the Julia API
 - #3342: Issue #1423: IEJoin Performance Improvements
 - #3343: Issue #3118: Non-string Formats
 - #3355: Fix #3349: correctly handle empty table case in grouping set
 - #3356: Fix #3350: correctly update statistics after a SINGLE join, since SINGLE joins may introduce NULL values
 - #3357: Fix #3351: avoid double-binding functions in subqueries after an initial binding error
 - #3358: Fix #3352: fix several bugs with index selection for verifying foreign key constraints
 - #3359: Fix #3353: check if any results are returned in sqlite api wrapper before looking at the chunk
 - #3360: Fix #3354: add missing recursive CTE node traversal in correlated subquery flattening
 - #3362: ODBC: unixodbc_setup.sh
 - #3363: Fix #3361: correctly handle overflows in sequences with cycles
 - #3369: Fix #3367: correctly detect overflow in statistics propagation for ORDER BY
 - #3370: Fix #3366: check for invalid double values in progress bar
 - #3372: Fix #3365: correctly handle overflows in left-shifts
 - #3376: Fix Python Windows CI
 - #3378: Correctly handle rowid scans in Julia DataFrame scan (for COUNT(*))
 - #3380: ArgMinMax: correctly manage memory of strings in both values and arguments
 - #3381: Python extension loading
 - #3383: ODBC: unixodbc_setup.sh usage message
 - #3399: removed -k param for gzip
 - #3406: Install AWS CLI in CentOS Extension

---

# v0.3.2 - 0.3.2 Preview Release "Gibberifrons" <a id="v032"></a>

*Released on 2022-02-07*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.3.2)

This preview release of DuckDB is named "Gibberifrons" after the [Sunda teal](https://en.wikipedia.org/wiki/Sunda_teal)

Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Below a list of changes in this release

### Features
 - #2797: Add interface support for incremental/deferred query execution in main thread
 - #2682: Issue #561: Time Zone Support, #2703: #561: Time Zone Foundations
 - #2578: Enable support for multi-dot column references
 - #2613: Add support for EXPLAIN ANALYZE
 - #2569: Support installation of extensions from central repository
 - #2843: Parquet Writer: Support writing all types (test_all_types), and write column statistics, #2838: Add support for reading and writing the MAP type to the Parquet reader/writer, #2832: Parquet Writer Rework: Support complex types, #2597: Extend Parquet writer support for UNSIGNED types, various timestamp types, and correctly set converted types in more cases

### Minor Changes & Bug Fixes

- #3042: Issue #3029: Prevent CURRENT_QUERY folding
 - #3041: Fix #3017: detect recursive view construction and throw an appropriate error
 - #3040: Fix #3015: fix edge case issue with many null values in physical Top N
 - #3039: Update Java DuckDBAppender to allow appending null values - fixes issue 3035
 - #3028: Install covr from main development branch
 - #3026: Issue #2965: CTE parameter binding
 - #3024: Issue #3023: Simple filtered aggregates
 - #3021: Move install_extension test to test_slow
 - #3016: Issue #2923: Quote ENUM types
 - #3014: Issue #2908: UTF8 BOM Headers
 - #3013: Fix #3005: correctly normalify vector in array_slice
 - #3012: Fix #2999: Support ANY_JOIN in flattening correlated subqueries
 - #3011: Fix #2986: correctly copy old data over when calling repalloc in parser
 - #3004: Fix #2997: allow maximum CSV line size to be configurable
 - #3001: Document installation of dependencies in Python package README
 - #3000: Lookup parent frames for replacement scans
 - #2983: Fix #2975: fix off-by-one in transform of string constant to decimal in case of large negative numbers
 - #2982: Python API - allow duckdb.query to run arbitrary queries
 - #2980: Fix dead link in readme
 - #2979: Fixing Python CI
 - #2978: Ensure that users cant run concurrent queries using cursor()
 - #2974: Use cpp11 for rpkg
 - #2973: ODBC: SQLGetTypeInfo, SQLTables, and SQLColumns
 - #2971: Arrow use_async argument deprecation
 - #2969: FieldWriter/FieldReader for Backwards/Forwards Compatible Storage
 - #2963: Fixing parquet scan with or filters (issue #2955)
 - #2957: Fixing wrongful release of arrow arrays
 - #2956: fix: use selection vector to ensure ids are ordered
 - #2953: Fix cancellation configuration
 - #2952: Check coverage for R
 - #2951: Adding Cross Product Relation
 - #2949: Update copyright info to name DuckDB Foundation
 - #2946: Style R code
 - #2943: Disable arrow integration tests on Windows
 - #2941: Prefix inlined third party libraries with duckdb_
 - #2940: CMakeLists.txt: Add 'delayimp.lib' to delay-loaded DLL on MSVC
 - #2939: src/include/duckdb/common/assert.hpp: Added winapi
 - #2937: Install Python 3.7 from source on Ubuntu 16
 - #2935: adding the v to the amalgamation version string
 - #2930: list_slice test fix
 - #2925: Enable building the HTTPFS extension for both Windows and OSX
 - #2924: Add Node 17 to build factory
 - #2921: Fix for array_slice when end index is out of bounds
 - #2920: ODBC: cursor functions
 - #2919: Preserve Identifier Case by default, rather than lower-casing all unquoted identifiers
 - #2918: Add left join type to python relational API
 - #2917: list_slice alias for array_slice
 - #2912: Fixing Arrow Stream Output Error
 - #2906: not export deletes to allow crosscompile
 - #2905: Use difftime_str instead of hms class
 - #2904: Use correct hms value
 - #2903: Robust cancellation via concurrency
 - #2901: Minor tweaks in R code
 - #2899: Support for GROUP BY ALL/ORDER BY ALL
 - #2895: Add duckdb_keywords function
 - #2894: OSS Fuzz Fixes
 - #2890: ODBC driver assets
 - #2888: Add JDBC's setTimestamp method
 - #2886: Use double to store scale factor in TPC-H answers
 - #2885: Better support for Parquet 2 Page Layout
 - #2880: fix python profile html generator to support updated JSON format.
 - #2871: Issue #1423: Refactor PiecewiseMergeJoin
 - #2870: bug fix for order by header
 - #2869: Value Rework: Make all members private and use accessors
 - #2867: test: fixed typo for decimal type in test_all_types
 - #2865: Issue #2782: Non-Gregorian Calendars
 - #2864: C API: Deprecate direct access into duckdb_result and duckdb_column structs
 - #2863: ODBC: conformance core level of SQLAllocHandle, SQLFreeStmt, SQLGetDiagRec, SQLSetStmtAttr, and descriptors
 - #2856: Issue #2842: Implement make_date/time/timestamp
 - #2855: right case for winsock2.h
 - #2854: Issue #2831: Disable WINDOW FILTER
 - #2852: Issue #2827: Postgres datepart compatibility
 - #2851: When using Replace, keep the alias of the original column
 - #2850: Avoid reading past the end of the string when parsing a time as part of an interval
 - #2848: Fix #2847: Write parquet files to test dir
 - #2846: Issue #2780: Remove DATETZ type
 - #2845: Turn FileSync into a nop in the PipeFileSystem, and add clear error message when ParquetReader is used to read from a FIFO stream (e.g. /dev/stdin)
 - #2844: Support read_csv_auto from /dev/stdin
 - #2837: Fix potential use after move detected by linter, and add DISABLE_DUCKDB_REMOTE_INSTALL define
 - #2835: Issue #2834: ICU BindAdapterData::Equals
 - #2833: CI Fixes, TSAN Fix
 - #2830: Fix #2828: setup.py BUILD_HTTPFS does not work
 - #2825: Fix #2823: Correctly alter cardinality estimation in LIMIT/SAMPLE clauses
 - #2822: Issue #2779: DATE_PART structs
 - #2819: add `INTERVAL` support to node.js
 - #2818: Adding Parquet extension to node module
 - #2817: R: Make method definition more similar to S3
 - #2808: Revert stack-overflow detection back to having a maximum (expression) depth in the transformer
 - #2807: Add discord badge
 - #2806: Refactor SQLLogicTest
 - #2802: R-Dataset: Add flag to enable async scanner
 - #2801: Add support for list equivalent of range/generate_series with timestamp+interval
 - #2800: Fix #2749: avoid copying subquery in BETWEEN expressions
 - #2799: Fix #2791: allocate data and mask locations to correctly handle counts > vector_size in the row_gather
 - #2798: Fix issue in perfect hash join when (max - min) does not fit into an INT64
 - #2796: Addition of QUALIFY clause
 - #2794: Add Extension Install CI tests, and fix various issues found through this process
  - #2793: Enum Functions
 - #2792: PhysicalStreamingWindow operator
 - #2788: Issue #2778: Missing date parts
 - #2784: adds `BOOLEAN` support to node.js bindings
 - #2773: Fix #2761: correctly check that stderr is pointing to a terminal
 - #2770: Fix a bug in the sqlite3_api_wrapper that resulted in not correctly reporting why a database could not be opened
 - #2767: Issue #561: Implement ICU AGE
 - #2765: Add Connection::GetTableNames method to C++ API that allows you to extract the required table names from a query
 - #2760: Issue #561: Implement ICU DATEDIFF
 - #2759: Fix string constructor usage
 - #2757: Extension dashes to underscores
 - #2756: Issue #561: Implement ICU DATESUB
 - #2753: Python - Test All Types
 - #2751: Fix #2750: check enable_external_access flag in more locations
 - #2748: Cleanup pointer swizzling code
 - #2746: Fix #2745: correctly detect when a RECURSIVE CTE does not contain a reference to itself (i.e. is not a recursive CTE at all)
 - #2744: C++17 warning fixes, plus CI tests for compiling (parquet) amalgamation with C++17
 - #2742: Common: typo and remove unused files
 - #2739: Add test_all_types function
 - #2738: GH Actions: avoid upload on master, and try to fix codecov failures on master
 - #2737: Typo: Rename Alises to Aliases
 - #2732: Tests for Python  + #1732
 - #2731: Pushing down OR filters
 - #2730: Issue #561: ICU Date addition
 - #2729: Add duckdb_functions table function
 - #2727: RAII for SortedBlock
 - #2725: Windows: Remove OVERLAPPED IO flag, it is not required and seems to cause concurrency problems
 - #2723: Fix #2471: correctly handle offset passed by ::UpdateSegment, and handle it earlier to clean up code
 - #2722: Infer COPY TO format from file extension
 - #2721: Update of PERCENT keyword in the LIMIT clause(#2671)
 - #2719: Fix #2713: correctly bind multi-part column references in correlated subqueries
 - #2718: Add "position" as an alias to the "instr" function
 - #2712: Use and_kleene for Arrow filters
 - #2711: Fix CSE optimizer: keep around expressions as they might be referenced in the expression_map
 - #2710: Modify LEAST/GREATEST to ignore NULL values
 - #2708: Fix #2701: Handle VALUES lists in correlated subqueries
 - #2706: Ignore cancel request on master
 - #2702: Rename snappy namespace to duckdb_snappy, and enable Parquet extension for the exported symbol checker
 - #2697: Support reading of ZSTD files, and add support for writing GZIP and ZSTD files
 - #2696: FetchDF for nested types (Lists, Maps and Structs)
 - #2693: Fix #2663: correctly implement EXTRACT(EPOCH from TIME) as seconds since midnight
 - #2692: Fix #2678: Fix undefined behavior for sequences close to INT64 min/INT64 max
 - #2691: Correctly handle synchronous I/O being returned from Windows API
 - #2690: Use templated memcpy/memcmp more
 - #2689: Reduce memory footprint of Python/R compilation by default by disabling unity builds unless DUCKDB_BUILD_UNITY flag is enabled
 - #2686: Fix #2685: prevent CSE optimizer from causing short-circuiting issues, and add disable_optimizers setting
 - #2684: Python 3.10 builds
 - #2681: Benchmark/test format cleanup
 - #2679: Bitpacking storage compression
 - #2673: remove extra semicolon.
 - #2665: Merge arrow_register into register function
 - #2662: Fix #2656: correctly transform DISTINCT with ORDER BY into DISTINCT ON
 - #2660: Issue #2614: Wide windows
 - #2659: Fix #2652: Make struct fields case insensitive
 - #2658: Fix various Windows unicode issues
 - #2657: Initializing matchers to avoid valgrind complaints
 - #2655: Add templated memcpy/memcmp
 - #2650: Fix bug in parquet reader causing list columns to be parsed incorrectly (#2557)
 - #2648: Fix #686: remove hard-coded memory limit in parser and fix error message propagation from exceptions thrown in parser
 - #2644: Fix #2641: correctly handle tab delimiters in COPY TO/FROM
 - #2642: Issue #2552: SUBSTR BIGINT
 - #2639: Fix #2586: correct semantics for extract(second, ...) from intervals
 - #2636: Hashing enum values (Enum comparison bug fix)
 - #2635: Fix for R factor scans
 - #2631: ODBC: Refactoring Parameter Descriptor
 - #2630: Try to Cast Enums to other types
 - #2626: Escape column names in dbWriteTable() Fixes #2622
 - #2623: Fix #2612: Correctly check that default is set on copy of SetDefaultInfo
 - #2611: Multithreaded Python
 - #2609: Configuration Rework & Cleanup
 - #2602: Adding pragma option for parquet binary as string
 - #2583: Issue #2549: Support IGNORE NULLS
 - #2576: Add generate_subscripts macro
 - #2526: Sequence ownership

---

# v0.3.1 - 0.3.1 Preview Release "Spectabilis" <a id="v031"></a>

*Released on 2021-11-16*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.3.1)

This preview release of DuckDB is named "Spectabilis" after the [King Eider](https://en.wikipedia.org/wiki/King_eider)

Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Below a list of changes in this release

**Features**
 - #2393: Switch to Push-Based Execution Model
 - #2417: Add support for GROUPING SETS, ROLLUP, CUBE and GROUPING/GROUPING_ID
 - #2347: Support for ENUM Types & #2404: Native mapping between R factors and DuckDB ENUMs
 - #2419: Allow WHERE clause referring aliases defined in SELECT clause
 - #2473: Adding Compression Option for Column Definitions to SQL Parser
 - #2489: Implement MAD (Moving Absolute Deviation) Aggregate
 - #2520: Add LIST_CONCAT and LIST_APPEND functions
 - #2522: MSD (Most Significant Digit) Radix Sort
 - #2529: Implement REGEXP_EXTRACT
 - #2482: Add support for EVEN
 - #2555: Adding BINARY_AS_STRING parameter to the parquet scan

**Minor Changes & Bug Fixes**
 - #2377: Fix current_schema() and current_schemas()
 - #2380: Add tests for "did you mean" error message
 - #2381: Let FTS index creation respect the current schema.
 - #2382: Dropping support to Python 2
 - #2385: BLOB support for JDBC
 - #2389: Replace __getattr__ on PyBind11 classes with individual properties.
 - #2390: Moving big categorical tests to tests_slow folder
 - #2394: Add SET s3_endpoint support for in-house Ceph
 - #2397: Add Python .pyi stubs
 - #2402: GH Actions Upload: retry asset upload with timeout
 - #2403: Not altering original DF when renaming columns in the binder
 - #2405: Fix bug with enum::varchar cast on null values
 - #2408: Rewrite Arrow table register for R using replacement scans
 - #2409: Adding dependency on Enum Types -> Tables
 - #2412: Updated src readme to state we use push-based execution.
 - #2413: Fix for #2411
 - #2421: Fix #2407: use correct template parameters for DATE in arg_min/arg_max
 - #2423: Fix #2416: fix binding issues related to binding parameters, null values, etc in list_extract and array_length
 - #2424: Issue #2388: QUANTILE_DISC for VARCHAR
 - #2430: Fix for #2426
 - #2431: More fixes for #2416
 - #2434: Issue #2388: Moving VARCHAR QUANTILE_DISC
 - #2437: implement GEN_RANDOM_UUID
 - #2438: Issue #2432: PERCENTILE_XXXX ignores DESC
 - #2439: fix: pass absolute path to `System.load()` in Java
 - #2444: Fix #2440: correctly report run-time errors in Python client
 - #2445: Several OSS Fuzz Fixes
 - #2448: Move to codecov v2, and use add_library for vector operations for low RAM machines
 - #2449: Enum to Enum Comparisons
 - #2451: Hooold the loooock for Python Strings under Dataframe Object Columns
 - #2453: Fix when getting single values from ENUMs
 - #2455: Doc Improve: Trying to Update doc in `QueryResult`
 - #2456: Add --test-dir parameter to unittest so we can test out-of-tree extensions with it
 - #2462: Fix #2452: Implement Coalesce instead of rewriting to CASE chain
 - #2463: More OSS Fuzz fixes
 - #2474: Allow Fetch of chunks containing a  multiple of vector sizes for the Arrow Record Batch Reader
 - #2476: Really holding the lock this time
 - #2477: Sorted aggregate: only re-order when ordering count > 0
 - #2485: Benchmarks: Handle comparisons for values that do not have a VARCHAR ->TYPE cast (e.g. complex/list types)
 - #2487: Conditionally define UNLIKELY in Thrift
 - #2488: ODBC: fetching the first chunk in SQLExecute
 - #2490: Clean up RadixSort code
 - #2491: These tests are now passing with arrow 6
 - #2494: Emit full vectors from VALUES lists instead of emitting individual tuples
 - #2497: Upgrade Catch to v2.13.7
 - #2500: Fix nested string order
 - #2501: Add CIFuzz action
 - #2503: Fix for py string conversion on large strings
 - #2504: More precision for `SUM` and `AVG`
 - #2517: Move Kahan sum to separate method (fsum, sum_kahan)
 - #2521: Issue #2515: Windowed quantile list
 - #2527: testing: Add oss-fuzz fuzzer
 - #2536: Fix #2518: in read_csv_auto don't override names if names have been provided
 - #2537: Fix #2531: in recursive CTE avoid waiting for events to finish if an event has thrown an error
 - #2539: Restructuring CI Workflow
 - #2542: Issue #2530: Reset windowed lists
 - #2550: ODBC: Running PSQLODBC tests on Win64
 - #2556: Fixed directory separator bug
 - #2558: Fixing positional reference binding in ORDER BY  clause
 - #2559: Issue #2552: General ordered aggregates
 - #2561: Fix master CI: Python workflow needs auth tokens for deployment
 - #2563: Move ExtensionHelper into main DuckDB Class
 - #2564: R Client: Moving UTF encoding to R to avoid multithreading issues
 - #2567: Fix #2538: crash in CSV auto-detect when reading ZSTD data
 - #2573: Move HTTPFS builds to separate test to avoid deploying them by default on Linux
 - #2574: Naming optimizer-created aggregates so plans are interpretable
 - #2579: Support to Arrow 6
 - #2580: Check magic bytes before checksum when opening a DuckDB database file
 - #2585: Fix #2584: correctly handle edge cases for bigger than 1 increments in range table function
 - #2587: Replacement Scans for Arrow Objects
 - #2592: Fix #2577: Rework case statement to avoid rewrite into nested binary cases
 - #2593: Fix #2591: avoid using ungrouped aggregate for non-combineable aggregates
 - #2594: Fix #2588: timestamp -> date cast is not invertible
 - #2595: Fix #2543: case insensitive replacement scans
 - #2598: OSS Fuzz Fixes
 - #2603: The asset upload script for releases was broken somehow
 - #2605: Clean up reupload by splitting it into two functions
 - #2604: Fix #2599: maintain correct dependencies between UNION ALL nodes so that output is deterministic/in-line with what a sequential execution would produce

---

# v0.3.0 - 0.3.0 Preview Release "Gracilis" <a id="v030"></a>

*Released on 2021-10-06*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.3.0)

This preview release of DuckDB is named "Gracilis" after the [Grey Teal](https://en.wikipedia.org/wiki/Grey_teal)

Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

This release contains a novel join method, the  #1959: Perfect Hash Join. Otherwise there are many improvements and bug fixes however, a list is below:

 - #2377: Fix current_schema() and current_schemas()
 - #2371: Installing pandoc so R pkg can be fully checked
 - #2369: More CI fixes
 - #2361: ODBC: First version Winsetup
 - #2360: Issue #2348: Support bankers rounding as default function
 - #2359: Implement UUID data type
 - #2358: Fixes minor flag comment
 - #2357: Issue #2351: Ordered aggregate transformation
 - #2356: Issue #2286: Numeric SUMMARIZE stats
 - #2353: Get rid of a couple of Clang warnings.
 - #2346: Avoid re-using RE2 regex between threads, since RE2 regex objects have locks internally
 - #2328: CI Fixes
 - #2321: Issue #1998: Exact Timestamp Subtraction
 - #2320: Change SET's default scope from GLOBAL to (PG-compatible) SESSION.
 - #2319: Fix #2315: correctly detect that index joins cannot be used for multi-column indexes, and clean up TPC-DS extension
 - #2318: Remove extra semicolon.
 - #2317: Support SET SCHEMA and SET SEARCH_PATH
 - #2316: Fix for #2304
 - #2314: Fix #2313: No Out of Range Error in Index Benchmark
 - #2311: Issue #2310: Create Index Benchmark
 - #2306: Windows (64 bits) and -DDISABLE_UNITY=1
 - #2302: Fix #2301: ART Leaf Node shrink
 - #2300: Fix #2293: Correctly escape all special characters (quotes, newlines, tabs, etc) in JSON output of query profiler
 - #2299: Fix #2296: Avoid requesting O_RDWR permissions when we only need O_WRONLY so we can write to FIFO streams
 - #2298: Fix #2294: In CSV reader correctly generate column names with many columns
 - #2297: Issue #2241: Transacted Index Reinsert
 - #2290: Fix #2289: align default continue prompt
 - #2287: ODBC: list catalog, schema and test_blob
 - #2284: Make S3 credentials session scoped
 - #2282: Fix for bug #2281
 - #2280: Initial support to read lists from R client
 - #2279: Fix #2277: add support for lists of structs to LIST_EXTRACT
 - #2276: Add support for EXCLUDE and REPLACE clauses
 - #2275: Run only CRAN tests for valgrind
 - #2274: Fix #2267: For structs, get the required amount of rows from a non-list child if there is one
 - #2272: Rename force_parallelism to verify_parallelism
 - #2271: Make regression run parallel with 2 Threads
 - #2266: A refactoring around FileSystem
 - #2265: Allow optional extensions when building the R package
 - #2263: Regression Test: TPC-DS/H20AI and other adjustments
 - #2262: Fix #2261: add support for filters pushed down into decimal columns in Parquet files
 - #2259: Fix a TSAN error for test/sql/window/test_partition_flushing.test
 - #2255: Make sorting even faster
 - #2254: More descriptive out-of-memory error when db is launched in-memory
 - #2253: Regression Tests
 - #2251: Changes from CRAN 0.2.9 release
 - #2234: Add support for S3 session token (STS)
 - #2228: Date functions on Windows

---

# v0.2.9 - 0.2.9 Preview Release "Platyrhynchos" <a id="v029"></a>

*Released on 2021-09-06*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.9)

This preview release of DuckDB is named "Platyrhynchos" after the very well-known [Mallard](https://en.wikipedia.org/wiki/Mallard), πλατυρυγχος meaning "broad-billed".

Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Major changes (not listing minor bug fixes and small changes):

Storage
 - #2099: **Persistent Storage Compression Framework** & RLE compression for numeric columns
 - #2157: Multi-Occupancy Blocks in the Storage


SQL
 - #2247: Support session and global `SET` statement variable scopes.
 - #2230: Full Case Insensitivity in the Binder & Catalog
 - #2208: Allow duplicate column names in subqueries/`CREATE TABLE AS`, similar to SQLite
 - #2206: Allow unnamed subqueries
 - #2189: Add support for `SUMMARIZE` of SQL statement/table
 - #2158: `ORDER BY` aggregates
 - #2171: Implement `LAST`
 - #2146: Support for `RANGE` and `ARRAY_LENGTH` scalar functions
 - #2133: Implement `DATESUB` & #2090: Implement `DATEDIFF`
 - #2128: Fall back to VARCHAR when the type of a prepared statement parameter is ambiguous

Performance Improvements
 - #2226: Issue #1657: Reduce Window copying
 - #2221: Prefetch Parquet Meta Data
 - #2172: Top-N Rework using new sort code
 - #2167: Use new sort code in window functions
 - #2098: Reduce unnecessary sorting overhead
 - #2077: Fetch Arrow - Streaming

C Client:
 - #2173: Don't strdup error msg
 - #2115: Improve performance of duckdb_value functions, add support for HUGEINT type and add extra result helper functions
 - #2107: CAPI Cleanup & DATE/TIME/TIMESTAMP rework

R Client
 - #2250: Support column subsets in dbAppendTable()
 - #2134: Implement dbAppendTable()
 - #2136: Implement dbBind() according to specification
 - #2119: Enable more DBItest tests

ODBC Client
 - #2184: Enabling pyodbc & #2124: Enable nanodbc & #2159: Making the R odbc package work with our ODBC driver
 - #2169: Supporting SQLPutData, SQLParamData, SQLMoreResults &  - #2096: SQLFetchScroll and SQLGetPrivateProfileString
 - #2236: Windows x64 Support

---

# v0.2.8 - 0.2.8 Preview Release "Ceruttii" <a id="v028"></a>

*Released on 2021-08-02*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.8)

This preview release of DuckDB is named "Ceruttii" after a [long-extinct relative of the present-day Harleqin Duck](https://en.wikipedia.org/wiki/Harlequin_duck#Taxonomy) (Histrionicus Ceruttii).
Binary builds are listed below. Feedback is very welcome.

Note: Again, this release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

### SQL

 - #2064: `RANGE`/`GENERATE_SERIES` for timestamp + interval
 - #1905: Add `PARQUET_METADATA` and `PARQUET_SCHEMA` functions
 - #2059, #1995, #2020 & #1960: Window `RANGE` framing, `NTH_VALUE` and other improvements

### APIs

 - [Many Arrow integration improvements](https://github.com/duckdb/duckdb/pulls?q=is%3Apr+is%3Aclosed+arrow)
 - [Many ODBC driver improvements](https://github.com/duckdb/duckdb/pulls?q=is%3Apr+is%3Aclosed+odbc)
 - #1815: Initial version: SQLite UDF API
 - #2001: Support DBConfig in C API

### Engine

 - #1975, #1876 & #2009: Unified row layout for sorting, aggregate & joins
 - #1930 & #1904: List Storage
 - #2050: CSV Reader/Casting Framework Refactor & add support for `TRY_CAST`
 - #1950: Add Constant Segment Compression to Storage
 - #1957: Add pipe/stream file system

---

# v0.2.7 - 0.2.7 Preview Release "Mollissima" <a id="v027"></a>

*Released on 2021-06-14*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.7)

This preview release of DuckDB is named "Mollissima" after the Common Eider (Somateria mollissima).
 Binary builds are listed below. Feedback is very welcome.

Note: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the documentation for details.

Major changes:

SQL
 - #1847: Unify catalog access functions, and provide views for common PostgreSQL catalog functions
 - #1822: Python/JSON-Style Struct & List Syntax
 - #1862: #1584 Implementing `NEXTAFTER` for float and double
 - #1860: `FIRST` implementation for nested types
 - #1858: `UNNEST` table function & array syntax in parser
 - #1761: Issue #1746: Moving `QUANTILE`

APIs

 - #1852, #1840, #1831, #1819 and #1779: Improvements to Arrow Integration
 - #1843: First iteration of ODBC driver
 - #1832: Add visualizer extension
 - #1803: Converting Nested Types to native python
 - #1773: Add support for key/value style configuration, and expose this in the Python API

Engine
 - #1808: Row-Group Based Storage
 - #1842: Add (Persistent) Struct Storage Support
 - #1859: Read and write atomically with offsets
 - #1851: Internal Type Rework
 - #1845: Nested join payloads
 - #1813: Aggregate Row Layout
 - #1836: Join Row Layout
 - #1804: Use Allocator class in buffer manager and add a test for a custom allocator usage

---

# v0.2.6 - 0.2.6 Preview Release "Jamaicensis" <a id="v026"></a>

*Released on 2021-05-08*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.6)

This preview release of DuckDB is named "Jamaicensis" after the [blue-billed Ruddy Duck (Oxyura jamaicensis)](https://en.wikipedia.org/wiki/Ruddy_duck). Binary builds are listed below. Feedback is very welcome.

Note: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the documentation for details.

Also note: Due to changes in the internal storage (#1530), databases created with this release wil require somewhat more disk space. This is transient as we are working hard to finalise the on-disk storage format.

Major changes:

Engine
 - #1666: External merge sort, #1580: Parallel scan of ordered result and #1561: Rework physical ORDER BY
 - #1520 & #1574: Window function computation parallelism
 - #1540: Add table functions that take a subquery parameter
 - #1533: Using vectors, instead of column chunks as lists
 - #1530: Store null values separate from main data in a Validity Segment

SQL
 - #1568: Positional Reference Operator `#1` etc.
 - #1671: `QUANTILE` variants and #1685: Temporal quantiles
 - #1695: New Timestamp Types `TIMESTAMP_NS`, `TIMESTAMP_MS` and `TIMESTAMP_NS`
 - #1647: Add support for UTC offset timestamp parsing to regular timestamp conversion
 - #1659: Add support for `USING` keyword in `DELETE` statement
 - #1638, #1663, #1621 & #1484: Many changes arount `ARRAY` syntax
 - #1610: Add support for `CURRVAL`
 - #1544: Add `SKIP` as an option to `READ_CSV` and `COPY`

APIs
 - #1525: Add loadable extensions support
 - #1711: Parallel Arrow Scans
 - #1569: Map-style UDFs for Python API
 - #1534: Extensible Replacement Scans & Automatic Pandas Scans and #1487: Automatically use parquet or CSV scan when using a table name that ends in `.parquet` or `.csv`
 - #1649: Add a QueryRelation object that can be used to convert a query directly into a relation object, #1665: Adding from_query to python api
 - #1550: Shell: Add support for Ctrl + arrow keys to linenoise, and make Ctrl+C terminate the current query instead of the process
 - #1514: Using `ALTREP` to speed up string column transfer to R
 - #1502: R: implementation of Rstudio connection-contract tab

---

# v0.2.5 - 0.2.5 Preview Release "Falcata" <a id="v025"></a>

*Released on 2021-03-10*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.5)

This preview release of DuckDB is named "Falcata" after the Falcated Duck (Mareca falcata). Binary builds are listed below. Feedback is very welcome.

Note: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the documentation for details.

Major Changes:

Engine
 - #1356: **Incremental Checkpointing**
 - #1422: Optimize Top N Implementation

SQL
 - #1406, #1372, #1387: Many, many new aggregate functions
 - #1460: `QUANTILE` aggregate variant that takes a list of quantiles &  #1346: Approximate Quantiles
 - #1461: `JACCARD`, #1441 `LEVENSHTEIN` & `HAMMING` distance  scalar function
 - #1370: `FACTORIAL` scalar function and ! postfix operator
 - #1363: `IS (NOT) DISTINCT FROM`
 - #1385: `LIST_EXTRACT` to get a single element from a list
 - #1361: Aliases in the `HAVING` clause (fixes issue #1358)
 - #1355: Limit clause with non constant values

APIs:
 - #1430 & #1424: **DuckDB WASM builds**
 - #1419: Exporting the appender api to C
 - #1408: Add blob support to C API
 - #1432,  #1459 & #1456: Progress Bar
 - #1440: Detailed profiler.

---

# v0.2.4 - 0.2.4 Preview Release "Jubata" <a id="v024"></a>

*Released on 2021-02-02*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.4)

This preview release of DuckDB is named "Jubata" after the [Australian Wood Duck](https://en.wikipedia.org/wiki/Australian_wood_duck) (Chenonetta jubata). Binary builds are listed below. Feedback is very welcome.

Note: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the documentation for details.

Major changes:
SQL
 - #1231: Full Text Search extension
 - #1309: Filter Clause for Aggregates
 - #1195: `SAMPLE` Operator
 - #1244: `SHOW` select queries
 - #1301: `CHR` and `ASCII` functions & #1252: Add `GAMMA` and `LGAMMA` functions

Engine
 - #1211: (Mostly) Lock-Free Buffer Manager
 - #1325: Unsigned Integer Types Support
 - #1229: Filter Pull Up Optimizer
 - #1296: Optimizer that removes redundant `DELIM_GET` and `DELIM_JOIN` operators
 - #1219: `DATE`, `TIME` and `TIMESTAMP` rework: move to epoch format & microsecond support

Clients
 - #1287 and #1275: Improving JDBC compatibility
 - #1260: Rework client API and prepared statements, and improve DuckDB -> Pandas conversion
 - #1230: Add support for parallel scanning of pandas data frames
 - #1256: JNI appender
 - #1209: Write shell history to file when added to allow crash recovery, and fix crash when .importing file with invalid
 - #1204: Add support for blobs to the R API and #1202: Add blob support to the python api

Parquet
 - #1314: Refactor and nested types support for Parquet Reader

---

# v0.2.3 - 0.2.3 Preview Release "Serrator" <a id="v023"></a>

*Released on 2020-12-03*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.3)

This preview release of DuckDB is named "Serrator" after the Red-breasted merganser (Mergus serrator). Binary builds are listed below. Feedback is very welcome.

Note: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the EXPORT DATABASE command with the old version followed by IMPORT DATABASE with the new version to migrate your data. See the documentation for details.

Major changes:

SQL:
 - #1179: Interval Cleanup & Extended `INTERVAL` Syntax
 - #1147: Add exact `MEDIAN` and `QUANTILE` functions
 - #1129: Support scalar functions with `CREATE FUNCTION`
 - #1137: Add support for (`NOT`) `ILIKE`, and optimize certain types of `LIKE` expressions

Engine
 - #1160: Perfect Aggregate Hash Tables
 - #1133: Statistics Rework & Statistics Propagation
 - #1144: Common Aggregate Optimizer, #1143: CSE Optimizer and #1135: Optimizing expressions in grouping keys
 - #1138: Use predication in filters
 - #1071: Removing string null termination requirement

Clients
 - #1112: Add DuckDB node.js API
 - #1168: Add support for Pandas category types
 - #1181: Extend DuckDB::LibraryVersion() to output dev version in format `0.2.3-devXXX` & #1176: Python binding: Add module attributes for introspecting DuckDB version

Parquet Reader:
 - #1183: Filter pushdown for Parquet reader
 - #1167: Exporting Parquet statistics to DuckDB
 - #1162: Add support for compression codec in Parquet writer &  #1163: Add ZSTD Compression Code and add ZSTD codec as option for Parquet export
 - #1103: Add object cache and Parquet metadata cache

---

# v0.2.2 - 0.2.2 Preview Release "Clypeata" <a id="v022"></a>

*Released on 2020-11-01*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.2)

This is a preview release of DuckDB.
Starting from this release, releases get named as well. Names are chosen from species of ducks (of course). We start with "Clypeata".

*Note*: This release introduces a backwards-incompatible change to the on-disk storage format. We suggest you use the `EXPORT DATABASE` command with the old version followed by `IMPORT DATABASE` with the new version to migrate your data. See the [documentation](https://duckdb.org/docs/sql/statements/export) for details.

Binary builds are listed below. Feedback is very welcome. Major changes:

SQL
 - #1057: Add PRAGMA for enabling/disabling optimizer & extend output for query graph
 - #1048: Allow CTEs in subqueries (including CTEs themselves) and #987: Allow CTEs in CREATE VIEW statements
 - #1046: Prettify Explain/Query Profiler output
 - #1037: Support FROM clauses in UPDATE statements
 - #1006: STRING_SPLIT and STRING_SPLIT_REGEX SQL functions
 - #1000: Implement MD5 function
 - #936: Add GLOB support to Parquet & CSV readers
 - #899: Table functions information_schema_schemata() and information_schema_tables() and #903: Add table function information_schema_columns()

Engine
 - #984: Parallel grouped aggregations and #1045: Some performance fixes for aggregate hash table
 - #1008: Index Join
 - #991: Local Storage Rework: Per-morsel version info and flush intermediate chunks to the base tables
 - #906: Parallel scanning of single Parquet files and #982: ZSTD Support in Parquet library
 - #883: Unify Table Scans with Table Functions
 - #873: TPC-H Extension
 - #884: Remove NFC-normalization requirement for all data and add COLLATE NFC

Client
 - #1001: Dynamic Syntax Highlighting in Shell
 - #933: Upgrade shell.c to 3330000
 - #918: Add in support for Python datetime types in bindings
 - #950: Support dates and times output into arrow
 - #893: Support for Arrow NULL columns

---

# v0.2.1 - 0.2.1 Preview Release <a id="v021"></a>

*Released on 2020-08-29*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.1)

This is a preview release of DuckDB. Binary builds are listed below. Feedback is very welcome. Major changes:

Engine
 - #770: Enable Inter-Pipeline Parallelism
 - #835: Type system updates with #779: `INTERVAL` Type,  #858: Fixed-precision `DECIMAL` types & #819: `HUGEINT` type
 - #790: Parquet write support

API
 - #866: Initial Arrow support
 - #809: Aggregate UDF support with #843: Generic `CreateAggregateFunction()` & #752: `CreateVectorizedFunction()` using only template parameters

SQL
 - #824: `strftime` and `strptime`
 - #858: `EXPORT DATABASE` and `IMPORT DATABASE`
 - #832: read_csv(_auto) improvements: optional parameters, configurable sample size, line number info

---

# v0.2.0 - 0.2.0 Preview Release <a id="v020"></a>

*Released on 2020-07-23*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.2.0)

This is a preview release of DuckDB. Binary builds are listed below. Feedback is very welcome.

SQL:
 - #730: `FULL OUTER JOIN` Support
 - #732: Support for `NULLS FIRST`/`NULLS LAST`
 - #698: Add implementation of the `LEAST`/`GREATEST` functions
 - #772: Implement `TRIM` function and add optional second parameter to `RTRIM`/`LTRIM`/`TRIM`
 - #771: Extended Regex Options

Clients:
 - Python: #720: Making Pandas optional and add support for PyPy
 - C++: #712: C++ UDF API

---

# v0.1.9 - 0.1.9 Preview Release <a id="v019"></a>

*Released on 2020-06-19*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.9)

This is a preview release of DuckDB. Binary are listed below. Feedback is very welcome. Major changes:
New [website](https://www.duckdb.org) [woo-ho](https://www.youtube.com/watch?v=H9cmPE88a_0)!

Engine
 - #653: Parquet reader integration

SQL
 - #685: Case insensitive binding of column names
 - #662: add `EPOCH_MS` function and test cases

Clients
 - #681: JDBC Read-only mode for and #677 duplicate()` method to allow multiple connections to same database

---

# v0.1.8 - 0.1.8 Preview Release <a id="v018"></a>

*Released on 2020-05-29*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.8)

This is a preview release of DuckDB. Feedback is very welcome.

SQL
 - SQL functions `IF` and `IFNULL` #644
 - SQL string functions `LEFT` #620 and `RIGHT` #631
 - #641: `BLOB` type support
 - #640: `LIKE` escape support

Clients
 - #627: Insertion support for Python relation API

---

# v0.1.7 - 0.1.7 Preview Release <a id="v017"></a>

*Released on 2020-05-04*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.7)

This is the sixth preview release of DuckDB. Feedback is very welcome.
[Binary builds are available as well](http://download.duckdb.org/alias/v0.1.7).

SQL
- [Add / remove columns, change default values & column type](https://www.duckdb.org/docs/current/sql/statements/altertable.html) #612
- [Collation support](https://www.duckdb.org/docs/current/sql/expressions/collations.html)
- CSV sniffer `READ_CSV_AUTO` for dialect, data type and header detection #582
- `SHOW` & `DESCRIBE` Tables #501
- String function `CONTAINS`  #488
- String functions `LPAD` / `RPAD`, `LTRIM` / `RTRIM`, `REPEAT`, `REPLACE` & `UNICODE` #597
- Bit functions `BIT_LENGTH`, `BIT_COUNT`, `BIT_AND`, `BIT_OR`, `BIT_XOR` & `BIT_AGG` #608

Engine
- `LIKE` optimization rules #559
- Adaptive filters in table scans #574
- ICU Extension for extended Collations & Extension Support #594
- Extended zone map support in scans #551
- Disallow NaN/INF in the system #541
- Use UTF Grapheme Cluster Breakers in Reverse and Shell #570

Clients
- Relation API for C++ #509 and Python #598
 - Java (TM) JDBC (R) Client for DuckDB #492 #520 #550

---

# v0.1.6 - 0.1.6 Preview Release <a id="v016"></a>

*Released on 2020-04-05*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.6)

This is the fifth preview release of DuckDB. Feedback is very welcome.
Binary builds can be found here: http://download.duckdb.org/alias/v0.1.6/

SQL
- #455 Table renames `ALTER TABLE tbl RENAME TO tbl2`
- #457 Nested list type can be created using `LIST` aggregation and unpacked with the new `UNNEST` operator
- #463 `INSTR` string function, #477 `PREFIX` string function, #480 `SUFFIX` string function

Engine
- #442 Optimized casting performance to strings
- #444 Variable return types for table-producing functions
- #453 Rework aggregate function interface
- #474 Selection vector rework
- #478 UTF8 NFC normalization of all incoming strings
- #482 Skipping table segments during scan based on min/max indices

Python client
- #451 `date` / `datetime` support
- #467 `description` field for cursor
- #473 Adding `read_only` flag to `connect`
- #481 Rewrite of Python API using `pybind11`

R client
- #468 Support for prepared statements in R client
- #479 Adding automatic CSV to table function `read_csv_duckdb`
- #483 Direct scan operator for R `data.frame` objects

---

# v0.1.5 - 0.1.5 Preview Release <a id="v015"></a>

*Released on 2020-03-02*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.5)

This is the fourth preview release of DuckDB. Feedback is very welcome. Note: The v0.1.4 version was skipped because of a Python packaging issue.

Binary builds can be found here:
http://download.duckdb.org/rev/59f8907b5d89268c158ae1774d77d6314a5c075f/

Major changes:
 - #409 Vector Overhaul
 - #423 Remove individual vector cardinalities
 - #418 `DATE_TRUNC` SQL function
 - #424 `REVERSE` SQL function
 - #416 Support for `SELECT table.* FROM table`
 - #414 STRUCT types in query execution
 - #431 Changed internal string representation
 - #433 Rename internal type `index_t` to `idx_t`
 - #439 Support for temporary structures in read-only mode
 - #440 Builds on Solaris & OpenBSD


*Note*: This release contains a bug in the Python API that leads to crashes when fetching strings to NumPy/Pandas #447

---

# v0.1.3 - 0.1.3 Preview Release <a id="v013"></a>

*Released on 2020-02-03*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.3)

This is the third preview release of DuckDB. Feedback is very welcome.
Binary builds can be found here:
http://download.duckdb.org/rev/59f8907b5d89268c158ae1774d77d6314a5c075f/

Major changes:
  * #388 Major updates to shell
  * #390 Unused Column & Column Lifetime Optimizers
  * #402 String and compound keys in indices/primary keys
  * #406 Adaptive reordering of filter expressions

---

# v0.1.2 - 0.1.2 Preview Release <a id="v012"></a>

*Released on 2020-01-06*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.2)

This is the third preview release of DuckDB. Feedback is very welcome.
Binary builds can be found here:
http://download.duckdb.org/rev/6fcb5ef8e91dcb3c9b2c4ca86dab3b1037446b24/

---

# v0.1.1 - 0.1.1 Preview Release <a id="v011"></a>

*Released on 2019-09-24*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.1)

This is the second preview release of DuckDB. Feedback is very welcome.
Binary builds can be found here:
http://download.duckdb.org/rev/2e51e9bae7699853420851d3d2237f232fc2a9a8/

---

# v0.1.0 - 0.1.0 Preview Release <a id="v010"></a>

*Released on 2019-06-27*

[View on GitHub](https://github.com/duckdb/duckdb/releases/tag/v0.1.0)

This is the first preview release of DuckDB. Feedback is very welcome.

Binary builds can be found here: http://download.duckdb.org/rev/c1cbc9d0b5f98a425bfb7edb5e6c59b5d10550e4/

