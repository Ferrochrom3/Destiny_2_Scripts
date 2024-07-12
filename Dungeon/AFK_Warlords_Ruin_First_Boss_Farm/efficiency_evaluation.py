import time

total_failed_attempts = 0
total_success_attempts = 0
consecutive_failed_attempts = 0


def display_status(start_time: float):
    if total_success_attempts + total_failed_attempts == 0:
        return

    total_attempts = total_success_attempts + total_failed_attempts
    success_rate = round((total_success_attempts / total_attempts) * 100, 2)
    average_time_per_attempt = round((time.time() - start_time) / total_attempts)
    average_time_per_success = round((time.time() - start_time) / total_success_attempts, 2) if total_success_attempts > 0 else 0

    print(
        f"Status: "
        f"\nTotal Attempts: {total_attempts}"
        f"\nFailed Attempts - {total_failed_attempts}"
        f"\nSuccess Attempts - {total_success_attempts}"
        f"\nSuccess Rate - {success_rate}%"
        f"\nAverage Time Per Attempt - {average_time_per_attempt}s"
        f"\nAverage Time Per Success - {average_time_per_success}s"
    )
