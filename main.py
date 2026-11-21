# main.py

# ایمپورت کردن پکیج Student
import Student

def main():
    # ۱. دریافت نام کاربر
    name = input("Enter student name: ")
    
    # ۲. دریافت لیست نمرات از کاربر
    # برای سادگی، از کاربر می‌خواهیم نمرات را با فاصله وارد کند
    grades_input = input("Enter grades separated by space: ")
    
    # تبدیل رشته ورودی به لیست اعداد (float)
    grades_list = [float(x) for x in grades_input.split()]
    
    # ۳. فراخوانی توابع
    avg = Student.calculate_avg(grades_list)
    max_grade = Student.find_max(grades_list)
    min_grade = Student.find_min(grades_list)
    status = Student.check_status(avg)
    
    # چاپ خروجی دقیقا مشابه وایت‌برد
    print("\n" + "-"*20)
    print(f"Student: {name}")
    print(f"Avg = {avg}")
    print(f"max = {max_grade}")
    print(f"min = {min_grade}") # این خط در وایت‌برد نبود، ولی چون تابعش رو خواسته بود اضافه کردم
    print(f"status = {status}")
    print("-"*20)

if __name__ == "__main__":
    main()