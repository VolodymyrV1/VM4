from pathlib import Path


def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            total_salary = []
            for line in lines:
                total_salary.append(float(line.split(',')[1].strip()))
                total = sum(total_salary)
                total_lines = len(total_salary)
                average = total / total_lines
            return total, average

    except FileNotFoundError:
        print("Didn't find txt file!")

    except Exception as e:
        print(f'{e} with file')


total, average = total_salary("/Users/volodymyr/Desktop/VM4/EX_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

