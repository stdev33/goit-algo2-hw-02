from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing queue based on priorities and printer constraints.

    Args:
        print_jobs: List of print jobs (dict format).
        constraints: Printer constraints.

    Returns:
        Dict containing optimized print order and total print time.
    """
    # Convert input jobs to a list of PrintJob objects
    jobs = [PrintJob(**job) for job in print_jobs]

    # Sort jobs by priority (ascending order, highest priority first)
    jobs.sort(key=lambda job: job.priority)

    print_order = []
    total_time = 0
    queue = []

    current_volume = 0
    current_batch_time = 0

    for job in jobs:
        # Check if the job can fit in the current batch
        if len(queue) < constraints["max_items"] and (current_volume + job.volume) <= constraints["max_volume"]:
            queue.append(job)
            current_volume += job.volume
            current_batch_time = max(current_batch_time, job.print_time)
        else:
            # Process current batch
            print_order.extend([job.id for job in queue])
            total_time += current_batch_time

            # Start a new batch
            queue = [job]
            current_volume = job.volume
            current_batch_time = job.print_time

    # Process the last batch if there are remaining jobs
    if queue:
        print_order.extend([job.id for job in queue])
        total_time += current_batch_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Test cases
def test_printing_optimization():
    # Test 1: All jobs have the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Test 2: Jobs with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # Lab work
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # Diploma work
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # Personal project
    ]

    # Test 3: Jobs exceeding printer limits
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (Same Priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print Order: {result1['print_order']}")
    print(f"Total Time: {result1['total_time']} minutes")

    print("\nTest 2 (Different Priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print Order: {result2['print_order']}")
    print(f"Total Time: {result2['total_time']} minutes")

    print("\nTest 3 (Exceeding Constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print Order: {result3['print_order']}")
    print(f"Total Time: {result3['total_time']} minutes")

if __name__ == "__main__":
    test_printing_optimization()
