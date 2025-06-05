import threading
import time

def countdown(thread_name):
    print(f"[{thread_name}] Поток начал работу")
    for i in range(10, 0, -1):
        print(f"[{thread_name}] {i}")
        time.sleep(1)
    print(f"[{thread_name}] Поток завершил работу")

# Создаем и запускаем два потока
thread1 = threading.Thread(target=countdown, args=("Поток 1",))
thread2 = threading.Thread(target=countdown, args=("Поток 2",))

print("Запускаем потоки...")
thread1.start()
thread2.start()

# Ждем завершения обоих потоков
thread1.join()
thread2.join()
print("\nОба потока завершили выполнение")
