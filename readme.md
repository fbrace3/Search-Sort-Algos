Search & Sort Algorithms in Python

A collection of classic searching and sorting algorithms implemented in Python with performance comparisons and benchmarking tools.

This project explores algorithm efficiency, runtime analysis, and implementation differences between multiple sorting strategies.

**Update 3/14/2026**
    I Will be adding additional algorithms as I work through them

    Floyds added on 4/14/2026


Algorithms Included
Sorting Algorithms

    Bubble Sort	Simple comparison-based sorting algorithm	O(n²)
    Merge Sort (2-way)	Divide and conquer merge sort	O(n log n)
    Merge Sort (3-way)	Variation of merge sort using three partitions	O(n log n)
    Quick Sort (First Pivot)	Quick sort using first element as pivot	O(n log n) average
    Quick Sort (Middle Pivot)	Quick sort using middle element as pivot	O(n log n) average

Searching Algorithms 

    Linear Search	Sequential search through the list	O(n)
    Binary Search	Efficient search on sorted lists	O(log n)

Project Structure

Search-Sort-Algos
│
├── SortVariations.py      # Sorting algorithms + runtime comparison
├── SearchVariations.py    # Searching algorithms
├── README.md
└── requirements.txt
Features

Multiple sorting algorithm implementations

Runtime comparison between algorithms

Automatic validation that sorted outputs match

Interactive CLI for selecting algorithms

Random dataset generation for testing

Example Output
Sorting Algorithm Comparison
Fastest: Merge 2 Way — 0.000031s

Algorithm       | Time (s)   | Δ from fastest (s)
---------------------------------------------------
Merge 2 Way     | 0.000031   | 0.000000
Quick Sort M    | 0.000042   | 0.000011
Quick Sort F    | 0.000048   | 0.000017
Merge 3 Way     | 0.000061   | 0.000030
Bubble Sort     | 0.003210   | 0.003179

Installation

Clone the repository:

git clone https://github.com/fbrace3/Search-Sort-Algos.git
cd Search-Sort-Algos

Install dependencies:

pip install -r requirements.txt
Running the Program

Run the sorting comparison tool:

python SortVariations.py

You will be prompted to select which algorithm to run.

Example Code Usage

You can import algorithms directly into other Python scripts.

from SortVariations import bubbleSort

nums = [5, 2, 9, 1, 3]

sorted_nums, runtime, label = bubbleSort(nums)

print(sorted_nums)
print(runtime)
Learning Goals

This project explores:

Algorithm design and analysis

Runtime complexity

Divide-and-conquer strategies

Performance benchmarking

Python implementation patterns

Future Improvements

Planned additions include:

Binary search implementation

Linear search implementation

Visualization of sorting algorithms

Runtime graphs using matplotlib

Larger dataset benchmarks

Algorithm complexity comparisons

Author

Fred Brace

Computer Science Graduate
Denver, Colorado

Interested in:

Software Engineering

Algorithms & Data Structures

Machine Learning

Python Development

License

This project is open source and available under the MIT License.
