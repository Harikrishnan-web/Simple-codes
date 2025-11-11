# 1) RAID
RAID stands for **Redundant Array of Independent Disks**. It is a technology where multiple secondary disks are connected together to enhance performance, reliability (data redundancy), or both. The operating system sees the array of disks as a single logical disk. Data is distributed across these disks, and in case of disk failure, parity information can help recover the data.

**Key Features:**
- Set of physical disk drives seen as a single logical disk by the OS.
- Data distributed across the array’s drives.
- Disk failures can be tolerated and recovered using parity/mirroring.

**Types/Levels of RAID:**

- **RAID 0 (Striping):**
  * Splits data into blocks and spreads them across all disks.
  * **No duplication** of data—*if any block/disk fails, data is lost*.
  * Focus: **Performance** (no redundancy).

- **RAID 1 (Mirroring):**
  * All data is duplicated on another disk.
  * Provides **100% redundancy**.
  * Only half of the drive's space is used for actual data—the rest is for the mirror.
  * Focus: **Fault tolerance**—if one disk fails, other contains all data.

- **RAID 2:**
  * Uses **mirroring** and **Error Correcting Codes (ECC)**.
  * Data is striped across different disks, ECC on other disks.
  * Complex and expensive—not commonly used commercially.

- **RAID 3:**
  * **Byte-level striping** with a **dedicated parity disk**.
  * Parity information is stored to recover data if any disk fails.
  * Upon failure, remaining devices and the parity disk reconstruct missing data.

- **RAID 4:**
  * **Block-level striping** with a dedicated parity disk.

- **RAID 5:**
  * Data blocks are written across disks with **distributed parity bits** (parity is not on one single disk).
  * Improves performance and fault tolerance.

- **RAID 6:**
  * Similar to RAID 5 but uses **two independent parity bits**, distributed across disks.
  * Increased fault tolerance (can withstand two disk failures).
  * Requires at least four disks.

**Factors for Choosing RAID Level:**
- Cost of extra disk space.
- Required I/O performance.
- Performance during disk failure.
- Performance during rebuild after a failure.

**Types of RAID Implementation:**

- **Hardware RAID** manages the array independently from the host, presenting a single disk to the OS.
- **Software RAID** is implemented in the kernel disk code, providing a cheaper solution.

**Summary of Benefits:**
RAID improves storage reliability and performance. With suitable redundancy (mirroring/parity, etc.), systems can recover from disk failures seamlessly and improve data read/write speed by accessing multiple disks in parallel.
---
# 2) File Organization

A **file organization** is a method of arranging records in a file when the file is stored on disk. A file is organized logically as a sequence of records; each record is a sequence of fields.

**Types of Records in File Organization:**

- **Fixed Length Record:**
  - Each record is of the same length.
  - If some fields are shorter, they are padded to maintain the correct length.
  - *Advantage*: Fast access because the location of each record is predictable.
  - *Disadvantages*:
    - Larger records may cross block boundaries needing multiple block accesses.
    - Deleting records can create gaps; handling deletion requires complex logic, such as a *free list* in the file header.

- **Variable Length Record:**
  - The length of records can vary due to:
    - Storing multiple record types in one file.
    - Fields that allow variable lengths.
    - Fields with arrays/multisets (repeating).
  - Record representation usually has:
    - An initial fixed part (offset, length for variable-length attributes)
    - Variable data part.
  - *Storage management* uses techniques like slotted page structure where the block header keeps track of record locations and sizes.

**Organization of Records in Files:**

- **Heap File Organization:**
  - Records are placed wherever there is space with no ordering.
  - Suitable for files where insertions are frequent.

- **Sequential File Organization:**
  - Records are stored in order based on search key value.
  - Keeping physical order is difficult when insertions and deletions happen.
  - May use pointer chains for deletions or overflow blocks for insertions.

- **Hashing File Organization:**
  - A hash function determines the storage location for each record.
  - Efficient for direct access to records based on key.

- **Multitable Clustering File Organization:**
  - Records of several different relations stored together in a single file.
  - Useful for join operations.

**Summary of Advantages and Disadvantages:**
- **Fixed length records:** Fast access, but can waste space and complicate deletions.
- **Variable length records:** Space efficient, supports flexible data, but accessing records can be a bit slower.
- **Heap organization:** Fast insertions, unorganized, slow search.
- **Sequential organization:** Fast search for sequential queries, complex to maintain after deletions/insertions.
- **Hash organization:** Very fast search for specific key values, poor at range queries.

---
# 3)Organization of Records in Files
Organization of Records in Files

There are **three commonly used approaches** for organizing records in a file:

1. **Heap File Organization**
   - Any record can be placed wherever there is space in the file. 
   - There is **no ordering** for record placement.
   - Used when insertions are frequent and searching order is not important.

2. **Sequential File Organization**
   - Records are stored in **sequential order based on a search key** (e.g., sorted by RollNo).
   - Inserting or deleting records requires adjusting pointers or adding records to overflow blocks.
   - Maintaining strict physical sequential order is difficult after multiple insertions and deletions.
   - Deletions can be managed using pointer chains.
   - Insertions use free space if present; otherwise, record goes in an overflow block and the pointer chain is updated.

3. **Hashing File Organization**
   - A **hash function** determines the location for each record in the file.
   - Efficient for direct access based on key value, since searching involves applying the hash function.

4. **Multitable Clustering File Organization**
   - Records of several different relations (tables) stored together in a single file.
   - Useful for join operations between tables (e.g., Student and Course records together).
   - Results in variable size records. Pointer chains can be added to track addresses of next records.

**Summary**
- Heap: Fast insertion, unorganized, slower search.
- Sequential: Fast search for sorted queries, complex maintenance for deletions/insertions.
- Hashing: Fast direct search, poor for range queries.
- Multitable clustering: Good for joins, increases record size variability.

Pointer chains and overflow blocks are common strategies to deal with deletion and insertion issues in sequential organization. The choice of organization affects search speed, update efficiency, and storage utilization.
---
# 4) Data Dictionary Storage
Data Dictionary Storage

**Definition:**  
A data dictionary is a *mini database management system* that stores and manages metadata, which is data about the database itself.

**Purpose & Uses:**
- Assists database administrators in managing the database.
- Stores critical information about the database’s structure, design, users, transactions, and usage statistics.
- Controls and documents all aspects of the database.
- Generates reports as needed.

**General Structure:**
- The data dictionary is integrated with database systems.
- Information stored includes:
  - Description of database schema
  - Details of physical design
  - List and roles of database users and their access rights
  - Description of transactions and relationships between transactions and data items
  - Usage statistics (e.g., number of queries, transactions by DBMS)

**Example – Student Database:**
- Fields: RollNo, FirstName, LastName, CourseID
- Data dictionary contains:
  - Column names
  - Data types for each field
  - Description of each column

**Types of Data Dictionaries:**

- **Active Data Dictionary:**
  - Managed automatically by the DBMS.
  - Always consistent with current database structure.
  - Modifications in DBMS are **automatically** reflected in the data dictionary.
  - Usually derived from the system catalog.

- **Passive Data Dictionary:**
  - Used mainly for *documentation purposes*.
  - It is a self-contained application or files set for documenting the database environment.
  - Maintenance and updates are done manually by users.
  - Changes in the database require manual updates in this dictionary.

**Summary:**  
A data dictionary is essential for database management and documentation, maintaining crucial metadata for design, administration, access control, transaction management, and usage monitoring. Active dictionaries are maintained automatically, while passive dictionaries must be updated manually.
---
# 5) Column Oriented Storage
Column Oriented Storage

Column-oriented storage (also called **columnar database management system**) stores data by columns instead of by rows.

**Features and Advantages:**
- Only the required columns for a query are retrieved, leading to efficient query performance and improved disk I/O.
- Data for each column is stored together, allowing more data to be packed into a small amount of memory.
- Efficient for queries that involve operations on columns (such as aggregation in analytics).
- Capable of handling very large amounts of data due to its storage optimization.

**Example:**
- In a row-oriented database, an entire row (all fields) is stored together.
- In column-oriented storage, all values for one column are stored together, followed by another column's values.
- When a query requests only specific columns, the system accesses only those columns, not the full rows.

**Applications:**
- Used in **data analytics**, **business intelligence**, and **data warehousing** where operations often need only a subset of columns.

**Summary:**
Column-oriented storage maximizes efficiency for analytic queries by storing and accessing columns independently, greatly improving performance for data analysis and aggregation tasks.
---
# 6) Indexing and Hashing
Indexing and Hashing

**Indexing:**
- An **index** is a data structure that organizes disk data records for efficient retrieval.
- The **search key** for an index comprises one or more fields used to locate data quickly.
- Indexes speed up search operations but add space and maintenance costs (extra CPU and disk IO during inserts/deletes).

**Types of Indices:**
- **Ordered Indices:** Based on sorted ordering values (e.g., primary indexing, clustering indexing).
- **Hash Indices:** Use a hash function for uniform distribution of values across buckets.

**Ordered Indices:**
- **Primary Index:** Index on fields that include the primary key, stored in sorted order.
- **Clustering Index:** Index on non-primary key columns; records with similar characteristics are grouped.
- **Dense Index:** An index appears for every search key value and holds a pointer to the actual record.
- **Sparse Index:** Index records created for some records; searching may require scanning sequential pointers after locating the closest indexed value.

**Single/Multilevel Indexing:**
- **Single-level Indexing:** Auxiliary file using binary search; can be primary, clustering, or secondary.
- **Multilevel Indexing:** Large indexes are broken into several smaller indices; the top level can reside in memory for faster access.

**Hashing:**
- Uses a **hash function** to determine record location.
- Memory location for records is called a *bucket*, capable of holding multiple records.
- Most often, hash function uses the primary key to generate bucket address.
- **Terms:**
  - Hash Table: Structure storing entries via hash function.
  - Hash Function: Function used to assign/retrieve data by key.
  - Bucket: Storage unit for records in hash structure.
  - Collision: Multiple records yield same address via hash function.
  - Overflow: Inserting new record into a full bucket.
  - Probe: Each hash address calculation and test for existence.
  - Synonym: Keys that hash to same location.

**Hashing Techniques:**
- **Static Hashing:** Fixed number of buckets, bucket address always the same.
- **Dynamic Hashing:** Buckets added/removed as needed (e.g., extendible hashing).

**Static Hashing:**
- Simple to implement and fast but cannot resize buckets with record growth/shrinkage.
- Overflow handled using *overflow pages* or *chains*.

**Dynamic Hashing (Extendible Hashing):**
- Directory of pointers to buckets.
- Upon overflow, bucket splits, redistributes entries, doubles directory size as needed.
- *Global depth* refers to directory bit size, *local depth* to individual bucket bit size.

**Comparison:**
- Ordered indices are better for range queries.
- Hashing is superior for direct search on specific values but poor for range queries.

**Dense vs Sparse Index:**
- **Dense Index:** Best when file not sorted on indexed field, or index file is small.
- **Sparse Index:** Suitable when file sorted; saves space but may require more reads.

**Summary:**
Indexing and hashing speed up data access but use additional space. Ordered indices help with sequential/range queries, while hashing is optimized for direct access. Techniques like dense/sparse indices and static/dynamic hashing manage trade-offs between speed, flexibility, and storage overhead.
---
# 7) Ordered Indices
Ordered Indices – Complete Details

**Definition:**  
Ordered indices are index structures built using the sorted values of one or more fields in a file. They organize and facilitate efficient searching, especially for range and equality queries.

**Types of Ordered Indices:**  
1. **Primary Index:**  
   - An index on a set of fields including the primary key; index file is sorted.
   - Used if the data file is arranged in sorted order by primary key.
   - Binary search can be used for fast lookup.  
   - Number of disk accesses with index: $$ \log_2 n' $$, where $$ n' $$ = blocks in index file.

2. **Clustered/Clustering Index:**  
   - Built on non-primary key columns.
   - Groups together records with similar non-unique fields.
   - File is sorted so that records with matching clustering field values are physically together.
   - Example: Students grouped by semester.

**Dense vs Sparse Indexing:**  
- **Dense Index:**  
  - Contains a record for every search key value, each pointing to the actual record.
  - Used when file not sorted or index is small, for direct access.
- **Sparse Index:**  
  - Contains records only for some search key values (e.g., one per block).
  - Searching involves finding largest search key less than/equal to target, then sequential scan.
  - Saves space, well-suited for files sorted on key.

**Single-Level vs Multilevel Indexing:**  
- **Single-Level:**  
  - Auxiliary file with keys and pointers.
  - Binary search retrieves record addresses.
  - Could be primary, clustering, or secondary.
- **Multilevel:**  
  - Large indices broken into smaller indices.
  - Upper levels reside in memory for fast access.

**Secondary Indices:**  
- Two or more levels used for fields other than the primary key.
- Improves query efficiency for non-key fields.

**Operations and Algorithms:**  
- For searching, binary search is common on ordered index files.
- On inserts/deletes, index and pointers must be updated to maintain sorted order.
- Deletions may require adjustments to pointer chains or overflow blocks.
- Insertions in sequential space; overflow block if no space available.

**Advantages:**  
- Fast searches, especially for range and equality queries.
- Space efficient with sparse indices for sorted data.
- Facilitates sequential and binary search in sorted datasets.

**Disadvantages:**  
- Additional space required for index maintenance.
- Updates (insert/delete) require frequent index modification.

**Dense Index Representation:**  
```plaintext
Index File
-----------
Key   | Pointer
---------------
101   | addr1
104   | addr2
107   | addr3
...   | ...
```
**Sparse Index Representation:**  
```plaintext
Index File (one per block)
-----------
Key   | Pointer
---------------
101   | addr1
110   | addr2
118   | addr3
...   | ...
```

**Primary Index Code Example (conceptual):**
```python
def search_primary_index(index, key):
    # index: list of (key, pointer)
    # binary search for key value
    left, right = 0, len(index)-1
    while left <= right:
        mid = (left + right) // 2
        if index[mid][0] == key:
            return index[mid][1]
        elif index[mid][0] < key:
            left = mid + 1
        else:
            right = mid - 1
    return None  # not found
```

**Clustering Index Example:**
- Records are grouped in data file (e.g., all students by semester).
- Index stores clustering field (semester), pointer to block containing those records.

**Review Questions:**
1. What are ordered indices?
2. Difference between dense and sparse index.
3. Why is dense index preferred in unsorted files?
4. How does B-tree differ from B-tree?

**Summarized Points:**
- Primary/Dense index: record for every key, direct access, used in unsorted files.
- Sparse index: record for some keys, space efficient, used in sorted files.
- Clustered index: groups based on other fields, improves query for group-based retrieval.
- Binary search and sequential scan common in ordered indices.

This covers all conceptual, operational and code-based details for ordered indices.
---
# 8) B+ Tree Index Files
B+ Tree Index Files – Complete Details

**Definition:**
A B+ tree is a balanced, multiway search tree ideal for database indexing. It maintains sorted data, enables efficient insertion, deletion, searching, and especially fast range queries.

**Structure:**
- **Internal Nodes**: Store only keys and child pointers, not actual data.
- **Leaf Nodes**: Store all actual data record pointers and are linked together for easy sequential access.
- All leaves are at the same depth ensuring balance.

**Node Structure:**
- Each node (order n) has up to n pointers and $$ n-1 $$ keys.
- Keys partition the search space, guiding search down correct branches.
- Leaf nodes are linked in a 'sequence set'—enables fast range queries.

**Insertion in B+ Tree:**
1. **Locate correct leaf node** for the key.
2. **Insert key** into leaf. If leaf overflows:
   - *Split leaf* into two, move middle key to parent.
   - *If parent overflows*, split and push up recursively.
   - *Root split* increases tree height.
3. After split, update leaf links for range queries.

**Deletion in B+ Tree:**
1. **Locate leaf node** containing key.
2. **Remove key**.
   - If leaf still half full, done.
   - If underflows, *borrow* from sibling or *merge* nodes.
   - If parent needs updating due to merge, propagate merge up.
   - Root may shrink, lowering tree height.

**Search in B+ Tree:**
1. Start at root.
2. Binary search through node keys.
3. Follow pointer to child until reaching leaf.
4. Search leaf for key.

**Merits**
- Fast search, insertion, deletion—all logarithmic to number of entries.
- Sequential and range queries very fast due to linked leaves.
- Tree always balanced with low height (less disk access).
- All data kept at leaves—internal nodes used for quick navigation.

**Demerits**
- More memory for links and keys compared to binary trees.
- Updating links and pointers on insert/delete can be complex.

**Difference: B+ Tree vs. B-tree**
- In B+ tree, *all data is stored only in leaves*; internal nodes store only keys.
- Leaves are linked for sequential access; not in B-tree.
- Redundant key storage avoided in B+ tree.

**Conceptual Python Example**
```python
class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.pointers = []
        self.leaf = leaf

def search_bplus(root, key):
    node = root
    while not node.leaf:
        for i, item in enumerate(node.keys):
            if key < item:
                node = node.pointers[i]
                break
        else:
            node = node.pointers[-1]
    # Search leaf
    for k in node.keys:
        if k == key:
            return True
    return False
```
*Real implementation needs split/merge logic for insertion/deletion.*

**Applications**
- Used by databases and file systems for large, sorted indexes.
- Especially efficient for range queries (e.g., SELECT ... WHERE id BETWEEN X AND Y).
- Scales with large amounts of data—height stays small, operations remain fast.

**Example**
- *Order 3 B+ tree* (max 2 keys per node): Insert 30, 31, 23, 32, 22, 28, 24, 29, results in splitting nodes and promoting middle keys to parent; tree stays balanced and leaves are sequentially linked.

**Summary**
B+ tree index files are essential for databases requiring efficient, balanced, and scalable storage of sorted and searchable data, supporting both individual lookups and range queries with consistent performance. Every node except root at least half full; changes (insert/delete) handled without losing balance. Leaf node links enable full sequential scan needed in analytic and reporting queries.

---
# 9) B Tree Index Files
B Tree Index Files

**Definition:**  
A B-tree is a balanced multiway search tree used for database indexing. It generalizes binary search trees by allowing nodes with more than two children, keeping tree height small and operations efficient for large datasets.

**Structure:**  
- Each node has up to $$ n-1 $$ search-key values and $$ n $$ pointers (for order $$ n $$).
- Keys within a node are sorted.
- Internal nodes direct search; leaf nodes contain data entries.
- Leaf nodes are often linked sequentially for efficient range queries.

**Properties:**  
- Every node (except root) has at least half-full occupancy.
- Tree stays balanced after insertions and deletions.
- All leaves are at the same depth.

**Insertion Algorithm:**
1. **Find correct leaf $$ L $$ for the key.**
2. **Insert key** into leaf $$ L $$.
   - If $$ L $$ has space: done.
   - If $$ L $$ is full:
     - Split leaf into two, redistribute entries.
     - Move up middle key to parent node.
     - If parent is full, recursively split parent up to root.
3. Root split increases tree height.

**Deletion Algorithm:**
1. **Find leaf $$ L $$ containing the key.**
2. **Remove key.**
   - If $$ L $$ is at least half-full after deletion: done.
   - If not, try to redistribute (borrow from adjacent sibling).
   - If redistribution is not possible, merge with sibling.
   - If parent needs update due to merge, propagate upward.
   - Root may shrink if merge propagates to top.

**Search Algorithm:**
1. Start at root.
2. Binary search keys in current node.
3. If found and at leaf: return.
4. If current node is leaf and not found: failure.
5. Otherwise, follow pointer to child node and repeat.

**Example – B-tree of Order 3 (max 2 keys per node):**
- Insert 20, 10 in ascending order: 
- Insert 30:  (split: 20 goes up)
- Continue insertions, split as needed, propagate keys upward.

**Difference from B+ Tree:**
- B-tree can store duplicates of data/keys in non-leaf nodes.
- Leaf nodes not always linked for fast range queries (may be optionally linked in implementation).
- In B-tree, search keys can appear in non-leaf and leaf nodes; in B+ tree, all data is only in leaves.

**Python-like Conceptual Code:**
```python
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

def search_btree(node, key):
    i = 0
    while i < len(node.keys) and key > node.keys[i]:
        i += 1
    if i < len(node.keys) and key == node.keys[i]:
        return True
    if node.leaf:
        return False
    return search_btree(node.children[i], key)
```
*Real implementation must handle insert, split, delete logic.*

**Merits:**
- Fast search, insertion, deletion, and range queries.
- Tree height remains low, minimizing disk access.
- Supports both random and sequential access.
- Balanced structure; every leaf at same depth.

**Demerits:**
- Extra insertion of non-leaf nodes.
- Space overhead for keys/pointers.

**Summary:**
B-tree index files maintain efficient and balanced structure for large sorted datasets, enabling fast search, insertion, and deletion. The dynamic adjustment of nodes keeps the tree balanced and operations performant. Suitable for database and file system indexing.
---
# 10) B Tree Index Files
B Tree Index Files – All Details

**Definition:**  
A **B-tree** is a balanced, multiway search tree used for indexing in file/database systems. It generalizes binary search trees by allowing nodes with more than two children, keeping the tree height small and search/insertion/deletion operations efficient for large datasets.

**Structure:**
- Each node of order $$ n $$ contains up to $$ n-1 $$ keys (sorted) and $$ n $$ pointers to children.
- Internal nodes partition the search space, guiding traversal to relevant branches.
- Leaf nodes hold actual data entries; often, leaf pages are linked as a sequence set for efficient full scan or range queries.
- Minimum occupancy (except root) is 50% (at least half full).

**Insertion Algorithm:**
1. **Find correct leaf $$ L $$ for the key.**
2. **Insert key into $$ L $$.**
   - If $$ L $$ has space: insert directly.
   - If $$ L $$ is full: split $$ L $$ into two nodes, redistribute entries.
   - When split occurs, promote middle key to parent—if parent is full, recursively split parent up to root.
   - Split in root increases tree height.
3. Update sequence set (linked leaf nodes) if applicable.

**Deletion Algorithm:**
1. **Locate leaf containing key to delete.**
2. **Remove key.**
   - If leaf still at least half full, done.
   - If not, borrow from adjacent sibling or merge nodes, updating parent.
   - Merges/redistribution can propagate up and shrink tree height.

**Search Algorithm:**
1. Start at root.
2. Binary search within current node's keys.
3. If correct key found and at leaf: finished.
4. If key not in leaf: record not present.
5. Otherwise, follow pointer to child node corresponding to search interval and repeat.

**Example (Order 3):**
Insert keys: 20, 10, 30  
Node:   
Split as needed (middle key promoted): root: , leaves: , 

**Characteristics:**
- Tree is always balanced, all leaves at the same level.
- Each node at least half-full (except possibly root).
- Fast operations, logarithmic in number of records.
- Efficient random and sequential access; leaves linked in sequence set.
- Storage overhead for internal node keys and pointers.

**Merits:**
- Small tree height for large datasets (minimized disk access).
- Fast search, insert, delete.
- Efficient full scan/range queries.
- Supports multiple keys compared to binary trees.

**Demerits:**
- Space overhead from extra keys and pointers.
- Complexity for insert/delete and maintaining balance after updates.

**B-tree vs B+ Tree:**
- In B-tree, search-key values can appear in both leaf and non-leaf nodes.
- B+ Tree stores all data entries only in leaves; internal nodes only for navigation.
- Leaves in B+ Tree linked for sequential scans; B-tree linkage optional.

**Conceptual Code Example:**
```python
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

def search_btree(node, key):
    i = 0
    while i < len(node.keys) and key > node.keys[i]:
        i += 1
    if i < len(node.keys) and key == node.keys[i]:
        return True
    if node.leaf:
        return False
    return search_btree(node.children[i], key)
# Real implementation should include insert, split, delete handling.
```

**Review Example (Order 3):**
- Insertion:  → 
- Insert 30: , split as node full, middle (20) goes up.
- Continue: , , , root: 

**Applications:**
- Database indexes, file system directories, and many scenarios requiring efficient, scalable, and reliable sorted data access.

**Summary:**
B-tree index files are a dynamic structure supporting efficient and balanced search, insertion, and deletion for large-scale indexed data. Guarantees good disk performance and balance, stores search keys for fast random/sequential access and minimizes height even with millions of records. Keys and pointers maintained for nodes, leaves have data entries, and all operations (search, insert, delete) keep the B-tree balanced.
---
# 11) Concept of Hashing
Concept of Hashing

**Definition:**  
Hashing is a file organization method in which data is stored at addresses generated by a hash function. The memory location or address is called a bucket; each bucket can store one or more records. Hashing provides direct access using a key—commonly the primary key.

**Basic Terms:**
- **Hash Table:** Data structure for storing/retrieving data quickly using hashing.
- **Hash Function:** Algorithm that computes address from the key (e.g., StudentID mod 10).
- **Bucket:** The storage location for the record, typically a disk block.
- **Collision:** Occurs when two different keys map to the same bucket address.
- **Overflow:** When a bucket is full and needs more space, an additional page is allocated and linked (overflow chain).
- **Probe:** The process of calculating address and checking for existence.
- **Synonym:** Keys that hash to the same bucket.
  
**Example:**  
If you hash student records by age, the age is converted to a number and the last digits are used to locate the data bucket (memory location).

**Advantages:**
- Fast and direct access using a key.
- Simple insertion and search by key value.

**Disadvantages:**
- Not suitable for range queries, as key values are distributed randomly across buckets.
- Collisions and overflow must be managed (detailed overflow management needed).

**Collision Resolution:**
- **Separate Chaining:** Linked list for each bucket.
- **Open Addressing (Linear Probing):** Next available bucket used if collision occurs.
- **Overflow Pages:** Additional pages allocated for extra data.

**Static Hashing:**  
Fixed number of buckets; hash function always yields the same address.
- Simple, fast
- Cannot easily expand/shrink as the database size changes
- Overflow managed via overflow pages or chains

**Dynamic Hashing (Extendible Hashing):**
- Buckets can be added or removed dynamically, depending on data size.
- Directory of pointers to buckets; if bucket overflows, directory is expanded (bit size increases).
- Splitting and redistributing contents occurs automatically in case of overflow.

**Static vs Dynamic Hashing**
- **Static** hashing is fixed-size, simple to implement but inefficient when data grows/shrinks or for ordered access.
- **Dynamic** hashing automatically expands/contracts, more flexible and efficient for growing databases.

**Review Points:**
- Hash function must distribute records uniformly to reduce overflow.
- Hashing is best for equality queries and direct value lookup, not for range queries.
- Hashing techniques: Static hashing and dynamic hashing (extendible hashing).

**Summary:**
Hashing enables efficient, direct record access using a key, but requires careful collision/overflow management and is not efficient for range queries. Dynamic hashing methods overcome limitations of static structures by growing/shrinking with data size.
---
# 12) Static Hashing
