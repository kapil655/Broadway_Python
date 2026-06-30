class Course:
    course_name = "Python"
    ins_name = "Sudan"
    duration = "1 hour"

    def show_course_details(self):
        return f'''Course: {self.course_name}
        instructor: {self.ins_name}
        duration: {self.duration}'''


class OnlineCourse(Course):
    platform_name = "Google Meet"
    course_link = "jkslfjd.kljdlfds"

    def show_platform_details(self):
        return f'''Platform_name: {self.platform_name}
          Course_Link: {self.course_link}'''

class PaidOnlineCourse(OnlineCourse):
    price = 124
    payment_status = "Completed"

    def show_payment_detail(self):
        return f'''Price: {self.price}
         Payment Status: {self.payment_status}'''


paid_obj = PaidOnlineCourse()
print(paid_obj.show_course_details())
print(paid_obj.show_platform_details())
print(paid_obj.show_payment_detail())