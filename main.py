import webapp2
import cgi

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
def valid_month(month):
    for i in months:
        if month.lower() == i.lower():
            return i
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if (day > 0) and (day < 32):
            return day
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if (year > 1900) and (year < 2020):
            return year

def escape_html(s):
    return cgi.escape(s, quote=True)

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month<input type="text" name="month" value="%(month)s"></label>
    <label>Day<input type="text" name="day" value="%(day)s"></label>
    <label>Year<input type="text" name="year" value="%(year)s"></label>
    <div style="color:red;">%(error)s</div>
    <br>
    <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, month="", day="", year="", error=""):
        self.response.out.write(form% {"month": escape_html(month),
                                       "day": escape_html(day),
                                       "year":escape_html(year),
                                       "error": error})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form(user_month, user_day, user_year,"That doesn't look right")
        else:
            self.redirect("/thanks")

class ThanksHandler (webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)
    ], debug=True)
