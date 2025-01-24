from odoo import api, fields, models, _


class StudentExcelReportWizard(models.TransientModel):
    _name = 'student.excel.report.wizard'
    _description = 'Student Excel Report Wizard'
    _rec_name = 'display_name'

    student_id = fields.Many2one('school_management.student', string='Student')
    preview = fields.Html(string='HTML Content', readonly=True)

    def student_report(self):
        student_results = self.prepare_student_result() or "Nothing to show"
        table = "<table border='1'>"
        table += "<tr>"
        table += "<th>course id Name</th>"
        table += "<th>grade</th>"
        table += "<th>marks</th>"
        table += "<th>result_date</th>"
        table += "</tr>"
        if student_results:
            for result in student_results:
                table += "<tr>"
                table += f"<td>{result['course_id']}</td>"
                table += f"<td>{result['grade']}</td>"
                table += f"<td>{result['marks']}</td>"
                table += f"<td>{result['result_date']}</td>"
                table += "</tr>"
        table += "</table>"
        self.write({
            'preview': table
        })



    def student_report_pdf(self):
        pass

    def student_report_excel(self):
        pass

    def prepare_student_result(self):
        if self.student_id:
            student = self.student_id
            sql = f"""
            SELECT * FROM school_management_student as student
            INNER JOIN school_management_result as result
            ON student.id = result.student_id 
            WHERE student.id = {student.id}"""

            self.env.cr.execute(sql)
            result = self.env.cr.dictfetchall()
            return result
