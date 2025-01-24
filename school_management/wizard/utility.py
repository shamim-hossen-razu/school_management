def create_styled_table(student_results):
    header_style = "background-color: #f2f2f2; font-weight: bold;"
    row_style = "background-color: #ffffff;"

    table = "<table border='1' style='border-collapse: collapse; width: 100%; padding-top: 10px;'>"
    table += f"<tr style='{header_style}'>"
    table += "<th>Course ID Name</th>"
    table += "<th>Grade</th>"
    table += "<th>Marks</th>"
    table += "<th>Result Date</th>"
    table += "</tr>"
    if student_results:
        for result in student_results:
            table += f"<tr style='{row_style}'>"
            table += f"<td>{result['course_name']}</td>"
            table += f"<td>{result['grade']}</td>"
            table += f"<td>{result['marks']}</td>"
            table += f"<td>{result['result_date']}</td>"
            table += "</tr>"
    table += "</table>"
    return table

